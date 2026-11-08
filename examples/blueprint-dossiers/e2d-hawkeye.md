---
generated_at: "2026-10-09T02:45:12Z"
generator: "antigravity-deep-research (agy-dsk, session 5aa41122-41b5-472f-8d87-b3da904ffdd2)"
research_method: "search"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "Google Gemini"
models:
  - "deep-research-preview-04-2026"
  - "gemini-3.5-flash-lite"
query: "Northrop Grumman E-2D Advanced Hawkeye Blueprint and Kinematics"
sources_count: 16
asset_id: "e2d-hawkeye"
title: "Naval Architectural Blueprint Dossier: Northrop Grumman E-2D Advanced Hawkeye"
---

# Naval Architectural Blueprint Dossier: Northrop Grumman E-2D Advanced Hawkeye Airborne Early Warning Aircraft

**Classification:** USA | US Navy | Carrier Airborne Early Warning and Control (AEW&C) | E-2 Hawkeye | E-2D
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

---

### 1. MASTER COORDINATE DATUM & DIMENSIONS

- **glTF 2.0 WebGL Coordinate Standard:**
  - Forward / Nose Heading: **-Z axis** (0 deg yaw)
  - Vertical / Dorsal Apex / Rotodome: **+Y axis**
  - Transverse / Starboard Wingtip: **+X axis**
  - Transverse / Port Wingtip: **-X axis**
  - **Ground Plane / Weight-on-Wheels:** Strictly at **Y = 0.000m**

| Parameter | Metric Value | Imperial Value | Engineering Notes |
|---|---|---|---|
| Length Overall (LOA) | 17.60 m | 57.7 ft | Nose radome to tail empennage trailing edge |
| Wingspan (Extended) | 24.56 m | 80.6 ft | High-aspect trapezoidal wing planform |
| Wingspan (Folded) | 8.94 m | 29.3 ft | Outboard wing panels folded 105 deg aft |
| Height Over Rotodome (+Y) | 5.58 m | 18.3 ft | Ground baseline to rotodome dorsal crown |
| Rotodome Diameter | 7.32 m | 24.0 ft | Pylon-mounted aerodynamic saucer radome |
| Maximum Takeoff Weight (MTOW) | 26,083 kg | 57,500 lbs | Catapult launch structural maximum |
| Empty Weight | 18,364 kg | 40,485 lbs | Operational baseline |
| Propulsion | 2x Rolls-Royce T56-A-427A | 5,100 shp each | Constant-speed turboprop engines |
| Propellers | 2x NP2000 8-bladed scimitar | 4.11 m dia | Digitally controlled composite blades |

---

### 2. FLIGHT CONTROL SURFACES & WING STATION LOFTS

The airframe comprises high-aspect trapezoidal wings with hydraulic wing-fold hinges located at outboard nacelle stations (X = +/- 4.47m). Quadruple vertical stabilizers (triple rudders) provide directional stability in the prop-wash wake.

| Wing Station | Transverse X (m) | Chord (m) | Thickness-to-Chord | Incidence | Dihedral |
|---|---|---|---|---|---|
| Fuselage Centerline | 0.00 | 4.25 | 15.0% | +3.0 deg | +0.0 deg |
| Nacelle Inboard Sill | +/- 3.10 | 3.80 | 14.5% | +2.5 deg | +3.5 deg |
| Wing Fold Hinge Axis | +/- 4.47 | 3.45 | 14.0% | +2.0 deg | +3.5 deg |
| Mid-Span Aileron Sill | +/- 8.50 | 2.55 | 13.0% | +1.0 deg | +3.5 deg |
| Starboard / Port Wingtip | +/- 12.28 | 1.65 | 12.0% | +0.0 deg | +3.5 deg |

---

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

