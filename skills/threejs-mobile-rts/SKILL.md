---
name: threejs-mobile-rts
description: >-
  Engineering standard and operational pipeline for Three.js WebGL2 RTS rendering on mobile phones (393x852)
  and desktop (1440x900). Covers draw-call budgets, instancing, LOD hierarchies, KTX2/Basis Universal texture
  compression, chunked heightfield terrain with splat shaders, mobile shadow topologies, iOS Safari Jetsam memory
  guardrails, gltf-transform/meshopt asset pipeline, spatial picking at scale, and touch RTS camera UX.
---

# Three.js / WebGL2 Mobile RTS Rendering Standard

This skill establishes the engineering benchmarks, architectural rules, memory ceilings, and operational optimization pipelines for high-performance RTS rendering in Three.js and WebGL2. It targets sustained 60 FPS (or rock-solid 30 FPS deterministic lockstep visual sync) across modern handhelds (baseline: **393x852** viewport, 3x DPR e.g. iPhone 14/15/16) and desktop displays (baseline: **1440x900**, 1x–2x DPR).

---

## 1. Hardware Benchmarks & Performance Budgets

Handheld web browsers—specifically WebKit / iOS Safari—operate under draconian thermal throttling and hard memory caps enforced by OS watchdogs (iOS `Jetsam`). Exceeding WebGL canvas memory will abruptly terminate the tab with zero catchable JavaScript exceptions.

### Table 1.1: Platform Target Budgets

| Metric | Mobile Target (393x852 @ 3x DPR) | Desktop Target (1440x900 @ 1x/2x DPR) | Critical Failure Limit (Mobile) |
| :--- | :--- | :--- | :--- |
| **Max Canvas Render Buffer** | $1179 \times 768$ (clamp `dpr` $\le 1.5$–$2.0$) | $1440 \times 900$ (or native $2880 \times 1800$ @ 2x) | Native 3x DPR ($1179 \times 2556 = 3.01\text{M}$ px) |
| **Target Frame Rate** | 60 FPS ($16.6\text{ms}$) or locked 30 FPS ($33.3\text{ms}$) | 60 FPS ($16.6\text{ms}$) | $< 24\text{ FPS}$ sustained (thermal throttle) |
| **Frame Time Budget (CPU)** | $\le 8.0\text{ ms}$ (Sim: $3.0\text{ms}$, Render prep: $5.0\text{ms}$) | $\le 10.0\text{ ms}$ | $> 16.0\text{ ms}$ |
| **Frame Time Budget (GPU)** | $\le 7.0\text{ ms}$ | $\le 6.0\text{ ms}$ | $> 14.0\text{ ms}$ |
| **Draw Calls / Frame** | **$\le 45$** (Hard ceiling: $60$) | **$\le 150$** (Ceiling: $250$) | $> 80$ calls (WebGL overhead collapse) |
| **Active Visible Triangles** | $50\text{k} - 90\text{k}$ | $200\text{k} - 450\text{k}$ | $> 150\text{k}$ triangles on mobile |
| **Shadow Map Budget** | Single directional cascade: $1024 \times 1024$ PCF | 2-3 cascades or single $2048 \times 2048$ PCFSoft | $\ge 2048 \times 2048$ with multi-cast on mobile |
| **Total VRAM Footprint** | $\le 160\text{ MB}$ (Safe margin under Jetsam) | $\le 750\text{ MB}$ | $> 280\text{ MB}$ (iOS Safari Jetsam OOM kill) |
| **Texture Format** | KTX2 / Basis Universal (UASTC / ETC1S) | KTX2 / WebP / BC7 | Uncompressed PNG/JPEG decoded to RGBA8 |
| **Shader Switches** | $\le 6$ material programmes per frame | $\le 20$ material programmes per frame | $> 15$ pipeline switches |

---

## 2. Geometric Complexity & Asset LOD Caps

All units, structures, and props must strictly conform to the 3-tier Level of Detail (LOD) envelope. Models exceeding caps will fail asset pipeline ingestion.

### Table 2.1: Triangle & Texture Ceilings by Class

```
+-------------------+----------------+----------------+----------------+---------------------+
| ASSET CLASS       | LOD0 (Hero/Near)| LOD1 (Mid Field| LOD2 (Far/Macro)| TEXTURE RESOLUTION  |
|                   | < 35m Camera   | 35m - 90m      | > 90m Dist     | LOD0 / LOD1 / LOD2  |
+-------------------+----------------+----------------+----------------+---------------------+
| Buildings / Base  | 6,000 tris     | 2,500 tris     | 800 tris       | 2048 / 1024 / 512   |
| Vehicles / Tanks  | 8,000 tris     | 3,000 tris     | 1,000 tris     | 2048 / 1024 / 512   |
| Aircraft & Ships  | 15,000 tris    | 5,000 tris     | 1,500 tris     | 2048 / 1024 / 512   |
| Infantry Squads   | 3,000 tris     | 1,200 tris     | 400 tris       | 1024 / 512 / 256    |
| Nature / Props    | 1,200 tris     | 400 tris       | 80 tris        | 512 / 256 / 128     |
+-------------------+----------------+----------------+----------------+---------------------+
```

