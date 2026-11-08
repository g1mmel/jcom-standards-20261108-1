# Research log: fgs-braunschweig-k130

- Start local time: 2026-10-14T15:14:43-04:00
- End local time: 2026-10-14T15:32:42-04:00
- Search count: 12
- Fetch count: 6 page reads used. Two further URLs were not fully read: one Wikipedia ship page stayed a search extract, and one Naval News page was blocked.

A separate clock was not stored at the first K130 query. The twelve queries below were run in the same paired-dossier session that started at 2026-10-14T15:14:43-04:00, after the Type 26 queries and before the finish time above. They are not the Type 26 queries. Query 4, query 7, and query 8 name the Sa'ar 6 because the worklist names that dossier as the base and asks for a re-check of 91.4 m. They are K130-audit queries, not a second count of Type 26 searches.

Asset: fgs-braunschweig-k130. Base: saar-6-corvette. Worklist similarity: same-class comparison, not same-family. Different navy and different hull. Sa'ar 6 weapons were not copied.

Bases read before writing:

- C:\Users\MAXGLA~1\AppData\Local\Temp\grok-dr-bases\saar-6-corvette--217.md (INS Magen blueprint, including the modelled 11-station table, which was not copied).

Not opened:

- C:\cnc_rev\canon\reference\eretz\dossiers\naval-expert-references\saar-6-corvette.md at 61,019 bytes. The task forbids opening any saar-6 file larger than 20 KB. The 91.4 m citation attributed to that pack was re-checked on the live Naval Technology Sa'ar 6 page instead. That page states overall length 90 m and does not state 91.4 m.

## Queries

1. K130 Braunschweig Korvette Länge Breite Tiefgang Verdrängung site:bundeswehr.de
2. Braunschweig-class corvette K130 length beam draft displacement specifications
3. K130 Braunschweig RBS-15 RAM 76 mm MLG 27 TRS-3D armament
4. Sa'ar 6 corvette length beam displacement TKMS OR "Naval Technology" 90 OR 91.4
5. K130 Braunschweig "89.12" OR "89,12" displacement 1840 TKMS OR Lürssen OR "Blohm"
6. FGS Braunschweig F260 flight deck hangar UAV no hangar helicopter
7. Sa'ar 6 "91.4" OR "91.4 m" length corvette Naval Technology
8. Sa'ar 6 INS Magen beam draft "13.2" OR "3.4 m" OR "21.5" height TKMS
9. K130 Braunschweig waterline length 82.8 beam 12.44 hull height air draft
10. Braunschweig-class Batch 1 TRS-3D versus Batch 2 TRS-4D RBS15 launcher count
11. K130 Braunschweig MASS Mirador Minenschiene 12,7 mm Stammbesatzung site:bundeswehr.de
12. TKMS OR "thyssenkrupp" K130 Braunschweig corvette length 89 displacement diesel technical data

## Fetches

Successful:

1. https://www.bundeswehr.de/de/ausruestung-technik-bundeswehr/seesysteme-bundeswehr/korvette-k130 — title "Korvette K130", page dated 05.11.2019. web_fetch dropped the Maße cell. open_page_with_find recovered line 63: "89,1 m Länge (über alles) 13,3 m Breite 3,4 m Tiefgang 1.800 t Verdrängung". The same page gives 3.4 m maximaler Tiefgang, two diesels at 14,800 kW (20,100 PS), one bow thruster, two propellers, more than 26 knots, TRS-3D above 200 km and above 750 tracks, UL 5000 K, two Mirador, two navigation radars, 76 mm Compact above 18 km, two 27 mm MLG, four 12.7 mm, two RBS15 Mk3 starters, two RIM-116 RAM starters, four mine rails, two MASS, Stammbesatzung 61, F260 commissioned 16 April 2008, helicopter drones, and an X-form caption. Sister commission dates are on the page and were not needed for the dimension table.
2. https://www.bundeswehr.de/de/organisation/marine/aktuelles/baltops-2024-deutsche-korvetten-ostsee-5809050 — title "BALTOPS 2024: Deutsche Korvetten in der Ostsee". Full fetch. Gave "nur viereinhalb Meter Tiefgang", verstellbarer Antriebspropeller, bow thruster, 1. Korvettengeschwader at Rostock-Warnemünde, crews over 60, Magdeburg as 1,800 tonnes, RAM within ten kilometres, RBS15 more than 200 km and warhead more than 200 kg, an MH-60R on Magdeburg's flight deck to refuel, mine laying, and helicopter drones. Same publisher as the equipment page.
3. https://www.naval-technology.com/projects/k130corvette/ — title "K130 Braunschweig Class Corvette". Full fetch. The specification box and the body contradict each other. Box: 89.12 m, waterline length 82.8 m, beam 13.28 m, waterline breadth 12.44 m, hull height 4.8 m, depth at waterline 3.4 m, full load 1,840 t, crew 50, 26 knots. Body: about 1,580 t, about 88 m, 13.2 m, crew 50, over 26 knots. Also Super Rapid at 120 rpm, four RBS15 Mk3, RAM 21 cells and 9.5 km, two MTU 20V 1163 TB 93 at 7.4 MW, controllable-pitch propellers, over 2,500 nm, 7 days or 21 with a tender, Blohm+Voss, April 2006 launch, April 2008 Warnemünde commission, Pathfinder ST Mk2, EADS SPS-N 5000, and KJS 5000.
4. https://en.wikipedia.org/wiki/Braunschweig-class_corvette — title "Braunschweig-class corvette". Fetch truncated after the characteristics block; the infobox was in the retained text. Gave 1,840 t (1,810 long tons), 89.12 m (292 ft 5 in), 13.28 m (43 ft 7 in), 3.4 m (11 ft 2 in), 4 x 550 kW MTU 12V 1600 DS550, 2 x 7.4 MW 20V 1163 TB 93 with CPP, bow thruster, 26 knots, 4,000 nmi at 15 knots, 7 or 21 days, complement 65, TRS-3D batch 1 and TRS-4D batch 2, two navigation radars, MSSR 2000 i, MIRADOR, UL 5000 K, Link 11 and 16, two MASS, 76 mm, two BK-27, four RBS15 Mk3, two RAM Block II of 21, two mine racks of 34 Mk 12, helicopter pad and hangar for two drones. Lists the Sa'ar 6 as a successor or subclass. The unread remainder was not used.
5. https://www.naval-technology.com/projects/saar-6-class-corvettes/ — title "Sa'ar 6 Class Corvette". Full fetch, for the base audit only. Gave 90 m, beam 13.2 m, height 21.5 m, about 2,000 t, crew up to 70, MEKO 100, SH-60 hangar, 40 Barak 8, up to two C-Dome, 76 mm Super Rapid, Gabriel/Harpoon/RBS-15 as options, two Typhoon 30 mm, two Mk 54 tubes, ELM-2248 MF-STAR, CODAD, two MTU diesels, two CPPs, about 26 knots, range 2,500 miles as printed. No 91.4 m. No draft.
6. https://en.wikipedia.org/wiki/Sa%27ar_6-class_corvette — title "Sa'ar 6-class corvette". Fetch truncated after the characteristics; those were in the retained text. Gave 1,900 long tons full load, 90 m (295 ft 3 in), complement 70, loosely based on the Braunschweig class. Infobox: 16 Barak MX cells, 40 C-Dome, 8 Gabriel V, two Typhoon, two 324 mm tubes, MH-60. Prose: up to 16 Gabriel. Beam and draft absent. Unread remainder was not used.

Not fully read:

- https://en.wikipedia.org/wiki/German_corvette_Braunschweig — search extract only. Used for hangar too small for Sea King, Lynx, or NH90, pad large enough, and two Skeldar. A Wilhelmshaven home-port line in search was not adopted.
- https://www.navalnews.com/naval-news/2020/11/tkms-hands-over-saar-6-corvette-ins-magen-to-the-israeli-navy/ — fetch returned a WAF block, not the article. Search snippet only: TKMS key data, length overall about 90 m, beam 13 m, full load about 1,900 t. Not treated as a full read. Wikipedia and Naval Technology Sa'ar 6 pages are the successful dimension reads for that class.

Same-publisher corroboration, not a second independent publisher:

- The BALTOPS article repeats 1,800 tonnes for Magdeburg.
- A Bundeswehr PDF seen in search repeats 89.1 m, 13.3 m, 3.4 m, and 1,800 t. Logged here and not counted as an independent source in the dossier.

Not used: GlobalSecurity Sa'ar 6 specifications, because that page mixes K130 numbers into the Sa'ar 6. seaforces, globalmilitary, shipshub, helis, and defencedb were not used as independent of Wikipedia.

## Numbers that failed the two-source test

Not public for the K130: length between perpendiculars, masthead air draft, design versus navigational versus full-load draft as a single condition, gun elevation and recoil, launcher elevation, rudder angle, radar rotation rate, door travel, and any station or pivot coordinate.

Single-source, labelled in the dossier:

- Waterline length 82.8 m, waterline breadth 12.44 m, hull height 4.8 m: Naval Technology specification box. The same page's body does not repeat them and contradicts length, beam, and displacement.
- Naval Technology body about 1,580 t, about 88 m, 13.2 m, and crew 50: same page as the specification box, so this is an internal contradiction, not a second source.
- Four 12.7 mm mounts, 76 mm range greater than 18 km, TRS-3D greater than 200 km and greater than 750 tracks, X-form caption: Bundeswehr equipment page.
- 120 rounds per minute and the Super Rapid name: Naval Technology. The Bundeswehr page says 76 mm Compact.
- RAM 9.5 km: Naval Technology. BALTOPS says within ten kilometres. Two ranges, two sources, not averaged.
- RBS15 greater than 200 km and warhead greater than 200 kg: BALTOPS article.
- Pathfinder ST Mk2, EADS SPS-N 5000, and KJS 5000: Naval Technology. UL 5000 K is the Bundeswehr and Wikipedia name and was not merged with those strings.
- 4 x 550 kW MTU 12V 1600 DS550, MSSR 2000 i, Link 11, Link 16: Wikipedia.
- Two Skeldar and the hangar-too-small sentence: Wikipedia ship-page search extract only.
- Blohm+Voss as builder and the April 2006 launch: Naval Technology. Commission in April 2008 is that page plus the Bundeswehr date 16 April 2008.
- Sa'ar 6 height 21.5 m: Naval Technology only, and it is not a K130 figure.
- TKMS snippet beam 13 m and full load about 1,900 t: one blocked page's search snippet, for the Sa'ar 6 audit only.

