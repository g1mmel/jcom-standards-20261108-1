# dossier-judge

Judge: grok-dr (xai grok-4.7, files only) vs naval-expert (agy/Gemini, already posted to :8470) on the same 8 assets.

Read-only. Nothing in `data/`, `asset-scratch/` or the gallery was changed. No emojis [OR-048].

## Bottom line

grok-dr wins all 8, and none of them is close.

Both writers usually get the headline length, beam and weight right. Below that headline, naval-expert makes things up:
- station tables, pivot XYZ and surface travels;
- "NATOPS" or "NAVSEA drawing" labels on figures that come from Wikipedia or nowhere;
- source lists with no URLs, some of them fabricated documents.

grok-dr writes "not public" when it does not know. It prints conflicting sources side by side, and every number checked traces to a fetched URL.

**Default writer from now on: grok-dr.** All 8 naval-expert dossiers on :8470 need corrections (list below).

## Method

- Four parallel checkers, two assets each. Each checker read both dossiers and both research logs.
- At least 6 key numbers per asset per writer were checked with WebSearch/WebFetch. Sources were primary pages first (NAVAIR, navy.mil, Bundeswehr, ARTEC, KNDS, GE, Boeing, FAS, NTSP), then reputable secondary pages (Naval Technology, Navy Lookout, FlightGlobal, Wikipedia as a cross-check only).
- Front matter, URL counts and game dimensions were checked by script against `data/rules/unit-dimensions.json` and `data/plan/dossier-examples/`.
- Limits:
  - navy.mil fact files, NAVAIR Hornet/Growler pages and royalnavy.mod.uk returned 403. Mirrors (USNA, CNATRA, Boeing) and search extracts were used instead.
  - web.archive.org was blocked, so grok-dr's 2018 NAVAIR Venom figures were left unverified. grok-dr itself only reports them as a disagreement.

Scores are 1-5, where 5 is best. For Invention, 5 means nothing invented.

## Scores per asset

### fa-18e-super-hornet (base fa-18-hornet)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 5 | 5 | 5 | 5 | 5 | 25 |
| naval-expert | 3 | 3 | 2 | 1 | 3 | 12 |

Winner: grok-dr. naval-expert's numbers are right at the top level. Its "NATOPS Fig 1-2" dimensions are Wikipedia's, and its internal fuel is wrong.

### ea-18g-growler (base fa-18-hornet)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 5 | 5 | 5 | 5 | 5 | 25 |
| naval-expert | 2 | 3 | 2 | 1 | 3 | 11 |

Winner: grok-dr. naval-expert uses the E/F length of 60.3 ft for the Growler. It also invents a pod-span explanation for 13.68 m and gets the station breakdown wrong.

### coalition-frigate-type26 (base nato-type26-frigate)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 5 | 5 | 5 | 5 | 5 | 25 |
| naval-expert | 2 | 2 | 1 | 1 | 3 | 9 |

Winner: grok-dr. naval-expert:
- gives controllable-pitch propellers where the ship has fixed-pitch;
- gives a 150 t mission-bay payload where the real rating is 15 t;
- carries over unsupported HMS Glasgow base numbers;
- gets the Hunter and River export numbers wrong;
- invents a "Coalition" fit.

### fgs-braunschweig-k130 (base saar-6-corvette)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 4 | 5 | 5 | 5 | 5 | 24 |
| naval-expert | 3 | 3 | 1 | 1 | 3 | 11 |

Winner: grok-dr. Its one slip is a "two Skeldar" line taken from a search extract, which it labels as unfetched. naval-expert drops the Sa'ar weapons correctly, but:
- it uses the Sa'ar 6 height (21.5 m) as the K130 air draft;
- it invents waterline exhausts and a 2x Camcopter hangar fit.

### usns-supply-taoe6 (no base)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 5 | 5 | 5 | 5 | 5 | 25 |
| naval-expert | 2 | 2 | 1 | 1 | 3 | 9 |

Winner: grok-dr. naval-expert shows Phalanx, Nixie, SRBOC, SLQ-32 and SPS-49 as the current USNS fit. Its 42 m "NAVSEA drawing" height is the game's own representative value, back-solved.

