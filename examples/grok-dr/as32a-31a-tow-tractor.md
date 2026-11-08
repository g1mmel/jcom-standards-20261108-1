---
generated_at: "2026-10-14T15:32:16-04:00"
generator: "dolphin2/dossier-grok-dr"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "xai"
models:
  - "grok-4.7"
query: "A/S32A-31A shipboard aircraft tow tractor versus A/S32A-32 spotting dolly, public particulars only"
sources_count: 8
asset_id: "as32a-31a-tow-tractor"
title: "Naval Architectural Blueprint Dossier: US Navy A/S32A-31A Aircraft Towing Tractor"
base_asset_id: "deck-tow-tractor"
---

# Naval Architectural Blueprint Dossier: US Navy A/S32A-31A Aircraft Towing Tractor

**Classification:** Unclassified. Public Navy training publications and a public FLIS extract. Not a NAVAIR drawing and not a substitute for NAVAIR 19-40-521.
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

The A/S32A-31A is the shipboard aircraft towing tractor that replaced the A/S32A-31. It is not the A/S32A-32 spotting dolly. NAVAIR 19-40-521 (January 1995) is the operation and intermediate-maintenance manual with IPB for the A/S32A-31A. The preoperational checklist is NAVAIR 19-600-287-6-1 and the periodic-maintenance requirements manual is NAVAIR 19-600-287-6-2. Both checklist titles in the June 1998 tow-tractor NTSP call the tractor "Shipboard A/S 32A-31A" [1]. The full text of NAVAIR 19-40-521 was not retrieved. Numbers below come from the NTSP physical-description table [1], NAVEDTRA 14014 chapter 9 [2][3], and the FLIS characteristic extract for NSN 1740-01-379-4633 [4].

### 1. MASTER COORDINATE DATUM & DIMENSIONS

glTF datum for a future mesh: forward = -Z, up = +Y, starboard/right = +X, port/left = -X, tire contact Y = 0. No station coordinate in this dossier is a measured pivot. Imperial-to-metric cells marked "converted" use 1 in = 0.0254 m, 1 lb = 0.45359237 kg, and 1 lbf = 4.4482216152605 N. They are not a second source.

