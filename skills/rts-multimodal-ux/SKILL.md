---
name: rts-multimodal-ux
description: >-
  Authoritative engineering standard and interaction specification for browser-based RTS input across desktop mouse/keyboard,
  iPad (capacitive touch, Magic Keyboard/trackpad, Apple Pencil), iPhone (landscape/portrait 393x852), and Gamepad (Xbox/PS/Steam Deck).
  Covers the InputAction abstraction layer, gesture recognizers (dwell-and-drag marquee, multi-touch pinch/twist),
  WebKit/Safari hostility hardening, 2-step building confirmation, +48pt ghost occlusion offsets, magnetic snap hulls,
  tactile Web Audio ticks, and responsive HUD rules for the 5 GUI styles (zh, cnc3, ra3, jslc, minimal).
---

# RTS Multimodal Input & UX Engineering Standard

This skill governs the multimodal input architecture, gesture disambiguation, hardware modality detection, and responsive HUD engineering for real-time strategy engines running in modern web browsers (TypeScript + Three.js WebGL2). It establishes rigorous, non-negotiable rules for translating high-tempo desktop RTS mechanics to capacitive glass, styluses, trackpads, and controllers.

---

## 1. Architectural Core: The Decoupled `InputAction` Layer

Raw hardware input events (`PointerEvent`, `KeyboardEvent`, `WheelEvent`, Gamepad API) **MUST NEVER** directly mutate simulation state or trigger simulation orders. All user input traverses a 4-stage pipeline:

```
[Physical Ingestion] ──▶ [Defensive Hostility Shield] ──▶ [Gesture / Normalization] ──▶ [InputAction Intent]
                                                                                               │
                                    ┌──────────────────────────────────────────────────────────┴────────┐
                                    ▼                                                                   ▼
                     [Client Immediate Feedback <50ms]                                    [Deterministic Sim Core 30Hz]
```

### 1.1 The Canonical `InputAction` Contract
All client interactions must map into a discrete `InputAction` variant:

```typescript
export type SelectionModifier = 'replace' | 'add' | 'toggle';
export type OrderKind = 'move' | 'attack' | 'attackMove' | 'guard' | 'stop' | 'scatter' | 'deploy';

export type InputAction =
  // Camera Navigation
  | { type: 'CAMERA_PAN'; deltaX: number; deltaZ: number; source: 'drag' | 'keys' | 'stick' | 'edge' }
  | { type: 'CAMERA_ZOOM'; factor: number; focalPoint?: { x: number; y: number } }
  | { type: 'CAMERA_ROTATE'; angleDelta: number }
  | { type: 'CAMERA_JUMP'; targetWorld: { x: number; z: number } }
  | { type: 'CAMERA_RESET' }
  | { type: 'CAMERA_JUMP_ALERT' }
  
  // Selection
  | { type: 'SELECT_POINT'; screenX: number; screenY: number; modifier: SelectionModifier; device: string }
  | { type: 'SELECT_BOX'; startX: number; startY: number; endX: number; endY: number; modifier: 'replace' | 'add' }
  | { type: 'SELECT_TYPE'; unitType: string; frustumOnly: boolean }
  | { type: 'SELECT_ALL_COMBAT' }
  | { type: 'SELECT_GROUP'; groupIndex: number; centerCamera: boolean }
  | { type: 'SET_GROUP'; groupIndex: number }
  | { type: 'CLEAR_SELECTION' }
  
  // Tactical Orders
  | { type: 'ORDER_ISSUE'; kind: OrderKind; targetWorld?: { x: number; z: number }; targetUnitId?: number; queue: boolean }
  | { type: 'ORDER_STOP' }
  | { type: 'ORDER_SCATTER' }
  | { type: 'ORDER_STANCE'; stance: 'aggressive' | 'guard' | 'holdGround' }
  | { type: 'ORDER_ABILITY'; abilityId: string; targetWorld?: { x: number; z: number }; targetUnitId?: number }
  
  // Base Building & Production
  | { type: 'PROD_QUEUE'; producerId: number; unitType: string; count: number }
  | { type: 'PROD_CANCEL'; producerId: number; queueIndex: number }
  | { type: 'BUILD_START'; structureType: string; builderId?: number }
  | { type: 'BUILD_UPDATE_GHOST'; tileX: number; tileY: number; facing: number; valid: boolean }
  | { type: 'BUILD_CONFIRM' }
  | { type: 'BUILD_CANCEL' }
  
  // HUD / Meta
  | { type: 'UI_MINIMAP_NAV'; tileX: number; tileY: number; button: number }
  | { type: 'UI_STYLE_CYCLE' }
  | { type: 'UI_PAUSE_TOGGLE' };
```

---

## 2. Hardware Modality & Ingestion Guidelines

