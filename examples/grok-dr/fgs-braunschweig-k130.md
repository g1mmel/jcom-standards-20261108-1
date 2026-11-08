---
generated_at: "2026-10-14T15:32:42-04:00"
generator: "dolphin2/dossier-grok-dr"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "xai"
models:
  - "grok-4.7"
query: "German Navy K130 Braunschweig-class public dimensions and fit, separated from the Sa'ar 6 base"
sources_count: 8
asset_id: "fgs-braunschweig-k130"
title: "Naval Architectural Blueprint Dossier: German Navy K130 Braunschweig-Class Corvette (FGS Braunschweig)"
base_asset_id: "saar-6-corvette"
---

# Naval Architectural Blueprint Dossier: German Navy K130 Braunschweig-Class Corvette (FGS Braunschweig)

**Classification:** Open-source architectural reference for the German Navy K130 Braunschweig class, lead ship FGS Braunschweig (F260). The named base is the Israeli Navy Sa'ar 6 (INS Magen). That is a different navy and a different hull. Israeli weapons and the base dossier's modelled body plan are not carried onto this ship.

**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

Wikipedia describes the Sa'ar 6 as loosely based on the Braunschweig class, and Naval Technology describes the Sa'ar 6 as based on the MEKO 100 [6][7]. That design remark is not a shared lines plan and is not a shared weapon fit. Station tables and pivot coordinates in the Sa'ar 6 base are modelled. They are not repeated.

### 1. MASTER COORDINATE DATUM & DIMENSIONS

glTF convention used here: bow = -Z, up = +Y, starboard = +X, port = -X, design waterline Y = 0. Two public draft sentences exist, and they disagree. Neither sentence is labelled design draft, navigational draft, or full-load draft beyond the Bundeswehr wording "maximaler Tiefgang". Keel Y is therefore not set to one negative number.

| Parameter | Metric | Imperial | Engineering notes |
| --- | --- | --- | --- |
| Length overall | 89.1 m; also 89.12 m; also about 88 m | 292 ft 5 in is Wikipedia's figure printed with 89.12 m [4]. The Bundeswehr page does not print an imperial length. | Do not average. Bundeswehr equipment page, Maße cell confirmed on the page text: 89.1 m Länge über alles [1]. Wikipedia infobox: 89.12 m [4]. Naval Technology specification box: 89.12 m [3]. The same Naval Technology page's body text says about 88 m [3]. The base dossier's 90.000 m is a Sa'ar 6 figure, not a K130 figure. |
| Waterline length | 82.8 m | not published | Single-source: Naval Technology specification box [3]. The same page's body does not repeat it. This is not a length between perpendiculars. |
| Length between perpendiculars | not public | not public | No fetched page states an LBP. The base value 84.5 m is the Sa'ar 6 dossier's modelled figure and was not found for either ship. |
| Moulded / maximum beam | 13.3 m; also 13.28 m; also 13.2 m | 43 ft 7 in is Wikipedia's figure printed with 13.28 m [4]. The Bundeswehr page does not print an imperial beam. | Do not average. Bundeswehr: 13.3 m Breite [1]. Wikipedia: 13.28 m [4]. Naval Technology specification box: 13.28 m [3]. Naval Technology body: 13.2 m [3]. |
| Waterline breadth | 12.44 m | not published | Single-source: Naval Technology specification box [3]. The base value 12.1 m was not found for the K130. |
| Draft | 3.4 m; also 4.5 m | 11 ft 2 in is Wikipedia's figure printed with 3.4 m [4]. No imperial figure was published with the 4.5 m sentence. | Do not average and do not pick a keel Y. Bundeswehr Maße cell: 3.4 m Tiefgang, and the same page says 3.4 m maximaler Tiefgang [1]. Wikipedia: 3.4 m [4]. Naval Technology specification box lists depth at the waterline as 3.4 m [3]. A second Bundeswehr article, on the corvettes at BALTOPS 2024, says the draft is only four and a half metres ("nur viereinhalb Meter Tiefgang") [2]. Load condition beyond "maximaler" is not stated. |
| Hull height | 4.8 m | not published | Single-source: Naval Technology specification box, hull height [3]. This is not an air draft. |
| Air draft to masthead | not public | not public | No fetched K130 page states a masthead air draft. The base value +28.500 m to a TACAN apex is a Sa'ar 6 dossier figure and was not found. Naval Technology's Sa'ar 6 page prints a height of 21.5 m for that other class [6]. That 21.5 m is not used as a K130 air draft. |
| Displacement | 1,800 t; also 1,840 t; also about 1,580 t | 1,810 long tons is Wikipedia's figure printed with 1,840 t [4]. The Bundeswehr page does not print long tons. | Do not average. Bundeswehr: 1,800 t Verdrängung [1]. The BALTOPS article calls Magdeburg, a sister, a 1,800-tonne corvette [2]. That is the same publisher, not a second publisher. Wikipedia: 1,840 t [4]. Naval Technology specification box: full load 1,840 t [3]. Naval Technology body: about 1,580 t [3]. The base "~1,900 t" is a Sa'ar 6 figure. |