| Parameter | Metric | Imperial | Engineering notes |
| --- | --- | --- | --- |
| Identity | Tractor, wheeled, aircraft towing, A/S32A-31A | same | NSN 1740-01-379-4633. P/N 3337AS100-1, CAGE 30003 (NAVAIR). Type designator A/S32A-31A, CAGE 80058. NSN assigned 31 Aug 1993. single-source for the date and CAGEs: WBParts [4]. The NSN, part number, and designator also appear on NSN Lookup [5]. |
| Role | Shipboard aircraft tow tractor | same | Designed for towing aircraft aboard ship [2]. NTSP: used aboard aircraft carriers and at Navy and Marine Corps air stations to maneuver and park aircraft and non-propelled support equipment, transport aircraft starting units, and pull arresting-gear cables. The 31 and 31A are used primarily to tow aircraft. A gas-turbine compressor may be mounted at the rear [1]. Delivery of the 31A to the fleet completed January 1998. It replaced the A/S32A-31 one-for-one. single-source for the date: NTSP [1]. |
| Basic length | 2.921 m converted from 115 in. Also 2.972 m converted from the FLIS figure 117 | 115 in (NTSP 31A line). FLIS: 117.000, labeled FEET NOMINAL | Disagreement. Do not average. NTSP appendix physical description, A/S 32A-31A: 115 inches length [1]. WBParts FLIS: OVERALL LENGTH 117.000 FEET NOMINAL [4]. The FEET label fails a volume check inside the same FLIS record: 117 x 65 x 36 / 1728 = 158.4375 cubic feet, and the record states cubic measure 158.4400 cubic feet [4]. Read as inches, 117 x 65 x 36 is the NTSP envelope of the predecessor A/S 32A-31, not the 31A line [1]. 115 in is single-source (NTSP). 117 is single-source (FLIS) and is the predecessor's length in the NTSP. |
| Width | 1.778 m converted from 70 in. Also 1.651 m converted from the FLIS figure 65 | 70 in (NTSP 31A). FLIS: 65.000, labeled FEET NOMINAL | Disagreement. NTSP 31A width 70 inches [1]. FLIS overall width 65.000 feet nominal [4]. 65 inches is the NTSP width of the A/S 32A-31 [1]. 70 in is single-source (NTSP). 65 is single-source (FLIS). |
| Height | 1.016 m converted from 40 in. Also 0.914 m converted from the FLIS figure 36 | 40 in (NTSP 31A). FLIS: 36.000, labeled FEET NOMINAL | Disagreement. NTSP 31A height 40 inches [1]. FLIS overall height 36.000 feet nominal [4]. 36 inches is the NTSP height of the A/S 32A-31 [1]. 40 in is single-source (NTSP). 36 is single-source (FLIS). Neither figure is a roll-guard or cab height. NAVEDTRA 14014 gives the 31A no enclosed cab [2]. |
| Ground clearance | 0.1905 m converted | 7.5 in | single-source: NTSP 31A line [1]. The predecessor 31 line in the same NTSP is also 7.5 in. That is not a second publication. |
| Turning radius | 3.353 m converted | 132 in | single-source: NTSP 31A line [1]. Same document gives the predecessor 31 the same 132 in. Swept radius and steering angle: not public. |
| Gross / unpackaged weight | 5,624.5 kg converted from 12,400 lb. Also 5,443.1 kg converted from 12,000 lb | 12,400 lb NTSP gross. 12,000.00 lb FLIS unpackaged unit weight | Disagreement. Do not average. NTSP 31A gross weight 12,400 pounds [1]. FLIS unpackaged unit weight 12,000.00 pounds [4]. 12,000 lb is the NTSP gross weight of the predecessor A/S 32A-31 [1]. 12,400 lb is single-source (NTSP). 12,000 lb on this NSN is single-source (FLIS). |
| Drawbar pull | 44.48 kN converted from 10,000 lbf. Also 37.81 kN converted from 8,500 lbf | 10,000 lb NTSP. 8,500.0 lb FLIS nominal | Disagreement. Do not average. NTSP 31A drawbar pull 10,000 pounds [1]. FLIS DRAWBAR PULL 8500.0 POUNDS NOMINAL [4]. 8,500 lb is the NTSP drawbar of the predecessor A/S 32A-31 [1]. Each figure is single-source. NAVEDTRA 14353A Table 2-3 was not retrieved, so it is not used as a second source. |
| Wheelbase, track, speed, steering angle, pintle height, horsepower, displacement, tire size, fuel capacity | not public | not public | The June 1998 NTSP table and NAVEDTRA 14014 chapter 9 do not state them [1][2]. A knowledge-pack draft that prints 91 in wheelbase, 101 hp, 12 mph, 85 gal, and tire pressures was not re-verified and is not copied [7]. |
| Shipping schema | not a vehicle envelope | 14,140 lb; 151 x 104 x 74 in | NSN Lookup shipping schema only [5]. Do not use it as length, width, height, or gross weight. |

### 2. RUNNING GEAR, HITCH OR TURRET, CREW

Fetched layout, NAVEDTRA 14014 chapter 9 [2], confirmed on the Integrated Publishing HTML of the same pages [3]:

- Drive: three-cylinder diesel engine, automatic transmission, rear-wheel drive with dual wheels.
- Steering: power-assisted front-wheel steering. The manual does not publish a steering angle.
- Brakes: hydraulic, power-operated, wet-disc service brakes, plus a mechanical hand brake for the rear wheels.
- Electrical: 24-volt system for starting, lighting, and instrumentation.
- Hitch: front and rear mounted pintles, used for aircraft towing [2]. Coupling is a pintle. The fetched pages do not describe a nose-gear clamp. That clamp is the A/S32A-32 spotting dolly [2][3].
- Rear interface: a universal jet-engine start unit mounts on the rear of the tractor [2]. The NTSP says a gas-turbine compressor may be mounted at the rear of the 31 and the 31A to supply compressed air for aircraft main-engine starters and air-conditioning systems [1]. The fetched pages do not name the start-unit model.
- Crew: seating for the driver only [2]. The sentence about a welded cab with a driver and one passenger belongs to the preceding A/S32A-30A paragraph. On the PDF it ends before the 31A heading [2]. The tpub HTML glues that cab sentence onto the 31A heading [3]. Do not give the 31A a two-person cab.
- Engine name: "Detroit Diesel, two-cycle, three cylinders" is single-source, the NTSP 31A line [1]. NAVEDTRA 14014 says "three-cylinder diesel" and "automatic transmission" and does not say Detroit, two-cycle, or a gear count [2]. Horsepower: not public.
- Gear count, wheelbase, and a numeric tire count: not public in the fetched pages. "Rear wheel drive with dual wheels" is the manual's wording [2]. The base dossier's "4-wheeled" claim is not what this manual says. An unretrieved NAVEDTRA 14353A extract says "conventional six-wheel vehicle." That sentence is not used, because the PDF was not fetched (pdf4pro returned 403).

No numeric station table. Axle offsets, kingpin coordinates, and pintle coordinates are not public.

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

Text tree of parts named in the fetched manuals. Motion in words. Travel is not public unless a source states it. No pivot XYZ.

```
A/S32A-31A_Tractor
|-- Frame (welded running gear; tie-down and lifting points are described on the preceding tractor in the same chapter, not measured here)
|   |-- Front axle, power-assisted steering, travel: not public
|   |-- Rear drive axle, dual wheels, wet-disc service brakes, mechanical hand brake, travel: not public
|   |-- Three-cylinder diesel (Detroit Diesel two-cycle: single-source NTSP)
|   |   |-- Automatic transmission, gear count: not public
|   |-- 24 V electrical system
|-- Operator station, driver only, side of the seat: not public
|-- Front pintle, aircraft tow, travel: not public
|-- Rear pintle, aircraft tow, travel: not public
|-- Rear mount for a universal jet-engine start unit / gas-turbine compressor, travel: not public
```

The tractor does not pivot the aircraft about a lifted nosewheel. That motion belongs to the A/S32A-32 [2].

### 4. SENSOR SITING OR DECK INTERFACE

There is no weapon, radar, or electro-optic sight on this tractor in the fetched sources.

Deck interface:

- The tractor couples to the aircraft through front and rear pintles [2]. A separate tow bar is the implied interface of a pintle tow. The fetched NTSP and NAVEDTRA 14014 do not name the ALBAR, do not list tow-bar lengths, and do not list a rated aircraft set. Those particulars are not public in the pages retrieved for this dossier.
- Places of use that are sourced: aircraft carriers, and Navy and Marine Corps air stations [1]. NAVEDTRA 14014 limits the design sentence to "towing aircraft aboard ship" [2]. A complete ship-class list (Nimitz, Ford, Wasp, America, or any LHA/LHD fit) is not public in these pages.
- Other sourced jobs, NTSP, not a second vehicle: move non-propelled support equipment, carry aircraft starting units, and pull arresting-gear cables aboard ships [1].
- The rear deck can carry a jet-engine start unit [2] or a gas-turbine compressor [1]. Added length and added weight of that configuration: not public. Do not copy 162 in, 168 in, 193 in, or 14,500–16,000 lb from the unsourced knowledge-pack draft [7].

### 5. DIFFERENCES FROM THE BASE DOSSIER

The filed base `deck-tow-tractor--328.md` is the A/S32A-32 spotting dolly. Its contrast paragraph is a claim, checked here against the NTSP [1] and NAVEDTRA 14014 [2][3].