1. **Unified Pointer Events:** Always listen on `pointerdown`, `pointermove`, `pointerup`, `pointercancel`. Never bind redundant legacy `touchstart` or `mousedown` listeners.
2. **Inspect `e.pointerType`:**
   - `'mouse'`: Enforce standard desktop RTS rules (Right-Click context orders, Left-Click select/marquee, edge pan, precision 24pt hitboxes).
   - `'touch'`: Enforce touch RTS rules (kinetic 1-finger pan, 180ms dwell marquee, double-tap type select, 44–52pt targets, magnetic snap).
   - `'pen'` (Apple Pencil / Stylus): Activate hover reticles (`pointerover` prior to contact), sub-pixel selection, barrel double-tap tool toggling.
3. **Gamepad Polling:** Poll `navigator.getGamepads()` at 60Hz. Apply a minimum $0.15$ radial deadzone on both analog sticks with quadratic sensitivity curves. Right Trigger opens an 8-way Radial Command Wheel (C&C CommandStick). Holding the A button expands a Halo Wars-style selection brush.

---

## 3. Gestural Disambiguation & The "Pan vs. Select" Rule

The fatal trap of mobile RTS design is ambiguous single-finger dragging. The engine **MUST** enforce the following disambiguation state machine:

- **Instant Single-Finger Drag ($v > 0.1\text{ px/ms}$ within $80\text{ms}$):** Immediate **Camera Ground Pan** with kinetic inertia. It must *never* draw an accidental selection box.
- **Stationary Dwell ($\ge 180\text{ms}$ motionless contact):** Triggers a haptic/audio tick and transitions into **Marquee Box Select Mode**. Subsequent dragging draws the selection rectangle.
- **Single Tap ($< 250\text{ms}$, $< 8\text{px}$ drift):**
  - If units are selected: Issues contextual order (Move or Attack).
  - If no units are selected: Selects unit under tap (evaluating 28pt magnetic snap hull).
- **Double Tap ($\le 300\text{ms}$ interval):** Selects **all visible friendly units of matching archetype** in the active camera frustum.
- **Two-Finger Pinch:** Exponential camera zoom along optical axis ($18\text{m} \le Z \le 120\text{m}$).
- **Two-Finger Twist:** Rotates camera azimuth $\phi$ (snapping to cardinal angles).
- **ADZA (Adaptive Dual-Zone Anchor):** On multi-touch tablets, anchor pointer ($v < 35\text{ px/s}$) + drag pointer ($>3.0\times$ velocity) directly pulls a dynamic marquee box.
- **Persistent Selection Lock (The Torch Protocol):** Tapping open ground while units are selected issues a formation movement order without clearing selection. Selection is explicitly cleared via an unhidden `[UNSELECT UNITS]` split-button on the HUD, `Escape` key, or Gamepad `B` button.
- **Expanding Selection Bubble (Louis Castle Invariant):** Holding Gamepad `A` button or Touch long-press smoothly expands a circular selection radius ($R \in [24\text{ px}, 180\text{ px}]$ over $600\text{ms}$).


---

## 4. Precision Aids: Touch Hitboxes, Occlusion & Confirmation

1. **Decoupled Touch Picking Capsules:**
   - Visual triangle meshes project to tiny screen areas. The engine must test raycasts against expanded collision capsules scaled to **$2.5\times - 3.5\times$** the geometric bounding sphere (minimum $R \ge 24\text{ pt}$).
2. **2D Screen-Space Target Magnetism:**
   - Any tap landing within $R = 28\text{ pt}$ of an enemy unit locks an attack order onto that enemy, displaying animated red target brackets. Raw ground move orders are issued only when the query circle is empty.
3. **Finger Occlusion Offset (+48 pt Y):**
   - When placing buildings, ghost reticles, or target beacons on touchscreens, offset the preview **$+48\text{ pt}$ vertically above the touch coordinate**. The user's thumb pad must never block the placement validation cells.
4. **Two-Step Stamp Confirmation:**
   - Never drop buildings or superweapons on a single touch-down. Releasing the drag anchors the ghost; execution requires tapping the floating **[✓ Confirm]** badge or **[✗ Cancel]** badge.

---

## 5. Web Platform Hostility Hardening (Safari & Chrome)

To prevent browser UI gestures from destroying game micro, the following shields are mandatory:

```css
/* Universal Defensive Shield */
html, body {
  width: 100%;
  height: 100%;
  height: 100dvh; /* Prevents URL bar resizing jumps */
  margin: 0;
  padding: 0;
  overflow: hidden;
  position: fixed;
  background-color: #000;
  
  touch-action: none;
  overscroll-behavior: none;
  -webkit-overscroll-behavior: none;
  user-select: none;
  -webkit-user-select: none;
  -webkit-touch-callout: none;
  -webkit-tap-highlight-color: transparent;
}

#app canvas {
  width: 100%;
  height: 100%;
  display: block;
  touch-action: none;
}

/* DOM Overlay Event Trapping */
#hud-layer, .hud-root {
  position: absolute;
  inset: 0;
  pointer-events: none; /* Allows 3D WebGL canvas clicks underneath */
  z-index: 20;
}
.interactive-panel, .cameo-slot, .drawer-button, button, a {
  pointer-events: auto; /* Restores touch/click strictly on UI buttons */
}
```