Not found, so not published: 91.4 m; Sa'ar 6 LBP 84.5 m; Sa'ar 6 waterline beam 12.1 m; Sa'ar 6 draft 3.400 m; Sa'ar 6 air draft 28.5 m.

## Contradictions versus the base

The base is a different hull. Almost every Sa'ar 6 particular is a difference. Printed, not averaged:

- K130 length: Bundeswehr 89.1 m; Wikipedia and the Naval Technology box 89.12 m; Naval Technology body about 88 m. Base 90.000 m does not hold for F260. For the Sa'ar 6, 90 m does appear on Naval Technology, Wikipedia, and the TKMS snippet. The millimetre form 90.000 m does not. 91.4 m does not appear on the fetched Naval Technology page.
- K130 beam: 13.3 m, 13.28 m, and 13.2 m in the Naval Technology body. Base 13.200 m is the Sa'ar 6 dossier. Live Sa'ar 6 beam is 13.2 m on Naval Technology and 13 m in the TKMS snippet. Wikipedia's Sa'ar 6 table has no beam.
- K130 draft: 3.4 m on the Bundeswehr equipment page, Wikipedia, and the Naval Technology box, against 4.5 m in the Bundeswehr BALTOPS article. Base keel Y = -3.400 m does not hold. No Sa'ar 6 draft was found to rescue it.
- K130 displacement: 1,800 t, 1,840 t, and about 1,580 t. Base about 1,900 t is a Sa'ar 6 claim. Live Sa'ar 6 figures are about 2,000 t (Naval Technology), 1,900 long tons full load (Wikipedia), and about 1,900 t (TKMS snippet). Not copied onto F260 and not averaged with each other.
- K130 waterline length 82.8 m is single-source and is not an LBP. Base LBP 84.5 m and waterline beam 12.1 m were not found.
- Air draft. K130 not public. Base +28.500 m not found. Naval Technology Sa'ar 6 height 21.5 m is a third, different number for the other ship.
- Weapons. Base Barak 32, C-Dome 40, Gabriel V, Typhoon 25 mm, and MF-STAR do not appear on the Bundeswehr K130 list. K130 public fit is 76 mm Compact or Super Rapid, two 27 mm, four 12.7 mm, RBS15 Mk3, RAM, mine rails, MASS, and TRS-3D. Sa'ar 6 Barak counts disagree among themselves (base 32, Wikipedia infobox 16, Naval Technology 40). Gabriel counts disagree (infobox 8, prose up to 16, Naval Technology lists options). Typhoon calibre disagrees (base 25 mm, Naval Technology 30 mm). None of those Sa'ar counts was chosen for F260.
- Aviation. Base and the Naval Technology Sa'ar 6 page describe an SH-60-capable hangar. K130 sources describe a drone hangar, with a manned helicopter documented as a deck landing to refuel on the sister Magdeburg.
- Propellers. The base video prompt's controllable-pitch propellers do match the K130 wording on Naval Technology, Wikipedia, and BALTOPS. The engine model and the absence of a gas turbine are stated from the K130 sources. Rudder angle plus or minus 35 degrees, director coordinates, and #00FF00 do not hold.
- Crew. K130 61, 65, and 50. Sa'ar 6 pages say up to 70 or complement 70.
- Hull angles and the 11-station table. Modelled. Not public.

## Game conflicts

no unit-dimensions row

no roster row

No braunschweig or k130 row in `C:\cnc_rev\data\rules\unit-dimensions.json` or `C:\cnc_rev\data\roster\jslc.json`.

The existing Sa'ar 6 rules row must not be applied to F260. `jslc.vehicle.saar-6-corvette` and `coalition.vehicle.saar-6-corvette` are lengthM 90, widthM 13, heightM 28, with the note that mast height 28 m is representative. The roster weapons are mk32-svtt-mk54, oto-melara-76-62-super-rapid, barak-8-vls, cdome-tamir-vls, gabriel-v-anti-ship-missile, and typhoon-25mm-spike-er. That is the Israeli game fit. Height 28 m matches neither Naval Technology's Sa'ar 6 height of 21.5 m nor the base dossier's 28.5 m, and it is not a K130 air draft.
