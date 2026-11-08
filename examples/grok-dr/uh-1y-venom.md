---
generated_at: "2026-10-14T15:29:37-04:00"
generator: "dolphin2/dossier-grok-dr"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "xai"
models:
  - "grok-4.7"
query: "Bell UH-1Y Venom fuselage length, rotor diameter, height, MTOW, engines, crew, and sensors"
sources_count: 10
asset_id: "uh-1y-venom"
title: "Naval Architectural Blueprint Dossier: Bell UH-1Y Venom"
---

# Naval Architectural Blueprint Dossier: Bell UH-1Y Venom

**Classification:** Unclassified public-source compilation. U.S. Marine Corps utility helicopter, H-1 upgrade. Four-blade main rotor, twin engines. This is not the AH-1W and not the AH-1Z.
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

### 1. MASTER COORDINATE DATUM & DIMENSIONS

glTF: forward/bow/nose = -Z, up = +Y, starboard = +X, port = -X.
Aircraft: weight-on-wheels or ground contact Y = 0. The UH-1Y ground contact is the skid landing gear [4][10]. Skid-to-datum offsets are not public.

| Parameter | Metric | Imperial | Engineering notes |
| --- | --- | --- | --- |
| Length, current official print | 17.78 m [1][2][7] | 58 feet, 4 inches [1][2][7] | [1] and [2] are one NAVAIR/Navy fact-file family restated, not two surveys. [7] repeats the same length. None of these three pages says whether 58 ft 4 in is fuselage length or rotors-turning length. |
| Length, archived NAVAIR split | metres not printed on that page | Fuselage length 44 feet; overall length 58 feet [6] | Disagreement with the current 58 ft 4 in. Do not average. [6] is a NAVAIR page updated May 2018. Overall length there is 58 feet, not 58 feet 4 inches, and fuselage length is a separate 44 feet. |
| Height, current print | 4.5 m [1][2]; 4.45 m [7] | 14 feet, 7 inches [1][2][7] | The inch figure agrees. The metre figure does not. [1] prints 4.5 m. [7] prints 4.45 m for the same 14 ft 7 in. Do not average. [1] and [2] are one fact-file family. |
| Height, archived NAVAIR | metres not printed | 17 feet [6] | Disagreement with 14 ft 7 in. Same publisher, later revised. Do not average. |
| Main rotor diameter | 14.88 m [1][2][7]. [10] prints no metric. | 48 feet, 10 inches [1][2][7]; 48' [10] | Disagreement at the inch. Do not average. 14.88 m is the diameter [1] prints for the UH-1Y, not a generic H-1 placeholder and not the AH-1Z. On [2] the AH-1Z line is a different aircraft: length 58 ft 3 in (17.75 m), height 14 ft 4 in (4.37 m), rotor diameter 48 feet (14.6 m). [10] is Bell's own kiosk and says "48' main rotor diameter" with no "10 inches." |
| Tail rotor diameter | not public | not public | [4] and [5] say the tail rotor is four-bladed. Neither prints a diameter. |
| Empty weight | 5,370 kg [1]; 5,371 kg [7] | 11,840 lb [1][7][8]; 11,839 lb [4][6]; 11,700 lb [9] | Disagreement. Do not average. [1] is the current NAVAIR print. [8] is the 2022 Marine Aviation Plan UH-1Y card. [7] prints 11,840 lb and converts it to 5,371 kg, one kilogram off [1]. [4] and [6] print 11,839 lb. [9], the 2015 Marine Aviation Plan, prints 11,700 lb. |
| Maximum gross / MTOW | 8,390 kg [1]; 8,391 kg [7] | 18,500 lb [1][2][3][4][6][7][8][9] | The pound figure is agreed across NAVAIR, Bell, the brochure, both aviation plans, and Wikipedia. The kilogram rounding disagrees by 1 kg between [1] and [7]. Do not average. |
| Basic design gross weight | not public as a second metric | 16,700 lb [4] | single-source Bell brochure, the weight at which that page states the sink speeds below. |
| Useful load | 3,021 kg is printed by [4] beside 6,661 lb, and [7] prints capacity 6,660 lb (3,021 kg) | 6,661 lb [4][6] | [4] and [6] agree on 6,661 lb. [7]'s 6,660 lb capacity is one pound off and is a capacity line, not labeled max useful load. [9] prints useful payload 5,930 lb HOGE, which is a different condition. Do not average. |
| Internal fuel | 1,172 kg printed by [4] beside the pounds | 2,584 lb [4][6]; 388 gal [3] | Pounds and gallons are different statements. Do not convert one into the other. 388 gal is single-source [3]. [8] is single-source for 77 gal auxiliary fuel adding about 30 nm or 15 minutes. |
| Engines | [1] prints 1,340 kW beside 1,800 shp. [7] prints 1,363 kW beside 1,828 shp, and 1,153 kW beside 1,546 hp continuous. | Two General Electric T700-GE-401C. 1,800 shp each [1][2]. Bell: 1,800 shp uninstalled, each engine [3]. [7]: 1,828 shp for 2 min 30 sec, and 1,546 hp continuous. | The engine model is agreed. The rating is not one number. [1] and [2] are one fact-file family. [3] agrees with them on 1,800 shp uninstalled. [7] publishes a different takeoff-style rating and a continuous rating. Do not collapse these into 1,800. |
| Crew and seats | not a dimension | [1][2][6]: pilot, co-pilot, crew chief, gunner, and eight combat-equipped troops (twelve). [3][10]: 4+8. [7]: crew of 2 (pilot and co-pilot), capacity up to ten crashworthy passenger seats, or six litters. | The NAVAIR count of twelve matches Bell's 4+8. [7] counts the pilots as crew and the cabin as capacity. Do not average the counting methods. |
| External stores | not public as a span | Two external store stations [6][7][8][9] | This is not an AH-1Z stub wing. Station coordinates and store-span are not public. |
| Main-rotor fold | travel not public | Wind limit while folding: up to and including 45 kt from any azimuth [4] | single-source [4] for the 45 kt limit. [5] confirms semiautomatic blade fold and does not print the wind limit. Hinge angle: not public. |
| Limit sink speed | 3.66 m/s (12 fps); reserve energy 4.48 m/s (14.7 fps) [4] | 12 fps and 14.7 fps, as [4] prints beside the metric | single-source Bell brochure, at the 16,700 lb basic design gross weight. |

