---
name: mesh-geometric-upscaling
description: >-
  Technical standard and operational pipeline for upscaling 3D asset geometry to match 1080p, 4K, and 8K cinematic resolutions without faceting.
  Includes curvature sagitta formulas, density targets per square foot, hero component integration, and non-destructive LOD workflows.
---

# 3D Geometric Upscaling & Cinematic Density Standard

This skill establishes the engineering formulas, polygon density benchmarks, and geometry reconstruction workflows required to upscale 3D models from low/mid-poly game assets into cinematic-grade hero models suitable for **1080p Full HD, 4K UHD, and 8K master cinematography**.

---

## 1. Optical Mathematics of Polygon Density

The required geometric detail of any 3D asset is governed by the camera's optical resolving power on the viewport raster.

### A. Linear Pixels Per Foot (PPF) Formula
$$\text{PPF} = \frac{W_{\text{raster}}}{W_{\text{viewport\_ft}}}$$

Where:
* $W_{\text{raster}}$ = Horizontal image width in pixels ($1,280$ for 720p, $1,920$ for 1080p, $3,840$ for 4K, $7,680$ for 8K).
* $W_{\text{viewport\_ft}}$ = Real-world width framed by the camera lens in feet.

```
+-------------------------------------------------------------------------------------------------------+
| RESOLUTION          ESTABLISHING (1,100 ft)    MEDIUM DECK (100 ft)   HERO INSERT (15 ft)    MACRO (5 ft) |
+-------------------------------------------------------------------------------------------------------+
| 720p Standard HD    1.16 px/ft                 12.80 px/ft            85.33 px/ft            256.0 px/ft   |
| 1080p Full HD       1.74 px/ft                 19.20 px/ft            128.00 px/ft           384.0 px/ft   |
| 2K Cine (2048x1080) 1.85 px/ft                 20.48 px/ft            136.53 px/ft           409.6 px/ft   |
| 4K UHD (3840x2160)  3.47 px/ft                 38.40 px/ft            256.00 px/ft           768.0 px/ft   |
| 8K DCI (8192x4320)  7.41 px/ft                 81.92 px/ft            546.13 px/ft           1,638.4 px/ft |
+-------------------------------------------------------------------------------------------------------+
```

---

## 2. The Curvature Sagitta Rule ($s \le 1.0\,\text{px}$)

To prevent the human eye from detecting polygonal silhouettes or faceted highlights along a curved surface, the geometric sagitta (the maximum deviation $s$ between the curved arc of radius $R$ and the flat chord of length $L$) must not exceed **$1.0$ pixel on the camera sensor**:

$$s = R - \sqrt{R^2 - \left(\frac{L}{2}\right)^2} \approx \frac{L^2}{8R} \le \frac{1}{\text{PPF}}$$

Solving for maximum segment length $L$:
$$L_{\text{max}} \le \sqrt{\frac{8 \cdot R}{\text{PPF}}}$$

### Minimum Radial Sides Formula
For a complete cylinder of radius $R$ (e.g., gun barrel, radar dome, mast pipe), the minimum number of radial segments $N_{\text{min}}$ is:
$$N_{\text{min}} = \left\lceil \frac{\pi}{\arccos\left(1 - \frac{s_{\text{max}}}{R}\right)} \right\rceil \approx \left\lceil \frac{2\pi R}{L_{\text{max}}} \right\rceil = \left\lceil \pi \sqrt{\frac{R \cdot \text{PPF}}{2}} \right\rceil$$

### Radial Edge Thresholds for 1080p vs. 720p (Hero $15\,\text{ft}$ Framing):
* **Hull Flare / Bilge Turn ($R = 30\,\text{ft}$):** $720p \rightarrow 113\,\text{sides}$; $1080p \rightarrow \mathbf{138\,\text{sides}}$.
* **Main Gun Barbette ($R = 6\,\text{ft}$):** $720p \rightarrow 51\,\text{sides}$; $1080p \rightarrow \mathbf{62\,\text{sides}}$.
* **Mk 45 5-inch / 76mm Gun Barrel ($R = 6\,\text{in}$):** $720p \rightarrow 14\,\text{sides}$; $1080p \rightarrow \mathbf{18\,\text{sides}}$ (Flight 1 rev01 used 12; visible faceting).
* **Mast Pipes & Canisters ($R = 3\,\text{in}$):** $720p \rightarrow 10\,\text{sides}$; $1080p \rightarrow \mathbf{13\,\text{sides}}$.
* **Safety Railings ($R = 1\,\text{in}$):** $720p \rightarrow 6\,\text{sides}$; $1080p \rightarrow \mathbf{8\,\text{sides}}$.

