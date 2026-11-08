---
generated_at: "2026-10-14T15:32:16-04:00"
generator: "dolphin2/dossier-grok-dr"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "xai"
models:
  - "grok-4.7"
query: "German Army GTK Boxer 8x8 GTF FLW 200 versus ARTEC Lance and tracked base claims"
sources_count: 13
asset_id: "gtk-boxer"
title: "Naval Architectural Blueprint Dossier: German Army GTK Boxer 8x8"
base_asset_id: "boxer-ifv"
---

# Naval Architectural Blueprint Dossier: German Army GTK Boxer 8x8

**Classification:** Unclassified. Official Bundeswehr equipment page, manufacturer pages, OCCAR, and secondary encyclopedias. Not a STANAG drawing.
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

GTK is the Bundeswehr name for the Boxer. The page states the official name Gepanzertes Transport-Kraftfahrzeug (GTK) Boxer [1]. English Wikipedia states that GTK is the official Bundeswehr designation for Boxer [10]. The vehicle in German service that this dossier describes is the wheeled 8x8 with a drive module and a mission module. The introduced versions on the Bundeswehr page dated 01.02.2023 are the Gruppentransportfahrzeug (APC), the Führungsfahrzeug (command), the schweres geschütztes Sanitätskraftfahrzeug (ambulance), and the Fahrschulfahrzeug (driver training) [1]. The Gruppentransportfahrzeug and the command vehicle carry the FLW 200 remote weapon station. They do not carry a Lance turret on that page.

Two later German programs are different machines and are not folded into the GTF dimensions: the Schwerer Waffenträger Infanterie (123 vehicles, manned Lance turret, Australian CRV basis) [7], and the Schakal / Boxer RCT30 order described by OCCAR in 2025 [5].

### 1. MASTER COORDINATE DATUM & DIMENSIONS

glTF datum: forward = -Z, up = +Y, starboard/right = +X, port/left = -X, tire contact Y = 0. Metric-to-imperial cells marked "converted" use 1 m = 3.280839895 ft (1 ft = 0.3048 m) and 1 kg = 2.2046226218 lb. They are not a second source.

The Bundeswehr technical table is the German GTF sheet. Manufacturer pages publish a family hull that is not labeled as that same measurement.

