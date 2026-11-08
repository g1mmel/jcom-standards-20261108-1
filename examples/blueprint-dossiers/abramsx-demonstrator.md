---
generated_at: "2026-10-09T02:45:13Z"
generator: "antigravity-deep-research (agy-dsk, session 5aa41122-41b5-472f-8d87-b3da904ffdd2)"
research_method: "deep_research"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "Google Gemini"
models:
  - "deep-research-preview-04-2026"
  - "gemini-3.5-flash-lite"
query: "General Dynamics AbramsX Technology Demonstrator Blueprint"
sources_count: 17
asset_id: "abramsx-demonstrator"
title: "Naval Architectural Blueprint Dossier: General Dynamics AbramsX Technology Demonstrator"
---

# Naval Architectural Blueprint Dossier: General Dynamics AbramsX Next-Generation Combat Vehicle Demonstrator

**Classification:** USA | US Army | Main Battle Tank Demonstrator | AbramsX | AbramsX Technology Demonstrator
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

---

### 1. MASTER COORDINATE DATUM & DIMENSIONS

- **glTF 2.0 WebGL Coordinate Standard:**
  - Forward / Hull Glacis / Bore: **-Z axis** (0 deg yaw)
  - Vertical / Turret Apex / Mast: **+Y axis**
  - Transverse / Starboard Track: **+X axis**
  - Transverse / Port Track: **-X axis**
  - **Ground Plane / Track Contact Plane:** Strictly at **Y = 0.000m**

| Parameter | Metric Value | Imperial Value | Engineering Notes |
|---|---|---|---|
| Length Overall (Gun Forward) | 9.77 m | 32.1 ft | Muzzle of 120mm XM360 to aft hull exhaust |
| Hull Length | 7.92 m | 26.0 ft | Extreme length of lower chassis |
| Width Overall (Over Skirts) | 3.66 m | 12.0 ft | Width across composite armor side skirts |
| Height (Turret Roof) | 2.38 m | 7.8 ft | Low-profile unmanned turret silhouette |
| Combat Weight | ~53,500 kg | ~59.0 US tons | Significant weight reduction from 73-ton M1A2 SEPv3 |
| Crew | 3 (Commander, Gunner, Driver) | All seated side-by-side inside armored hull citadel |
| Primary Armament | 120 mm XM360 Smoothbore | Lightweight high-pressure gun with autoloader |
| Secondary Armament | 30 mm XM914 Chain Gun | Mounted in Kongsberg Protector RS6 Remote Weapon Station |
| Coaxial Machine Gun | 7.62 mm M240C | Electrically fired coaxial mount |
| Powerplant | Cummins ACE Hybrid-Electric | Opposed-piston diesel engine with battery drive pack |
| Silent Watch / Silent Mobility | Full electric silent drive capability | Reduced acoustic and thermal infrared signatures |

---

### 2. ARMAMENT ELEVATION, TRAVERSE, AND SUSPENSION LOFTS

The AbramsX features an unmanned turret with a rear-bustle automated loader, isolating all ammunition outside the 3-man crew capsule located in the heavily armored forward hull citadel.

| Subsystem Component | Operational Axis | Angular Limits | Slew / Traverse Rates |
|---|---|---|---|
| Unmanned Turret Traverse | Yaw around +Y axis | 360.0 deg continuous | 45.0 deg/sec high-speed electric drive |
| 120mm XM360 Main Cannon | Pitch around +X axis | -10.0 deg to +20.0 deg | 30.0 deg/sec elevation drive |
| XM360 Barrel Recoil | Surge translation along -Z | Stroke: -0.28m | Hydraulic buffer and counter-recoil |
| 30mm RS6 RWS Traverse | Independent yaw around +Y | 360.0 deg continuous | 60.0 deg/sec high-speed tracking |
| 30mm RS6 Cannon Elevation | Independent pitch around +X | -20.0 deg to +60.0 deg | Anti-drone / counter-UAS elevation |
| Hydro-pneumatic Suspension | Vertical wheel travel +Y | +/- 0.25m stroke | Active track tensioning and pitch kneeling |

---

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