F260 is the lead ship. The Bundeswehr page dates her commission 16 April 2008 [1]. Naval Technology says Blohm+Voss, launched April 2006, commissioned April 2008 at Warnemünde [3]. The exact day is the Bundeswehr sentence. The builder name on the pages used here is Naval Technology. The BALTOPS article places 1. Korvettengeschwader at Rostock-Warnemünde [2]. A home port of Wilhelmshaven was not taken from the search extract of the ship page.

Station offsets are not public.

### 2. GENERAL ARRANGEMENT AND ARMAMENT

F260 is a German Navy missile corvette. The public machinery is two diesel engines and two propellers, with a bow thruster [1][4]. It is not a gas-turbine ship. The Bundeswehr page gives two diesels at 14,800 kW (20,100 PS) and does not print the engine model or the word CODAD [1]. Naval Technology and Wikipedia name two MTU 20V 1163 TB 93 diesels at 7.4 MW each, which is the same 14.8 MW total, and both describe controllable-pitch propellers [3][4]. The BALTOPS article also says the corvettes have a controllable-pitch propeller ("verstellbarer Antriebspropeller") and a bow thruster [2]. Four generator sets of 550 kW, named by Wikipedia as MTU 12V 1600 DS550, appear on that page only [4].

The gun and missile fit below is the K130 fit. Barak, C-Dome, Gabriel, and MF-STAR are Sa'ar 6 systems and are absent from the Bundeswehr K130 list [1]. No numeric body plan is available. Station offsets are not public.

