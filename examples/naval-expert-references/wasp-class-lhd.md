# Naval Reference: Wasp-Class Amphibious Assault Ship (LHD 1–8)

**Asset Identifier:** `wasp-class-lhd` | **Classification:** US Navy Amphibious Assault Ship (LHD)  
**Standard:** JSLC / Project Eretz Standard | **Worker Identity:** `nrf6` (`nrf6_gem_3.8_hi`)  
**Handoff:** `HO-20261009-naval-nrf6` | **Observed UTC:** `2026-10-09T11:34:00Z`  
**Target:** `references/wasp-class-lhd.md`  

---

## 1. Hull Registry & Variant Differences

The *Wasp* class comprises eight 844-ft multi-purpose amphibious assault ships built by Ingalls Shipbuilding [`sourced-wasp-class`: [USN 2169814][ref-usn]]:

- **LHD 1–5 & 7 (*Wasp*, *Essex*, *Kearsarge*, *Boxer*, *Bataan*, *Iwo Jima*):** Steam baseline (2 boilers, 2 geared steam turbines, 70,000 shp, twin controllable pitch screws) [`sourced-wasp-class`: [USN 2169814][ref-usn]]. LHD-1, 2, 4, 5, 7 modernized for F-35B with Thermion non-skid coating on Spots 7 & 9, deck structural stiffeners, and relocated lighting [`sourced-lhd1`: [DVIDS 8525689][d-8525689]].
- **LHD-6 *Bonhomme Richard*:** Steam baseline. Stricken after pier fire in San Diego (July 2020); decommissioned 2021, scrapped.
- **LHD-8 *Makin Island*:** **Major subclass variant.** First US amphibious ship with hybrid-electric CODLOG propulsion: 2x GE LM2500+ gas turbines (70,000 shp) + 2x 5,000 hp electric auxiliary propulsion motors (APM) [`sourced-lhd8`: [USN 2169814][ref-usn]]. No boilers; all-electric auxiliaries. Reconfigured machinery spaces, enlarged intake/exhaust trunks, modified stack profile, and SPQ-9B radar.

---

## 2. Sourced Dimensions & Capacities

| Parameter | Metric SI | Imperial | Tier | Primary Source & Supporting Evidence |
| :--- | :---: | :---: | :---: | :--- |
| **Length Overall (LOA)** | **257.25 m** | **844.0 ft** | `sourced-wasp-class` | [USN Fact File 2169814][ref-usn] ("844 ft"); [FAS SLCP LHD-3][ref-slcp-1] p.1. |
| **Waterline Length ($L_{WL}$)** | **237.13 m** | **778.0 ft** | `sourced-wasp-class` | [FAS SLCP LHD-3 Sect I][ref-slcp-1] p.1: *"Water Line: 778 feet"*. |
| **Flight Deck Length** | **249.33 m** | **818.0 ft** | `sourced-wasp-class` | [FAS SLCP LHD-3 Sect I][ref-slcp-1] p.1: *"Flight Deck: 818 feet"*. |
| **Beam (Waterline)** | **32.31 m** | **106.0 ft** | `sourced-wasp-class` | [USN Fact File 2169814][ref-usn]: *"Beam: 106 feet (32.3 meters)"*. |
| **Beam (Elevators Out)** | **60.96 m** | **200.0 ft** | `sourced-wasp-class` | [FAS SLCP LHD-3 Sect I][ref-slcp-1]: *"Beam w/elevators extended: 200 ft"*. |
| **Draft (Full Load Nav)**| **8.15–8.23 m**| **26.75–27.0 ft**| `sourced-wasp-class` | [USN 2169814][ref-usn] ("27 ft"); [FAS SLCP LHD-3][ref-slcp-1] ("26 ft 9 in"). |
| **Ballasted Stern Draft** | **10.97 m** | **36.0 ft** | `sourced-wasp-class` | [FAS SLCP LHD-3 Sect I][ref-slcp-1]: *"Draft, Ballasted: 36 ft at stern"*. |
| **Full Load Displacement** | **41,182–41,810 t**| **40,532–41,150 LT**| `sourced-wasp-class` | [FAS SLCP LHD-3][ref-slcp-1] ("40,532 LT"); [USN 2169814][ref-usn] ("41,150 tons"). |
| **Freeboard (Main / Flight)**| **10.36 / 19.81 m**| **34.0 / 65.0 ft** | `sourced-wasp-class` | [FAS SLCP LHD-3 Sect I][ref-slcp-1]: Main Deck 34 ft, Flight Deck 65 ft. |
| **Well Deck ($L \times W \times H$)** | **81.1 $\times$ 15.2 $\times$ 8.5 m**| **266 $\times$ 50 $\times$ 28 ft** | `sourced-wasp-class` | [FAS SLCP LHD-3][ref-slcp-1]. 13,300 sq ft. Holds 3 LCACs (tandem), 2 LCUs, 40 AAVs. |
| **Vehicle Area / Cargo Cube** | **1,939 m² / 2,832 m³** | **20,878 sq ft / 100,000 ft³** | `sourced-wasp-class` | [FAS SLCP LHD-3 Sect II][ref-slcp-2]: Upper/lower vehicle decks; Holds 4, 5, 9, 10. |