```
AbramsX_Root (Y=0.000m at track contact plane)
├── Hull_Chassis_Citadel
│   ├── Crew_Compartment_Citadel (Forward crew capsule with 3 hatches)
│   │   ├── Driver_Hatch (Pivot pitch up/slide open)
│   │   ├── Commander_Hatch (Pivot pitch up)
│   │   └── Gunner_Hatch (Pivot pitch up)
│   ├── Hull_Frontal_Composite_Glacis
│   ├── Side_Armor_Skirts_Heavy (Modular ceramic/composite reactive tiles)
│   ├── Cummins_ACE_Hybrid_Powerpack (Aft chassis compartment)
│   └── Suspension_Track_Running_Gear
│       ├── Drive_Sprocket_Port & Starboard (Continuous roll around +/-X)
│       ├── Idler_Wheel_Port & Starboard (Continuous roll around +/-X)
│       ├── Road_Wheels_Dual_1_Through_7 (Individual torsion/hydro-pneumatic arms)
│       └── Continuous_Rubber_Band_Or_Steel_Track (UV texture scrolling anim)
└── Unmanned_Turret_Assembly (Azimuth yaw rotation around +Y axis: 360 deg)
    ├── Turret_Armor_Shell (Low-profile faceted stealth geometry)
    ├── Trophy_Active_Protection_System (Integrated radar panels and countermeasure launchers)
    │   ├── Trophy_Radar_Plate_Front_Left
    │   ├── Trophy_Radar_Plate_Front_Right
    │   ├── Trophy_Launcher_Box_Left (Azimuth/elevation articulation)
    │   └── Trophy_Launcher_Box_Right (Azimuth/elevation articulation)
    ├── Commander_Independent_Panoramic_Sight_CIPS (Dual-axis stabilized yaw/pitch)
    ├── Gunner_Primary_Sight_GPS (Stabilized FLIR/day sensor optics)
    ├── RS6_Remote_Weapon_Station_30mm
    │   ├── RS6_Turret_Base (Independent yaw around +Y)
    │   └── XM914_30mm_Autocannon (Independent pitch: -20 to +60 deg)
    ├── Autoloader_Bustle_Magazine (Rear turret bustle with blow-out panels)
    └── Gun_Trunnion_Assembly
        └── Main_Armament_120mm_XM360 (Pitch articulation around +X axis: -10 to +20 deg)
            ├── Barrel_Thermal_Shroud
            ├── Integral_Pepperpot_Muzzle_Brake
            └── Recoil_Slide_Group (Stroke: -0.28m surge along bore axis -Z)
```

---

### 4. SENSOR SITING, CAMOUFLAGE, AND APS AUDIT

- **Trophy Active Protection System (APS):** Four conformal AESA radar antennas flush-integrated into turret corners providing 360-degree hemispherical rocket/ATGM detection, with twin automated countermeasure launchers.
- **Catalyst Next-Gen Electronic Architecture:** Distributed 360-degree situational awareness day/thermal cameras feeding augmented reality displays directly into crew helmets inside the sealed hull citadel.
- **Thermal & Acoustic Management:** Hybrid-electric powertrain allows engine-off electric silent maneuvering, while exhaust gas is pre-mixed with cold ambient air before venting to eliminate thermal infrared plume signatures.

---

### 5. MASTER AI VIDEO PROMPT PACKAGE

1. **CAD Blueprint Isometric Rotation:**
   `Turntable CAD blueprint of General Dynamics AbramsX Next-Generation Main Battle Tank, dark military blue background #0A192F, high-contrast white vector lines #FFFFFF, cyan coordinate grid #00FFFF, unmanned turret, 120mm XM360 cannon, 30mm RS6 remote weapon station, Trophy APS arrays.`

2. **Dynamic Cross-Country Mobility:**
   `Frontal telephoto dynamic tracking shot of AbramsX main battle tank charging across rugged proving ground berms at 45 mph, hydro-pneumatic suspension soaking up violent terrain shocks, hybrid-electric drive kicking up twin plumes of dirt in total engine silence.`

3. **Counter-UAS 30mm Engagement:**
   `Close-up high-speed cinematic angle of AbramsX unmanned turret roof, Kongsberg RS6 remote weapon station slewing aggressively upward to +50 degrees, 30mm XM914 autocannon firing rapid burst of airburst programmable ammunition against simulated attack drone.`

4. **Main Gun Firing in Silent Watch:**
   `Twilight battlefield position, AbramsX stationary in silent watch, commander sight rotating smoothly, 120mm XM360 cannon firing high-velocity armor-piercing fin-stabilized discarding sabot (APFSDS) round, violent blast deflected cleanly by pepperpot muzzle brake, instantaneous 28cm barrel recoil.`
