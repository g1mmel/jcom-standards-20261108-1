# Research log: fa-18e-super-hornet

- Start local time: 2026-10-14T15:14:39-04:00
- End local time: 2026-10-14T15:27:18-04:00
- Search count: 17
- Fetch count: 7 successful page reads. Failed fetches are listed and were replaced or left unused.

## Queries

1. site:navy.mil F/A-18E/F Super Hornet fact file length wingspan height weight
2. site:navair.navy.mil F/A-18E/F Super Hornet specifications length span height
3. Boeing F/A-18 Super Hornet fact sheet length wingspan height wing area weight
4. F/A-18E Super Hornet empty weight maximum takeoff weight 66000 pounds Navy
5. F/A-18E Super Hornet folded wingspan 30 feet OR 32 feet wing fold
6. F/A-18E AN/APG-79 AESA radar nose Raytheon NAVAIR Block II
7. F/A-18E F414-GE-400 thrust 22000 pounds two engines General Electric
8. F/A-18E M61A2 20mm cannon 412 rounds weapon stations pylons wingtip AIM-9
9. F/A-18E Super Hornet dorsal speed brake deleted LEX spoiler aerodynamic braking
10. F/A-18E Super Hornet retractable refueling probe starboard wing fold mechanism
11. "F/A-18E" "500 sq ft" OR "500 square" wing area Boeing OR Navy OR NAVAIR
12. Congressional Research Service F/A-18E/F Super Hornet EA-18G Growler background dimensions
13. F/A-18E Block II AN/APG-79 Block I AN/APG-73 no internal weapons bay external stores
14. F/A-18E caret intake rectangular LEX no fence 11 weapon stations Boeing
15. F/A-18E/F NATOPS dimensions "60 ft" length wingspan folded height figure
16. GAO F/A-18E/F Super Hornet weight empty maximum gross 66000
17. site:boeing.com F/A-18 Super Hornet 11 weapons stations length 60.3 OR "60 feet"

Query 12 is shared with the Growler log because the query text names both aircraft. It did not return a CRS dimension table.

## Fetches

Successful:

1. https://www.navair.navy.mil/product/FA-18EF-Super-Hornet — title "F/A-18E/F Super Hornet | NAVAIR". Gave crew, Block II AESA, Block III, two F414-GE-400 at 22,000 lb (9,977 kg), length 60.3 ft (18.5 m), height 16 ft (4.87 m), span 44.9 ft (13.68 m), MTOW 66,000 lb (29,932 kg), Mach 1.8+, ceiling 50,000+ ft, combat range 1,275 nm (2,346 km), ferry 1,660 nm (3,054 km), M61A1/A2.
2. https://www.navair.navy.mil/product/FA-18-D-Hornet — title "F/A-18 A-D Hornet | NAVAIR". Gave the legacy card used to audit the base: 56 ft (16.8 m), 15 ft 4 in (4.6 m), 40 ft 5 in (13.5 m), 51,900 lb (23,537 kg), two F404-GE-402 at 17,700 lb.
3. https://www.boeing.com/defense/fighters-and-bombers/fa-18-super-hornet-and-ea-18-growler — title "F/A-18 Super Hornet & EA-18 Growler". The fetch of the Growler URL returned this combined page. Super Hornet block: width 44.9 ft (13.7 m), length 60.2 ft (18.3 m), height 16 ft (4.9 m), MTOW 66,000 lb (29,937 kg), Mach 1.6, bring-back E 9,900 lb and F 9,000 lb, thrust each engine up to 17,000 lb, 11 weapons stations.
4. https://www.geaerospace.com/military-defense/engines/f414 — title "F414 Engine | GE Aerospace". Gave 22,000 lb thrust class, length 154 in, diameter 35 in, airflow 170 lb/sec, pressure ratio 30:1, and the F/A-18E/F application.
5. https://www.flightglobal.com/fixed-wing/1999/01/f-a-18e-f-balanced-upgrade/ — title "F/A-18E/F: Balanced Upgrade". Gave the 34 in / 860 mm stretch, 500 ft2 / 46 m2 wing, 11-station split, caret inlets, deleted dorsal airbrake, LEX spoilers, no LEX fences, APG-73, ATFLIR status, arresting hook, and specification empty weight 13,860 kg.
6. https://www.gdots.com/wp-content/uploads/2025/11/400003005-20mm-F-A-18-E-F-Gatling-Gun-System-ARMAMENT.pdf — GD-OTS E/F gun sheet. Gave M61A2, nose pallet, 412 rounds, 4,000/6,000 shots per minute.
7. https://www.navair.navy.mil/node/11616 — title "AESA Second Low-Rate Initial Production Contract Awarded". Gave AN/APG-79, Raytheon, Block II, replacement of mechanically scanned antennas.