Performance figures that are not dimensions, kept here so they are not averaged:

- [3]: maximum 170 KIAS; cruise 147 KTAS; sideward and rearward 45 KIAS; combat radius 119 nm; maximum range 325 nm. The sideward/rearward figure and the g range below are single-source [3] unless noted. [3] also prints maneuverability -0.5 to +2.3 g. A SAR-profile assumption is printed on that Bell page; it is not attached here to every Bell number.
- [6]: 170 knots maximum, 146 knots cruise; mission radius 129 nautical miles with combat load; endurance 3.3 hours; ceiling 20,000 feet, with maximum operational altitude 10,000 ft pressure altitude; hot-day payload 3,079 lb. The 3,079 lb and the 10,000 ft operational altitude are single-source [6].
- [9]: cruise 139 kts; combat radius 119 nm with eight combat-loaded troops, 5 minutes mid-mission HOGE, 10 minutes on station, and 20 minutes reserve; useful payload 5,930 lb HOGE.
- [4], marked preliminary as of November 2001: long-range cruise 135 kts; maximum continuous power 158 kts; dash 164 kts.
- [7]: maximum 164 kn; cruise 158 kn; Vne 198 kn; combat range 130 nmi with a 2,182 lb payload; endurance 3 hours 18 minutes; service ceiling 20,000 ft (6,100 m)+; rate of climb 2,520 ft/min (12.8 m/s). The climb rate, Vne, and 130 nmi figure are [7]. The 2001 brochure dash/MCP pair echoes 164 and 158 and is not an independent flight-test report.
- [10] repeats 170 kts and 325 nm beside the 4+8 capacity. Those two match [3] and are Bell's own pages.

The 119 nm combat radius appears on both [3] and [9]. [9] defines the profile. [3] does not print that same profile in the notes used here, so the shared 119 nm is recorded, not treated as one test point.

[6] says the four-bladed all-composite rotor is ballistically tolerant up to 23 mm. [7] says the rotor is designed to withstand up to 23 mm rounds. [7] may be repeating the NAVAIR description. It is not a second laboratory measurement.

[7] is single-source for a 21-inch fuselage extension just forward of the main door, printed with the parenthetical 530 mm. This dossier does not replace 530 mm with a recalculated millimetre. [7] is also single-source for main rotor area 1,808 sq ft (168.0 m2).