- Base claim: "The A/S32A-31A is a heavier (12,400 lb), 4-wheeled tractor with a conventional steering wheel and rear-wheel drive designed for open flight-deck towing using rigid towbars." Corrected: 12,400 lb is the NTSP gross weight and is single-source [1]. The FLIS unpackaged weight on the 31A NSN is 12,000.00 lb [4]. "4-wheeled" is not in the fetched 31A description. The description is rear-wheel drive with dual wheels and power-assisted front-wheel steering [2]. Rigid towbars and an open flight deck are a fair reading of pintle towing aboard ship [1][2], but the pages do not say "rigid" or name a tow bar model.
- Base claim: the A/S32A-32 is a 3-wheeled ultra-low vehicle that lifts the nose landing gear with hydraulic clamp/lift arms and has zero-radius turning. This part holds as a role statement. NAVEDTRA 14014: the 32, also called the Spotting Dolly, spots aircraft inside the carrier hangar deck; a three-cylinder diesel drives two hydraulic pumps and independent wheel motors; a joystick controls speed and direction; a lift cylinder and two spread cylinders hold the arms on the nose gear with axle pins; it pivots on a caster wheel about its center within a zero turning radius [2][3]. NTSP: maximum maneuverability by moving the aircraft on its own main landing gear with the nose gear elevated, and the tractor can maneuver aircraft within a zero radius [1].
- Base dimensions for the 32 (LOA 148 in / 3.759 m, width 81 in / 2.057 m, chassis height 30 in / 0.762 m, roll-guard height 54 in, wheelbase 90 in "assumed", ground clearance 6 in, curb 7,000 lb, gross 11,500 lb) were not re-verified from NAVAIR 19-1-163. The fetched NTSP line for the A/S 32A-32 is: gross 11,200 lb, drawbar 10,000 lb, length 148 in, width 81 in, height 29 in, ground clearance 5 in, turning radius 0 in, liquid-cooled diesel, three cylinders [1]. Length 148 in and width 81 in agree with the base. Height, weight, clearance, and drawbar do not: the base prints 30 in, 11,500 lb, 6 in, and a 3,000/8,000 lbf drawbar pair that this pass did not find. The 54 in roll guard, 7,000 lb curb, 90 in wheelbase, and NSN 1740-01-270-3615 were not re-checked. Those base 32 numbers stay unverified. They are not 31A numbers.
- Base station-offset table and scene-graph XYZ for the 32 are not copied. No public station table for the 31A was found.
- The canon knowledge pack `carrier-tow-tractors.md` drafts many 31A figures (91 in wheelbase, 101 hp at 2,800 rpm, steering plus or minus 35 deg, 12 mph, 85 gal, 70/60 psig, ALBAR length table, LOA 193 in with bumpers). Its own 2026-10-09 review marks those draft numbers unresolved and warns not to merge the tractor, the huffer, the spotting dolly, or the crane [7]. This dossier does not promote them.

### 6. GAME DATA CHECK

Searched `C:\cnc_rev\data\rules\unit-dimensions.json` for as32a, tow-tractor, and deck-tow. There is no `as32a-31a` row.

These keys share one placeholder [8]:

- `jslc:shared:coalition.vehicle.deck-tow-tractor`
- `jslc:shared:deck-tow-tractor`
- `jslc:shared:TowTractor`
- `jslc:shared:FlightDeckTractor` (same numbers, seen adjacent in the file)

Each is lengthM 6, widthM 2.4, heightM 2.2, fit length, bandMinM 5.1, bandMaxM 6.9, source "UNVERIFIED. Manifest key had no roster row and no role map.", confidence low, designSize false [8].

That box is about 236 in long, 94 in wide, and 87 in high (converted at 0.0254 m per inch: 6/0.0254 = 236.2 in, 2.4/0.0254 = 94.5 in, 2.2/0.0254 = 86.6 in). It matches neither factory line retrieved here:

- 31A NTSP: 115 x 70 x 40 in [1]
- 31A FLIS numbers if the feet label is ignored: 117 x 65 x 36 [4]
- 32 NTSP: 148 x 81 x 29 in [1]

The game size is the spotting-dolly asset key with an unverified placeholder. It is not a factory sheet for the 31A, and it does not match the 32 either. It is longer, wider, and much taller than both.

