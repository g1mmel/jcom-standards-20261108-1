---
generated_at: "2026-10-14T15:32:42-04:00"
generator: "dolphin2/dossier-grok-dr"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "xai"
models:
  - "grok-4.7"
query: "Royal Navy Type 26 City-class public dimensions and fit, separated from coalition-dossier inventions"
sources_count: 12
asset_id: "coalition-frigate-type26"
title: "Naval Architectural Blueprint Dossier: Royal Navy Type 26 City-Class Frigate (Coalition Type 26)"
base_asset_id: "nato-type26-frigate"
---

# Naval Architectural Blueprint Dossier: Royal Navy Type 26 City-Class Frigate (Coalition Type 26)

**Classification:** Open-source architectural reference for the Royal Navy City-class Type 26. Not a lines plan. There is no separate public "coalition Type 26" hull or weapon fit. Australian Hunter-class and Canadian River-class / CSC ships are Type 26 derivatives with different published particulars and are not used as City-class numbers.

**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

The asset is the same Type 26 / City-class hull family as the base dossiers. Shared facts below were re-checked. Body-plan stations, pivot coordinates, deadrise, tumblehome, stem rake, and knuckle heights from the base dossiers are not repeated. Those tables are modeled, not public drawings.

### 1. MASTER COORDINATE DATUM & DIMENSIONS

glTF convention used here: bow = -Z, up = +Y, starboard = +X, port = -X, design waterline Y = 0. No public source fetched for this dossier states a draft, so the keel is not given a negative Y. A keel offset of -6.5 m or -7.0 m would invent a draft.

| Parameter | Metric | Imperial | Engineering notes |
| --- | --- | --- | --- |
| Length overall | 149.9 m | 491 ft 10 in, converted from 149.9 m, not a separate measurement | Naval Technology and Navy Lookout both publish 149.9 m and beam 20.8 m [4][5]. The BAE Systems product-page search extract agrees: length 149.9 metres, maximum beam 20.8 metres [8]. The Royal Navy equipment page rounds length to 149 metres and does not state beam [1]. A Royal Navy news sentence rounds the same class to 150 m [3]. The base value 149.900 m adds millimetre precision that these pages do not print. |
| Length between perpendiculars | not public | not public | Not stated on the Royal Navy, Naval Technology, or Navy Lookout pages fetched. Base values 140 m and 142 m are not public. |
| Moulded / maximum beam | 20.8 m | 68 ft 3 in, converted from 20.8 m, not a separate measurement | Dual-source as above [4][5], with the BAE search extract agreeing [8]. The base value 20.800 m is the same figure with unstated millimetre precision. |
| Waterline beam | not public | not public | Base values 19.5 m and 19.0 m were not found. |
| Draft, any condition | not public | not public | Navy Lookout's Norwegian-variant page, seen in search, prints draft as unknown. No Royal Navy or Naval Technology Type 26 page fetched gives a draft. Keel Y is therefore not public. |
| Air draft to masthead | not public | not public | Base values 35.000 m to a TACAN apex and 38.500 m were not found as masthead air draft. |
| Primary-radar height | about 35 m above the waterline | converted about 115 ft, not a separate measurement | Single-source: Navy Lookout, siting of the Artisan antenna, not the masthead and not a TACAN radome [5]. |
| Displacement | 6,900 tonnes, and also 8,000 tonnes | not published as long tons on the pages fetched | Do not average. Royal Navy equipment page: 6,900 tonnes, load condition not named [1]. Naval Technology: 6,900 t [4]. Navy Lookout guide: "officially displacing 6,900 tonnes" [5]. Royal Navy news, 4 July 2025: "150m long, 8,000 tonnes apiece" [3]. Navy Lookout's mission-bay article says the Chinook-capable flight deck drives displacement to about 8,000 tonnes [7]. The base label "full load 8,000 t" uses a load condition the 8,000-tonne sentences do not state. |
| Flight deck | Chinook-capable; circa 30 m by 20 m is single-source | not published | Capability is on the 2017 Royal Navy announcement and on Naval Technology [2][4]. The circa 30 m by 20 m figure is Navy Lookout only [7]. A later Navy Lookout caption says the flight deck is "about 55 m2" [5]. That area conflicts with a circa 30 m by 20 m deck and with Chinook operations, so 55 m2 is not used. |
| Mission bay | about 20 m wide by 15 m long | not published | Single-source Navy Lookout [7]. Full width of the ship, side access. Not a length-between-perpendiculars or a station spacing. |