---

## 3. Surface Density Benchmarks Across Resolutions

Warship hulls consist of vast planar steel plates punctuated by dense mechanical clusters. Target triangle densities must be blended accordingly:

```
+---------------------------------------------------------------------------------------------------+
| TIER / RESOLUTION      BROAD PLATING       DECK & ISLAND FITTINGS    HERO WEAPONS      WHOLE SHIP AVERAGE |
+---------------------------------------------------------------------------------------------------+
| 720p HD                0.5 - 1.0 t/sq ft   5 - 12 t/sq ft            20 - 50 t/sq ft   0.8 - 1.5 t/sq ft  |
| 1080p Full HD          1.0 - 2.0 t/sq ft   10 - 25 t/sq ft           40 - 100 t/sq ft  1.8 - 3.5 t/sq ft  |
| 2K Cinematic           1.5 - 3.0 t/sq ft   15 - 35 t/sq ft           60 - 150 t/sq ft  2.5 - 5.0 t/sq ft  |
| 4K UHD                 4.0 - 8.0 t/sq ft   40 - 100 t/sq ft          150 - 400 t/sq ft 7.0 - 15.0 t/sq ft |
| 8K Master              15 - 30 t/sq ft     150 - 350 t/sq ft         500 - 1,500 t/sf  25 - 60 t/sq ft    |
+---------------------------------------------------------------------------------------------------+
```

---

## 4. The Four Pillars of Geometric Upscaling

Upscaling a low/mid-poly model for 1080p+ is **not** achieved by applying a naive global Catmull-Clark subdivision modifier (which balloons planar polygon counts without adding detail, softens sharp naval plate edges, and distorts UV maps). It is executed through four targeted operations:

### Pillar 1: Targeted Radial Curvature Resampling
* Isolate all cylindrical and conical nodes (gun barrels, radar radomes, propeller hubs, life raft canisters, stanchions).
* Replace or resample vertices along the perimeter to meet the $s \le 1.0\,\text{px}$ threshold ($\ge 18$ radial segments for barrels, $\ge 8$ for stanchions).
* Preserve the longitudinal extrusion length and endcap cap planes.

### Pillar 2: Physical Deck Relief (Replacing Texture Bakes)
At 1080p deck-level shots ($19.2\,\text{px/ft}$), normal-mapped details look flat at grazing angles. Replace flat texture planes with physical geometry:
* **EMALS Catapult Troughs:** Extrude a recessed channel $0.15\text{m}$ deep by $0.45\text{m}$ wide with longitudinal guide lips.
* **Jet Blast Deflector (JBD) Coamings:** Model the recessed perimeter water-cooling troughs and authentic aft hinge knuckles.
* **Tie-Down Stars:** Array physical 5-point deck sockets or cruciform recesses across flight decks ($10\text{ft}$ centers).
* **Arresting Gear:** Model physical deck sheave housings, retracting wire dampers, and purchase cables.

### Pillar 3: Hero Assembly Swapping
Never attempt to subdivide a 200-triangle surrogate box representing a weapon or sensor. Swap it with a dedicated high-fidelity CAD/GLB component:
* Replace proxy CIWS boxes with authentic **$42\text{k}$-triangle Phalanx Block 1B** (`weapons-cad/phalanx_ciws_naval.glb`).
* Replace low-poly turret shells with authentic **$23\text{k}$-triangle Oto Melara 76/62 SR** (`weapons-cad/oto_melara_76_sr.glb`).
* Replace flat VLS deck textures with authentic **Mk 41 / C-Dome 8-cell coaming grids** with individual recessed hatch lips.