| Item | Public fit | Notes |
| --- | --- | --- |
| Gun | 1 x 76 mm. Bundeswehr: 76 mm Compact. Naval Technology: Oto Melara 76 mm Super Rapid | Both wordings are printed [1][3]. Bundeswehr range greater than 18 km is single-source [1]. Naval Technology's 120 rounds per minute is single-source [3]. Elevation, train, and recoil: not public. |
| 27 mm | 2 x 27 mm | Bundeswehr: two MLG [1]. Wikipedia: two Mauser BK-27 [4]. Train and elevation: not public. |
| 12.7 mm | 4 mounts | Single-source: Bundeswehr [1]. |
| Anti-ship missiles | Two RBS15 Mk3 starters; also four RBS15 Mk3 missiles | Bundeswehr counts two starters [1]. Naval Technology and Wikipedia count four RBS15 Mk3 missiles [3][4]. Both can describe two twin starters. They are not collapsed into one number. BALTOPS: range more than 200 km and a warhead of more than 200 kg, single-article Bundeswehr wording [2]. |
| RAM | Two RIM-116 starters; 21 missiles or cells also stated | Bundeswehr: two starters [1]. Wikipedia: two RAM Block II launchers, 21 each [4]. Naval Technology states 21 cells [3]. "21" is not on the Bundeswehr equipment page. Range: Naval Technology 9.5 km [3]; BALTOPS "within ten kilometres" [2]. Not averaged. |
| Mines | 4 rails; also 2 racks of 34 Mk 12 | Bundeswehr: four mine rails [1]. Wikipedia: two mine racks of 34 naval mines Mk 12 [4]. Not averaged. |
| Decoys | 2 x MASS | Bundeswehr and Wikipedia [1][4]. |
| Radar | TRS-3D on the first batch, including F260 | Bundeswehr names TRS-3D and, as single-source performance, more than 200 km and more than 750 tracks [1]. Wikipedia: TRS-3D on batch 1 and TRS-4D on batch 2 [4]. F260 is batch 1. |
| Navigation radars | 2 | Bundeswehr and Wikipedia [1][4]. The Pathfinder ST Mk2 name is single-source Naval Technology [3]. |
| Electro-optics | 2 x Mirador | Count of two is Bundeswehr [1]. The Mirador name is also on Naval Technology and Wikipedia [3][4]. Coordinates: not public. |
| ESM | UL 5000 K; Naval Technology uses other strings | Bundeswehr and Wikipedia: UL 5000 K [1][4]. Naval Technology prints EADS SPS-N 5000 and KJS 5000 [3]. Those names are not merged. |
| Other Wikipedia-only sensors | MSSR 2000 i; Link 11 and Link 16 | Single-source Wikipedia [4]. |
| Aviation | Flight deck, and a hangar described for two drones | Wikipedia class page: helicopter pad, hangar for two drones [4]. Bundeswehr discusses helicopter drones [1]. BALTOPS records an MH-60R landing on Magdeburg's flight deck to refuel [2]. The Braunschweig ship-page search extract says the hangar is too small for Sea King, Lynx, or NH90, that the pad is large enough for a helicopter, and that two Skeldar are carried [5]. That page was not fully fetched. An SH-60 hangar is the Sa'ar 6 description [6] and is not used here. |
| Propulsion | Two diesels, 14,800 kW total; two propellers; bow thruster | Power is Bundeswehr [1] and matches 2 x 7.4 MW on Naval Technology and Wikipedia [3][4]. Engine model MTU 20V 1163 TB 93 is Naval Technology and Wikipedia [3][4]. Controllable pitch is Naval Technology, Wikipedia, and the BALTOPS article [2][3][4]. No gas turbine is listed. |
| Crew | 61; also 65; also 50 | Bundeswehr Stammbesatzung 61 [1]. BALTOPS says crews of more than 60 [2]. Wikipedia complement 65 [4]. Naval Technology specification and body both say 50 [3]. Not averaged. |
| Speed | more than 26 knots; also 26 knots; also over 26 knots | Bundeswehr: more than 26 knots [1]. Wikipedia: 26 knots [4]. Naval Technology specification: 26 knots, and the body says over 26 knots [3]. Not averaged. |
| Range | over 2,500 nautical miles; also 4,000 nmi at 15 knots | Naval Technology: over 2,500 nm [3]. Wikipedia: 4,000 nmi at 15 knots [4]. Not averaged. |
| Endurance | 7 days, or 21 days with a tender | Naval Technology and Wikipedia [3][4]. |

The Bundeswehr weapons and sensors list used here does not include a hull sonar or torpedo tubes [1].

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

Text tree of equipment the K130 sources name. Motion is in words. No pivot XYZ is stated.

- Hull, design waterline Y = 0. Keel Y: not public, because the 3.4 m and 4.5 m draft sentences disagree and neither is a stated design-waterline draft [1][2].
  - Machinery. Two diesel engines [1]. Model name, where stated: MTU 20V 1163 TB 93 [3][4]. Two shafts, two propellers [1]. Controllable pitch [2][3][4]. Pitch travel: not public. Bow thruster [1][2]. Rudders are implied by a steered ship; rudder angle: not public. Generator sets of 4 x 550 kW are single-source Wikipedia [4].
  - 76 mm gun, one mount [1][3]. Train, elevation, and recoil: not public.
  - Two 27 mm MLG [1]. Train and elevation: not public.
  - Four 12.7 mm mounts, single-source [1]. Travel: not public.
  - Two RBS15 Mk3 starters [1]. Missile count also stated as four [3][4]. Launcher elevation: not public.
  - Two RAM starters [1]. Cell or missile count 21 is Wikipedia and Naval Technology, not the Bundeswehr equipment sentence [3][4]. Hatch travel: not public.
  - Mine rails. Bundeswehr counts four rails [1]. Wikipedia counts two racks [4]. Deploy travel: not public.
  - Two MASS launchers [1][4]. Train: not public.
  - TRS-3D [1]. Rotation or array motion: not public. Two navigation radars [1][4]. Rotation rate: not public. Two Mirador directors [1]. Train and elevation: not public.
  - Flight deck and hangar. The hangar is described for drones [4][5]. Door travel: not public. A manned helicopter has used a sister ship's deck to refuel [2].

