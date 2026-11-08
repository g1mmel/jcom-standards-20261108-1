---
generated_at: "2026-10-14T15:27:18-04:00"
generator: "dolphin2/dossier-grok-dr"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "xai"
models:
  - "grok-4.7"
query: "F/A-18E Super Hornet naval architectural dimensions, kinematics, and sensors versus the legacy Hornet dossier"
sources_count: 7
asset_id: "fa-18e-super-hornet"
title: "Naval Architectural Blueprint Dossier: Boeing F/A-18E Super Hornet"
base_asset_id: "fa-18-hornet"
---

# Naval Architectural Blueprint Dossier: Boeing F/A-18E Super Hornet

**Classification:** USA | US Navy | carrier-based multirole strike fighter | single-seat F/A-18E. The F/A-18F is the two-seat sister and is not this asset. Boeing also lists Australia and Kuwait as Super Hornet customers [3].
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

The E entered fleet service in 1999. NAVAIR records first flight in November 1995, initial operational capability in September 2001 with VFA-115, and the first operational cruise on USS Abraham Lincoln (CVN 72) [1]. Block II added an active electronically scanned array. Block III is the later service-life and cockpit upgrade. Early production aircraft did not leave the factory with that array [1][5][7].

### 1. MASTER COORDINATE DATUM & DIMENSIONS

glTF: forward/nose = -Z, up = +Y, starboard = +X, port = -X, weight-on-wheels ground plane Y = 0.

Published cards do not define the measuring points (for example, static fin apex versus overall height, or clean tip versus tip with a missile). Where a card prints both feet and metres, both are copied. They are not averaged. An arithmetic check is a conversion of a printed figure. It is not a new measurement.

| Parameter | Metric | Imperial | Engineering notes |
| --- | --- | --- | --- |
| Length overall | NAVAIR prints 18.5 m. Boeing prints 18.3 m. | NAVAIR prints 60.3 ft. Boeing prints 60.2 ft. | Dual publishers, and they disagree [1][3]. Arithmetic check, not a published measurement: 60.3 ft = 18.38 m, and 60.2 ft = 18.35 m. NAVAIR's own pair, 60.3 ft and 18.5 m, does not convert. 18.5 m = 60.7 ft. Do not average. |
| Height | NAVAIR prints 4.87 m. Boeing prints 4.9 m. | 16 ft on both cards. | Feet are dual-source [1][3]. The metre labels are different roundings. Arithmetic check: 16 ft = 4.8768 m. |
| Wingspan | NAVAIR prints 13.68 m. Boeing prints 13.7 m. | 44.9 ft on both cards. | Feet are dual-source [1][3]. Arithmetic check: 44.9 ft = 13.69 m. Neither printed metre is that value. Neither card says whether 44.9 ft includes wingtip missiles. |
| Wing area | 46 m2 | 500 ft2 | single-source, FlightGlobal, 20 January 1999, quoting Boeing F/A-18 programme engineering [5]. Not printed on the current NAVAIR or Boeing specification cards fetched this pass [1][3]. |
| Maximum takeoff gross weight | NAVAIR prints 29,932 kg. Boeing prints 29,937 kg. FlightGlobal prints 30,000 kg. | 66,000 lb on all three. | Pounds are three-source [1][3][5]. Kilograms disagree. Arithmetic check: 66,000 lb = 29,937 kg. Do not average the kilograms. |
| Empty weight | not public as an operational empty weight | not public as an operational empty weight | Not on the fetched NAVAIR or Boeing cards [1][3]. FlightGlobal states a specification empty weight of 13,860 kg and says the development aircraft was under that figure [5]. single-source. That is not a fleet empty weight. |
| Engine static thrust, each | NAVAIR prints 9,977 kg. Boeing prints 7,711 kg as the kilogram of its 17,000 lb line. GE does not print a kilogram. | NAVAIR: 22,000 lb static thrust per engine. GE: 22,000 lb thrust class. FlightGlobal: 44,000 lb total maximum (196 kN). Boeing card: each engine up to 17,000 lb. | NAVAIR, GE, and FlightGlobal support a 22,000 lb class, stated differently [1][4][5]. The current Boeing card disagrees at 17,000 lb per engine [3]. Arithmetic check: 22,000 lb = 9,979 kg, not NAVAIR's 9,977 kg, and = 97.9 kN, against FlightGlobal's 196 kN for two engines. Do not average 17,000 and 22,000. |
| Crew | 1 | 1 | NAVAIR: "The E is a single seat" and "A, C and E models: One" [1]. The fetched Boeing specification block does not repeat crew [3]. |
| Ceiling | Boeing prints 15,240+ m. | 50,000+ ft | Feet are dual-source [1][3]. The metre line is Boeing's conversion of 50,000 ft [3]. |
| Maximum speed | not printed as a metric | NAVAIR: Mach 1.8+. Boeing: Mach 1.6. | Disagreement [1][3]. Do not average. |
| Combat range | NAVAIR prints 2,346 km. | 1,275 nautical miles, clean plus two AIM-9s. | single-source pair, NAVAIR [1]. Arithmetic check: 1,275 nautical miles = 2,361 km at 1.852 km per nautical mile, not 2,346 km. Print the card. Do not replace it. |
| Ferry range | NAVAIR prints 3,054 km. | 1,660 nautical miles, two AIM-9s, three 480-gallon tanks retained. | single-source pair, NAVAIR [1]. Arithmetic check: 1,660 nautical miles = 3,074 km, not 3,054 km. |
| Carrier bring-back payload, E | Boeing prints 4,491 kg. | 9,900 lb | single-source, Boeing [3]. The same card prints 9,000 lb (4,082 kg) for the F, which is not this asset. |
| External stores capacity | 8,050 kg | not printed beside that kilogram | single-source, FlightGlobal [5]. |
| Internal fuel | 6,560 kg, described as 33 percent more than the C/D | not printed in pounds on the fetched page | single-source, FlightGlobal [5]. |
| Fuselage stretch versus C/D | 860 mm | 34 in | single-source, FlightGlobal [5]. NAVAIR says the E/F is substantially larger and roughly 7,000 lb heavier, without this length [1]. |
| Folded wingspan | not public | not public | Not on the fetched NAVAIR or Boeing cards [1][3]. No fold angle was fetched. |
| Wing sweep, dihedral, anhedral, station coordinates, pivot coordinates | not public | not public | No fetched page prints them. |

