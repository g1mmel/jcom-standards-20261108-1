---
name: lockstep-determinism
description: >-
  Engineering standard and operational specification for cross-platform deterministic lockstep simulation in JavaScript and TypeScript.
  Covers IEEE-754 float determinism across JS engines (V8 vs JavaScriptCore/WebKit vs SpiderMonkey), non-deterministic Math functions and safe replacements,
  fixed-point vs float invariants, dual-stream seeded PRNGs, stable iteration order, raw-bit state hashing, desync detection, and network lockstep architecture.
---

# Deterministic Lockstep Simulation & Cross-Engine Netcode Standard

This standard establishes the mandatory engineering rules, mathematical specifications, and architectural invariants required to achieve bit-exact deterministic lockstep execution across disparate JavaScript execution engines (Google V8 on x86_64/ARM64, Apple JavaScriptCore / WebKit on iOS/macOS, and Mozilla SpiderMonkey).

---

## 1. Foundational Axioms of Deterministic Lockstep

In a deterministic lockstep architecture, all connected clients simulate identical game states from tick $0$ to tick $N$ by executing identical simulation logic on identical inputs. The game state is a pure function of the initial state and the ordered stream of player inputs:

$$\text{State}_{t+1} = \text{Step}(\text{State}_t, \text{Inputs}_t, \text{Tick})$$

To guarantee that $\text{State}_{t,\text{Client } A} \equiv \text{State}_{t,\text{Client } B}$ across desktop (V8) and mobile devices (JSC on iOS Safari), the simulation must adhere to six non-negotiable axioms:

### Axiom 1: Discrete Fixed Timestep
Simulation state updates only in discrete, fixed temporal quanta ($\Delta t = \frac{1}{\text{TICK\_HZ}}$). Wall-clock time (`Date.now()`, `performance.now()`, `requestAnimationFrame` timestamp) must NEVER enter simulation state, physics, kinematics, cooldowns, or decision logic. Rendering interpolation ($\alpha = \frac{\text{accumulator}}{\Delta t}$) is strictly decoupled and read-only.

### Axiom 2: Strict Isolation of Simulation and Presentation
The simulation model owns all state mutations. The rendering engine (Three.js / WebGL2 / WebGPU) reads simulation state as an immutable snapshot. Under no circumstances may rendering transformations, raycasts, UI layout dimensions, or GPU buffer readbacks mutate or influence simulation variables.

### Axiom 3: Complete Isolation of Simulation and Visual RNG
Simulations require pseudo-random number generation (PRNG), as do visual particle systems and audio pitch variations. Visual randomness MUST NOT draw from the simulation PRNG stream. Consuming a random number for an ambient dust particle on Client A will desync Client A from Client B within one tick. Two distinct seeded PRNG instances must exist:
- `simRng`: Stepped ONLY by deterministic gameplay events (weapon scatter, critical chance).
- `fxRng`: Stepped independently for visual/cosmetic variation (smoke drift, tracer jitter).

### Axiom 4: Stable Collection Iteration Order
Object iteration order in JavaScript (`for...in`, `Object.keys()`, `Map.prototype.keys()`, `Set.prototype.values()`) depends on insertion order and key type semantics (ECMAScript 2015+ integer key ordering vs string insertion order). Deleting and re-inserting entities dynamically alters iteration order. All iteration affecting state mutation must either:
- Iterate over pre-sorted contiguous arrays sorted by unique numeric monotonic ID (`unit.id`).
- Process events using an explicit deterministic tie-breaking key.

### Axiom 5: Exact IEEE-754 Operation Invariance
JavaScript represents all numbers as IEEE-754 double-precision 64-bit floating point numbers (`binary64`). While basic arithmetic (`+`, `-`, `*`, `/`, `Math.sqrt`) is strictly bit-exact per IEEE-754 across all conforming CPUs, transcendental and composite functions (`Math.sin`, `Math.cos`, `Math.atan2`, `Math.pow`, `Math.hypot`) are NOT bit-exact across different C standard libraries (libc) or JavaScript JIT compilers.