Station offsets are not public.

### 2. ARRANGEMENT

The UH-1Y is a Marine utility helicopter that replaced the UH-1N [1][2]. Bell is the contractor [1]. Initial operational capability is August 2008 [1][2]. [1] dates full operational capability to 2016 and lists inventory 160, acquisition category IC, now in sustainment. [6], updated May 2018, projected FOC in March 2016 and inventory 160 while the aircraft was still in production. [7] dates first flight 20 December 2001, introduction 8 August 2008, full-rate production September 2009, and final U.S. Marine Corps delivery January 2019, and it also discusses later Czech aircraft. [2] says full-rate production in 2008 and says U.S. domestic production ended in 2020. The 2008 versus September 2009 full-rate date is a disagreement. Do not average.

The airframe is a utility cabin with two pilot seats, a crew chief and gunner in the NAVAIR crew line, and eight combat-equipped Marines [1]. [7]'s 21-inch extension sits just forward of the main door and is single-source. Landing gear is skid type [4][10]. [4] says the USMC baseline also has shipboard tie-downs, a semi-monocoque tailboom and vertical fin, an elevator, and a tail skid, and that the aircraft can be towed at the 18,500 lb maximum using forward and aft ground-handling wheels. Those wheels are ground equipment, not the flight gear.

The main rotor is four-bladed, all-composite, and bearingless, with semiautomatic blade folding [4][5][6]. The tail rotor is four-bladed [4][5]. [1] says "four-bladed all-composite rotor system" and does not, on the current spec block, separately say "four-bladed tail." Tail-rotor diameter is not public. There are two engines, General Electric T700-GE-401C, on top of the cabin. Ratings disagree and are in the table.

The UH-1Y does not carry the AH-1Z stub-wing arrangement. It has two external store stations and two pintle positions for door or cabin guns [6][7][8]. [7] names 70 mm Hydra 70 or APKWS II on the external stations, and 7.62 mm M240D, .50-caliber GAU-21, or 7.62 mm GAU-17/A on the pintles. [8] names 2.75-inch rockets, guided and unguided, and GAU-17A, GAU-21, and M240D. [9] adds a fixed-forward or crew-served 7.62 mm/GAU-17A option and crew-served M240D, GAU-16, or GAU-21. GAU-17 is 7.62 mm on [7], not a .50-caliber gun.

[1] and [3] say about 85 percent parts commonality with the AH-1Z. [10] prints 85%+. [6] says 85 percent common parts with the AH-1Z. An older acquisition note of "84 percent" was not re-fetched as a full page and is not used. Commonality is not a statement that the UH-1Y rotor diameter equals the AH-1Z rotor diameter. [2] prints those diameters as different numbers.

[4] says blade folding is by automatic and manual means, commanded from the cockpit, with blade pins and an interlock that prevents rotor start if the pins are unlocked. Ground crew need not climb on top of the aircraft. No retracking is required after folding. Manual backups exist. Folding and unfolding are stated for horizontal winds up to and including 45 knots from any azimuth. Fold angle and hinge travel are not public. [5] confirms semiautomatic bladefold and new four-bladed tail rotors. [5] also uses the phrase "blade and tail folding" as a marinization remark. That page does not describe a tail-fold procedure or a travel. Tail-fold travel is not public.

Station offsets are not public.

| Item | What the sources support |
| --- | --- |
| Rotor | Four-blade composite main rotor [1][4][6]. Four-blade tail rotor [4][5]. Main diameter 48 ft 10 in (14.88 m) [1][2][7], or 48' with no inches [10]. Tail diameter not public. |
| Gear | Skids [4][10]. Ground-handling wheels for towing [4]. |
| Engines | Two T700-GE-401C [1][2][3][7]. 1,800 shp class on [1][2][3]. Different 1,828 / 1,546 ratings on [7]. |
| Cabin | Two pilots plus crew chief, gunner, and eight Marines on the NAVAIR crew line [1]. Wikipedia counts crew as two [7]. |
| Stores | Two external stations and two pintles [6][7]. Not AH-1Z stub wings. |
| Fold | Main-rotor blades, semiautomatic, 45 kt wind limit [4]. Travel not public. |

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

No pivot coordinates are published. Unpublished travel is "travel: not public."

