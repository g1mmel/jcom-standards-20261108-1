---
generated_at: "2026-10-09T02:46:12Z"
generator: "antigravity-deep-research (agy-dsk, session 5aa41122-41b5-472f-8d87-b3da904ffdd2)"
research_method: "deep_research"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "Google Gemini"
models:
  - "deep-research-preview-04-2026"
  - "gemini-3.5-flash-lite"
query: "Rafael C-Dome Point Defense Naval VLS Blueprint and Kinematics"
sources_count: 16
asset_id: "rafael-c-dome"
title: "Naval Architectural Blueprint Dossier: Rafael C-Dome Point Defense Naval VLS"
---

# Naval Architectural Blueprint Dossier: Rafael C-Dome Point Defense Naval Vertical Launch System

**Classification:** Israel | Israeli Navy | Naval Air Defense System | C-Dome | C-Dome 40-cell VLS
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

---

### 1. MASTER COORDINATE DATUM & DIMENSIONS

- **glTF 2.0 WebGL Coordinate Standard:**
  - Forward / Ship Heading: **-Z axis** (0 deg yaw)
  - Vertical / Missile Egress Vector: **+Y axis**
  - Transverse / Starboard: **+X axis**
  - Transverse / Port: **-X axis**
  - **Forecastle Deck Level Mounting Plane:** Strictly at **Y = 0.000m**

| Parameter | Metric Value | Imperial Value | Engineering Notes |
|---|---|---|---|
| Cell Count | 40 vertical launch cells | 40-round modular canister array | Sa'ar 6 forward forecastle battery |
| Module Envelope Width (X) | 3.40 m | 11.2 ft | Transverse width across 40-cell matrix |
| Module Envelope Length (Z) | 2.80 m | 9.2 ft | Longitudinal depth forward of bridge |
| Penetration Below Deck (-Y)| 3.20 m | 10.5 ft | Depth of canister tubes beneath deck level |
| Interceptor Missile | Tamir Navalized | 3.0 m length, 160 mm dia | Active radar/electro-optical proximity seeker |
| Interceptor Mass | 90 kg | 198 lbs | Solid propellant rocket motor |
| Effective Range | 4,000 m to 70,000 m | 2.2 to 38.0 nautical miles | Multi-threat saturation defense |
| Reaction Time | < 1.0 second | Instantaneous vertical launch | 360-degree omnidirectional coverage |
| Launch Method | Vertical Hot Launch | Sealed frangible / hinged cell cover blowout |

---

### 2. VLS ARRAY CELL MATRIX & DECK INTEGRATION LOFTS

On the Sa'ar 6 corvette, the 40-cell C-Dome VLS is flush-integrated into the forward well deck directly abaft the Oto Melara 76/62 SR main gun and forward of the bridge superstructure bulwark.

| Grid Coordinate | Cell Pitch X (m) | Cell Pitch Z (m) | Cover Type | Gas Management |
|---|---|---|---|---|
| 4x10 Matrix | 0.32m spacing | 0.32m spacing | Rapid-reaction mechanical hatch | Central plenum gas exhaust duct |
| Vertical Egress Vector | Yaw 0 deg, Pitch +90 deg | Straight vertical +Y | Frangible blast composite cap | Flame deflector sill at base |

---

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

```
CDome_40Cell_VLS_Root (Y=0.000m at forecastle deck level)
├── Sub_Deck_Canister_Silo_Array (-Y=0.000m to -3.200m)
│   ├── Central_Exhaust_Gas_Plenum
│   ├── Flame_Deflector_Trough (V-shaped gas diverter sill)
│   └── Canister_Tubes_1_Through_40
│       └── Tamir_Interceptor_Missile_Canister
│           ├── Umbilical_Data_Cable_Release
│           └── Gas_Generator_Ejector
└── Deck_Level_Hatch_Array (Y=0.000m)
    ├── Silo_Hatches_Row_1_Through_4 (Pitch articulation: 90 deg vertical open)
    ├── Blast_Deflector_Coaming (Flush deck coaming sill)
    └── Missile_Launch_VFX_Sockets_1_Through_40
        ├── Egress_Vector_Direct (+Y vertical thrust socket)
        └── Plenum_Smoke_Exhaust_Sockets (Bilateral deck gas vents)
```

---

### 4. RADAR INTEGRATION & THREAT ENGAGEMENT AUDIT

- **MF-STAR Radar Integration:** C-Dome is slaved directly to the EL/M-2248 MF-STAR 4-face active electronically scanned array radar, which tracks hundreds of incoming low-RCS threats and transmits uplink mid-course correction data.
- **Simultaneous Target Engagement:** Can engage multiple incoming saturation salvos of anti-ship cruise missiles, precision-guided munitions, loitering kamikaze drones, and heavy artillery rockets concurrently.
- **RF Signature Flush Suppression:** Closed hatch covers sit perfectly flush with the radar-absorbent painted deck plates, preventing radar cavity returns.

---

### 5. MASTER AI VIDEO PROMPT PACKAGE

1. **CAD Blueprint Isometric Rotation:**
   `Turntable CAD blueprint of Rafael C-Dome 40-cell naval VLS, navy blue background #0A192F, stark white vector lines #FFFFFF, cyan coordinate grid #00FFFF, 40-cell vertical canister matrix, below-deck gas exhaust plenum, Tamir interceptor missile.`

2. **Vertical Salvo Launch Sequence:**
   `Dramatic low-angle view of Sa'ar 6 corvette forecastle at dusk, dual C-Dome hatches snapping open, two Tamir interceptor missiles erupting vertically from cells in rapid succession with brilliant white-orange rocket trails, instantaneous pitch-over toward incoming sea-skimming threat.`

3. **Multi-Drone Swarm Interception:**
   `Night naval combat perspective from warship bridge wing, C-Dome VLS launching rapid defensive ripple, missiles arcing across night sky, proximity airburst detonations destroying incoming hostile suicide drones over Mediterranean sea.`

4. **Forecastle Flush Deck Detail:**
   `Close-up technical tracking shot moving over the closed C-Dome 40-cell deck grid on Israeli corvette, non-skid stealth coating, stenciled Hebrew caution markings, recessed hydraulic hatch actuators.`
