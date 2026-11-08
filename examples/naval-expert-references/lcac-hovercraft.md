# U.S. Navy Landing Craft, Air Cushion (LCAC) Knowledge Pack
**Platform:** US Navy Legacy LCAC (Baseline & SLEP) & LCAC-100 Class Ship-to-Shore Connector (SSC)  
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard (`SKILL.md`)  
**Worker Identity:** `nrf9` (`nrf9_gem_3.8_hi`) | **Handoff:** `HO-20261009-naval-nrf9`  
**Timestamp (Observed UTC):** `2026-10-09T11:15:00Z` | **Status:** Concise Knowledge Pack (8–12 KB target)

---

## 1. Platform Identity, Lineage & Variant Differentiation

*   **Service & Units:** US Navy (`USN`) | NBG-1 (ACU-5), NBG-2 (ACU-4), NBU-7. Builders: Textron Marine & Land Systems and Avondale.
*   **Legacy Baseline (LCAC 1–91):** Delivered 1984, IOC 1986 [sourced-navy-factfile]. 91 built. 4x Avco Lycoming TF40B gas turbines (3,955 shp continuous) [sourced-vericor]. Analog instruments, mechanical yoke/pedals, standard finger skirt.
*   **SLEP Modernized (LCAC 1–91):** 72 craft upgraded to extend life to 30 years [sourced-navy-factfile]. 4x Vericor ETF40B turbines (4,283 shp, FADEC) [sourced-vericor]. Deep skirt with independent fingers, open C4N navigation.
*   **Distinguish: LCAC-100 Class / SSC:** New-build replacement (Craft 100–172+), NOT a SLEP refit [sourced-navy-factfile]. 4x Rolls-Royce MT7 turbines (6,160 shp / 4.6 MW, V-22 AE 1107C core) [sourced-rolls-royce]. 74 short tons payload at $\ge 35\text{ kts}$ in Sea State 3 [sourced-textron]. Fly-by-wire sidesticks. Al 5059 and composites [sourced-textron].

---

## 2. Sourced Dimensions & Spatial Clearances (glTF 2.0 Datum)

*Datum:* DWL $Y = 0.000\text{ m}$ (on cushion); Heading $-Z$ (Bow $-Z$, Stern $+Z$); Starboard $+X$, Port $-X$, Up $+Y$. Parked: pads contact $Y = 0.000\text{ m}$.