### uh-1y-venom (no base)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 5 | 5 | 5 | 5 | 5 | 25 |
| naval-expert | 2 | 2 | 1 | 1 | 3 | 9 |

Winner: grok-dr. naval-expert says the AH-1Z rotor is "identical" to the UH-1Y's: it is 14.6 m vs 14.88 m. It also invents a g-limit, a cruise speed and a jammer.

### as32a-31a-tow-tractor (base deck-tow-tractor)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 5 | 5 | 5 | 5 | 5 | 25 |
| naval-expert | 2 | 3 | 1 | 1 | 3 | 10 |

Winner: grok-dr. naval-expert took the predecessor A/S32A-31 FLIS numbers (117 x 65 x 36 in, 8,500 lb drawbar) as the 31A's, then built invented specs around them.

### gtk-boxer (base boxer-ifv)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 5 | 5 | 5 | 5 | 5 | 25 |
| naval-expert | 2 | 3 | 1 | 1 | 4 | 11 |

Winner: grok-dr. naval-expert:
- swaps the driver and powerpack sides;
- uses crew 3+8 where the German vehicle carries a maximum of 10;
- names the wrong transmission;
- invents an A2 at 38.5 t with a TE21 engine;
- keeps the Lance-turret height of 3.24 m.

### Totals

| Writer | Sum (max 200) | Assets won |
| --- | ---: | ---: |
| grok-dr | 199 | 8 |
| naval-expert | 82 | 0 |

## Wrong facts, naval-expert

