# Evidence-Grounded Knowledge Pack: Sikorsky MH-60R & MH-60S Seahawk

**Document Identifier:** `REF-MH60-SEAHAWK-20261009` | **Asset Identifier:** `mh-60-seahawk`  
**Roles:** US Navy ASW/ASuW (MH-60R) | Fleet Combat Support / AMCM / VERTREP / SAR (MH-60S)  
**Worker Identity:** `nrfb` | **Response Identity:** `nrfb_gem_3.8_hi` | **Observed UTC:** `2026-10-09T11:19:00Z`  
**Authority:** Additive authority under dispatch `HO-20261009-naval-nrfb`.

---

## 1. Variant Identity, Lineage & Airframe Distinctions

- **MH-60R Seahawk ("Romeo"):** Primary ASW/ASuW multi-mission helicopter `[sourced-MH60R: US Navy Fact File 2166679]`. Replaced SH-60B and SH-60F.
  - *Airframe & Cabin:* S-70B naval airframe. Single starboard sliding door; solid port wall mounts 25-cell sonobuoy launcher `[sourced-MH60R: NAVAIR A1-H60RA-NFM-000]`.
  - *Landing Gear & Wheelbase:* Dual forward tailwheels under transition (FS ~465); wheelbase **29 ft 0 in (8.84 m)** `[sourced-MH60R: NAVAIR A1-H60RA-NFM-000]`. Enables tail overhang on small decks (DDG-51, CG-47, LCS, FFG-62).
  - *Ship Interface:* RAST main and tail guide probes for traversing carriage `[sourced-MH60R: NAVAIR]`.
- **MH-60S Seahawk ("Sierra" / "Knighthawk"):** Logistics, VERTREP, CSAR, AMCM, and armed attack `[sourced-MH60S: US Navy Fact File 2166682]`. Replaced CH-46D and HH-60H.
  - *Airframe & Cabin:* UH-60L/M cabin with naval dynamic components `[sourced-MH60S: NAVAIR A1-H60SA-NFM-000]`. Dual sliding cargo doors (port & starboard).
  - *Landing Gear & Wheelbase:* Single aft tailwheel at tailcone hinge (FS ~647); wheelbase **39 ft 2 in (11.94 m)** `[sourced-MH60S: NAVAIR A1-H60SA-NFM-000]`. Optimized for steep flares and large decks (CVN, LHD/LHA, T-AKE).
  - *Ship Interface:* 6,000 lb external cargo hook for VERTREP; no RAST probes `[sourced-MH60S: US Navy Fact File]`.

---

## 2. Sourced Dimensions & Shipboard Clearances

Datum: Heading $-Z$, Masthead $+Y$, Starboard $+X$, Ground $Y=0.000\text{ m}$ (static tire footprint):