---

## 3. Real Fitted Systems & Siting

- **Mk 49 RAM (2 Mounts):** 21-round RIM-116 launcher [`sourced-wasp-class`: [USN 2169814][ref-usn]]. Fwd Port and Aft Stbd Sponsons. Missile only; no gun or SeaRAM dome.
- **Mk 29 Sea Sparrow / ESSM (2 Launchers):** 8-cell box launcher [`sourced-wasp-class`: [USN 2169814][ref-usn]]. Fwd Stbd and Aft Port Quarter Sponsons.
- **Mk 15 Phalanx Block 1B CIWS (2 Mounts):** 20mm 6-barrel Gatling [`sourced-wasp-class`: [USN 2167831][ref-ciws]]. Fwd Island (Mt 22) and Aft Port Stern (Mt 23). Cadence **4,500 rd/min** = **750 RPM** rotor speed ($4,500 \div 6$).
- **Mk 38 Mod 2/3 25mm Chain Guns (3–4 Mounts):** Catwalk sponsons [`sourced-wasp-class`: [USN 2169814][ref-usn]].
- **AN/SPS-48E 3D Radar:** Main mast. Continuously rotates at **7.5 RPM** (Surveillance) or **15.0 RPM** (Track) [`sourced-wasp-class`: SKILL.md].
- **AN/SPS-49(V) 2D Radar:** Aft mast. Continuously rotates at **6.0 RPM** or **12.0 RPM** [`sourced-wasp-class`: SKILL.md].
- **AN/SPS-67(V) Surface Search:** Forward island. Rotates at **15.0 RPM** [`sourced-wasp-class`: SKILL.md].
- **AN/SPS-73(V) Navigation Radar:** Rotates at **24.0–30.0 RPM** [`sourced-wasp-class`: SKILL.md].
- **AN/SPQ-9B Track Radar:** Enclosed rotating antenna (30 RPM) on LHD-8 and refits [`sourced-lhd8`: [USN 2169814][ref-usn]].
- **Stationary Radomes & SATCOM:** AN/USC-38, OE-82, and TACAN housings are **fixed shells that do not rotate** [`sourced-CVN-78`: references/todays-lessons-20261009.md].

---

## 4. Moving Parts, Rigging Kinematics & Ranges

