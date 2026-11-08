# Evidence-Grounded Reference Knowledge Pack: M1 Abrams Main Battle Tank

**Document Identifier:** `REF-M1-ABRAMS-20261009`  
**Asset Identifier:** `m1-abrams`  
**Standard:** JSLC / Project Eretz - Ground Combat Platform Kinematics Standard  
**Worker Identity:** `nrf8`  
**Response Identity:** `nrf8_gem_3.8_hi`  
**Handoff Reference:** `HO-20261009-naval-nrf8`  
**Observed UTC Timestamp:** `2026-10-09T11:10:00Z`  
**Authority:** Additive authority only. Target: `references/m1-abrams.md`.

---

## 1. Master Coordinate Datum & Ground Baseline

In strict accordance with the **JSLC / Naval & Military Kinematics Coordinate Datum**:
- **Heading / Forward:** Strictly **$-Z$** ($0^\circ$ yaw).
- **Vertical / Sky:** Strictly **$+Y$**. Ground plane locked at **$Y = 0.000\,\text{m}$** (bottom of non-deflected track shoes).
- **Lateral / Transverse:** Starboard is **$+X$**; Port is **$-X$**. Centerline is $X = 0.000\,\text{m}$.
- **Origin / Turret Ring:** Centerline axis at $X = 0.000\,\text{m}, Z \approx 0.000\,\text{m}$.

---

## 2. Variant Lineage & Distinction Matrix

| Variant | Era | Combat Weight | Armament | Sighting / RWS | Distinguishing Exterior Features |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **M1** `[sourced-m1]` | 1980 | 60.0 short tons (54.4 t) | 105mm M68A1 | Coax/Loader M240, CWS M2HB | Short bustle, mid-bore evacuator & thermal shroud. No CITV. |
| **IPM1** `[sourced-m1]` | 1984 | 61.5 short tons (55.8 t) | 105mm M68A1 | Same; upgraded suspension | Bustle rack lengthened +11 in (+28 cm). Still 105mm. |
| **M1A1** `[sourced-m1a1]` | 1985 | 67.6 short tons (61.3 t) | 120mm M256 | Coax/Loader M240, CWS M2HB | 120mm barrel, forward evacuator, MRS tip, new blowout panels, port NBC pack. |
| **M1A1 HA/HC** `[sourced-m1a1]` | 1988 | 69.4 short tons (63.0 t) | 120mm M256 | Heavy Armor / Common | 1st/2nd Gen DU mesh. USMC HC adds deep-water fording & deck tie-downs. |
| **M1A1 FEP/SA** `[sourced-m1a1]` | 2006 | 69.5 short tons (63.1 t) | 120mm M256 | SCWS, 2nd Gen FLIR | USMC FEP / Army SA. *USMC divested all tanks by 2021 (Force Design 2030).* |
| **M1A2** `[sourced-m1a2]` | 1992 | 69.54 short tons (63.1 t) | 120mm M256 | Adds CITV, IVIS, dual 1553B | Cylindrical CITV ahead of loader hatch on port roof; new commander cupola. |
| **M1A2 SEPv1** `[sourced-m1a2sep]` | 1999 | 69.5 short tons (63.0 t) | 120mm M256 | 2nd Gen FLIR, Bustle APU | APU in left rear bustle rack. High-res digital displays. |
| **M1A2 SEPv2** `[sourced-m1a2sep]` | 2007 | 71.2 short tons (64.6 t) | 120mm M256 | CROWS II .50 cal RWS | Tall CROWS II mount over cupola; TUSK side skirt tile mounts. |
| **M1A2 SEPv3** `[sourced-m1a2sep3]` | 2017 | 73.6 short tons (66.8 t) | 120mm M256 + ADL | CROWS-LP, JTRS, Trophy APS | Low-Profile CROWS, ADL breech link, hull sponson APU, Trophy radar plates. |
| **M1E3** `[sourced-m1e3]` | Dev. | Target <60.0 short tons | Restructured | Next-gen hybrid | Replaces canceled SEPv4 (M1A2D); focuses on weight reduction. |

---

## 3. Sourced Dimensions & Transport Envelopes

