# Research log: as32a-31a-tow-tractor

- Start local time: 2026-10-14T15:14:41-04:00
- End local time: 2026-10-14T15:32:16-04:00
- Elapsed: about 18 minutes from the recorded start to the finish stamp.
- Search count: 14 distinct web_search queries for this asset.
- Fetch count: 6 successful pages or PDFs, plus 1 failed fetch that was replaced by already-retrieved Navy PDFs rather than by a new manual.

## Queries

1. A/S32A-31A aircraft towing tractor specifications dimensions weight NAVAIR
2. NSN 1740-01-379-4633 A/S32A-31A tractor wheeled aircraft towing
3. A/S32A-31A leading particulars 12400 pounds 117 inches NAVEDTRA 14329
4. "A/S32A-31A" "drawbar" OR "gross weight" OR "turning radius" site:navy.mil OR site:navair.navy.mil
5. NAVEDTRA 14329 A/S32A-31A tow tractor drawbar pull 8500 dual rear wheels
6. A/S32A-32 spotting dolly leading particulars length width height weight turning radius NAVEDTRA
7. Navy NTSP tow tractor A/S32A-31A Detroit Diesel engine horsepower "10,000 pounds"
8. "3337AS100" A/S32A-31A tractor length width height pounds
9. NAVAIR 19-40-521 A/S32A-31A aircraft towing tractor manual leading particulars
10. MSU-200NAV air start unit mounted A/S32A-31A tow tractor NAVAIR
11. ALBAR tow bar aircraft carrier A/S32A-31A pintle F/A-18 NAVAIR 00-80T-96
12. A/S32A-31A six-wheel counterweights drawbar pull pintle NAVEDTRA 14353A
13. NAVEDTRA 14353A chapter 2 A/S32A-31A Table 2-3 basic length 117 inches PDF
14. "Table 2-3" "A/S32A-31A" "Basic length" 117 OR "117 inches" NAVEDTRA

Query 4 did not return a navy.mil or navair.navy.mil tractor page. Queries 10, 11, and 12 returned snippets of NAVEDTRA 14353A and ALBAR prose. Those PDFs were not successfully fetched, so the snippet numbers were not written into the dossier.

## Fetches

1. https://www.nsnlookup.com/fsg-17/fsc-1740/us/1740-01-379-4633-tractor-wheeled-aircraft-towing-1740013794633-013794633-3337as100-s32a-31a — Title on the fetch: 1740-01-379-4633 Aircraft Towing Wheeled Tractor. Gave the NSN, part number 3337AS100-1, designator A/S32A-31A, FSC class boilerplate, and a shipping schema of 14140 lb and 151 x 104 x 74 in. Did not give the FLIS characteristic table.
2. https://www.wbparts.com/rfq/1740-01-379-4633.html — Title: 1740-01-379-4633 - AIRCRAFT TOWING WHEELED TRACTOR | WBParts. NSN assigned 31 AUG 1993. DRAWBAR PULL 8500.0 POUNDS NOMINAL. OVERALL LENGTH 117.000 FEET NOMINAL. OVERALL WIDTH 65.000 FEET NOMINAL. OVERALL HEIGHT 36.000 FEET NOMINAL. III CUBIC MEASURE 158.4400 CUBIC FEET. III UNPACKAGED UNIT WEIGHT 12000.00 POUNDS. CAGE 30003 for 3337AS100-1. CAGE 80058 for A/S32A-31A.
3. https://www.globalsecurity.org/military/library/policy/navy/ntsp/Towtractor.pdf — PDF, 84 pages, N88-NTSP-A-50-8411B, June 1998, TOW TRACTORS. Gave the 31A line: gross 12400 lb, drawbar 10000 lb, 115 x 70 x 40 in, ground clearance 7.5 in, turning radius 132 in, Detroit Diesel two-cycle three cylinders. Predecessor 31 line: 12000 lb, 8500 lb, 117 x 65 x 36 in, same clearance and turning radius, same engine sentence. 32 line: 11200 lb, 10000 lb, 148 x 81 x 29 in, clearance 5 in, turning radius 0. Delivery of the 31A completed January 1998. NAVAIR 19-40-521 named as the 31A manual.
4. https://www.globalsecurity.org/military/library/policy/navy/nrtc/14014_chp9.pdf — PDF, 26 pages, NAVEDTRA 14014 chapter 9. Gave the 31A prose (driver only, three-cylinder diesel, automatic transmission, dual rear wheels, power-assisted front steering, wet-disc brakes, mechanical hand brake, 24 V, front and rear pintles, universal jet start unit on the rear) and the 32 spotting-dolly prose (joystick, lift and spread cylinders, caster, zero turning radius).
5. https://navyaviation.tpub.com/14014/css/A-S32A-31A-Aircraft-Towing-Tractor-216.htm — Same 31A sentences. The HTML places the A/S32A-30A cab sentence (driver and one passenger) immediately before the 31A heading. The PDF shows that sentence is still the 30A paragraph.
6. https://navyaviation.tpub.com/14014/css/A-S32A-32-Aircraft-Towing-Tractor-217.htm — Continuation: 24 V, pintles, rear start unit, then the full spotting-dolly paragraph, then the A/S32A-37.