### 4. SENSOR SITING

Coordinates are not public.

The Bundeswehr equipment page names TRS-3D, two Mirador directors, two navigation radars, and UL 5000 K, and it does not publish deck coordinates or a mast height [1]. A Bundeswehr caption describes X-form sides [1]. That is a topside description, not a station.

The 76 mm, the two 27 mm mounts, the 12.7 mm mounts, the two RBS15 starters, and the two RAM starters are named without a published bow, mast, or hangar-roof coordinate [1]. Placing them on a Sa'ar 6 mast or hangar roof would copy the other ship.

Wikipedia adds MSSR 2000 i and Link 11/16 without coordinates [4]. Naval Technology's Pathfinder, SPS-N 5000, and KJS 5000 strings likewise have no coordinates on the page used here [3].

### 5. DIFFERENCES FROM THE BASE DOSSIER

The base file is the INS Magen blueprint. Its 11-station table is captioned as representative for 3D modelling. None of those station offsets, half-breadths, or pivot coordinates are public drawings for the Sa'ar 6 or for the K130, and none are copied.

Navy and identity:

- Base: Israeli Navy Sa'ar 6, INS Magen. Corrected claim for this asset: German Navy K130, FGS Braunschweig, F260, commissioned 16 April 2008 on the Bundeswehr page [1].

Hull and dimensions:

- Base: LOA 90.000 m. Corrected claim for F260: 89.1 m [1], also 89.12 m [3][4], and the Naval Technology body also says about 88 m [3]. Separately, the current Naval Technology Sa'ar 6 page does print overall length 90 m [6], and Wikipedia prints 90 m (295 ft 3 in) for the Sa'ar 6 [7]. A search snippet of the blocked TKMS handover article says length overall about 90 m [8]. The millimetre form 90.000 m was not found. A 91.4 m Sa'ar 6 length was not on the Naval Technology page fetched for this check [6] and was not found in a second source. The local Sa'ar 6 knowledge pack was not opened; it is larger than the 20 KB limit set for this task.
- Base: LBP 84.500 m. Corrected claim: not public for the K130. It was also not found on the Sa'ar 6 pages fetched [6][7].
- Base: maximum beam 13.200 m. Corrected claim for F260: 13.3 m [1], also 13.28 m [3][4], and the Naval Technology body also says 13.2 m [3]. For the Sa'ar 6 itself, Naval Technology prints maximum beam 13.2 m [6] and the TKMS search snippet prints beam 13 m [8]. Wikipedia's Sa'ar 6 infobox does not state beam [7].
- Base: waterline beam 12.100 m. Corrected claim: not found for the Sa'ar 6. The only waterline breadth found for the K130 is Naval Technology's single-source 12.44 m [3].
- Base: design draft 3.400 m and keel Y = -3.400 m. Corrected claim: the K130 pages print 3.4 m and, in another Bundeswehr article, 4.5 m [1][2][4]. Neither is adopted as design draft, so keel Y is not public. The Sa'ar 6 pages fetched do not state a 3.4 m draft [6][7].
- Base: masthead air draft +28.500 m to a TACAN apex. Corrected claim: K130 air draft is not public. The Sa'ar 6 pages fetched do not state 28.5 m. Naval Technology prints a Sa'ar 6 height of 21.5 m [6], which is a different number and a different ship.
- Base: full load displacement about 1,900 t. Corrected claim for F260: 1,800 t [1], also 1,840 t [3][4], and the Naval Technology body also says about 1,580 t [3]. For the Sa'ar 6, Naval Technology says approximately 2,000 t [6], Wikipedia says 1,900 long tons full load [7], and the TKMS snippet says full load approximately 1,900 t [8]. Those Sa'ar figures stay on the Sa'ar 6.
- Base: stem rake 65 degrees, deadrise 12 degrees amidships and 25 degrees forward, tumblehome 11 to 14 degrees, and knuckle heights. Corrected claim: not public for either ship on the pages used here. The Bundeswehr caption's X-form sides are a qualitative description [1].