| Asset | Claimed | Correct | Source |
| --- | --- | --- | --- |
| fa-18e | Dims "NATOPS Fig 1-2" 18.31 / 13.62 / 4.88 m | Values are Wikipedia's. NAVAIR prints 60.3 ft / 18.5 m. | usna.edu/NavalAviation/FixedWingAircraft/FA18_Hornet.php |
| fa-18e | Internal fuel 14,950 lb / 6,780 kg | About 14,400-14,700 lb; FlightGlobal 6,560 kg | flightglobal.com/fixed-wing/1999/01/f-a-18e-f-balanced-upgrade/ |
| fa-18e | 32,081 lb called OWE "with pilot and fluids" | It is empty weight | Wikipedia F/A-18E/F |
| fa-18e | ATFLIR on Station 4 and Station 5; APG-79 called GaN and GaAs | Station 5; GaAs | Boeing, Wikipedia |
| ea-18g | Length 60.3 ft | 60.2 ft | boeing.com/defense/fighters-and-bombers/fa-18-super-hornet-and-ea-18-growler; CNATRA |
| ea-18g | 13.68 m span "measured over ALQ-218 pods" | 44.9 ft / 13.68 m is the same printed span as the E with rails. Secondary sources give 13.62 m with pods. | usna.edu/NavalAviation/FixedWingAircraft/EA18G_Growler.php |
| ea-18g | 9 stations = 2 wingtip + 6 underwing + 1 centreline | 6 underwing + 3 fuselage. The wingtips are pods, not stations. | USNA, Wikipedia |
| ea-18g | 66,000 lb = 29,964 kg | 29,937 kg | arithmetic |
| ea-18g | 48,000 lb "max arrestment" | Recovery weight | CNATRA / USNA |
| type26 | 5-blade controllable-pitch propellers | Fixed-pitch | navylookout.com/powering-the-stealthy-submarine-hunter-type-26-frigate-propulsion-system-in-focus/ |
| type26 | 150 t mission-bay payload | 15 t handling system | Navy Lookout mission-bay article |
| type26 | 35 m = TACAN masthead air draft | Artisan radar is about 35 m above the waterline. No masthead height is published. | navylookout.com/a-guide-to-the-type-26-frigate/ |
| type26 | 6,900 t lightship / 8,000 t full load | 6,900 t is unlabelled. The 8,000 t is an RN news sentence that does not say "full load". | Naval Technology, Navy Lookout |
| type26 | Hunter LOA 149.9 m | 151.4 m | navy.gov.au/capabilities/ships-boats-and-submarines/hunter-class-frigate |
| type26 | River about 9,400 t | 7,800 t | canada.ca River-class destroyer page |
| k130 | LBP 82.80 m | 82.8 m is waterline length | naval-technology.com/projects/k130corvette/ |
| k130 | Beam 13.28 m "molded at DWL" | Waterline breadth 12.44 m; 13.28 m is max beam | Naval Technology |
| k130 | Crew 58 core | 61 core (Bundeswehr); 65 complement | bundeswehr.de/de/ausruestung-technik-bundeswehr/seesysteme-bundeswehr/korvette-k130 |
| k130 | Range 2,500 nm @ 15 kn / 4,000 nm @ 12 kn | 4,000 nm @ 15 kn; more than 2,500 nm with no speed given | Wikipedia; Naval Technology |
| k130 | 2 mine rails, 34 mines | 4 rails (Bundeswehr), or 2 racks x 34 | Bundeswehr |
| k130 | Air draft 21.5 m | That is the Sa'ar 6 height. No K130 height is published. | naval-technology.com/projects/saar-6-class-corvettes/ |
| k130 | Sa'ar column: 32 Barak, 91.4 m | 40 Barak 8, about 90 m | Naval Technology Sa'ar 6 |
| supply | Controllable-pitch 21 ft propellers | Fixed-pitch, 23 ft | man.fas.org/dod-101/sys/ship/aoe-6.htm |
| supply | Cargo 156,000 bbl, 1,800 / 400 / 250 st, "per fact file" | Fact file: 177,000 bbl, 2,150 t ammo, 500 t dry, 250 t refrigerated | navy.mil fact file Article/2174658 |
| supply | Crew: 28 Navy + about 30 air det | 160 civilians + 29 military | navy.mil fact file |
| supply | Phalanx, Nixie, SRBOC, SLQ-32 in current fit; SPS-49 | Weapons landed at the MSC transfer (13 Jul 2001). SPS-49 is not in the sensor list. | en.wikipedia.org/wiki/USNS_Supply; FAS |
| supply | 42 m keel-to-mast "NAVSEA/MSC drawings" | Game-representative value; no public source | unit-dimensions.json own note |
| supply | Mesh 35.75 x 49.38 m | Measured 35.01 x 45.51 x 230.26 m | asset-scratch/picks/jslc/measured.json |
| venom | AH-1Z main and tail rotor "identical" | AH-1Z rotor 48 ft / 14.6 m; UH-1Y 48 ft 10 in / 14.88 m | navy.mil H-1 fact file Article/2160217 |
| venom | 1,828 shp "per NAVAIR" | NAVAIR prints 1,800 shp; 1,828 is the 2.5-minute rating | navair.navy.mil/product/UH-1Y-Venom |
| venom | 160 kt max continuous cruise | 170 KIAS max, 147 KTAS cruise | bellflight.com/products/bell-uh-1y |
| venom | +3.5 g | -0.5 to +2.3 g | Bell |
| venom | AN/ALQ-144A IR jammer | AN/ALQ-231(V)3 Intrepid Tiger II is the documented pod | Wikipedia UH-1Y |
| venom | UH-1N carried 6 troops | About 13 | Wikipedia UH-1N |
| tow-tractor | Length 117 in | 115 in (117 in is the predecessor -31) | NTSP N88-NTSP-A-50-8411B, globalsecurity.org/military/library/policy/navy/ntsp/Towtractor.pdf |
| tow-tractor | 65 in hood width / 36 in deck height | These are the -31's width and height | NTSP |
| tow-tractor | Drawbar 8,500 lbf | 10,000 lb | NTSP |
| tow-tractor | 12,400 lb "unladen curb" | Gross | NTSP |
| tow-tractor | NTSP "8401B/A, Sept 1998" | 8411B, June 1998 | NTSP |
| tow-tractor | "4 wheels (6 tires)" | Front steer, dual rear wheels | NTSP |
| tow-tractor | Dolly: 30 in, 11,500 lb, 14,000 lbf | 29 in, 11,200 lb, 10,000 lb | NTSP |
| gtk-boxer | Driver front left, powerpack starboard | Driver front right, powerpack front left | bundeswehr.de/de/ausruestung-technik-bundeswehr/landsysteme-bundeswehr/gtk-boxer |
| gtk-boxer | Crew 3+8 | Maximum 10 (3+7) | Bundeswehr; knds.com/en/products/systems/boxer/boxer-gtv |
| gtk-boxer | Allison HD4070 | Allison HD4800SP + RRW3001 | Bundeswehr |
| gtk-boxer | A2 38.5 t, TE21 600 kW | A2 changes exhaust, cooling air and driver vision only; TE20, 530 kW | Bundeswehr |
| gtk-boxer | Weapon-station top 3.24 m (base Lance figure) | 3.4 m overall | Bundeswehr |
| gtk-boxer | 7.93 m as overall length | 7.93 m is the hull; 8.3 m overall | Bundeswehr; artec-boxer.com |
| gtk-boxer | Turning about 15 m with brakes; 3 twin roof hatches | About 16 m; 4 pairs | Bundeswehr |