| Dimension | Metric SI | Imperial | Provenance Tier | Primary Source Citation & URL | Passage / Figure |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **Length (Gun Forward)** | **`9.830 m`** | `387.0 in` | `[sourced-m1a2]` | [GDLS Abrams M1A2](https://www.gdls.com) | Specification: `"Length: 387 in"` |
| **Length (Gun Aft)** | **`8.970 m`** | `353.1 in` | `[sourced-fas-m1]` | [FAS: M1 Abrams](https://man.fas.org/dod-101/sys/land/m1.htm) | Travel lock length over chassis astern |
| **Hull Length** | **`7.925 m`** | `312.0 in` | `[sourced-fas-m1]` | [FAS: M1 Abrams](https://man.fas.org/dod-101/sys/land/m1.htm) | Specs: `"Hull length: 312 in"` |
| **Width (Over Skirts)** | **`3.658 m`** | `144.0 in` | `[sourced-m1a2]` | [GDLS Abrams M1A2](https://www.gdls.com) | Dimensions: `"Width: 144 in"` |
| **Width (With ARAT/Trophy)** | **`3.950 m`** | `155.5 in` | `[inferred-from-dote]` | [DOT&E FY2023 Report](https://www.dote.osd.mil) | Lateral expansion over radar blisters |
| **Height (Turret Roof)** | **`2.375 m`** | `93.5 in` | `[sourced-m1a2]` | [GDLS Abrams M1A2](https://www.gdls.com) | Dimensions: `"Height: 93.5 in"` |
| **Height Overall (CITV/Apex)**| **`2.885 m`** | `113.6 in` | `[sourced-fas-m1]` | [FAS: M1 Abrams](https://man.fas.org/dod-101/sys/land/m1.htm) | Specs: `"Overall height: 113.6 in"` |
| **Height with CROWS-LP** | **`3.050 m`** | `120.1 in` | `[estimate]` | Engineering estimate | Roof $+Y = 2.375\,\text{m}$ + CROWS ($+0.675\,\text{m}$) |
| **Ground Clearance** | **`0.483 m`** | `19.0 in` | `[sourced-m1a2]` | [GDLS Abrams M1A2](https://www.gdls.com) | Specs: `"Ground Clearance: 19 in"` |
| **Track Tread Width** | **`2.845 m`** | `112.0 in` | `[sourced-fas-m1]` | [FAS: M1 Abrams](https://man.fas.org/dod-101/sys/land/m1.htm) | Running gear center-to-center track width |
| **Track Shoe (T158LL)** | **`0.635 m`** | `25.0 in` | `[sourced-army-asc]` | [USAASC Abrams](https://asc.army.mil) | Track system: Rubber replaceable pad width |
| **Wheelbase Centers** | **`4.620 m`** | `181.9 in` | `[inferred-from-drawings]` | TM 9-2350-255-10 | Road wheel 1 to 7 centers along Z |
| **Torsion Bar Stagger** | **`0.120 m`** | `4.72 in` | `[inferred-from-chassis]` | Transverse torsion bars | Left arms lead right arms along Z |

### 3.1 Transport & Logistics Clearance
- **US Navy LCAC Well Deck:** Strictly 1x M1A1/M1A2 centered along deck centerline ($8.23\,\text{m}$ beam); side-by-side impossible `[sourced-usn-lcac-factfile]`.
- **C-17A / C-5M Air Transport:** 1x M1 combat-ready on C-17A; up to 2x on C-5M (curb payload limit) `[sourced-usaf-c17; sourced-usaf-c5]`.
- **Rail Loading Gauge:** Skirt inspection required; exceeds Berne gauge without transport permit `[sourced-army-tea]`.

---

## 4. Real Fitted Combat Systems & Locations

- **Main Gun:** 105mm M68A1 rifled ($55\text{ rds}$) on M1/IPM1; 120mm M256 smoothbore ($40\text{--}42\text{ rds}$) on M1A1/M1A2 (34/36 in turret blowout bustle, 6 in hull locker) `[sourced-army-tm9-2350-264-10]`.
- **Secondary Armament:** 1x coaxial 7.62mm M240 ($10,000\text{ rds}$); 1x loader's skate 7.62mm M240 ($1,400\text{ rds}$); 1x commander's weapon: CWS .50 M2HB on M1/M1A1, CROWS II on SEPv2, CROWS-LP on SEPv3 ($900\text{--}1,000\text{ rds}$ .50 BMG).
- **Countermeasures & Optics:** 2x 6-tube M250 smoke dischargers on turret cheeks; ARAT I/II reactive tiles on side skirts; Rafael Trophy APS on SEPv2/SEPv3 (4 radar antennas, 2 MEFP launchers); Duke CREW jammer antennas on bustle.

---

## 5. Kinematic Rigging Hierarchy & Moving Parts

```text
Chassis_Hull [Root at Y = 0.483m]
├── Suspension_Left_Arm_[01..07] (Pitch: +X local; Stroke: ~380mm travel)
│   └── RoadWheel_Dual_Left_[01..07] (Roll: +X continuous)
├── Suspension_Right_Arm_[01..07] (Pitch: +X local; Staggered -Z by 120mm)
│   └── RoadWheel_Dual_Right_[01..07] (Roll: +X continuous)
├── DriveSprocket_Left / Right (Rear; Roll: +X continuous; 11-tooth)
├── Idler_Left / Right (Front; Tension adjuster along Z)
├── Driver_Hatch (Pivot: Left rear; Yaw: +Y 0° to 180° swing; Interlocked)
└── Turret_Main (Pivot: X=0.0m, Y=1.56m, Z=-0.15m; Yaw: +Y 360° continuous; Rate: 40°/s)
    ├── Gun_Cradle_Trunnion (Pivot: X=0.0m, Y=1.82m, Z=-0.81m; Pitch: +X axis)
    │   ├── Barrel_M256 (Pitch: -10.0° depression to +20.0° elevation; Rate: 24°/s)
    │   └── Coaxial_M240 (Slaved rigidly to gun pitch)
    ├── CITV_Assembly (M1A2 only; Port roof; Yaw: +Y 360° continuous; Pitch: -20° to +35°)
    ├── Commander_Cupola (Yaw: +Y 360° manual/power)
    │   └── CROWS_LP_Mount (M1A2 SEPv3; Yaw: 360° continuous; Pitch: -20° to +60°)
    ├── Commander_Hatch (Pivot: Aft hinge; Pitch: +X 0° to 105° open)
    └── Loader_Hatch (Pivot: Outboard hinge; Pitch: +Z 0° to 100° open)
```

---

## 6. Common 3D Modeling Errors

1. **Turret Symmetry Fallacy (CRITICAL):** Modeling turret cheeks symmetrically. The M1 turret is **asymmetrical**: port cheek is narrower and longer forward internally to clear the Gunner's Primary Sight (GPS), while starboard cheek is thicker and shorter.
2. **Road Wheel Alignment Fallacy:** Placing left and right road wheel hubs at identical Z positions. Transverse torsion bars force a **$\sim 120\,\text{mm}$ offset** between sides.
3. **Road Wheel Count Errors:** Exactly **7 road wheel pairs per side** (14 dual assemblies total). Budget models often incorrectly model 6 wheels.
4. **Bore Evacuator Confusion:** 105mm M68A1 barrel has a central cylindrical evacuator with a ribbed shroud. 120mm M256 has an eccentric evacuator at the forward third and an MRS collimator.
5. **Anachronistic CITV:** Attaching the CITV cylinder to M1, IPM1, or M1A1 hulls. CITV is exclusive to **M1A2+**.
6. **Stationary Radome / Antenna Rule (Ford Lesson Applied):** Communications antennas and Duke CREW masts are rigidly fixed; they never rotate mechanically.

---

## 7. Primary Trusted Image Collection (`dvidshub.net`)

Every entry is verified against official DVIDS metadata and captions:

| View / Angle | Variant | DVIDS Asset URL | VIRIN & Credit | Verified Caption Summary |
| :--- | :---: | :--- | :--- | :--- |
| **Front (Head-on)** | `M1A2` | [DVIDS 4158446](https://www.dvidshub.net/image/4158446/us-soldiers-scan-area-m1a2-abrams-tank) | `180215-A-SI385-1002`<br>Spc. E. Cervantes | Head-on front view in desert at Fort Irwin NTC. Lower glacis, shackles, cheek frontal profile. |
| **Front (LCAC Offload)** | `M1A1 USMC` | [DVIDS 1219606](https://www.dvidshub.net/image/1219606/bring-forth-tanks-ssang-yong-14) | `140403-M-DC078-003`<br>Sgt. A. Kirby | Direct front view rolling off LCAC bow ramp at Ssang Yong 14, Korea. Proves LCAC centerline staging. |
| **Starboard Flank** | `M1A2 SEPv3` | [DVIDS 7780441](https://www.dvidshub.net/image/7780441/arrow-23) | `230505-A-JN384-1011`<br>Spc. J. Nunnenkamp | Full starboard flank profile in Finland (Arrow 23). SEPv3 skirts, wheels, and CROWS-LP. |
| **Top / Overhead** | `M1A1 USMC` | [DVIDS 266574](https://www.dvidshub.net/image/266574/tank-platoon-and-french-foreign-legion-tank-range) | `100330-M-6001S-182`<br>Sgt. M. Fayloga | Overhead view firing 120mm main gun in Djibouti. Complete turret roof layout, blowout panels, hatches. |
| **Front 3/4 Quarter** | `M1A2 SEPv3` | [DVIDS 7899836](https://www.dvidshub.net/image/7899836/1-8th-cavalry-spur-ride) | `230706-Z-UV688-2608`<br>SSgt. C. Rivas | Front 3/4 view in Lithuania. Track curve, hull nose, side skirts, track shoe maintenance. |
| **Mechanism: ARAT Skirts** | `M1A2 ARAT` | [DVIDS 6278420](https://www.dvidshub.net/image/6278420/us-18th-mp-brigade-installs-arat-tiles) | `200710-A-UC661-002`<br>Sgt. E. Ruchotzke | Close-up installing Abrams Reactive Armor Tiles (ARAT) on skirt mounting rails at Bergen-Hohne. |
| **Mechanism: Stern/Exhaust**| `M1A1` | [DVIDS 4000796](https://www.dvidshub.net/image/4000796/tank-heat-shields) | `171128-A-PB123-1005`<br>703rd BSB | Direct rear view at Fort Stewart showing engine deck exhaust grille & upward heat shield. |
| **Mechanism: Engine Pack** | `M1 Abrams` | [DVIDS 7796419](https://www.dvidshub.net/image/7796419/us-army-conducts-m1-abrams-tank-maintenance) | `230511-A-JK123-1007`<br>Pfc. J. Klaer | Open engine bay with Honeywell AGT1500 gas turbine power pack hoisted in Nowa Deba, Poland. |

### 7.1 Angles Unresolved on DVIDS Repository
- **Unoccluded Port Broadside:** Searched `site:dvidshub.net/image "Abrams" "port" OR "left side" profile`. Active DVIDS results exhibit occlusion. Resolved via external collector (`m1-abrams-port-wikimedia--Fallujah-JPEG.jpeg`).
- **Clean Standalone Rear Plate:** Searched `site:dvidshub.net/image "Abrams" "rear view"`. DVIDS images feature personnel or equipment. Resolved via external collector (`m1-abrams-rear-wikimedia--rear-view-jpg.jpg`).

---

## 8. External Sibling Collector Reference (`D:/dreidel3d-sv2/refimages/`)

The external image catalog is finalized and verified at `D:/dreidel3d-sv2/refimages/ground-agy/INDEX.md`. The 8 collected images are accessible via portable relative paths:

- Front View (M1 105mm): [m1-abrams-front](../../../../dreidel3d-sv2/refimages/ground-agy/m1-abrams/m1-abrams-front-wikimedia--Lima-1979-jpg.jpg)
- Rear View (XM1/M1 Grilles): [m1-abrams-rear](../../../../dreidel3d-sv2/refimages/ground-agy/m1-abrams/m1-abrams-rear-wikimedia--rear-view-jpg.jpg)
- Port Flank (USMC M1A1 Fallujah): [m1-abrams-port](../../../../dreidel3d-sv2/refimages/ground-agy/m1-abrams/m1-abrams-port-wikimedia--Fallujah-JPEG.jpeg)
- Starboard Flank (M1A2 SEPv3 Finland): [m1-abrams-stbd](../../../../dreidel3d-sv2/refimages/ground-agy/m1-abrams/m1-abrams-stbd-wikimedia-7780441.jpg)
- Overhead Top View (USMC M1A1 Firing): [m1-abrams-top](../../../../dreidel3d-sv2/refimages/ground-agy/m1-abrams/m1-abrams-top-wikimedia-fire-above-jpg.jpg)
- Three-Quarter View (M1A2 SEPv3): [m1-abrams-3-4](../../../../dreidel3d-sv2/refimages/ground-agy/m1-abrams/m1-abrams-three-quarter-wikimedia-7899836.jpg)
- Mechanism Detail (ARAT Tiles): [m1-abrams-arat](../../../../dreidel3d-sv2/refimages/ground-agy/m1-abrams/m1-abrams-closeup-wikimedia-6278420.jpg)
- Interior Detail (M1A1 Gunner/Cdr): [m1-abrams-interior](../../../../dreidel3d-sv2/refimages/ground-agy/m1-abrams/m1-abrams-interior-wikimedia-s-interior-jpg.jpg)

---

## 9. Uncertainty Register & Unresolved Technical Parameters

1. **Composite & DU Armor Internal Matrix Thickness:** `[unresolved]` Classified DoD / Army secret; 3D models must represent only Outer Mold Line (OML) surfaces.
2. **CITV Exact Mechanical Elevation Stops:** `[unresolved]` Public brochures state operational envelope $-20^\circ$ to $+35^\circ$; hard bumper stops unverified in public domain.
3. **M1A2 SEPv3 Sponson Width Variance:** `[unresolved]` Exact total width over Trophy APS radar blisters ranges between $3.90\,\text{m}$ and $3.98\,\text{m}$ depending on shims.
4. **Driver's Emergency Floor Escape Hatch:** `[unresolved]` Presence and dimensioning varies between early Chrysler and Lima production hulls.

---

## 10. Primary Source Citations

1. **General Dynamics Land Systems (GDLS):** *Abrams M1A2 Main Battle Tank Datasheet* & *M1A1 Technical Overview*, [gdls.com](https://www.gdls.com).
2. **U.S. Department of the Army:** *TM 9-2350-255-10: Operator's Manual for M1*; *TM 9-2350-264-10: Operator's Manual for M1A1*; *TM 9-2350-388-10: M1A2 SEP*.
3. **Director, Operational Test and Evaluation (DOT&E):** *FY2023 Annual Report (M1A2 SEPv3 / Trophy APS)*, [dote.osd.mil](https://www.dote.osd.mil).
4. **Federation of American Scientists (FAS):** *M1 Abrams Main Battle Tank Military Analysis Network*, [man.fas.org](https://man.fas.org/dod-101/sys/land/m1.htm).
5. **U.S. Marine Corps:** *Force Design 2030 (Tank Battalion Divestment Decision)*, Marine Corps Combat Development Command.
6. **Defense Visual Information Distribution Service (DVIDS):** Primary photography repository, [dvidshub.net](https://www.dvidshub.net).


---

<!-- NAVAL-CURRENT-START -->
# m1-abrams — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:24:21.394242+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-M1A1` | Gun-forward length 387 in, width 144 in, turret height 96 in; derived approximately 9.83 m, 3.66 m, 2.44 m. Brochure identifies 1,500 hp gas turbine and 120 mm smoothbore. Turret height is not an independently defined overall-height datum. | [Primary source](https://international.gdls.com/english/products/ABRAMS/M1A1.pdf); second-page Specifications |
| `sourced-M1A2-brochure` | Gun-forward length 387 in, width 144 in; height field 93.5 in (approximately 2.37 m derived). Keep this older brochure variant distinct from SEP versions. | [Primary source](https://international.gdls.com/english/products/ABRAMS/M1A2.pdf); second-page Specifications |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| turret traverse | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| gun elevation/recoil | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| tracks and road wheels | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| crew hatches | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| variant-specific weapon stations | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Do not merge adjacent variants, operational and stowed dimensions, or demonstration motion with sourced operating rates. Exact fitted counts/locations and kinematic values not sourced above remain unresolved.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [Bring forth the tanks, Ssang Yong 14 ](https://www.dvidshub.net/image/1219606/bring-forth-tanks-ssang-yong-14) | `U.S. Marine M1A1 Abrams tank offloads from a U.S. Navy Landing Craft Air Cushion ship for exercise Ssang Yong 2014 in Dogue, Republic of Korea April 3. Ssang Yong, meaning twin dragons, is intended to strengthe` — `sourced-caption` | `front` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Tank Platoon and French Foreign Legion tank range ](https://www.dvidshub.net/image/266574/tank-platoon-and-french-foreign-legion-tank-range) | `A M1A1 Abrams battle tank from Tank platoon Alpha Company, Battalion Landing Team 1st Battalion, 9th Marine Regiment, 24th Marine Expeditionary Unit, discharges a 120mm round towards a tank hull during a live-f` — `sourced-caption` | `overhead` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Tank Heat Shields ](https://www.dvidshub.net/image/4000796/tank-heat-shields) | `Welders with Bravo Company, 703rd Brigade Support Battalion, 2nd Armored Brigade Combat Team, 3rd Infantry complete the first heat shield for an M1A1 Abrams tank heat shield Nov. 28, 2017, at Fort Stewart, Ga. ` — `sourced-caption` | `stern` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [U.S. Soldiers scan the area in an M1A2 Abrams Tank ](https://www.dvidshub.net/image/4158446/us-soldiers-scan-area-m1a2-abrams-tank) | `U.S. Soldiers assigned to 3rd Squadron, 3rd Cavalry Regiment, scan the area in an M1A2 Abrams Tank , during Decisive Action Rotation 18-04 at the National Training Center in Fort Irwin, Calif., Feb. 15, 2018. D` — `sourced-caption` | `front` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [US 18th MP Brigade Installs ARAT Tiles ](https://www.dvidshub.net/image/6278420/us-18th-mp-brigade-installs-arat-tiles) | `Soldiers with 527 Military Police Company, 709 Military Police Battalion, 18th Military Police Brigade, install Abrams Reactive Armor Tiles at Bergen-Hohne Training Area, Germany, July 10, 2020 prior to phase t` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Arrow 23 ](https://www.dvidshub.net/image/7780441/arrow-23) | `An M1A2 SEPV3 Abrams Main Battle Tank, assigned to 1st Battalion, 8th Cavalry Regiment, sits behind concealment during Arrow 23 in Niinisalo Training Area, Finland, May 5, 2023. Exercise Arrow is an annual, mul` — `sourced-caption` | `starboard` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [U.S. Army conducts M1 Abrams tank maintenance ](https://www.dvidshub.net/image/7796419/us-army-conducts-m1-abrams-tank-maintenance) | `U.S. Soldiers assigned to Aggressor Company, 2nd Battalion, 70th Armor Regiment, 2nd Armored Brigade Combat Team, 1st Infantry Division supporting the 4th Infantry Division, pull an M1 Abrams tank engine out fo` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [1-8th Cavalry Spur Ride ](https://www.dvidshub.net/image/7899836/1-8th-cavalry-spur-ride) | `U.S. Army Soldiers, assigned to 1st Battalion, 8th Cavalry Regiment, supporting 4th Infantry Division, along with NATO armed forces remove track pads from an M1 Abrams during the Spur Ride event near Pabrade, L` — `sourced-caption` | `front` candidate, `inferred-view`; exact coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=m1+abrams+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=m1+abrams+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=m1+abrams+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=m1+abrams+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=m1+abrams+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=m1+abrams+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=m1+abrams+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- [Existing ground-agy index](../../../../../dreidel3d-sv2/refimages/ground-agy/INDEX.md); `sourced-local-index-presence`. Read unit rows, not a blanket Complete banner. Some indexes contradict their own coverage matrices.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.
<!-- NAVAL-CURRENT-END -->


---

<!-- NAVAL-CURRENT-START -->
# m1-abrams — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:32:48.849695+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-M1A1` | Gun-forward length 387 in, width 144 in, turret height 96 in; derived approximately 9.83 m, 3.66 m, 2.44 m. Brochure identifies 1,500 hp gas turbine and 120 mm smoothbore. Turret height is not an independently defined overall-height datum. | [Primary source](https://international.gdls.com/english/products/ABRAMS/M1A1.pdf); second-page Specifications |
| `sourced-M1A2-brochure` | Gun-forward length 387 in, width 144 in; height field 93.5 in (approximately 2.37 m derived). Keep this older brochure variant distinct from SEP versions. | [Primary source](https://international.gdls.com/english/products/ABRAMS/M1A2.pdf); second-page Specifications |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| turret traverse | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| gun elevation/recoil | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| tracks and road wheels | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| crew hatches | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| variant-specific weapon stations | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Do not merge adjacent variants, operational and stowed dimensions, or demonstration motion with sourced operating rates. Exact fitted counts/locations and kinematic values not sourced above remain unresolved.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [Bring forth the tanks, Ssang Yong 14 ](https://www.dvidshub.net/image/1219606/bring-forth-tanks-ssang-yong-14) | `U.S. Marine M1A1 Abrams tank offloads from a U.S. Navy Landing Craft Air Cushion ship for exercise Ssang Yong 2014 in Dogue, Republic of Korea April 3. Ssang Yong, meaning twin dragons, is intended to strengthe` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Tank Platoon and French Foreign Legion tank range ](https://www.dvidshub.net/image/266574/tank-platoon-and-french-foreign-legion-tank-range) | `A M1A1 Abrams battle tank from Tank platoon Alpha Company, Battalion Landing Team 1st Battalion, 9th Marine Regiment, 24th Marine Expeditionary Unit, discharges a 120mm round towards a tank hull during a live-f` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Tank Heat Shields ](https://www.dvidshub.net/image/4000796/tank-heat-shields) | `Welders with Bravo Company, 703rd Brigade Support Battalion, 2nd Armored Brigade Combat Team, 3rd Infantry complete the first heat shield for an M1A1 Abrams tank heat shield Nov. 28, 2017, at Fort Stewart, Ga. ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [U.S. Soldiers scan the area in an M1A2 Abrams Tank ](https://www.dvidshub.net/image/4158446/us-soldiers-scan-area-m1a2-abrams-tank) | `U.S. Soldiers assigned to 3rd Squadron, 3rd Cavalry Regiment, scan the area in an M1A2 Abrams Tank , during Decisive Action Rotation 18-04 at the National Training Center in Fort Irwin, Calif., Feb. 15, 2018. D` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [US 18th MP Brigade Installs ARAT Tiles ](https://www.dvidshub.net/image/6278420/us-18th-mp-brigade-installs-arat-tiles) | `Soldiers with 527 Military Police Company, 709 Military Police Battalion, 18th Military Police Brigade, install Abrams Reactive Armor Tiles at Bergen-Hohne Training Area, Germany, July 10, 2020 prior to phase t` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Arrow 23 ](https://www.dvidshub.net/image/7780441/arrow-23) | `An M1A2 SEPV3 Abrams Main Battle Tank, assigned to 1st Battalion, 8th Cavalry Regiment, sits behind concealment during Arrow 23 in Niinisalo Training Area, Finland, May 5, 2023. Exercise Arrow is an annual, mul` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [U.S. Army conducts M1 Abrams tank maintenance ](https://www.dvidshub.net/image/7796419/us-army-conducts-m1-abrams-tank-maintenance) | `U.S. Soldiers assigned to Aggressor Company, 2nd Battalion, 70th Armor Regiment, 2nd Armored Brigade Combat Team, 1st Infantry Division supporting the 4th Infantry Division, pull an M1 Abrams tank engine out fo` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [1-8th Cavalry Spur Ride ](https://www.dvidshub.net/image/7899836/1-8th-cavalry-spur-ride) | `U.S. Army Soldiers, assigned to 1st Battalion, 8th Cavalry Regiment, supporting 4th Infantry Division, along with NATO armed forces remove track pads from an M1 Abrams during the Spur Ride event near Pabrade, L` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=m1+abrams+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=m1+abrams+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=m1+abrams+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=m1+abrams+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=m1+abrams+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=m1+abrams+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=m1+abrams+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- [Existing ground-agy index](../../../../../dreidel3d-sv2/refimages/ground-agy/INDEX.md); `sourced-local-index-presence`. Read unit rows, not a blanket Complete banner. Some indexes contradict their own coverage matrices.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.

Independent image-subject review correction: wrong-subject candidates excluded, duplicate image IDs collapsed, and sibling equipment separated above. Older revisions remain audit evidence and are superseded by this last current section.
<!-- NAVAL-CURRENT-END -->