| Part / Node | Parent Assembly | Motion Type | Local Axis | Kinematic Limits | Rates / Operational Notes | Status |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| **Port Aircraft Elevator** | Port Hull Fr 45–55 | `prismatic` | `[0, 1, 0]` ($+Y$) | 0.0 m (Hangar) to $+11.3\text{m}$ (Flight deck) | ~100 ft/min; pump rate `unresolved` | `sourced-wasp-class` |
| **Port Elevator Flap** | Port Elevator Plat | `revolute` | `[0, 0, -1]` ($-Z$) | 0.0° (Spread) to $+90.0^\circ$ (Folded vertical) | 90° upward fold for Panama Canal | `sourced-wasp-class` |
| **Stbd Aircraft Elevator** | Stbd Hull Fr 85–95 | `prismatic` | `[0, 1, 0]` ($+Y$) | 0.0 m (Hangar) to $+11.3\text{m}$ (Flight deck) | Capacity 75,000 lbs (34,019 kg) | `sourced-wasp-class` |
| **Stbd Elevator Flap** | Stbd Elevator Plat | `revolute` | `[0, 0, 1]` ($+Z$) | 0.0° (Spread) to $+90.0^\circ$ (Folded vertical) | 90° upward fold along outer platform | `sourced-wasp-class` |
| **Stern Well Deck Gate** | Bottom Sill Fr 124 | `revolute` | `[1, 0, 0]` ($+X$) | 0.0° (Closed vertical) to $+90.0^\circ$ (Open ramp) | ~120–180 s cycle; exact rate `unresolved` | `sourced-wasp-class` |
| **Internal Vehicle Ramp**| 3rd Deck (Upper Veh)| `revolute` | `[1, 0, 0]` ($+X$) | 48'6" x 13' ramp lowers to 4th Deck | Inter-deck vehicle transfer | `sourced-wasp-class` |
| **Twin Horn Rudders** | Rudder Stock Fr 114| `revolute` | `[0, 1, 0]` ($+Y$) | $-35.0^\circ$ to $+35.0^\circ$ (Stops $\pm 36.5^\circ$) | 3.8°/s – 4.2°/s slew; 0° vertical stock | `sourced-wasp-class` |
| **Twin Propeller Screws** | Shaft Struts | `continuous` | **Shaft line ($\approx 2.5^\circ$ rake)** | Continuous roll (Port CCW, Stbd CW looking fwd) | Shaft rake follows hull, NOT global $Z$ | `inferred-from-usn` |
| **Phalanx CIWS Mounts** | Mount Barbette | `revolute` | `[0, 1, 0]` ($+Y$) | 360° continuous rotation | Up to 100°/s slew rate | `sourced-wasp-class` |
| **Phalanx Gun Trunnion** | CIWS Turret | `revolute` | Local transverse | $-25.0^\circ$ to $+85.0^\circ$ elevation | Up to 100°/s elevation rate | `sourced-wasp-class` |
| **Phalanx M61A1 Rotor** | Gun Housing | `continuous` | Gun bore axis | Continuous roll | **750 RPM** ($4,500\text{ shots/min} \div 6$) | `sourced-wasp-class` |
| **Mk 49 RAM Train/Elev** | Mount Pedestal / Tur| `revolute` | Azimuth $+Y$ / Pitch | Azimuth $\pm 180^\circ$; Elev $-10^\circ$ to $+80^\circ$ | $\approx 60^\circ/\text{s}$; missile only, no rotor | `sourced-wasp-class` |

---

## 5. Common Modelling Errors & Non-Conflation Warnings

1. **LCAC Tandem Rule Violation:** LCAC beam is **14.3 m** (47.0 ft) in a **15.24 m** (50.0 ft) well deck (94.08% breadth). Side-by-side parking is physically impossible. LCACs must be staged in single-file tandem (Spots 1, 2, 3) [`sourced-wasp-class`: [FAS SLCP LHD-3][ref-slcp-1]].
2. **Conflating LHD-8 with LHD 1–7:** Treating LHD-8 as identical to LHD-1 is an error. LHD-8 has gas turbines, no steam boilers, no steam pipes, different stack profiles, and all-electric auxiliaries.
3. **Phalanx CIWS Rotor Rate Error:** Animating M61A1 barrel cluster at 4,500 RPM is an error. 4,500 is firing cadence (shots/min); physical shaft rotation is 750 RPM.
4. **Conflating SeaRAM and Mk 49 RAM:** Mk 49 RAM has 21 missile cells and no radar dome. SeaRAM has 11 cells and a Phalanx dome. Wasp-class carries Mk 49 RAM.
5. **Propeller Shaft Rake:** Propeller screw rotation axis must follow the ship's authentic downward shaft angle ($\approx 2.5^\circ$), not the global horizontal $Z$-axis.
6. **Stationary Radomes:** Weather domes, TACAN casings, and SATCOM enclosures are rigid static structures; do not animate them spinning.
7. **Elevator Folding Hinges:** Outboard platform edges fold 90° upward for canal transit; they are not rigid monolithic slabs.

---

## 6. Verified DVIDS Image Registry by Angle

*Primary trusted repository: [dvidshub.net][ref-dvids].* All captions and URLs verified:

- **Bow / Underwater:** [DVIDS 7667221][d-7667221] (*USS Essex Conducts Maintenance*, 2023-02-28). Drydock bow view showing bulbous bow and draft marks.
- **Bow Stem / Anchor:** [DVIDS 7743890][d-7743890] (*USS Essex Recovers Starboard Anchor*, 2023-04-12). Starboard anchor hawse pipe, bullnose, and flight deck overhang.
- **Port Profile:** [DVIDS 8525689][d-8525689] (*Wasp Passes Through The Strait Of Gibraltar*, 2024-06-26). Broadside port underway profile; elevator cutout, sponsons, sheer line.
- **Starboard Island:** [DVIDS 6436626][d-6436626] (*USS Wasp Operations at Sea*, 2020-10-24). Starboard bridge wing, island superstructure, and mast yards.
- **Top / Overhead Deck:** [DVIDS 3449831][d-3449831] (*USS Bataan Alongside Washington Chambers*, 2017-06-06). Aerial flight deck view; 9 spots, tramline, Spot 7/9 thermal areas.
- **Top / Overhead Aerial:** [DVIDS 4779448][d-4779448] (*USS Wasp Conducts DATF Drill*, 2018-09-26). High-angle aerial view of flight deck layout.
- **Stern Gate / Ingress:** [DVIDS 9305358][d-9305358] (*LCAC 64 Enters USS Makin Island*, 2025-09-08). Lowered stern gate, flooded well deck sill, LCAC entry.
- **Stern Operations:** [DVIDS 9037885][d-9037885] (*USS Iwo Jima Well Deck Operations*, 2025-05-14). LCAC entering well deck; stern transom opening and water level.
- **Well Deck Interior:** [DVIDS 5076063][d-5076063] (*USS Wasp Operations at Sea*, 2019-02-02). LCAC staged on dry sill, wing walls, overhead monorail.
- **Elevator Mechanism:** [DVIDS 8697390][d-8697390] (*Wasp Sailors Weld Aircraft Elevator*, 2024-10-09). Underside structural truss, guide rails, and folding flap hinge of port elevator.
- **Elevator Deck Level:** [DVIDS 8185828][d-8185828] (*HSC 26 Live-Fire Aboard USS Bataan*, 2023-11-20). Elevator platform flush at flight deck.
- **CIWS Mount Detail:** [DVIDS 5642357][d-5642357] (*USS Wasp Operations at Sea*, 2019-08-03). Phalanx CIWS Block 1B mount, radar dome, trunnion, and M61A1 barrel cluster.
- **Sea Sparrow Mk 29:** [DVIDS 214349][d-214349] (*Wasp Sailors Load Sea Sparrow Missiles*, 2009-10-20). Mk 29 8-cell launcher elevation box and training mechanism.
- **Boat Davit Mechanism:** [DVIDS 7713785][d-7713785] (*TYCOM Sea Trials*, 2023-03-30). Starboard boat recess, gravity davit arms, and 7m RHIB handling.
- **Crash Crane:** [DVIDS 5115473][d-5115473] (*USS Makin Island Crane Operations*, 2019-02-14). Tilly crash crane on flight deck; rotating cab, boom, and counterweight.

---

## 7. External Collector Links & Uncertainty Register

- **Local Collector (Ships Grok):** `../../../../dreidel3d-sv2/refimages/ships-grok/wasp-class-lhd/` (`elevator-dvids-8697388.jpg`, `elevator-dvids-2824807.jpg`, `overhead-wikimedia-2012.jpg`, `stern-dvids-9557429.jpg`, `9557430.jpg`, well deck series `4712220.jpg`–`9557431.jpg`).
- **Local Collector (Ships Agy):** `../../../../dreidel3d-sv2/refimages/ships-agy/wasp-class-lhd/` (`front-commons-LHD-1-bow.jpg`, `port-commons-LHD-1-port.jpg`, `stbd-commons-LHD-3-stbd.jpg`, `rear-stern-gate-commons-LHD-4-stern-gate.jpg`, `elevator-structure-commons-LHD-1-elevator-welding.jpg`, `vehicle-deck-cargo-commons-LHD-5-vehicle-deck.jpg`, `vehicle-deck-staging-commons-LHD-5-vehicle-ramp.jpg`).
- **Collector Status:** Image downloads complete in both `ships-grok` and `ships-agy`; formal `INDEX.md` catalog compilation pending background runner completion.
- **Uncertainty Register:**
  1. *Elevator Hoist Flow Timing:* ~100 ft/min (~0.5 m/s); exact loaded vs. unloaded hydraulic transit time remains `unresolved`.
  2. *Stern Gate Flow Rate:* Full lower cycle ~120–180 s; exact hydraulic throttling rate `unresolved`.
  3. *Hangar Division Fire Doors:* Sliding/rolling transit speed `unresolved`.
  4. *Propeller Shaft Strut Dimensions:* Hydrodynamic bossing fairing offsets and strut knuckle coordinates remain proprietary shipyard data (`unresolved`).

---

## 8. Primary Sources & Reference Links