| Parameter | Metric | Imperial | Engineering notes |
| --- | --- | --- | --- |
| Configuration | 8x8 wheeled. Drive module plus mission module | same | Bundeswehr: permanenter Allradantrieb and Einzelradaufhängung [1]. ARTEC APC page: 8x8 family APC [2]. Not tracked. |
| Length, German GTF table | 8.3 m | 27.23 ft converted | Bundeswehr table row "Länge Gruppentransportfahrzeug" 8,3 m [1]. The page does not say whether this includes a weapon, a bumper, or the hull only. |
| Length, family hull | 7.93 m | 26.02 ft converted | ARTEC APC key figures: length 7.93 m [2]. English Wikipedia specifications table: length (hull) 7.93 m [10]. Dual-source for 7.93 m as a hull/family length. It is not the Bundeswehr 8.3 m cell. |
| Length, KNDS GTV page | 7.9 m and 8.01 m on the same page | 25.92 ft and 26.28 ft converted | Disagreement inside one KNDS page. BOXER GTV lists length 7.9 m and length 8.01 m [3]. Do not average. Do not treat either as the Bundeswehr 8.3 m figure. |
| Width, German GTF table | 3 m | 9.84 ft converted | Bundeswehr table "Breite Gruppentransportfahrzeug" 3 m [1]. Rounded official figure. |
| Width, manufacturer | 2.99 m | 9.81 ft converted | ARTEC APC 2.99 m [2]. KNDS GTV 2.99 m [3]. English Wikipedia hull width 2.99 m [10]. Three sources agree on 2.99 m. The Bundeswehr 3 m cell is the rounded GTF table value, printed separately. |
| Height, German GTF table | 3.4 m | 11.15 ft converted | Bundeswehr table "Höhe Gruppentransportfahrzeug" 3,4 m [1]. Measurement point not stated. |
| Height, hull roof | 2.38 m | 7.81 ft converted | ARTEC APC: height (hull roof) 2.38 m [2]. English Wikipedia: height (hull) 2.38 m [10]. Dual-source for hull height. This is not the GTF overall height. |
| Height, KNDS roof | 2.94 m | 9.65 ft converted | KNDS GTV: height (roof) 2.94 m [3]. single-source for that roof figure. It is not 3.4 m and it is not 2.38 m. |
| Combat / GVW, German table | 36.5 t | 80,469 lb converted | Bundeswehr "Gefechtsgewicht" 36,5 t [1]. KNDS GTV "Weight (class A/C) 36.5 t" [3]. English Wikipedia prose: combat weight of 36.5 tonnes in 2016 in A1 and A2 configurations, and a GVW column of 36.5 t [10]. Multi-source for 36.5 t as a class/combat figure. It is not a weighed German serial number with a tolerance. |
| Family maximum GVW | up to 38.5 t | 84,878 lb converted | ARTEC APC: max GVW up to 38.5 t [2]. English Wikipedia: A3 combat weight quoted as up to 38.5 tonnes, and a GVW cell of 38.5 t tactical / 41.0 t technical limit in one column [10]. This is a family limit, not the Bundeswehr GTF table weight. The base dossier's use of 38.5 t as Lance combat weight does not hold for the German GTF. |
| Empty / chassis mass | not the Bundeswehr table | English Wikipedia chassis column includes 24.0 t, 25.2 t, and 28.0 t | single-source: English Wikipedia specifications table [10]. The fetched Bundeswehr page does not state an empty weight. Do not present 25.2 t as the current German combat weight. |
| Ground clearance | 0.50 m | 1.64 ft converted | ARTEC APC 0.50 m [2]. German Wikipedia technical list: Bodenfreiheit 0,50 m [9]. Dual-source. Not on the Bundeswehr five-line table. |
| Grade / side slope / step / trench | 60%; 30%; 0.80 m; 2.0 m | step 2.62 ft; trench 6.56 ft converted | ARTEC APC: gradient 60%, slope 30%, step 0.80 m, trench 2.00 m [2]. German Wikipedia: Steigfähigkeit 60%, max Querneigung 30%, Kletterfähigkeit 0,80 m, Grabenüberschreitfähigkeit 2,0 m [9]. Dual-source for the family mobility set. |
| Protected volume | about 14 m3 on manufacturer APC/GTV pages. German Wikipedia 14–17.5 m3 | not converted | ARTEC APC protected volume 14 m3 [2]. KNDS GTV interior about 14 m3 [3]. German Wikipedia: Nutzvolumen unter Panzerschutz 14–17,5 m3 [9]. Think Defence: ambulance higher roof 17.5 m3 and floor-to-roof 1.85 m [11]. 1.85 m is single-source (Think Defence). |
| Crew, GTF | maximum 10 persons | same | Bundeswehr table: Besatzung maximal 10 Personen (Gruppentransportfahrzeug) [1]. KNDS GTV crew 3+7 [3]. ARTEC APC crew 3+8 is the family APC page, not the German seat count [2]. See section 2. |
| Glacis angle, lower plate angle, sponson overhang | not public | not public | Not on the Bundeswehr page or the fetched manufacturer tables. |
| Tire size code | not public for the German fit in the pages fetched | not public | Bundeswehr does not print a tire code [1]. The Think Defence variants page fetched here says Australian CRV vehicles use larger 27 inch Michelin XML tires [11]. That sentence is the Australian CRV, not a German GTK factory line. The base code 415/80 R685 was not on the fetched pages. |

### 2. RUNNING GEAR, HITCH OR TURRET, CREW

Real layout from the Bundeswehr page [1]:

- Eight wheels. Permanent all-wheel drive. Independent suspension (Einzelradaufhängung). Both front axles are steered, with hydraulic assist.
- Driver station: front right of the drive module. The driver hatch is part of that station. The fetched page says the driver sits vorn rechts. Road view is through front and side glass; the tactical view uses periscopes. From A2, a new driver-vision system is added [1]. German Wikipedia adds three periscopes for the driver, the center one replaceable by a night sight, and a camera system from A2 [9]. The "three periscopes" count is single-source (German Wikipedia). The right-hand driver seat is on the Bundeswehr page.
- Powerpack: front left. MTU 8V 199 TE20 turbodiesel, angle gearbox RRW3001, Allison automatic HD4800SP, cooling, air filter, and steering hydraulics [1]. Headlines on the same page: 530 kW/720 PS and 103 km/h [1].
- Transmission conflict, do not average: Bundeswehr names Allison HD4800SP [1]. The English Wikipedia specifications table says Allison HD4800SP with seven forward and three reverse gears through an RRW3001 [10]. A later prose paragraph on that same Wikipedia page says the powerpack was coupled to an Allison HD4070 [10]. Gear count 7 forward / 3 reverse is single-source (English Wikipedia). The Bundeswehr page names the transmission and does not state the gear count.
- Power conflict, do not average: Bundeswehr prints 530 kW/720 PS together for this vehicle [1]. KNDS GTV prints 530 kW and speed greater than 100 km/h [3]. ARTEC APC prints engine up to 600 kW (816 hp), MTU V8 199 TE20/21, and speed greater than 100 km/h [2]. English Wikipedia table: TE20 column 720 PS (530 kW); TE21 column 820 PS (600 kW) [10]. A Wikipedia prose sentence says the TE20 is now available at 530 kW (711 hp) or 600 kW (805 hp) [10]. The official German pairing remains 530 kW/720 PS. The 711 hp conversion is a Wikipedia sentence, not the Bundeswehr headline.
- Speed: 103 km/h on the Bundeswehr headline [1]. Greater than 100 km/h on ARTEC and on KNDS GTV [2][3]. Print both. 103 km/h is the German service headline. The ">100 km/h" lines are manufacturer family lines.
- Turning: Bundeswehr Wendekreis 21 m, reduced to about 16 m with the wheel-side brake [1]. German Wikipedia: Wendekreis 21 m (16 m with the side brake) [9]. English Wikipedia: turning radius 10.5 m with two steering axles, or 7.5 m with skid steer [10]. ARTEC APC: turning radius 7.50 m (skid steering) [2]. These are not the same words. 21 m and about 16 m are turning circles on the Bundeswehr page. 10.5 m and 7.5 m are radii on Wikipedia and ARTEC. Twice 10.5 m is 21 m, and twice 7.5 m is 15 m, which is near "about 16 m," but neither source states that equivalence. Do not merge them into one number.
- Suspension type that is multi-source: independent suspension on eight wheels [1][2][3]. KNDS GTV adds "long spring travel and hydraulic end stop damper" [3]. German Wikipedia says hydraulic shock absorbers and coil springs [9]. The Bundeswehr page does not choose coil versus hydropneumatic. No numeric wheel-station table is published. Wheelbase 1.55 + 1.90 + 1.55 m and track 2.58 m appear in the German Wikipedia technical list [9]. single-source (German Wikipedia). Not used as a station-offset table.
- Other German Wikipedia mobility figures, single-source unless noted: fording 1.20 m, deep wade 1.50 m without preparation [9]. Range is not on the Bundeswehr five-line table. ARTEC says range greater than 1,000 km [2]. That is a family APC figure.
- Turret: the introduced GTF and command vehicle use FLW 200, armed with a 12.7 mm heavy machine gun or a 40 mm grenade machine gun [1]. Not a 30 mm cannon. A1 raises the FLW 200 mount by 30 cm and adds CG-12 protection. A2 changes exhaust and cooling-air routing and adds the new driver-vision system [1].
- Seats, GTF, all from the Bundeswehr page [1]: maximum 10 persons. The base Gruppentransportfahrzeug has nine seats in the mission module and an FLW 200. In the rear of the mission module, four seats are on the left wall and three on the right. Those seven are the wall seats described. A reading that stays inside those sentences: seven dismount seats, plus commander and gunner, is nine in the module, plus the driver is ten. That reading is an interpretation of the Bundeswehr sentences, not an extra published count. German Wikipedia says the APC module has space for eight soldiers and that the Bundeswehr has a different configuration for seven soldiers [9]. KNDS prints 3+7 [3]. ARTEC prints 3+8 on the family APC page [2].
- Rear closure: a large rear hatch (Heckklappe) with an integrated door, opened and closed by electrically driven hydraulics, is the primary entrance [1]. Four paired roof hatches are emergency exits [1].
- Ambulance: the variant list says seven seated wounded or three lying [1]. A photo caption on the same page says space for two lying and three seated, or seven seated, or three lying, and one intensive-care patient [1]. A caption says the ambulance crew is three [1]. Print both casualty statements. They are the same official page and they are not identical.
- Command vehicle: extensive command and radio fit, FLW 200, A1 raise of 30 cm and CG-12 [1]. Internal seat count: not public beyond that description.
- Driver-training vehicle: listed [1]. Seat count of the training cab: not public on the Bundeswehr page. Think Defence says the shared German/Dutch training module has an instructor and two passenger seats [11]. single-source for that seat description.