- Fuselage, nose = -Z, skid contact Y = 0.
  - Cockpit, two stations, mirror-imaged crew stations as described in the 2015 plan's H-1 cockpit sentence [9]. Seat travel: not public.
  - Cabin and main door. The 21-inch stretch just forward of the main door is single-source [7]. Door travel: not public.
  - Skid landing gear, left and right [4][10]. Stroke: not public beyond the single-source sink speeds in section 1.
  - Tailboom, vertical fin, elevator, tail skid [4]. Elevator travel: not public. Tail-skid travel: not public.
- Propulsion and rotors.
  - Two T700-GE-401C turboshafts [1][3]. Power ratings disagree. Nacelle coordinates: not public.
  - Main gearbox. Presence is required by the rotor drive. Gearbox model and shaft angles: not public.
  - Main rotor, four blades, bearingless head, semiautomatic fold [4][5][6]. Diameter is the 48 ft 10 in versus 48' disagreement. Fold travel: not public. Rotor rpm: not public.
  - Tail rotor, four blades [4][5]. Diameter: not public. Fold travel: not public. [5]'s "blade and tail folding" phrase is not a measured tail-fold.
- Mission hardware.
  - Nose sensor. BRITE Star Block II is named by [6], [8], [9], and [10]. The current [1] spec block does not name the model. The current [3] page says FLIR and does not name BRITE Star. Station coordinates: not public. Turret travel: not public.
  - Two external store stations [6][7]. Travel of the stores: not public. These are not AH-1Z stub wings.
  - Two pintle mounts [6][7]. Gun travel: not public.
  - Optimized TopOwl helmet sight [3][10]. Head motion: not a ship or airframe pivot.

### 4. SENSOR SITING & MISSION SYSTEMS

Coordinates of the sensor, the radios, the stores, and the guns are not public.

Sensor: archived NAVAIR names "Advanced Third Gen - FLIR Systems, Inc. BRITE Star Block II" [6]. The Bell kiosk names FLIR BriteStar Block II [10]. The 2022 UH-1Y card names Brite Star Block II and Intrepid Tiger II [8]. The 2015 plan names BRITE Star Block II on the H-1 line [9]. The current NAVAIR spec block [1] does not name the FLIR model. The current Bell product page [3] says FLIR, an Optimized TopOwl helmet, radar and missile warning, and crew-served weapons, without the model list in the fetched specs.

[8] says Intrepid Tiger II versions (V)1 and (V)3 are in service on the AV-8B and the UH-1Y respectively, so the UH-1Y set named there is (V)3. [7] describes AN/ALQ-231(V)3 Intrepid Tiger II. That nomenclature agrees with the (V)3 assignment. Antenna location is not public.

Defensive sets named on the 2015 UH-1Y card are AAR-47, ALE-47, and APR-39 [9]. The 2022 plan also lists APR-39(D)V2 and a DAIRCM line in an H-1 upgrade paragraph. That paragraph is a roadmap, not a coordinate, and it is not copied here as a proven installed station.

Radios: [8] lists networked systems ANW2, FMV, and Tactical Targeting on the UH-1Y card. The extract line was truncated after "Tactical Targeting." No further radio model is added. [9] describes cockpit systems that assimilate communications, digital fire control, all-weather navigation, day/night targeting, and weapons. No antenna coordinates.

Door guns and external weapons are the sets in section 2. Two pintles and two external stations are the sourced counts [6][7][8].

### 5. DIFFERENCES FROM THE BASE DOSSIER

Written from scratch. Worklist similarity is none. No base dossier was used.

An AH-1W Cobra dossier or an AH-1Z Viper dossier would have been the wrong base. The Navy fact file prints the AH-1Z rotor as 48 feet (14.6 m) and the UH-1Y rotor as 48 feet 10 inches (14.88 m) [2]. The Venom is the utility aircraft, with a cabin, skids, and door guns, not the attack helicopter's stub wings.

### 6. GAME DATA CHECK

`unit-dimensions.json` keys `jslc.aircraft.uh-1y-venom` and `coalition.aircraft.uh-1y-venom` are the same block: lengthM 17.78, widthM 14.88, heightM 4.5, fit length, bandMinM 15.65, bandMaxM 19.91, confidence high, designSize false, category aircraft, represents "UH-1Y Venom." Source string: "UH-1Y deployed length about 17.78 m. https://www.navair.navy.mil/product/UH-1Y-Venom . Rotor width is an H-1 representative."

