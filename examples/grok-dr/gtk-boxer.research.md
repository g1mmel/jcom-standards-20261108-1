# Research log: gtk-boxer

- Start local time: 2026-10-14T15:14:41-04:00
- End local time: 2026-10-14T15:32:16-04:00
- Elapsed: about 18 minutes from the recorded start to the finish stamp. Writing followed the last fetch.
- Search count: 12 distinct web_search queries for this asset.
- Fetch count: 11 successful page reads (web_fetch or open_page). One Think Defence URL returned only a title and was replaced by the variants page the tool actually opened.

## Queries

1. GTK Boxer Bundeswehr Gepanzertes Transport-Kraftfahrzeug mission module APC command ambulance dimensions
2. GTK Boxer Bundeswehr FLW 200 Gruppentransportfahrzeug technische Daten 36,5 t 8,3 m
3. Boxer 8x8 Rheinmetall KMW ARTEC length width height combat weight tire 415/80R685
4. Boxer Schakal RCT30 Bundeswehr Radschützenpanzer versus GTK Gruppentransportfahrzeug FLW 200
5. OCCAR Boxer Germany drive module mission module APC command ambulance quantities
6. Boxer GTK "415/80" Michelin German OR Dutch tyre OR tire ARTEC
7. Schwerer Waffenträger Infanterie Boxer Lance Bundeswehr 123 Fahrzeuge
8. Bundeswehr GTK Boxer Wendekreis 21 Meter Allison HD4800 MTU 8V 199 TE20
9. KNDS Boxer GTFz Höhe Dach 2,94 m Gewicht 36,5 t fernbedienbare Waffenstation
10. Rheinmetall FLW 200 elevation range LAZ 400 Bundeswehr GTK Boxer remote weapon station
11. ARTEC last GTK Boxer delivered Bundeswehr 405 vehicles army-technology infantry group ambulance command
12. Boxer armoured fighting vehicle Allison HD4070 versus HD4800SP Wikipedia specification table MTU

## Fetches

1. https://www.bundeswehr.de/de/ausruestung-technik-bundeswehr/landsysteme-bundeswehr/gtk-boxer — Title: Ausrüstung und Technik: GTK Boxer. Dated 01.02.2023. Layout, four introduced versions, 530 kW/720 PS, 103 km/h, turning circle, powerpack, FLW 200, LAZ 400 (L), seats, rear hatch. First markdown render dropped the length cell. A second pattern read of the same URL restored the table: Länge 8,3 m, Höhe 3,4 m, Breite 3 m, Gefechtsgewicht 36,5 t, Besatzung maximal 10 (GTF).
2. https://www.artec-boxer.com/vehicles/armoured-personnel-carrier/ — Title: Armoured Personnel Carrier | Artec Boxer. Family key figures listed in the dossier. APS is an exemplary option.
3. https://knds.com/en/products/systems/boxer/boxer-gtv — Title: BOXER GTV | KNDS Group. Two lengths on one page (7.9 m and 8.01 m), roof height 2.94 m, width 2.99 m, class A/C 36.5 t, 530 kW, crew 3+7, about 14 m3, remote station.
4. https://occar.int/our-work/programmes/boxer-a-multi-role-armoured-vehicle/general-information — Title: OCCAR general information. 605 DE+NL vehicles in nine variants delivered. 2025: 48 additional DE vehicles and 222 Schakal IFVs for DE and NL.
5. https://www.rheinmetall.com/de/media/news-watch/news/2024/05/2024-05-03-schwerer-waffentraeger-infanterie-fuer-die-bundeswehr-nachweismuster-vorgestellt — Title: Schwerer Waffenträger Infanterie für die Bundeswehr | Rheinmetall, 03.05.2024. 123 Lance vehicles, not the GTF.
6. https://de.wikipedia.org/wiki/GTK_Boxer — Title: GTK Boxer – Wikipedia. Mobility list, seven-versus-eight seat sentence, smoke-launcher photo captions. Infobox length and mass cells did not survive the markdown extract, so 7.93 m and 36.5 t were not taken from this fetch.
7. https://en.wikipedia.org/wiki/Boxer_(armoured_fighting_vehicle) — Title: Boxer (armoured fighting vehicle) - Wikipedia. Hull 7.93 / 2.38 / 2.99 m, HD4800SP table versus HD4070 prose, turning radius 10.5 m or 7.5 m, 36.5 t and 38.5 t columns, 720 PS (530 kW) versus a prose 711 hp conversion.
8. https://www.army-technology.com/news/artec-gtk-boxer-vehicles-bundeswehr/ — Title: ARTEC completes delivery of GTK Boxer vehicles to Bundeswehr, 24 June 2021. Repeats 405, 72 ambulance, 65 command, 256 infantry group vehicles.
9. https://knds.com/en/products/systems/flw-200-range/flw-200 — Title: FLW 200 | KNDS Group. Elevation, traverse, speeds, mass, ammunition. Product sheet, not a German serial-vehicle measurement.
10. https://www.rheinmetall.com/de/media/news-watch/news/2021/2021-06-23_lieferung-der-bisher-durch-die-bundeswehr-beauftragten-gtk-boxer-abgeschlossen — Title: Lieferung der bisher durch die Bundeswehr beauftragten GTK Boxer abgeschlossen, 23/06/2021. Primary 405-vehicle handover text.
11. https://www.thinkdefence.co.uk/docs/boxer-variants/ — Opened after https://www.thinkdefence.co.uk/2022/11/boxer-armoured-vehicle-details-and-variants/ returned only the title "Boxer (Variants) - Think Defence." The variants page confirms German FLW-200 versus separate Lance and Schakal lines, and gives ambulance 17.5 m3 and 1.85 m floor-to-roof. It does not give the 415/80R685 code. That code stays unused.