### Hysteresis and LOD Transition Dynamics
To prevent visual popping and thrashing at LOD boundaries:
1. **Hysteresis Band:** An asset switching from LOD0 $\rightarrow$ LOD1 at distance $D_0 = 35\text{m}$ must not switch back from LOD1 $\rightarrow$ LOD0 until distance drops below $D_0 - \Delta D$ where $\Delta D = 4.0\text{m}$.
2. **Screen-Space Error (SSE):** For variable camera tilts, calculate LOD by projected pixel footprint:
   $$\text{Coverage}_{\text{px}} = \frac{R_{\text{bounding\_sphere}} \cdot H_{\text{viewport}}}{D \cdot 2 \tan\left(\frac{\text{FOV}}{2}\right)}$$
   - $\text{Coverage}_{\text{px}} > 120\text{ px} \implies \text{LOD0}$
   - $40\text{ px} \le \text{Coverage}_{\text{px}} \le 120\text{ px} \implies \text{LOD1}$
   - $\text{Coverage}_{\text{px}} < 40\text{ px} \implies \text{LOD2}$

---

## 3. Core Mobile Techniques

### 3.1 Instancing Hierarchy (`THREE.InstancedMesh`)
Never spawn individual `THREE.Mesh` instances for repetitive RTS entities (projectiles, trees, rocks, infantry squads, debris, treads).
- **Static Scenery:** Consolidate props into a single `THREE.InstancedMesh` per archetype with precomputed bounding spheres. Disable `matrixAutoUpdate` and call `computeBoundingSphere()` once.
- **Dynamic Units:** For homogenous vehicle batches (e.g., T-72 tanks, marine riflemen), utilize `THREE.InstancedMesh` with a dynamic instance buffer:
  ```typescript
  instancedMesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
  ```
  Pass per-instance state (health bar ratio, player tint, selection bitmask) via custom `InstancedBufferAttribute` vectors rather than duplicating draw calls or using individual uniforms.
- **Draw Call Impact:** Reduces 1,500 tree draw calls $\rightarrow$ **1 draw call**.

### 3.2 Texture Compression: KTX2 / Basis Universal
Mobile GPUs (Apple Apple Silicon / ARM Mali / Qualcomm Adreno) do not sample PNG or JPEG directly; the browser decodes them into uncompressed 32-bit RGBA8888 arrays in VRAM.
- A single $2048 \times 2048$ PNG ($1.2\text{ MB}$ disk) expands to:
  $$2048 \times 2048 \times 4\text{ bytes} \times 1.333\text{ (mipmaps)} = \mathbf{22.37\text{ MB VRAM}}$$
  Ten such textures consume $224\text{ MB}$, triggering an immediate iOS Jetsam crash.
- **KTX2 / ASTC / ETC1S Solution:**
  - Standard maps (albedo, normal, roughness-metalness-AO packed): compress to **ASTC 4x4 or 6x6** on mobile ($4\text{ bits/pixel}$ or $2.67\text{ bits/pixel}$).
  - A $2048 \times 2048$ ASTC texture occupies **$2.8\text{ MB VRAM}$** (8x reduction).
  - Deploy Basis Universal UASTC for high-detail normal maps and ETC1S for diffuse/albedo maps where low bitrate is prioritized.

### 3.3 Terrain Heightfield Chunking & Splat Shading
Avoid single monolithic geometry planes for heightfields (e.g. $256 \times 256$ vertices).
- **Chunk Partitioning:** Divide map into grid chunks of $16 \times 16$ or $32 \times 32$ cells.
- **Frustum Culling:** Enable chunk-level bounding sphere frustum culling. At $52^\circ$ RTS pitch, camera viewports only intersect $25\% - 40\%$ of the map tiles.
- **Splat Texturing:**
  - Never use multi-pass material blending.
  - Employ a single custom `MeshStandardMaterial.onBeforeCompile` or raw shader reading a 4-channel Splat Map (RGBA weights for Grass, Dirt, Rock, Sand).
  - Use texture arrays (`sampler2DArray`) in WebGL2 to eliminate texture unit binding limits and bind all terrain biomes in a single slot.