No hitch in the artillery sense. No invented axle XYZ.

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

Parts named on the Bundeswehr page for the fielded GTF [1]. Angles and travels are not public unless a source states them. FLW numbers below are the KNDS FLW 200 product sheet, single-source, and are the station's published range, not a measurement of a German serial vehicle [4].

```
GTK_Boxer_GTF
|-- Drive_module_8x8
|   |-- Powerpack_front_left (MTU 8V 199 TE20, RRW3001, Allison HD4800SP)
|   |-- Driver_station_front_right
|   |   |-- Driver hatch, lift: not public (page says electrically lifted)
|   |-- Steered axle 1, travel: not public
|   |-- Steered axle 2, travel: not public
|   |-- Axle 3, not described as steered, travel: not public
|   |-- Axle 4, not described as steered, travel: not public
|-- Mission_module_GTF
|   |-- Rear hatch with integrated door, hydraulic, electrically driven, travel: not public
|   |-- Four left wall seats and three right wall seats
|   |-- Four paired roof hatches, emergency exit, travel: not public
|   |-- Commander hatch, left of the FLW 200, five periscopes, folding weather shield
|   |-- FLW_200
|       |-- Traverse: n x 360 deg (KNDS product sheet, single-source)
|       |-- Elevation: -15 to +70 deg with sMG .50; -12 to +60 deg with GMW 40 mm (KNDS, single-source)
|       |-- Lateral speed up to 60 deg/s; vertical speed up to 30 deg/s (KNDS, single-source)
|       |-- LAZ 400 (L): CCD color camera, thermal imager, laser rangefinder (Bundeswehr)
```

KNDS also prints FLW 200 rotation radius 996 mm with the .50 and 580 mm with the 40 mm GMW, total height about 750 mm, and carriage weight about 185 kg without weapon and ammunition [4]. single-source. Ammunition on that sheet: 7.62 mm 250/480 rounds, .50 100 rounds, 40 mm 32 rounds [4]. The Bundeswehr page does not publish those counts for the installed German fit. Bundeswehr weapons actually named for the GTF and command vehicle are 12.7 mm or 40 mm [1].

Do not put a Lance turret, a Spike pod, a 30 mm cannon, or an APS array on this tree.

### 4. SENSOR SITING OR DECK INTERFACE

This is a land vehicle. There is no flight-deck interface.

Sights and weapons that the sourced German GTF and command fit actually have [1]:

- FLW 200 on the GTF and on the command vehicle. Weapons: 12.7 mm heavy machine gun or 40 mm grenade machine gun.
- Sensor head LAZ 400 (L) on the FLW 200: CCD color camera, thermal imager, laser rangefinder. Day, night, and poor visibility [1].
- Commander hatch to the left of the FLW 200, with five periscopes and a folding weather shield [1].
- Rear-view system: a digital color camera and an analog black-and-white camera, images on displays inside the vehicle [1].
- Driver: periscopes for the tactical view, front and side glass for the road view. A2 adds a new driver-vision system [1].

Not on the fielded GTK as described by the Bundeswehr page:

- No Lance 30 mm turret.
- No APS. ARTEC lists APS, laser warning, ECM, 360-degree situational awareness, and ATGM under exemplary options on the family APC page [2]. Those options are not a German standard-fit statement.
- Smoke launchers: German Wikipedia photo captions call a Nebelmittelwurfanlage the secondary armament of a pictured Bundeswehr GTK [9]. The fetched Bundeswehr text does not say the GTF is fitted with smoke launchers. Treat the smoke fit as single-source (German Wikipedia captions), not as a bundeswehr.de specification.
- FLW elevation limits are the KNDS product sheet [4], not a Bundeswehr installed-angle table.

### 5. DIFFERENCES FROM THE BASE DOSSIER

**Holds, re-verified**

- The vehicle is an 8x8 wheeled drive module plus a mission module [1][2]. The base file `boxer-ifv--171.md` is right that the family vehicle is wheeled and is not a tracked vehicle with sprockets and return rollers.
- Family hull length 7.93 m and width 2.99 m are on the ARTEC APC page [2] and, for the hull, on English Wikipedia [10]. KNDS also prints width 2.99 m [3].
- Hull-roof height 2.38 m is on ARTEC [2] and English Wikipedia [10].
- Ground clearance 0.50 m is on ARTEC [2] and German Wikipedia [9].
- Grade 60%, side slope 30%, step 0.80 m, and trench 2.0 m are on ARTEC [2] and German Wikipedia [9].
- Independent suspension is real [1][3].
- MTU 8V 199 TE20 at the German headline 530 kW/720 PS, with Allison HD4800SP and RRW3001, is on the Bundeswehr page [1].
- A remote weapon station, not a cannon, is the introduced German GTF and command fit [1].

**Base claim does not hold for the German GTK fit**

- `boxer-ifv--93.md` says the DEU GTK Boxer is a tracked vehicle with a drive sprocket, rear idler, return rollers, and oscillating roadwheels. Corrected: the Bundeswehr GTK is an 8x8 [1]. That tracked description does not hold.
- `boxer-ifv--93.md` combat weight 45.0 t, gun-related length 8.230 m, turret-roof height 3.240 m, glacis 22 deg, and an APS fit. Corrected for the German GTF table: combat weight 36.5 t, length 8.3 m, height 3.4 m, width 3 m [1]. Glacis angle is not public. APS is not on the Bundeswehr page.
- `boxer-ifv--171.md` is an ARTEC Lance 30 mm blueprint: gun-forward 8.85 m, turret-roof height 3.24 m, combat weight 38.5 t, glacis 15 deg, tire 415/80 R685, steer plus or minus 30 deg, and wheel stations at X plus or minus 1.250 with invented Z values. Corrected: the introduced German versions are GTF, command, ambulance, and driver training with FLW 200 on the GTF and command vehicle [1]. 8.85 m, 3.24 m, glacis 15 deg, the tire code, the steer angle, and the XYZ table were not re-verified and are not the German GTF. 38.5 t is the ARTEC family maximum GVW [2], not the Bundeswehr Gefechtsgewicht of 36.5 t [1].
- `boxer-ifv--172.md` treats a "Nato Boxer Ifv Master" as tracked, with six roadwheels, width 3.3 m, hull 7.5 m, height 3.2 m, and combat weight 45 t. Those figures do not hold for the wheeled German GTK.
- Lance, Spike, StrikeShield APS, and CITV as the German fit: does not hold for the introduced GTK. The Lance vehicle in German service is the separate Schwerer Waffenträger Infanterie program: Rheinmetall, 3 May 2024, 123 vehicles, Boxer 8x8 with a manned Lance turret and MK30-2/ABM, based on the Australian CRV, series delivery from 2025, production mainly at Redbank [7]. The Schakal is a further, later IFV: OCCAR states that 2025 contracts bring 48 additional vehicles for Germany and develop and produce 222 Schakal IFVs for Germany and the Netherlands [5]. Neither program is the 01.02.2023 GTF.
- Invented wheel-station XYZ in the base files: not public. German Wikipedia's wheelbase sum and track are a single Wikipedia list [9], not a pivot table, and they are not copied forward as coordinates.