Weapons, sensors, and aviation. These base items do not transfer:

- Base: 76 mm with elevation from -15 degrees to +85 degrees and a named recoil stroke. Corrected claim: F260 has a 76 mm gun, identified as Compact by the Bundeswehr and as Super Rapid by Naval Technology [1][3]. Elevation and recoil are not public.
- Base: two Typhoon 25 mm mounts. Corrected claim: the Bundeswehr K130 list has two 27 mm MLG and four 12.7 mm mounts [1]. Typhoon is not on that list. Sa'ar 6 sources themselves disagree on the Typhoon calibre (the base says 25 mm; Naval Technology's Sa'ar 6 page says two Typhoon 30 mm [6]) and that disagreement is left on the Sa'ar 6.
- Base: 32 Barak MX cells. Corrected claim: no Barak on the K130 list [1]. Sa'ar 6 cell counts are unstable even among Sa'ar sources: the base says 32, Wikipedia's infobox says 16 Barak MX cells, and Naval Technology says 40 Barak 8 [6][7]. None of those counts is applied here.
- Base: 40 C-Dome cells. Corrected claim: no C-Dome on the K130 list [1]. The K130 point-defence system in the sources is RAM, two starters [1], with 21 missiles or cells stated by Wikipedia and Naval Technology [3][4].
- Base: Gabriel V, eight missiles per side in quad racks fixed 45 degrees off the centreline. Corrected claim: no Gabriel on the K130 list [1]. The K130 anti-ship weapon is RBS15 Mk3, two starters [1] or four missiles [3][4]. Sa'ar 6 sources also disagree among themselves: Wikipedia's infobox says 8 Gabriel V and its prose says up to 16, while Naval Technology lists Gabriel, Harpoon, or RBS-15 as options [6][7]. That disagreement is not resolved by copying any of them onto F260.
- Base: EL/M-2248 MF-STAR with four fixed arrays tilted about 15 degrees, plus a TACAN apex. Corrected claim: F260's primary radar in the batch-1 sources is TRS-3D [1][4]. MF-STAR and a TACAN apex were not found for the K130. Array tilt: not public.
- Base: electro-optical directors at stated Y and Z, and bilateral SATCOM sponsons. Corrected claim: two Mirador are named, with no coordinates [1]. SATCOM coordinates: not public.
- Base: hangar arranged for the aviation fit of that dossier, and the video prompt's SH-60-class reading is the Sa'ar 6 hangar on Naval Technology [6]. Corrected claim: the K130 hangar is described for two drones [4], the ship-page extract says it will not take Sea King, Lynx, or NH90 [5], and a manned helicopter on a K130 deck is documented as a refuelling landing on Magdeburg [2].
- Base video prompt: twin controllable-pitch propellers, and flight-deck paint #00FF00. Corrected claim on propellers: controllable pitch does hold for the K130, on Naval Technology, Wikipedia, and the BALTOPS wording [2][3][4], with two propellers on the Bundeswehr page [1]. Blade count and pitch angle: not public. The green circle #00FF00 was not found as a German Navy flight-deck specification.
- Base: rudders limited to plus or minus 35 degrees. Corrected claim: rudder angle is not public.
- Base crew is not stated in the dimension block. Sa'ar 6 public crew on the pages fetched is up to 70 [6][7]. K130 crew figures are 61, 65, and 50, as in section 2 [1][3][4].