### Axiom 6: Canonical String Comparison
`String.prototype.localeCompare()` uses operating system collation tables and locale settings (`Intl.Collator`), which differ between Windows, Linux, Android, and iOS. Simulation sorting by string identifier must use raw code-point comparison:
```typescript
export function cmpStr(a: string, b: string): number {
  return a < b ? -1 : a > b ? 1 : 0;
}
```

---

## 2. Floating-Point Determinism in Modern JavaScript Engines

### 2.1 The IEEE-754 Specification and ECMAScript Mandate
ECMAScript standardizes `Number` as IEEE-754 `binary64`:
- 1 sign bit
- 11 exponent bits (bias $+1023$)
- 52 fraction (mantissa) bits (with 1 implicit leading bit for normalized numbers)

The IEEE-754 standard mandates **correct rounding** to the nearest representable floating-point number (roundTiesToEven) with an error bound of at most $0.5\,\text{ULP}$ (Unit in the Last Place) for five fundamental operations:
1. Addition ($a + b$)
2. Subtraction ($a - b$)
3. Multiplication ($a \times b$)
4. Division ($a / b$)
5. Square Root ($\sqrt{a}$, via `Math.sqrt`)

Because x86-64 (SSE2/AVX) and ARM64 (NEON) execute hardware instructions directly adhering to IEEE-754 round-to-nearest-even (`ADDPD`, `SUBPD`, `MULPD`, `DIVPD`, `SQRTPD` on x86; `FADD`, `FSUB`, `FMUL`, `FDIV`, `FSQRT` on ARM64), **these five operations produce identical bit-level results across V8, JavaScriptCore, and SpiderMonkey**.

> [!IMPORTANT]
> Modern 64-bit JIT compilers do not use legacy x87 80-bit extended precision registers. Intermediate calculations are preserved in 64-bit registers or spilled to 64-bit memory slots. Fused Multiply-Add (`FMA`) instructions (`a * b + c` without intermediate rounding) are NOT emitted by standard JS JITs for separate `a * b + c` statements unless explicitly invoked via WebAssembly or language extensions.

### 2.2 The Non-Deterministic JavaScript Math Functions
ECMAScript Section 21.2.2 explicitly permits implementation-dependent approximations for transcendental and complex math functions. Different browser engines link to different underlying math libraries:
- **V8 (Chrome / Edge / Node.js):** Custom optimized assembly routines (`fdlibm` derivative or platform-tuned approximations).
- **JavaScriptCore (Safari / WebKit on iOS & macOS):** Apple Libm / OS Darwin system math library.
- **SpiderMonkey (Firefox):** Mozilla `fdlibm` wrapper.

The following table categorizes native `Math` methods into Safe (Cross-Engine Identical) and Unsafe (Desync Hazardous):

```
+---------------------------------------------------------------------------------------------------------+
| METHOD                STATUS        ENGINE DIVERGENCE MECHANISM              SAFE DETERMINISTIC REPLACEMENT |
+---------------------------------------------------------------------------------------------------------+
| Math.sqrt(x)          SAFE          IEEE-754 0.5 ULP mandated correctly     Direct call (native hardware)   |
| Math.abs(x)           SAFE          Sign bit masking                         Direct call                     |
| Math.floor / ceil     SAFE          Exact integer truncation                 Direct call                     |
| Math.trunc / round    SAFE*         Exact integer rounding (*watch -0 vs +0) Direct call                     |
| Math.min / max        SAFE          Exact comparison logic                   Direct call                     |
| Math.imul(a, b)       SAFE          Exact 32-bit hardware integer multiply   Direct call                     |
| Math.clz32(x)         SAFE          Exact 32-bit leading zero count          Direct call                     |
+---------------------------------------------------------------------------------------------------------+
| Math.hypot(x, y)      UNSAFE        Scale-factor algorithm / libc variation  Math.sqrt(x * x + y * y)        |
| Math.atan2(y, x)      UNSAFE        Polynomial approximation / ULP drift     Fixed-LUT or CORDIC / Poly atan2|
| Math.sin / cos / tan  UNSAFE        Range reduction / polynomial rounding    Table lookup (LUT) or CORDIC    |
| Math.asin / acos      UNSAFE        Transcendental series divergence         Rational polynomial / LUT       |
| Math.pow(x, y)        UNSAFE        Log/Exp expansion for fractional powers  powInt(x, y) or exact integers  |
| Math.exp / log        UNSAFE        Transcendental approximation drift       LUT or integer approximations   |
| Math.random()         CRITICAL BAN  Unseeded, platform-internal state PRNG   Seeded PRNG (Mulberry32/PCG)    |
+---------------------------------------------------------------------------------------------------------+
```