Engine envelope, not airframe envelope: GE prints F414-GE-400 length 154 in, maximum diameter 35 in, airflow 170 lb/sec, and pressure ratio 30:1 [4]. FlightGlobal independently reports pressure ratio 30:1, thrust-to-weight class 9:1, and 16 percent more airflow than the F404 [5]. dual-source for pressure ratio 30:1. The inch figures are single-source, GE [4].

### 2. FLIGHT CONTROL SURFACES, WING FOLD, AND STORES

No loft table is printed. Chord and thickness are not public.

FlightGlobal names the real surfaces and the real station groups [5]:

- Leading-edge flaps, with a leading-edge snag on the outer wing.
- Trailing-edge flaps.
- Ailerons.
- Rudders, one in each vertical tail. The tails are 15 percent larger than the C/D. single-source [5].
- All-moving horizontal stabilators, 36 percent larger than the C/D. single-source [5].
- One spoiler on the upper surface of each leading-edge extension. These are the speed-brake surfaces.
- Leading-edge-extension vents were tested and were planned for removal before full-rate production. single-source [5]. Do not model them as a production feature on that evidence alone.
- Outer wing panels fold for carrier handling. The fold angle, hinge station, and folded span are not public.
- Arresting hook. FlightGlobal says the only control cable in the aircraft runs to the hook [5]. Hook angle and shank length are not public.
- Eleven stores stations. dual-source for the count: Boeing says 11 weapons stations [3]; FlightGlobal says 11 stores stations [5]. The split is single-source, FlightGlobal: two wingtip missile rails, six under-wing pylons, two inlet stations, and one centre-fuselage pylon [5]. Station coordinates are not public.
- Wingtip stores on the E are missile rails, not receiver pods [5]. NAVAIR's combat-range condition is "clean plus two AIM-9s" [1].
- Nose gun. NAVAIR's armament line says one M61A1/A2 Vulcan 20 mm cannon [1]. The E/F manufacturer sheet names an M61A2 on a pallet in the nose, 412 rounds, and 4,000 or 6,000 shots per minute [6]. The round count and the rates are single-source. The sheet also prints pallet dimensions of 71.9 in, 25 in, and 22.3 in. Those are single-source and are not airframe stations [6].
- There is no published internal weapon bay, bay door, or trapeze launcher [1][3][5].

The dorsal speed brake of the C/D is not on the E/F. FlightGlobal states that the E/F lacks the C/D upper-fuselage airbrake. The flight-control system deflects the leading-edge-extension spoilers up, the ailerons up, the trailing-edge flaps down, and the rudders out [5]. single-source. Deflection angles and rates are not public.

