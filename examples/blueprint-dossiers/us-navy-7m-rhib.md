---
generated_at: "2026-10-09T02:45:13Z"
generator: "antigravity-deep-research (agy-dsk, session 5aa41122-41b5-472f-8d87-b3da904ffdd2)"
research_method: "search"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "Google Gemini"
models:
  - "deep-research-preview-04-2026"
  - "gemini-3.5-flash-lite"
query: "US Navy 7-Meter RHIB Blueprint and Body Plan"
sources_count: 15
asset_id: "us-navy-7m-rhib"
title: "Naval Architectural Blueprint Dossier: United States Navy 7-Meter Rigid Hull Inflatable Boat"
---

# Naval Architectural Blueprint Dossier: United States Navy 7-Meter Rigid Hull Inflatable Boat (RHIB)

**Classification:** USA | US Navy | Rigid Hull Inflatable Boat | 7-Meter RHIB | 7m Standard Navy RHIB
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

---

### 1. MASTER COORDINATE DATUM & DIMENSIONS

- **glTF 2.0 WebGL Coordinate Standard:**
  - Forward / Bow: **-Z axis** (0 deg yaw)
  - Vertical / Console Apex / Radar Arch: **+Y axis**
  - Transverse / Starboard: **+X axis**
  - Transverse / Port: **-X axis**
  - **Design Waterline (DWL):** Strictly at **Y = 0.000m**
  - **Keel Deepest Extent:** At **Y = -0.580m**

| Parameter | Metric Value | Imperial Value | Engineering Notes |
|---|---|---|---|
| Length Overall (LOA) | 7.30 m | 23.9 ft | Bow collar apex to stern waterjet/drive transom |
| Beam Overall (BOA) | 2.74 m | 9.0 ft | Extreme width over fully inflated collar |
| Beam Hull (Rigid Monohull) | 2.10 m | 6.9 ft | Molded rigid fiberglass/aluminum deep-V hull |
| Draft at DWL (Loaded) | 0.58 m | 1.9 ft | Full load displacement draft |
| Air Draft (Mast Up) | 2.45 m | 8.0 ft | DWL to radar mast navigation light apex |
| Displacement (Full Load) | 3,950 kg | 8,708 lbs | Boat, crew of 3, 10 passengers/combat troops, fuel |
| Empty Weight (Hoisting) | 2,400 kg | 5,291 lbs | Davit hoisting condition with 4-point bridle |
| Deep-V Deadrise Angle | 24.0 deg | Continuous deep-V hull form with planing strakes |
| Propulsion | Caterpillar 3126 / Cummins QSB 5.9 | 380 hp | High-speed marine turbo-diesel engine |
| Propulsor | HamiltonJet HJ274 Waterjet | High-thrust reverse deflector bucket |

---

### 2. 11-STATION TRANSVERSE OFFSET TABLE (BODY PLAN)

The monohull features an aggressive 24-degree deadrise deep-V forward entry with two continuous lifting strakes per side and wide spray chine flats beneath the multi-chambered hypalon collar.

| Station | Axial Position Z (m) | Half-Breadth at DWL X (m) | Keel Baseline Y (m) | Deck Sheer Y (m) | Deadrise Angle |
|---|---|---|---|---|---|
| Station 0 (Transom) | +3.40 | 1.05 | -0.42 | +0.48 | 20.0 deg |
| Station 1 | +2.72 | 1.05 | -0.44 | +0.49 | 20.5 deg |
| Station 2 | +2.04 | 1.04 | -0.46 | +0.50 | 21.0 deg |
| Station 3 | +1.36 | 1.02 | -0.48 | +0.52 | 22.0 deg |
| Station 4 (Midships) | +0.68 | 0.98 | -0.52 | +0.55 | 23.0 deg |
| Station 5 | 0.00 | 0.92 | -0.55 | +0.58 | 24.0 deg |
| Station 6 | -0.68 | 0.84 | -0.58 | +0.62 | 24.0 deg |
| Station 7 | -1.36 | 0.72 | -0.54 | +0.68 | 26.0 deg |
| Station 8 | -2.04 | 0.56 | -0.45 | +0.76 | 32.0 deg |
| Station 9 | -2.72 | 0.36 | -0.30 | +0.86 | 45.0 deg |
| Station 10 (Bow Stem) | -3.40 | 0.00 | +0.00 | +1.02 | 58.0 deg (Fine entry) |

