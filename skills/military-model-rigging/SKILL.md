---
name: military-model-rigging
description: >-
  Expert guide and technical standard for naval architecture, military vehicle 3D modeling,
  kinematic rigging (elevators, doors, well decks, CIWS, VLS), and sensor/radome verification in Blender and Three.js/WebGL.
---

# Naval Architecture & Military Vehicle Kinematics Standard

This skill establishes the engineering and 3D modeling standard for capital warships, amphibious vessels, combat systems, and military vehicles. It provides exact geometric constraints, kinematic hierarchies, common Blender pitfalls, and sensor audit procedures.

---

## 1. Naval Coordinate System & Transform Conventions

To ensure flawless interoperability between Blender, Trimesh, glTF, and WebGL (Three.js):

| Axis | Naval Convention | glTF / WebGL Convention | Blender Convention | Kinematic Translation |
| :--- | :--- | :--- | :--- | :--- |
| **X** | Transverse (Port / Starboard) | Lateral: $-X$ = Port, $+X$ = Starboard | Lateral: $+X$ = Starboard, $-X$ = Port | Sway / Roll axis |
| **Y** | Vertical (Keel to Masthead) | Vertical: $+Y$ = Up (Height), $-Y$ = Keel | Forward/Back ($+Y$ = Bow, $-Y$ = Stern) | Heave (Elevators) |
| **Z** | Longitudinal (Bow to Stern) | Longitudinal: $-Z$ = Bow (Ahead), $+Z$ = Stern (Astern) | Vertical ($+Z$ = Up, $-Z$ = Down) | Surge / Pitch axis |

> [!IMPORTANT]
> **Blender to glTF Export Rule:** In Blender, Warship Bow must face $+Y$ or $-Y$ depending on exporter settings, but glTF standard mandates **Forward is $-Z$, Up is $+Y$, Right/Starboard is $+X$**. Always apply transforms (`Ctrl+A` -> *All Transforms*) before parenting or exporting.

---

## 2. Aircraft Elevators & Guide Rail Kinematics

### A. Amphibious Assault Ships (*Wasp*-class LHD / *America*-class LHA)
* **Configuration:** Two deck-edge folding elevators:
  * **Elevator 1 (Port Forward):** Frame 45–55.
  * **Elevator 2 (Starboard Aft of Island):** Frame 85–95.
* **Vertical Travel:**
  * Lower position: Hangar Deck ($Y \approx 8.5\text{m}$ above baseline).
  * Upper position: Flight Deck ($Y \approx 19.8\text{m}$ above baseline).
  * Net vertical stroke: $\approx 11.3\text{m}$.
* **Folding Platform Kinematics:**
  * For Panama Canal lock transit, the outboard section of each elevator platform hinges **$90^\circ$ vertically upward**.
  * **Kinematic Chain:**
    `Ship Hull` -> `Elevator_Carriage` (Vertical Translation Constraint along $Y$) -> `Elevator_Platform_Hinge` (Rotation Constraint around $Z$-axis, $0^\circ$ to $90^\circ$).
  * When elevator is at flight deck level, platform locks into deck coaming; safety stanchions automatically retract.

### B. Nuclear Supercarriers (*Gerald R. Ford* CVN-78 / *Nimitz*-class)
* **Configuration:**
  * CVN-78 features **3 deck-edge Aircraft Elevators** (A/E 1: Starboard forward of island, A/E 2: Starboard aft of island, A/E 3: Port aft). *Note: Unlike Nimitz which had 4, CVN-78 eliminated Elevator 4 to optimize flight deck flow.*
  * Plus **11 Advanced Weapons Elevators (AWE)** utilizing MagneMotion linear synchronous motor (LSM) electromagnetic actuation.
* **Rigging Advanced Weapons Elevators (AWE):**
  * Upper Stage Hatch: Bi-parting blast-resistant flush hatch on flight deck / gallery deck.
  * Elevator Cab: Travels between deep magazine decks and flight deck weapons handling sponsons.
  * Sequence: `Hatch Opens` ($90^\circ$ upward hinge or slide) -> `Cab Rises to Deck Flush` -> `Munitions Transfer` -> `Cab Departs` -> `Hatch Closes & Seals`.

---

## 3. Well Deck Operations & Tandem LCAC Staging Rule

Amphibious assault ships (*Wasp* LHD, *San Antonio* LPD, *Whidbey Island* LSD) carry Landing Craft Air Cushion (LCAC) hovercraft. Incorrectly staging them side-by-side is a severe amateur modeling error.