[ref-usn]: https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169814/amphibious-assault-ships-lhdlhar/ "U.S. Navy Fact File: Amphibious Assault Ships - LHD/LHA(R)"
[ref-ciws]: https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2167831/mk-15-phalanx-close-in-weapon-system-ciws/ "U.S. Navy Fact File: MK 15 Phalanx CIWS"
[ref-slcp-1]: https://man.fas.org/dod-101/sys/ship/docs/slcp-lhd-3/Secti.html "USS Kearsarge (LHD-3) SLCP Section I: General Characteristics"
[ref-slcp-2]: https://man.fas.org/dod-101/sys/ship/docs/slcp-lhd-3/Sectii.html "USS Kearsarge (LHD-3) SLCP Section II: Loading, Stowage, and Offloading"
[ref-dvids]: https://www.dvidshub.net "Defense Visual Information Distribution Service"
[d-7667221]: https://www.dvidshub.net/image/7667221/uss-essex-conducts-maintenance-period
[d-7743890]: https://www.dvidshub.net/image/7743890/uss-essex-recovers-starboard-anchor
[d-8525689]: https://www.dvidshub.net/image/8525689/wasp-passes-through-strait-gibraltar
[d-6436626]: https://www.dvidshub.net/image/6436626/uss-wasp-lhd-1-operations-sea
[d-3449831]: https://www.dvidshub.net/image/3449831/uss-bataan-lhd-5-pulls-alongside-dry-cargo-and-ammunition-ship-usns-washington-chambers-t-ake-11
[d-4779448]: https://www.dvidshub.net/image/4779448/uss-wasp-lhd-1-conducts-datf-drill
[d-9305358]: https://www.dvidshub.net/image/9305358/landing-craft-air-cushion-64-enters-uss-makin-island-lhd-8
[d-9037885]: https://www.dvidshub.net/image/9037885/uss-iwo-jima-conducts-well-deck-operations
[d-5076063]: https://www.dvidshub.net/image/5076063/uss-wasp-lhd-1-operations-sea
[d-8697390]: https://www.dvidshub.net/image/8697390/wasp-sailors-weld-aircraft-elevator-during-mdvr
[d-8185828]: https://www.dvidshub.net/image/8185828/hsc-26-sailors-execute-live-fire-exercise-aboard-uss-bataan
[d-5642357]: https://www.dvidshub.net/image/5642357/uss-wasp-lhd-1-operations-sea
[d-214349]: https://www.dvidshub.net/image/214349/wasp-sailors-load-sea-sparrow-missiles
[d-7713785]: https://www.dvidshub.net/image/7713785/tycom-sea-trials
[d-5115473]: https://www.dvidshub.net/image/5115473/uss-makin-island-lhd-8-crane-operations


---