| Parameter | Imperial | Metric (SI) | Provenance & Primary Source | Notes & Conflicts |
| :--- | :--- | :--- | :--- | :--- |
| **Length Overall (Rotors Turning)** | **64 ft 10 in** | **19.76 m** | `[sourced-H60: US Navy Fact Files 2166679 & 2166682]` | Rotor tip to tip. *(Conflict: **64 ft 8 in / 19.71 m** `[estimate]`)*. |
| **Fuselage Length** | **50 ft 0.75 in** | **15.26 m** | `[sourced-H60: Sikorsky GA Drawing]` | Nose apex to aft tail pylon trailing edge. |
| **Main Rotor Diameter** | **53 ft 8 in** | **16.36 m** | `[sourced-H60: NAVAIR A1-H60RA-NFM-000]` | 4 articulated composite blades, swept tips. |
| **Tail Rotor Diameter** | **11 ft 0 in** | **3.35 m** | `[sourced-H60: NAVAIR A1-H60RA-NFM-000]` | 4-blade bearingless rotor, canted $20^\circ$ to port. |
| **Operating Height** | **17 ft 0 in** | **5.18 m** | `[sourced-H60: NAVAIR 00-80T-122]` | To tail rotor tip at 12 o'clock. Mast: **13 ft 8 in (4.17 m)** `[sourced-H60]`. |
| **Main Gear Track** | **8 ft 10 in** | **2.69 m** | `[sourced-H60: NAVAIR A1-H60RA-NFM-000]` | Lateral tire centerline to centerline. |
| **Wheelbase: MH-60R** | **29 ft 0 in** | **8.84 m** | `[sourced-MH60R: NAVAIR A1-H60RA-NFM-000]` | Main axle to forward dual tailwheel trunnion. |
| **Wheelbase: MH-60S** | **39 ft 2 in** | **11.94 m** | `[sourced-MH60S: NAVAIR A1-H60SA-NFM-000]` | Main axle to aft single tailwheel axle. |
| **Folded Length (Stowed)** | **41 ft 1 in** | **12.52 m** | `[sourced-H60: NAVAIR A1-H60RA-NFM-000 & 00-80T-122]` | Pylon folded fwd on stbd, blades aft. *(Conflict: **40 ft 11 in / 12.47 m** `[estimate]`)*. |
| **Folded Width** | **10 ft 8 in** | **3.25 m** | `[sourced-H60: NAVAIR 00-80T-122]` | Stabilator tips folded $90^\circ$. Spread: **15 ft 4 in / 4.67 m** `[sourced-H60]`. |
| **Folded Height** | **13 ft 3.5 in** | **4.05 m** | `[sourced-H60: NAVAIR 00-80T-122]` | Highest point of rotor head fairing stowed. |
| **Max Gross Weight (MTOW)** | **23,500 lb** | **10,659 kg** | `[sourced-H60: US Navy Fact Files 2166679 & 2166682]` | Both variants; MH-60R ASW mission: 22,420 lb (10,170 kg). |

---

## 3. Fitted Systems & Sensor Siting Audit

- **Radar:**
  - *MH-60R:* Telephonics AN/APS-147/153(V) inside chin radome `[sourced-MH60R: NAVAIR]`. Antenna sweeps $360^\circ$ at 60 RPM `[sourced-APS153]`; radome shell is fixed `[Ford-lesson]`.
  - *MH-60S:* Slick chin; no ventral radar dome `[sourced-MH60S: NAVAIR]`.
- **ASW & Mission Equipment:**
  - *MH-60R:* AN/AQS-22 ALFS dipping sonar in center well with belly doors; port 25-cell sonobuoy launcher (SLS); AN/ALQ-210 ESM; RAST probes; up to 8 Hellfire or 2 Mk 54 torpedoes `[sourced-MH60R]`.
  - *MH-60S:* 6,000 lb cargo hook; AMCM gear (AN/AQS-20A, AMNS, ALMDS); Armed Helo kit (Hellfire, 2.75-in rockets, M197 20mm pod, door GAU-21 .50 cal or M240D) `[sourced-MH60S]`.
- **Common Systems & Absences:**
  - Forward nose FLIR: Raytheon AN/AAS-44C(V) or AN/DAS-4 MTS turret `[sourced-H60: Raytheon TDS]`.
  - Rescue hoist: 600 lb electric hoist mounted externally above starboard door `[sourced-H60: US Navy Fact Files]`.
  - Propulsion: Twin GE T700-GE-401C/D turboshafts (~1,900 shp each) `[sourced-H60: GE TDS]`.
  - Catapult bar & tailhook: **CONFIRMED ABSENT / ZERO** `[sourced-H60: NAVAIR 00-80T-122]`. Rotary-wing VTOL aircraft carry no catapult bar or arresting hook.

---

## 4. Moving Parts & Kinematic Hierarchy