```
+-----------------------------------------------------------------------------------+
|                               WASP-CLASS WELL DECK                                |
|  Length: 81.4 m (267 ft)  |  Width: 15.2 m (50 ft)                                |
|                                                                                   |
|  +--------------------+   +--------------------+   +--------------------+         |
|  |     LCAC #1        |   |     LCAC #2        |   |     LCAC #3        |  ===    | STERN
|  |  26.4m x 14.3m     |   |  26.4m x 14.3m     |   |  26.4m x 14.3m     |  ===    | GATE
|  |   (Spot 1 - Bow)   |   |  (Spot 2 - Center) |   |   (Spot 3 - Aft)   |  ===    | (Hinges
|  +--------------------+   +--------------------+   +--------------------+         |  Down)
|                                                                                   |
+-----------------------------------------------------------------------------------+
       <------------------ SINGLE-FILE TANDEM CENTERLINE ------------------>
```

### The Physical Geometric Proof:
* **Well Deck Dimensions:** Length $81.4\text{m}$ ($267\text{ ft}$), Width $15.2\text{m}$ ($50\text{ ft}$).
* **LCAC Dimensions:** Length $26.4\text{m}$ ($87.9\text{ ft}$ off-cushion), Beam $14.3\text{m}$ ($47\text{ ft}$ off-cushion).
* **Clearance Analysis:**
  $$\text{Clearance} = W_{\text{deck}} - B_{\text{LCAC}} = 15.2\text{m} - 14.3\text{m} = 0.9\text{m} \ (2.95\text{ ft total}, \approx 1.47\text{ ft per side})$$
* **The Inviolable Tandem Rule:**
  Because the LCAC beam ($14.3\text{m}$) occupies $94\%$ of the well deck width ($15.2\text{m}$), **side-by-side parking is physically impossible**.
  LCACs MUST be staged **in single-file tandem (one directly in front of the other)** along the centerline:
  1. **Spot 1 (Forward):** Directly behind the well deck control station / vehicle staging ramp.
  2. **Spot 2 (Center):** Middle staging zone.
  3. **Spot 3 (Aft):** Immediate landing zone inside stern gate sill.

### Stern Gate Kinematics:
* **Hinge Line:** Located along bottom sill ($Y \approx 1.8\text{m}$ above keel).
* **Motion:** Folds downward $90^\circ$ into horizontal or slightly depressed plane, forming a continuous ramp into the sea.
* **Ballast Condition:**
  * *Dry Well:* Stern gate vertical closed, deck dry for vehicle maintenance.
  * *Flooded Well:* Ship ballasts aft (trim by stern), submerging well deck sill to $1.8\text{m} - 3.0\text{m}$ of water. Stern gate lowered horizontally, allowing LCACs to fly in on cushion.

---

## 4. Doors, Hatches, and VLS Launch Tube Kinematics

### A. Vertical Launch System (VLS) Hatches (Mk 41, Mk 57, C-Dome, Sylver)
* **Structure:** Flush armored blast hatches protecting canister cells.
* **Kinematics:**
  * **Hinge Axis:** Outer edge of cell coaming.
  * **Actuation:** High-speed pneumatic or hydraulic struts opening to $\ge 90^\circ$ (typically $105^\circ$ to clear missile plume).
  * **Interlock:** Missile motor cannot ignite until hatch microswitch verifies full open angle.

### B. Guided Missile Box Launchers (Mk 29 ESSM, Mk 49 RAM)
* **Mk 29 (8-cell Sea Sparrow / ESSM):**
  * Train/Azimuth: $360^\circ$ on deck pedestal.
  * Elevation: $0^\circ$ to $+65^\circ$.
  * Front muzzle covers: Individual frangible or hinged blast covers.
* **Mk 49 RAM (21-round Guided Missile Launching System):**
  * Train: Continuous circular ring base.
  * Elevation: $-10^\circ$ to $+80^\circ$.

### C. Torpedo Tube Hull Doors & Clamshell Sponsons
* **Mechanism:** Flush exterior hull doors swinging outboard horizontally $90^\circ$ on four-bar pantograph hinges, clearing the triple Mk 32 SVTT torpedo launch barrels.

### D. Aircraft Hangar Doors
* **Pocket Sliding Doors:** Divided into 2–4 vertical telescoping steel panels sliding laterally into recessed side pockets.
* **Rolling Vertical Shutters:** Heavy articulated steel slat curtains rolling upward into overhead barrels.

---

## 5. Phalanx CIWS (Close-In Weapon System) Rigging Standard

The Mk 15 Phalanx Block 1B / SeaRAM requires a rigorous 3-tier kinematic hierarchy:

```
[Phalanx_Base / Barbette] (Fixed to Warship Deck)
   └── [Phalanx_Turret_Azimuth] (Yaw: 360° continuous rotation around Y/Z axis)
         └── [Phalanx_Trunnion_Elevation] (Pitch: -25° depression to +85° elevation)
               ├── [Radome_Head & FLIR_Pod] (Tilted with elevation)
               └── [M61A1_Gatling_Rotor] (Continuous roll around barrel bore axis at 4,500 RPM)
```

### Critical Visual & Mechanical Details:
1. **Radome Profile:** Distinctive cylindrical base with hemispherical white radome dome (housing Ku-band search & track radar).
2. **Block 1B FLIR Pod:** Mounted on the port side of the radome, features optical lens window for surface threat electro-optical tracking.
3. **Gun Barrels:** 6-barrel $20\text{mm}$ M61A1 Vulcan with barrel restraint clamp ring and muzzle flash suppressor.
4. **Elevation Limits:** Never allow gun barrels to elevate past $+85^\circ$ or depress below $-25^\circ$. Ensure clearance over ship superstructure firing cutouts.

---

## 6. Radome & Sensor Array Verification Methodology

Never guess radome counts or locations. Warship electronic warfare and communications follow strict physics-based placement rules:

### A. SATCOM Bilateral Symmetry Rule
* **The Rule:** High-data-rate satellite communication radomes (e.g. AN/WSC-6, OE-82, USC-38 EHF) are ALWAYS installed in **bilateral pairs** (Port and Starboard yardarms/sponsons).
* **Physical Cause:** A single centerline radome is subject to "mast shadowing"—when the ship maneuvers, the steel mast structure blocks line-of-sight to the geostationary satellite, terminating operational comms. A dual-sponson setup guarantees uninterrupted 360° hemispherical sky view.

### B. Sensor Mast Hierarchy (Capital Ships & Carriers)
1. **Primary 3D Air Surveillance:**
   * *Wasp*-class / *America*-class: **AN/SPS-48E** (large planar rectangular phased array antenna) mounted on forward mast.
   * *Ford*-class CVN-78: **Dual Band Radar (DBR) / AN/SPY-3 & AN/SPY-6(V)3 EASR** fixed planar faces integrated directly into island facets at $120^\circ$ separation.
2. **2D Long-Range Air Search:**
   * **AN/SPS-49** (curved parabolic wire-mesh reflector with feed horn) mounted on aft mast or dedicated pedestal.
3. **Surface Search & Navigation:**
   * Dual commercial/military slotted waveguide scanners (Furuno / AN/SPS-73) on lower yardarm.
4. **TACAN Antenna:**
   * Conical dielectric cylinder mounted at the absolute highest apex of the main masthead (unobstructed $360^\circ$ omnidirectional beacon).

---

## 7. Common Blender 3D Military Vehicle Pitfalls & Solutions

| Mistake | Consequence | Correct Technique |
| :--- | :--- | :--- |
| **Unapplied Scale (`Ctrl+A`)** | Modifiers distort; rotations shear; physics engines flip; animations scale unpredictably. | Always `Ctrl+A` -> *Apply All Transforms* before parenting, skinning, or rigging. |
| **Raw Boolean Hull Cuts** | Creates non-manifold zero-thickness geometry, flipped face normals, and massive black shading artifacts. | Keep hull plates watertight and manifold. Mount coamings, aprons, and weapon wells as separate closed geometries or use clean quad topology. |
| **Missing / Flat Normals** | In WebGL/Blender, lighting blows out into flat white chalk or dark facets (`NORMAL=None`). | Compute vertex normals (`trimesh.geometry.mean_vertex_normals`), use Auto Smooth ($30^\circ - 45^\circ$) or Weighted Normal modifier in Blender. |
| **Pivots at Mesh Centers** | Doors rotate around their volumetric center instead of their hinge pin; turrets wobble off barbette centerlines. | Set Origin to Selected on hinge line/pin geometry (`Object -> Set Origin -> Origin to 3D Cursor`). |
| **LCAC Side-by-Side Staging** | Models clip through hull bulkheads because LCAC beam ($14.3\text{m}$) exceeds half the well deck width ($7.6\text{m}$). | **Always stage LCACs in single-file tandem (one in front of the other)** along the well deck centerline. |
| **Floating Underwater Shafts** | Propeller shafts intersect rudders or hover disconnectedly in water. | Extend shaft through bossing/stern tube casting, reinforce with P-struts, and attach directly to 5-bladed marine bronze hub. |

---

## 8. Radar Rotation & Mechanical Sensor Kinematics

Never confuse mechanically rotated radars with electronically steered phased arrays. Rigging errors in warship radar arrays instantly break physical authenticity.

