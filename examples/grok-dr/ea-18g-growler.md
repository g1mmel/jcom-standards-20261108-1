---
generated_at: "2026-10-14T15:27:18-04:00"
generator: "dolphin2/dossier-grok-dr"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "xai"
models:
  - "grok-4.7"
query: "EA-18G Growler naval architectural dimensions, electronic-attack fit, and comparison with the F/A-18E"
sources_count: 12
asset_id: "ea-18g-growler"
title: "Naval Architectural Blueprint Dossier: Boeing EA-18G Growler"
base_asset_id: "fa-18-hornet"
---

# Naval Architectural Blueprint Dossier: Boeing EA-18G Growler

**Classification:** USA | US Navy | carrier-based airborne electronic attack | two-seat EA-18G, built on the F/A-18F Super Hornet platform. The Royal Australian Air Force operates the type with the U.S. Navy [1]. The single-seat F/A-18E is not this asset.
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

NAVAIR and the Navy fact file both say the Growler combines the F/A-18F with an electronic-warfare suite and replaced the EA-6B Prowler [1][2]. The same pages contradict themselves on first flight. The "date deployed" line says first flight in October 2004. The background says the first test aircraft went into production in October 2004 and made its first flight in August 2006 [1][2]. Aviation Today separates those events: an F/A-18E modified with Growler wingtip pods began flight test in March 2006, and the first purpose-built two-seat EA-18G flew in August 2006 [5]. Do not average the dates. Initial operational capability is September 2009 on both official cards, with VAQ-132's first deployment in November 2010 [1][2]. Unit cost is $68 million on the NAVAIR page and $67 million on the Navy fact file [1][2]. Do not average.

### 1. MASTER COORDINATE DATUM & DIMENSIONS

glTF: forward/nose = -Z, up = +Y, starboard = +X, port = -X, weight-on-wheels ground plane Y = 0.

Measuring points are not defined on the cards. Feet and metres are copied as printed. They are not averaged. An arithmetic check is not a new measurement.

| Parameter | Metric | Imperial | Engineering notes |
| --- | --- | --- | --- |
| Length overall | NAVAIR and the Navy fact file print 18.5 m. Boeing prints 18.3 m. | NAVAIR, the Navy fact file, and Boeing all print 60.2 ft. | Feet agree across the three cards [1][2][3]. The NAVAIR and fact-file metre does not match their own feet. Arithmetic check: 60.2 ft = 18.35 m. 18.5 m = 60.7 ft. Boeing's 18.3 m is a rounding of 60.2 ft. The NAVAIR F/A-18E/F card prints 60.3 ft, not 60.2 ft [9]. Do not average 60.2 and 60.3. |
| Height | NAVAIR and the Navy fact file print 4.87 m. Boeing prints 4.9 m. | 16 ft on all three cards. | Feet are repeated official text plus Boeing [1][2][3]. Arithmetic check: 16 ft = 4.8768 m. |
| Wingspan | NAVAIR and the Navy fact file print 13.68 m. Boeing prints 13.7 m. | 44.9 ft on all three cards. | Same published feet as the F/A-18E/F cards [1][3][9]. Arithmetic check: 44.9 ft = 13.69 m. No fetched page prints a separate span "with ALQ-218 pods" or says the pods make the span larger than the E. |
| Wing area | not public for the G as its own measurement | not public for the G as its own measurement | Not on the Growler cards [1][2][3]. The E/F figure of 500 ft2 is single-source FlightGlobal and is not repeated here as a Growler measurement [11]. |
| Empty weight | not printed on the current Boeing card. Arithmetic check of 33,094 lb = 15,011 kg. | 33,094 lb | Printed by NAVAIR and the Navy fact file [1][2]. Those two pages come from the same programme office, so this is repeated official text, not two independent weighings. Boeing's current specification block does not list it [3]. |
| Recovery weight | Boeing prints 21,772.4 kg. | 48,000 lb | dual-source: NAVAIR and the Navy fact file, and Boeing [1][2][3]. Arithmetic check: 48,000 lb = 21,772 kg. This is a recovery weight, not a maximum takeoff weight. |
| Maximum takeoff weight | not public | not public | Not on the fetched Growler cards [1][2][3]. Do not copy the E/F figure of 66,000 lb onto the G. |
| Engine thrust | NAVAIR and the Navy fact file print 9,977 kg per engine. Boeing prints 19,958 kg for 44,000 lb total. | 22,000 lb static thrust per engine [1][2]. GE thrust class 22,000 lb [4]. Boeing Growler line: 44,000 lb total [3]. | The 22,000 lb class is NAVAIR plus GE [1][4]. Boeing's Growler total is two times 22,000 lb [3]. The same Boeing page prints "up to 17,000 lb" for each Super Hornet engine [3]. That line disagrees with the Growler total and with NAVAIR. Do not average. |
| Crew | 2 | 2 | NAVAIR and the Navy fact file [1][2]. Aviation Today: pilot in front, electronic-countermeasures officer in back [5]. Role title is single-source on the fetched pages. |
| Ceiling | Boeing prints 15,240+ m. | 50,000 ft on NAVAIR and the Navy fact file. Boeing prints 50,000+ ft. | Feet are official text plus Boeing [1][2][3]. |
| Maximum speed | not printed by NAVAIR or the Navy fact file | Boeing Growler block: Mach 1.8 | single-source, Boeing [3]. The Super Hornet block on that same page says Mach 1.6 [3]. NAVAIR's E/F card says Mach 1.8+ [9]. Do not move the E/F speed onto the G. |
| Combat range | kilometre equivalent not printed | 850+ nautical miles with two AIM-120, three ALQ-99, two AGM-88, and two 480-gallon tanks | repeated official text, NAVAIR and the Navy fact file [1][2]. |
| Folded wingspan | not public | not public | Not on the fetched cards [1][2][3]. No fetched page shows a folded span across the ALQ-218 pods. |
| Wing sweep, dihedral, station coordinates, pivot coordinates | not public | not public | No fetched page prints them. |
| Spot factor | not a length | 1.23 | single-source, Boeing [3]. |

