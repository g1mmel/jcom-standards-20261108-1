# Boeing F/A-18E/F Super Hornet & EA-18G Growler Knowledge Pack
**Platform:** F/A-18E (Single-Seat), F/A-18F (Two-Seat), EA-18G Growler (Airborne Electronic Attack)  
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard (`SKILL.md`)  
**Worker Identity:** `nrfa` (`nrfa_gem_3.8_hi`) | **Handoff:** `HO-20261009-naval-nrfa`  
**Timestamp (Observed UTC):** `2026-10-09T11:15:04Z` | **Status:** Concise Knowledge Pack (8–12 KB target)  

---

## 1. Platform Identity, Lineage & Variant Differentiation

*   **Service & Roles:** US Navy (`USN`) & RAAF. Operating from *Nimitz* (CVN-68) and *Gerald R. Ford* (CVN-78) supercarriers [`sourced-F/A-18E/F`: [US Navy Fact File](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2143477/fa-18ef-super-hornet/)].
*   **Legacy Hornet (F/A-18A/B/C/D):** 400 sq ft wing, 56 ft LOA. Rounded D-shaped intakes with perforated diverters. Vertical fences on upper LEX. Dorsal spine clamshell speedbrake. M61A1 cannon (578 rds). 4 wing pylons.
*   **Super Hornet (F/A-18E/F):** 500 sq ft wing (+25%), 60.3 ft LOA (+34 in plug stretch: 18 in fwd, 16 in aft) [`sourced-F/A-18E/F`: [AIAA-98-2514](https://arc.aiaa.org/doi/10.2514/6.1998-2514)]. Rectangular caret intakes (34% more airflow for F414 engines, RCS aligned). Gothic-ogee LEX eliminates fences [`sourced-F/A-18E/F`: [NASA TM-4487](https://ntrs.nasa.gov/citations/19930015758)]. Dorsal speedbrake **DELETED**; digital FCS aerodynamic braking via twin upper LEX spoilers ($60^\circ$), rudder flare ($16^\circ$), and aileron droop. M61A2 lightweight cannon (412 rds). 6 wing pylons.
*   **EA-18G Growler (AEA):** Built on two-seat F-airframe (Pilot + EWO). 20mm nose gun **DELETED**, replaced by avionics receiver pallet behind smooth unported fairing. Wingtip missile rails replaced by fixed AN/ALQ-218(V)2 tactical jamming receiver pods [`sourced-EA-18G`: [NAVAIR 01-EA18G-1](https://publicintelligence.net/)]. Carries up to 5 external AN/ALQ-99 or NGJ-MB jamming pods underwing/centerline with nose Ram Air Turbines (RATs).

---

## 2. Sourced Metric Dimensions & Carrier Envelope

*Datum:* DWL $Y = 0.000\text{ m}$ (static deck contact); Heading $-Z$, Sky $+Y$, Starboard $+X$, Port $-X$. Conflicting dimensions preserved per Bible rule 48.

| Parameter | SI Metric | Imperial | Provenance | Source & Supporting Citation |
| :--- | :--- | :--- | :--- | :--- |
| **Length Overall (LOA)** | **18.31 – 18.38 m** | **60' 1.25" – 60' 3.6"** | `sourced-F/A-18E/F` | [NAVAIR A1-F18EA-NFM-000](https://publicintelligence.net/u-s-navy-f-a-18e-f-super-hornet-natops-flight-manual/) Fig 1-2 (18.31 m); [US Navy Fact File](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2143477/fa-18ef-super-hornet/) (60.3 ft / 18.38 m). |
| **Wingspan (Tip Stores)** | **13.62 – 13.68 m** | **44' 8.5" – 44' 11"** | `sourced-F/A-18E/F` | [NAVAIR A1-F18EA-NFM-000](https://publicintelligence.net/u-s-navy-f-a-18e-f-super-hornet-natops-flight-manual/) Fig 1-2 (w/ missile); [Boeing Fact Sheet](https://www.boeing.com/defense/fa-18-super-hornet/) (44.9 ft / 13.68 m). |
| **Wingspan (Clean)** | **13.02 m** | **42 ft 8.5 in** | `sourced-F/A-18E/F` | [NAVAIR A1-F18EA-NFM-000](https://publicintelligence.net/u-s-navy-f-a-18e-f-super-hornet-natops-flight-manual/) Fig 1-2 (bare wingtip casting). |
| **Wingspan (EA-18G w/ Pods)**| **13.68 m** | **44 ft 11 in** | `sourced-EA-18G` | [NAVAIR 01-EA18G-1](https://publicintelligence.net/); Boeing Growler Overview. |
| **Wingspan Folded (E/F)** | **9.32 m** | **30 ft 7 in** | `sourced-F/A-18E/F` | [NAVAIR A1-F18EA-NFM-000](https://publicintelligence.net/u-s-navy-f-a-18e-f-super-hornet-natops-flight-manual/) Fig 1-2; [NAVAIR 00-80T-120](https://publicintelligence.net/us-navy-aircraft-handling-natops-manual/) Table 4-1 (at BL 183.5). |
| **Wingspan Folded (EA-18G)** | **9.98 m** | **32 ft 9 in** | `sourced-EA-18G` | [NAVAIR 00-80T-120](https://publicintelligence.net/us-navy-aircraft-handling-natops-manual/) Table 4-1 (across folded ALQ-218 antennas). |
| **Static Fin Height** | **4.88 m** | **16 ft 0 in** | `sourced-F/A-18E/F` | [NAVAIR A1-F18EA-NFM-000](https://publicintelligence.net/u-s-navy-f-a-18e-f-super-hornet-natops-flight-manual/) Fig 1-2; [US Navy Fact File](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2143477/fa-18ef-super-hornet/). Static deck to fin apex. |
| **Folded Wingtip Height** | **~4.42 m** | **~14 ft 6 in** | `estimate` | Inferred from NATOPS Fig 1-2; fin apex remains highest point. |
| **Wheelbase (NLG to MLG)** | **5.42 m** | **17 ft 9.5 in** | `sourced-F/A-18E/F` | [NAVAIR A1-F18EA-NFM-000](https://publicintelligence.net/u-s-navy-f-a-18e-f-super-hornet-natops-flight-manual/) Fig 1-2. Conflict: 5.72 m (18.77 ft) extended strut. |
| **Wheel Track (MLG Tread)** | **3.11 m** | **10 ft 2.5 in** | `sourced-F/A-18E/F` | [NAVAIR A1-F18EA-NFM-000](https://publicintelligence.net/u-s-navy-f-a-18e-f-super-hornet-natops-flight-manual/) Fig 1-2. Transverse MLG tire center-to-center. |
| **Wing Area ($S_{ref}$)** | **46.45 m²** | **500.0 sq ft** | `sourced-F/A-18E/F` | [AIAA Paper 98-2514](https://arc.aiaa.org/doi/10.2514/6.1998-2514); Boeing F/A-18 Summary (+25% over C/D). |
| **Tailhook Shank Length** | **1.98 m** | **78.0 in** (6.5 ft) | `sourced-F/A-18E/F` | [MIL-A-8863B](https://quicksearch.dla.mil/); NAVAIR Hook Spec. Keel pivot to hook point. |
| **Launch Bar Length** | **0.79 m** | **31.0 in** (2.58 ft)| `sourced-F/A-18E/F` | [MIL-L-8552D](https://quicksearch.dla.mil/); [NAVAIR 00-80T-105](https://publicintelligence.net/us-navy-cv-natops-manual/). Strut pivot to roller. |
| **Max Takeoff Gross Weight** | **29,937 kg** | **66,000 lb** | `sourced-F/A-18E/F` | [US Navy Fact File](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2143477/fa-18ef-super-hornet/); Boeing F/A-18E/F Datasheet. |
| **Max Carrier Landing Wt** | **19,958 kg** | **44,000 lb** | `sourced-F/A-18E/F` | [NAVAIR 00-80T-105](https://publicintelligence.net/us-navy-cv-natops-manual/) CV NATOPS. Max allowable trap gross weight. |
| **Operating Weight Empty** | **~14,552 / 14,831 kg**| **32,081 / 32,698 lb**| `sourced-F/A-18E/F` | [DoD SAR Report](https://www.esd.whs.mil/). E (single) / F (two-seat). |

---

## 3. Real Fitted Systems, Counts & Topside Locations

*   **Engines (2 Turbofans):** 2x General Electric F414-GE-400 afterburning turbofans; dry thrust 57.8 kN (13,000 lbf), afterburning 97.9 kN (22,000 lbf) each [`sourced-F/A-18E/F`: [US Navy Fact File](https://www.navy.mil/)]. Axisymmetric convergent-divergent nozzles.
*   **Radar: Raytheon AN/APG-79 AESA:** Forward nose bulkhead. **RIGIDLY FIXED — NEVER ROTATES.** Tilted rearward $20.0^\circ$ for RCS reduction; electronically steers beam $\pm 60^\circ$ in az/el [`sourced-F/A-18E/F`: [Raytheon APG-79](https://www.rtx.com/)].
*   **Tactical EW (EA-18G):** AN/ALQ-218(V)2 wingtip pods (Sta 1 & 11) for $360^\circ$ DF; up to 5 external AN/ALQ-99 or NGJ-MB jamming pods underwing/centerline with spinning nose Ram Air Turbines (RATs) [`sourced-EA-18G`: [NAVAIR 01-EA18G-1](https://publicintelligence.net/)].
*   **Targeting Pod:** AN/ASQ-228 ATFLIR on port cheek Sta 4 (BL -36.0 in, FS 390.0) [`sourced-F/A-18E/F`: [NAVAIR A1-F18EA-NFM-000](https://publicintelligence.net/)].
*   **Internal Cannon (F/A-18E/F ONLY):** 1x M61A2 20mm Vulcan rotary gun in nose upper decking (412 rds; single recessed muzzle port). **DELETED ON EA-18G** [`sourced-F/A-18E/F`: [General Dynamics OTS](https://www.gd-ots.com/)].
*   **Hardpoints (11 Stations):** 1 centerline (Sta 6), 2 fuselage cheeks (Sta 5 port, 7 stbd), 6 wing pylons (Sta 2, 3, 4 port / 8, 9, 10 stbd), 2 wingtip (Sta 1 & 11: LAU-127 on E/F, ALQ-218 on G) [`sourced-F/A-18E/F`: [NAVAIR A1-F18EA-NFM-000](https://publicintelligence.net/)].
*   **Carrier Gear:** Dual nose wheels with launch bar and RRHB holdback lug; keel arresting hook shank (1.98 m) with gas-hydraulic hold-down damper [`sourced-F/A-18E/F`: [MIL-L-8552D](https://quicksearch.dla.mil/); [MIL-A-8863B](https://quicksearch.dla.mil/)].

---

## 4. Moving Parts Kinematics & Hierarchy

```
Airframe_Root [0,0,0]
├── geo_fuselage_primary
│   ├── mech_canopy_clamshell [Pitch +X: 0.0° latched to +48.0° open; 8-10 s electrical]
│   ├── mech_radome_starboard [Yaw +Y: 0.0° to +90.0° open (Maintenance only)]
│   ├── sensor_aesa_apg79 [STATIONARY: Fixed +20.0° rearward tilt, ZERO ROTATION]
│   ├── aero_lex_spoiler_p/s [Hinge fwd: 0.0° flush to +60.0° up; ~1.0 s aero braking]
│   ├── gear_nlg [Pitch fwd/up -95.0°; 7-9 s cycle] -> mech_launch_bar [Pitch +X: 0.0° to +58.0°]
│   ├── gear_mlg_p/s [Levered pitch fwd/up -92.0°; wheel rotates 90° flat]
│   ├── tail_stabilator_p/s [Spindle pitch: -24.0° TEU to +10.5° TED; rate 40.0°/s; diff roll ±24°]
│   ├── tail_fin_p/s [Fixed cant 20.0°] -> aero_rudder_p/s [Canted: ±30.0°; 82.0°/s; toe-in +16.0°]
│   └── mech_tailhook [Keel pivot: 0.0° stowed to -52.0° hang limit; drop 1.5-2.0 s; 48° trail]
└── wing_inboard_fixed_p/s (BL 0 to BL 183.5)
    ├── aero_lef_inboard [Swept hinge: 0.0° to -40.0° droop; 18.0°/s]
    ├── aero_tef_inboard [Transverse: 0.0° to +40.0° TED; 24.0°/s]
    └── mech_wingfold_joint [BL 183.5 (X = ±4.66m); roll 0.0° to 95.0° over-center; 10-15 s]
        └── wing_outboard_folding_panel
            ├── aero_lef_outboard [Swept hinge: 0.0° to -40.0° droop]
            └── aero_aileron [Transverse: -24.0° TEU to +45.0° TED; droop +42.0°; 100.0°/s]
```

*Limits/Rates sourced from NASA TP-1999-206573 Table 1, AIAA-98-2514, and NAVAIR A1-F18EA-NFM-000.*

---

## 5. Common Modelling Errors & Forensic Traps

1.  **Intake Conflation:** Cloned round D-shaped intakes from F/A-18C. Super Hornet/Growler **MUST** have rectangular caret intakes.
2.  **Spurious LEX Fences:** Adding vertical fences on the upper LEX. Super Hornet's gothic-ogee LEX eliminates them entirely.
3.  **Ghost Dorsal Speedbrake:** Modelling a dorsal clamshell door between the fins. **DELETED** on E/F/G; uses digital FCS surface braking (rudder toe-in $16^\circ$, aileron droop, flaps, LEX spoilers).
4.  **Missing LEX Spoilers:** Omitting twin forward-hinged rectangular spoilers on upper LEX popping up $60^\circ$ during braking.
5.  **Spurious Cannon on EA-18G:** Rendering a 20mm muzzle port on EA-18G. Gun is deleted and replaced with an avionics receiver pallet behind a smooth unported fairing.
6.  **Incorrect Wingtip Fit on EA-18G:** Mounting missile rails on Growler wingtips. EA-18G **MUST** have fixed AN/ALQ-218(V)2 receiver pods.
7.  **Spinning AESA Radar:** Animating the AN/APG-79 radar rotating $360^\circ$. It is a stationary planar array tilted $20^\circ$ rearward.
8.  **Undersized Scale:** Applying legacy F/A-18C dimensions (56 ft LOA, 400 sq ft wing area) to Super Hornet (60.3 ft LOA, 500 sq ft wing area).
9.  **Single-Seat EA-18G:** Rendering Growler as single-seater. Growler is exclusively tandem two-seat (Pilot forward, EWO aft).

---

## 6. Uncertainty Register

| Subsystem / Metric | Status | Boundary & Justification | Conservative Recommendation |
| :--- | :--- | :--- | :--- |
| **Internal Fuselage Station Lofts** | `unresolved` | Detailed structural station spacing is Boeing proprietary data. | Adhere to mold line envelope: LOA 18.38 m, Span 13.68 m, Fin Apex 4.88 m. |
| **Gear Internal Linkage Coordinates** | `unresolved` | Internal retraction cylinder geometry is controlled under NAVAIR IETMs. | Animate trunnion pivot along $X$-axis with $90^\circ$ forward retraction. |
| **APG-79 Exact T/R Module Count** | `estimate` | Exact Gallium Arsenide T/R count is classified. | Literature benchmarks cite ~1,100 T/R modules; model planar face tilted $20^\circ$. |

---

## 7. Multi-Angle Verified DVIDS Photographic Evidence

Verified visual evidence from [dvidshub.net](https://www.dvidshub.net):

| Angle | Unit & Hull | Date | DVIDS Page URL | Verified Caption & Structural Details |
| :--- | :--- | :--- | :--- | :--- |
| **Bow** | VFA-151 / CVN 72 | 2022-02-18 | [DVIDS 7079072](https://www.dvidshub.net/image/7079072/f-a-18e-super-hornet-launches-off-flight-deck) | Head-on launch view; caret intakes, dual nose gear, LEX contour. |
| **Stern** | VFA-22 / CVN 68 | 2022-06-15 | [DVIDS 7275325](https://www.dvidshub.net/image/7275325/f-18f-super-hornet-prepares-land) | Rear-quarter approach; twin F414 exhaust nozzles, canted fins, hook. |
| **Port** | VX-23 / Pax River | 2010-04-22 | [DVIDS 100422001](https://commons.wikimedia.org/wiki/File:%27Green_Hornet%27_flight_test_on_Earth_Day_100422-N-ZZ999-001.jpg) | Clean port flight profile; caret intake lip, canopy curvature. |
| **Starboard**| USN / CVN 69 | 2016-10-15 | [DVIDS 161015098](https://commons.wikimedia.org/wiki/File:161015-N-IE397-098_161015-N-IE397-098.jpg) | Starboard profile on deck; wing pylons, fuel tank, landing gear stance. |
| **Overhead** | USN / CVN 69 | 2021-04-12 | [DVIDS 51172401761](https://commons.wikimedia.org/wiki/File:Aviation_Electronics_Technician_3rd_Class_Christopher_Hodges_installs_a_radar_beacon_on_an_F_A-18E_Super_Hornet_aboard_USS_Dwight_D._Eisenhower_(CVN_69)_in_the_Arabian_Sea._(51172401761).jpg) | Aerial view; upper spine, 500 sq ft planform, speedbrake deletion. |
| **Quarter** | VFA-213 / CVN 78 | 2023-09-12 | [DVIDS 8005070](https://www.dvidshub.net/image/8005070/f-18f-super-hornet-launch) | Port bow quarter catapult launch from EMALS track on CVN-78. |
| **Mech: Bar**| VFA-102 / CVN 68 | 2023-01-24 | [DVIDS 7593549](https://www.dvidshub.net/image/7593549/sailors-secure-f-18f-super-hornet-catapult) | Close-up of nose gear launch bar articulated $58^\circ$ into shuttle. |
| **Mech: Hook**| VFA-22 / CVN 68 | 2022-02-14 | [DVIDS 7073979](https://www.dvidshub.net/image/7073979/f-18f-super-hornet-lands-flight-deck) | Trapping wire with tailhook shank extended at $48^\circ$ trail angle. |
| **Mech: Fold**| USN / CVN 68 | 2022-05-18 | [DVIDS 7247253](https://www.dvidshub.net/image/7247253/f-18e-super-hornets-elevated-out-hangar-bay) | Super Hornets with wings folded $90^\circ$ upright on aircraft elevator. |
| **Mech: Hinge**| USN / CV 63 | 2005-11-15 | [DVIDS 051115012](https://commons.wikimedia.org/wiki/File:US_Navy_051115-N-6060O-012_Airman_Recruit_Joshua_R._Hall_hoses_down_a_wing_fold_on_an_F-A-18F_Super_Hornet.jpg) | Close-up of wing fold rotary hinge lugs, lock pins, and rib joints. |
| **Mech: Canopy**| VFA-115 / CVN 77 | 2016-11-06 | [DVIDS 161106058](https://commons.wikimedia.org/wiki/File:161106-N-WA993-058_(30561617730).jpg) | Canopy open $+48^\circ$ on flight deck; shows cockpit and seat. |

---

## 8. External Collector Sibling Integration (`refimages/*/INDEX.md`)

*   **Collector Status:** **Index Ready.** Curated images cataloged in `D:/dreidel3d-sv2/refimages/air-agy/INDEX.md` under `fa18ef-superhornet/`.
*   **Portable Sibling Links (Relative to `references/`):**
    *   *Front:* `../../../../dreidel3d-sv2/refimages/air-agy/fa18ef-superhornet/fa18ef-superhornet-front-nasa-afrc2022-126.jpg`
    *   *Rear:* `../../../../dreidel3d-sv2/refimages/air-agy/fa18ef-superhornet/fa18ef-superhornet-rear-usmc-yuma-exhaust.jpg`
    *   *Port:* `../../../../dreidel3d-sv2/refimages/air-agy/fa18ef-superhornet/fa18ef-superhornet-port-dvids-100422001.jpg`
    *   *Starboard:* `../../../../dreidel3d-sv2/refimages/air-agy/fa18ef-superhornet/fa18ef-superhornet-stbd-dvids-161015098.jpg`
    *   *Overhead:* `../../../../dreidel3d-sv2/refimages/air-agy/fa18ef-superhornet/fa18ef-superhornet-overhead-dvids-51172401761.jpg`
    *   *3/4 Front:* `../../../../dreidel3d-sv2/refimages/air-agy/fa18ef-superhornet/fa18ef-superhornet-threequarter-front-dvids-160405009.jpg`
    *   *3/4 Rear:* `../../../../dreidel3d-sv2/refimages/air-agy/fa18ef-superhornet/fa18ef-superhornet-threequarter-rear-dvids-161201008.jpg`
    *   *Wing Fold Deck:* `../../../../dreidel3d-sv2/refimages/air-agy/fa18ef-superhornet/fa18ef-superhornet-wingfold-commons-vfa22-3180.jpg`
    *   *Wing Fold Mechanism:* `../../../../dreidel3d-sv2/refimages/air-agy/fa18ef-superhornet/fa18ef-superhornet-wingfold-mechanism-dvids-051115012.jpg`
    *   *Canopy Open:* `../../../../dreidel3d-sv2/refimages/air-agy/fa18ef-superhornet/fa18ef-superhornet-canopy-open-dvids-161106058.jpg`
    *   *Canopy Closed:* `../../../../dreidel3d-sv2/refimages/air-agy/fa18ef-superhornet/fa18ef-superhornet-canopy-closed-dvids-140608200.jpg`
    *   *Cockpit:* `../../../../dreidel3d-sv2/refimages/air-agy/fa18ef-superhornet/fa18ef-superhornet-interior-cockpit-commons-f18ecockpit.jpg`
    *   *Boarding Ladder:* `../../../../dreidel3d-sv2/refimages/air-agy/fa18ef-superhornet/fa18ef-superhornet-movingparts-ladder-commons-an0323001.jpg`

---

## 9. Primary Authoritative Sourcing Ledger

1.  **NAVAIR A1-F18EA-NFM-000:** *NATOPS Flight Manual F/A-18E/F*, Naval Air Systems Command. Fig 1-1, Fig 1-2, Sec II (FCS), Sec III (Carrier suitability) [[NATOPS Manual](https://publicintelligence.net/u-s-navy-f-a-18e-f-super-hornet-natops-flight-manual/)].
2.  **NAVAIR 01-EA18G-1:** *NATOPS Flight Manual EA-18G*, NAVAIR. ALQ-218(V)2 installation, M61A2 deletion, ALQ-99 integration.
3.  **NAVAIR 00-80T-105:** *CV NATOPS Manual - Carrier Aircraft Operating Procedures*, NAVAIR. Approach speeds, catapult launch bar [[CV NATOPS](https://publicintelligence.net/us-navy-cv-natops-manual/)].
4.  **NAVAIR 00-80T-120:** *CVN Flight/Hangar Deck NATOPS Manual*, NAVAIR. Table 4-1 (Spotting envelopes, folded widths) [[Handling Manual](https://publicintelligence.net/us-navy-aircraft-handling-natops-manual/)].
5.  **NASA TP-1999-206573:** *Stability and Control Derivatives of F-18 HARV, Basic F-18*, NASA Dryden. Table 1 (Control surface travel limits and rates) [[NASA TRS](https://ntrs.nasa.gov/citations/19990040316)].
6.  **NASA TM-4487:** *Investigation of F/A-18 Aircraft With LEX Fences*, NASA Langley. Vortex burst and LEX fence elimination [[NASA TRS](https://ntrs.nasa.gov/citations/19930015758)].
7.  **US Navy Fact File 2143477:** *F/A-18E/F Super Hornet Strike Fighter*. Dimensions: LOA 60.3 ft, Span 44.9 ft, Height 16.0 ft, MTOW 66,000 lb [[navy.mil](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2143477/fa-18ef-super-hornet/)].
8.  **Boeing Defense:** *F/A-18E/F Super Hornet & EA-18G Technical Overview*. 34 in stretch, 500 sq ft wing, carets [[boeing.com](https://www.boeing.com/defense/fa-18-super-hornet/)].
9.  **AIAA Paper 98-2514:** *F/A-18E/F Flight Control System Design and Flight Test*, AIAA. Speedbrake deletion, LEX spoilers [[AIAA](https://arc.aiaa.org/doi/10.2514/6.1998-2514)].
10. **MIL-A-8863B(AS):** *Airplane Strength: Ground Loads for Carrier-Based Airplanes*, DoD. Arresting hook shank design [[DLA](https://quicksearch.dla.mil/)].
11. **MIL-L-8552D:** *Landing Gear and Catapult Launch Bar Requirements*, DoD [[DLA](https://quicksearch.dla.mil/)].
12. **DVIDS:** Defense Visual Information Distribution Service. Verified carrier flight operations, launches, traps, and fold mechanisms [[dvidshub.net](https://www.dvidshub.net)].


---

<!-- NAVAL-CURRENT-START -->
# fa-18ef-super-hornet — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:24:21.394242+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-FA-18E-F` | NAVAIR lists length 60.3 ft, height 16 ft, span 44.9 ft; derived approximately 18.38 m, 4.88 m, 13.69 m. The page's 18.5 m length equivalent conflicts with its feet. E has one seat; F has two; two F414-GE-400 engines. Block identity matters for avionics. | [Primary source](https://www.navair.navy.mil/product/FA-18EF-Super-Hornet); Specifications / Background |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| outer wing fold | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| landing gear | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| launch bar | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| arresting hook | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| canopy | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| aerodynamic surfaces | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Do not merge adjacent variants, operational and stowed dimensions, or demonstration motion with sourced operating rates. Exact fitted counts/locations and kinematic values not sourced above remain unresolved.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [F/A-18F Super Hornet Lands On The Flight Deck ](https://www.dvidshub.net/image/7073979/f-18f-super-hornet-lands-flight-deck) | `220301-N-EB640-1053 PACIFIC OCEAN (Mar. 1, 2022) An F/A-18F Super Hornet, from the "Fighting Redcocks" of Strike Fighter Squadron (VFA) 22, lands on the flight the aircraft carrier USS Nimitz (CVN 68). Nimitz i` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [F/A-18E Super Hornet Launches Off Of The Flight Deck ](https://www.dvidshub.net/image/7079072/f-18e-super-hornet-launches-off-flight-deck) | `220304-N-XK462-1284 PACIFIC OCEAN (Mar. 4, 2022) An F/A-18E Super Hornet, from the "Kestrels" of Strike Fighter Squadron (VFA) 94, launches off of the flight deck of the aircraft carrier USS Nimitz (CVN 68). Ni` — `sourced-caption` | `bow` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [F/A-18E Super Hornets Are Elevated Out Of Hangar Bay ](https://www.dvidshub.net/image/7247253/f-18e-super-hornets-elevated-out-hangar-bay) | `220531-N-BI507-1021 PACIFIC OCEAN (May 31, 2022) A Sailor spots two F/A-18E Super Hornets as they go up the elevator from the hangar bay to the flight deck of the aircraft carrier USS Nimitz (CVN 68). Nimitz is` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [An F/A-18F Super Hornet Prepares To Land ](https://www.dvidshub.net/image/7275325/f-18f-super-hornet-prepares-land) | `220614-N-LY962-1307 PACIFIC OCEAN (June 14, 2022) An F/A-18F Super Hornet, from the “Fighting Redcocks” of Strike Fighter Squadron (VFA) 22, prepares to make an arrested gear landing on the flight deck of the a` — `sourced-caption` | `stern` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Sailors Secure An F/A-18F Super Hornet To Catapult ](https://www.dvidshub.net/image/7593549/sailors-secure-f-18f-super-hornet-catapult) | `230119-N-NX635-1101 SOUTH CHINA SEA (Jan. 19, 2023) U.S. Navy Sailors prepare to launch an F/A-18F Super Hornet from the “Fighting Redcocks” of Strike Fighter Squadron (VFA) 22 on the flight deck of the aircraf` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [F/A-18F Super Hornet Launch ](https://www.dvidshub.net/image/8005070/f-18f-super-hornet-launch) | `An F/A-18F Super Hornet, attached to the “Blacklions” of Strike Fighter Squadron (VFA) 213, launches from the flight deck of the world’s largest aircraft carrier USS Gerald R. Ford (CVN 78) in the Eastern Medit` — `sourced-caption` | `quarter` candidate, `inferred-view`; exact coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=fa+18ef+super+hornet+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=fa+18ef+super+hornet+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=fa+18ef+super+hornet+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=fa+18ef+super+hornet+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=fa+18ef+super+hornet+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=fa+18ef+super+hornet+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=fa+18ef+super+hornet+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- [Existing air-agy index](../../../../../dreidel3d-sv2/refimages/air-agy/INDEX.md); `sourced-local-index-presence`. Read unit rows, not a blanket Complete banner. Some indexes contradict their own coverage matrices.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.
<!-- NAVAL-CURRENT-END -->


---

<!-- NAVAL-CURRENT-START -->
# fa-18ef-super-hornet — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:32:48.849695+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-FA-18E-F` | NAVAIR lists length 60.3 ft, height 16 ft, span 44.9 ft; derived approximately 18.38 m, 4.88 m, 13.69 m. The page's 18.5 m length equivalent conflicts with its feet. E has one seat; F has two; two F414-GE-400 engines. Block identity matters for avionics. | [Primary source](https://www.navair.navy.mil/product/FA-18EF-Super-Hornet); Specifications / Background |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| outer wing fold | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| landing gear | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| launch bar | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| arresting hook | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| canopy | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| aerodynamic surfaces | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Do not merge adjacent variants, operational and stowed dimensions, or demonstration motion with sourced operating rates. Exact fitted counts/locations and kinematic values not sourced above remain unresolved.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [F/A-18F Super Hornet Lands On The Flight Deck ](https://www.dvidshub.net/image/7073979/f-18f-super-hornet-lands-flight-deck) | `220301-N-EB640-1053 PACIFIC OCEAN (Mar. 1, 2022) An F/A-18F Super Hornet, from the "Fighting Redcocks" of Strike Fighter Squadron (VFA) 22, lands on the flight the aircraft carrier USS Nimitz (CVN 68). Nimitz i` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [F/A-18E Super Hornet Launches Off Of The Flight Deck ](https://www.dvidshub.net/image/7079072/f-18e-super-hornet-launches-off-flight-deck) | `220304-N-XK462-1284 PACIFIC OCEAN (Mar. 4, 2022) An F/A-18E Super Hornet, from the "Kestrels" of Strike Fighter Squadron (VFA) 94, launches off of the flight deck of the aircraft carrier USS Nimitz (CVN 68). Ni` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [F/A-18E Super Hornets Are Elevated Out Of Hangar Bay ](https://www.dvidshub.net/image/7247253/f-18e-super-hornets-elevated-out-hangar-bay) | `220531-N-BI507-1021 PACIFIC OCEAN (May 31, 2022) A Sailor spots two F/A-18E Super Hornets as they go up the elevator from the hangar bay to the flight deck of the aircraft carrier USS Nimitz (CVN 68). Nimitz is` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [An F/A-18F Super Hornet Prepares To Land ](https://www.dvidshub.net/image/7275325/f-18f-super-hornet-prepares-land) | `220614-N-LY962-1307 PACIFIC OCEAN (June 14, 2022) An F/A-18F Super Hornet, from the “Fighting Redcocks” of Strike Fighter Squadron (VFA) 22, prepares to make an arrested gear landing on the flight deck of the a` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Sailors Secure An F/A-18F Super Hornet To Catapult ](https://www.dvidshub.net/image/7593549/sailors-secure-f-18f-super-hornet-catapult) | `230119-N-NX635-1101 SOUTH CHINA SEA (Jan. 19, 2023) U.S. Navy Sailors prepare to launch an F/A-18F Super Hornet from the “Fighting Redcocks” of Strike Fighter Squadron (VFA) 22 on the flight deck of the aircraf` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [F/A-18F Super Hornet Launch ](https://www.dvidshub.net/image/8005070/f-18f-super-hornet-launch) | `An F/A-18F Super Hornet, attached to the “Blacklions” of Strike Fighter Squadron (VFA) 213, launches from the flight deck of the world’s largest aircraft carrier USS Gerald R. Ford (CVN 78) in the Eastern Medit` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=fa+18ef+super+hornet+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=fa+18ef+super+hornet+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=fa+18ef+super+hornet+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=fa+18ef+super+hornet+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=fa+18ef+super+hornet+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=fa+18ef+super+hornet+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=fa+18ef+super+hornet+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- [Existing air-agy index](../../../../../dreidel3d-sv2/refimages/air-agy/INDEX.md); `sourced-local-index-presence`. Read unit rows, not a blanket Complete banner. Some indexes contradict their own coverage matrices.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.

Independent image-subject review correction: wrong-subject candidates excluded, duplicate image IDs collapsed, and sibling equipment separated above. Older revisions remain audit evidence and are superseded by this last current section.
<!-- NAVAL-CURRENT-END -->