### Pillar 4: Specular Edge Beveling (Chamfers)
In real warships, armor plate edges are rounded or welded with beads ($5\text{mm} - 25\text{mm}$ radius). Razor-sharp $90^\circ$ computer graphics edges fail to capture specular lighting highlights, making models look fake:
* Apply a **$15\text{mm} - 30\text{mm}$ 2-segment bevel/chamfer** with limit method set to `Angle` ($30^\circ - 60^\circ$) on all primary hull chines, superstructure coamings, and mast yardarms.
* Enable **Weighted Normal** to maintain perfectly flat shading across large planar armor plates while keeping highlights sharp on the beveled boundaries.

---

## 5. Non-Destructive Multi-Tier LOD Production Pipeline

To support both **1080p/4K cinematic video production** and **real-time C++ game engines**:

```
+---------------------------------------------------------------------------------+
|                       ORIGINAL HIGH-FIDELITY RAW MASTER                         |
|             (Preserved in /masters/ or sketchfab-library - NEVER DESTROY)       |
+---------------------------------------------------------------------------------+
                                        │
             ┌──────────────────────────┴──────────────────────────┐
             ▼                                                     ▼
+───────────────────────────+                         +───────────────────────────+
| LOD0: CINEMATIC MASTER    |                         | LOD1: 1080p GAME / CUTSCENE|
| (1080p, 4K, 8K Video)     |                         | (JSLCnC High Detail Engine)|
| - Full physical relief    |                         | - Clean welded hulls      |
| - 18-32 side cylinders    |                         | - Hero weapons attached   |
| - Hero CAD weapon mounts  |                         | - 18-side barrels         |
| - Target: 300k - 1.5M tris|                         | - Target: 150k - 400k tris|
+───────────────────────────+                         +───────────────────────────+
                                                                   │
                                                                   ▼
                                                      +───────────────────────────+
                                                      | LOD2: FLEET RTS OVERHEAD  |
                                                      | (Performance C++ Gameplay)|
                                                      | - Baked normal textures   |
                                                      | - 8-12 side cylinders     |
                                                      | - Target: 25k - 60k tris  |
                                                      +───────────────────────────+
```

---

## 6. Verification Checklist Before Asset Release

Every upscaled warship model must pass this verification matrix before promotion:

1. **Sagitta Test:** Do gun barrels have at least 18 radial segments? Do masts have at least 12 segments?
2. **Deck Relief Test:** Are catapult tracks and elevator gaps physically modeled rather than painted?
3. **Bevel Highlight Test:** Do primary superstructure edges have specular catchers under directional sunlight?
4. **Kinematic Decoupling:** Are animated parts (elevators, doors, turrets, barrels) separated into individual nodes with correct parent links?
5. **Metric Scale:** Is length overall within $\pm 0.5\%$ of real-world naval specifications?
6. **Waterline Alignment:** Is the design waterline exactly at $Y = 0.000\,\text{m}$?

---

## 7. Host Platform & Parasite / Child Asset Hierarchy Standard