### 2. FLIGHT CONTROL SURFACES, WING FOLD, AND STORES

The Growler is the F/A-18F platform [1][2]. FlightGlobal's E/F description is used only for airframe features that a Growler source does not contradict: caret inlets, no leading-edge-extension fences, no dorsal speed brake, leading-edge-extension spoilers, folding outer wings, and an arresting hook [11]. Deflection angles for those surfaces are not public. Travel: not public.

Growler-specific stores and deletions, from fetched pages:

- Wingtip air-to-air rails are replaced by AN/ALQ-218(V)2 receiver pods [5]. single-source for the station. The Navy fact file names the ALQ-218 receiver and does not say where it is mounted [2].
- Most of the ALQ-218 and the electronic-attack unit sit on a nose pallet that replaces the Super Hornet's 20 mm cannon [5]. single-source for that sentence. NAVAIR and the Navy fact file omit a gun from the armament line [1][2]. The E/F gun sheet is titled for the E/F and is not a Growler installation [12].
- Published armament line: two AIM-120, two AGM-88 HARM, and three ALQ-99 tactical jamming pods [1][2]. Aviation Today says up to five ALQ-99 pods on under-wing pylons [5]. Print both. Do not average.
- AN/ALQ-99 is an external pod. It stays in service until Next Generation Jammer increments reach full operational capability [6].
- AN/ALQ-249 Next Generation Jammer Mid-Band is an external pod. NAVAIR records Milestone C in 2021, a low-rate production contract in March 2023, and first production pods in July 2023 [7]. The Navy fact file, updated 17 September 2021, still called the AN/ALQ-249 a successor in final development [2]. The later NAVAIR jammer page is the production status. Low-band Next Generation Jammer was still in engineering and manufacturing development on the fetched page [7]. Pod station coordinates are not public. A NAVAIR caption places one mid-band pod under the right wing in a test photograph [1]. That caption is one installation, not a full station map.
- AN/ALQ-227 communications countermeasures set is named by the Navy fact file and described by Aviation Today [2][5]. Station coordinates are not public.
- Interference Cancellation System: it restores radio reception while the jammer is transmitting [5][8]. No station coordinate.
- A numeric weapon-station count for the G is not public on the fetched pages. Do not copy "nine stations" or "eleven stations" onto the G. The E/F count of 11 includes two wingtip rails [3][11]. Those tips are pods on the G [5].
- No fetched page describes an internal weapon bay.

Fold angle, hinge station, and folded span: not public.

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

Numbers appear only where a source states them. No pivot coordinates are published.