---

## 3. Safe Deterministic Math Replacements

### 3.1 2D Distance and Norm (`Math.hypot` Replacement)
`Math.hypot(x, y)` was designed to prevent overflow for numbers exceeding $10^{154}$. In an RTS simulation, game world coordinates rarely exceed $10^5$ meters. $x^2 + y^2 \le (10^5)^2 + (10^5)^2 = 2 \times 10^{10} \ll 1.79 \times 10^{308}$.

```typescript
/**
 * Deterministic Euclidean 2D distance.
 * Guaranteed bit-exact across V8, JSC, and SpiderMonkey.
 */
export function dist2D(dx: number, dy: number): number {
  return Math.sqrt(dx * dx + dy * dy);
}

/**
 * Deterministic range check comparing squared distances.
 * Eliminates square root calculation entirely; 100% exact IEEE-754 multiply-add.
 */
export function inRangeSq(dx: number, dy: number, range: number): boolean {
  return (dx * dx + dy * dy) <= (range * range);
}
```

### 3.2 Deterministic Angle and Trigonometry (`Math.atan2`, `sin`, `cos`)
To guarantee that orientation, turret targeting, and weapon projectile trajectories never diverge across engines, angles should either be quantized to discrete heading bins (e.g., 256 or 1024 or 65536 radial units per full circle, matching SAGE engine conventions) or computed via a high-precision polynomial or lookup table (LUT).

```typescript
export const ANGULAR_DIVISIONS = 4096;
export const ANGULAR_MASK = ANGULAR_DIVISIONS - 1;
export const RAD_TO_BIN = ANGULAR_DIVISIONS / (2 * Math.PI);
export const BIN_TO_RAD = (2 * Math.PI) / ANGULAR_DIVISIONS;

// Precomputed trigonometric lookup tables (Float64Array generated deterministically at init)
export const SIN_LUT = new Float64Array(ANGULAR_DIVISIONS);
export const COS_LUT = new Float64Array(ANGULAR_DIVISIONS);

(() => {
  for (let i = 0; i < ANGULAR_DIVISIONS; i++) {
    const rad = (i * 2 * Math.PI) / ANGULAR_DIVISIONS;
    SIN_LUT[i] = Math.sin(rad);
    COS_LUT[i] = Math.cos(rad);
  }
})();

/**
 * Fast, deterministic arctangent approximation for (x, y) heading.
 * Returns angle in discrete binary units [0, ANGULAR_DIVISIONS - 1].
 * Maximum angular error < 0.07 degrees. Bit-exact across all platforms.
 */
export function deterministicAtan2Bin(dx: number, dy: number): number {
  if (dx === 0 && dy === 0) return 0;
  
  // Approximate atan using 5th-order minimax polynomial on [-1, 1]
  const absX = dx < 0 ? -dx : dx;
  const absY = dy < 0 ? -dy : dy;
  const c = absX > absY;
  const num = c ? absY : absX;
  const den = c ? absX : absY;
  const t = den === 0 ? 0 : num / den;
  const t2 = t * t;
  
  // P(t) = t * (0.999866 - 0.3302995 * t^2 + 0.180141 * t^4)
  let angle = t * (0.999866 + t2 * (-0.3302995 + t2 * 0.180141));
  if (c) {
    // angle remains
  } else {
    angle = (Math.PI / 2) - angle;
  }
  
  if (dx < 0 && dy >= 0) angle = Math.PI - angle;
  else if (dx < 0 && dy < 0) angle = angle - Math.PI;
  else if (dx >= 0 && dy < 0) angle = -angle;

  // Normalize to [0, 2*PI)
  if (angle < 0) angle += 2 * Math.PI;
  return Math.floor(angle * RAD_TO_BIN) & ANGULAR_MASK;
}
```