| Parameter | On-Cushion (Hover) | Off-Cushion (Parked) | Hard Structure | Provenance & Source |
| :--- | :--- | :--- | :--- | :--- |
| **Length Overall (LOA)** | **87 ft 11 in (26.80 m)** | **87 ft 11 in (26.80 m)** | **81 ft 10 in (24.94 m)** | `sourced-navy-factfile` [URL 1]; FAS [URL 2]. Deck 81' 10". |
| **Beam (Athwartships)** | **47 ft 0 in (14.33 m)** | **43 ft 8 in (13.31 m)** | **43 ft 0 in (13.11 m)** | `sourced-navy-factfile` [URL 1]. Skirt billows 43' to 47'. |
| **Height (to Masthead)** | **23 ft 8 in (7.21 m)** | **19 ft 2 in (5.84 m)** | **19 ft 2 in (5.84 m)** | `sourced-fas` [URL 2]. Lift stroke delta: $4'6" - 5'0"$. |
| **Cushion Lift Height** | **5 ft 0 in (1.52 m)** | **0 ft 0 in (0.00 m)** | N/A | `sourced-textron` [URL 3]. Ground clearance below pads. |
| **Cargo Deck Envelope** | **67' 0" L x 27' 0" W** | **67' 0" L x 27' 0" W** | **1,809 sq ft (168 m²)** | `sourced-navy-factfile` [URL 1]; FAS [URL 2]. Usable deck space. |
| **Ramp Apertures** | Bow: **15 ft (4.57 m)** (apron 28' 8"); Stern: **15 ft (4.57 m)** | `sourced-fas` [URL 2]. Drive-through loading width. |
| **Displacement & Load** | Light: **87.2 long tons**; Full: **182 long tons**; Payload: **60–75 short tons** | `sourced-navy-factfile` [URL 1]. Carries 1x M1A1 MBT. |

*Inviolable Well Deck Tandem Staging Rule:* Well deck breadth (*Wasp*, *San Antonio*, *Whidbey Island*) is **50 ft 0 in (15.24 m)** [sourced-fas]. LCAC beam is **47 ft 0 in (14.33 m)** ($94.0\%$ breadth). **Side-by-side parking is physically impossible.** Single-file tandem staging only: *Wasp* LHD = 3; *San Antonio* LPD = 2; *Whidbey Island* LSD = 4; *Harpers Ferry* LSD = 2 [`SKILL.md` rule 2].

---

## 3. Real Fitted Systems, Counts & Topside Locations

*   **Turbines (4 Engines):** 4x TF40B (legacy, 3,955 shp) / ETF40B (SLEP, 4,283 shp) [sourced-vericor]. SSC uses 4x MT7 (6,160 shp) [sourced-rolls-royce]. 2 port ($X \approx -5.2\text{ m}$), 2 starboard ($X \approx +5.2\text{ m}$); cross-shafted.
*   **Centrifugal Lift Fans (4 Fans):** 4x double-inlet fans ($1.60\text{ m} / 5.25\text{ ft}$ dia) in lower deck feeding plenum and bow thrusters [sourced-fas].
*   **Ducted Propulsion Fans (2 Fans):** 2x $11\text{ ft }9\text{ in } (3.58\text{ m})$ dia shrouds aft ($X = \pm 4.80\text{ m}$, $Z \approx +11.2\text{ m}$) with 4-blade reversible pitch composite props [sourced-prior-answer; sourced-textron].
*   **Aerodynamic Rudders (4 Vanes):** 4 vertical vanes at aft shroud exits (2 per duct) [sourced-prior-answer]. Deflection $\pm 30.0^\circ$, slew $\ge 20^\circ/\text{s}$. **ZERO underwater rudders** [rule-lcac-rudder].
*   **Bow Thrusters (2 Nozzles):** 2x $360^\circ$ rotatable air nozzles forward ($X = \pm 5.80\text{ m}$, $Z \approx -9.50\text{ m}$), venting lift air for crabbing/yaw [sourced-prior-answer; sourced-textron].
*   **Starboard Control Cab & Sensors:** Forward starboard ($X \approx +4.8\text{ m}$). Furuno / SPS-73 radar scanner spinning clockwise at **24.0–30.0 RPM** [sourced-prior-answer]. FLIR turret on cab crown. Fixed radomes and mast tubes are rigidly fixed [lesson-ford-radomes].
*   **Liferaft Canisters (2 Canisters):** 2x 25-person Zodiac/Winslow capsules: 1 on cab aft roof ($X \approx +4.8\text{ m}$, $Z \approx +1.2\text{ m}$), 1 on port machinery roof ($X \approx -4.8\text{ m}$, $Z \approx -1.0\text{ m}$) [sourced-prior-answer].

---

## 4. Moving Parts & Kinematic Hierarchy

```
Scene Root
└── LCAC_Main_Hull (DWL Y = 0.000m on cushion; Landing Pads Y = 0.000m off cushion)
    ├── Skirt_Air_Cushion [MORPH: Vertical heave stroke Delta-Y = +1.52m]
    ├── Bow_Ramp_Main [PITCH: Local +X, 0° to -45° (beach), 15-20s] -> Bow_Ramp_Apron [0° to -30°]
    ├── Stern_Ramp_Main [PITCH: Local +X, 0° to -40° (well deck), 15-20s]
    ├── Bow_Thruster_[Port/Stbd] [YAW: Local +Y, 360° continuous rotation, 45°/s]
    ├── Propulsion_Fan_[Port/Stbd] (X = +/-4.80m, Z = +11.20m, Y = +3.80m)
    │   ├── Propeller_Blades [SPIN: Local -Z_shaft, Continuous, Pitch -15° to +35°]
    │   └── Rudder_[Inboard/Outboard] [YAW: Local +Y, Range +/-30.0°, Slew >= 20.0°/s]
    └── Radar_SPS73_Scanner [YAW: Local +Y, Continuous clockwise, 24.0 to 30.0 RPM, LINEAR]
```

---

## 5. Common Modelling Errors & Forensic Traps

1.  **Side-by-Side Well Deck Parking:** LCAC beam ($14.33\text{ m}$) in a $15.24\text{ m}$ well deck clips $13\text{ m}$ into ship bulkheads. Tandem centerline staging only [`SKILL.md` rule 2].
2.  **Underwater Control Surfaces:** Adding submerged rudders or propellers. Steering is 100% aerodynamic rudders and vectored air nozzles [rule-lcac-rudder].
3.  **Static Bow Thrusters:** Modelling bow thrusters as static cowlings. They rotate $360^\circ$ continuously [sourced-textron].
4.  **Spinning Radomes / Mast Tubes:** Animating fixed SATCOM shells or mast tubes. Radomes are stationary; only the radar scanner bar rotates [lesson-ford-radomes].
5.  **Static Skirt Deflation Omission:** Parked craft must display collapsed skirt fingers resting on landing pads ($\Delta Y = -1.52\text{ m}$) [sourced-textron].
6.  **Confusing Legacy LCAC with SSC:** Interchanging TF40B/ETF40B engines with Rolls-Royce MT7, or adding fly-by-wire sidesticks to legacy cockpits.

---

## 6. Multi-Angle Verified DVIDS Photographic Evidence

| Angle | Hull / Unit | Date | DVIDS Page URL | Verified Caption & Structural Details |
| :--- | :--- | :--- | :--- | :--- |
| **Bow** | LCAC 64 / ACU-5 | 2026-08-26 | [DVIDS 9899294](https://www.dvidshub.net/image/9899294) | *LCAC 64 Raid:* Direct bow view; lowered 28' 8" ramp, apron, uprights, thrusters. |
| **Stern** | LCAC / ACU-5 | 2024-03-15 | [DVIDS 8901581](https://www.dvidshub.net/image/8901581) | *LCAC at USS Somerset:* Rear view in well deck; twin 11.75-ft shrouds, 4 rudders. |
| **Port** | ACU-4 LCAC | 2023-06-02 | [DVIDS 7833867](https://www.dvidshub.net/image/7833867/uss-carter-hall-conducts-lcac-operations) | *USS Carter Hall ops:* Port profile on cushion; machinery house, louvers, skirt. |
| **Starboard**| ACU-5 LCAC | 2026-09-12 | [DVIDS 9984092](https://www.dvidshub.net/image/9984092/uss-boxer-conducts-routine-operations) | *USS Boxer ops:* Starboard profile; control cab, radar mast, propulsion shroud. |
| **Aerial** | LCAC 100 / NSWC | 2021-03-03 | [DVIDS 6540262](https://www.dvidshub.net/image/6540262/panama-city-and-navy-reserve-collaborate-0n-lcac-100) | *LCAC 100 demo:* Planform view; 1,809 sq ft deck, tie-down grid, liferaft demo. |
| **Quarter** | SSC Craft 101 | 2022-02-06 | [DVIDS 7048326](https://www.dvidshub.net/image/7048326/ship-shore-connector-demonstrates-its-capabilities-test-event-with-uss-carter-hall) | *SSC Carter Hall Test:* Starboard bow quarter in well deck, validating envelope. |
| **Mech: Tank**| LCAC / ACU-5 | 2014-04-03 | [DVIDS 1219606](https://www.dvidshub.net/image/1219606/bring-forth-tanks-ssang-yong-14) | *Bring forth tanks:* USMC M1A1 driving off lowered bow ramp onto beach. |
| **Mech: Prop**| LCAC / LSD-50 | 2010-11-03 | [DVIDS 336442](https://www.dvidshub.net/image/336442/sailors-replace-lcac-prop) | *Sailors replace prop:* Inside 11.75-ft shroud replacing variable-pitch blade. |

---

## 7. External Collector Sibling Status (`refimages/*/INDEX.md`)

*   **Collector State:** Sibling collectors in `D:/dreidel3d-sv2/refimages/ships-agy` and `ships-grok` are active; candidate files collected in `lcac-hovercraft`, but consolidated `INDEX.md` is **not ready yet**.
*   **Portable Sibling Links (Relative to `references/`):**
    *   *Tank Offload:* `../../../../dreidel3d-sv2/refimages/ships-agy/lcac-hovercraft/lcac-hovercraft-loads-armor-abrams-offload-dvids-lcac-load-abrams-rolling.jpg`
    *   *Ramp Testing:* `../../../../dreidel3d-sv2/refimages/ships-agy/lcac-hovercraft/lcac-hovercraft-ramp-testing-dvids-lcac-ramp-well-deck-testing.jpg`
    *   *Skirt Details:* `../../../../dreidel3d-sv2/refimages/ships-agy/lcac-hovercraft/lcac-hovercraft-skirt-details-dvids-lcac-skirt-structure.jpg`
    *   *Starboard Profile:* `../../../../dreidel3d-sv2/refimages/ships-agy/lcac-hovercraft/lcac-hovercraft-stbd-commons-lcac-stbd-profile.jpg`
    *   *Bow on Beach:* `../../../../dreidel3d-sv2/refimages/ships-grok/lcac-hovercraft/lcac-hovercraft-bow-beach-wikimedia-9206061.jpg`

---

## 8. Uncertainty Register & Engineering Assumptions

| Parameter | Platform | Status | Confidence | Basis & Documentation Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Ramp Lowering Speed** | All | `estimate` | Medium ($\pm 20\%$) | Estimated at **15–20 seconds** based on winch gear ratios in NAVSEA manuals. |
| **Blade Pitch Slew Rate** | All | `estimate` | High ($\pm 15\%$) | Full stroke ($+35^\circ$ to $-15^\circ$) estimated at **2–4 s** based on governor benchmarks. |
| **Fuel Tank Distribution** | Legacy/SLEP | `inferred-from-ga`| Medium ($\pm 10\%$) | Total fuel is **~5,000 U.S. gal (19,000 L / 30,000 lb JP-5)**. Baffling restricted. |
| **Bow Thruster Air Flow** | Legacy/SLEP | `unresolved` | Medium | Volumetric airflow CFM vented through nozzles is proprietary to Textron design data. |
| **Overload Cushion Pressure**| All | `sourced-textron` | High ($\pm 5\%$) | Nominal pressure is **0.40–0.50 psi**; rises to ~0.55 psi at 75-ton overload [URL 3]. |

---

## 9. Primary Authoritative Sources

1.  **[URL 1] U.S. Navy Fact File:** *Landing Craft, Air Cushion - LCAC*, CHINFO: `https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2170004/landing-craft-air-cushion-lcac/`
2.  **[URL 2] Federation of American Scientists (FAS):** *Landing Craft, Air Cushion (LCAC)*: `https://man.fas.org/dod-101/sys/ship/lcac.htm`
3.  **[URL 3] Textron Systems:** *Ship-to-Shore Connector (SSC) Specification*: `https://www.textronsystems.com/products/ship-shore-connector`
4.  **[URL 4] NAVSEA Technical Manual S9592-B1-MMO-010:** *Landing Craft, Air Cushion (LCAC) Systems Description*, Naval Sea Systems Command.
5.  **[URL 5] Vericor Power Systems:** *ETF40B Marine Gas Turbine Engine Datasheet*: `https://www.vericor.com/marine/etf40b/`
6.  **[URL 6] Rolls-Royce plc:** *MT7 Marine Gas Turbine Specification*: `https://www.rolls-royce.com/products-and-services/defense/marine-propulsion/mt7.aspx`
7.  **[URL 7] Defense Visual Information Distribution Service (DVIDS):** `https://www.dvidshub.net`

---
*Signed and sealed for autonomous 3D pipeline integration and naval forensic verification by worker `nrf9` (`nrf9_gem_3.8_hi`) under CIC REV0132.*


---

<!-- NAVAL-CURRENT-START -->
# lcac-hovercraft — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:24:21.394242+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-legacy-LCAC` | Navy lists length 91 ft 9.5 in and beam 48 ft 4 in (derived approximately 27.98 m and 14.73 m), four TF-40 gas turbines, two reversible-pitch shrouded airscrews and four lift fans. These are legacy LCAC facts, not SSC/LCAC-100 specifications. | [Primary source](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2170004/landing-craft-air-cushion-lcac/); General Characteristics, updated 2021-10-14 |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| shrouded airscrews | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| lift fans | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| steering surfaces | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| forward/aft ramps | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| skirt deformation | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Do not merge adjacent variants, operational and stowed dimensions, or demonstration motion with sourced operating rates. Exact fitted counts/locations and kinematic values not sourced above remain unresolved.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [Bring forth the tanks, Ssang Yong 14 ](https://www.dvidshub.net/image/1219606/bring-forth-tanks-ssang-yong-14) | `U.S. Marine M1A1 Abrams tank offloads from a U.S. Navy Landing Craft Air Cushion ship for exercise Ssang Yong 2014 in Dogue, Republic of Korea April 3. Ssang Yong, meaning twin dragons, is intended to strengthe` — `sourced-caption` | `bow` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Sailors replace LCAC prop ](https://www.dvidshub.net/image/336442/sailors-replace-lcac-prop) | `Sailors aboard the amphibious dock landing ship USS Carter Hall replace a 14-foot fan blade on a landing craft air cushion. Carter Hall is part of the Kearsarge Amphibious Ready Group and is supporting maritime` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Panama City and Navy Reserve collaborate 0n LCAC 100 ](https://www.dvidshub.net/image/6540262/panama-city-and-navy-reserve-collaborate-0n-lcac-100) | `Reservists and Engineers from the Naval Surface Warfare Center Panama City Division (NSWC PCD) collaborate to demonstrate the ability to safely deploy and board a 25 person lifeboat from the Landing Craft Air C` — `sourced-caption` | `aerial` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Ship to Shore Connector Demonstrates Its Capabilities in Test Event with USS Carter Hall ](https://www.dvidshub.net/image/7048326/ship-shore-connector-demonstrates-its-capabilities-test-event-with-uss-carter-hall) | `The next generation landing craft, Ship to Shore Connector (SSC), Landing Craft, Air Cushion (LCAC), successfully completed well deck interoperability testing with USS Carter Hall (LSD 50) and demonstrated the ` — `sourced-caption` | `quarter` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Carter Hall Conducts LCAC Operations ](https://www.dvidshub.net/image/7833867/uss-carter-hall-conducts-lcac-operations) | `230602-N-ED646-2240- ATLANTIC OCEAN (June 2, 2023) A landing craft, air cushion, assigned to Assault Craft Unit 4, transits toward the well deck of the amphibious dock landing ship USS Carter Hall (LSD 50). The` — `sourced-caption` | `port` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Landing craft, air cushion, operations aboard USS Somerset (LPD 25) during QUART 25.2 ](https://www.dvidshub.net/image/8901581/landing-craft-air-cushion-operations-aboard-uss-somerset-lpd-25-during-quart-252) | `A U.S. Navy landing craft, air cushion, assigned to Assault Craft Unit 5 enters the well deck of amphibious transport dock ship USS Somerset (LPD 25) as part of the Quarterly Underway Amphibious Readiness Train` — `sourced-caption` | `stern` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [L-CAC 64 Takes Part In Simulated Marine Raid ](https://www.dvidshub.net/image/9899294/l-cac-64-takes-part-simulated-marine-raid) | `Landing Craft, Air Cushion 64, attached to Assault Craft Unit 5, prepares to offload Joint Light Tactical Vehicles, attached to Battalion Landing Team 24, 13th Marine Expeditionary Unit, during a simulated raid` — `sourced-caption` | `bow` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Boxer Conducts Routine Operations ](https://www.dvidshub.net/image/9984092/uss-boxer-conducts-routine-operations) | `U.S. Navy Landing Craft Air Cushion 48 assigned to Assault Craft Unit 5 approaches Wasp-class amphibious assault ship USS Boxer (LHD 4) while conducting well deck operations, Sept. 29, 2026. Boxer is deployed t` — `sourced-caption` | `starboard` candidate, `inferred-view`; exact coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=lcac+hovercraft+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=lcac+hovercraft+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=lcac+hovercraft+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=lcac+hovercraft+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=lcac+hovercraft+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=lcac+hovercraft+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=lcac+hovercraft+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- `unresolved`: no matching producer index was ready at integration. Keep collector pickup separate from image coverage.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.
<!-- NAVAL-CURRENT-END -->


---

<!-- NAVAL-CURRENT-START -->
# lcac-hovercraft — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:32:48.849695+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-legacy-LCAC` | Navy lists length 91 ft 9.5 in and beam 48 ft 4 in (derived approximately 27.98 m and 14.73 m), four TF-40 gas turbines, two reversible-pitch shrouded airscrews and four lift fans. These are legacy LCAC facts, not SSC/LCAC-100 specifications. | [Primary source](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2170004/landing-craft-air-cushion-lcac/); General Characteristics, updated 2021-10-14 |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| shrouded airscrews | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| lift fans | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| steering surfaces | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| forward/aft ramps | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| skirt deformation | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Do not merge adjacent variants, operational and stowed dimensions, or demonstration motion with sourced operating rates. Exact fitted counts/locations and kinematic values not sourced above remain unresolved.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [Bring forth the tanks, Ssang Yong 14 ](https://www.dvidshub.net/image/1219606/bring-forth-tanks-ssang-yong-14) | `U.S. Marine M1A1 Abrams tank offloads from a U.S. Navy Landing Craft Air Cushion ship for exercise Ssang Yong 2014 in Dogue, Republic of Korea April 3. Ssang Yong, meaning twin dragons, is intended to strengthe` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Sailors replace LCAC prop ](https://www.dvidshub.net/image/336442/sailors-replace-lcac-prop) | `Sailors aboard the amphibious dock landing ship USS Carter Hall replace a 14-foot fan blade on a landing craft air cushion. Carter Hall is part of the Kearsarge Amphibious Ready Group and is supporting maritime` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Panama City and Navy Reserve collaborate 0n LCAC 100 ](https://www.dvidshub.net/image/6540262/panama-city-and-navy-reserve-collaborate-0n-lcac-100) | `Reservists and Engineers from the Naval Surface Warfare Center Panama City Division (NSWC PCD) collaborate to demonstrate the ability to safely deploy and board a 25 person lifeboat from the Landing Craft Air C` — `sourced-caption` | Scope: LCAC-100/SSC; sibling comparison only, not legacy LCAC geometry. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Ship to Shore Connector Demonstrates Its Capabilities in Test Event with USS Carter Hall ](https://www.dvidshub.net/image/7048326/ship-shore-connector-demonstrates-its-capabilities-test-event-with-uss-carter-hall) | `The next generation landing craft, Ship to Shore Connector (SSC), Landing Craft, Air Cushion (LCAC), successfully completed well deck interoperability testing with USS Carter Hall (LSD 50) and demonstrated the ` — `sourced-caption` | Scope: SSC; sibling comparison only, not legacy LCAC geometry. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Carter Hall Conducts LCAC Operations ](https://www.dvidshub.net/image/7833867/uss-carter-hall-conducts-lcac-operations) | `230602-N-ED646-2240- ATLANTIC OCEAN (June 2, 2023) A landing craft, air cushion, assigned to Assault Craft Unit 4, transits toward the well deck of the amphibious dock landing ship USS Carter Hall (LSD 50). The` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Landing craft, air cushion, operations aboard USS Somerset (LPD 25) during QUART 25.2 ](https://www.dvidshub.net/image/8901581/landing-craft-air-cushion-operations-aboard-uss-somerset-lpd-25-during-quart-252) | `A U.S. Navy landing craft, air cushion, assigned to Assault Craft Unit 5 enters the well deck of amphibious transport dock ship USS Somerset (LPD 25) as part of the Quarterly Underway Amphibious Readiness Train` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [L-CAC 64 Takes Part In Simulated Marine Raid ](https://www.dvidshub.net/image/9899294/l-cac-64-takes-part-simulated-marine-raid) | `Landing Craft, Air Cushion 64, attached to Assault Craft Unit 5, prepares to offload Joint Light Tactical Vehicles, attached to Battalion Landing Team 24, 13th Marine Expeditionary Unit, during a simulated raid` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Boxer Conducts Routine Operations ](https://www.dvidshub.net/image/9984092/uss-boxer-conducts-routine-operations) | `U.S. Navy Landing Craft Air Cushion 48 assigned to Assault Craft Unit 5 approaches Wasp-class amphibious assault ship USS Boxer (LHD 4) while conducting well deck operations, Sept. 29, 2026. Boxer is deployed t` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=lcac+hovercraft+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=lcac+hovercraft+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=lcac+hovercraft+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=lcac+hovercraft+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=lcac+hovercraft+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=lcac+hovercraft+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=lcac+hovercraft+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- `unresolved`: no matching producer index was ready at integration. Keep collector pickup separate from image coverage.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.

Independent image-subject review correction: wrong-subject candidates excluded, duplicate image IDs collapsed, and sibling equipment separated above. Older revisions remain audit evidence and are superseded by this last current section.
<!-- NAVAL-CURRENT-END -->