<!-- NAVAL-CURRENT-START -->
# wasp-class-lhd — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:24:21.394242+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-LHD-1` | USS Wasp lists length 844 ft, beam 106 ft, draft 27 ft. Derived SI: approximately 257.25 m, 32.31 m, 8.23 m. The class page's 253.2 m and 31.8 m equivalents conflict with its feet; never silently copy those conversions. | [Primary source](https://www.surflant.usff.navy.mil/Organization/Operational-Forces/Amphibious-Ships/USS-WASP-LHD-1/About-Us/); General Characteristics |
| `sourced-Wasp-class-historical-fit` | LHD 1-7 have boiler/steam-turbine propulsion; LHD 8 has gas turbines and auxiliary propulsion motors. The class list gives three Phalanx mounts for LHD 1-4, two for LHD 5-8, and capacity for three LCACs or two LCUs. Present individual-hull fits need dated confirmation. | [Primary source](https://www.surflant.usff.navy.mil/Organization/Operational-Forces/Amphibious-Ships/Amphibious-Assault-Ship-LHD-LHA-Info-Page/); General Characteristics, Wasp Class |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| propeller/shaft assemblies | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| rudders | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| aircraft elevators | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| stern gate | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| identified radars and weapon mounts | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| davits | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Do not use two CIWS mounts as a universal class count. Preserve hull/date configuration and conflicting displacement/area tables. Draft future UTC timestamps are unverified worker claims. Do not equate no new motion contacts with clearance of inherited contacts.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [USS Bataan (LHD 5) ](https://www.dvidshub.net/image/3449831/uss-bataan-lhd-5) | `170604-N-HP188-0145 U.S. 5TH FLEET AREA OF OPERATIONS (June 4, 2017) The amphibious assault ship USS Bataan (LHD 5) pulls alongside the dry cargo and ammunition ship USNS Washington Chambers (T-AKE 11) during a` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Defense of the Amphibious Task Force (DATF) ](https://www.dvidshub.net/image/4779448/defense-amphibious-task-force-datf) | `SOUTH CHINA SEA (Sept. 27, 2018) - Sailors conduct a foreign object debris walk down prior to flight operations during a Defense of the Amphibious Task Force (DATF) drill on the flight deck of the amphibious as` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS WASP (LHD 1) OPERATIONS AT SEA ](https://www.dvidshub.net/image/5076063/uss-wasp-lhd-1-operations-sea) | `190203-N-OX029-2014 PHILIPPINE SEA (Feb. 3, 2019) - Marines disembark a Landing Craft, Air Cushion (LCAC) in the well deck of the amphibious assault ship USS Wasp (LHD 1). Wasp, flagship of the Wasp Amphibious ` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Makin Island (LHD 8) Crane Operations ](https://www.dvidshub.net/image/5115473/uss-makin-island-lhd-8-crane-operations) | `190219-N-TF178-1053 SAN DIEGO (Feb. 19, 2019) Aviation Support Equipment Technician 2nd Class Leslie Bueso transports a dolly aboard the amphibious assault ship USS Makin Island (LHD 8) during crane operations.` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS WASP (LHD 1) OPERATIONS AT SEA ](https://www.dvidshub.net/image/5642357/uss-wasp-lhd-1-operations-sea) | `190803-N-RI884-1088 CORAL SEA (Aug. 3, 2019) – Fire Controlmen conduct routine maintenance checks on an MK-15 Phalanx close-in weapons system (CIWS) aboard the amphibious assault ship USS Wasp (LHD 1). Wasp, fl` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Wasp (LHD 1) Operations at Sea ](https://www.dvidshub.net/image/6436626/uss-wasp-lhd-1-operations-sea) | `201024-N-RI884-1010 NORFOLK (Oct. 24, 2020) Sailors stand watch on the starboard bridge wing aboard the amphibious assault ship USS Wasp (LHD 1) as the ship transits Naval Station Norfolk. Wasp is currently und` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Essex Conducts A Maintenance Period ](https://www.dvidshub.net/image/7667221/uss-essex-conducts-maintenance-period) | `SAN DIEGO (Feb. 28, 2023) Amphibious assault ship USS Essex (LHD 2) conducts a maintenance period in San Diego to upgrade and refurbish many key systems aboard, Feb. 28, 2023. The U.S. Navy takes a methodical a` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [TYCOM Sea Trials ](https://www.dvidshub.net/image/7713785/tycom-sea-trials) | `230330-N-OX029-3021 ATLANTIC OCEAN (March 30, 2023) – Sailors lower a rigid hull inflatable boat from the starboard side boat deck aboard the amphibious assault ship USS Wasp (LHD 1) during a man overboard dril` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Essex Recovers Starboard Anchor ](https://www.dvidshub.net/image/7743890/uss-essex-recovers-starboard-anchor) | `SAN DIEGO (April 12, 2023) The starboard chain and anchor aboard amphibious assault ship USS Essex (LHD 2) are hauled into the hawse pipe during an anchor recovery, April 12, 2023. Essex is dry docked in San Di` — `sourced-caption` | `starboard` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [HSC 26 Sailors Execute a Live-Fire Exercise Aboard USS Bataan ](https://www.dvidshub.net/image/8185828/hsc-26-sailors-execute-live-fire-exercise-aboard-uss-bataan) | `231221-N-OQ442-1897 U.S. 5TH FLEET AREA OF OPERATIONS (Dec. 21, 2023) Naval Air Crewman (Helicopter) 2nd Class Aiden Oakley, assigned to Helicopter Sea Combat Squadron 26, adjusts the front sights of a M-4 semi` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Wasp Passes Through The Strait Of Gibraltar ](https://www.dvidshub.net/image/8525689/wasp-passes-through-strait-gibraltar) | `240626-N-ME988-1053 STRAIT OF GIBRALTAR (June 26, 2024) Mass Communication Specialist Seaman Troy Davis, assigned to Amphibious Squadron 4, documents the transit of the amphibious assault ship USS Wasp (LHD 1) ` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Wasp Sailors Weld Aircraft Elevator During MDVR ](https://www.dvidshub.net/image/8697390/wasp-sailors-weld-aircraft-elevator-during-mdvr) | `241009-N-NT298-1339 LIMASSOL, Cyprus (Oct. 9, 2024) Hull Maintenance Technician 1st Class Aaron Patterson, assigned to the amphibious assault ship USS Wasp (LHD 1), welds struts on the ship’s port aircraft elev` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Iwo Jima Conducts Well Deck Operations ](https://www.dvidshub.net/image/9037885/uss-iwo-jima-conducts-well-deck-operations) | `ATLANTIC OCEAN (May 14, 2025) A landing craft air cushion, assigned to Assault Craft Unit (ACU) 4, approaches the well deck of the Wasp-class amphibious assault ship USS Iwo Jima (LHD 7) to dock and unload equi` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Landing Craft, Air Cushion 64 enters USS Makin Island (LHD 8) ](https://www.dvidshub.net/image/9305358/landing-craft-air-cushion-64-enters-uss-makin-island-lhd-8) | `Landing Craft, Air Cushion 64, assigned to Assault Craft Unit 5, prepares to enter the well deck of the Wasp-class amphibious ship USS Makin Island (LHD 8), Sept. 9, 2025. Makin Island is currently underway con` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=wasp+class+lhd+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=wasp+class+lhd+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=wasp+class+lhd+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=wasp+class+lhd+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=wasp+class+lhd+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=wasp+class+lhd+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=wasp+class+lhd+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- `unresolved`: no matching producer index was ready at integration. Keep collector pickup separate from image coverage.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.
<!-- NAVAL-CURRENT-END -->


---

<!-- NAVAL-CURRENT-START -->
# wasp-class-lhd — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:32:48.849695+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-LHD-1` | USS Wasp lists length 844 ft, beam 106 ft, draft 27 ft. Derived SI: approximately 257.25 m, 32.31 m, 8.23 m. The class page's 253.2 m and 31.8 m equivalents conflict with its feet; never silently copy those conversions. | [Primary source](https://www.surflant.usff.navy.mil/Organization/Operational-Forces/Amphibious-Ships/USS-WASP-LHD-1/About-Us/); General Characteristics |
| `sourced-Wasp-class-historical-fit` | LHD 1-7 have boiler/steam-turbine propulsion; LHD 8 has gas turbines and auxiliary propulsion motors. The class list gives three Phalanx mounts for LHD 1-4, two for LHD 5-8, and capacity for three LCACs or two LCUs. Present individual-hull fits need dated confirmation. | [Primary source](https://www.surflant.usff.navy.mil/Organization/Operational-Forces/Amphibious-Ships/Amphibious-Assault-Ship-LHD-LHA-Info-Page/); General Characteristics, Wasp Class |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| propeller/shaft assemblies | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| rudders | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| aircraft elevators | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| stern gate | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| identified radars and weapon mounts | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| davits | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Do not use two CIWS mounts as a universal class count. Preserve hull/date configuration and conflicting displacement/area tables. Draft future UTC timestamps are unverified worker claims. Do not equate no new motion contacts with clearance of inherited contacts.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [USS Bataan (LHD 5) ](https://www.dvidshub.net/image/3449831/uss-bataan-lhd-5) | `170604-N-HP188-0145 U.S. 5TH FLEET AREA OF OPERATIONS (June 4, 2017) The amphibious assault ship USS Bataan (LHD 5) pulls alongside the dry cargo and ammunition ship USNS Washington Chambers (T-AKE 11) during a` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Defense of the Amphibious Task Force (DATF) ](https://www.dvidshub.net/image/4779448/defense-amphibious-task-force-datf) | `SOUTH CHINA SEA (Sept. 27, 2018) - Sailors conduct a foreign object debris walk down prior to flight operations during a Defense of the Amphibious Task Force (DATF) drill on the flight deck of the amphibious as` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS WASP (LHD 1) OPERATIONS AT SEA ](https://www.dvidshub.net/image/5076063/uss-wasp-lhd-1-operations-sea) | `190203-N-OX029-2014 PHILIPPINE SEA (Feb. 3, 2019) - Marines disembark a Landing Craft, Air Cushion (LCAC) in the well deck of the amphibious assault ship USS Wasp (LHD 1). Wasp, flagship of the Wasp Amphibious ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Makin Island (LHD 8) Crane Operations ](https://www.dvidshub.net/image/5115473/uss-makin-island-lhd-8-crane-operations) | `190219-N-TF178-1053 SAN DIEGO (Feb. 19, 2019) Aviation Support Equipment Technician 2nd Class Leslie Bueso transports a dolly aboard the amphibious assault ship USS Makin Island (LHD 8) during crane operations.` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS WASP (LHD 1) OPERATIONS AT SEA ](https://www.dvidshub.net/image/5642357/uss-wasp-lhd-1-operations-sea) | `190803-N-RI884-1088 CORAL SEA (Aug. 3, 2019) – Fire Controlmen conduct routine maintenance checks on an MK-15 Phalanx close-in weapons system (CIWS) aboard the amphibious assault ship USS Wasp (LHD 1). Wasp, fl` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Wasp (LHD 1) Operations at Sea ](https://www.dvidshub.net/image/6436626/uss-wasp-lhd-1-operations-sea) | `201024-N-RI884-1010 NORFOLK (Oct. 24, 2020) Sailors stand watch on the starboard bridge wing aboard the amphibious assault ship USS Wasp (LHD 1) as the ship transits Naval Station Norfolk. Wasp is currently und` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Essex Conducts A Maintenance Period ](https://www.dvidshub.net/image/7667221/uss-essex-conducts-maintenance-period) | `SAN DIEGO (Feb. 28, 2023) Amphibious assault ship USS Essex (LHD 2) conducts a maintenance period in San Diego to upgrade and refurbish many key systems aboard, Feb. 28, 2023. The U.S. Navy takes a methodical a` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [TYCOM Sea Trials ](https://www.dvidshub.net/image/7713785/tycom-sea-trials) | `230330-N-OX029-3021 ATLANTIC OCEAN (March 30, 2023) – Sailors lower a rigid hull inflatable boat from the starboard side boat deck aboard the amphibious assault ship USS Wasp (LHD 1) during a man overboard dril` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Essex Recovers Starboard Anchor ](https://www.dvidshub.net/image/7743890/uss-essex-recovers-starboard-anchor) | `SAN DIEGO (April 12, 2023) The starboard chain and anchor aboard amphibious assault ship USS Essex (LHD 2) are hauled into the hawse pipe during an anchor recovery, April 12, 2023. Essex is dry docked in San Di` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [HSC 26 Sailors Execute a Live-Fire Exercise Aboard USS Bataan ](https://www.dvidshub.net/image/8185828/hsc-26-sailors-execute-live-fire-exercise-aboard-uss-bataan) | `231221-N-OQ442-1897 U.S. 5TH FLEET AREA OF OPERATIONS (Dec. 21, 2023) Naval Air Crewman (Helicopter) 2nd Class Aiden Oakley, assigned to Helicopter Sea Combat Squadron 26, adjusts the front sights of a M-4 semi` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Wasp Passes Through The Strait Of Gibraltar ](https://www.dvidshub.net/image/8525689/wasp-passes-through-strait-gibraltar) | `240626-N-ME988-1053 STRAIT OF GIBRALTAR (June 26, 2024) Mass Communication Specialist Seaman Troy Davis, assigned to Amphibious Squadron 4, documents the transit of the amphibious assault ship USS Wasp (LHD 1) ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Wasp Sailors Weld Aircraft Elevator During MDVR ](https://www.dvidshub.net/image/8697390/wasp-sailors-weld-aircraft-elevator-during-mdvr) | `241009-N-NT298-1339 LIMASSOL, Cyprus (Oct. 9, 2024) Hull Maintenance Technician 1st Class Aaron Patterson, assigned to the amphibious assault ship USS Wasp (LHD 1), welds struts on the ship’s port aircraft elev` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Iwo Jima Conducts Well Deck Operations ](https://www.dvidshub.net/image/9037885/uss-iwo-jima-conducts-well-deck-operations) | `ATLANTIC OCEAN (May 14, 2025) A landing craft air cushion, assigned to Assault Craft Unit (ACU) 4, approaches the well deck of the Wasp-class amphibious assault ship USS Iwo Jima (LHD 7) to dock and unload equi` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Landing Craft, Air Cushion 64 enters USS Makin Island (LHD 8) ](https://www.dvidshub.net/image/9305358/landing-craft-air-cushion-64-enters-uss-makin-island-lhd-8) | `Landing Craft, Air Cushion 64, assigned to Assault Craft Unit 5, prepares to enter the well deck of the Wasp-class amphibious ship USS Makin Island (LHD 8), Sept. 9, 2025. Makin Island is currently underway con` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=wasp+class+lhd+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=wasp+class+lhd+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=wasp+class+lhd+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=wasp+class+lhd+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=wasp+class+lhd+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=wasp+class+lhd+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=wasp+class+lhd+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- `unresolved`: no matching producer index was ready at integration. Keep collector pickup separate from image coverage.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.

Independent image-subject review correction: wrong-subject candidates excluded, duplicate image IDs collapsed, and sibling equipment separated above. Older revisions remain audit evidence and are superseded by this last current section.
<!-- NAVAL-CURRENT-END -->