The E/F has rectangular caret inlets, aligned with the wing leading edges, and no leading-edge-extension fences and no inlet diverter ramps [5]. single-source. Two F414-GE-400 afterburning turbofans [1][4].

Landing gear is strengthened relative to the C/D and uses Aermet 100 steel [5]. single-source. Gear travel, track, and wheelbase are not public. A catapult launch bar is not named on the fetched pages. Travel: not public.

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

Motion is stated only where a fetched source states it. Otherwise travel is not public. No pivot coordinates are published.

```
Airframe_Root
├── Fuselage
│   ├── Nose_Radome
│   │   └── Radar_Antenna (mechanical APG-73 on early jets; AN/APG-79 array on Block II and later; does not mechanically scan)
│   ├── Canopy_Single_Seat
│   ├── Inflight_Refueling_Probe (location not public on pages fetched this pass)
│   ├── Nose_Landing_Gear (travel: not public)
│   ├── Main_Landing_Gear_Port (travel: not public)
│   ├── Main_Landing_Gear_Starboard (travel: not public)
│   ├── Arresting_Hook (present; travel: not public)
│   ├── M61_Gun_Pallet_Nose (E/F only)
│   ├── LEX_Spoiler_Port (up for speed brake and high-AoA control; angle: not public)
│   ├── LEX_Spoiler_Starboard
│   ├── Inlet_Caret_Port
│   ├── Inlet_Caret_Starboard
│   ├── Engine_F414_Port
│   │   └── Afterburner_Nozzle_Port (travel: not public)
│   └── Engine_F414_Starboard
│       └── Afterburner_Nozzle_Starboard (travel: not public)
├── Wing_Inner_Port
│   ├── Leading_Edge_Flap_Inboard (travel: not public)
│   ├── Trailing_Edge_Flap (travel: not public)
│   └── Wing_Fold (outer panel folds; angle: not public)
│       ├── Leading_Edge_Flap_Outboard (travel: not public)
│       ├── Aileron (up in the speed-brake function; angle: not public)
│       └── Wingtip_Missile_Rail
├── Wing_Inner_Starboard
│   └── (same hand, opposite side)
├── Vertical_Tail_Port
│   └── Rudder_Port (out in the speed-brake function; angle: not public)
├── Vertical_Tail_Starboard
│   └── Rudder_Starboard
├── Stabilator_Port (travel: not public)
└── Stabilator_Starboard (travel: not public)
```

Hydraulic system pressure switches from 207 bar to 345 bar (3,000 psi to 5,000 psi) at high speed and high angle of attack [5]. single-source. Flight controls are quadruplex digital fly-by-wire. The mechanical backup of the C/D was removed [5]. single-source.

### 4. SENSOR SITING & AVIONICS

- Radar sits in the nose cavity. FlightGlobal, writing in 1999, says production E/F aircraft kept the Raytheon AN/APG-73, a mechanically scanned upgrade of the APG-65, with growth reserved for an active array [5]. NAVAIR says Block II production incorporated the active electronically scanned array [1]. NAVAIR's 9 February 2004 award names that set as the Raytheon AN/APG-79 and says it replaces mechanically scanned antennas [7]. The array is solid-state and the beam is steered electronically [7]. Installation tilt, module count, and antenna coordinates are not public. Do not animate a rotating dish on a Block II or later jet. Do not put an APG-79 on every early E.
- Targeting. FlightGlobal says a Raytheon Advanced Targeting Forward-Looking Infra-Red pod was in development in 1999 to replace the AAS-38 pod, with service planned for 2001 [5]. single-source for that programme status. It is an external pod, not a fixed sapphire nose fairing. Station coordinates are not public. The current Boeing card lists IRST among Block III avionics and does not give a station [3].
- Defensive electronics planned at the time of FlightGlobal's article: AN/ALR-67(V)3, AN/ALQ-214, and ALE-55, with ALE-50 used first and a three-decoy dispenser under the fuselage between the engines [5]. single-source. Coordinates are not public.
- No fetched page describes an electro-optical targeting system fairing, a distributed aperture system, or internal weapon-bay sensors.

### 5. DIFFERENCES FROM THE BASE DOSSIER

The base dossier is the legacy F/A-18 Hornet, not the Super Hornet. None of its dimensions, loft tables, surface angles, or sensor fittings are carried onto the E. Current NAVAIR legacy-Hornet card, for the audit only [2]:

- Base claim: length overall 17.070 m. NAVAIR A-D card: 56 ft, printed as 16.8 m [2]. Arithmetic check: 56 ft = 17.07 m, so the base metre follows the feet and not NAVAIR's printed 16.8 m. Corrected E claim: 60.3 ft / 18.5 m on NAVAIR [1], and 60.2 ft / 18.3 m on Boeing [3]. Those pairs disagree with each other and, on the NAVAIR card, with themselves.
- Base claim: span 12.310 m. NAVAIR A-D card: 40 ft 5 in, printed as 13.5 m [2]. Arithmetic check: 40 ft 5 in = 12.32 m, not 12.310 m and not 13.5 m. Corrected E claim: 44.9 ft, printed as 13.68 m by NAVAIR and 13.7 m by Boeing [1][3].
- Base claim: folded span 8.380 m. Not printed on the fetched A-D card [2]. Not confirmed. Corrected E claim: folded span is not public [1][3].
- Base claim: height 4.670 m. NAVAIR A-D card: 15 ft 4 in, printed as 4.6 m [2]. Arithmetic check: 15 ft 4 in = 4.67 m. Corrected E claim: 16 ft, printed as 4.87 m by NAVAIR and 4.9 m by Boeing [1][3].
- Base claim: wing area 37.160 m2. Not printed on the fetched A-D card [2]. Corrected E claim: 500 ft2 (46 m2), single-source FlightGlobal [5].
- Base claim: maximum takeoff weight 23,541 kg. NAVAIR A-D card: 51,900 lb, printed as 23,537 kg [2]. Arithmetic check: 51,900 lb = 23,541 kg, so the base kilogram follows the pounds and not the printed 23,537 kg. Corrected E claim: 66,000 lb, with kilograms 29,932, 29,937, and 30,000 depending on the publisher [1][3][5].
- Base claim: leading-edge sweep 26.7 degrees, anhedral -3.0 degrees, chine pitch -5.0 degrees, and stealth facets parallel to the sweep. Not public for the A-D card or the E [1][2][5]. Do not carry them.
- Base claim: wing-station chords 4.040 m, 2.520 m, and 1.210 m, with thickness ratios 0.050, 0.045, and 0.040. Not public [5]. Do not carry the loft table.
- Base claim: leading-edge flaps 0 to 30 degrees down; trailing-edge flaperons and ailerons 45 degrees down and 25 degrees up; rudders 30 degrees; elevators 35 degrees up and 25 degrees down; dorsal spoilers 60 degrees. Not public for the E [5]. FlightGlobal describes directions only, and it deletes the dorsal airbrake [5].
- Base claim: wing fold 0 degrees in flight to 95 degrees stowed. Fold angle is not public for the E [1][3][5].
- Base claim: an APG active-array antenna as a general Hornet fit. Legacy card does not name an AESA [2]. Early E/F aircraft used the mechanically scanned AN/APG-73 [5]. Block II and later E/F aircraft use the AN/APG-79, which does not mechanically scan [1][7].
- Base claim: an EOTS sapphire fairing. No fetched source gives the E an electro-optical targeting system or a sapphire fairing. The targeting sensor described in 1999 is a pod [5].
- Base claim: internal weapon-bay doors and an internal trapeze. No fetched source gives the E an internal bay. Stores are external on 11 stations [3][5].
- Base claim: a distributed aperture system. Not described [1][5].
- Base claim: wingtip ESM pods. The E's wingtips are missile rails [5]. Wingtip receiver pods belong to the EA-18G, not to this asset.
- Base claim, implied by the legacy identity: two F404-class engines. NAVAIR's A-D card prints two F404-GE-402 engines at 17,700 lb static thrust each [2]. Corrected E claim: two F414-GE-400 engines [1][4].
- Role and crew. The base dossier is a generic legacy Hornet. The E is a single-seat strike fighter with tanker capability among its missions [1]. The F is two-seat and is not this mesh.
- Airframe shape that the base dossier does not state, and that must not be copied from a legacy Hornet model: caret inlets, no leading-edge-extension fences, no dorsal speed brake, larger wing, and a 34 in fuselage stretch [5]. NAVAIR also says roughly 7,000 lb heavier and about 50 percent more range than the predecessor, without a more precise empty weight [1]. single-source for those two comparisons.

### 6. GAME DATA CHECK

Quoted from `data/rules/unit-dimensions.json` and `data/roster/jslc.json` for `jslc.aircraft.fa-18e-super-hornet` and `coalition.aircraft.fa-18e-super-hornet`:

- lengthM 18.5, widthM 13.68, heightM 4.87.
- Source note: "US Navy F/A-18E/F length 18.5 m, span 13.68 m (44.9 ft), height 4.87 m."
- Notes: "Folded span 32.6 ft (9.94 m) is storage only."
- Roster basis: "representative". Mass is null.