### 6. GAME DATA CHECK

Searched `C:\cnc_rev\data\rules\unit-dimensions.json` and `C:\cnc_rev\data\roster\jslc.json` for boxer and gtk.

- `jslc.json`: no match [13].
- `unit-dimensions.json`: no GTK or Boxer vehicle row. The only Boxer hits are USS Boxer (LHD-4) ship text inside Wasp-class source strings [13].

`boxer-ifv--288.md` is a mesh audit of a game file, not a rules row and not a factory sheet. It records bounding width 3.34 m, bounding height 3.33 m, bounding length 7.93 m, ground contact Y = 0, and 347,850 triangles [12]. The 7.93 m length matches the ARTEC/Wikipedia hull length [2][10]. The 3.34 m width matches neither the manufacturer 2.99 m [2][3] nor the Bundeswehr 3 m table [1]. The 3.33 m height is close to the Bundeswehr 3.4 m only as a rough mesh bound. It is not a second source for 3.4 m.

### 7. MASTER AI VIDEO PROMPT PACKAGE

1. Daylight side view of a Bundeswehr GTK Boxer Gruppentransportfahrzeug, 8x8, driver on the right, powerpack bay on the left, FLW 200 on the roof with either a 12.7 mm machine gun or a 40 mm grenade launcher. No Lance turret and no cannon.

2. Rear three-quarter, ramp-style rear hatch with a personnel door opening on electric-hydraulic power, infantry seats visible, four paired roof hatches closed. No invented station callouts.

3. Interior gunner view of the FLW 200 display: color camera, thermal image, and a laser-rangefinder readout. The commander hatch is to the left of the weapon station. Angles are not printed on screen.

4. Separate shot, clearly labeled as a different vehicle: a Boxer with a manned Lance turret, the Schwerer Waffenträger, not the GTK troop carrier. Do not mix the two in one livery caption.

### 8. SOURCES

