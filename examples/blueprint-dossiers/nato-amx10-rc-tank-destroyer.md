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
query: "Nexter AMX-10 RC / RCR Tank Destroyer Blueprint"
sources_count: 17
asset_id: "nato-amx10-rc-tank-destroyer"
title: "Naval Architectural Blueprint Dossier: Nexter AMX-10 RC / RCR Armoured Reconnaissance Vehicle"
---

# Naval Architectural Blueprint Dossier: Nexter AMX-10 RC / RCR Armoured Reconnaissance Vehicle

**Classification:** France | French Army / NATO | Armoured Reconnaissance Vehicle / Tank Destroyer | AMX-10 RC | AMX-10 RCR
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

---

### 1. MASTER COORDINATE DATUM & DIMENSIONS

- **glTF 2.0 WebGL Coordinate Standard:**
  - Forward / Glacis / Bore Axis: **-Z axis** (0 deg yaw)
  - Vertical / Turret Apex: **+Y axis**
  - Transverse / Starboard Wheels: **+X axis**
  - Transverse / Port Wheels: **-X axis**
  - **Ground Contact Plane (Tires):** Strictly at **Y = 0.000m**

| Parameter | Metric Value | Imperial Value | Engineering Notes |
|---|---|---|---|
| Length Overall (Gun Forward) | 9.15 m | 30.0 ft | 105mm F2 gun forward to rear hull |
| Hull Length | 6.35 m | 20.8 ft | Compact welded aluminum hull |
| Width Overall | 2.95 m | 9.7 ft | Width across 6x6 high-flotation tires |
| Height (Overall) | 2.68 m | 8.8 ft | Ground plane to turret roof panoramic sight |
| Combat Weight (AMX-10 RCR) | 17,200 kg | 37,920 lbs | With modernized SEPAR modular steel applique |
| Primary Armament | 105 mm F2 BK MECA L/47 | Semi-automatic medium-pressure rifled cannon |
| Secondary Armament | 7.62 mm NF1 Coaxial MG | Coaxial machine gun mount |
| Roof Armament | 7.62 mm Pintle Mount | Commander cupola defense gun |
| Drive Configuration | 6x6 Skid-Steering | Turns in place like a tracked tank via skid-steer |
| Suspension | Variable Hydro-Pneumatic | Adjustable ride height, tilt, kneel, and squat |
| Powerplant | Baudouin 6F11 SRX Diesel | 280 hp turbo-charged diesel engine |

---

### 2. ARMAMENT AND HYDRO-PNEUMATIC SUSPENSION LOFTS

The AMX-10 RCR utilizes a specialized 6x6 skid-steering transmission (no steerable axles; steering is achieved by varying wheel speeds on opposite sides) paired with active hydro-pneumatic suspension allowing dynamic ground clearance adjustment from 210mm to 600mm.

| Subsystem Component | Operational Axis | Angular Limits | Slew Rate |
|---|---|---|---|
| TK 105 Turret Traverse | Yaw around +Y axis | 360.0 deg continuous | 35.0 deg/sec electric drive |
| 105mm F2 Cannon Elevation | Pitch around +X axis | -8.0 deg to +20.0 deg | 20.0 deg/sec elevation drive |
| F2 Gun Recoil Stroke | Surge translation along -Z | Stroke: -0.32m | Hydraulic recoil brake |
| Hydro-Pneumatic Ride Height | Vertical translation +Y | 0.21m to 0.60m clearance | Kneel, squat, or high-clearance modes |
| Skid-Steer Wheels (6x) | Continuous pitch roll +/-X | High-speed 85 km/h | Independent Michelin run-flat tires |

---

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

```
AMX10_RCR_Root (Y=0.000m at tire contact plane)
├── Hull_Aluminum_Armored
│   ├── Modular_Steel_Applique_Plates (SEPAR armor package)
│   ├── Driver_Hatch_Glacis (Pivot pitch/slide left)
│   ├── Baudouin_Diesel_Engine_Bay
│   ├── Bilateral_Waterjet_Propulsors (Aft amphibious nozzles - original baseline)
│   └── Suspension_6x6_Skid_Steer
│       ├── Front_Wheel_Station_Port & Starboard (Hydro-pneumatic vertical travel: 0.39m)
│       ├── Center_Wheel_Station_Port & Starboard (Hydro-pneumatic travel: 0.39m)
│       ├── Rear_Wheel_Station_Port & Starboard (Hydro-pneumatic travel: 0.39m)
│       └── Heavy_Michelin_RunFlat_Tires_6x (Continuous pitch roll around +/-X)
└── Turret_TK105_Modernized (Azimuth yaw rotation around +Y axis: 360 deg)
    ├── Commander_Cupola (Vision periscopes and 7.62mm pintle mount)
    ├── Gunner_Station_Roof_Hatch
    ├── COTAC_Digital_Fire_Control_System
    ├── Thales_Castor_Thermal_Camera
    ├── GALIX_Concealment_Smoke_Dischargers (Turret flank banks)
    └── Main_Cannon_Trunnion
        └── Elevating_Mass_105mm_F2 (Pitch articulation around +X: -8 to +20 deg)
            ├── Thermal_Jacket_Shroud
            ├── Double-Baffle_Muzzle_Brake
            └── Barrel_Recoil_Group (Surge translation along -Z: -0.32m stroke)
```

---

### 4. SENSOR SITING & RECONNAISSANCE PAYLOAD AUDIT

- **COTAC Fire Control System:** Automated ballistic computer integrating laser rangefinder and meteorological sensors for high-probability first-round hits on moving targets.
- **Thales Thermal Imaging:** High-resolution cooled infrared sensor providing 24/7 identification of armored vehicles at ranges exceeding 4,000 meters.
- **Skid-Steering Kinematics:** Wheel rotational speeds on port and starboard sides are independently variable, enabling 360-degree pivot turns on roads or rough terrain without wheel steering knuckles.

---

### 5. MASTER AI VIDEO PROMPT PACKAGE

1. **CAD Blueprint Isometric Rotation:**
   `Turntable CAD blueprint of French Army Nexter AMX-10 RCR 6x6 tank destroyer, dark navy blue background #0A192F, stark white architectural linework #FFFFFF, cyan coordinate grid #00FFFF, 105mm F2 gun with double-baffle muzzle brake, 6x6 skid-steer chassis, SEPAR armor package.`

2. **Skid-Steer Pivot Turn on Highway:**
   `High-angle drone shot of French AMX-10 RCR armored vehicle performing a rapid 180-degree pivot spin in place using 6x6 skid-steering on open roadway, heavy tire smoke, vehicle accelerating away instantly at 50 mph.`

3. **Hydro-Pneumatic Suspension Kneeling:**
   `Close-up technical view of AMX-10 RCR hull adjusting its hydro-pneumatic suspension behind an earthen berm, smoothly dropping ground clearance from 60cm to 21cm to adopt a hull-down ambush stance.`

4. **105mm High-Velocity Armor Piercing Shot:**
   `Dawn desert proving ground, AMX-10 RCR firing 105mm F2 armor-piercing fin-stabilized sabot round, double-baffle muzzle brake venting supersonic gases horizontally, 32cm barrel recoil kick, immediate forward recovery.`