Agree that 18.5 m, 13.68 m, and 4.87 m are the metre labels printed on the current NAVAIR E/F card [1].

Disagree that those metres are exact conversions of the feet on that same card. NAVAIR prints 60.3 ft, 44.9 ft, and 16 ft [1]. Arithmetic check: 18.38 m, 13.69 m, and 4.88 m. Boeing prints 60.2 ft (18.3 m), 44.9 ft (13.7 m), and 16 ft (4.9 m) [3]. The game length matches NAVAIR's metre and not Boeing's metre or either publisher's feet.

Disagree with using one span number as if the missile-on and missile-off spans were both published. Neither fetched card says what 44.9 ft includes [1][3].

The folded-span sentence is not confirmed. No fetched NAVAIR or Boeing card prints 32.6 ft or 9.94 m. Calling a folded span a storage figure, rather than the flight span, is the right category if a folded figure is later sourced. The number itself failed the two-source test this pass.

Agree with basis "representative". The cards disagree, and an operational empty weight is not on them. Agree that mass should stay null until an empty weight is sourced. `massTonnes` is null in the roster. No conflict.

### 7. MASTER AI VIDEO PROMPT PACKAGE

Technical CAD blueprint isometric fly-around:
Render a single-seat F/A-18E on a navy blueprint grid. Show rectangular caret intakes, no leading-edge-extension fences, no dorsal speed brake, a spoiler on each leading-edge extension, twin vertical tails, wing fold breaks, and wingtip missile rails. External pylons only. No internal bay doors and no chin sensor fairing.

Flight-control articulation and external stores:
Unfold the outer wings without stating an angle. Raise the leading-edge-extension spoilers, raise the ailerons, drop the trailing-edge flaps, and splay the rudders as the speed-brake function. Extend the arresting hook without stating an angle. Leave the weapon load on external rails and pylons.

Carrier launch and arrested recovery:
Show a catapult launch with both afterburners lit, then an arrested landing. Keep the single-seat canopy. Do not open weapon-bay doors. Do not extend a dorsal panel between the tails.

Night deck, wings folded:
Park the jet with outer wings folded. The fold angle is not stated because it is not published. Wingtip rails stay missile rails. Formation lights may be shown, but no dimension callouts.

### 8. SOURCES

1. NAVAIR, "F/A-18E/F Super Hornet," Naval Air Systems Command, https://www.navair.navy.mil/product/FA-18EF-Super-Hornet. Used for identity, crew, dates, Block II and Block III, F414 thrust, the 60.3 ft / 18.5 m card, height, span, 66,000 lb, speed, ceiling, ranges, and the M61A1/A2 armament line.
2. NAVAIR, "F/A-18 A-D Hornet," Naval Air Systems Command, https://www.navair.navy.mil/product/FA-18-D-Hornet. Used only to audit the legacy base card: 56 ft, 15 ft 4 in, 40 ft 5 in, 51,900 lb, F404-GE-402.
3. Boeing, "F/A-18 Super Hornet & EA-18 Growler," https://www.boeing.com/defense/fighters-and-bombers/fa-18-super-hornet-and-ea-18-growler. Used for the Super Hornet specification block: 60.2 ft, 44.9 ft, 16 ft, 66,000 lb, Mach 1.6, bring-back, 17,000 lb thrust line, and 11 weapons stations.
4. GE Aerospace, "F414 Engine," https://www.geaerospace.com/military-defense/engines/f414. Used for F414-GE-400 thrust class, length, diameter, airflow, and pressure ratio, and for the Super Hornet application.
5. FlightGlobal, "F/A-18E/F: Balanced Upgrade," 20 January 1999, https://www.flightglobal.com/fixed-wing/1999/01/f-a-18e-f-balanced-upgrade/. Used for the 34 in stretch, 500 ft2 wing, station split, caret inlets, deleted dorsal airbrake, leading-edge-extension spoilers, APG-73, ATFLIR programme status, hook, and specification empty weight.
6. General Dynamics Ordnance and Tactical Systems, "F/A-18 E/F 20mm Gatling Gun System," data sheet, https://www.gdots.com/wp-content/uploads/2025/11/400003005-20mm-F-A-18-E-F-Gatling-Gun-System-ARMAMENT.pdf. Used for M61A2, nose pallet, and 412 rounds.
7. NAVAIR, "AESA Second Low-Rate Initial Production Contract Awarded," 9 February 2004, https://www.navair.navy.mil/node/11616. Used for the AN/APG-79 name, Raytheon as builder, and replacement of mechanically scanned antennas on the Block II E/F.
