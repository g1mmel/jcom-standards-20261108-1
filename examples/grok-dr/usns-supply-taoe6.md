---
generated_at: "2026-10-14T15:29:37-04:00"
generator: "dolphin2/dossier-grok-dr"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "xai"
models:
  - "grok-4.7"
query: "USNS Supply (T-AOE-6) Supply-class fast combat support ship public dimensions, draft, UNREP, and aviation"
sources_count: 10
asset_id: "usns-supply-taoe6"
title: "Naval Architectural Blueprint Dossier: USNS Supply (T-AOE-6)"
---

# Naval Architectural Blueprint Dossier: USNS Supply (T-AOE-6)

**Classification:** Unclassified public-source compilation. US Navy / Military Sealift Command. Supply-class fast combat support ship. Real hull T-AOE-6. The roster name USNS Manna (T-AOE-26) is a game rename and is not used as the ship identity.
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

### 1. MASTER COORDINATE DATUM & DIMENSIONS

glTF: forward/bow/nose = -Z, up = +Y, starboard = +X, port = -X.
Ship: design waterline Y = 0. No public source in this set gives the vertical distance from that waterline to the keel, the mast, or the flight deck as a single factory air-draft figure. Draft values below disagree and are different definitions. They are not averaged and are not a mast height.

| Parameter | Metric | Imperial | Engineering notes |
| --- | --- | --- | --- |
| Length overall | 229.9 m [1]; 229.8 m [6]; 230.0 m [7]; 230 m [5]. [8] does not print metres. | 754 ft [1][2][6]; 754.6 ft [7]; 754,6 ft [5]; 753 ft 8.5 in [8] | Disagreement. Do not average. [1] prints 754 feet (229.9 meters). [6] prints 754 ft (229.8 m) overall for the same foot length. [5] and [7] print 754.6 ft. [8], a 1997 Carderock paper read here from a Scribd text extract, prints length overall 753 feet 8.5 inches. [10] prints 229.9 m and is a secondary page. Game 229.8 m matches the [6] conversion, not the [1] printed metre. |
| Waterline length | not public | 730 ft waterline [2] | single-source [2]. No second source. Metric not printed on that page. |
| Beam | 32.6 m [1][5][6][10]. [7] prints 33 m as the parenthetical of 107 ft. | 107 ft [1][2][5][6][7][8] | Dual-source agreement on 107 ft. [2] marks it extreme/waterline. [6] marks it extreme. The 33 m on [7] is a coarser conversion of 107 ft, not a separate beam measurement. [10] is secondary and repeats 32.6 m. |
| Draft | 11.9 m [5][6]; 12 m [10]. [1] prints no draft. [8] prints no metres. | 38 ft maximum navigation [2]; 39 ft [5][6]; 37 ft 10 in mean draft at full load [8] | Disagreement. Do not average. [2] is single-source for "38 ft max nav." [5] and [6] both print 39 ft (11.9 m); they may share a data sheet and are not treated as two surveys. [8] is single-source for mean full-load draft 37 ft 10 in, tied on that page to displacement 48,500 long tons. [10] is single-source for the round figure "draught 12 m." |
| Keel-to-mast, air draft, flight-deck height | not public | not public. [7] prints "Height 39 ft (12 m)." | No fetched source gives a keel-to-mast height or a flight-deck height. The [7] "height" is the same magnitude as the draft figures and is not used as air draft. Game height 42 m is a game representative, not a factory figure. |
| Full-load displacement | [1] prints 49,583.15 metric tons beside 48,800 tons. [6] infobox prints 49,600 t beside 48,800 long tons. [6] body prints 49,000 tons full. [10] prints 48,800 t. | 48,800 tons full load [1][3]; approx. 48,800 tons [5]; 48,800 long tons [6] infobox; 49,000 tons full [6] body; 48,603 full [2]; 48,500 long tons [8] | Disagreement. Do not average. [3] and the [6] body empty/full pair are one FAS-family text if [6] is following FAS, not two weighings. [10] is a secondary repeat of 48,800 t. [2] prints "48,603 full" without a long-ton versus short-ton word in the notes used here. |
| Light or empty displacement | not public as a metric tonne figure | 19,700 tons [3], and [6] body prints 19,700 tons empty; 20,840 light [2] | Disagreement. Do not average. The 19,700 figure is FAS-family; [6] is not counted as an independent weighing. [2] is single-source for 20,840 light. |
| Installed power | [6] infobox prints 78 MW beside 105,000 hp. [6] body prints 78.33 MW. | 105,000 hp [1][6][10]; 100,000 HP [2][8]; 100,000 shp [3] | Disagreement. Do not average. [10] is secondary. Four GE LM2500 gas turbines and two shafts are stated by [1][2][3][8]. |
| Speed | not public as a metric rate | 25 knots [1][2][3][6][10]; 26 knots [5][7]; cruise 22 kt [10] | Disagreement on maximum speed. Do not average. Cruise 22 kt is single-source [10]. |
| Range | [10] prints 6,000 miles. [6] body prints 6,000 nm. | same figures; the units are not the same word | Not treated as agreement. [10] is single-source for "6,000 miles." The [6] body figure is tied there to a factsheet this dossier did not re-fetch. No range is dual-confirmed. |
| Propeller diameter | not public | 23-foot fixed-pitch [3], repeated as 23 ft by [10] | FAS-family figure repeated by a secondary page. Not two independent measurements. [8] says fixed-pitch propellers and does not print the diameter. |
| Crew | not a dimension | See notes | Disagreement. [1]: 160 civilians and 29 military. [5] and [7]: 176 civilians and 59 military. [10]: 219, written there as 160 civilians plus 59 military. [6] body: 40 officers plus 667 enlisted (USN), and 176 civilians with 30-45 military (MSC). [3]: 40 officers, 36 CPO, 591 enlisted (USN-era). [2]: accommodations 51 officers and 125 enlisted. Do not average. |
| Aircraft associated with the hull | not a dimension | See notes | Disagreement. [1] and [6] infobox: two CH-46E or MH-60S normally embarked. [5]: two MH-60S. [3]: three CH-46E. [10]: three CH-46E (that page's "UH-46E" wording is its own). Do not average. |

Station offsets are not public. No station-offset table is printed.

### 2. ARRANGEMENT

USNS Supply (T-AOE-6) was built by National Steel and Shipbuilding Company, San Diego [1][2][5][8]. Ordered or awarded 22 January 1987 [2][5]. Keel 24 February 1989 [2][5]. Launched 6 October 1990 [2][5]. [8] records propulsion trials on 2 February 1993 and delivery to the Navy on 29 October 1993. Commissioned 26 February 1994 [2][5][7]. Decommissioned and transferred to Military Sealift Command on 13 July 2001 [1][5][7]. [1] also records sister transfers: Arctic in June 2002, Rainier in August 2003, Bridge in June 2004. [1] lists USNS Supply (T-AOE 6) with no homeport. [5] prints homeport Earle, N.J. Those homeport statements disagree. [6] describes Supply and Arctic as the active pair and Rainier and Bridge as stricken; that later status is [6] only in this dossier.

The hull is a fast combat support ship built to combatant standards [3][9]. [9] is a search-indexed GAO account, not a full PDF read in this session: January 1987 award to NASSCO of an $862.9-million fixed-price incentive contract for detailed design and construction of the lead AOE 6, with options for three more; the program was reduced from seven ships to four; the AOE 9 option was not exercised; the class was the first Navy design to use the new reversing reduction gears.

Propulsion is four GE LM2500 gas turbines on two shafts [1][2][3][8]. [8] names two Cincinnati Gear main reduction gears and two SSS-TOSI reversible coupling converters per shaft, driving fixed-pitch propellers, for reverse and slow-speed maneuvering. [3] describes the same kind of plant as a reversing reduction gear with an SSS clutch and a Franco-Tosi RCC, and calls the propellers 23-foot fixed-pitch. Power and speed disagreements are in the table above. [2] is single-source for two low funnels aft, in contrast to the single taller funnel of the earlier Sacramento class. Funnel coordinates are not public.

Replenishment is the ship's function. Sources do not agree on a single station count, and none of them give frame offsets.

- [3]: six stream stations, three port and three starboard; one receive-only sliding padeye; four 10-ton cargo booms; three double-probe stream fueling stations; two single-probe stream fueling stations. This is an older USN-era technical description.
- [10], a secondary page that overlaps [3]: five fueling-at-sea stations, six replenishment-at-sea stations, four 10 t cargo booms, and a VERTREP position described for two helicopters.
- [4], OPNAVINST 3501.243C of 11 March 2026, is a current requirements text and is internally inconsistent. It says the ship provides ammunition, provisions, stores, fleet freight, mail, personnel, and fuel (F-76 or JP-5) "from a combination of nine UNREP stations simultaneously: five fueling at sea (FAS) stations (two starboard and three port) and six replenishment at sea (RAS) stations (three starboard and three port) or seven RAS and FAS stations and one Vertical Replenishment (VERTREP) station." Five plus six is not nine. The same instruction says maximum ammunition and cargo stations in operation are two on one side and one on the opposite side, and that fuel uses two of three port fuel stations (double probe) and two of two starboard fuel stations (single probe). A Condition R passage in the same extract says F-76 and F-44 from five FAS stations (three port and two starboard) and provisions from two RAS stations (one port and one starboard), with a maximum of five CONREP stations in operation for cargo and fuel. UNREP is normally not to exceed 32 hours per week. VERTREP uses helicopters from another unit and is simultaneous with UNREP only when seven or fewer stations are manned. Rigs are not to be sent to two ships at once until transfer to the first ship has started. The instruction requires a helicopter direction center. This dossier does not reconcile those sentences into one count.

Cargo capacity is also published in incompatible sets. Do not average.

- [1]: more than 177,000 barrels of oil; 2,150 tons of ammunition; 500 tons of dry stores; 250 tons of refrigerated stores.
- [3]: DFM 1,965,600 gal; JP-5 2,620,800 gal; DFM/JP-5 convertible 1,965,600 gal; lube oil 500 55-gal drums; bottled gas 800 gallons; ordnance 1,800 long tons; chill/freeze 400 long tons; water 20,000 gal emergency.
- [6] body: ordnance 2,150 short tons; chill/freeze 250 short tons; gallon figures that match the [3] DFM and JP-5 lines. The short-ton figures are not the [1] ton figures and not the [3] long-ton figures.
- [10]: 156,000 barrels of fuel; 500 55-gal lube barrels; 20,000 gallons cargo water; 1,800 t ammunition; 400 t refrigerated; 250 t general cargo; 800 bottles of bottled gas. Secondary page.

[5] is single-source for a remark that refueling rigs can move up to 3,000 gallons of fuel per minute. [10] is single-source for a dedicated cargo control centre and for five service diesel generators. Neither claim was found on a second independent page.

The flight deck is aft. Hangar count, hangar-door size, and hangar-door travel are not public. A 1995 Naval Postgraduate School thesis was indexed with a sentence about three helicopter hangars and a later port-hangar VERTREP conversion. That PDF was not successfully re-read, so those sentences are not used as facts.

Weapons: [2], [5], and [7] say the USN combat system was removed when the ship transferred to MSC on 13 July 2001. [5] states armament none and specifically that Phalanx CIWS is no longer carried. [6] infobox still lists multiple .50-caliber machine guns and small arms. [3] and [10] describe the commissioned USN suite (NATO Sea Sparrow, two Phalanx CIWS, two 25 mm, and the decoy and Nixie fit on those pages). The USN list is not the demonstrated current MSC fit. Current small-arms carriage is the disagreement between [5] and [6], not a counted factory outfit.

[5] and [7] record a collision with USS Truxtun (DDG 103) during underway replenishment in the Caribbean. [7] dates it 11 February 2026. [5] uses 11 February 2026 in the narrative and 12 February 2026 in a table. Both ships continued. [5] says two minor injuries.

Station offsets are not public.

| Item | What the sources support |
| --- | --- |
| Builder | NASSCO, San Diego [1][2][5][8] |
| Hull identity | USNS Supply (T-AOE-6). IMO 8644199, MMSI 338947000, call sign NACO are single-source [7], which incorporates Naval Vessel Register material. |
| Propulsion | Four GE LM2500, two shafts, fixed-pitch propellers, reversing reduction gears with RCC units [1][2][3][8]. Power disagrees: 105,000 hp versus 100,000 hp. |
| Funnels | Two low funnels aft. single-source [2]. |
| UNREP | FAS, RAS, cargo booms, sliding padeye, and VERTREP are described. Counts disagree. Offsets not public. |
| Aviation | Flight deck aft. Embarked-helicopter count disagrees (two versus three; CH-46E versus MH-60S). Hangar geometry not public. |
| Present weapons | Removed at the 2001 MSC transfer [2][5][7]. [6] still prints .50-caliber guns and small arms. USN missile and CIWS fit is historical [3][10]. |

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

Motion is described only where a source describes a function. No pivot coordinates are published. Travel that is not published is marked "travel: not public."

- Hull, bow forward = -Z, starboard = +X, design waterline Y = 0.
  - Shell and replenishment deck. Station count is the disagreement in section 2. Station travel: not public. Station offsets: not public.
  - Cargo booms. [3] and [10] say four booms rated 10 tons. Boom travel: not public. Pivot XYZ: not public.
  - Receive-only sliding padeye [3]. Travel: not public.
  - Flight deck, aft. Deck height: not public. Aircraft elevator or hangar-door travel: not public.
  - Hangar. Existence of aviation support is implied by the flight deck and by [4]'s helicopter direction center. Hangar count and door travel: not public.
  - Masts and antennas. Keel-to-mast: not public. Train and elevation: not public.
  - Funnels, two, low, aft. single-source [2]. Height: not public.
- Propulsion train.
  - Four GE LM2500 gas turbines [1][2][3][8].
  - Two main reduction gears, Cincinnati Gear, each with two SSS-TOSI reversible coupling converters [8]. [3] names the clutch SSS and the converter Franco-Tosi. The gears reverse the shafts and provide slow-speed maneuvering [8]. Gear ratio and maximum shaft rpm: not public in the text extract used here.
  - Two shafts, fixed-pitch propellers [3][8]. Diameter 23 ft is FAS-family only, repeated by [10].
- Boats and kingposts. No source read for this dossier uses the word kingpost for a measured structure. A 35-foot workboat appeared only in the unconfirmed thesis index and is not used. Boat davit travel: not public.

### 4. SENSOR SITING & MISSION SYSTEMS

Coordinates of every sensor and every replenishment station are not public.

UNREP and aviation are the mission systems. [4] requires a helicopter direction center and describes FAS, RAS, and VERTREP with the inconsistent counts in section 2. VERTREP in that instruction is by helicopters from another unit. Embarked aircraft, when sources name them, are the CH-46E and MH-60S disagreement in section 1.

The USN-era combat and sensor list below is the commissioned-ship description. [2], [5], and [7] say the weapons were removed at MSC transfer. No fetched page gives the current MSC radar fit. It is not public.

[3], repeated rather than independently measured by [10], lists AN/SPS-67, AN/SPS-64(V)9, MK 23 TAS, WRN-6 GPS, and an IFF set, plus AN/SLQ-32(V)3, four decoy launchers, and AN/SLQ-25 Nixie, with the NATO Sea Sparrow, two CIWS, and two 25 mm mounts of the USN fit. [10] also names URN-25 and two fire-control radars. URN-25 is single-source [10] in this dossier. None of these items has a published station coordinate.

### 5. DIFFERENCES FROM THE BASE DOSSIER

Written from scratch. Worklist similarity is none. No base dossier was used.

No replenishment-ship dossier was used as a base. A Sa'ar 6, a Hornet, a Cobra, or a car-ferry dossier would have been the wrong hull. The game roster titles this key "USNS Manna (T-AOE-26)." That is a rename. This dossier is USNS Supply (T-AOE-6).

### 6. GAME DATA CHECK

`unit-dimensions.json` keys `jslc.vehicle.usns-supply-ship` and `coalition.vehicle.usns-supply-ship` are the same block: lengthM 229.8, widthM 32.6, heightM 42, fit length, bandMinM 206.82, bandMaxM 252.78, confidence medium, designSize false, category naval, represents "Supply-class fast combat support ship." Source string: "Supply-class T-AOE: 754 ft (229.8 m), beam 107 ft (32.6 m). Height 42 m is a representative keel-to-mast envelope."

Roster `jslc.json` id `jslc.vehicle.usns-supply-ship`, display name "USNS Manna (T-AOE-26)", legacyId `coalition.vehicle.usns-supply-ship`. Dimension block:

```
"dimensions": {
  "lengthM": 229.8,
  "widthM": 32.6,
  "heightM": 42,
  "massTonnes": null,
  "basis": "representative"
}
```

Length 229.8 m agrees with the Wikipedia class conversion of 754 ft [6] and disagrees with the Navy fact file's own printed 229.9 m for that same 754 ft [1]. It also does not match 753 ft 8.5 in [8] or 754.6 ft [5][7]. Beam 32.6 m agrees with the published 107 ft conversion used by [1], [5], and [6]. [7] rounds the same 107 ft to 33 m. Draft is absent from the game file; public drafts disagree and are not a missing game error to "correct" by averaging. Height 42 m is a game representative, not a factory sheet. No public keel-to-mast or flight-deck height was found. massTonnes null is correct to leave empty: full-load displacement is disputed and is not a single mass in tonnes. basis "representative" matches the height caveat and is stricter than treating 229.8 m as the only length.

### 7. MASTER AI VIDEO PROMPT PACKAGE

1. Gray fast combat support ship underway, bow toward the camera's forward axis, long replenishment deck, flight deck aft, two low funnels aft, no missile launcher and no Phalanx mount, because the MSC transfer removed the commissioned combat system. Do not label a mast height.

2. Port-side underway replenishment. Fuel probes and cargo lines are rigged. Station count is left unnumbered because public sources disagree. No frame numbers on the hull.

3. Flight deck aft with one helicopter on deck. Do not set the embarked detachment at two or at three. Hangar door travel is not shown as a measured stroke.

4. Engine-room impression of four marine gas turbines geared to two shafts with fixed-pitch propellers and reversing couplings. No shaft-rpm callout and no propeller-diameter callout.

### 8. SOURCES

1. Fast Combat Support Ships T-AOE. U.S. Navy fact file, last updated 29 September 2021. https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2174658/fast-combat-support-ships-t-aoe/ . Length 754 ft (229.9 m), beam 107 ft (32.6 m), full-load displacement, 105,000 hp, 25 knots, crew 160 civilians and 29 military, two aircraft normally embarked, cargo narrative, NASSCO, MSC transfer dates, no homeport. No draft and no mast height.

2. AOE-6 class page, compiled 24 October 2021. Stephen S. Roberts, shipscribe. https://www.shipscribe.com/usnaux2/AOE/AOE06.html . 754 ft overall, 730 ft waterline, 107 ft beam, 38 ft maximum navigation draft, 20,840 light, 48,603 full, 100,000 HP, dates, two low funnels, weapons landed at MSC transfer, accommodations.

3. AOE 6 Supply. Federation of American Scientists, Military Analysis Network. https://man.fas.org/dod-101/sys/ship/aoe-6.htm . USN-era plant, 23-foot propellers, cargo gallons and tons, six stream stations, booms, padeye, probes, sensors, weapons, 19,700 tons and 48,800 tons full load, three CH-46E, USN crew. A GlobalSecurity mirror of this text is the same family, not a second source.

4. OPNAVINST 3501.243C, 11 March 2026. Department of the Navy. https://www.secnav.navy.mil/doni/Directives/03000%20Naval%20Operations%20and%20Readiness/03-500%20Training%20and%20Readiness%20Services/3501.243C.pdf . Current UNREP requirement text, including its internal station-count inconsistency, helicopter direction center, and weekly UNREP limit. No hull dimensions.

5. USNS Supply (T-AOE 6). navysite.de. https://www.navysite.de/ships/aoe6.htm . Dates, 754,6 ft, beam 107 ft, draft 39 ft (11.9 m), about 48,800 tons, 26 knots, two MH-60S, crew 176 civilians and 59 military, weapons removed, Earle homeport, 3,000 gal/min remark, Truxtun collision.

6. Supply-class fast combat support ship. Wikimedia Foundation. https://en.wikipedia.org/wiki/Supply-class_fast_combat_support_ship . Infobox 754 ft (229.8 m), beam 107 ft (32.6 m), draft 39 ft (11.9 m), 48,800 long tons, 25 knots, 105,000 hp, two helicopters. Body disagrees with that infobox on empty and full displacement, complement, and some cargo tons. Not independent of [3] where it follows FAS.

7. USNS Supply. Wikimedia Foundation, incorporating Naval Vessel Register material. https://en.wikipedia.org/wiki/USNS_Supply . 754.6 ft (230.0 m), beam 107 ft (33 m), the "height" 39 ft (12 m) that is not used as air draft, 26 knots, crew 176/59, IMO/MMSI/call sign, weapons removed, collision date 11 February 2026.

8. B. Michael Zekas and Andrew N. Schultz, "Unique Reverse and Maneuvering Features of the AOE-6 Reverse Reduction Gear," ASME GT1997. Carderock Division, Naval Surface Warfare Center, Philadelphia. Read from a Scribd text extract of the paper, not from a full ASME PDF download. Length overall 753 feet 8.5 inches, beam 107 feet, mean full-load draft 37 feet 10 inches, displacement 48,500 long tons, 100,000 HP, four LM2500s, Cincinnati Gear, two SSS-TOSI RCCs per shaft, fixed-pitch propellers, trials 2 February 1993, delivery 29 October 1993.

9. Navy Ships: Lessons of Prior Acquisition Problems Can Improve AOE 6 and Other Programs, GAO/NSIAD-93-298, 30 September 1993. U.S. Government Accountability Office. Product page https://www.gao.gov/products/nsiad-93-298 . Search-indexed. The PDF was not opened in full. Used for the $862.9-million lead-ship contract, the seven-to-four program cut, combatant standards, and the reversing-gear first.

10. Supply Class Fast Combat Support Ships. Naval Technology. https://www.naval-technology.com/projects/aoe6/ . Secondary compilation. Used for 229.9 m, 32.6 m, the single-source 12 m draught, 48,800 t, 105,000 hp, 25 knots, cruise 22 kt, 6,000 miles, crew line 219, five FAS and six RAS, four 10 t booms, and the repeat of the FAS propeller and combat-system list. Not treated as an independent measurement of figures it shares with [3].