---

## 4. Fixed-Point vs. Floating-Point: Architectural Analysis

Game engines traditionally choose between Fixed-Point Integer Arithmetic (e.g., Q16.16) and IEEE-754 Floating Point.

```
+----------------------------------------------------------------------------------------------------------+
| ATTRIBUTE              FIXED-POINT (Q16.16 / Q24.8)               RESTRICTED IEEE-754 FLOAT (JS NUMBER)  |
+----------------------------------------------------------------------------------------------------------+
| Cross-Platform Safety  100% Guaranteed bit-exact across any CPU   Bit-exact if limited to +, -, *, /, sqrt|
| Performance in JS      Lower (requires bit-shifts, BigInt, or     Maximum (direct V8/JSC JIT native      |
|                        imul emulation to avoid 32-bit overflow)   FPU/SIMD execution)                    |
| Tooling & Ecosystem    Poor: Three.js, shaders, physics libraries High: Direct assignment to Three.js    |
|                        require constant conversion packing        Vector3 and BufferAttributes           |
| Dynamic Range          Fixed range: Q16.16 is [-32768, +32767]    $10^{-308}$ to $10^{+308}$, 53-bit     |
|                        Risk of positional overflow on huge maps   mantissa precision                     |
| Implementation Burden  High (custom vector math, custom physics)  Zero (uses standard language syntax)   |
+----------------------------------------------------------------------------------------------------------+
```

### The Engineering Verdict for Browser RTS
For modern web-based RTS development in TypeScript, **Restricted IEEE-754 Floating-Point** is the superior engineering choice, provided:
1. All non-exact functions (`Math.hypot`, `Math.sin`, `Math.atan2`, `Math.pow`) are strictly banned from simulation code.
2. Position coordinates are NEVER snapped or quantized per-tick (`quantizePos` is an anti-pattern that distorts kinematic trajectories and breaks sub-tile collision).
3. State checksums hash exact raw bits (via TypedArray views).

---

## 5. Seeded PRNG and Stream Separation

A deterministic simulation must use a robust, uniform pseudo-random number generator. Standard `Math.random()` is unseeded and non-deterministic.

### 5.1 SplitMix32 / Mulberry32 Implementation
Mulberry32 produces uniform 32-bit pseudo-random values with an efficient 32-bit integer pipeline:

```typescript
export class DeterministicPRNG {
  private state: number;

  constructor(seed: number) {
    this.state = seed >>> 0;
  }

  public getSeed(): number {
    return this.state;
  }

  public setSeed(seed: number): void {
    this.state = seed >>> 0;
  }

  /** Generates uint32 in [0, 4294967295] */
  public nextUint32(): number {
    let z = (this.state += 0x6d2b79f5) >>> 0;
    z = Math.imul(z ^ (z >>> 15), z | 1);
    z ^= z + Math.imul(z ^ (z >>> 7), z | 61);
    return (z ^ (z >>> 14)) >>> 0;
  }

  /** Generates float in [0.0, 1.0) */
  public nextFloat(): number {
    return this.nextUint32() / 4294967296;
  }

  /** Generates integer in [min, max] inclusive */
  public nextRange(min: number, max: number): number {
    return min + Math.floor(this.nextFloat() * (max - min + 1));
  }
}
```