### 3.4 Mobile Shadow Topology
Directional shadows are the #1 GPU fillrate and vertex bottleneck on mobile WebGL2.
- **Tightly Fitted Orthographic Frustum:**
  - Never set shadow camera bounds to map extents (e.g. $[-W/2, W/2]$). This wastes $95\%$ of shadow texels outside the viewport.
  - Calculate the intersection of the camera frustum with the ground plane ($Y = 0 \dots Y_{\text{max}}$). Fit the `directionalLight.shadow.camera` tightly to this bounding box every frame or camera move.
- **Resolution & Filtering:**
  - Mobile: Max $1024 \times 1024$, `THREE.PCFShadowMap`. Avoid `PCFSoftShadowMap` (requires 16 texture taps per fragment).
  - Infantry & Small Missiles: Disable `castShadow`. Render planar billboard blob shadows or decal projectors onto the terrain.
  - Cull shadow casters behind the camera that do not cast into the visible frustum.

### 3.5 Frame Pacing & Memory Hygiene (iOS Safari Jetsam Mitigation)
- **Decoupled Simulation & Free-Running Render:**
  - Run deterministic logic at $30\text{ Hz}$ or $20\text{ Hz}$ via fixed accumulation loop:
    ```typescript
    while (accumulator >= stepDuration) { sim.step(); accumulator -= stepDuration; }
    ```
  - Render via `requestAnimationFrame` with transform interpolation between sim ticks.
  - Cap `Math.min(dt, 0.1)` to avoid the "spiral of death" when tab resumes from background.
- **Garbage Collection (GC) Elimination:**
  - Zero allocation in the render loop. Pre-allocate all working `Vector3`, `Matrix4`, `Box3`, and `Raycaster` instances.
  - Never instantiate inline arrays, anonymous closures, or object literals during `render()`.
- **Context Loss Recovery:**
  - Listen for `webglcontextlost` and prevent default. Dispose all GPU resources, pause simulation, and wait for `webglcontextrestored`.

### 3.6 Raycasting and Spatial Picking at Scale
Calling `raycaster.intersectObjects(scene.children, true)` against complex GLTF hierarchies or dense terrain meshes destroys frame times ($> 25\text{ ms}$ on mobile).
- **Two-Tier Picking Architecture:**
  1. **Units:** Perform 2D circle/capsule tests in simulation coordinate space (screen point $\rightarrow$ ground plane ray $\rightarrow$ 2D spatial hash grid). Only test units within $5\text{m}$ of the ground ray.
  2. **Terrain:** If raycasting against heightfields is required, use a 2D Digital Differential Analyzer (DDA) grid march across the heightmap array, testing only the 2 triangles of the intersected cell. Do not raycast BufferGeometry triangles directly.

### 3.7 RTS Camera UX Architecture
- **Orientation:** Fixed tilt pitch $\theta \in [50^\circ, 55^\circ]$, fixed azimuth (top-down isometric style). Disable free orbit rotation to minimize disorientation and preserve shadow cascade stability.
- **Touch Gestures:**
  - Single-finger drag: Pan ground position with inertia damping.
  - Two-finger pinch: Exponential zoom along optical axis with min/max distance clamping ($20\text{m} - 120\text{m}$).
  - Tap / Double-tap: Select unit / select all matching units on screen.
  - Drag-box: Touch-and-hold (250ms threshold) or explicit UI marquee mode button.
- **Ground Projection:**
  - Pan calculations must intersect rays with the mathematical plane $Y = Y_{\text{average\_terrain}}$ to ensure constant linear dragging velocity regardless of camera tilt.

---

## 4. Automated GLB Optimization Pipeline

Incoming raw GLBs from artists or external CAD repositories are typically bloated with unindexed vertices, duplicate materials, multi-megabyte embedded PNGs, and excessive node transforms.

### The Standard Optimization Sequence
Execute this gltf-transform recipe on every candidate GLB before committing to the asset pipeline:

```bash
# 1. Deduplicate & weld shared vertices within 0.0005m threshold
npx @gltf-transform/cli weld input.glb temp1.glb --tolerance 0.0005

# 2. Prune unused nodes, accessors, materials, and animations
npx @gltf-transform/cli prune temp1.glb temp2.glb

# 3. Consolidate duplicate textures and materials
npx @gltf-transform/cli dedup temp2.glb temp3.glb

# 4. Generate LODs (LOD1 at 40% ratio, LOD2 at 15% ratio)
# (Using gltf-transform simplify or meshoptimizer)
npx @gltf-transform/cli simplify temp3.glb lod1.glb --ratio 0.40 --error 0.001
npx @gltf-transform/cli simplify temp3.glb lod2.glb --ratio 0.15 --error 0.005

# 5. Compress textures to KTX2 (Basis Universal UASTC / ETC1S)
npx @gltf-transform/cli etc1s temp3.glb lod0_compressed.glb --quality 150
# Or for high-fidelity normal maps:
npx @gltf-transform/cli uastc temp3.glb lod0_uastc.glb --level 2 --zstd 18

# 6. Apply Meshopt geometry compression
npx @gltf-transform/cli meshopt lod0_compressed.glb final_lod0.glb
```