### 7. MASTER AI VIDEO PROMPT PACKAGE

1. Flight-deck daylight, photoreal, a low yellow US Navy A/S32A-31A tow tractor with dual rear tires, one driver, and a front pintle. No nose-gear clamp and no zero-radius spin. An aircraft tow bar is in the pintle. Non-skid deck, no readable tail numbers.

2. Hangar-bay contrast, same carrier: the A/S32A-31A stays on the tow bar, while a separate low A/S32A-32 spotting dolly lifts a nosewheel with clamp arms and pivots on its caster. Do not give the 31A the dolly's arms.

3. Close view of the 31A operator station: one seat, steering wheel, no passenger cab. Wet-disc brake hardware is not shown in cutaway unless the shot stays exterior. 24-volt lights on.

4. Rear three-quarter of the 31A with a jet start unit sitting on the rear deck and the rear pintle still visible. No invented bumper-to-bumper length callout on screen.

### 8. SOURCES

1. Navy Training System Plan, Tow Tractors, N88-NTSP-A-50-8411B, June 1998. Naval Air Systems Command, hosted by GlobalSecurity. https://www.globalsecurity.org/military/library/policy/navy/ntsp/Towtractor.pdf — Role, January 1998 delivery, 31A and 31 and 32 physical-description lines, gas-turbine compressor, manual numbers NAVAIR 19-40-521 and 19-600-287-6-1/6-2, zero-radius description of the 32.
2. NAVEDTRA 14014, Airman, Chapter 9, Support Equipment. Naval Education and Training, PDF hosted by GlobalSecurity. https://www.globalsecurity.org/military/library/policy/navy/nrtc/14014_chp9.pdf — 31A drive, steering, brakes, 24 V, driver only, front and rear pintles, rear start unit. 32 spotting-dolly hydraulics and zero turning radius. Shows the two-person cab sentence belongs to the A/S32A-30A.
3. Integrated Publishing HTML of the same NAVEDTRA 14014 pages. https://navyaviation.tpub.com/14014/css/A-S32A-31A-Aircraft-Towing-Tractor-216.htm and https://navyaviation.tpub.com/14014/css/A-S32A-32-Aircraft-Towing-Tractor-217.htm — Same sentences as source 2. The 31A HTML page concatenates the 30A cab sentence in front of the 31A heading. Not an independent measurement.
4. WBParts, NSN 1740-01-379-4633, Aircraft Towing Wheeled Tractor. https://www.wbparts.com/rfq/1740-01-379-4633.html — FLIS: NSN date 31 Aug 1993, CAGE 30003 and 80058, drawbar 8500.0 lb nominal, overall length/width/height 117.000 / 65.000 / 36.000 feet nominal, cubic measure 158.4400 cubic feet, unpackaged unit weight 12000.00 lb.
5. NSN Lookup, 1740-01-379-4633. https://www.nsnlookup.com/fsg-17/fsc-1740/us/1740-01-379-4633-tractor-wheeled-aircraft-towing-1740013794633-013794633-3337as100-s32a-31a — Identity and a shipping schema (14140 lb, 151 x 104 x 74 in). The characteristic table was not on the fetched page. The FSC class boilerplate is not a 31A crew or winch fact.
6. Base dossier under audit, `deck-tow-tractor--328.md`, local temp path `C:\Users\MAXGLA~1\AppData\Local\Temp\grok-dr-bases\deck-tow-tractor--328.md` — Contrast paragraph and 32 envelope claims. Not a measurement source for the 31A.
7. Canon knowledge pack `C:\cnc_rev\canon\reference\eretz\dossiers\naval-expert-references\carrier-tow-tractors.md` — Draft 31A numbers and the 2026-10-09 review that leaves them unresolved. Not used as a measurement source.
8. `C:\cnc_rev\data\rules\unit-dimensions.json` — Unverified deck-tow placeholder 6 x 2.4 x 2.2 m. No as32a-31a row.