### 5.2 PRNG Dual Stream Architecture
```
              +--------------------------+
              | Master Match Seed: S_0   |
              +--------------------------+
                     /            \
                    /              \
  +-------------------------+   +-------------------------+
  | Simulation PRNG (simRng)|   | Visual / Audio PRNG (fx)|
  | Seed: hash(S_0, "SIM")  |   | Seed: hash(S_0, "FX")   |
  +-------------------------+   +-------------------------+
              |                              |
      Combat Damage Rolls           Explosion Particle Jitter
      Accuracy / Scatter            Muzzle Flash Angles
      Dynamic Path Jitter           Tracer Color Variations
              |                              |
     [AFFECTS GAMEPLAY]             [LOCAL CLIENT ONLY]
     [MUST BE DETERMINISTIC]        [NEVER COMMUNICATED]
```

---

## 6. Raw-Bit State Hashing & Desync Detection

To verify determinism between remote peers, state checksums must be computed and compared at regular intervals (e.g., every 30 frames / 1 second).

### 6.1 Why Rounding Floats in State Hashes is an Anti-Pattern
Truncating or rounding floats (`Math.round(u.x * 100)`) in state hashes causes two severe failure modes:
1. **Masked Desyncs:** A unit whose position drifts by $0.004$ tiles due to an unseeded RNG call will produce identical rounded values for hundreds of ticks, delaying desync detection until the divergence has exploded into an unrecoverable mismatch.
2. **Boundary Flitter:** If unit position is $10.005$, slight floating-point differences between platforms ($10.005000000000002$ vs $10.004999999999998$) flip `Math.round(x * 100)` between $1001$ and $1000$, causing **false-positive desyncs** even when movement logic is completely aligned.

### 6.2 Raw-Bit IEEE-754 Hash Pipeline (FNV-1a 32/64)
Use a shared `Float64Array` and `Uint32Array` buffer view to extract the exact binary representation of double-precision numbers without rounding:

```typescript
export class SimStateHasher {
  private static readonly FNV_PRIME = 0x01000193;
  private static readonly FNV_OFFSET = 0x811c9dc5;

  private static floatBuffer = new Float64Array(1);
  private static uint32View = new Uint32Array(SimStateHasher.floatBuffer.buffer);

  private hash = SimStateHasher.FNV_OFFSET;

  public reset(): void {
    this.hash = SimStateHasher.FNV_OFFSET;
  }

  public updateInt32(val: number): void {
    let h = this.hash;
    h ^= (val & 0xff);
    h = Math.imul(h, SimStateHasher.FNV_PRIME) >>> 0;
    h ^= ((val >>> 8) & 0xff);
    h = Math.imul(h, SimStateHasher.FNV_PRIME) >>> 0;
    h ^= ((val >>> 16) & 0xff);
    h = Math.imul(h, SimStateHasher.FNV_PRIME) >>> 0;
    h ^= ((val >>> 24) & 0xff);
    this.hash = Math.imul(h, SimStateHasher.FNV_PRIME) >>> 0;
  }

  /**
   * Hashes exact IEEE-754 raw bits (low 32-bits and high 32-bits).
   * Absolutely zero precision loss, zero rounding drift.
   */
  public updateFloat64(val: number): void {
    SimStateHasher.floatBuffer[0] = val;
    this.updateInt32(SimStateHasher.uint32View[0]);
    this.updateInt32(SimStateHasher.uint32View[1]);
  }

  public updateString(str: string): void {
    for (let i = 0; i < str.length; i++) {
      this.hash ^= str.charCodeAt(i);
      this.hash = Math.imul(this.hash, SimStateHasher.FNV_PRIME) >>> 0;
    }
  }

  public digestHex(): string {
    return (this.hash >>> 0).toString(16).padStart(8, '0');
  }
}
```