```
Airframe_Root
├── Fuselage_F_model_two_seat
│   ├── Nose_Radome
│   │   └── AN_APG-79 (electronically scanned; tilt and module count: not public)
│   ├── Canopy_Tandem
│   │   ├── Crewstation_Pilot_Front
│   │   └── Crewstation_ECMO_Rear (role title: single-source [5])
│   ├── Nose_Pallet_ALQ-218_and_Electronic_Attack_Unit (replaces the 20 mm cannon [5])
│   ├── Antennas_Nose_Aft_Fuselage_Dorsal (Aviation Today; coordinates: not public [5])
│   ├── Nose_Landing_Gear (travel: not public)
│   ├── Main_Landing_Gear_Port (travel: not public)
│   ├── Main_Landing_Gear_Starboard (travel: not public)
│   ├── Arresting_Hook (inherited from the E/F description [11]; travel: not public)
│   ├── LEX_Spoiler_Port (E/F speed-brake surface [11]; angle: not public)
│   ├── LEX_Spoiler_Starboard
│   ├── Inlet_Caret_Port
│   ├── Inlet_Caret_Starboard
│   ├── Engine_F414_Port
│   │   └── Afterburner_Nozzle_Port (travel: not public)
│   └── Engine_F414_Starboard
│       └── Afterburner_Nozzle_Starboard (travel: not public)
├── Wing_Inner_Port
│   ├── Leading_Edge_Flap (travel: not public)
│   ├── Trailing_Edge_Flap (travel: not public)
│   ├── Underwing_Pylon_Group (ALQ-99 or ALQ-249, fuel, or missiles; coordinates: not public)
│   └── Wing_Fold (angle: not public)
│       ├── Aileron (travel: not public)
│       └── Wingtip_ALQ-218_Pod (fixed receiver pod, not a missile rail [5])
├── Wing_Inner_Starboard
│   └── (same hand, opposite side; one test caption shows an NGJ-MB pod under the right wing [1])
├── Vertical_Tail_Port
│   └── Rudder_Port (travel: not public)
├── Vertical_Tail_Starboard
│   └── Rudder_Starboard
├── Stabilator_Port (travel: not public)
└── Stabilator_Starboard (travel: not public)
```

Aviation Today says the Growler added about 1,400 lb, about 2,500 ft of new radio-frequency cable, and 66 antennas to the Super Hornet airframe [5]. single-source. Antenna coordinates are not public.

### 4. SENSOR SITING & AVIONICS

- AN/APG-79 active electronically scanned array. Named for the Growler by the Navy fact file [2]. Aviation Today ties it to the Lot 30 F/A-18F fit and does not print a station coordinate [5]. The E/F programme page says Block II production incorporated an active electronically scanned array [9]. Tilt and module count are not public. Do not animate a mechanical dish.
- AN/ALQ-218(V)2 tactical jamming receiver. Navy fact file names it [2]. Aviation Today: wingtip pods in place of missile rails; the receiver is also distributed around the nose, mid-fuselage, and wingtips; most of it is on the nose pallet that replaces the cannon [5]. Wingtip and nose-pallet locations are single-source.
- AN/ALQ-99 pods, external, under the wings in the "up to five" description, and three in the official armament line [1][2][5][6].
- AN/ALQ-249 pods, external, mid-band in production and low-band still in development on the fetched NAVAIR page [7].
- AN/ALQ-227 communications countermeasures set [2][5]. Coordinates not public.
- Interference Cancellation System, in the radio receive path while jamming [5][8]. Coordinates not public.
- Joint Tactical Terminal receiver, named by the Navy fact file [2]. Coordinates not public.
- No fetched page gives the Growler an electro-optical targeting-system fairing, a distributed aperture system, or internal weapon-bay sensors.

### 5. DIFFERENCES FROM THE BASE DOSSIER

The base dossier is the legacy F/A-18 Hornet. Its dimensions and fittings are not the Growler. The E is a different asset. Differences below quote the base, then the corrected Growler claim.