Failed and not used for numbers:

- https://pdf4pro.com/cdn/chapter-2-aircraft-handling-equipment-nonskid-and-markings-440f4a.pdf — 403 Forbidden. This was the public copy of NAVEDTRA 14353A chapter 2. Table 2-3 was therefore not read. Dropped from the dossier: any 14353A "basic length 117 inches," the 8500 lb training-manual drawbar, 85 gal, 70/60 psig, left-side seat, three-speed versus four-speed conflict, 1500 psi brake warning, 196 F and 220 F limits, "six-wheel" sentence, counterweight sentence, and MSU-200NAV model name.

## Numbers that failed the two-source test

- 12,400 lb gross: only the NTSP 31A line among fetched measurement sources. FLIS says 12,000.00 lb unpackaged on the same NSN.
- 10,000 lb drawbar: only the NTSP 31A line. FLIS says 8,500.0 lb nominal.
- 115 in length, 70 in width, 40 in height: only the NTSP 31A line. FLIS prints 117 / 65 / 36 and labels the unit FEET.
- 7.5 in ground clearance and 132 in turning radius: only the NTSP. The predecessor line in the same PDF repeats them. That is one publication.
- "Detroit Diesel" and "two-cycle": only the NTSP. NAVEDTRA 14014 says three-cylinder diesel only.
- NSN assignment date, CAGEs, cubic feet, and the feet-labeled FLIS dimensions: only WBParts.
- Shipping 14,140 lb and 151 x 104 x 74 in: only NSN Lookup, and it is a shipping schema.
- Wheelbase, track, speed, steering angle, horsepower, fuel, tire size, pintle coordinates: not public in the fetched pages.
- A/S32A-32 height 29 in, gross 11,200 lb, drawbar 10,000 lb, clearance 5 in, turning radius 0 in: only the NTSP. Zero turning radius as a capability is also in NAVEDTRA 14014, so the capability is dual-source. The 0 inch figure is the NTSP number.

## Contradictions versus the base

- Base calls the 31A a 4-wheeled 12,400 lb flight-deck tractor. Fetched manual: dual rear wheels, driver only, pintles. Weight is 12,400 lb in the NTSP and 12,000 lb in FLIS.
- Base 32 sheet uses 11,500 lb, 30 in chassis height, 6 in clearance, 54 in roll guard, 7,000 lb curb, and a 3,000/8,000 lbf drawbar pair. Fetched NTSP 32 line is 11,200 lb, 29 in height, 5 in clearance, 10,000 lb drawbar. Length 148 in and width 81 in agree. The other base 32 figures were not re-verified. NSN 1740-01-270-3615 was not re-checked.
- Knowledge-pack draft figures (91 in wheelbase, 80 in alternate wheelbase, 101 hp, plus or minus 35 deg, 12 mph, 85 gal, ALBAR table, 193 in LOA) stay unresolved. The 2026-10-09 review in carrier-tow-tractors.md already said so. This pass did not re-find a public wheelbase.

## Game conflicts

- No as32a-31a row.
- `jslc:shared:deck-tow-tractor` and the sibling keys `coalition.vehicle.deck-tow-tractor`, `TowTractor`, and `FlightDeckTractor` are 6 x 2.4 x 2.2 m, source UNVERIFIED, confidence low, designSize false.
- 6 x 2.4 x 2.2 m is larger than the 31A (115 x 70 x 40 in, or the FLIS 117 x 65 x 36) and larger than the 32 (148 x 81 x 29 in). It matches neither machine. The key name is the spotting-dolly asset, not a confirmed 31A row.