---

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

```
RHIB_Root (Y=0.000m at Design Waterline)
├── Hull_Deep_Vee_Rigid
│   ├── Inflatable_Collar_Hypalon_Chambers (Multi-cell perimeter tube)
│   ├── Bow_Towing_Bollard (Eye bolt fitting, X=0, Z=-3.30m)
│   ├── Forward_Weapons_Mount (Pintle socket for M240B / M2HB 50 cal)
│   │   └── Weapon_Pintle_Assembly (Yaw 360 deg, pitch -15 to +45 deg)
│   ├── Center_Console_Station
│   │   ├── Helm_Wheel (Steering roll around -Z axis: +/- 360 deg)
│   │   ├── Throttle_Control_Quadrant (Pitch lever articulation: -30 to +40 deg)
│   │   ├── Marine_Radar_Display_Furuno
│   │   └── Windshield_Polycarbonate
│   ├── Crew_Jockey_Seats_Suspension (Shockwave shock-absorbing travel along +Y: 0.12m)
│   ├── Engine_Compartment_Hatch (Pivot pitch along forward hinge: +55 deg)
│   │   └── Caterpillar_Marine_Diesel_Engine
│   ├── Radar_Arch_Rollcage_T_Top
│   │   ├── Marine_Radar_Dome (Continuous yaw roll around +Y: 24 RPM)
│   │   ├── VHF_Antenna_Whip_Port (Flexible mast dynamics)
│   │   ├── GPS_Sensor_Mushroom
│   │   └── Blue_Law_Enforcement_Strobe
│   ├── Stern_Waterjet_Drive (HamiltonJet HJ274)
│   │   ├── Steering_Nozzle (Yaw deflection around +Y axis: +/- 30 deg)
│   │   └── Reversing_Deflector_Bucket (Pitch clamshell stroke: down for reverse, up for ahead)
│   └── Davit_Hoisting_Slings (4-point lifting padeyes on rigid deck)
```

---

### 4. SENSOR SITING & SMALL BOAT EQUIPMENT AUDIT

- **Navigation Radar:** Furuno or Raymarine high-resolution radome centered atop the aluminum aft arch pylon (Y = +2.30m, Z = +1.10m).
- **Communication & Navigation:** Dual high-gain VHF whip antennas, WAAS GPS sensor antenna, and stern LED navigation lanterns.
- **Weapon Mount Sockets:** Reinforced structural pedestal deck plate at bow centerline servicing Mk 93 twin-cradle or single-pin mount for M2HB .50 caliber heavy machine gun or Mk 19 40mm grenade launcher.
- **Davit Hoisting Provisions:** Four structural lifting padeyes bolted directly into longitudinal aluminum/composite stringers, rated for 6:1 safety factor dynamic shipboard recovery in sea state 4.

---

### 5. MASTER AI VIDEO PROMPT PACKAGE

1. **CAD Blueprint Isometric Rotation:**
   `Turntable CAD blueprint of US Navy 7-meter RHIB, navy blue background #0A192F, crisp white technical lines #FFFFFF, cyan waterline marker #00FFFF at Y=0.000m, deep-V monohull strakes, multi-chambered hypalon sponson collar, HamiltonJet waterjet transom assembly.`

2. **Davit Launch From Warship Sponson:**
   `Starboard boat davit of Arleigh Burke DDG-125 destroyer underway in ocean swell, US Navy 7m RHIB suspended from 4-point wire bridle, smoothly lowered into foaming ocean water, release hook trip, waterjet reverse bucket raising.`

3. **High-Speed Planing & Wave Piercing:**
   `Frontal telephoto tracking shot of US Navy 7-meter RHIB slamming through rough chop at 38 knots, intense bow spray curling off chine flats, crew in tactical helmets and flotation gear bracing on shock-mitigation jockey seats, bow M2HB machine gun mounted.`

4. **Night VBSS Boarding Approach:**
   `Night tactical VBSS approach in choppy black sea, US Navy 7m RHIB running dark with infrared navigation beacons, subdued console red night lighting, stealthy tactical insertion alongside cargo vessel.`