Roster `jslc.json` id `jslc.aircraft.uh-1y-venom`, name "UH-1Y Venom", legacyId `coalition.aircraft.uh-1y-venom`. Dimension block:

```
"dimensions": {
  "lengthM": 17.78,
  "widthM": 14.88,
  "heightM": 4.5,
  "massTonnes": null,
  "basis": "representative"
}
```

Length 17.78 m agrees with the current NAVAIR, Navy fact file, and Wikipedia figure of 58 ft 4 in [1][2][7]. Those pages do not say fuselage versus rotors turning. The May 2018 NAVAIR page instead splits fuselage 44 feet from overall 58 feet [6]. The game length matches the later NAVAIR number and does not match the archived overall length of 58 feet.

Width 14.88 m is the UH-1Y main-rotor diameter printed by NAVAIR and the Navy fact file [1][2], and repeated by Wikipedia [7]. It is not the AH-1Z's 48 ft / 14.6 m [2]. The game source string calls it "an H-1 representative," which is more cautious than NAVAIR's explicit UH-1Y label. Bell's kiosk prints 48 feet and omits the 10 inches [10], so the inch-level diameter is not unanimous. The game value matches NAVAIR, not the kiosk's shorter wording.

Height 4.5 m matches the metre NAVAIR prints for 14 ft 7 in [1]. Wikipedia prints 4.45 m for those same inches [7]. Archived NAVAIR prints height 17 feet [6]. The game height is the current NAVAIR rounding, not a match to the archived 17 feet, and it is not a second measurement of the airframe.

massTonnes null stays empty. 18,500 lb is well supported, and the kilogram prints disagree by 1 kg [1][7]. No tonne figure is manufactured from the pounds. Roster basis "representative" is stricter than unit-dimensions confidence "high." The length and the rotor match current NAVAIR publications. The height matches NAVAIR's printed metres and conflicts with that agency's own 2018 height of 17 feet.

### 7. MASTER AI VIDEO PROMPT PACKAGE

1. Marine utility helicopter on skids, nose forward, four-blade main rotor, four-blade tail rotor, cabin doors, twin engines above the cabin. No attack-helicopter stub wings. No rotor-diameter callout, because Bell and NAVAIR do not print the same inch value.

2. Blade-fold on the ground. Main-rotor blades pin for shipboard stow. No hinge angle and no folded width. Wind is simply "within the published folding limit."

3. Cabin with two pilots and embarked Marines, a crew chief and a gunner at the doors, pintle guns trained outboard. Gun model left off the picture label because M240D, GAU-17, and GAU-21 are all sourced and are not one gun.

4. Nose sensor turret and a helmet sight in the cockpit, day-into-dusk, no turret-travel numbers and no antenna coordinates.

### 8. SOURCES

1. UH-1Y Venom. Naval Air Systems Command, product page updated March 2026. https://www.navair.navy.mil/product/UH-1Y-Venom . Current length 58 ft 4 in (17.78 m), height 14 ft 7 in (4.5 m), rotor diameter 48 ft 10 in (14.88 m), empty 11,840 lb (5,370 kg), MTOW 18,500 lb (8,390 kg), two T700-GE-401C at 1,800 shp (1,340 kW) each, crew of twelve, four-bladed composite rotor, 85 percent commonality with the AH-1Z, IOC August 2008, FOC 2016, inventory 160. Does not say fuselage versus rotors-turning, and does not name BRITE Star in the spec block.

2. AH-1Z Viper and UH-1Y Venom Helicopters. U.S. Navy fact file, last updated 22 October 2021. https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2160217/ah-1z-viper-and-uh-1y-venom-helicopters/ . Same UH-1Y length, height, rotor, MTOW, engines, and crew as [1]. Does not reprint empty weight. Same data family as [1]. Used to show the AH-1Z rotor on the same page is 48 feet (14.6 m), a different aircraft.

3. Bell UH-1Y. Bell Textron, current product page. https://www.bellflight.com/products/bell-uh-1y . 170 KIAS, 147 KTAS, 45 KIAS sideward/rearward, combat radius 119 nm, maximum range 325 nm, -0.5 to +2.3 g, gross weight 18,500 lb, fuel 388 gal, T700-GE-401C at 1,800 shp uninstalled, capacity 4+8, 85 percent commonality, FLIR without a model name, Optimized TopOwl, marinized airframe. Does not print overall length, height, or rotor diameter in the fetched spec block.