```
Airframe_Root (Y=0.000m at tire contact)
├── Fuselage_Main_Body
│   ├── Canopy_Cockpit_Glazing
│   ├── Nose_Radome_AN_APY9_Forward
│   ├── Crew_Entry_Door_Port (Door hinge roll: +X swing)
│   ├── Rotodome_Pylon_Mast (+Y = 3.65m)
│   │   └── Rotodome_AN_APY9 (Continuous yaw roll around +Y axis, 6 RPM, 360 deg)
│   ├── Arresting_Hook_Assembly (Pivot pitch around +X: stowed -Z 0 deg, extended -60 deg)
│   └── Tail_Bumper_Skid
├── Landing_Gear_Nose
│   ├── Nose_Strut_Oleo (Pneumatic travel: 0.22m along +Y)
│   ├── Nose_Wheels_Dual (Continuous pitch roll around +X)
│   └── Catapult_Launch_Bar (Carrier shuttle link, pitch articulation -45 deg)
├── Landing_Gear_Main_Port & Starboard
│   ├── Main_Gear_Oleo_Struts (Travel: 0.35m along +Y)
│   └── Main_Wheels_Single (Roll around +/-X)
├── Center_Wing_Carrythrough
│   ├── Engine_Nacelle_Port (Rolls-Royce T56-A-427A)
│   │   └── Propeller_NP2000_Port (8 composite blades, continuous roll around -Z, counter-clockwise)
│   └── Engine_Nacelle_Starboard (Rolls-Royce T56-A-427A)
│       └── Propeller_NP2000_Starboard (8 composite blades, continuous roll around -Z, clockwise)
├── Wing_Outer_Fold_Port (Hinge roll: 105 deg upward and aft stowage along fuselage flank)
│   ├── Flap_Fowler_Port (Travel: +Y/-Z track deflection 0-40 deg)
│   └── Aileron_Port (Pitch articulation +/- 25 deg)
├── Wing_Outer_Fold_Starboard (Hinge roll: 105 deg upward and aft stowage)
│   ├── Flap_Fowler_Starboard (Deflection 0-40 deg)
│   └── Aileron_Starboard (Pitch articulation +/- 25 deg)
└── Empennage_Assembly
    ├── Horizontal_Stabilizer_Main
    ├── Vertical_Fin_Outboard_Port (Rudder active yaw: +/- 30 deg)
    ├── Vertical_Fin_Inboard_Port (Fixed stabilizer)
    ├── Vertical_Fin_Inboard_Starboard (Rudder active yaw: +/- 30 deg)
    └── Vertical_Fin_Outboard_Starboard (Rudder active yaw: +/- 30 deg)
```

---

### 4. SENSOR SITING & AVIONICS RF AUDIT

- **Primary Mission Sensor:** Lockheed Martin AN/APY-9 UHF Active Electronically Scanned Array (AESA) housed within the 24-foot dorsal rotodome. Provides 360-degree air and maritime surface surveillance with Space-Time Adaptive Processing (STAP).
- **Secondary Surveillance:** AN/APX-122A IFF interrogator system co-located inside rotodome array.
- **ALQ-217 Electronic Support Measures (ESM):** Four bilaterally sited ESM quadrant antennas providing 360-degree ELINT coverage:
  - Nose radome chine antennas (Port/Starboard forward)
  - Tail cone empennage antenna (Aft hemispace)
- **Cooperative Engagement Capability (CEC):** Planar antenna array flush-mounted beneath lower fuselage forward of tail bumper skid.

---

### 5. MASTER AI VIDEO PROMPT PACKAGE

1. **CAD Blueprint Isometric Rotation:**
   `Cinematic orthographic wireframe turn of Northrop Grumman E-2D Advanced Hawkeye, navy blue backdrop #0A192F, clean white architectural lines #FFFFFF, cyan datum grid #00FFFF, 24ft dorsal rotodome, 8-bladed NP2000 propellers, technical carrier aviation schematics.`

2. **Carrier Deck Launch & Mechanical Articulation:**
   `USS Gerald R. Ford CVN-78 flight deck, Northrop Grumman E-2D Advanced Hawkeye unhurriedly unfolding outer wings at cat 2, NP2000 8-blade scimitar props spinning smoothly, launch bar seating into EMALS shuttle, catapult steam and blast deflector raised.`

3. **Rotodome Radar Operation Close-Up:**
   `Extreme telephoto close-up of Northrop Grumman E-2D Advanced Hawkeye dorsal rotodome turning at 6 RPM in clear flight over open ocean, pristine composite texture, stenciled caution placards, heat shimmer from twin Rolls-Royce turboprop nacelles.`

4. **Arrested Night Landing Recovery:**
   `Carrier twilight recovery of E-2D Advanced Hawkeye, NVIS green deck luminescent markings, tailhook engaging 3-wire cross deck pendant with kinetic arrest tension, twin main gear compressing smoothly onto deck non-skid.`