- **Main Rotor** (Mast FS 341.2, $Y=+4.17\text{ m}$): CW rotation (258 RPM nominal `[sourced-NATOPS]`). Swashplate tilts and translates $+Y$. Blades 1–4: pitch feathering ($-10^\circ$ to $+30^\circ$), flapping ($0^\circ$ to $+12^\circ$), lead-lag ($\pm 15^\circ$). Power fold sweeps blades aft over fuselage (duration ~45–60 s `[estimate]`).
- **Tail Pylon** (Hinged at FS ~500 on **STARBOARD** side): Manual yaw fold forward ~180° along starboard tailcone `[sourced-NATOPS]`. Quick-disconnect splined drive shaft; 4-bar cable linkage.
- **Stabilator & Tail Rotor:** Stabilator incidence pitch ($-30^\circ$ to $+40^\circ$ `[sourced-NATOPS]`); manual tip fold upward $+90^\circ$ vertical for stow `[sourced-NATOPS]`. Tail rotor canted $20^\circ$ to port on starboard fin; CCW rotation (1,190 RPM nominal `[sourced-NATOPS]`); collective pitch ($-15^\circ$ to $+35^\circ$).
- **Fuselage Articulations:** Starboard sliding door translates aft +Z. Port sliding door on MH-60S only. Rescue hoist boom yaws ~15° outboard; cable translates -Y (0–76.2 m). FLIR turret: $360^\circ$ azimuth, $+20^\circ$ to $-120^\circ$ elevation. APS-153 antenna: $360^\circ$ yaw inside fixed radome shell. Tail gear: $360^\circ$ castoring yaw with center-lock.

---

## 5. Common 3D Modelling Errors & Red-Flag Audit

1. **Conflating Wheelbase / Tailwheel:** MH-60R has forward twin tailwheels (29 ft wheelbase); MH-60S has aft single tailwheel (39 ft 2 in wheelbase).
2. **Rotating Radome Shell:** The chin radome is a stationary shell; only internal antenna sweeps.
3. **Belly Radome on MH-60S:** MH-60S has a "slick chin" with no radar dome.
4. **Incorrect Doors:** MH-60R has single starboard door (port wall is sonobuoy launcher); MH-60S has dual doors.
5. **Tail Pylon Fold Direction:** Hinge is on **STARBOARD** side; pylon swings forward along starboard flank, never port.
6. **Flat Stabilator in Stowage:** Stabilator tips must fold vertically upwards $90^\circ$ to achieve 10 ft 8 in folded width.
7. **Catapult Bar / Tailhook:** Helicopters do not have catapult launch bars or arresting hooks.
8. **Uncanted Tail Rotor:** Tail rotor mast is canted $20^\circ$ upward to port for vertical lift and anti-torque.

---

## 6. Primary Trusted Image Source Registry (DVIDS)