Hunter-class figures are a different hull and are excluded from the table: BAE Systems Australia publishes length 151.4 m, approximate light-ship displacement 8,200 t, and top speed 27 knots [12].

Station offsets are not public.

### 2. GENERAL ARRANGEMENT AND ARMAMENT

Eight City-class ships are named for the Royal Navy: HMS Glasgow (F88), Cardiff (F89), Belfast (F90), then Birmingham, Sheffield, Newcastle, Edinburgh, and London [1]. The 2017 contract was for the first three; a later contract covered five more [4]. As of the Navy Lookout guide update of July 2026, HMS Glasgow was fitting out, with sea trials described as expected in late 2026 or early 2027, and the Royal Navy equipment page still places the first three in the fleet before 2030 [1][5]. That is a programme status, not a lines-plan date.

The Royal Navy fit, which is the public fit for this hull, is a quiet anti-submarine frigate with a CODLOG plant (Navy Lookout spells the same arrangement CODELOG): one Rolls-Royce MT30 gas turbine direct-drives the shafts for higher speed, or the turbine is declutched and two electric motors on the shaft lines are fed by up to four diesel generators [1][4][6]. It is one gas turbine, not two. A secondary page that says two MT30s is rejected because the Royal Navy, Naval Technology, and Navy Lookout each describe one [1][4][6].

The foredeck gun is a 127 mm Mk 45 Mod 4 [4][5]. Air defence is Sea Ceptor, but the cell count is disputed and is printed both ways below. Strike-length launch is a 24-cell Mk 41 [1][5][10]. Close-in guns on the Navy Lookout fit are two Phalanx Block 1B and two 30 mm automated small-calibre guns [5]. Naval Technology names the Mk 45 Mod 4 and two Phalanx mounts and, in that weapons paragraph, small arms rather than the 30 mm mounts [4]. The mission bay is a full-width space with roll-up doors each side and a separate port boat bay, not a stern well deck [5][7][9]. The hangar is described as taking a Merlin or two Wildcats, with a Chinook able to land but not to be housed [7]. Naval Technology instead describes a main hangar for a Merlin or Wildcat and a secondary hangar for a UAV [4]. Both descriptions are printed. No numeric body plan is available. Station offsets are not public.