What is in the same broad class of machinery, and still not a copied hull: both ships are published with two diesel-driven shafts and controllable-pitch propellers [2][3][6]. The K130 model, where named, is the MTU 20V 1163 TB 93 at 7.4 MW each [3][4]. The Sa'ar 6 page says two MTU diesels in a CODAD plant and does not print that K130 model in the text used here [6]. Speed sentences for both ships sit at 26 knots or more than 26 knots, which is a similar band and not a shared measured trial [1][3][6].

### 6. GAME DATA CHECK

no unit-dimensions row

no roster row

Searches of `C:\cnc_rev\data\rules\unit-dimensions.json` and `C:\cnc_rev\data\roster\jslc.json` for braunschweig and k130 found no row.

A Sa'ar 6 row does exist and is not a K130 row. `jslc.vehicle.saar-6-corvette` and `coalition.vehicle.saar-6-corvette` store lengthM 90, widthM 13, heightM 28. The source text on that row says mast height 28 m is representative. The roster entry `jslc.vehicle.saar-6-corvette` lists mk32-svtt-mk54, oto-melara-76-62-super-rapid, barak-8-vls, cdome-tamir-vls, gabriel-v-anti-ship-missile, and typhoon-25mm-spike-er. Those weapons are the Israeli game fit. They are not the K130 fit in section 2. The 90 m and 13 m figures are in the Sa'ar 6 band (90 m published; beam 13 m in the TKMS snippet and 13.2 m on Naval Technology [6][8]). Height 28 m is the game row's representative value. It is not Naval Technology's 21.5 m Sa'ar 6 height [6] and it is not the base dossier's 28.5 m. It is not a K130 air draft.

### 7. MASTER AI VIDEO PROMPT PACKAGE

1. Technical fly-around of a German Navy K130 corvette, pennant F260, grey topsides with an X-form section, bow gun, a mast, and a flight deck aft. Blueprint linework, bow to the near lower corner, mast up, starboard to the right. No dimension callouts and no Israeli missile arrays.

2. Close view of the single 76 mm turret training on the foredeck. Keep elevation numbers off the picture. Grey angular surfaces, overcast light. No vertical-launch battery of the Sa'ar 6 type.

3. The same corvette in a short Baltic sea, wake from two propellers, diesel exhaust only. No gas-turbine uptake and no numeric draft painted on the hull.

4. Flight deck aft, hangar door open on a small drone bay, deck-edge lights on. A helicopter may sit in a hover off the deck as a visiting aircraft. No green landing circle and no specific paint formula.

### 8. SOURCES

1. Bundeswehr, "Korvette K130", equipment page dated 05.11.2019 on the page used, https://www.bundeswehr.de/de/ausruestung-technik-bundeswehr/seesysteme-bundeswehr/korvette-k130 . The Maße line was recovered from the page text after a fetch dropped that cell: 89.1 m Länge über alles, 13.3 m Breite, 3.4 m Tiefgang, 1,800 t Verdrängung, and 3.4 m maximaler Tiefgang. Also two diesels at 14,800 kW (20,100 PS), one bow thruster, two propellers, more than 26 knots, TRS-3D with the single-source range and track figures, UL 5000 K, two Mirador, two navigation radars, 76 mm Compact with range greater than 18 km, two 27 mm MLG, four 12.7 mm, two RBS15 Mk3 starters, two RIM-116 RAM starters, four mine rails, two MASS, Stammbesatzung 61, F260 commissioned 16 April 2008, helicopter drones, and the X-form caption.

2. Bundeswehr, "BALTOPS 2024: Deutsche Korvetten in der Ostsee", https://www.bundeswehr.de/de/organisation/marine/aktuelles/baltops-2024-deutsche-korvetten-ostsee-5809050 . Used for the 4.5 m draft sentence, controllable-pitch propeller, bow thruster, 1. Korvettengeschwader at Warnemünde, crews of more than 60, Magdeburg as a 1,800-tonne sister, RAM within ten kilometres, RBS15 more than 200 km and warhead more than 200 kg, an MH-60R on Magdeburg's flight deck to refuel, and mine laying. Same publisher as source 1.