### Draco vs. Meshopt Decoder Benchmark (Mobile Runtime)
- **Draco:** Higher compression ratio on disk, but heavy CPU/WASM decompression spikes on mobile. Decoding 10 Draco meshes stalls the main JavaScript thread for $120\text{ms} - 350\text{ms}$, causing visible frame stutter during unit spawning.
- **Meshopt (`EXT_meshopt_compression`):** Decompresses at over $1.0\text{ GB/sec}$ via lightweight SIMD/WASM. **Meshopt is the mandatory standard for runtime streaming.**

---

## 5. Performance Profiling Procedure

Follow this deterministic sequence when evaluating or profiling an RTS scene:

### Step 1: Render Statistics Baseline
Extract active GPU counters via Three.js internal metrics:
```typescript
console.table({
  drawCalls: renderer.info.render.calls,
  triangles: renderer.info.render.triangles,
  geometries: renderer.info.memory.geometries,
  textures: renderer.info.memory.textures,
});
```

### Step 2: CPU vs. GPU Bottleneck Identification
1. Open Chrome DevTools $\rightarrow$ **Performance** panel (or Safari Web Inspector $\rightarrow$ Timelines).
2. Set CPU Throttling to **4x slowdown** (simulates midrange mobile ARM core).
3. Record 5 seconds of active combat (moving 40 units, issuing attack orders).
4. Analyze `Main` thread flame chart:
   - If `renderer.render()` consumes $> 10\text{ ms}$: Inspect Three.js scene graph matrix updates (`scene.updateMatrixWorld()`) and shader uniform uploads.
   - If Garbage Collection `Major GC` or `Minor GC` spikes occur: Scan for object allocations in `tick()` or event handlers.
5. GPU Fillrate Test: Resize browser canvas to $25\%$ dimensions ($0.25 \times$ width/height). If frame rate jumps significantly, the bottleneck is fragment shading/shadow map overdraw.

### Step 3: WebGL State Inspection via Spector.js
1. Capture a single frame using **Spector.js** extension.
2. Inspect the command stream:
   - Identify redundant `gl.useProgram` calls (materials not sharing program cache).
   - Verify that shadow pass draw calls do not exceed visible shadow casters.
   - Check texture upload sizes and verify mipmap generation is performed offline, not on the main thread during gameplay.

---

## 6. PR Review Audit Checklist

Engine and asset PRs must satisfy every check before merge:

- [ ] **Draw Call Budget:** Total frame draw calls $\le 45$ (mobile) / $\le 150$ (desktop).
- [ ] **Instancing:** Scenery props, infantry units, and particle systems utilize `THREE.InstancedMesh`.
- [ ] **Geometry Caps:**
  - [ ] Buildings $\le 6,000$ (LOD0), $\le 2,500$ (LOD1), $\le 800$ (LOD2).
  - [ ] Vehicles $\le 8,000$ (LOD0), $\le 3,000$ (LOD1), $\le 1,000$ (LOD2).
  - [ ] Aircraft/Ships $\le 15,000$ (LOD0), $\le 5,000$ (LOD1), $\le 1,500$ (LOD2).
- [ ] **Texture Caps:** Max $2048 \times 2048$ for hero units/terrain, $1024 \times 1024$ for standard vehicles, $512 \times 512$ for props.
- [ ] **Texture Compression:** Compressed via KTX2/Basis or WebP; no raw uncompressed 4K PNGs.
- [ ] **Memory Ceiling:** Total scene VRAM $\le 160\text{ MB}$; verified safe against iOS Safari Jetsam.
- [ ] **Shadow Optimization:** Single directional shadow map $\le 1024 \times 1024$ on mobile; shadow frustum tightly clamped to visible camera volume.
- [ ] **Terrain Chunking:** Terrain partitioned into frustum-culled chunks; no full-mesh raycasting.
- [ ] **Zero Per-Frame Allocations:** No `new THREE.Vector3()`, `new THREE.Matrix4()`, or object allocations inside `requestAnimationFrame` or `sim.step()`.
- [ ] **Picking Architecture:** Units picked via spatial 2D collision or bounding proxy cylinders; terrain picked via DDA heightfield math or low-poly proxy.