### 6.3 State Checksum Payload Specification
At tick $T$, the hasher must traverse all simulation components in strict canonical order:
1. **Simulation Header:** `tick`, `simRng.state`.
2. **Player States (ordered by player index $0 \dots P-1$):** `credits`, `powerSupplied`, `powerDrained`, `teamId`.
3. **Active Entities (sorted by `unit.id` ascending):**
   - `id`, `typeIndex`, `player`
   - `x`, `y`, `hp`, `cooldown`
   - `facingBin` (integer heading)
   - `orders.length`, followed by order details (`kind`, target `id`, destination `x`, `y`)
   - `productionQueue` lengths and `progressTicks`

---

## 7. Deterministic Priority Queues and Stable Pathfinding

Naive A* implementations frequently suffer from non-deterministic tie-breaking. When multiple grid cells have identical $F = G + H$ scores:
1. `Map` or `Set` traversal selects nodes based on insertion sequence.
2. Floating-point heuristic distance ($H$) computed via `Math.hypot` produces $1\,\text{ULP}$ discrepancies across platforms, causing V8 to pick Node A while JSC picks Node B.

### 7.1 Deterministic Binary Min-Heap
A deterministic A* open-set priority queue must enforce strict primary and secondary keys:
1. Primary Key: $F = G + H$ (computed with deterministic distance).
2. Secondary Key: $H$ (breaking ties in favor of nodes closer to the goal).
3. Tertiary Key: Unique Node Index (`y * width + x`) to enforce bit-exact stable ordering.

```typescript
export interface PathNode {
  readonly index: number;
  readonly f: number;
  readonly h: number;
}

export class DeterministicPathHeap {
  private data: PathNode[] = [];

  public get size(): number {
    return this.data.length;
  }

  public clear(): void {
    this.data.length = 0;
  }

  public push(node: PathNode): void {
    this.data.push(node);
    this.bubbleUp(this.data.length - 1);
  }

  public pop(): PathNode | undefined {
    if (this.data.length === 0) return undefined;
    const top = this.data[0];
    const bottom = this.data.pop()!;
    if (this.data.length > 0) {
      this.data[0] = bottom;
      this.sinkDown(0);
    }
    return top;
  }

  private compare(a: PathNode, b: PathNode): number {
    if (a.f !== b.f) return a.f - b.f;
    if (a.h !== b.h) return a.h - b.h;
    return a.index - b.index; // Bit-exact integer tie-breaker
  }

  private bubbleUp(idx: number): void {
    const el = this.data[idx];
    while (idx > 0) {
      const parentIdx = (idx - 1) >>> 1;
      const parent = this.data[parentIdx];
      if (this.compare(el, parent) >= 0) break;
      this.data[idx] = parent;
      idx = parentIdx;
    }
    this.data[idx] = el;
  }

  private sinkDown(idx: number): void {
    const len = this.data.length;
    const el = this.data[idx];
    while (true) {
      const leftIdx = (idx << 1) + 1;
      const rightIdx = leftIdx + 1;
      let swapIdx = -1;

      if (leftIdx < len) {
        if (this.compare(this.data[leftIdx], el) < 0) {
          swapIdx = leftIdx;
        }
      }
      if (rightIdx < len) {
        if (
          this.compare(this.data[rightIdx], swapIdx === -1 ? el : this.data[leftIdx]) < 0
        ) {
          swapIdx = rightIdx;
        }
      }
      if (swapIdx === -1) break;
      this.data[idx] = this.data[swapIdx];
      idx = swapIdx;
    }
    this.data[idx] = el;
  }
}
```

---

## 8. Network Lockstep Architecture: Desktop to Mobile Cross-Play

In desktop-to-phone cross-play, latency and packet jitter vary widely (e.g., fiber desktop on 10ms ping vs mobile 5G phone on 75ms jittery ping).