| Item | Public fit | Notes |
| --- | --- | --- |
| Gun | 1 x 127 mm / 5-inch Mk 45 Mod 4 | Naval Technology and Navy Lookout [4][5]. The 2017 Royal Navy release says only "a 5ins main gun" [2]. Naval Technology's 20 nm firing range is single-source and is not repeated as a checked figure. Train, elevation, and recoil: not public. |
| Sea Ceptor | 48 missiles. Cell count: 12 cells, or two 24-cell modules | Royal Navy equipment page: 12 VLS cells, four Sea Ceptors per cell, 48 missiles, plus 24 Mk 41 cells [1]. Navy Lookout: two separated 24-cell Sea Ceptor modules, one below the bridge and one abaft the funnel, 48 missiles, and a theoretical 144 if the 24 Mk 41 cells were also quad-packed [5]. Not averaged. The base "48-cell" scene node matches only the Navy Lookout cell count. |
| Mk 41 | 24 cells (three 8-cell modules) | Royal Navy page [1], Navy Lookout [5], and Shephard reporting the Lockheed Martin modules for the first three ships [10]. What is embarked in those cells is not fixed in the sources. Navy Lookout treats FC/ASW (Stratus LO) as the likely first outfit, not as a missile already at sea [5]. |
| 30 mm | 2 x 30 mm ASCG | Navy Lookout guide [5]. The same publisher's 30 mm article, seen in search, identifies the Type 26 mounts as DS30M Mk II removed from Type 23s. Train and elevation: not public. |
| CIWS | 2 x Phalanx Block 1B | Navy Lookout [5]. Naval Technology says two Phalanx CIWS without the block number [4]. |
| Radar | Artisan 3D / Type 997 | Royal Navy and the BAE search extract say Artisan 3D [1][8]. Naval Technology says Type 997 Artisan [4]. More than 800 tracks and about 200 km are on both the Royal Navy page and Navy Lookout's report of the BAE claim [1][5]. Rotation rate: not public. |
| Sonar | Sonar 2087 towed array; Sonar 2150 bow set | Both names are on Naval Technology [4]. The BAE search extract lists Sonar 2087 [8]. The Royal Navy page describes a towed array with active and passive detection and torpedo warning, without the type number [1]. A 2023 Naval Technology news item says all eight ships are to receive Type 2150 and that it replaces Type 2050 [11]. A 2017 secondary claim of a Type 2050 bow sonar is the legacy set, not the current contract. |
| Other sensors named by one detailed source | Terma SCANTER; Raytheon navigation radar; three Sea Eagle FCEO mounts; MEWSIC / UAT; Sonar 2170 torpedo defence; Ancilia decoys | SCANTER and a navigation radar are on Naval Technology [4]. The FCEO count and the decoy/torpedo-defence names are Navy Lookout [5]. SCOT-5 was not on the Royal Navy or BAE extracts used here and is not treated as checked. |
| Aviation | Merlin or Wildcat in the hangar; Chinook on the flight deck; UAV space also described | See the hangar disagreement above [2][4][7]. |
| Mission bay | Side doors, port boat bay, overhead handler | Four 12 m boats or up to 11 twenty-foot containers is a BAE description quoted by UK Defence Journal [9]. Navy Lookout also says about 20 m by 15 m, MBHS capacity 15 tonnes, and a separate 10-tonne at-sea launch figure in a later article from the same publisher [5][7]. Door travel: not public. |
| Propulsion | CODLOG: 1 x MT30, 4 x MTU 20V 4000 M53B generator sets, 2 x electric motors | Royal Navy, Naval Technology, Navy Lookout [1][4][6]. About 3 MW electric per generator set is Navy Lookout [6]. 3,015 kW mechanical per set was seen only in a Marine Log search extract and is not used as a checked figure. 36 MW as the limited MT30 output is single-source Navy Lookout [6]. Rolls-Royce's product page lists 36 MW or 40 MW as family ratings, which is not a second ship-specific source. |
| Propellers | Fixed, two shaft lines, one bracket per shaft | Single-source for "fixed" and for the bracket: Navy Lookout [6]. The base controllable-pitch propellers are not supported. Blade count for the Type 26 is not public. Navy Lookout's five-blade remark is about the Type 23. |
| Crew | Core 157; accommodation 208 | Royal Navy, 2 July 2017: typically 157, space for up to 208 [2]. Naval Technology: complement 157 and berths for 51 embarked [4]. Navy Lookout: core 157 and space for about another 50 [5]. The equipment page states accommodation for 208 [1]. An older "118" complement on secondary pages is not the current Royal Navy or Naval Technology figure. |
| Speed | 26 knots; also "more than 26 knots"; also "at least 28 knots" | Royal Navy equipment page: 26 knots [1]. Naval Technology: more than 26 knots [4]. BAE search extract: 26+ knots [8]. Navy Lookout: one MT30 can drive the 6,900-tonne ship to at least 28 knots [6]. Not averaged. |
| Range | 7,000 nautical miles; also "more than 7,000 nm" | Royal Navy: 7,000 nautical miles [1]. Naval Technology: more than 7,000 nm [4]. BAE search extract: in excess of 7,000 nautical miles in electric-motor drive [8]. |
| Endurance | 60 days | Naval Technology [4]. UK Defence Journal's 2018 guide, in the search extract, also says 60 days [9]. |

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

Text tree of equipment that the sources actually name. Motion is described in words. No pivot XYZ is stated because none was published.