Failed, and what replaced them:

- https://www.cnatra.navy.mil/tw6/vt86/aircraft-FA18F.asp — fetch failed. Search extract only. Not used as a certified figure. The extract showed 60 ft 4 in, 44 ft 11 in, empty 32,081 lb, and thrust 20,000 lb per engine.
- https://www.usni.org/magazines/proceedings/1995/november/special-fa-18ef-update — blocked. Search extract only. Not used as a certified figure. The extract showed 60.3 ft, 16 ft, 44.9 ft with wingtip missiles, 500 square feet, empty about 30,500 lb, M61A1 with 400 rounds, and 11 stations.
- https://www.history.navy.mil/content/dam/nhhc/research/histories/naval-aviation/Naval%20Aviation%20News/1990/1997/may-june/hornet.pdf — open failed. Search extract only. The extract is the only place 32.6 ft folded span appeared. Not used as a certified figure.
- https://navalaviationnews.navy.mil/DesktopModules/ArticleCS/Print.aspx?PortalId=59&ModuleId=80178&Article=4345217 — access denied.
- https://www.history.navy.mil/content/history/nhhc/research/histories/naval-aviation-history/naval-aircraft/current-aircraft-inventory/f-a-18-hornet.html — open failed.
- https://www.pprune.org/military-aviation/6596587-post11.html — thread missing. The search extract quoted a NATOPS speed-brake passage and a 60 degree spoiler figure. Because the page did not open, 60 degrees was not used.
- NATOPS manuals on publicintelligence.net were not fetched. No NATOPS figure plate was opened. The 60 ft 1.25 in / 18.31 m family was not certified.

## Numbers that failed the two-source test

- 18.5 m versus 60.3 ft on one NAVAIR card. Boeing's 60.2 ft / 18.3 m is a second publisher and disagrees.
- Boeing thrust "up to 17,000 lb" per engine versus NAVAIR and GE at 22,000 lb class.
- Boeing Mach 1.6 versus NAVAIR Mach 1.8+.
- NAVAIR MTOW kilogram 29,932 versus Boeing 29,937 versus FlightGlobal 30,000 kg. Pounds agree at 66,000.
- NAVAIR range pairs 1,275 nm / 2,346 km and 1,660 nm / 3,054 km do not convert at 1.852 km per nautical mile.
- Wing area 500 ft2 / 46 m2: one fetched source, FlightGlobal.
- Fuselage stretch 34 in, station split, 8,050 kg stores, 6,560 kg internal fuel, specification empty weight 13,860 kg, caret inlets, deleted dorsal brake, no LEX fences: FlightGlobal only.
- M61A2 round count 412, rates, and pallet inches: GD-OTS only. NAVAIR says M61A1/A2 and gives no round count.
- Folded span, fold angle, sweep, dihedral, wheelbase, wheel track, hook angle, launch-bar length, refuelling-probe side, radar tilt, and T/R module count: not public on fetched pages.
- Empty weight 32,081 lb, 30,564 lb, and about 30,500 lb: search extracts only, and they disagree. Not used.
- Control-surface angles and rates in the local knowledge pack, including 95 degree fold, 60 degree spoiler, 20 degree radar tilt, and station butt lines: not re-verified. Not copied.

## Contradictions versus the base dossier

- Base length 17.070 m, span 12.310 m, folded span 8.380 m, height 4.670 m, wing area 37.160 m2, and MTOW 23,541 kg are legacy-Hornet figures. They are not the E. The current A-D card prints 56 ft, 40 ft 5 in, 15 ft 4 in, and 51,900 lb, and its own metre labels do not match those feet.
- Base sweep, anhedral, chine angle, loft table, and surface angles are not on a fetched page.
- Base APG AESA, EOTS sapphire fairing, distributed aperture, internal bays, and wingtip ESM pods are not the E. Early E/F radar was the mechanical APG-73. Block II and later use the APG-79. Targeting was described as a pod. Wingtips are missile rails. Stores are external.
- Base dorsal speed brake and 60 degree spoiler travel. FlightGlobal says the dorsal airbrake was deleted. The 60 degree figure was not confirmed.

## Game conflicts

- Game 18.5 / 13.68 / 4.87 m matches NAVAIR's printed metres and not the feet on that card, and not Boeing's metres.
- Game folded span 32.6 ft (9.94 m) was not confirmed by a fetched page.
- Roster basis "representative" matches the disagreement. Null mass matches the lack of a fetched operational empty weight.