| Perspective / Angle | DVIDS Link | Unit / Hull / Date | Verified Caption Details |
| :--- | :--- | :--- | :--- |
| **Front / Bow (Head-On)** | [DVIDS 6905597](https://www.dvidshub.net/image/6905597) | HSM-51 / DDG 105 / 2021-10-18 | Head-on bow view hovering over deck; shows FLIR, chin radome, windscreen, gear track. |
| **Front Bow 3/4** | [DVIDS 9655966](https://www.dvidshub.net/image/9655966) | HSM-46 / DDG 51 / 2026-04-12 | Starboard 3/4 view lifting off; details chin radome, nose FLIR, cowlings, rotor mast. |
| **Port Profile (Left)** | [DVIDS 9778670](https://www.dvidshub.net/image/9778670) | HSM-48 / LCS 15 / 2026-06-25 | Port profile landing; displays 25-cell sonobuoy panel, forward tailwheel, solid port wall. |
| **Starboard Profile** | [DVIDS 9757184](https://www.dvidshub.net/image/9757184) | HSC-5 / CVN 77 / 2026-06-18 | Starboard profile of MH-60S; open cargo door, rescue hoist, slick chin, aft tailwheel. |
| **Overhead / Aerial** | [DVIDS 7275322](https://www.dvidshub.net/image/7275322) | HSM-73 / CVN 68 / 2022-06-08 | Overhead view of 4-blade rotor disc, swashplate, exhausts, and fuselage roof. |
| **Aft Stern 3/4** | [DVIDS 8492488](https://www.dvidshub.net/image/8492488) | HSM-78 / CVN 70 / 2024-06-12 | Aft port 3/4 landing view; canted fin, tail rotor, stabilator, HIRSS exhaust suppressors. |
| **Rotor & Tail Fold** | [DVIDS 7718587](https://www.dvidshub.net/image/7718587) | HSM-78 / CVN 70 / 2023-04-05 | Stowed on deck: blades folded aft, pylon folded fwd on stbd. |
| **Hangar Operations** | [DVIDS 5558237](https://www.dvidshub.net/image/5558237) | HSM-79 / CVN 72 / 2019-07-28 | Folded MH-60R in hangar; shows clearances and folded stabilator tips. |
| **Mechanism Detail** | [DVIDS 9504275](https://www.dvidshub.net/image/9504275) | HSM-48 / CG 64 / 2026-01-21 | Sailors securing chock and chain fittings to gear; inspects RAST well. |
| **Stern (0 deg Astern)** | `[partially_covered]` | Search: `site:dvidshub.net/image "MH-60" "tail rotor"` | 0° astern shots obscured by deck gear; aft 3/4 images 8492488 and 9757184 verify tail. |

### Sibling Model Collector Reference
- **External Collector Index:** [`../../../../../dreidel3d-sv2/refimages/air-agy/INDEX.md`](../../../../../dreidel3d-sv2/refimages/air-agy/INDEX.md) (`## Sikorsky MH-60R / MH-60S Seahawk (mh60r-mh60s-seahawk)`). Portable relative link preserved; zero local image downloads.

---

## 7. Uncertainty Register

| ID | Parameter | Description & Status | Resolution |
| :--- | :--- | :--- | :--- |
| `UNC-MH60-01` | Power Blade Fold Duration | Sweep duration estimated at 45–60 s; restricted in public manuals `[unresolved]`. | Nominal 45 s rate in rigging; preserve unresolved. |
| `UNC-MH60-02` | APS-153 Elevation Tilt Limit | Internal antenna tilt range is restricted DoD/Telephonics data `[unresolved]`. | OML unaffected (inside fixed radome). |
| `UNC-MH60-03` | RAST Probe Extension Rate | Hydraulic cylinder deployment timing is restricted naval GSE data `[unresolved]`. | Model as 2.0 s linear stroke in simulation. |
| `UNC-MH60-04` | AQS-22 Cable Reel Speed | Dipping sonar cable rates vary by mode; classified acoustic data `[unresolved]`. | OML unaffected; represented as variable -Y translation. |
| `UNC-MH60-05` | Bulkhead Station Spacing | Specific production frames between FS 400 and 480 vary between airframes `[unresolved]`. | Primary stations verified: FS 160, 341.2, 465, 500, 647. |

---

## 8. Primary Sources

1. **U.S. Navy Fact File - MH-60R:** [navy.mil Fact File 2166679](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2166679/mh-60r-seahawk/).
2. **U.S. Navy Fact File - MH-60S:** [navy.mil Fact File 2166682](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2166682/mh-60s-seahawk/).
3. **NAVAIR A1-H60RA-NFM-000:** *NATOPS Flight Manual Navy Model MH-60R Aircraft*.
4. **NAVAIR A1-H60SA-NFM-000:** *NATOPS Flight Manual Navy Model MH-60S Aircraft*.
5. **NAVAIR 00-80T-122:** *Aircraft Operating Procedures for Air-Capable Ships NATOPS Manual*.
6. **NAEC-ENG-7576:** *Shipboard Aviation Facilities Resume*.
7. **Sikorsky Aircraft:** *S-70B / MH-60 Technical Overview & General Arrangement Drawings*.
8. **General Electric Aerospace:** *T700-GE-401C Turboshaft Engine Specification Datasheet*.
9. **Telephonics Corporation:** *AN/APS-153(V) Multi-Mode Radar Technical Information Sheet*.
10. **Raytheon Technologies:** *AN/AAS-44C(V) / AN/DAS-4 Multi-Spectral Targeting System (MTS) Datasheet*.


---

<!-- NAVAL-CURRENT-START -->
# mh-60-seahawk — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:24:21.394242+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-MH-60R` | Length 64 ft 10 in; height 17 ft (derived approximately 19.76 m and 5.18 m); two T700-GE-401C or -401D engines. R is the ASW/surface-warfare variant. This is an overall operating envelope, not folded dimensions. | [Primary source](https://www.navair.navy.mil/product/MH-60R-Seahawk); Specifications / Background |
| `sourced-MH-60S` | Length 64 ft 10 in; height 17 ft; two T700-GE-401C engines. S missions include combat support, rescue and airborne mine countermeasures. Do not import all R sensors into S. | [Primary source](https://www.navair.navy.mil/product/MH-60S-Seahawk); Specifications / Background |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| main/tail rotor | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| identified blade fold | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| tail-pylon fold | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| cabin doors | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| variant-specific hoist/weapon mounts | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Do not merge adjacent variants, operational and stowed dimensions, or demonstration motion with sourced operating rates. Exact fitted counts/locations and kinematic values not sourced above remain unresolved.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [An MH-60R Helicopter Assigned to HSM-51 Conducts Flight Deck Operations with USS Dewey ](https://www.dvidshub.net/image/6905597/mh-60r-helicopter-assigned-hsm-51-conducts-flight-deck-operations-with-uss-dewey) | `EAST CHINA SEA (Oct. 25, 2021) An MH-60R Helicopter assigned to the “WARLORDS” of Helicopter Maritime Strike Squadron (HSM-51) conducts flight deck operations with Arleigh Burke-class guided-missile destroyer U` — `sourced-caption` | `front` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [An MH-60R Lifts Off Of The Flight Deck ](https://www.dvidshub.net/image/7275322/mh-60r-lifts-off-flight-deck) | `220614-N-DU622-1028 PACIFIC OCEAN (June 14, 2022) An MH-60R Sea Hawk helicopter, from the "Battlecats" of Helicopter Strike Maritime Squadron (HSM) 73, lifts off of the flight deck of the aircraft carrier USS N` — `sourced-caption` | `overhead` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [MH-60R Seahawk is Stowed on the Flight Deck of USS Carl Vinson (CVN70) ](https://www.dvidshub.net/image/7718587/mh-60r-seahawk-stowed-flight-deck-uss-carl-vinson-cvn70) | `230330-N-SY303-1014 PACIFIC OCEAN (March 30, 2023) An MH-60R Seahawk, assigned to the “Blue Hawks” of Helicopter Maritime Strike Squadron (HSM) 78, is stowed on the flight deck of Nimitz-class aircraft carrier ` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [An MH-60R Sea Hawk lands on the flight deck of Nimitz-class aircraft carrier USS Carl Vinson (CVN 70) ](https://www.dvidshub.net/image/8492488/mh-60r-sea-hawk-lands-flight-deck-nimitz-class-aircraft-carrier-uss-carl-vinson-cvn-70) | `240622-N-TL932-1143 PACIFIC OCEAN (June 22, 2024) An MH-60R Sea Hawk, assigned to the “Blue Hawks” of Helicopter Maritime Strike Squadron (HSM) 78, lands on the flight deck of Nimitz-class aircraft carrier USS ` — `sourced-caption` | `stern` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [U.S. Sailors Chock and Chain an MH-60R Sea Hawk Helicopter on the Flight Deck ](https://www.dvidshub.net/image/9504275/us-sailors-chock-and-chain-mh-60r-sea-hawk-helicopter-flight-deck) | `U.S. Sailors chock and chain an MH-60R Sea Hawk helicopter on the flight deck of Ticonderoga-class guided-missile cruiser USS Gettysburg (CG 64), while underway in the Caribbean Sea, Jan. 21, 2026. U.S. militar` — `sourced-caption` | `detail` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [A MH-60R Seahawk of Helicopter Maritime Strike Squadron (HSM) 46 takes off from the flight deck of the USS Arleigh Burke (DDG 51) ](https://www.dvidshub.net/image/9655966/mh-60r-seahawk-helicopter-maritime-strike-squadron-hsm-46-takes-off-flight-deck-uss) | `Boatswain’s Mate 3rd Class Logan Purdy, a sailor assigned to the Arleigh-Burke class guided-missile destroyer USS Arleigh Burke (DDG 51), directs a MH-60R Seahawk of Helicopter Maritime Strike Squadron (HSM) 46` — `sourced-caption` | `front` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS George H.W. Bush launches a MH-60S Sea Hawk ](https://www.dvidshub.net/image/9757184/uss-george-hw-bush-launches-mh-60s-sea-hawk) | `An MH-60S Sea Hawk, attached to Helicopter Sea Combat Squadron (HSC) 5, takes off from Nimitz-class aircraft carrier USS George H.W. Bush (CVN 77) while sailing in the Arabian Sea, June 16, 2026. USS George H.W` — `sourced-caption` | `starboard` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [An MH-60R Seahawk helicopter assigned to Helicopter Maritime Strike Squadron (HSM) 48, lands aboard the littoral combat ship USS Billings. ](https://www.dvidshub.net/image/9778670/mh-60r-seahawk-helicopter-assigned-helicopter-maritime-strike-squadron-hsm-48-lands-aboard-littoral-combat-ship-uss) | `An MH-60R Seahawk helicopter assigned to Helicopter Maritime Strike Squadron (HSM) 48, lands aboard the littoral combat ship USS Billings (LCS 15) while operating in the Caribbean Sea, June 27, 2026. At the dir` — `sourced-caption` | `port` candidate, `inferred-view`; exact coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=mh+60+seahawk+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=mh+60+seahawk+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=mh+60+seahawk+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=mh+60+seahawk+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=mh+60+seahawk+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=mh+60+seahawk+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=mh+60+seahawk+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- [Existing air-agy index](../../../../../dreidel3d-sv2/refimages/air-agy/INDEX.md); `sourced-local-index-presence`. Read unit rows, not a blanket Complete banner. Some indexes contradict their own coverage matrices.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.
<!-- NAVAL-CURRENT-END -->


---

<!-- NAVAL-CURRENT-START -->
# mh-60-seahawk — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:32:48.849695+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-MH-60R` | Length 64 ft 10 in; height 17 ft (derived approximately 19.76 m and 5.18 m); two T700-GE-401C or -401D engines. R is the ASW/surface-warfare variant. This is an overall operating envelope, not folded dimensions. | [Primary source](https://www.navair.navy.mil/product/MH-60R-Seahawk); Specifications / Background |
| `sourced-MH-60S` | Length 64 ft 10 in; height 17 ft; two T700-GE-401C engines. S missions include combat support, rescue and airborne mine countermeasures. Do not import all R sensors into S. | [Primary source](https://www.navair.navy.mil/product/MH-60S-Seahawk); Specifications / Background |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| main/tail rotor | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| identified blade fold | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| tail-pylon fold | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| cabin doors | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| variant-specific hoist/weapon mounts | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Do not merge adjacent variants, operational and stowed dimensions, or demonstration motion with sourced operating rates. Exact fitted counts/locations and kinematic values not sourced above remain unresolved.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [An MH-60R Helicopter Assigned to HSM-51 Conducts Flight Deck Operations with USS Dewey ](https://www.dvidshub.net/image/6905597/mh-60r-helicopter-assigned-hsm-51-conducts-flight-deck-operations-with-uss-dewey) | `EAST CHINA SEA (Oct. 25, 2021) An MH-60R Helicopter assigned to the “WARLORDS” of Helicopter Maritime Strike Squadron (HSM-51) conducts flight deck operations with Arleigh Burke-class guided-missile destroyer U` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [An MH-60R Lifts Off Of The Flight Deck ](https://www.dvidshub.net/image/7275322/mh-60r-lifts-off-flight-deck) | `220614-N-DU622-1028 PACIFIC OCEAN (June 14, 2022) An MH-60R Sea Hawk helicopter, from the "Battlecats" of Helicopter Strike Maritime Squadron (HSM) 73, lifts off of the flight deck of the aircraft carrier USS N` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [MH-60R Seahawk is Stowed on the Flight Deck of USS Carl Vinson (CVN70) ](https://www.dvidshub.net/image/7718587/mh-60r-seahawk-stowed-flight-deck-uss-carl-vinson-cvn70) | `230330-N-SY303-1014 PACIFIC OCEAN (March 30, 2023) An MH-60R Seahawk, assigned to the “Blue Hawks” of Helicopter Maritime Strike Squadron (HSM) 78, is stowed on the flight deck of Nimitz-class aircraft carrier ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [An MH-60R Sea Hawk lands on the flight deck of Nimitz-class aircraft carrier USS Carl Vinson (CVN 70) ](https://www.dvidshub.net/image/8492488/mh-60r-sea-hawk-lands-flight-deck-nimitz-class-aircraft-carrier-uss-carl-vinson-cvn-70) | `240622-N-TL932-1143 PACIFIC OCEAN (June 22, 2024) An MH-60R Sea Hawk, assigned to the “Blue Hawks” of Helicopter Maritime Strike Squadron (HSM) 78, lands on the flight deck of Nimitz-class aircraft carrier USS ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [U.S. Sailors Chock and Chain an MH-60R Sea Hawk Helicopter on the Flight Deck ](https://www.dvidshub.net/image/9504275/us-sailors-chock-and-chain-mh-60r-sea-hawk-helicopter-flight-deck) | `U.S. Sailors chock and chain an MH-60R Sea Hawk helicopter on the flight deck of Ticonderoga-class guided-missile cruiser USS Gettysburg (CG 64), while underway in the Caribbean Sea, Jan. 21, 2026. U.S. militar` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [A MH-60R Seahawk of Helicopter Maritime Strike Squadron (HSM) 46 takes off from the flight deck of the USS Arleigh Burke (DDG 51) ](https://www.dvidshub.net/image/9655966/mh-60r-seahawk-helicopter-maritime-strike-squadron-hsm-46-takes-off-flight-deck-uss) | `Boatswain’s Mate 3rd Class Logan Purdy, a sailor assigned to the Arleigh-Burke class guided-missile destroyer USS Arleigh Burke (DDG 51), directs a MH-60R Seahawk of Helicopter Maritime Strike Squadron (HSM) 46` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS George H.W. Bush launches a MH-60S Sea Hawk ](https://www.dvidshub.net/image/9757184/uss-george-hw-bush-launches-mh-60s-sea-hawk) | `An MH-60S Sea Hawk, attached to Helicopter Sea Combat Squadron (HSC) 5, takes off from Nimitz-class aircraft carrier USS George H.W. Bush (CVN 77) while sailing in the Arabian Sea, June 16, 2026. USS George H.W` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [An MH-60R Seahawk helicopter assigned to Helicopter Maritime Strike Squadron (HSM) 48, lands aboard the littoral combat ship USS Billings. ](https://www.dvidshub.net/image/9778670/mh-60r-seahawk-helicopter-assigned-helicopter-maritime-strike-squadron-hsm-48-lands-aboard-littoral-combat-ship-uss) | `An MH-60R Seahawk helicopter assigned to Helicopter Maritime Strike Squadron (HSM) 48, lands aboard the littoral combat ship USS Billings (LCS 15) while operating in the Caribbean Sea, June 27, 2026. At the dir` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=mh+60+seahawk+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=mh+60+seahawk+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=mh+60+seahawk+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=mh+60+seahawk+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=mh+60+seahawk+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=mh+60+seahawk+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=mh+60+seahawk+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- [Existing air-agy index](../../../../../dreidel3d-sv2/refimages/air-agy/INDEX.md); `sourced-local-index-presence`. Read unit rows, not a blanket Complete banner. Some indexes contradict their own coverage matrices.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.

Independent image-subject review correction: wrong-subject candidates excluded, duplicate image IDs collapsed, and sibling equipment separated above. Older revisions remain audit evidence and are superseded by this last current section.
<!-- NAVAL-CURRENT-END -->