- Hull, design waterline Y = 0. Keel Y: not public.
  - Machinery. One MT30 in an acoustic enclosure, clutched through a splitter gearbox and two reduction gearboxes for the sprint mode [6]. Four MTU generator sets in acoustic enclosures, two of them described as above the waterline [6]. Two GE induction motors on the shaft lines for the quiet mode [4][6]. Clutch travel: not public. Uptakes and funnels exist; Navy Lookout says removal rails are in the air downtakes and that exhaust cooling in the uptakes is likely [6]. Coordinates: not public.
  - Shaft lines. Two fixed propellers, one bracket each, single-source [6]. Rotation about the shaft. Pitch mechanism: not supported. Rudders and fin stabilisers are fitted [6]; angles: not public.
  - Mk 45 Mod 4, foredeck [5]. Train and elevation: not public. Recoil stroke: not public.
  - Sea Ceptor silo or silos. Count disputed, section 2. Hatch motion: not public. Mk 41, 24 cells, forward of the Sea Ceptor arrangement described by Navy Lookout [5]. Hatch motion: not public. No midships box launcher was found.
  - Two Phalanx Block 1B and two 30 mm mounts [5]. Train and elevation: not public. Navy Lookout places a Phalanx near the funnel in a photograph caption and places an electro-optical mount on each side of the hangar for the 30 mm guns [5]. Coordinates: not public.
  - Hangar door and flight deck. Door travel: not public. The deck is Chinook-capable [2][4].
  - Mission bay. Roll-up doors port and starboard, MacTaggart Scott named by Navy Lookout, plus a door into the hangar [7]. A separate boat bay is on the port side only [7]. The handler traverses on athwartship overhead rails and slews, lifts, and telescopes, with a constant-tension winch [5][7]. Travel distances: not public. This is not a well-deck ramp.
  - Artisan, rotating, on the composite mast [5]. Rate: not public. Bow sonar in a fibreglass dome; towed array worked from the quarterdeck under the wide transom [5][7]. Deployed length: not public.

### 4. SENSOR SITING

Coordinates are not public.

Artisan is on the enclosed composite mast. Navy Lookout says that placement puts the primary radar about 35 m above the waterline [5]. That sentence is not a masthead air draft and does not mention a TACAN radome. The base TACAN-at-35 m claim does not hold as written.

The towed-array winch is on the quarterdeck, under a wide transom that Navy Lookout says does not taper, with the bow array in a fibreglass dome forward [5][7].

Navy Lookout's 2022 fit places one electro-optical director forward for the 5-inch gun and one on each side of the hangar for the 30 mm guns, and it shows a satcom sponson in a photograph caption [5]. The same caption says the electro-optical mount on that sponson has likely been deleted. Bilateral satcom coordinates in the base dossiers are not public. ESM aerials are described at the top of the mainmast, without coordinates [5].

Sea Ceptor is either 12 cells whose deck position the Royal Navy page does not give [1], or one module below the bridge and one abaft the funnel [5]. Mk 41 is the forward multi-purpose silo in the Navy Lookout arrangement [5]. The Mk 45 is the foredeck gun [5].

### 5. DIFFERENCES FROM THE BASE DOSSIER

The base set is four files: the HMS Glasgow blueprint (149.900 m, LBP 140 m, beam 20.800 m, waterline beam 19.5 m, keel -6.5 m, air draft 35 m, 8,000 t), the coalition master (LBP 142 m, waterline beam 19.0 m, keel -7.0 m, air draft 38.5 m, well deck, box launcher), the NATO master (LBP 142 m, keel -7.0 m, air draft 38.5 m), and a glTF measurement sheet. Station tables and pivot coordinates from all four are modeled. They are not corrected here number by number because they are not public drawings.

Holds, re-verified:

- Length 149.9 m and beam 20.8 m hold as published metres, not as 149.900 m and 20.800 m [4][5].
- A 5-inch Mk 45, a 24-cell Mk 41, Sea Ceptor giving 48 missiles, Artisan, a mission bay, and a gas-turbine installation all hold in substance [1][4][5]. The Sea Ceptor cell count does not hold as a single number.
- Core crew 157 and space for 208 hold [2][4].
- Two electric motors, four diesel generators, and one gas turbine hold [1][4][6].
- The mesh audit's inclusion of both DS30M and Phalanx node names agrees with the Navy Lookout gun fit [5]. That agreement is about equipment names, not about the mesh coordinates.

Does not hold, or was not public:

- Base: full-load displacement 8,000 t as a single figure. Corrected claim: 6,900 tonnes is the figure the Royal Navy equipment page, Naval Technology, and the Navy Lookout guide call the displacement or the official displacement [1][4][5]. 8,000 tonnes is also printed by a Royal Navy news item and by Navy Lookout's mission-bay article, without the words "full load" [3][7].
- Base: LBP 140 m, and in other base files 142 m. Corrected claim: not public.
- Base: waterline beam 19.5 m or 19.0 m. Corrected claim: not public.
- Base: keel Y = -6.5 m "navigational draft including sonar dome", or -7.0 m. Corrected claim: draft is not public, so keel Y is not public.
- Base: air draft 35 m to a TACAN apex, or 38.5 m. Corrected claim: masthead air draft is not public. The only related figure is Navy Lookout's "about 35 m" to the Artisan antenna [5].
- Base: stem rake, deadrise, tumblehome, and knuckle heights. Corrected claim: not public.
- Base: Sea Ceptor as a 48-cell block at one modelled station. Corrected claim: 48 missiles, with cells stated as 12 by the Royal Navy and as two 24-cell modules by Navy Lookout [1][5].
- Base: controllable-pitch propellers and rudders at +/-35 degrees. Corrected claim: Navy Lookout says fixed propellers [6]. Rudder angle is not public.
- Base: Artisan at 30 rpm and a navigation radar at 24 rpm. Corrected claim: rates are not public.
- Base: gun elevation, recoil stroke, and mission-bay door slide of 5.0 m. Corrected claim: not public.
- Coalition master: a well-deck ramp. Corrected claim: UK Defence Journal, quoting the design history, says the adopted BAE design has a mission bay instead of the stern well deck of earlier studies [9]. Navy Lookout describes side doors and a wide transom used for the towed array [7].
- Coalition master: a midships box launcher fixed at 30 degrees elevation, and a scene-graph bank of 32 launch cells. Corrected claim: neither was found. The public launcher counts are the disputed Sea Ceptor cells plus 24 Mk 41 cells [1][5].
- Coalition master and NATO master: hull angles and a 19 m-class waterline beam. Corrected claim: not public.
- Base sensor coordinates, including SATCOM at X = +/-10.5 m and named Y heights for directors. Corrected claim: not public.
- Flight-deck paint specified as unlit #00FF00. Corrected claim: not an RN publication used here. It is a game-marking convention in the mesh audit, not a ship fact.

### 6. GAME DATA CHECK

no unit-dimensions row

no roster row

Searches of `C:\cnc_rev\data\rules\unit-dimensions.json` and `C:\cnc_rev\data\roster\jslc.json` for type26, type-26, and city-class found no row.

The mesh verification base is not a rules row. It records a glTF bounding length of 149.9 m, which matches the published overall length, a bounding width of 22.89 m, which is wider than the published 20.8 m beam, a bounding height of 39.21 m, which is not a published air draft, and a lowest vertex at Y = -5.5 m, which is not a published draft. Submesh extents in that audit run to hundreds of metres and are not ship dimensions. Those telemetry numbers are model measurements, not a second public source for the hull.

### 7. MASTER AI VIDEO PROMPT PACKAGE

1. Technical fly-around of a Royal Navy City-class Type 26 frigate in blueprint linework, bow to the near lower corner, mast up, starboard to the right. Show a foredeck gun, forward vertical-launch hatches, a mast radar, side mission-bay doors, and a wide flight deck. Do not letter dimensions onto the hull. No well deck.

2. Close view of the foredeck as the 5-inch turret trains and a vertical-launch hatch opens. Keep cell counts off the picture. Grey angular surfaces, overcast light, no invented elevation angle.

3. The same frigate in a head sea, bow wave along the topsides, gas-turbine uptake aft of the mast, and a wake from two screws. Do not show a controllable-pitch mechanism and do not show a stern ramp.

4. Night approach to the flight deck. Hangar door open, deck-edge lights on, a Merlin-sized helicopter over the deck. No specific paint formula and no numeric deck size.

### 8. SOURCES

1. Royal Navy, "City Class Type 26 Anti-Submarine Frigate", https://www.royalnavy.mod.uk/equipment/ships/city-class . Used for 6,900 tonnes, 149 metres, 26 knots, 7,000 nautical miles, crew accommodation 208, Artisan 3D, 12 Sea Ceptor cells and 48 missiles, 24 Mk 41 cells, one gas turbine, four diesel generators, two electric motors, and the ship's names and pennants for the first three.