3. Naval Technology, "K130 Braunschweig Class Corvette", https://www.naval-technology.com/projects/k130corvette/ . Specification box used for 89.12 m, waterline length 82.8 m, beam 13.28 m, waterline breadth 12.44 m, hull height 4.8 m, depth at the waterline 3.4 m, full load 1,840 t, crew 50, and 26 knots. Body text of the same page used for the conflicting about 1,580 t, about 88 m, 13.2 m, crew 50, and over 26 knots. Also Oto Melara 76 mm Super Rapid at 120 rpm, four RBS15 Mk3, RAM 21 cells and 9.5 km, two MTU 20V 1163 TB 93 at 7.4 MW, controllable-pitch propellers, range over 2,500 nm, endurance 7 days or 21 with a tender, Blohm+Voss, launched April 2006, commissioned April 2008 at Warnemünde, Pathfinder ST Mk2, and the ESM strings EADS SPS-N 5000 and KJS 5000.

4. Wikipedia, "Braunschweig-class corvette", https://en.wikipedia.org/wiki/Braunschweig-class_corvette . Infobox used for 1,840 t (1,810 long tons), 89.12 m (292 ft 5 in), 13.28 m (43 ft 7 in), 3.4 m (11 ft 2 in), four 550 kW generator sets named MTU 12V 1600 DS550, two MTU 20V 1163 TB 93 at 7.4 MW with controllable-pitch propellers, bow thruster, 26 knots, 4,000 nmi at 15 knots, endurance 7 days or 21 with a tender, complement 65, TRS-3D on batch 1 and TRS-4D on batch 2, two navigation radars, MSSR 2000 i, MIRADOR, UL 5000 K, Link 11 and Link 16, two MASS, 76 mm, two BK-27, four RBS15 Mk3, two RAM Block II with 21 each, two mine racks of 34 Mk 12, and a helicopter pad with a hangar for two drones. The page lists the Sa'ar 6 as a related successor. The fetch retained the infobox and characteristics; it was truncated later in the article.

5. Wikipedia, "German corvette Braunschweig", https://en.wikipedia.org/wiki/German_corvette_Braunschweig . Search extract only, not a full fetch. Used for the hangar being too small for Sea King, Lynx, or NH90, the pad being large enough for a helicopter, and two Skeldar. Not used for a home port.

6. Naval Technology, "Sa'ar 6 Class Corvette", https://www.naval-technology.com/projects/saar-6-class-corvettes/ . Used only to audit the base ship: overall length 90 m, maximum beam 13.2 m, height 21.5 m, displacement about 2,000 t, crew up to 70, MEKO 100, hangar for an SH-60, CODAD with two MTU diesels and two controllable-pitch propellers, about 26 knots, range 2,500 miles as printed on that page. Weapons on that page, not copied: 40 Barak 8, up to two C-Dome, 76 mm Super Rapid, anti-ship missiles listed as Gabriel, Harpoon, or RBS-15 options, two Typhoon 30 mm, two Mk 54 tubes, ELM-2248 MF-STAR. No 91.4 m and no draft on this page.

7. Wikipedia, "Sa'ar 6-class corvette", https://en.wikipedia.org/wiki/Sa%27ar_6-class_corvette . Used only to audit the base ship: 1,900 long tons full load, 90 m (295 ft 3 in), complement 70, loosely based on the Braunschweig class. Infobox weapons, not copied: 16 Barak MX cells, 40 C-Dome, 8 Gabriel V, two Typhoon, two 324 mm tubes, MH-60. Prose says up to 16 Gabriel. Beam and draft are absent from the table read. The fetch was truncated after the characteristics block.

8. Naval News, "TKMS hands over Sa'ar 6 corvette INS Magen to the Israeli Navy", 11 November 2020, https://www.navalnews.com/naval-news/2020/11/tkms-hands-over-saar-6-corvette-ins-magen-to-the-israeli-navy/ . The fetch was blocked. A search snippet of TKMS key data was used only as a labelled snippet: length overall about 90 m, beam 13 m, full load about 1,900 t. The article body was not read.
