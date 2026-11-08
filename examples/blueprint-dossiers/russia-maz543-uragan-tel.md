---
generated_at: "2026-10-09T02:45:42Z"
generator: "antigravity-deep-research (agy-dsk, session 5aa41122-41b5-472f-8d87-b3da904ffdd2)"
research_method: "search"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "Google Gemini"
models:
  - "deep-research-preview-04-2026"
  - "gemini-3.5-flash-lite"
query: "9K57 Uragan 9P140 MAZ-543M TEL Blueprint"
sources_count: 16
asset_id: "russia-maz543-uragan-tel"
title: "Naval Architectural Blueprint Dossier: 9K57 Uragan 9P140 220mm MLRS TEL (MAZ-543M)"
---

# Naval Architectural Blueprint Dossier: 9K57 Uragan 9P140 220mm Multiple Launch Rocket System TEL (MAZ-543M Chassis)

**Classification:** Russia | Russian Ground Forces | Multiple Launch Rocket System TEL | 9K57 Uragan | 9P140 TEL / MAZ-543M
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

---

### 1. MASTER COORDINATE DATUM & DIMENSIONS

- **glTF 2.0 WebGL Coordinate Standard:**
  - Forward / Cab / Road Travel: **-Z axis** (0 deg yaw)
  - Vertical / Launcher Apex / Roof: **+Y axis**
  - Transverse / Starboard Wheels: **+X axis**
  - Transverse / Port Wheels: **-X axis**
  - **Ground Contact Plane (8 Wheels):** Strictly at **Y = 0.000m**

| Parameter | Metric Value | Imperial Value | Engineering Notes |
|---|---|---|---|
| Length Overall (Travel Stowed) | 9.63 m | 31.6 ft | Heavy 8x8 chassis length bumper to tube rear |
| Chassis Width | 3.23 m | 10.6 ft | Width over heavy cross-country run-flat tires |
| Height (Travel Stowed) | 3.23 m | 10.6 ft | Ground plane to top of stowed rocket tube pack |
| Maximum Height (Elevated) | 5.80 m | 19.0 ft | Tube pack elevated to maximum +55 degrees |
| Combat Weight (Fully Loaded) | 42,700 kg | 94,137 lbs | Chassis, launcher, 16x 220mm rockets, 4 crew |
| Rocket Caliber | 220 mm | 8.66 inches | 9M27 series spin-stabilized artillery rockets |
| Number of Launch Tubes | 16 tubes | (4 rows of 4 tubes) | Tubular steel launcher bank |
| Firing Salvo Duration | 20 seconds | Full 16-round salvo discharge |
| Maximum Firing Range | 35,800 m | 22.2 miles | Standard 9M27F high-explosive fragmentation |
| Powerplant | V-12 Diesel D12A-525 | 525 hp | 38.88-liter heavy multi-fuel tank diesel engine |

---

### 2. ARTICULATION, FIRING SECTOR, AND STABILIZING JACK LOFTS

The 9P140 launcher mount is positioned on the rear deck of the MAZ-543M heavy 8x8 chassis. Two hydraulic stabilizer outrigger jacks deploy downward to the ground plane before firing to isolate chassis suspension.

| Subsystem Component | Operational Axis | Angular Limits | Slew Rate |
|---|---|---|---|
| Launcher Azimuth (Traverse) | Yaw around +Y axis | +/- 30.0 deg (Left / Right) | 6.0 deg/sec hydraulic slewing |
| Launcher Elevation (Pitch) | Pitch around +X axis | +5.0 deg to +55.0 deg | 5.0 deg/sec hydraulic cylinders |
| Rear Hydraulic Stabilizer Jacks (2x) | Vertical translation -Y | Stroke: 0.55m to ground | Hydraulic leveling jacks with foot pads |
| Chassis Steering Axles (1 & 2) | Yaw around +Y axis | +/- 28.0 deg steering | Dual front steering axle geometry |

---

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