- Base claim: length overall 17.070 m. Legacy NAVAIR card: 56 ft, printed as 16.8 m [10]. Arithmetic check: 56 ft = 17.07 m. Corrected G claim: 60.2 ft, printed as 18.5 m by NAVAIR and the Navy fact file and as 18.3 m by Boeing [1][2][3]. NAVAIR's E/F card is 60.3 ft, so the official E and G length lines are not identical [9].
- Base claim: span 12.310 m. Legacy card: 40 ft 5 in, printed as 13.5 m [10]. Arithmetic check: 40 ft 5 in = 12.32 m. Corrected G claim: 44.9 ft, printed as 13.68 m or 13.7 m [1][2][3]. That is the same published feet as the E. A larger span caused by the wingtip pods is not public.
- Base claim: folded span 8.380 m. Not on the fetched legacy card [10], and not on the Growler cards [1][2][3]. Corrected claim: not public.
- Base claim: height 4.670 m. Legacy card: 15 ft 4 in, printed as 4.6 m [10]. Corrected G claim: 16 ft, printed as 4.87 m or 4.9 m [1][2][3].
- Base claim: wing area 37.160 m2. Not printed on the fetched legacy card or the Growler cards [1][10]. Not carried.
- Base claim: maximum takeoff weight 23,541 kg. Legacy card: 51,900 lb, printed as 23,537 kg [10]. Corrected G claim: maximum takeoff weight is not public. Empty weight 33,094 lb and recovery weight 48,000 lb are the published Growler weights [1][2].
- Base claim: sweep 26.7 degrees, anhedral -3.0 degrees, chine -5.0 degrees, stealth-facet alignment, and the three-row loft table. Not public. Not carried.
- Base claim: numeric surface travels, including a dorsal spoiler to 60 degrees and a wing fold to 95 degrees. Not public for the G. The E/F description that the G inherits deletes the dorsal airbrake and uses leading-edge-extension spoilers [11]. Angles remain not public.
- Base claim: APG active array as a generic Hornet fit, plus an EOTS sapphire fairing and a distributed aperture system. The Growler fact file names the AN/APG-79 only [2]. No fetched page adds an electro-optical targeting-system fairing or a distributed aperture.
- Base claim: internal weapon bays and a trapeze. Not described. Stores and jamming pods are external [1][5][6][7].
- Base claim: wingtip ESM pods. The legacy Hornet card does not say that [10]. The Growler does carry wingtip receiver pods, and they are the AN/ALQ-218(V)2, replacing missile rails [5]. That fit is Growler-specific. It is not a reason to put the same pods on the legacy Hornet or on the E.
- Base claim, by legacy identity: one or two seats depending on A/B/C/D, F404 engines, and an M61 in the nose. Corrected G claim: two seats on the F airframe [1]; two F414-GE-400 engines [1][4]; the 20 mm cannon is replaced by the nose electronic-attack pallet [5].
- Role. The base dossier is a strike fighter. The Growler is airborne electronic attack [1][2]. It keeps a self-protection missile fit on the published armament line, AIM-120 and AGM-88 [1][2]. It is not a single-seat fighter and it is not an F-35.

### 6. GAME DATA CHECK

Quoted from `data/rules/unit-dimensions.json` and `data/roster/jslc.json` for `jslc.aircraft.ea-18g-growler` and `coalition.aircraft.ea-18g-growler`:

- lengthM 18.5, widthM 13.68, heightM 4.87.
- Source note: "EA-18G uses the Super Hornet outer mould line," citing https://www.navair.navy.mil/product/EA-18G-Growler.
- Roster basis: "representative". Mass is null.

Agree that 18.5 m, 13.68 m, and 4.87 m are the metre labels on the NAVAIR Growler card and the Navy fact file [1][2].

Disagree that those metres match the feet on those cards. The feet are 60.2 ft, 44.9 ft, and 16 ft [1][2]. Arithmetic check: 18.35 m, 13.69 m, and 4.88 m. Boeing prints 18.3 m, 13.7 m, and 4.9 m for the same feet [3].

Agree in part with "outer mould line." Boeing prints the same 60.2 ft, 44.9 ft, and 16 ft for the Super Hornet block and the Growler block [3]. NAVAIR prints the same span and height for the E/F and the G, but prints E/F length 60.3 ft and Growler length 60.2 ft [1][9]. The fetched NAVAIR Growler page says "F/A-18F Super Hornet platform" and "extensive commonality." It does not use the words "outer mould line" [1].

Agree that the published flight span is the same number for the E and the G. Disagree with any inference that the wingtip pods have been measured and found identical in span to the E's missile rails. No fetched page makes that measurement. A pod-versus-rail difference is not public, not disproved.

The E game note of folded span 32.6 ft is not on the Growler cards. Do not apply it to the G. Folded span remains not public, including folded width across the pods.

Agree with basis "representative" and with null mass. Empty weight 33,094 lb is published [1][2], but it was not entered as `massTonnes`. That is an omission relative to the fact file, not a contradictory mass. 33,094 lb = 15.011 metric tonnes by arithmetic check. It is not entered here as a game correction.

### 7. MASTER AI VIDEO PROMPT PACKAGE