1. Bundeswehr, "Ausrüstung und Technik: GTK Boxer," page dated 01.02.2023. https://www.bundeswehr.de/de/ausruestung-technik-bundeswehr/landsysteme-bundeswehr/gtk-boxer — Variants, driver right, powerpack left, MTU 8V 199 TE20, RRW3001, Allison HD4800SP, 530 kW/720 PS, 103 km/h, turning circle 21 m and about 16 m, FLW 200, LAZ 400 (L), seats, rear hatch, A1/A2 notes. Technical table: length 8.3 m, height 3.4 m, width 3 m, combat weight 36.5 t, crew max 10 for the GTF. The length cell was confirmed on a second read of the same URL after the first markdown render dropped it.
2. ARTEC, "Armoured Personnel Carrier." https://www.artec-boxer.com/vehicles/armoured-personnel-carrier/ — Family APC key figures: 7.93 m, 2.99 m, hull roof 2.38 m, clearance 0.50 m, max GVW up to 38.5 t, crew 3+8, skid-steer radius 7.50 m, gradient 60%, slope 30%, trench 2.00 m, step 0.80 m, protected volume 14 m3, speed greater than 100 km/h, engine up to 600 kW, range greater than 1,000 km. APS listed under exemplary options.
3. KNDS, "BOXER GTV." https://knds.com/en/products/systems/boxer/boxer-gtv — Length printed as both 7.9 m and 8.01 m, width 2.99 m, height (roof) 2.94 m, weight class A/C 36.5 t, power 530 kW, speed greater than 100 km/h, crew 3+7, interior about 14 m3, remote station for 7.62 mm, 12.7 mm, or 40 mm, independent suspension with hydraulic end-stop damper.
4. KNDS, "FLW 200." https://knds.com/en/products/systems/flw-200-range/flw-200 — Station product sheet: traverse n x 360 deg, elevation -15 to +70 deg (.50) and -12 to +60 deg (40 mm), laying speeds, carriage about 185 kg, height about 750 mm, ammunition counts. Not a Bundeswehr installed-fit table.
5. OCCAR, "Boxer - A multi-role armoured vehicle, General information." https://occar.int/our-work/programmes/boxer-a-multi-role-armoured-vehicle/general-information — Drive module plus mission module. First series contract December 2006 for Germany and the Netherlands. Further German batch 2015. All 605 German and Dutch vehicles in nine variants delivered and in retrofit. 2025 contracts: 48 additional vehicles for Germany and 222 Schakal IFVs for Germany and the Netherlands.
6. Rheinmetall press release, 23 June 2021, "Lieferung der bisher durch die Bundeswehr beauftragten GTK Boxer abgeschlossen." https://www.rheinmetall.com/de/media/news-watch/news/2021/2021-06-23_lieferung-der-bisher-durch-die-bundeswehr-beauftragten-gtk-boxer-abgeschlossen — Second batch December 2015, 131 GTK Boxer, 478 million euro, A2. Total delivered stated as 405, of which 72 ambulance, 65 command, and 256 infantry group vehicles. Those three categories add to 393. The release does not name the other 12. A2 upgrade of the command fleet contracted February 2021, all 65 command vehicles at the latest standard from 2024.
7. Rheinmetall press release, 3 May 2024, "Schwerer Waffenträger Infanterie für die Bundeswehr." https://www.rheinmetall.com/de/media/news-watch/news/2024/05/2024-05-03-schwerer-waffentraeger-infanterie-fuer-die-bundeswehr-nachweismuster-vorgestellt — 123 vehicles, Lance turret, MK30-2/ABM, Australian CRV basis. Not the GTK GTF.
8. Army Technology, "ARTEC completes delivery of GTK Boxer vehicles to Bundeswehr," 24 June 2021. https://www.army-technology.com/news/artec-gtk-boxer-vehicles-bundeswehr/ — Repeats the Rheinmetall 405 / 72 / 65 / 256 handover. Not an independent count.
9. German Wikipedia, "GTK Boxer." https://de.wikipedia.org/wiki/GTK_Boxer — Technical list: clearance 0.50 m, track 2.58 m, wheelbase 1.55+1.90+1.55 m, fording 1.20 m, deep wade 1.50 m, 60%, 30%, step 0.80 m, trench 2.0 m, turning circle 21 m (16 m with side brake), protected volume 14–17.5 m3. APC module space for eight; Bundeswehr configuration for seven. Photo captions show a smoke launcher on a Bundeswehr vehicle. Wheelbase, track, fording, and the smoke caption are single-source here.
10. English Wikipedia, "Boxer (armoured fighting vehicle)." https://en.wikipedia.org/wiki/Boxer_(armoured_fighting_vehicle) — Hull 7.93 m, hull height 2.38 m, width 2.99 m. GVW columns include 36.5 t and 38.5 t. Transmission table HD4800SP, seven forward and three reverse, via RRW3001. Prose paragraph says Allison HD4070. Turning radius 10.5 m or 7.5 m skid steer. TE20 720 PS (530 kW) in the table. Prose also converts 530 kW to 711 hp. GTK named as the official Bundeswehr designation. Original German order 125/65/72/12 is marked citation-needed on the page and is not used as a count.
11. Think Defence, "Boxer (Variants)," last updated 12 October 2026. https://www.thinkdefence.co.uk/docs/boxer-variants/ — German GTF described with KMW FLW-200 in 12.7 mm, 7.62 mm, or 40 mm. Ambulance higher roof 17.5 m3 and floor-to-roof 1.85 m (1.85 m is single-source). States the introduced German set as APC, command, ambulance, and driver training, and treats Lance and Schakal as separate planned vehicles. The 27 inch Michelin line on this page is the Australian CRV.
12. Local base files under audit: `C:\Users\MAXGLA~1\AppData\Local\Temp\grok-dr-bases\boxer-ifv--171.md`, `boxer-ifv--93.md`, `boxer-ifv--172.md`, and `boxer-ifv--288.md`. Claims checked in section 5 and section 6. Not measurement sources.
13. `C:\cnc_rev\data\rules\unit-dimensions.json` and `C:\cnc_rev\data\roster\jslc.json` — No GTK or Boxer vehicle row. USS Boxer LHD-4 appears only as ship text. `jslc.json` has no boxer or gtk match.