## Wrong facts, grok-dr

| Asset | Claimed | Correct | Source |
| --- | --- | --- | --- |
| k130 | Hangar for "two Skeldar" (labelled a search extract) | Skeldar order cancelled. UAVs not fitted; Camcopter only trialled. | Wikipedia K130; Naval Technology |

Over-caution, not errors:
- Growler MTOW and station count are given as "not public on fetched pages". USNA and CNATRA print 66,000 lb and 9 stations.
- E/F folded span is given as not public. Secondary sources print 9.32 m.

## Invented content

**naval-expert, all 8 assets:**
- full station / offset / loft tables and pivot XYZ for every node;
- surface travels and slew rates;
- citations with no URL (generic document titles).

Asset-specific inventions:
- fa-18e / ea-18g: FS/BL/WL datum and loft table; LEX spoiler 60 deg at 60 deg/s; APG-79 tilted 20 deg; "AIM-9X dummy" explanation for 9.94 m; "41%" radius gain; NATOPS "01-EA18G-1"; "00-80T-120 Table 4-1" folded span 9.98 m; weight deltas +134 / +459 kg; 12,000 lb bring-back; RAT RPM and 27 kVA; ALQ-218 antennas on the fin crowns.
- type26: draft 5.4 / 7.5 m; LBP 140 m; waterline beam 19.5 m; 0.700 m frames; hangar door 8.5 x 5.8 m; flight deck 26 m; SCOT-5 positions; the "Coalition Integrated Combat System" fit with 2x MH-60R and CAMM-ER; "Lionfish" for the River 30 mm; River lengthened "for SPY-7 trim".
- k130: waterline side exhausts with seawater injection; 2x Camcopter S-100 embarked; "Aeronavali Harpoon grid"; 0.650 m frames; depth 7.40 m; TRS-3D at 10-30 rpm; Sa'ar "lengthened 0.88 m for 10 t helicopters". Fabricated-looking sources: TKMS GA drawings, GNYK production data.
- supply: LBP 709 ft; depth 21.4 m; extreme beam 35.75 m; kingpost heights and UNREP coordinates; ram-tensioner strokes; 168 rpm shafts; 5 x 2,500 kW generators; 1,500 kW bow thruster; 900,000 gal/h. Fabricated-looking sources: DTIC "AD-A285517" AOE-6 trials, CRS "RS21183", "MSC Public Operations Manual", NASSCO body-plan data.
- venom: tail rotor 2.97 m; fuselage 14.17 m; folded 13.97 x 2.84 m; blade-station chord/twist table; 246 / 1,660 rpm; FS 138/159/485. Fabricated-looking sources: fact file "2166683" (the real ID is 2160217), "H1Y-PG-01", NATOPS "01-H1Y-1".
- tow-tractor: Detroit 3-53 at 101 hp; Allison 4-speed; 12-13 mph; 91 in wheelbase; 54 in track; tyre sizes and pressures; 85 gal fuel; 16,000-28,000 lbf breakaway; "11,200 lbf for aircraft to 74,500 lb" (this is the dolly's gross weight, relabelled); ALBAR lengths; air-start configuration lengths and weights; "A/S32A-49 STT on a Schopf F59, 21,600 lb".
- gtk-boxer: glacis 15 / 45 deg; tyre-pressure modes; LAZ 400 performance; egress under 4.5 s; ramp stroke 0.85 m; 8 hardpoints; module Z values. Fabricated-looking sources: "BAAINBw Referat K1.2 2020", "ARTEC brochure 2022".

**grok-dr:** none found. Single-source figures are marked single-source, and coordinates are marked "not public".

## Variant discipline summary

- Hornet base (legacy Hornet with F-35 features):
  - Both writers dropped the internal bays, EOTS, DAS and dorsal airbrake.
  - naval-expert kept the base's surface travels and rates.
  - grok-dr flagged them as not public.
- Sa'ar 6 to K130: both dropped the Israeli weapons. naval-expert imported the Sa'ar 21.5 m height.
- Glasgow to Type 26: naval-expert kept the base's LBP, waterline beam, keel and "full load 8,000 t" figures, which are not public or not supported.
- A/S32A-32 dolly to 31A:
  - Neither writer gave the 31A the dolly's clamp or zero turning radius.
  - naval-expert mixed in the predecessor -31's numbers.
- Boxer Lance to GTK: both dropped Lance, Spike and the tracks. naval-expert kept the 3.24 m turret height, the 15 deg glacis and the 415/80 R685 tyre.

## Format

Both writers have all nine required fields: asset_id, title, generated_at, skills, provider, models, query, sources_count, generator. In all 16 files, sources_count matches the number of entries in the source list.

**grok-dr:** matches the house examples exactly (quoted strings, YAML lists, house skills). Every source has a URL.

**naval-expert:**
- `skills: ["naval-expert"]` instead of the house skills.
- `models` carries a bare "pro".
- In the 7 batch-1 files, `title:` is unquoted and contains ": ". Strict YAML rejects that ("mapping values are not allowed"). The :8470 API accepted it, so its parser is lenient. gtk-boxer (batch 3) is quoted and fine.
- Six of the eight have no URLs at all. The fa-18e and ea-18g have some links, several of them homepage-only.

## Game dimensions (`data/rules/unit-dimensions.json`)

| Asset | Game row | Finding |
| --- | --- | --- |
| fa-18e | 18.5 x 13.68 x 4.87 | Matches NAVAIR's metre labels. 60.3 ft is 18.38 m, so the metres and feet do not convert exactly. Within band. naval-expert's "rounded 60.3 ft" explanation is wrong. |
| ea-18g | 18.5 x 13.68 x 4.87 | The Growler card says 60.2 ft (18.35 m). The row is 0.15 m long but in band. "Outer mould line" is not on the cited NAVAIR page. naval-expert's "exact pod span" claim is wrong. |
| type26 | none | 149.9 x 20.8 is supported. Do NOT take naval-expert's proposed height of 41.5 m: it is unsupported, and the radar alone sits at about 35 m above the waterline. Mark any height representative. |
| k130 | none (Sa'ar 6 rows 90 x 13 x 28) | 89.1 x 13.3 is supported. Do NOT take naval-expert's 21.5 m height (a Sa'ar 6 figure). Do not apply the Sa'ar row to F260. |
| supply | 229.8 x 32.6 x 42 | Fact file prints 229.9 m; 229.8 m is a 754 ft conversion. 42 m is representative, and nothing public backs it. Roster `locomotion.type: "tracked"` on the ship is a real bug (naval-expert found it correctly). |
| venom | 17.78 x 14.88 x 4.5 | Exact NAVAIR match. The width is the UH-1Y rotor itself, so the "H-1 representative" note undersells it. `jslc:shared:uh-1y-venom` and `jslc:shared:Venom` are still 6 x 2.4 x 2.2 placeholders. |
| tow-tractor | deck-tow-tractor 6 x 2.4 x 2.2 (UNVERIFIED) | Wrong by 2x. The NTSP 31A is 2.92 x 1.78 x 1.02 m. naval-expert's 2.97 m and 4.12 m proposals are the predecessor's figure and an invented one. |
| gtk-boxer | none | Use 8.3 x 3.0 x 3.4 m overall (Bundeswehr), or 7.93 x 2.99 x 2.38 m labelled as hull. naval-expert's 7.93 x 2.99 x 2.37 m drops the weapon station. The base mesh's 3.34 m width is too wide. |

These are proposals for the MODELS lane. Nothing was written back.

## Verdict

1. **Default writer: grok-dr.** It is slower but correct, and every number traces to a URL. Its "not public" discipline is what the browser needs.
2. If naval-expert stays in use for volume, gate it with three rules:
   - no number without a URL;
   - no coordinate or station table unless it is marked "modelled, not sourced";
   - a grok-dr or human spot-check of 6 numbers per dossier before POST.
3. Posted naval-expert dossiers that need correcting (all 8):

| asset_id | dossier_id | Fixes |
| --- | --- | --- |
| fa-18e-super-hornet | 792 | Re-attribute 18.31 / 13.62 / 4.88 m to secondary sources. 32,081 lb is empty weight. Fuel about 14,400-14,700 lb. ATFLIR Station 5; APG-79 GaAs. Strip coordinates, lofts and rates, the AIM-9X explanation and the 41% claim. |
| ea-18g-growler | 794 | Length 60.2 ft. Span reasoning: shared 44.9 ft; 13.62 m with pods. Stations 6+3 plus wingtip pods. 29,937 kg. 48,000 lb is recovery weight. Drop NATOPS/Table 4-1 citations, 9.98 m, 12,000 lb, the deltas and the RAT figures. Cite fact file Article/2166036. |
| coalition-frigate-type26 | 796 | Fixed propellers. 15 t bay. 35 m is the Artisan height, not air draft. Draft, LBP and waterline beam not public. Drop the full-load and lightship labels. Sea Ceptor: 12 vs 2x24 cells, 48 missiles. Hunter 151.4 m; River 7,800 t. Remove the Coalition fit and the station table. |
| fgs-braunschweig-k130 | 785 | Remove the 21.5 / 24.9 m heights. Waterline length 82.8 m; waterline beam 12.44 m. Crew 61/65. Range 4,000 nm @ 15 kn. Mines 4 rails. Hangar for two drones (none embarked). Delete the exhausts. Fix the Sa'ar column. |
| usns-supply-taoe6 | 807 | 42 m is representative. Fixed-pitch 23 ft propellers. Fact-file cargo. Crew 160+29. 25 kt. Remove Phalanx, Nixie, SRBOC, SLQ-32 and SPS-49 from the current fit. Delete the offsets, UNREP coordinates and machinery figures. Mesh 35.01 x 45.51 x 230.26. |
| uh-1y-venom | 800 | Remove "identical AH-1Z rotor". 1,800 shp. 170 KIAS / 147 KTAS. 8 Marines. -0.5 to +2.3 g. ALQ-231 not ALQ-144A. Remove tail rotor diameter, fuselage length, folded dimensions, blade table and RPMs. Check which side the tail rotor is on. |
| as32a-31a-tow-tractor | 786 | Length 115 in. Drawbar 10,000 lb. 12,400 lb is gross. 65 / 36 in are the -31's. NTSP 8411B June 1998. Front steer with dual rears. Dolly column 29 in / 11,200 lb / 10,000 lb. Strip engine, transmission, speed, tyre, fuel and STT/Schopf inventions. |
| gtk-boxer | 646 | Driver front right, powerpack front left. Crew max 10. HD4800SP + RRW3001. No A2 38.5 t / TE21. Height 3.4 m, length 8.3 m (7.93 m hull), roof 2.38 m. Turning about 16 m. 4 hatch pairs. Strip glacis, tyre and sensor inventions. |

All 8 also need real URLs in place of their source lists, and quoted `title:` values (batch 1).

The same fabrication pattern probably runs through the rest of the naval-expert batches (about 160 dossiers). A sampled audit of batches 1-6 is recommended before anyone trusts them.

## Time per dossier (from lane reports and `lanes/registry/STATUS.md`)

| Writer | Lane wall clock | Dossiers | Wall per dossier | Worker time per dossier |
| --- | --- | ---: | --- | --- |
| grok-dr | 15:06-15:35, 28.8 min | 8 | about 3.6 min | 13-18 min per parallel pair, so about 7-9 min each; 12-17 searches and 6-11 fetches each |
| naval-expert writer-1 | 15:13-15:39, 26.1 min | 27 | about 58 s | not reported; no search counts |
| naval-expert writer-3 (gtk-boxer) | 15:13-15:33, 19.8 min | 31 | about 38 s | not reported |

naval-expert is about 4-6x faster per dossier on wall clock. The extra time grok-dr spends goes into the fetches that make its numbers true.