## Numbers that failed the two-source test

- Bundeswehr 8.3 m, 3.4 m, and the rounded 3 m width: official table, one publisher. 2.99 m is the multi-source manufacturer/Wikipedia width and is printed beside 3 m, not averaged into it.
- KNDS 7.9 m and 8.01 m: one page, two values. Neither was averaged with 7.93 m or 8.3 m.
- KNDS roof height 2.94 m: single-source.
- FLW angles, laying speeds, 185 kg, 750 mm, rotation radii, and ammunition counts: KNDS product sheet only.
- Driver periscope count of three, track 2.58 m, wheelbase 1.55+1.90+1.55 m, fording 1.20 m, deep wade 1.50 m: German Wikipedia only.
- Gear count 7 forward / 3 reverse: English Wikipedia only. The same page also names HD4070 in prose against HD4800SP in the table and on the Bundeswehr page.
- Wikipedia torque 2,699 N·m and 2,999 N·m: not used. single-source and not required.
- Empty masses 24.0 / 25.2 / 28.0 t: English Wikipedia chassis columns only. Not a Bundeswehr empty weight.
- Ambulance floor-to-roof 1.85 m: Think Defence only. 17.5 m3 also appears as the top of the German Wikipedia 14–17.5 m3 range.
- Tire code 415/80R685: searched, not present on a fetched page for the German fit. Marked not public.
- Glacis 15 deg and 22 deg, sponson widths, plate angles, steer plus or minus 30 deg, gun-forward 8.85 m and 8.23 m: base claims, not re-verified.
- Army Technology 405 split is the Rheinmetall press release repeated, not a second count. 72+65+256 = 393, and the Rheinmetall text still says 405. The missing 12 are not named in the fetched release.
- OCCAR "605 delivered" (DE+NL, nine variants) is later than the June 2021 figure of 405. Both are printed. They are not averaged.
- A November 2025 trade snippet that splits 150 Schakal for Germany plus 38 ambulances and 10 driver trainers was not fetched. Not used. The fetched OCCAR sentence is 48 additional German vehicles and 222 Schakal for Germany and the Netherlands.

## Contradictions versus the base

- `--93` and `--172` describe a tracked GTK. The Bundeswehr vehicle is an 8x8.
- `--171` Lance blueprint (8.85 m gun-forward, 3.24 m turret roof, 38.5 t, 415/80 R685, glacis 15 deg, invented wheel XYZ, StrikeShield) is an IFV/export-style sheet. The introduced German GTK uses FLW 200 on the APC and command vehicle. 38.5 t is a family maximum GVW on the ARTEC APC page, not the 36.5 t German table.
- `--93` combat weight 45 t and width-style claims do not match 36.5 t or 2.99 m / 3 m.
- HD4070 versus HD4800SP is inside English Wikipedia. Bundeswehr says HD4800SP.
- Turning circle 21 m / about 16 m (Bundeswehr) versus turning radius 10.5 m / 7.5 m (Wikipedia) versus 7.50 m skid radius (ARTEC). Not merged.
- Power 530 kW/720 PS (Bundeswehr) versus up to 600 kW (ARTEC family) versus a Wikipedia prose line that calls 530 kW "711 hp."

## Game conflicts

- No boxer or gtk row in `unit-dimensions.json` or `jslc.json`.
- USS Boxer LHD-4 is a ship string only.
- Mesh audit `--288`: bounding box 3.34 m wide, 3.33 m high, 7.93 m long. Width does not match 2.99 m or 3 m. Length matches the family hull figure only. The mesh is not a factory sheet.