2. Royal Navy, "Multi-billion pound deal signed for first three new Type 26 frigates", 2 July 2017, https://www.royalnavy.mod.uk/news/2017/july/02/170702-deal-for-t26-frigates . Used for core crew 157, space for 208, 5-inch gun, Sea Ceptor, bow and towed sonar, mission bay, and Chinook-capable flight deck with Merlin or Wildcat as the usual aircraft.

3. Royal Navy, "Gimme shelter: new frigate HMS Belfast moves under cover for completion", 4 July 2025, https://www.royalnavy.mod.uk/news/2025/july/04/20250704-new-frigate-hms-belfast-moves-under-cover-for-completion . Used for the conflicting 150 m and 8,000 tonnes sentence.

4. Naval Technology, "Type 26 Global Combat Ship Programme, UK", https://www.naval-technology.com/projects/type-26-gcs-programme-uk/ . Used for 149.9 m, beam 20.8 m, 6,900 t, crew 157 plus 51 berths, more than 26 knots, more than 7,000 nm, 60 days, Mk 45 Mod 4, two Phalanx, Type 997 Artisan, Sonar 2087, Sonar 2150, MTU 20V 4000 M53B, MT30, two electric motors, and the hangar wording.

5. Navy Lookout, "A guide to the Type 26 Frigate", 28 November 2022, updated July 2026, https://www.navylookout.com/a-guide-to-the-type-26-frigate/ . Used for 149.9 m, beam 20.8 m, official displacement 6,900 tonnes, Artisan at about 35 m, two 24-cell Sea Ceptor modules, 24 Mk 41 cells, Mk 45 Mod 4, two Phalanx Block 1B, two 30 mm guns, core crew 157, mission-bay doors, and sensor arrangement. The "about 55 m2" flight-deck caption was rejected.

6. Navy Lookout, "Powering the stealthy submarine hunter – Type 26 frigate propulsion system in focus", 26 September 2019, https://www.navylookout.com/powering-the-stealthy-submarine-hunter-type-26-frigate-propulsion-system-in-focus/ . Used for one MT30, the 36 MW single-source limit, at least 28 knots as a single-source claim, four MTU sets at about 3 MW, two motors, two shaft lines, fixed propellers, one bracket per shaft, and uptakes.

7. Navy Lookout, "The Type 26 frigate mission bay. Part 1 – design and development", 27 February 2019, https://www.navylookout.com/the-type-26-frigate-mission-bay-part-1-design-and-development/ . Used for the about 20 m by 15 m bay, side doors, port-only boat bay, Merlin or two Wildcats, Chinook deck circa 30 m by 20 m, about 8,000 tonnes, and MBHS capacity of 15 tonnes.

8. BAE Systems, "Global Combat Ship", https://www.baesystems.com/en/product/global-combat-ship . Direct fetch was blocked. The search extract was used only where it agrees with fetched pages: 6,900 tonnes, 149.9 m, maximum beam 20.8 m, 26+ knots, range in excess of 7,000 nautical miles in electric-motor drive, Artisan, Sonar 2087, two electric motors, four diesel generators, one gas-turbine direct drive, core 157 and accommodation 208.

9. UK Defence Journal, "A Guide to the Type 26 'City class' Frigate", 1 March 2018, https://ukdefencejournal.org.uk/guide-type-26-city-class-frigate/ . Search extract used for the BAE mission-bay description (four 12 m boats or up to 11 twenty-foot containers) and for the statement that the adopted design replaced an earlier stern well deck. Not fully fetched.

10. Shephard, "Lockheed's MK 41 VLS for Type 26", 6 March 2018, https://www.shephardmedia.com/news/naval-warfare/lockheeds-mk-41-vls-type-26/ . Search extract used for three 8-cell Mk 41 modules per ship. Not fully fetched.

11. Naval Technology, "UK to acquire further five Type 2150 sonars for Type 26 frigates", 10 July 2023, https://www.naval-technology.com/news/uk-type-2150-sonars-frigates/ . Search extract used for Type 2150 on all eight ships and for replacement of Type 2050. Not fully fetched.

12. BAE Systems Australia, "Hunter class frigate", https://www.baesystems.com/en-aus/product/hunter-class-frigates . Search extract used only to keep Hunter-class 151.4 m, about 8,200 t light ship, and 27 knots off the City-class table. Not fully fetched.