Technical CAD blueprint isometric fly-around:
Render a two-seat EA-18G on a navy blueprint grid. Use the Super Hornet family shape: caret intakes, no leading-edge-extension fences, no dorsal speed brake, twin tails, and wing fold breaks. Replace both wingtip rails with receiver pods. Delete the nose cannon port and show a smooth nose fairing. External pods only. No internal bay and no chin sapphire fairing.

Electronic-attack fit:
Show wingtip receiver pods, under-wing jamming pods, and a tandem canopy with a pilot forward and an electronic-warfare officer aft. Do not state a pod count beyond the published loads, and do not mark station coordinates.

Carrier launch and arrested recovery:
Catapult launch with both afterburners lit, then an arrested landing. Wings may fold on deck. Do not state the fold angle. Do not open weapon-bay doors.

Formation and jamming pass:
Fly the jet with external pods in company with fighters. The receiver pods stay on the wingtips. No rotating nose radar. No distributed-aperture windows.

### 8. SOURCES

1. NAVAIR, "EA-18G Growler," Naval Air Systems Command, https://www.navair.navy.mil/product/EA-18G-Growler. Used for platform, dates, crew, F414 thrust, the 60.2 ft / 18.5 m card, empty weight, recovery weight, range, armament, and the mid-band pod caption.
2. U.S. Navy, "EA-18G Growler Airborne Electronic Attack Aircraft," fact file, updated 17 September 2021, https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2166036/ea-18g-growler-airborne-electronic-attack-aircraft. Used for the same specification card, the ALQ-218, ALQ-99, ALQ-227, Joint Tactical Terminal, and APG-79 names, and the older Next Generation Jammer status.
3. Boeing, "F/A-18 Super Hornet & EA-18 Growler," https://www.boeing.com/defense/fighters-and-bombers/fa-18-super-hornet-and-ea-18-growler. Used for the Growler block: 60.2 ft, 44.9 ft, 16 ft, recovery weight, Mach 1.8, spot factor 1.23, and 44,000 lb total thrust, and for the differing Super Hornet block on the same page.
4. GE Aerospace, "F414 Engine," https://www.geaerospace.com/military-defense/engines/f414. Used for the F414-GE-400 thrust class and the Growler application.
5. Frank Colucci, "Teeth of the Growler," Aviation Today, 1 March 2008, https://www.aviationtoday.com/2008/03/01/teeth-of-the-growler/. Used for wingtip ALQ-218(V)2 pods, deletion of the 20 mm cannon, nose pallet, up to five ALQ-99 pods, ALQ-227, INCANS, crew roles, March 2006 and August 2006 flights, and the 1,400 lb, cable, and antenna counts.
6. NAVAIR, "ALQ-99 Tactical Jamming System," https://www.navair.navy.mil/product/ALQ-99-Tactical-Jamming-System. Used for external carriage on the EA-18G and for retention until the Next Generation Jammer is fully fielded.
7. NAVAIR, "Next Generation Jammer," https://www.navair.navy.mil/product/Next-Generation-Jammer. Used for AN/ALQ-249 mid-band production dates and for low-band development status.
8. L3Harris, "EA-18G Interference Cancellation System (INCANS)," https://www.l3harris.com/all-capabilities/ea-18g-interference-cancellation-system-incans. Used for the function of INCANS. No installation coordinate.
9. NAVAIR, "F/A-18E/F Super Hornet," https://www.navair.navy.mil/product/FA-18EF-Super-Hornet. Used to compare length 60.3 ft, span, height, speed, and the E/F AESA statement with the Growler card.
10. NAVAIR, "F/A-18 A-D Hornet," https://www.navair.navy.mil/product/FA-18-D-Hornet. Used only to audit the legacy base card.
11. FlightGlobal, "F/A-18E/F: Balanced Upgrade," 20 January 1999, https://www.flightglobal.com/fixed-wing/1999/01/f-a-18e-f-balanced-upgrade/. Used for E/F airframe features the F-based Growler inherits where no Growler source contradicts them: caret inlets, no dorsal airbrake, no leading-edge-extension fences, spoilers, hook, and 11 E/F stations including wingtip rails.
12. General Dynamics Ordnance and Tactical Systems, "F/A-18 E/F 20mm Gatling Gun System," https://www.gdots.com/wp-content/uploads/2025/11/400003005-20mm-F-A-18-E-F-Gatling-Gun-System-ARMAMENT.pdf. Used to show the gun installation is specified for the E/F, not the G.