4. Bell UH-1Y brochure. Bell Helicopter Textron, PDF hosted at https://www.aviatorsdatabase.com/wp-content/uploads/2013/07/Bell-UH1Y.pdf . Four-blade bearingless main rotor, semiautomatic blade fold, 45 kt wind limit, four-blade tail rotor, skids, tailboom, elevator, tail skid, empty 11,839 lb, useful load 6,661 lb, internal fuel 2,584 lb, maximum gross 18,500 lb, basic design gross weight 16,700 lb, sink speeds, preliminary November 2001 speed table. Pattern search of this PDF did not return a "48 ft 10 in" or "58 ft 4 in" line.

5. UH-1Y. GlobalSecurity.org. https://www.globalsecurity.org/military/systems/aircraft/uh-1y.htm . Semiautomatic bladefold, four-bladed tail rotor, and the marinization phrase "blade and tail folding," with no tail-fold travel and no tail-rotor diameter.

6. UH-1Y Venom platform page, updated May 2018. NAVAIR, via the Wayback Machine. https://web.archive.org/web/20181017195629/http://www.navair.navy.mil/index.cfm?fuseaction=home.displayPlatform&key=059321A9-8B4A-4839-8E70-F386299C8FF8 . Fuselage 44 feet, overall length 58 feet, height 17 feet, empty 11,839 lb, maximum gross 18,500 lb, useful load 6,661 lb, internal fuel 2,584 lb, hot-day payload 3,079 lb, endurance 3.3 hours, 170/146 knots, ceiling 20,000 feet with 10,000 ft pressure-altitude operational limit, mission radius 129 nm, BRITE Star Block II, two pintles and two external stores, crew plus eight troops, 23 mm ballistic tolerance, 85 percent common parts.

7. Bell UH-1Y Venom. Wikimedia Foundation. https://en.wikipedia.org/wiki/Bell_UH-1Y_Venom . Length 58 ft 4 in (17.78 m), height 14 ft 7 in (4.45 m), rotor 48 ft 10 in (14.88 m), empty 11,840 lb (5,371 kg), MTOW 18,500 lb (8,391 kg), 1,828 shp and 1,546 hp continuous ratings, 21-inch (530 mm) extension, rotor area, performance and armament lines, crew counted as two, AN/ALQ-231(V)3, dates. Cited there to a Bell guide and the International Directory of Civil Aircraft, so it is not an independent weighing of the NAVAIR figures it repeats.

8. 2022 Marine Aviation Plan, April 2022. U.S. Marine Corps, PDF via https://s3.documentcloud.org/documents/21849866/2022-marine-aviation-plan-final-april-2022.pdf . UH-1Y card: empty 11,840 pounds, maximum gross 18,500 pounds, two weapons stations, 2.75-inch rockets, GAU-17A, GAU-21, M240D, Brite Star Block II, Intrepid Tiger II, ANW2, FMV, Tactical Targeting (line truncated), 77 gal auxiliary fuel, and IT-II (V)3 on the UH-1Y. Cruise speed on that card was not in the extracted lines and is not stated.

9. 2015 Marine Aviation Plan. U.S. Marine Corps. https://www.aviation.marines.mil/Portals/11/2015%20Marine%20Aviation%20Plan%20Final_%2010%20Oct%202014_1110%20EDT.pdf . Search extract of the UH-1Y card: empty weight 11,700 lb, maximum gross 18,500 lb, useful payload 5,930 lb HOGE, cruise 139 kts, combat radius 119 nm with the printed profile, two weapons stations, rockets and the listed guns, AAR-47, ALE-47, APR-39, BRITE Star Block II. A direct pattern search of the PDF did not isolate that card; the search index of this URL did. Treated as search-indexed official text.

10. Bell UH-1Y kiosk. Bell. https://experience.bellflight.com/bell-uh-1y-kiosk . "With a 48' main rotor diameter and skid-type landing gear." Also FLIR BriteStar Block II, Optimized TopOwl, 85%+ commonality, 4+8, 170 kts, and 325 nm. The kiosk page is mixed with other Bell models. Figures for the 407 and the 505 on that page are not used.