In military and naval cinematography, no capital combatant operates in a vacuum. A capital ship is a host platform for a nested hierarchy of **parasite / child assets** (embarked aircraft, landing craft, ship's boats, ground combat vehicles, and deck support equipment).

### The Inviolable Resolution Matching Rule:
> [!IMPORTANT]
> **Resolution Matching Rule:** When staging child or parasite assets on the deck, in the well deck, or in the davits of a host vessel, **the child asset must match or exceed the optical resolution tier of the host platform**.
> * Staging a low-poly $4\text{k}$-triangle game asset (e.g. proxy F-35) on a $300\text{k}$-triangle 1080p flight deck destroys visual immersion instantly when the camera closes in.
> * The child asset must be drawn from the **LOD0 Hero Master** catalog with matching radial curvature and physical detail.

### Host-to-Parasite Mapping Matrix:

```
+---------------------------------------------------------------------------------------------------------------+
| HOST PLATFORM             PARASITE / CHILD ASSET CATEGORY       SPECIFIC EMBARKED ASSETS        HERO REPOSITORY FILE |
+---------------------------------------------------------------------------------------------------------------+
| USS Gerald R. Ford        Embarked Carrier Air Wing (CVW)       F-35C Lightning II (Carrier)    flight-1a / CAD Hero |
| (CVN-78 / INS Adir)                                             E-2D Advanced Hawkeye (AEW)     flight-1a / Raw E-2D |
|                                                                 MH-60R/S Seahawk (Helo)         D:\sketchfab (1.52M) |
|                           Flight Deck Ground Equipment          A/S32A-31A Tow Tractor ("Mule") flight-1a GSE       |
|                                                                 A/S32A-32 Crash Crane ("Tilly") flight-1a GSE       |
|                           Ship's Boats (Sponsons/Davits)        11m / 7m Navy RHIB              flight-1a (139k)     |
|                           Integrated Defensive Weapons          Mk 15 Phalanx Block 1B CIWS     weapons-cad (42.9k)  |
|                                                                 RIM-116 RAM & ESSM Launchers    weapons-cad          |
+---------------------------------------------------------------------------------------------------------------+
| USS Wasp                  Well Deck Amphibious Craft            3x LCAC (Tandem Spots 1-3)      flight-1a (29.5k raw)|
| (LHD-1)                                                         Alternative: 2x LCU-1610        amphibious library   |
|                           Embarked Marine Air Wing (ACE)        MV-22B Osprey (Tiltrotor)       aviation library     |
|                                                                 AV-8B / F-35B Lightning II      aviation library     |
|                                                                 CH-53K, AH-1Z, UH-1Y, MH-60S    aviation library     |
|                           Ground Combat Element (GCE / Staging) M1A2 SEPv2 Abrams MBT           flight-1b (306k)     |
|                                                                 M998 HMMWV Humvee               raw library (1.87M)  |
|                                                                 LAV-25 & ACV-30 Amphibious      flight-1b armor      |
|                           Ship's Boats (Davit Pockets)          7m Navy RHIB                    flight-1a (139k)     |
|                           Integrated Defensive Weapons          Phalanx Block 1B & Mk 49 RAM    weapons-cad (42.9k)  |
+---------------------------------------------------------------------------------------------------------------+
| Arleigh Burke             Embarked Aviation (Dual Hangar)       2x MH-60R Seahawk LAMPS III     D:\sketchfab (1.52M) |
| Flight III (DDG-125)                                            Optional: MQ-8C Fire Scout      aviation library     |
|                           Ship's Boats (Amidships Davits)       2x 7m Navy RHIB (Vestdavit)     flight-1a (139k)     |
|                           Primary Combat & Launchers            Mk 45 Mod 4 5-inch/62 Gun       hero 24-side barrel  |
|                                                                 Mk 41 VLS (32 Fwd / 64 Aft)     physical hatch grids |
|                                                                 2x Phalanx Block 1B CIWS        weapons-cad (42.9k)  |
+---------------------------------------------------------------------------------------------------------------+
| Sa'ar 6 Stealth Corvette  Embarked Aviation (Enclosed Hangar)   1x SH-60F / MH-60R Seahawk      D:\sketchfab (1.52M) |
| (INS Magen)                                                     Optional: Orbiter 4 / Heron UAV tactical VTOL UAV    |
|                           Ship's Boats                          1x 7m Commando RHIB / USV       flight-1a (139k)     |
|                           Integrated Weapons Payloads           Oto Melara 76/62 SR Gun         weapons-cad (23.3k)  |
|                                                                 40x Rafael C-Dome VLS Cells     physical 16-side cyl |
|                                                                 32x IAI Barak-8 VLS Cells       forecastle well      |
|                                                                 16x Gabriel V AShM Canisters    amidships battery    |
|                                                                 2x Rafael Typhoon 25mm RWS      bridge wings         |
+---------------------------------------------------------------------------------------------------------------+
```

---

## 8. Ordnance Elevators, Catwalk Stairways, & Secondary Combat Suites Standard

At **1080p Full HD ($19.2\,\text{px/ft}$ flight deck ops, $128\,\text{px/ft}$ hero insert)**, camera angles skimming the flight deck or tracking crew operations expose fine architectural and weapon details that are invisible at 720p:

### A. Advanced Weapons Elevators (AWE / Bomb Elevators)
* **Carrier Magazine Logistics:** On nuclear supercarriers (*Ford* CVN-78), 11 electromagnetic Advanced Weapons Elevators (AWE) transport ordnance from deep armored magazines (decks 5–8) to flight deck arming stations.
* **Flight Deck Blast Hatches:**
  * Hatches must be modeled as **physical bi-parting armored flush leaves** with perimeter drainage gutters ($0.15\text{m}$ deep) and raised coamings ($0.10\text{m}$).
  * Hatches are positioned on dedicated **weapons handling sponsons** (outboard of flight paths) to allow ordnance staging without fouling active catapult or arrestment operations.
  * Internal elevator cabs must have physical interior wall tracks (MagneMotion LSM stators) and clearance for A/M32K-4A bomb carts bearing $2,000\,\text{lb}$ munitions.
* **Amphibious Ships (*Wasp* LHD-1):** 6 ordnance elevators with flush armored hatches across spots 2, 4, 6, 8 connecting vehicle staging decks and magazines to the flight deck.

### B. Stairways, Catwalk Ladders, & Vertical Circulation
* **Inclined Catwalk Staircases (Naval Ladders):**
  * Stair rise angles: $45^\circ$ to $55^\circ$.
  * Treads: Open-grate steel grip-strut ($0.70\text{m}$ wide, $0.25\text{m}$ deep, $0.22\text{m}$ riser).
  * Handrails: Dual tubular steel railings ($1.05\text{m}$ top rail, $0.55\text{m}$ intermediate knee rail).
  * Peripheral catwalks running the entire perimeter of flight decks and gallery decks require physical treads and open scuppers.
* **Vertical Rung Ladders & Monkey Ladders:**
  * Round steel rungs ($25\text{mm}$ diameter, $300\text{mm}$ vertical pitch, $450\text{mm}$ width).
  * Safety hoop cages required on all ladder runs exceeding $3.0\text{m}$ vertical climb on masts, island faces, and elevator shafts.
* **Quick-Acting Watertight Scuttles (QAWTS) & Companionways:**
  * Raised hatch coamings ($0.30\text{m} - 0.45\text{m}$ above deck) with counterbalanced spring-assist cylinders, dogging handles, and escape ladders leading below.

### C. Secondary Defensive Systems & Close-In Weapons
* **Phalanx Block 1B Sub-Assemblies:** Radome search dome, port-side FLIR thermal sight turret, 6-barrel M61A1 Vulcan with restraint clamp and flash suppressor, 1,550-round cylindrical drum, and deck Local Control Station (LCS) cabinet.
* **Autocannons & Machine Guns:** Mk 38 Mod 2/3 $25\text{mm}$ Bushmaster chain guns and $.50$-cal M2HB machine gun pintle mounts with curved ballistic gunner shields.
* **Soft-Kill EW & Decoys:** AN/SLQ-32(V)6/7 SEWIP active/passive enclosures, Mk 36/53 SRBOC 6-tube chaff mortar banks, Mk 234 Nulka hovering decoy launchers, and AN/SLQ-25 Nixie stern torpedo decoy winches.
* **Fire Control Illuminators:** Mk 99 / AN/SPG-62 parabolic radar dish directors (3 on *Burke* DDG).

---

## 9. Canister Lid & Blast Cover Kinematic Standard (The Lift-and-Pivot Sequence)

On modern warships, missile launch canisters (C-Dome, Mk 41 VLS, Gabriel V, Harpoon) and torpedo hull doors do **not** simply rotate on a primitive hinge pin. Doing so in 1080p close-ups causes the lid geometry to clip straight through the raised coaming flange. They operate via a precise **three-phase lift-and-pivot kinematic sequence**:

```
PHASE 1: UNLATCH & VERTICAL LIFT          PHASE 2: ACTUATOR SWEEP TO 105°          PHASE 3: DAMPED RETURN & CLAMP SEAT
┌─────────────────────────────────┐      ┌───────────────────────────────┐        ┌─────────────────────────────────┐
│     [Canister Lid / Cover]      │      │            \                  │        │     [Canister Lid / Cover]      │
│               ▲                 │      │             \  Lid Locked at  │        │               ▼                 │
│               │ ΔY = +30mm      │      │              \ 105° Over-Ctr  │        │               │ Pull-down clamp │
│  +---------------------------+  │      │               \               │        │  +===========================+  │
│  | Gasket Clears Raised Lip  |  │      │    [Dual Chrome Pistons]      │        │  | Gasket Compressed 100%    |  │
│  +---------------------------+  │      │    [Fully Extended +105°]     │        │  | Locking Dogs Engage       |  │
└─────────────────────────────────┘      └───────────────────────────────┘        └─────────────────────────────────┘
```

### A. The 3-Phase Kinematic Breakdown:
1. **Phase 1: Unseating & Vertical Lift ($\Delta Y = +25\text{mm}$ to $+50\text{mm}$):**
   * Before rotation begins, hydraulic or pneumatic locking dogs disengage.
   * A pantograph or four-bar linkage lifts the entire lid **vertically upward** perpendicular to the canister face.
   * **Visual Purpose:** Breaks the vacuum seal on the thick elastomeric compression gasket and clears the $20\text{mm}$ raised coaming lip without dragging the gasket across the metal rim.
2. **Phase 2: Actuator Sweep ($0^\circ \rightarrow +105^\circ$ Over-Center Lock):**
   * Driven by dual hydraulic or pneumatic cylinders with polished chrome-plated piston rods visibly extending.
   * The lid rotates open past vertical to approximately **$105^\circ$ into an over-center mechanical lock**.
   * **Operational Cause:** A lid stopped at exactly $90^\circ$ can be slammed shut by missile rocket motor plume backpressure, deck winds, or heavy sea roll, destroying the launch vehicle. The $105^\circ$ over-center detent guarantees a clear missile trajectory.
3. **Phase 3: Damped Return & Compressive Seating ($\Delta \theta = -105^\circ \rightarrow \text{Final } -30\text{mm}$ Pull-Down):**
   * After launch or cycle test, the cylinder retracts under smooth hydraulic damping (no metallic bounce).
   * As the lid reaches horizontal alignment, hardened steel alignment guide pins enter female conical indexing sockets on the canister flange.
   * The linkage pulls the lid **vertically downward**, compressing the black molded neoprene gasket against the machined metallic sealing face.
   * Perimeter rotating locking dog wedges turn into position, creating an audible, visible mechanical seal.

### B. Critical Visual & Mechanical Details for 1080p Modeling:
* **Dual Chrome Actuator Rams:** High-specular reflective cylinder rods extending from satin-gray actuator barrels.
* **Flexible Braided Grounding Straps:** Copper/tin braided lightning and static bonding straps looping between lid and canister body.
* **Elastomer Compression Gasket:** Molded black rubber seal ($20\text{mm}$ width, semi-gloss sheen) seated in a recessed perimeter channel.
* **Perimeter Locking Dog Wedges & Proximity Limit Switches:** Microswitch interlocks that prevent missile ignition until the lid sensor confirms $\ge 100^\circ$ open angle.

---

## 10. Marking Conventions & Decal Architecture Standard

At 1080p and 4K resolutions, flight deck markings, hull numbers, draft scales, and hazard boundaries must be rendered with authentic geometric precision and correct optical response.

### A. Color & Specular Specifications (Fed-Std-595 / AMS-STD-595)
* **Deck Non-Skid Dark Gray (#36076 / #36081):** sRGB `#3B3E42`, Roughness `0.88 - 0.95`. Coarse broadcast aggregate texture.
* **Deck Marking White (#37875 / #17875):** sRGB `#ECEFF1`, Roughness `0.45 - 0.55`. High contrast against non-skid.
* **Hazard Yellow (#33538 / #13538):** sRGB `#F5A800`, Roughness `0.42 - 0.50`. Used for JBD chevrons, elevator boundaries, helo spots.
* **Danger / Foul Line Red (#31105 / #11105):** sRGB `#B71C1C`, Roughness `0.45 - 0.52`. Angled deck foul lines, weapons elevator boxes.
* **AFFF / Safety Green (#14187):** sRGB `#1B5E20`, Roughness `0.35 - 0.45`. Firefighting and washdown coamings.
* **Drop-Shadow Black (#37038):** sRGB `#1A1A1A`, Roughness `0.80 - 0.90`. 45° hull drop shadows, JBD black chevrons.
* **Haze Gray Topsides (#26270 / #36270):** sRGB `#7D838A`, Roughness `0.55 - 0.65`. Vertical hull and superstructure plating.
* **Dynamic Team-Tint Channel (#00FF00):** Strictly reserved as a dynamic shader mask. Pure green `#00FF00` must NEVER be used for static painted markings.

### B. Core Operational Markings (NAVAIR 00-80T-105)
1. **Catapult Launch Tracks:** Continuous solid white line ($0.30\text{m} / 12\text{in}$ width) with yellow boundary dashed guidelines ($0.10\text{m}$ width, $3.05\text{m} / 10\text{ft}$ offset).
2. **Angled Deck Recovery Foul Line:** Alternating red and white segments ($0.45\text{m} \times 0.15\text{m} / 1.5\text{ft} \times 0.5\text{ft}$). Inviolable recovery zone boundary.
3. **Helicopter TLOF Spots (Spots 1–9 on LHD, DDG & Sa'ar 6 Helidecks):**
   * Outer aiming circle ($6.1\text{m} - 9.1\text{m} / 20\text{ft} - 30\text{ft}$ diameter) in Fed-Std-595 White or Yellow.
   * Bold stencil spot number ($1.8\text{m} - 2.4\text{m} / 6\text{ft} - 8\text{ft}$ tall) facing the pilot's landing approach corridor.
   * Longitudinal heading alignment bar bisecting the circle.
4. **Moving Machinery & Elevator Hazards:**
   * JBD perimeter: $45^\circ$ diagonal alternating yellow and black hazard chevrons ($0.15\text{m} / 6\text{in}$ width).
   * Deck-edge elevators: $45^\circ$ diagonal red and white fall-hazard zebra stripes with an inner solid yellow boundary.
   * Advanced Weapons Elevators (AWE): Solid red perimeter box with bold yellow stenciled text: `"WEAPONS ELEVATOR - KEEP CLEAR"`.

### C. Hull Topsides & Waterline Markings (NAVSEA Standard)
1. **Tactical Hull Numbers (Bow & Stern):**
   * Typography: Norfolk Naval Shipyard Block Stencil.
   * Classic 45° Drop Shadow: White digit face (#37875) with a flat black shadow (#37038) cast $45^\circ$ down-and-aft. Provides optical contrast against Haze Gray in all maritime weather conditions.
   * Scale: $3.6\text{m} - 4.8\text{m}$ ($12 - 16\text{ft}$) on CVN/LHD; $2.4\text{m} - 3.0\text{m}$ ($8 - 10\text{ft}$) on DDG.
2. **Hull Draft Marks:**
   * Located at Stem (FP), Midships, and Stern (AP).
   * 6-inch Arabic numerals spaced at 12-inch vertical intervals. The bottom of the numeral marks the exact whole-foot waterline.
3. **Subsurface Appendage Warning Icons:**
   * Stylized white sonar bulb symbol stenciled on the bow flare above the waterline to warn tugs and lines of the underwater dome.
   * Transom propeller warning stencils (`"DANGER - DUAL SCREWS"`).

### D. 3D Engine Decal Architecture
* **Z-Fighting Prevention:** Model painted deck lines and markings as floating decal geometry offset along the surface normal vector by $\Delta Y = +0.50\text{mm}$ to $+1.20\text{mm}$.
* **Dual-UV PBR Setup:**
  * UV1: Tileable coarse aggregate normal/roughness map for the base non-skid deck.
  * UV2: Macro unwrap for decal markings, alpha-blended over UV1.
* **Roughness Delta:** Retain a distinct roughness delta between the rough base deck ($0.90$) and the smoother marking topcoat ($0.48$). This creates authentic specular glint under wet weather and deck floodlights.