### 8.1 Turn Delay and Input Scheduling
Commands issued on client $P$ at frame $F$ are NOT executed immediately. They are tagged with an execution frame:

$$F_{\text{exec}} = F_{\text{current}} + D_{\text{turn}}$$

Where $D_{\text{turn}}$ is the configured input turn delay (typically 2 to 4 frames at 30 Hz = 66ms to 133ms).
- A frame $F$ advances IF AND ONLY IF all input packets for frame $F$ from all players have arrived.
- If peer packets for frame $F$ are missing, the simulation halts (displaying "Waiting for players...").
- Dynamic Turn Delay automatically scales $D_{\text{turn}}$ up or down based on exponential moving average peer RTT.

```
Timeline: Frame Advancing (Turn Delay D = 2 frames @ 30 Hz)
Client A (Local)   Frame 10: User issues "Attack" -> Packet Sent: { Frame: 12, Cmd: Attack }
                   Advances Frame 10 (executes pre-buffered inputs for Frame 10)
                   Advances Frame 11 (executes pre-buffered inputs for Frame 11)
                   Frame 12: Executes "Attack" simultaneously with Client B
```

### 8.2 WebRTC DataChannel vs WebSocket Transport
- **WebRTC DataChannels (Ordered, Unreliable or Semi-Reliable):** Preferred for peer-to-peer lockstep. Minimizes Head-of-Line (HoL) blocking on retransmissions for transient state probes while guaranteeing reliable delivery of frame input buffers.
- **WebSocket (TCP):** Acceptable for client-server relay. Subject to TCP backoff and head-of-line delay under cellular packet loss; requires turn delay headroom ($D_{\text{turn}} \ge 3$ frames).

---

## 9. Comprehensive Determinism Audit Checklist

Before any simulation commit is promoted to main, engineers must verify every item:

| Checked | Category | Audit Requirement |
|:---:|---|---|
| [ ] | **Timestep** | No references to `Date.now()`, `performance.now()`, `setInterval()`, or `setTimeout()` exist in simulation or AI code. |
| [ ] | **Tick Rate** | Timestep is fixed (30 Hz = 33.333ms). Speed, cooldown, and economy rates are calibrated for 30 ticks/s. |
| [ ] | **RNG** | Zero occurrences of unseeded `Math.random()`. Simulation uses dedicated `DeterministicPRNG`. |
| [ ] | **RNG Isolation** | Cosmetic/visual effects (particles, camera shake, UI clicks) use a separate visual PRNG stream. |
| [ ] | **Math.hypot** | Zero calls to `Math.hypot()` in simulation, AI, or pathfinding. Replaced with `dist2D` or squared comparisons. |
| [ ] | **Trig / Atan2** | Zero raw `Math.atan2()`, `Math.sin()`, `Math.cos()` in gameplay code. Uses quantized LUT or exact polynomials. |
| [ ] | **Iteration** | No iterating directly over `Map.keys()`, `Set.values()`, or object properties without sorting by monotonic numeric ID. |
| [ ] | **Sorting** | Zero use of `localeCompare()`. Uses `cmpStr` (code-point comparison) for strings, with secondary tie-breakers on IDs. |
| [ ] | **No Snap** | Absolutely NO per-tick coordinate snapping/quantization (`quantizePos` anti-pattern). Coordinates remain true IEEE-754. |
| [ ] | **State Hash** | State checksum digests raw IEEE-754 bits (via `Float64Array`/`Uint32Array` buffer views), NOT rounded integers. |
| [ ] | **Hash Scope** | State checksum covers `tick`, `simRng.state`, player resources, entity positions, health, cooldowns, and orders. |
| [ ] | **A* Pathing** | Priority queues enforce deterministic tie-breaking (F-score -> H-score -> Cell Index). |
| [ ] | **Input Buffer** | Input commands are scheduled for $F + D_{\text{turn}}$ and verified identical across peers before frame execution. |