```
MAZ543_9P140_Root (Y=0.000m at tire contact plane)
├── Chassis_MAZ543M_8x8
│   ├── Cab_Forward_Port (Driver & Commander cab with heavy blast-shield shutters)
│   │   ├── Cab_Door_Port (Pivot pitch open)
│   │   └── Blast_Shield_Shutters_Windshield (Armor shutters fold down over glass)
│   ├── Cab_Forward_Starboard (Crew station cab)
│   ├── V12_Diesel_D12A_Engine_Housing (Centered between forward cabs)
│   ├── Heavy_Frame_Chassis_Rails
│   ├── Hydraulic_Outrigger_Jack_Left (Vertical extension down to Y=0.000m)
│   ├── Hydraulic_Outrigger_Jack_Right (Vertical extension down to Y=0.000m)
│   └── Wheel_Suspension_Assemblies_8x8
│       ├── Front_Axle_1 (Steering yaw +/- 28 deg, independent torsion arms)
│       ├── Front_Axle_2 (Steering yaw +/- 22 deg, independent torsion arms)
│       ├── Rear_Axle_3 (Fixed tracking axle, independent torsion arms)
│       ├── Rear_Axle_4 (Fixed tracking axle, independent torsion arms)
│       └── Large_Cross_Country_Tires_8x (Continuous pitch roll +/-X)
└── Launcher_Assembly_9P140 (Turntable yaw rotation around +Y axis: +/- 30 deg)
    ├── Launcher_Base_Turntable
    ├── Operator_Firing_Sight_Pod
    └── Tube_Pack_Elevating_Cradle (Pitch articulation around +X axis: +5 to +55 deg)
        ├── Elevation_Hydraulic_Cylinders
        └── 16_Cell_220mm_Rocket_Tubes (4x4 matrix of 220mm launching tubes)
            ├── Tube_Locks_And_Detents
            └── Rocket_Launch_VFX_Sockets_1_Through_16 (Backblast and muzzle nodes)
```

---

### 4. SENSOR SITING & ARTILLERY FIRE CONTROL AUDIT

- **Panoramic Artillery Sight:** PG-1M panoramic collimator sight mounted on the left side of the elevating launcher cradle for optical laying in deflection and elevation.
- **Blast Protection System:** Heavy steel armor shutters deploy automatically over all forward cab windshields and side glazing to protect the crew from the violent thermal backblast of departing 220mm rockets.
- **All-Wheel Drive Independent Suspension:** Independent torsion bar suspension on all 8 wheels with central tire pressure regulation system (CTIS) allowing tire pressure drop for crossing soft sand or mud.

---

### 5. MASTER AI VIDEO PROMPT PACKAGE

1. **CAD Blueprint Isometric Rotation:**
   `Turntable CAD blueprint of Russian 9K57 Uragan 9P140 220mm MLRS on MAZ-543M 8x8 chassis, dark navy background #0A192F, crisp white vector linework #FFFFFF, cyan coordinate grid #00FFFF, twin split front cabs, 16-tube rocket launch pack elevated, rear hydraulic jacks.`

2. **Firing Position Emplacement:**
   `Tactical clearing in pine forest, MAZ-543M 8x8 heavy truck halting, twin heavy hydraulic stabilizer jacks deploying downward to press firmly into earth, blast shutters closing over front cab windows, 16-tube launcher elevating to +45 degrees.`

3. **Full 16-Round Rocket Salvo Discharge:**
   `Slow-motion side angle of 9P140 Uragan unleashing full 16-round 220mm artillery rocket salvo, massive sheets of orange rocket backblast churning dust and leaves, spin-stabilized rockets leaving tubes at 1-second intervals with fiery exhaust plumes.`

4. **8x8 Heavy Cross-Country Transit:**
   `Russian MAZ-543M Uragan heavy MLRS vehicle convoy plowing through deep autumn mud ruts at 30 mph, dual front steering axles turning in tandem, giant 8-wheel drive throwing rooster tails of mud.`
