# Research log: USNS Supply (T-AOE-6)

- asset_id: usns-supply-taoe6
- start_local: 2026-10-14T15:14:49-04:00
- end_local: 2026-10-14T15:29:37-04:00
- search_count: 13
- fetch_count_successful: 8 full or targeted page reads, plus 1 search-result text extract of the ASME paper
- dossier: C:\cnc_rev\asset-scratch\dossiers\grok-dr\usns-supply-taoe6.md
- game files read: C:\cnc_rev\data\rules\unit-dimensions.json keys jslc.vehicle.usns-supply-ship and coalition.vehicle.usns-supply-ship; C:\cnc_rev\data\roster\jslc.json id jslc.vehicle.usns-supply-ship at line 8862

## Queries

1. USNS Supply T-AOE-6 specifications length beam draft displacement
2. Supply-class fast combat support ship dimensions NASSCO
3. site:navy.mil USNS Supply T-AOE-6 fact file length beam
4. site:msc.usff.navy.mil Supply T-AOE-6 fast combat support ship
5. "T-AOE-6" "Naval Vessel Register" length beam draft
6. USNS Supply T-AOE-6 hangar flight deck helicopter UNREP stations kingpost
7. USNS Supply AOE-6 air draft mast height "feet" OR metres keel
8. NASSCO "AOE 6" OR "AOE-6" Supply launch keel San Diego
9. site:nvr.navy.mil T-AOE 6 Supply characteristics
10. Supply class AOE-6 FAS RAS stations "10-ton" OR "cargo boom" OR hangar
11. "AOE-6" OR "AOE 6" OR "T-AOE-6" hangar "flight deck" helicopter Supply class
12. GAO NSIAD-93-298 AOE 6 NASSCO reversing reduction gear
13. "AOE-6" "753 feet" OR "37 feet 10" Zekas Schultz draft

## Fetches

1. https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2174658/fast-combat-support-ships-t-aoe/ — U.S. Navy fact file, Fast Combat Support Ships T-AOE. Full article read. Gave 754 ft (229.9 m), beam 107 ft (32.6 m), 48,800 tons (49,583.15 metric tons) full load, 25 knots, four GE LM2500, two shafts, 105,000 hp, crew 160 civilians and 29 military, two CH-46E or MH-60S normally embarked, cargo narrative, NASSCO, MSC transfer dates, no homeport. No draft. No mast height.
2. https://www.shipscribe.com/usnaux2/AOE/AOE06.html — Stephen S. Roberts, shipscribe, compiled 24 October 2021. Full page. Gave 754 ft overall, 730 ft waterline, 107 ft, 38 ft max nav, 20,840 light, 48,603 full, 100,000 HP, dates, two low funnels, weapons landed at MSC transfer.
3. https://man.fas.org/dod-101/sys/ship/aoe-6.htm — FAS Military Analysis Network, AOE 6. Full page. Gave USN-era sensors, weapons, cargo gallons, UNREP station list, 23-foot propellers, 19,700 / 48,800 tons, three CH-46E, 100,000 shp. GlobalSecurity mirror is the same text family.
4. https://www.secnav.navy.mil/doni/Directives/03000%20Naval%20Operations%20and%20Readiness/03-500%20Training%20and%20Readiness%20Services/3501.243C.pdf — OPNAVINST 3501.243C, 11 March 2026. Targeted read. Gave the UNREP requirement, including the nine-versus-five-plus-six wording, probe arrangement, VERTREP condition, 32 hours per week, and the helicopter direction center. No length, beam, draft, or hangar size.
5. https://www.navysite.de/ships/aoe6.htm — navysite.de, USNS Supply. Full page. Gave dates, 754,6 ft (230 m), beam 107 ft (32.6 m), draft 39 ft (11.9 m), about 48,800 tons, 26 knots, two MH-60S, crew 176/59, armament none, Earle homeport, 3,000 gal/min remark, Truxtun collision with both 11 February 2026 and a table date of 12 February 2026.
6. https://en.wikipedia.org/wiki/Supply-class_fast_combat_support_ship — Wikipedia class page. Full page. Infobox and body disagree with each other. Used for 754 ft (229.8 m), beam, 39 ft draft, 25 knots, 105,000 hp, and the conflicting displacement and cargo lines. Not independent of FAS where it follows FAS.
7. https://en.wikipedia.org/wiki/USNS_Supply — Wikipedia ship page. Full page. Gave 754.6 ft (230.0 m), beam parenthetical 33 m, "Height 39 ft (12 m)" which is not used as air draft, 26 knots, IMO 8644199, MMSI 338947000, call sign NACO, weapons removed, collision date 11 February 2026.
8. https://www.naval-technology.com/projects/aoe6/ — Naval Technology, Supply Class. Full page. Secondary. Gave 229.9 m, 32.6 m, draught 12 m, 48,800 t, 105,000 hp, 25 knots, cruise 22 kt, 6,000 miles, crew 219, five FAS, six RAS, four 10 t booms, and a repeat of the FAS combat-system and 23 ft propeller material.

Search-result extract, not a full ASME download:

- Scribd text of Zekas and Schultz, ASME GT1997, returned inside the results for query 13. Gave length overall 753 feet 8.5 inches, beam 107 feet, mean draft full load 37 feet 10 inches, displacement 48,500 long tons, 100,000 HP, four LM2500s, two Cincinnati Gear reduction gears, two SSS-TOSI RCCs per shaft, fixed-pitch propellers, trials 2 February 1993, delivery 29 October 1993. Gear ratio and shaft rpm were not in the extract that was actually read, so they are not in the dossier.

## Failed or unused fetches

- https://www.navy.mil/DesktopModules/ArticleCS/Print.aspx?PortalId=1&ModuleId=4201&Article=2174658 — web_fetch Access Denied. Replaced by the successful fact-file article read.
- https://www.msc.usff.navy.mil/Ships/Ship-Inventory/Fast-Combat-Support-Ships — web_fetch Access Denied. Not used. A search snippet had length 754 ft, beam 107 ft, displacement 48,500 tons, speed 25+ knots, civilian crew 170. Those cells are not in the dossier.
- MSC handbook PDFs were indexed by search and not opened. A snippet that aligned draft 38 ft and a cargo set with T-AOE 6/8 was not used, because the column alignment was not verified.
- https://apps.dtic.mil/sti/tr/pdf/ADA304147.pdf — DTIC maintenance page. No hangar sentence.
- https://dn760103.eu.archive.org/0/items/DTIC_ADA304147/DTIC_ADA304147.pdf — archive.org copy searched; hangar, flight deck, CH-53, and workboat phrases did not match. The indexed thesis sentence about three hangars, a port VERTREP conversion, two CH-46s, CH-53 certification, and a 35-foot workboat is not used.
- ASME digital-collection PDF was not downloaded. The Scribd extract above was used instead.
- https://www.navsource.net/archives/09/59/5906.htm — not fetched. A search snippet draft of 40 ft is not used.
- site:nvr.navy.mil did not return a characteristics page. IMO, MMSI, and call sign are cited only from the Wikipedia ship page's NVR incorporation.
- Forecast International, archived December 2000, was a search snippet that repeated 753 ft 8.5 in and 37 ft 10 in. Treated as the same data-sheet family as the ASME paper, not as a second measurement. Its cargo-transfer table looked garbled and was not used. A 10,000 nm range in that snippet was not used.
- GAO/NSIAD-93-298 product page was search-indexed. The PDF was not opened in full. The dossier uses only the lead-ship contract figure $862.9 million, the seven-to-four cut, combatant standards, and the reversing-gear first. https://www.gao.gov/products/nsiad-93-298

## Game data quoted

unit-dimensions source string: "Supply-class T-AOE: 754 ft (229.8 m), beam 107 ft (32.6 m). Height 42 m is a representative keel-to-mast envelope."

Roster dimension block, name "USNS Manna (T-AOE-26)":

```
"dimensions": {
  "lengthM": 229.8,
  "widthM": 32.6,
  "heightM": 42,
  "massTonnes": null,
  "basis": "representative"
}
```

## Numbers that failed the two-source test

- Waterline 730 ft: shipscribe only.
- Draft 38 ft max nav: shipscribe only. Draft 37 ft 10 in mean full load: ASME extract only. Draught 12 m: Naval Technology only. 39 ft (11.9 m) appears on navysite and Wikipedia and may be one shared sheet.
- Light displacement 20,840: shipscribe only. 19,700 tons: FAS family, repeated by Wikipedia.
- Full-load figures 48,800 / 48,603 / 48,500 long tons / 49,000 tons disagree. No average.
- Power 105,000 hp versus 100,000 hp. Both families have more than one printing. They disagree.
- Speed 25 knots versus 26 knots. Cruise 22 kt: Naval Technology only.
- Range 6,000 miles versus 6,000 nm. Not the same unit. Neither is dual-confirmed.
- Propeller diameter 23 ft: FAS, repeated by Naval Technology. Not two measurements.
- Two low funnels: shipscribe only.
- 3,000 gallons per minute: navysite only.
- Five service diesel generators and a cargo control centre: Naval Technology only.
- IMO 8644199, MMSI 338947000, call sign NACO: Wikipedia/NVR only.
- Homeport none versus Earle, N.J.
- Crew sets disagree. Aircraft counts two versus three disagree.
- URN-25: Naval Technology only.
- Keel-to-mast and flight-deck height: not public. Wikipedia "height 39 ft (12 m)" is not a mast height.
- Hangar count and hangar-door travel: not public.
- Station offsets: not public.
- Gear ratio and maximum shaft rpm: not in the ASME extract that was read. Not printed.

## Game conflicts

- lengthM 229.8 matches Wikipedia's conversion of 754 ft and does not match the Navy fact file's printed 229.9 m, the ASME 753 ft 8.5 in, or the 754.6 ft printed by navysite and the ship Wikipedia page.
- widthM 32.6 matches the 107 ft / 32.6 m sources. The ship Wikipedia page rounds 107 ft to 33 m.
- heightM 42 is the game file's own representative keel-to-mast envelope. No public factory height was found, so 42 m is unsupported rather than a contradiction of a published mast height.
- massTonnes null. Left null on purpose. Displacement is not a single public tonne figure.
- The roster name USNS Manna (T-AOE-26) is a game rename of the real USNS Supply (T-AOE-6).
