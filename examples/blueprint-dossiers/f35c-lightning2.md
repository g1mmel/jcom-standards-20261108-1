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
query: "Lockheed Martin F-35C Lightning II Carrier Strike Fighter Blueprint"
sources_count: 18
asset_id: "f35c-lightning2"
title: "Naval Architectural Blueprint Dossier: Lockheed Martin F-35C Lightning II"
---

# Naval Architectural Blueprint Dossier: Lockheed Martin F-35C Lightning II Carrier Strike Fighter

**Classification:** USA | US Navy / US Marine Corps | Carrier Strike Fighter | F-35 Lightning II | F-35C
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

---

### 1. MASTER COORDINATE DATUM & DIMENSIONS

- **glTF 2.0 WebGL Coordinate Standard:**
  - Forward / Nose Heading: **-Z axis** (0 deg yaw)
  - Vertical / Canopy Apex: **+Y axis**
  - Transverse / Starboard Wingtip: **+X axis**
  - Transverse / Port Wingtip: **-X axis**
  - **Ground Plane / Weight-on-Wheels:** Strictly at **Y = 0.000m**

| Parameter | Metric Value | Imperial Value | Engineering Notes |
|---|---|---|---|
| Length Overall (LOA) | 15.70 m | 51.5 ft | Pitot nose to trailing edge of exhaust nozzle |
| Wingspan (Extended) | 13.10 m | 43.0 ft | Enlarged carrier wing planform (vs 10.7m on F-35A) |
| Wingspan (Folded) | 9.10 m | 30.0 ft | Outboard wingtip panels fold upward 90 deg |
| Height (+Y) | 4.48 m | 14.7 ft | Ground contact plane to vertical tail tip |
| Wing Area | 62.10 m^2 | 668 sq ft | Lowers carrier approach speed to 135-140 kts |
| Maximum Takeoff Weight (MTOW) | 31,751 kg | 70,000 lbs | Maximum catapult launch envelope |
| Empty Weight | 15,686 kg | 34,581 lbs | Heavy navalized carrier structure |
| Internal Fuel Capacity | 8,960 kg | 19,750 lbs | Extended range carrier air wing strike asset |
| Propulsion | 1x Pratt & Whitney F135-PW-400 | 43,000 lbf afterburning | Navalized titanium corrosion-resistant engine |

---

### 2. CARRIER LAUNCH & RECOVERY WING STATION LOFTS

The F-35C incorporates enlarged wings, ailerons, and leading-edge flaps compared to CTOL variants, reducing approach speed and providing precise glide-slope control via Integrated Direct Lift Control (IDLC).

| Wing Station | Transverse X (m) | Chord (m) | Thickness-to-Chord | Leading-Edge Sweep | Dihedral |
|---|---|---|---|---|---|
| Fuselage Chine Blend | 0.00 | 6.80 | 11.5% | +35.0 deg | -2.5 deg (anhedral) |
| Inboard Wing Root | +/- 1.85 | 5.20 | 10.0% | +35.0 deg | -2.5 deg |
| Wing Fold Hinge Axis | +/- 4.55 | 3.10 | 9.0% | +35.0 deg | -2.5 deg |
| Outboard Wing Fold Section | +/- 5.80 | 2.15 | 8.0% | +35.0 deg | -2.5 deg |
| Starboard / Port Wingtip | +/- 6.55 | 1.25 | 7.5% | +35.0 deg | -2.5 deg |

---

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