### A. Fixed Phased Array Standard (Zero Mechanical Rotation)
* **Systems:** AN/SPY-1D (Aegis *Burke* / *Ticonderoga*), AN/SPY-6(V)1 AMDR (*Burke* Flight III), AN/SPY-3 & AN/SPY-6(V)3 EASR (*Ford* CVN-78), EL/M-2248 MF-STAR (*Sa'ar 6*), APAR, Sampson.
* **Kinematics:** **RIGIDLY STATIONARY**. Electronic beam steering steers radar pulses at the speed of light using thousands of solid-state transmit/receive modules (T/R).
* **Critical Rule:** If a modeler animates SPY-1, SPY-6, or MF-STAR faces spinning on a mast, it is a catastrophic design error. Radar plates are permanently welded to deckhouse bulkheads at fixed tilt angles ($8.5^\circ$ to $20^\circ$ pitch back).

### B. Mechanically Rotated Radar Categories & Exact RPMs
When a radar antenna mechanically rotates, it requires a continuous $360^\circ$ yaw animation channel around its local vertical axis ($+Y$ in glTF, $+Z$ in Blender) using **`LINEAR` interpolation** (constant angular velocity $\omega = \frac{2\pi \cdot \text{RPM}}{60}$, zero bezier easing):

| Radar Nomenclature | Antenna Geometry & Type | Operational Role | Standard Rotation Rate | Direction |
| :--- | :--- | :--- | :--- | :--- |
| **AN/SPS-48E** | Large rectangular planar phased array ($5.2\text{m} \times 5.3\text{m}$) | 3D Long-Range Air Surveillance | **$7.5\,\text{RPM}$** (Surveillance) / **$15.0\,\text{RPM}$** (Track) | Clockwise (from above) |
| **AN/SPS-49(V)** | Curved parabolic wire-mesh reflector with projecting feed horn ($7.3\text{m}$) | 2D Long-Range Air Search | **$6.0\,\text{RPM}$** (Long Range) / **$12.0\,\text{RPM}$** (High Data) | Clockwise |
| **AN/SPS-73(V) / Furuno** | Horizontal slotted waveguide scanner bar ($1.8\text{m} - 3.7\text{m}$) | Surface Search & Navigation | **$24.0\,\text{RPM} - 30.0\,\text{RPM}$** | Clockwise |
| **AN/SPS-67(V)** | Curved parabolic surface search dish on pedestal | Medium-Range Surface Search | **$15.0\,\text{RPM}$** | Clockwise |
| **E-2D Hawkeye Rotodome** | Lenticular rotodome ($7.32\text{m} / 24\text{ft}$ diameter) | Airborne Early Warning (AEW) | **$6.0\,\text{RPM}$** | Continuous |
| **Phalanx Ku-Band Dome** | Hemispherical radome on CIWS turret | Search & Track Radar | Internal feed horn spins, dome remains stationary with turret | Slews with Turret |
| **Mk 99 / SPG-62 Illuminator**| $2.4\text{m}$ parabolic dish on 2-axis gimbal pedestal | Semi-Active Missile Guidance | **DOES NOT SPIN 360°**: Slews and tracks targets ($\pm 180^\circ$ yaw, $-10^\circ/+85^\circ$ pitch) | Tracking Slews |

---

## 9. Warship Lighting Systems: Active Underway vs. "Running Dark"

Warship lighting is governed by international maritime law (COLREGs 1972) during peacetime, and military tactical blackout doctrine (Condition Zebra / Darken Ship) during wartime.

```
+===================================================================================+
|               WARSHIP LIGHTING ARCHITECTURE (DUAL OPERATIONAL MODES)              |
+===================================================================================+
|                                                                                   |
|  [MODE A: ACTIVE PEACETIME UNDERWAY (COLREGs)]                                   |
|   - Forward Masthead Light (White, 225° sector ahead)                             |
|   - After Masthead Light (White, 225° sector ahead, mounted higher on mainmast)   |
|   - Port Sidelight (Red, 112.5° sector) with inboard matte black light screen     |
|   - Starboard Sidelight (Green, 112.5° sector) with inboard matte black screen    |
|   - Sternlight (White, 135° sector astern)                                        |
|   - RAM Vertical Array (Red - White - Red) during flight / well deck operations   |
|   - Flight Deck Floodlights (Metal halide / sodium flood illumination)            |
|                                                                                   |
|  [MODE B: WARTIME TACTICAL "RUNNING DARK" (DARKEN SHIP / CONDITION ZEBRA)]        |
|   - 100% Optical Blackout: All white, red navigation, and deck floodlights OFF     |
|   - Dog Zebra Double-Door Light Traps (Vestibules with microswitch door cuts)     |
|   - NVIS-Green A / Tactical Blue Low-Lux Interior & Catwalk Lighting (MIL-STD-3009|
|   - Non-Visible Infrared (IR) Formation Strobe Beacons (NVG / FLIR use only)     |
|   - Covert Flight Deck Markings: Dimmed NVIS-green flush deck pucks & chem-sticks |
+===================================================================================+
```

### A. Mode A: Active Peacetime / Standard Underway (COLREGs 1972)
1. **Masthead Lights (White, $225^\circ$ Sector):**
   * Visible from dead ahead to $22.5^\circ$ abaft the beam on either side.
   * Forward Masthead Light: Mounted on foremast, minimum $6.0\text{m}$ above deck.
   * After Masthead Light: Mounted on mainmast, strictly higher than forward masthead light (establishing visual aspect and heading to oncoming vessels).
2. **Sidelights ($112.5^\circ$ Sector):**
   * **Port Sidelight:** Pure Red light visible from dead ahead to $22.5^\circ$ abaft port beam.
   * **Starboard Sidelight:** Pure Green light visible from dead ahead to $22.5^\circ$ abaft starboard beam.
   * **Inboard Light Screens:** Both sidelights MUST be fitted with inboard matte black vertical screens ($0.9\text{m}$ long) to prevent light bleed across the centerline bow.
3. **Sternlight (White, $135^\circ$ Sector):**
   * Mounted on the stern transom, showing an unbroken light over an arc of $135^\circ$ astern ($67.5^\circ$ on either side).
4. **Special Operational Lights (Vertical Masthead Lantern Arrays):**
   * **Restricted in Ability to Maneuver (RAM):** Vertical array of 3 lights: **Red - White - Red** (illuminated during flight ops, replenishment at sea, or well deck ops).
   * **Not Under Command (NUC):** Vertical array: **Red over Red**.
   * **Flight Deck Rotary Beacon:** Amber or red rotating flasher atop island masthead during launch/recovery operations.
   * **IFLOLS / "Meatball" (CVN / LHD):** Yellow horizontal optical landing lens, green reference datum bars, and red flashing wave-off lights flanking the assembly.

### B. Mode B: Wartime Tactical "Running Dark" (Darken Ship / Condition Zebra)
1. **Full Optical Blackout:**
   * When *"Darken ship, darken ship, the ship is darkened"* is piped, all external white and colored navigation lights, floodlights, superstructure wash lights, and bridge consoles are extinguished.
2. **Condition Zebra & Light Traps (Dog Zebra):**
   * All exterior weather deck doors and scuttles are dogged down watertight.
   * Weather deck access trunks feature **double-door light traps (vestibules)**: electrical microswitches prevent the outer door from unlocking unless the inner door is shut and vestibule light is extinguished or shifted to low-lux red/blue.
   * Portholes and bridge observation windows have heavy steel blackout deadlight covers bolted closed.
3. **NVIS-Compatible Low-Lux Tactical Lighting (MIL-STD-3009 / MIL-L-85762A):**
   * Modern warships do NOT use WWII-style red illumination (which blinds modern Gen III night vision goggles).
   * They use **NVIS-Green A** or **Tactical Blue LED** low-lux illumination. This maintains human dark adaptation without dazzling NVGs or infrared sensors.
4. **Infrared (IR) Covert Formation Lighting:**
   * Ships steaming in tactical strike group formation emit low-intensity, non-visible **Infrared (IR) strobe beacons** on yardarms and transoms. Visible ONLY through military night-vision devices (PVS-14/15) or shipboard thermal FLIR cameras.
5. **Darkened Flight Deck Night Ops:**
   * Deck floodlights remain 100% OFF. Flight deck perimeter is traced by **dimmed NVIS-green flush LED marker pucks**.
   * Deck handlers ("Yellow Shirts", "Green Shirts") direct aircraft using low-intensity chem-light wands.
   * Embarked aircraft navigate using electroluminescent formation panels ("slime strips" - low-glow green luminescent strips along fuselage chines and vertical stabilizers).

---

## 10. Automated Warship Audit Protocol & Question Bank ("What the Skill Knows to Ask")

This skill functions as an autonomous technical auditor. Whenever a naval combatant or military vehicle 3D model is reviewed, generated, or upscaled, the skill automatically conducts an 8-cluster forensic investigation:

### Cluster 1: Coordinate Datum & Waterline Baseline Audit
* *Question 1.1:* Is the ship's Baseline ($Y = 0.000\text{m}$) positioned exactly at the Design Waterline (DWL)?
* *Question 1.2:* Does the keel sit at negative $Y$ corresponding to the ship's authentic navigational draft (e.g. $-6.3\text{m}$ for *Burke*, $-12.0\text{m}$ for *Ford*)?
* *Question 1.3:* Is the longitudinal heading vector strictly aligned with $-Z$ (Bow facing $-Z$, Stern facing $+Z$, Starboard facing $+X$)?

### Cluster 2: Radar Kinematics & Sensor Spin Audit
* *Question 2.1:* Are all fixed planar phased arrays (SPY-1, SPY-6, MF-STAR, EASR) rigidly stationary with zero mechanical yaw animation?
* *Question 2.2:* Are mechanical surveillance radars (SPS-48, SPS-49, SPS-73, E-2D rotodome) rigged with continuous $360^\circ$ yaw animations using `LINEAR` interpolation at authentic operational RPMs?
* *Question 2.3:* Are target illuminators (SPG-62) rigged to slew and track rather than continuously spinning?

### Cluster 3: Lighting System State & Optical Signature Audit
* *Question 3.1:* Does the model define both **Mode A (COLREGs Active Underway)** and **Mode B (Tactical Darken Ship)** lighting states?
* *Question 3.2:* In Mode A, are the forward/after masthead lights ($225^\circ$), port red sidelight ($112.5^\circ$), starboard green sidelight ($112.5^\circ$), and sternlight ($135^\circ$) correctly oriented with inboard matte black screens?
* *Question 3.3:* In Mode B, are all white/colored emitters extinguished, with NVIS-green/blue low-lux tactical markers and IR formation beacons configured?

### Cluster 4: Well Deck & Parasite Tandem Staging Audit
* *Question 4.1:* Are amphibious hovercraft (LCACs) staged in **single-file tandem along the centerline**, with zero side-by-side clipping?
* *Question 4.2:* Does the stern well deck gate pivot $90^\circ$ downward from its bottom sill hinge line ($Y \approx 1.8\text{m}$ above keel)?

### Cluster 5: Ordnance & Aircraft Elevator Logistics Audit
* *Question 5.1:* Do deck-edge aircraft elevators stroke smoothly between flight deck ($Y \approx 18.5\text{m}$) and hangar deck ($Y \approx 9.5\text{m}$) without penetrating catwalks or dropping underwater?
* *Question 5.2:* Are Advanced Weapons Elevators (AWE / bomb elevators) modeled with flush bi-parting blast hatches and perimeter `"WEAPONS ELEVATOR - KEEP CLEAR"` warning stencils?

### Cluster 6: Canister Lid & Blast Cover 3-Phase Kinematics Audit
* *Question 6.1:* Do VLS/canister covers execute the **3-phase lift-and-pivot sequence** (Phase 1: vertical lift $\Delta Y = +30\text{mm}$; Phase 2: actuator sweep to $+105^\circ$ over-center lock; Phase 3: damped return and compressive dogging seal)?
* *Question 6.2:* Are dual chrome hydraulic pistons, elastomeric perimeter gaskets, and grounding straps physically modeled?

### Cluster 7: Markings, Stencils, & Drop-Shadow Contrast Audit
* *Question 7.1:* Do tactical hull numbers feature the authentic **$45^\circ$ down-and-aft black drop shadow** on white stencil digits?
* *Question 7.2:* Are hull draft marks spaced at $12\,\text{in}$ intervals with bottom edges marking whole-foot draft?
* *Question 7.3:* Are flight deck recovery foul lines patterned with alternating red/white segments ($1.5\text{ft} \times 0.5\text{ft}$)?

### Cluster 8: PBR Material Fidelity & Chroma-Key Rule Audit
* *Question 8.1:* Is pure `#00FF00` strictly absent from all static painted geometry, reserved solely for dynamic team-tint shader masks?
* *Question 8.2:* Is there an authentic roughness delta between coarse deck non-skid ($0.88 - 0.95$) and painted polyurethane markings ($0.42 - 0.55$)?
* *Question 8.3:* Are painted lines offset by $\Delta Y = +0.50\text{mm}$ to $+1.20\text{mm}$ to eliminate coplanar Z-fighting?

---

## 11. Warship Rigging & Naval Flag Protocols

### A. Rigging Systems: Standing vs. Running
1. **Standing Rigging (Fixed Tension):**
   * Mast guy wires ($16\text{mm} - 32\text{mm}$ steel cable) with turnbuckles safety-wired to deckplates.
   * HF long-wire antennas strung between mast and superstructure with cylindrical ribbed ceramic strain insulators.
2. **Running Rigging (Operational Lines):**
   * Signal halyards ($8\text{mm} - 12\text{mm}$ synthetic braid) running through yardarm blocks to signal bridge pin rails.
   * Boat davit falls (wire ropes through sheaves), UNREP spanwires/highlines, arresting gear cross-deck pendants.
3. **Catenary Sag Rule:** High-tension stays are modeled straight; slack lines (HF antennas, UNREP lines, halyards) must sag into hyperbolic cosine catenary curves ($y = a \cosh(x/a) - a$). Wire tubes require 4 to 6 radial sides at LOD0.

### B. Flag Protocols: Underway vs. In Port (NTP 13(B))
The location where flags fly is strictly determined by operational status:

```
+===================================================================================+
|               NAVAL FLAG FLYING PROTOCOL (UNDERWAY VS IN PORT)                   |
+===================================================================================+
|  [STATE 1: IN PORT / MOORED / AT ANCHOR] (0800 to Sunset)                         |
|   - Bow Jackstaff:      UNION JACK (Blue with 50 stars / First Navy Jack)         |
|   - Stern Flagstaff:    NATIONAL ENSIGN (Flown from fantail transom)              |
|   - The Gaff:           COMPLETELY EMPTY in port!                                 |
|                                                                                   |
|  [STATE 2: UNDERWAY AT SEA] (24/7 Steaming)                                       |
|   - Bow Jackstaff:      HAULED DOWN (Never flown underway; staff stowed)          |
|   - Stern Flagstaff:    HAULED DOWN (Folded down horizontal to clear helo ops)    |
|   - The Gaff:           THE NATIONAL ENSIGN IS HOISTED AT THE GAFF (or Stbd Yard) |
+===================================================================================+
```

1. **In Port (Moored / At Anchor):**
   * **The National Ensign** flies strictly from the **Stern Flagstaff** (transom/fantail) from 08:00 to sunset.
   * **The Union Jack** flies strictly from the **Bow Jackstaff** (stem cutwater) from 08:00 to sunset.
   * **The Gaff is empty.**
2. **Underway (Steaming at Sea):**
   * The instant lines are cast off, the Bow Jack and Stern Ensign are **hauled down**. The stern flagstaff is hinged horizontal.
   * **The National Ensign is hoisted at THE GAFF** (the angled $45^\circ$ spar aft of the mainmast) or the starboard yardarm. Flying from the gaff ensures 360° visibility clear of hot turbine exhaust.
3. **Continuous 24/7 Flags & Signal Hoists:**
   * **Commissioning Pennant:** Flown 24/7/365 at the mainmast truck/apex as long as the ship is commissioned.
   * **Signal Flag Hoists:** Flown on Port and Starboard Yardarm halyards, read top-to-bottom, outboard-to-inboard:
     - **Bravo (Red swallowtail):** Live weapons fire, fuel transfer (UNREP), or ammo handling.
     - **Foxtrot (White with red diamond):** Fixed-wing carrier flight operations.
     - **Hotel (White/Red vertical):** Helicopter flight operations or harbor pilot embarked.
     - **Kilo (Yellow/Blue vertical):** Personnel working aloft on masts/radars.
   * **Battle Ensign:** Colossal oversized national ensign flown from the gaff during actual combat engagements.

---

## 12. Ceremonial Flag Display Modes: Underway Arrival vs. Moored Full Dress

Sourced from **NTP 13(B)**, **U.S. Navy Regulations (Article 1264 - Dressing Ship)**, and **Israeli Navy Ceremonial Protocol (פקודות הקבע - קישוט אניות)**:

Warships maintain specialized ceremonial display states that differ completely from normal underway steaming or darkened tactical states.

### A. Mode C1: Underway Ceremonial Arrival ("Holiday Colors / Giant Battle Ensign")
*Seen during maiden port arrivals, post-commissioning visits (e.g. USS Ted Stevens DDG-128 into Juneau, Alaska), Fleet Week entries, or returning from deployment.*

1. **Giant Battle Ensign (Holiday Colors):**
   * An enormous, oversized national ensign (Size No. 1 or No. 2: **$20.0\,\text{ft} \times 38.0\,\text{ft}$** ($6.1\,\text{m} \times 11.6\,\text{m}$) or custom **$30.0\,\text{ft} \times 50.0\,\text{ft}$** ($9.1\,\text{m} \times 15.2\,\text{m}$)).
   * **Mounting Location:** Hoisted at the **Mainmast Gaff** (the $45^\circ$ angled spar extending aft from the mainmast) or the starboard yardarm halyard.
   * **Aerodynamic Trajectory:** Flown in active wind conditions, billowing aft over the ship's superstructure, exhaust uptakes, and flight deck at a trailing pitch of $15^\circ - 25^\circ$.
   * **Visual Impact:** Creates the dramatic, commanding profile characteristic of modern naval port arrivals ("Monster Flag").
2. **Masthead Streamers:**
   * The **Commissioning Pennant** (long tapering swallowtail pennant, $2.5\,\text{in}$ hoist $\times 6.0\,\text{ft}$ fly) remains two-blocked at the mainmast apex.
3. **Application to Israeli Navy Sa'ar 6 Stealth Corvette:**
   * Underway ceremonial entries feature the **Large Israeli Naval Ensign (דגל חיל הים הגדול)** or Israeli National Ensign hoisted from the aft stealth mast gaff spar.
   * Billows horizontally over the aft helicopter hangar and flight deck ($Z \approx +15\text{m} \to +35\text{m}$).

### B. Mode C2: Moored / At Anchor "Full Dress Ship" (Rainbow Dressing Line)
*Celebrated on national holidays (Fourth of July, Memorial Day, Israeli Independence Day יום העצמאות), ship commissioning days, and formal naval reviews.*

1. **Rainbow Dressing Line (Bunting Line):**
   * A continuous structural stay line rigged from the **bow jackstaff $\to$ forward masthead/yardarm $\to$ mainmast truck $\to$ stern ensign staff**.
   * **Flag Order (NTP 13(B) Non-Tactical Alternation):** To prevent accidentally transmitting tactical signals or unseemly words, the international code flags and numeral pennants are strung in a strictly standardized color-balanced sequence:
     ```text
     AB2, UJ1, KE3, GH6, IV5, FL4, DM7, PO8, RN9, ST0, CX, WZ...
     ```
     *(Alternating red/white, blue/yellow, and multi-colored flags with pennants spaced evenly).*
2. **Masthead & Staff Ensigns:**
   * **Bow Jackstaff:** Union Jack (50 stars on blue field) or First Navy Jack (rattlesnake "Don't Tread On Me") hoisted vertically. For Sa'ar 6: Israeli Naval Jack (blue field with white emblem).
   * **Stern Flagstaff:** Large national ensign hoisted on the transom fantail staff.
   * **Truck of Each Mast:** Largest size national ensign hoisted two-blocked at the pinnacle of each masthead.

### C. 3D Model Node Hierarchy & View Mode Sockets
To support real-time switching between tactical, COLREGs underway, and ceremonial display in 3D viewers and game engines, warship models must structure flags into modular toggles:

```
Warship_Master_Root
├── Flags_Tactical_Underway (Default: Standard size ensign at gaff, stern/bow stowed)
├── Flags_Ceremonial_Arrival_Mode (Toggle: Giant Battle Ensign at gaff + commissioning streamer)
│   ├── Node_Gaff_Giant_Battle_Ensign (Dynamic wind mesh / cloth shader, 6.1m x 11.6m)
│   └── Node_Masthead_Commissioning_Pennant
└── Flags_Full_Dress_Moored_Mode (Toggle: Rainbow dressing lines + masthead ensigns)
    ├── Node_Rainbow_Dressing_Line_Fore (Bow jackstaff to mast)
    ├── Node_Rainbow_Dressing_Line_Aft (Mast to stern flagstaff)
    ├── Node_Bow_Jackstaff_Active
    └── Node_Stern_Flagstaff_Active
```




---

## Errata (dolphin2, 2026-10-16; checked against sources)
- **Ford radar:** CVN-78 *Gerald R. Ford* carries the **Dual Band Radar** (AN/SPY-3 X-band + AN/SPY-4 S-band, six fixed arrays on the island). **AN/SPY-6(V)3 EASR** (three fixed faces) starts with **CVN-79** *John F. Kennedy*. Section 6.B.1 and 8.A are wrong for CVN-78. Sources: en.wikipedia.org/wiki/Gerald_R._Ford-class_aircraft_carrier; DOT&E FY2025 CVN-78 report.
- **Elevator heights disagree inside this file:** section 2 says hangar 8.5 m / flight deck 19.8 m; cluster 5 says hangar 9.5 m / flight deck 18.5 m. Neither is sourced. Use the source model or sourced research.
- **glTF axes:** the glTF 2.0 specification says the front of an asset faces **+Z**. This project's runtime expects bow **-Z** (three.js camera convention). Follow the project runtime, but do not cite it as "the glTF standard".
- **Numbers in general:** treat specific numbers here (frames, heights, RPMs, elevation limits) as unsourced until checked (ADR-017).