```typescript
// JavaScript Hostility Shield & Tactical Keyboard Guard
window.addEventListener('contextmenu', (e) => e.preventDefault(), { passive: false });
window.addEventListener('gesturestart', (e) => e.preventDefault(), { passive: false });
window.addEventListener('gesturechange', (e) => e.preventDefault(), { passive: false });
window.addEventListener('gestureend', (e) => e.preventDefault(), { passive: false });

// Quarantines dangerous browser shortcuts during competitive play
const QUARANTINED_KEYS = new Set(['w', 't', 'r', 'a', 's', 'p']);
window.addEventListener('keydown', (e) => {
  if ((e.ctrlKey || e.metaKey) && QUARANTINED_KEYS.has(e.key.toLowerCase())) e.preventDefault();
  if (e.key === 'F5') e.preventDefault();
}, { capture: true, passive: false });
```

```html
<!-- Viewport Meta -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no, viewport-fit=cover">
```

---

## 6. Ergonomics, Thumb Zones & Safe Area Insets

1. **Safe Area Inset Clearance:**
   - All HUD roots must pad against hardware notches and home indicators:
     `padding-left: max(12px, env(safe-area-inset-left))`
     `padding-bottom: max(16px, env(safe-area-inset-bottom))`
   - Interactive elements must never sit within $21\text{ pt}$ of the bottom edge on iPhones.
2. **Hoober Thumb Arcs (Landscape 393x852):**
   - Concentrate primary controls into lower-left (base tabs, marquee wand) and lower-right (combat action dock) quarter-circles.
   - Status, timer, and resources sit along the top center.
3. **Touch Target Dimensions:**
   - Absolute minimum interactive target: **$44 \times 44\text{ pt}$** (Apple HIG) / **$48 \times 48\text{ dp}$** (Material).
   - Critical tactical buttons (`Stop`, `Attack-Move`, `Superweapon`): **$52 \times 52\text{ pt}$**.
   - Minimum inter-button padding: **$8\text{ pt}$**.

---

## 7. The 5 GUI Styles Matrix

Every HUD implementation must implement the standard `Hud` interface and adapt across viewports:

| GUI Style | Core Layout Concept | Target Viewports | Primary Interaction Paradigm |
| :--- | :--- | :--- | :--- |
| **`zh` (Zero Hour)** | Classic bottom dashboard (Radar left, portrait center-left, 3x4 grid center-right, powers right). | Desktop $1440\times 900$, iPad Landscape | M+K dense command grid, builder placement tabs. |
| **`cnc3` (Tiberium Wars)**| Westwood vertical right sidebar (Radar top, tabbed production, 3x4 cameos, powers bottom). | Desktop $1440\times 900$, iPad Portrait/Landscape | Global off-map production queues, tab cycling. |
| **`ra3` (Red Alert 3)** | Top status strip + Right build strip + CommandStick radial wheel support. | Desktop, Gamepad Controller | Dual-stick camera/cursor, 8-way radial abilities, secondary 'F' toggle. |
| **`jslc` (Torch / JSLC)** | Split drawer layout (ADZA: Adaptive Dual-Zone Anchor, Cobalt design system). | iPad Portrait $820\times 1180$, iPhone Landscape | Left macro drawer / Right tactical micro drawer. |
| **`minimal` (Phone Overlay)**| Transparent floating action buttons, collapsed radar bubble, maximum 3D view. | iPhone Landscape & Portrait ($393\times 852$) | Dual thumb arcs, lower 40% thumb dock, tap-to-tile micro. |

---

## 8. Latency Perception & Tactile Audio Synthesis

1. **$<50\text{ms}$ Response Ceiling:** Client-side prediction must immediately render green movement ripples, target lock brackets, and trigger voice lines without awaiting network lockstep ticks.
2. **iOS Tactile Audio Substitute:** Because mobile Safari permanently blocks `navigator.vibrate`, synthesize an $8\text{ms}$ $2.4\text{kHz}$ decaying sine wave via Web Audio API upon touch down to generate a psychoacoustic tactile click in the player's fingertips.

---

## 9. Verification & Automated Playwright Emulation

All PRs and feature branches touching input handling must pass Playwright device emulation tests:
- Desktop M+K ($1440\times 900$): RMB move, LMB marquee, WASD pan, hotkey grid.
- iPhone 15 Pro Landscape ($852\times 393$ pt, 3x DPR): Safe-area padding, dual-thumb reach, $+48\text{ pt}$ offset build ghost, $28\text{ pt}$ target snap.
- iPad Pro 11 ($1024\times 1366$ pt): 1-finger pan, $180\text{ms}$ dwell box select, 2-finger pinch zoom, double-tap archetype select, trackpad `pointerType: 'mouse'` switching.