```
Airframe_Root (Y=0.000m at tire contact)
├── Fuselage_Main_Chine
│   ├── Canopy_Cockpit (Hinge pitch around forward bulkhead: +45 deg lift)
│   ├── Internal_Weapons_Bay_Port
│   │   ├── Weapons_Bay_Door_Inboard_Port (Bi-fold roll outwards)
│   │   ├── Weapons_Bay_Door_Outboard_Port (Bi-fold roll outwards)
│   │   └── EAD_Launcher_Rail_Port (Pneumatic trapeze deploy: 0.45m down)
│   ├── Internal_Weapons_Bay_Starboard
│   │   ├── Weapons_Bay_Door_Inboard_Starboard (Bi-fold roll outwards)
│   │   ├── Weapons_Bay_Door_Outboard_Starboard (Bi-fold roll outwards)
│   │   └── EAD_Launcher_Rail_Starboard (Pneumatic trapeze deploy)
│   ├── Engine_Exhaust_Nozzle (Variable axisymmetric iris petals pitch/yaw)
│   ├── Arresting_Hook_Cover (Bay door pitch open)
│   └── Heavy_Carrier_Tailhook (Forged stinger hook, pivot pitch down: -55 deg)
├── Landing_Gear_Nose (Heavy carrier dual-wheel design)
│   ├── Nose_Gear_Oleo_Strut (Stroke: 0.38m along +Y)
│   ├── Nose_Wheels_Dual (Continuous roll around +X)
│   ├── Catapult_Launch_Bar (Carrier launch shuttle link, pitch articulation -50 deg)
│   └── Holdback_Fitting_Aft
├── Landing_Gear_Main_Port & Starboard (Reinforced carrier-rated wide track)
│   ├── Main_Gear_Heavy_Trunnion
│   ├── Main_Gear_Oleo_Struts (High-sink rate 7.5 m/s absorption)
│   └── Main_Wheels_Single (Continuous roll around +/-X)
├── Wing_Root_Port & Starboard
│   ├── Leading_Edge_Flap_Inboard (Deflection: 0 to -34 deg pitch)
│   └── Trailing_Edge_Flap_Inboard (Deflection: +15 deg to -40 deg pitch)
├── Wing_Fold_Outboard_Port (Hinge roll: 90 deg vertical upward fold)
│   ├── Leading_Edge_Flap_Outboard (Deflection: 0 to -34 deg)
│   └── Aileron_Droop_Port (Differential flaperon pitch: +/- 30 deg)
├── Wing_Fold_Outboard_Starboard (Hinge roll: 90 deg vertical upward fold)
│   ├── Leading_Edge_Flap_Outboard (Deflection: 0 to -34 deg)
│   └── Aileron_Droop_Starboard (Differential flaperon pitch: +/- 30 deg)
└── Empennage_Twin_Canted_Tails
    ├── Vertical_Fin_Port (Canted outboard 20 deg, all-moving rudder pitch/yaw: +/- 25 deg)
    ├── Vertical_Fin_Starboard (Canted outboard 20 deg, all-moving rudder pitch/yaw: +/- 25 deg)
    ├── Horizontal_Stabilator_Port (All-moving slab pitch: -30 deg to +20 deg)
    └── Horizontal_Stabilator_Starboard (All-moving slab pitch: -30 deg to +20 deg)
```

---

### 4. SENSOR SITING & STEALTH LO AUDIT

- **AN/APG-81 Active Electronically Scanned Array (AESA):** Nose cone forward bulkhead radar array providing ultra-long range air-to-air tracking and synthetic aperture radar (SAR) ground mapping.
- **AN/AAQ-40 Electro-Optical Targeting System (EOTS):** Faceted sapphire glass prism chin pod below nose radome forward of nose landing gear.
- **AN/AAQ-37 Distributed Aperture System (DAS):** Six flush-mounted infrared sensor windows around fuselage providing 360-degree spherical missile warning and situational awareness.
- **MADL (Multifunction Advanced Data Link):** Directional phased array antenna tiles flush with airframe skin to maintain low radar cross section (RCS).

---

### 5. MASTER AI VIDEO PROMPT PACKAGE

1. **CAD Blueprint Isometric Rotation:**
   `Cinematic orthographic turntable CAD blueprint of Lockheed Martin F-35C Lightning II, dark navy blue environment #0A192F, stark white technical line art #FFFFFF, cyan dimensional grids #00FFFF, enlarged carrier wings, folding wingtips, faceted stealth chin EOTS, arrestor tailhook stinger.`

2. **Catapult Launch Sequence:**
   `Flight deck catapult 1 of USS Gerald R. Ford CVN-78, F-35C Lightning II kneeling on nose gear oleo, launch bar engaged with EMALS carrier shuttle, Pratt & Whitney F135 engine in full afterburner, orange-blue Mach diamonds, blast deflector raised.`

3. **Carrier Approach & IDLC Direct Lift Control:**
   `Stern camera view of F-35C on carrier final approach, 135 knots glide slope, large trailing edge control surfaces continuously twitching in active IDLC stabilization, heavy carrier landing gear extended, arrestor hook deployed downward.`

4. **3-Wire Trap Kinetic Recovery:**
   `Low-angle carrier flight deck perspective, F-35C Lightning II carrier strike fighter trapping wire 3, arresting hook engaging cross deck cable with sparks and tension payout, heavy main oleos compressing smoothly on non-skid.`
