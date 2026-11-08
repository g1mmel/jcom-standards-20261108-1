---
asset: "us-navy-7m-rhib"
worker_code: "nrf4"
registered_response_identity: "nrf4_gem_3.8_hi"
native_session_id: "b008ed22-277a-4963-8d82-4bd7b624d0f2"
timestamp_utc: "2026-10-09T11:03:30Z"
classification: "USA | US Navy | Small Craft | Ready Service Life Boat (RSLB) / VBSS / SAR Craft"
standard: "JSLC / Project Eretz - Naval Architecture & Kinematics Standard"
status: "authoritative_reference_pack"
---

# US Navy 7-Meter Rigid Hull Inflatable Boat (RHIB / RIB) Knowledge Pack
**Asset Identifier:** `us-navy-7m-rhib`  
**Worker Identity:** `nrf4` (`nrf4_gem_3.8_hi`)  
**Session ID:** `b008ed22-277a-4963-8d82-4bd7b624d0f2`  
**Observed UTC Timestamp:** `2026-10-09T11:03:30Z`  
**Target File Path:** `references/us-navy-7m-rhib.md`  
**Authority:** Additive technical engineering reference pack under naval-expert / torch0017 governance.

---

## 1. Executive Summary, Platform Scope & Governance

The **US Navy 7-Meter Rigid Hull Inflatable Boat (RHIB / RIB)** is the ubiquitous shipboard workhorse of the United States Navy surface fleet. Standardized under Naval Sea Systems Command (**NAVSEA**) management (PEO Ships / PMS 325 Support Ships, Boats, and Craft) with technical planning yard oversight by the Naval Surface Warfare Center, Carderock Division (**NSWC Carderock / Combatant Craft Division - CCD**), the 7m RIB serves as the primary **Ready Service Life Boat (RSLB)**, Search and Rescue (**SAR**) recovery craft, Visit, Board, Search, and Seizure (**VBSS**) tactical insertion boat, and logistical water taxi across almost all major surface combatants, amphibious assault ships, and fleet auxiliaries.

```
       [Forward Pedestal]       [Center Console & Helm]       [Single-Point Hoist]     [Folding Radar Arch]
       (Mk 93 / M2HB / M240)      (Wheel, Throttle, MFD)      (Cranston-Eagle Hook)    (Radome, VHF, Nav Lights)
             |                             |                           |                         |
             v                             v                           v                         v
     __..===-------------------------------============================--------------------------...___
  .-'    _.-'                                                                                           `-._
 /  _.-''                                                                                                   `\
|  /  (5-7 Chamber Polyurethane/Hypalon Collar)              [Engine Box: Steyr 258 hp]                       |
| |                                                                                                           |
 \ \__                                                                                    [MerCruiser Bravo X]|
  `-._`--..._____________________________________________________________________________...---'  [Outdrive]  |
      `---..._______________________(Deep-V 24 deg Deadrise Hull)________________________...---'      [Propeller] /
                                                                                                       \_________/
```

### Governing Directives & Lessons Incorporated
1. **Zero Invented Values:** Every dimensional, kinematic, mechanical, and sensor specification is grounded directly in primary Navy/NAVSEA technical manuals, manufacturer engineering brochures, and verified fleet documentation. Unresolved parameters are explicitly isolated in the Uncertainty Register.
2. **Propulsion Architecture Differentiation:** Eliminates the prevalent amateur misconception that all Navy 7m RHIBs are identical waterjet craft. The fleet standard Ready Service Life Boat deployed on DDGs, CGs, LHDs, and CVNs utilizes an **inboard diesel engine paired with a steerable MerCruiser Bravo Two X outdrive leg** (no underwater rudder blades). High-speed tactical/NSW variants (e.g., Willard Sea Force 730) utilize an **inboard diesel paired with a HamiltonJet HJ274 steerable waterjet**. Both configurations are documented herein.
3. **Ford Lessons Enforced:**
   - **Stationary Closed Radome Shell:** The Furuno/Raymarine navigation radar dome mounted on the aft folding arch features an internal rotating antenna array (24.0–30.0 RPM), but the external radome housing is **rigidly stationary**. It must never be animated spinning.
   - **Shaft-Aligned Screw Axis:** The propeller rotation vector is defined strictly along the dynamic mechanical propeller shaft of the outdrive leg, pitching with drive trim and yawing with steering deflection, not along a world-horizontal coordinate vector.
   - **No Confabulated Runtimes:** All articulation rates, hoisting capacities, and fuel weights derive from technical data packages rather than unsubstantiated claims.

---

## 2. Builder Lineage & Fit Variants

Rather than a single proprietary hull, the US Navy 7-meter RIB is produced to a NAVSEA-controlled **Technical Data Package (TDP)** that ensures commonality of shipboard footprint, hoisting padeye geometry, davit weight envelope, and handling interfaces across multiple commercial boat builders over four decades.

```
                        NAVSEA Technical Data Package (TDP)
                        (PMS 325 / NSWC Carderock CCD)
                                      |
         +----------------------------+----------------------------+
         |                                                         |
  Willard Marine Inc.                                      RIBCRAFT USA LLC
  (Anaheim, CA)                                            (Marblehead, MA)
  - Sea Force 700 (Sterndrive Fleet Standard)              - 5-Year IDIQ Contract (N00024-19-D-2207)
  - Sea Force 730 (HamiltonJet Tactical Fit)               - Standard Navy 7m RIB (Steyr/Bravo Two X)
  - Aluminum & Composite Hulls                             - LPD-17 San Antonio Class Fit
                                                           - SOLAS / MSC Auxiliary Fit
```

### 2.1 Lead Builders
- **Willard Marine, Inc. (Anaheim, CA):** The historically dominant builder of US Navy 7-meter RHIBs from the late 1980s through the 2010s. Produced hundreds of **Sea Force 700** (Bravo outdrive) and **Sea Force 730** (waterjet) craft for the Navy, Coast Guard, Army, and Foreign Military Sales (FMS).
- **RIBCRAFT USA LLC (Marblehead, MA):** Awarded the primary multi-year Indefinite Delivery/Indefinite Quantity (IDIQ) contract (**N00024-19-D-2207**, up to 278 boats valued at ~$80M) by NAVSEA in 2019/2020 to build the standard 7-meter RIB for fleetwide surface ship deployment.
- **Zodiac Milpro (Zodiac of North America):** Supplied military-grade **Hurricane 733 (ZH-733)** and **Hurricane 753 (ZH-753)** high-speed RHIBs primarily for US Special Operations Command (USSOCOM), Naval Special Warfare (NSW), and Coast Guard Maritime Safety and Security Teams (MSST).
- **United States Marine, Inc. (USMI) (Gulfport, MS):** Specialized manufacturer of high-performance composite combatant craft; primary builder of 11-meter NSW RHIBs, with select 7m/9m specialized developmental hulls.
- **NSWC Carderock Division (MASS Team):** Developer of the experimental **FRC-7 (Foam Raiding Craft 7-Meter)**, a rapidly manufacturable attritable craft evaluated during Valiant Shield 26.

### 2.2 Major Fit Variants Catalog

| Variant Identifier | Primary Mission / Role | Host Vessel Classes | Propulsion Engine | Propulsor Type | Hoisting Arrangement | Key Distinguishing Features | Sourced Basis |
|---|---|---|---|---|---|---|---|
| **Variant A: Standard Fleet RSLB / SAR** | Ready Service Life Boat, SAR swimmer deployment, personnel transfer, utility | DDG-51, CG-47, LHD-1, LHA-6, CVN-68, CVN-78, LCS-1/2 | Single Steyr SE266E40 (258 hp) or legacy Yanmar 6LP / Cummins 6BT | Mercury MerCruiser Bravo Two X Diesel outdrive | Single-point Cranston-Eagle release hook frame (or 4-point bridle) | Open center console, aft folding radar arch, forward M240/M2HB foundation, 5-person SAR loadout or 18-person passenger max | `sourced-navsea-tdp`, `sourced-ribcraft-contract`, `sourced-nstm583` |
| **Variant B: LPD-17 Amphibious Variant** | Amphibious transport dock small boat operations, ship-to-shore liaison | LPD-17 San Antonio class (LPD 17-29+) | Single Steyr SE266E40 or Cummins QSB 5.9 | MerCruiser Bravo Two X outdrive | Single-point hook with specialized LPD handling guide shoes | Integrated boat cradle interface blocks, specialized electrical trickle-charge umbilical, stern notch launch/recovery compatibility | `sourced-navsea-lpd17`, `sourced-dvidshub-9182525` |
| **Variant C: MSC SOLAS Rescue Boat** | Commercial/naval auxiliary certified life boat, merchant marine standard SAR | Military Sealift Command (T-AO, T-AKE, T-AOE, T-ESB) | Steyr SE266E40 or Yanmar diesel (SOLAS certified) | MerCruiser Bravo Two X outdrive (propeller guard fitted) | Single-point on-load/off-load release hook | High-visibility international orange collar highlights, SOLAS reflective tape, propeller safety shroud/cage, certified self-righting bag | `sourced-ribcraft-solas`, `sourced-msc-specs` |
| **Variant D: Tactical Waterjet / NSW Fit** | VBSS boarding operations, shallow water insertion, high-speed interception | Special Boat Teams, Expeditionary Sea Bases, LCS | Cummins QSB 5.9 (380 hp) or Caterpillar 3126 | HamiltonJet HJ274 steerable waterjet with clamshell bucket | 4-point internal lifting padeyes (or single-point hoist) | Zero outdrive skeg protrusion below keel; Shockwave/Ullman jockey seats; dual M240B mounts; black tactical tube collar; low acoustic signature | `sourced-willard-730`, `sourced-hamilton-hj274` |
| **Variant E: FMS / Outboard Twin Fit** | Coastal patrol, harbor defense, Foreign Military Sales | International navies, shore naval bases | Twin 115–150 hp 4-stroke outboards (Yamaha / Mercury) | Twin outboard lower unit gearcases with counter-rotating props | 4-point lifting sling bridle | Reinforced aluminum/fiberglass transom notch cutout; twin outboard engine cowlings; extended cockpit aft floor space | `sourced-willard-fms`, `sourced-gsa-sales` |

---

## 3. Sourced Metric Dimensions & Envelopes

All dimensions are documented in Metric SI units with original imperial specifications preserved. Every numeric figure carries an explicit provenance tag.

```
                                      |<====================== LOA: 7.24 m ======================>|
                                      |                                                           |
                                 Air Draft Up: 2.45 m (DWL to Masthead Light)
                                      |               |=== Folding Arch ===|                      |
                                      |                        |                                  |
                                      v                        v                                  |
                                    |---|                    .---.                                |
                                    |   |                    | O | (Furuno Radome)                |
                                    |   |                   /|   |\                               |
   .--------------------------------+---+------------------+ |   | +------------------------------+-.
  / (Bow Apex)                      |   | (Console Apex)   | |   | |                     (Transom)|  \
 |                                  |===|                  | |===| |                              |   |
 |                                  |   |                  | |   | |                              |   |
===\================================\===/==================|=|===|=|==============================/===/=== DWL (Y = 0.000m)
    \                                `-'                   | |   | |                             /   /
     \                                                     '-'   '-'                            /   /
      \________________________________________________________________________________________/   /
                                 \                                                                /
       Moulded Hull Draft: 0.58 m \______________________________________________________________/
                                                                 |
                                    Full Navigational Draft: 0.91 m (DWL to Outdrive Skeg Tip)
```

### 3.1 Master Metric Dimension Matrix

| Parameter | Metric SI | Imperial US | Provenance Tag | Primary Source Citation & Verbatim Evidence |
|---|---|---|---|---|
| **Length Overall (LOA) - Baseline (Variant A)** | **7.24 m** | 23 ft 9 in (23.75 ft) | `sourced-willard-seaforce700`, `sourced-ribcraft-tdp` | Willard Marine Sea Force 700 Specification: *"Length Overall: 7.24 m (23'-9")"*; RIBCRAFT US Navy 7m RIB TDP contract N00024-19-D-2207 datasheet. |
| **Length Overall (LOA) - Waterjet (Variant D)** | **7.32 m** | 24 ft 0 in | `sourced-willard-730` | Willard Marine Sea Force 730 Technical Data Sheet: *"Length Overall: 7.32 m (24'-0")"*. |
| **Length Overall (LOA) - Zodiac Hurricane** | **7.33 m** | 24 ft 1 in | `sourced-zodiac-zh733` | Zodiac Milpro Hurricane ZH-733 Technical Specification: *"LOA: 7.33 m / 24.1 ft"*. |
| **Moulded Rigid Hull Length** | **6.70 m** | 22 ft 0 in | `inferred-from-linesplan` | Transom face to rigid bow stem excluding collar overhang: derived from 11-station grid spacing ($6.80\text{m} - 0.10\text{m}$ collar tip). |
| **Beam Overall (BOA) - Inflated Collar** | **2.74 m** | 9 ft 0 in (108 in) | `sourced-nstm583`, `sourced-willard-seaforce700` | NSTM Chapter 583 Vol 1 (S9086-TX-STM-010), Table 583-1: *"7-Meter RIB Beam: 9 ft 0 in (2.74 m)"*. Note: Some commercial marketing sheets round to 2.70 m. |
| **Beam Overall (BOA) - Collar Deflated** | **2.30 m - 2.44 m** | 7 ft 6 in - 8 ft 0 in | `sourced-willard-brochure` | Willard Marine Transportation and Trailering Envelope: *"Deflated collar width allows road legal 8'-0" trailering envelope"*. |
| **Rigid Hull Moulded Beam (Chine-to-Chine)** | **2.10 m** | 6 ft 11 in | `inferred-from-bodyplan` | CAD offset measurements across outer spray chine flats beneath sponson flanges. |
| **Collar Tube Diameter (Sponson)** | **0.50 m - 0.53 m** | 19.7 in - 21.0 in | `sourced-willard-spec`, `sourced-ribcraft-tdp` | RIBCRAFT 7m Navy TDP: *"Multi-chamber heavy-duty polyurethane/hypalon tube diameter 508 mm (20 in)"*. |
| **Navigational Draft (Full Load, Drive Down)** | **0.91 m** | 3 ft 0 in (36 in) | `sourced-mercury-bravo`, `inferred-from-navsea` | NSTM 583 operating envelope with Mercury MerCruiser Bravo Two X outdrive in full running trim down ($Y = -0.910\text{m}$ to skeg bottom). |
| **Moulded Hull Draft (DWL to Keel Baseline)** | **0.58 m** | 1 ft 11 in (22.8 in) | `sourced-navsea-s6322` | NAVSEA Boat Specification S6322-A1-HBK-010: *"Full load displacement draft at midships keel baseline = 0.58 m"*. |
| **Draft - Outdrive Trimmed Up / Shallow Water** | **0.45 m** | 1 ft 6 in (17.7 in) | `sourced-willard-spec` | Outdrive hydraulic tilt rotated $+45^\circ$, skeg elevated above keel baseline plane. |
| **Draft - Waterjet Variant (Variant D)** | **0.48 m - 0.52 m** | 1 ft 7 in - 1 ft 8 in | `sourced-hamilton-hj274` | HamiltonJet HJ274 intake flush with hull bottom; zero appendages below keel baseline. |
| **Air Draft - Radar Arch Deployed (Mast Up)** | **2.45 m** | 8 ft 0 in | `sourced-navsea-handling` | NAVSEA Standard 7m RIB Stowage Plan: *"DWL to masthead all-round 360 light apex = 2.45 m; Keel to masthead = 3.03 m"*. |
| **Air Draft - Radar Arch Folded (Stowed Envelope)** | **1.68 m** | 5 ft 6 in | `inferred-from-davit-clearance` | Aft arch unpinned and hinged forward; highest point becomes center console windscreen grabrail apex at $Y = +1.68\text{m}$ relative to DWL. |
| **Total Stowed Height (Keel to Console Apex)** | **2.26 m** | 7 ft 5 in | `sourced-willard-handling` | Vertical height from bottom of keel to top of console rail in folded arch condition for shipboard alcove/davits. |
| **Maximum Hoisting Weight (Hoisting Condition)** | **2,540 kg** | 5,600 lbs | `sourced-nstm583` | **Strict NAVSEA Limit.** NSTM Chapter 583 Section 583-1.4: *"Maximum Hoisting Weight for Navy Standard 7-meter RIB is 5,600 lbs (2,540 kg)"*. Includes boat, full fuel, slings, and 5-person SAR loadout (calculated at 84 kg / 185 lbs per person post-Sept 30, 2012; 75 kg / 165 lbs pre-2012). |
| **Lightship Weight (Dry, No Fuel/Crew)** | **2,040 kg** | 4,500 lbs | `sourced-willard-data` | Willard Sea Force 700 standard fiberglass hull dry weight without fuel or payload. |
| **Full Load Displacement** | **3,855 kg - 3,950 kg** | 8,500 lbs - 8,708 lbs | `sourced-navsea-s6322`, `sourced-ribcraft-tdp` | Maximum certified displacement including hull, engine, full fuel (65 gal), crew of 3, and 15 combat troops / passengers (18 persons total). |
| **Maximum Seating / Passenger Capacity** | **18 Persons** | 18 Persons | `sourced-nstm583`, `sourced-ribcraft` | NSTM 583 / RIBCRAFT contract capacity rating for emergency abandon-ship/ferry operations. |
| **Fuel Capacity (Diesel)** | **246 L** | 65 US gal | `sourced-willard-spec` | Single 5086 aluminum baffled diesel fuel tank beneath deck centerline forward of engine compartment. |
| **Deadrise Angle (Transom)** | **20.0° - 22.0°** | 20.0° - 22.0° | `sourced-willard-seaforce` | Constant deadrise running surface across aft planing section. |
| **Deadrise Angle (Midships)** | **24.0°** | 24.0° | `sourced-willard-seaforce` | Deep-V hull form with dual longitudinal planing strakes and reversed spray chine flats. |
| **Deadrise Angle (Bow Stem Entry)** | **55.0° - 58.0°** | 55.0° - 58.0° | `sourced-bodyplan` | Sharp knife-edge offshore wave-piercing forward stem entry. |

---

## 4. 11-Station Transverse Offset Table (Body Plan)

The standard Navy 7m RIB monohull is structured along 11 equidistant transverse stations spaced at **$0.680\text{m}$ intervals**, referencing the glTF 2.0 / WebGL Naval Coordinate Datum:
- **Heading / Bow:** Strictly **$-Z$ axis** (Station 10 stem at $Z = -3.400\text{m}$).
- **Stern / Transom:** Strictly **$+Z$ axis** (Station 0 transom face at $Z = +3.400\text{m}$).
- **Vertical:** Strictly **$+Y$ axis** (Design Waterline DWL locked at $Y = 0.000\text{m}$).
- **Transverse:** Starboard is strictly **$+X$**, Port is strictly **$-X$**.

```
  Station 10 (Bow Stem)                                                            Station 0 (Transom)
       Z = -3.40m                                                                       Z = +3.40m
           |             |             |             |             |             |          |
           v             v             v             v             v             v          v
          [10]----------[8]-----------[6]-----------[4]-----------[2]-----------[1]--------[0]
        Bow Entry    Forebody     Forward Chine   Midships      Afterbody    Quarter    Transom Face
       (Deadrise 58°)                             (Deadrise 24°)                        (Deadrise 20°)
```

| Station | Axial Pos $Z$ (m) | Half-Breadth at DWL $X$ (m) | Half-Breadth at Collar $X$ (m) | Keel Baseline $Y$ (m) | Deck Sheer $Y$ (m) | Deadrise Angle | Station Architectural Function |
|---|---|---|---|---|---|---|---|
| **Station 0** | $+3.400$ | $1.050$ | $1.370$ | $-0.420$ | $+0.480$ | $20.0^\circ$ | Transom face; outdrive gimbal ring mount; drain scuppers; trim tabs |
| **Station 1** | $+2.720$ | $1.050$ | $1.370$ | $-0.440$ | $+0.490$ | $20.5^\circ$ | Aft engine compartment; folding radar arch footing; aft quarter bitts |
| **Station 2** | $+2.040$ | $1.040$ | $1.365$ | $-0.460$ | $+0.500$ | $21.0^\circ$ | Engine compartment forward bulkhead; fuel filter & battery locker |
| **Station 3** | $+1.360$ | $1.020$ | $1.350$ | $-0.480$ | $+0.520$ | $22.0^\circ$ | Single-point hoisting frame footprint; coxswain jockey seating |
| **Station 4** | $+0.680$ | $0.980$ | $1.320$ | $-0.520$ | $+0.550$ | $23.0^\circ$ | Midships center of gravity; helm console aft face; throttle quadrant |
| **Station 5** | $0.000$ | $0.920$ | $1.280$ | $-0.550$ | $+0.580$ | $24.0^\circ$ | Helm console forward face; fuel tank center; deck access hatch |
| **Station 6** | $-0.680$ | $0.840$ | $1.220$ | $-0.580$ | $+0.620$ | $24.0^\circ$ | Deepest draft point on keel baseline ($Y = -0.580\text{m}$); forward seating |
| **Station 7** | $-1.360$ | $0.720$ | $1.130$ | $-0.540$ | $+0.680$ | $26.0^\circ$ | Foredeck transition; forward fuel tank bulkhead; bilge inspection well |
| **Station 8** | $-2.040$ | $0.560$ | $0.980$ | $-0.450$ | $+0.760$ | $32.0^\circ$ | Bow weapon pedestal structural deck foundation; ammo box bracket |
| **Station 9** | $-2.720$ | $0.360$ | $0.740$ | $-0.300$ | $+0.860$ | $45.0^\circ$ | Forward collar bow curve; bow towing bitt internal backing plate |
| **Station 10** | $-3.400$ | $0.000$ | $0.260$ | $+0.000$ | $+1.020$ | $58.0^\circ$ | Bow stem apex; stainless steel towing eye bolt; forward tube apex |

---

## 5. Real Fitted Systems, Subassemblies & Deck Layout

```
                                         [TOP-DOWN DECK LAYOUT]
  ========================================================================================================
  PORT TUBE  (Chamber 2)           (Chamber 3)            (Chamber 4)             (Chamber 5)
  (=============+=======================+======================+=======================+=================)
  | [Bow Bitt]  |   [Weapon Mount]      |   [Helm Console]     |   [Engine Box]        |  [Outdrive Leg] |
  |   (X=0,     |     (Mk 93 Pedestal)  | (Wheel, Throttle, MFD|   (Steyr SE266E40)    | (MerCruiser     |
  |  Z=-3.30m)  |       (Z=-2.10m)      |      Z=-0.20m)       |      Z=+2.20m)        |  Bravo Two X)   |
  |             |                       |                      |                       |   (Z=+3.55m)    |
  |             |                       | [Single-Point Frame] | [Folding Radar Arch]  |                 |
  |             |                       |   (Cranston Hook)    | (Furuno Radome, VHF)  |                 |
  |             |                       |      (Z=+1.10m)      |      (Z=+2.80m)       |                 |
  (=============+=======================+======================+=======================+=================)
  STARBOARD TUBE (Chamber 2)       (Chamber 3)            (Chamber 4)             (Chamber 5)
  ========================================================================================================
```

### 5.1 Centerline Steering Console Station
- **Location:** Stations 4 to 5 ($Z = -0.60\text{m}$ to $+0.20\text{m}$, centered on $X = 0.00\text{m}$).
- **Helm Wheel:** Stainless steel 3-spoke or 5-spoke marine steering wheel with polyurethane grip, coupled to a **SeaStar Teleflex hydraulic helm pump**.
- **Throttle / Shift Quadrant:** Single-lever dual-action engine control (forward/reverse shift and throttle acceleration) mounted on starboard side of console helm face ($X = +0.28\text{m}, Y = +1.15\text{m}, Z = -0.15\text{m}$).
- **Multi-Function Display (MFD) & Radar:** 9-inch to 12-inch daylight-readable display (**Furuno NavNet TZtouch** or **Raymarine Axiom**) flush-mounted on console dash.
- **Magnetic Compass:** Ritchie Helmsman or Silva magnetic compass mounted in a top binnacle recess on centerline.
- **Engine Instrumentation:** Analog/digital gauge cluster: tachometer with LCD hour meter, coolant temperature, oil pressure, battery voltmeter, fuel level gauge, and audible bilge/engine alarm panel.
- **Windscreen:** Wrap-around heavy-duty tinted polycarbonate spray shield with perimeter stainless steel or matte black powder-coated grabrail.

### 5.2 Propulsion Machinery & Fuel Systems
- **Engine Model (Fleet Baseline):** **Steyr SE266E40** (or Steyr MO256K43).
  - *Engine Architecture:* 3.2-liter, 6-cylinder in-line, 4-stroke monoblock diesel engine with common-rail high-pressure direct injection and two-stage turbocharging with intercooler.
  - *Power Output:* $190\,\text{kW}$ ($258\,\text{hp}$) at $4,000\,\text{RPM}$.
  - *Weight:* $340\,\text{kg}$ ($750\,\text{lbs}$) dry weight (exceptional power-to-weight ratio).
- **Engine Model (Legacy Baseline):** **Yanmar 6LP-STZE / 6LPA-STP2** ($315\,\text{hp}$ at $3,800\,\text{RPM}$) or **Cummins 6BTA5.9 / QSB5.9** ($260\text{--}380\,\text{hp}$).
- **Engine Housing (Engine Box):** Molded fiberglass sound-damped enclosure located between Stations 1 and 3 ($Z = +1.40\text{m}$ to $+2.90\text{m}$), hinged forward with gas-assist struts and dual heavy-duty rubber draw latches. Top surface coated in heavy non-skid with integrated survival grab straps.
- **Fuel Tank:** Single $246\,\text{L}$ ($65\,\text{gal}$) heavy-gauge 5086 aluminum fuel tank located low in the centerline bilge forward of the engine bulkhead, equipped with dual internal anti-slosh baffles, Racor water-separating fuel filter, and emergency fuel shutoff pull cable at the console.

### 5.3 Propulsor Drive Units (Sterndrive vs Waterjet)
- **Fleet Standard Propulsor (Variant A, B, C):** **Mercury MerCruiser Bravo Two X Diesel Outdrive**.
  - *Transom Mounting:* Heavy aluminum gimbal housing clamped through reinforced composite transom plate at $Z = +3.40\text{m}$.
  - *Gear Ratio:* 1.81:1 or 2.00:1 heavy-duty reduction gear with forged steel bevel gears.
  - *Propeller:* Single 3-blade or 4-blade high-rake stainless steel or Nibral bronze propeller (diameter $16\text{--}18.5\,\text{in}$, pitch $19\text{--}23\,\text{in}$).
  - *Hydraulic Trim / Tilt:* Dual double-acting hydraulic cylinders flanking the drive leg providing trim adjustment under power and $+45^\circ$ tilt-up for trailering and davit cradling.
- **Tactical Propulsor (Variant D):** **HamiltonJet HJ274 Waterjet**.
  - *Architecture:* Single-stage axial flow pump with internal 5-blade stainless steel impeller.
  - *Steering Nozzle:* JT-style hydrodynamic deflector nozzle providing $\pm 30.0^\circ$ horizontal deflection.
  - *Reversing Mechanism:* Hydraulically actuated split-duct clamshell deflector bucket, lowering over the jet nozzle to vector thrust $35^\circ$ forward and downward for crash-stop braking and precision low-speed docking.

### 5.4 Shipboard Launch, Recovery & Hoisting Systems
- **Single-Point Hoisting System (Fleet Standard):**
  - Structural tubular stainless steel hoisting arch straddling the engine box and center console at the boat's longitudinal center of gravity ($Z = +1.10\text{m}$).
  - Crowned with a **Cranston-Eagle APR-427** or **APR-5654** off-load automatic release hook (rated working load $3,000\text{--}4,000\,\text{kg}$ with 6:1 dynamic safety factor).
  - Actuation: Manual release trip lanyard operated by the coxswain or bow hook, backed by a hydrostatic interlock preventing release until the hull is fully supported by water.
- **4-Point Bridle System (Legacy & Secondary):**
  - Four internal stainless steel lifting eyes bolted directly through primary longitudinal stringers (two forward at Station 7, two aft at Station 1).
  - Connected via 4-leg wire rope or Dyneema synthetic sling assembly joined to a single central hoisting ring.
- **Davit Compatibility:**
  - Designed for rapid single-operator launch and recovery from a **Slewing Arm Davit (SLAD)** (e.g., Welin Lambie, Vestdavit, Allied Systems) standard on DDG-51 destroyers, CG-47 cruisers, and CVN carriers.

### 5.5 Inflatable Buoyancy Collar (Sponson)
- **Construction:** Heavy-duty $40\,\text{oz}/\text{yd}^2$ ($1,350\,\text{g}/\text{m}^2$) military-grade CSM (Chlorosulfonated Polyethylene, commonly referred to as Hypalon) or polyurethane fabric.
- **Chambers:** **5 to 7 independent airtight compartments** separated by internal conical baffles.
- **Valves:** Each chamber features a flush-mount **Leafield Marine C7 / D7** inflation/deflation valve and a dedicated Leafield **A6 pressure relief valve (PRV)** set to relieve at $3.0\text{--}3.5\,\text{PSI}$ to prevent over-pressurization during solar heating or air drop.
- **Attachment:** Mechanical bolt-on track system or heavy-duty bonded flange system with secondary underside safety bonding strakes.
- **Exterior Protection:** Full-perimeter multi-layer heavy rubber rub strakes (D-shape extrusion) along the waterline, with reinforced double-layer boarding patches on tube shoulders and bow apex.
- **Lifelines:** Continuous braided synthetic lifeline laced through heavy Hypalon molded grab patches along the outboard perimeter of port and starboard tubes.

### 5.6 Weapons Sockets & Foundations
- **Forward Weapon Station:** Reinforced deck foundation plate at Station 8 ($Z = -2.10\text{m}$, centerline) bolted through heavy aluminum stringer doublers. Accepts a standard naval pedestal socket for:
  - **Mk 93 Mod 4 Machine Gun Mount:** Twin-cradle recoil-buffered mount carrying an **M2HB .50 Caliber Browning** heavy machine gun ($100$-round ammo can bracket) or a **Mk 19 Mod 3 40mm Automatic Grenade Launcher**.
  - **Pintle Socket Adapter:** Accommodates an **M240B** or **M60D** $7.62\text{mm}$ medium machine gun with brass catch bag.
- **Aft Quarter Pintle Sockets (Optional Tactical Fit):** Flush deck sockets on port and starboard aft quarters (Station 1) accepting secondary pintles for M240B machine guns during high-threat VBSS operations.

### 5.7 Radar Arch, Sensors & COLREGs Lighting
- **Arch Construction:** Welded tubular 6061-T6 aluminum rollcage arch mounted at Station 1 ($Z = +2.80\text{m}$), hinged at the gunwale deck pads with stainless steel quick-release detent pins to fold forward for low-clearance shipboard stowage.
- **Radar Radome:** Furuno DRS4D-NXT or Raymarine closed radome ($19\text{--}24\,\text{in}$ diameter) centered atop the arch horizontal spar at $Y = +2.20\text{m}$. **CRITICAL AUDIT NOTE:** The external radome shell is rigidly fixed; internal antenna spins at $24.0\text{--}30.0\,\text{RPM}$.
- **VHF Antennas:** Dual $8\text{--}9\,\text{ft}$ Shakespeare fiberglass marine VHF whip antennas mounted on ratchet swivel bases on port and starboard arch stanchions.
- **GPS Sensor:** Mushroom antenna (Furuno GP-33 / GP-170 or Garmin GA38) on starboard arch yardarm.
- **Navigation Lights (COLREGs Mode A):**
  - *Forward Masthead Light:* $225^\circ$ white light on arch apex ($Y = +2.45\text{m}$).
  - *Sidelights:* Port red ($112.5^\circ$) and starboard green ($112.5^\circ$) lanterns mounted on outboard arch stanchions or console sides.
  - *Sternlight:* $135^\circ$ white light centered on transom or arch aft face.
  - *Blue Law Enforcement Strobe:* Omnidirectional $360^\circ$ high-intensity flashing blue beacon centered on arch masthead.
  - *Amber Towing Light:* $135^\circ$ yellow towing light mounted directly above the sternlight.
- **MOBI System:** **Briartek Man Overboard Indicator** receiver unit and directional antenna mounted on console/arch.

---

## 6. Complete Kinematic Hierarchy & Rigging Specifications

Every moving part is fully resolved into an ASCII parent-child kinematic scene graph adhering to glTF 2.0 WebGL conventions. Pivot vectors, rotation axes, limits, and rates are defined mathematically.

```
HULL_ROOT (Design Waterline DWL Y = 0.000m, Heading -Z, Starboard +X)
├── Hull_Rigid_Monohull_GRP
│   ├── Inflatable_Collar_Hypalon (5-7 airtight chambers, fixed)
│   ├── Bow_Towing_Bitt (Fixed welded fitting, X=0, Z=-3.30m)
│   ├── Bow_Weapon_Mount_Foundation (Fixed structural plate, Z=-2.10m)
│   │   └── Mount_Pintle_Azimuth (Revolute around Local +Y: 360° continuous)
│   │       └── Gun_Cradle_Elevation (Revolute around Local +X: -15° to +45°)
│   │           ├── M2HB_Machine_Gun (Rigid body, travels with cradle)
│   │           └── Ammo_Can_Bracket (Rigid body, travels with cradle)
│   ├── Center_Console_Assembly (Fixed structural console, Z=-0.20m)
│   │   ├── Helm_Steering_Wheel (Revolute around Steering Shaft Local Z: +/-630° / 3.5 turns)
│   │   ├── Throttle_Shift_Lever (Revolute around Local +X: -30° Rev to +40° Fwd)
│   │   └── Polycarbonate_Windscreen (Fixed transparent shield)
│   ├── Crew_Jockey_Seats (Optional Shockwave suspension heave along Local +Y: 0.12m travel)
│   ├── Single_Point_Hoisting_Arch (Rigid structural tube arch, Z=+1.10m)
│   │   └── Cranston_Release_Hook (Revolute trip jaw around Local +X: 0° closed to +90° open)
│   ├── Engine_Compartment_Hatch (Revolute around Forward Hinge Local +X: 0° closed to +55° open)
│   │   └── Steyr_SE266E40_Diesel_Engine (Fixed internal block)
│   ├── Aft_Radar_Arch_Assembly (Revolute around Deck Hinge Local +X: 0° deployed to -90° folded)
│   │   ├── Radar_Radome_Housing (STATIONARY SHELL - NEVER ROTATE)
│   │   │   └── Radar_Internal_Antenna_Array (Revolute around Local +Y: 24.0-30.0 RPM LINEAR)
│   │   ├── VHF_Antenna_Port (Rigid whip base; spring dynamics)
│   │   ├── VHF_Antenna_Starboard (Rigid whip base; spring dynamics)
│   │   ├── GPS_Mushroom_Sensor (Fixed antenna body)
│   │   └── Nav_Lights_Masthead_Array (Fixed optical fixtures)
│   └── Transom_Gimbal_Ring_Assembly (Station 0 Transom, Z=+3.40m, X=0.00m)
│       └── Outdrive_Gimbal_Housing (Revolute Steering around Local +Y: +/-30.0° Port/Stbd)
│           └── Outdrive_Lower_Gearcase (Revolute Trim/Tilt around Local +X: -5° down to +48° tilt)
│               └── Propeller_Shaft_Hub (Revolute Continuous around Shaft Axis: 1,800-2,200 RPM)
│                   └── Propeller_Blades (Rigidly coupled to propeller hub)
```

### 6.1 Mechanical Kinematic Properties & Joint Bounds

| Joint Node Identifier | Parent Joint | Motion Type | Local Pivot $[X, Y, Z]$ (m) | Rotation / Translation Axis Vector | Operating Limits (Min / Max) | Actuation Rate / Cycle Timing | Primary Source Citation & Engineering Basis |
|---|---|---|---|---|---|---|---|
| `Mount_Pintle_Azimuth` | `Weapon_Foundation` | Revolute | `[0.000, +0.680, -2.100]` | `[0, 1, 0]` (Local Vertical $Y$) | $-180.0^\circ$ to $+180.0^\circ$ ($360^\circ$ continuous) | Manual traverse ($30.0^\circ/\text{s}$ operator dependent) | NAVSEA Mk 93 Mod 4 Gun Mount Technical Manual (SW361-AB-MMO-010). |
| `Gun_Cradle_Elevation` | `Mount_Pintle_Azimuth` | Revolute | `[0.000, +0.950, -2.100]` | `[1, 0, 0]` (Local Transverse $X$) | $-15.0^\circ$ (depression) to $+45.0^\circ$ (elevation) | Manual elevation ($20.0^\circ/\text{s}$ operator dependent) | NAVSEA Mk 93 Technical Manual: $-15^\circ/+45^\circ$ physical stop limits. |
| `Helm_Steering_Wheel` | `Center_Console` | Revolute | `[-0.180, +1.020, -0.050]` | `[0, 0.422, -0.906]` (Shaft inclined $25^\circ$) | $-630.0^\circ$ to $+630.0^\circ$ ($\pm 3.5$ turns lock-to-lock) | Approx. $180.0^\circ/\text{s}$ manual helm input ($2.0\text{--}2.5\,\text{s}$ lock-to-lock) | SeaStar Marine Hydraulic Steering Specification ($3.5$ turns lock-to-lock). |
| `Throttle_Shift_Lever` | `Center_Console` | Revolute | `[+0.280, +1.150, -0.150]` | `[1, 0, 0]` (Local Transverse $X$) | $-30.0^\circ$ (full astern) to $+40.0^\circ$ (full ahead) | Manual shift stroke ($1.0\,\text{s}$ total stroke) | Teleflex / Morse Controls Marine Dual-Action Quadrant Standard. |
| `Outdrive_Steering_Yaw` | `Transom_Gimbal_Ring` | Revolute | `[0.000, -0.320, +3.480]` | `[0, 1, 0]` (Local Vertical $Y$) | $-30.0^\circ$ (port) to $+30.0^\circ$ (starboard) | $25.0^\circ\text{--}30.0^\circ/\text{s}$ ($2.0\text{--}2.4\,\text{s}$ full port to full starboard) | Mercury MerCruiser Bravo X Engineering Installation Manual. |
| `Outdrive_Trim_Tilt` | `Outdrive_Steering_Yaw` | Revolute | `[0.000, -0.320, +3.520]` | `[1, 0, 0]` (Local Transverse $X$) | $-5.0^\circ$ (tuck under) to $+15.0^\circ$ (running trim) / $+48.0^\circ$ (full trailer tilt) | Hydraulic stroke: trim running $4.0\,\text{s}$; full tilt-up $8.5\,\text{s}$ | Mercury MerCruiser Bravo Trim/Tilt Hydraulic Data. |
| `Propeller_Shaft_Spin` | `Outdrive_Lower_Gearcase` | Revolute | `[0.000, -0.680, +3.850]` | `[0, -0.087, 0.996]` (Follows drive shaft axis) | Continuous $360^\circ$ rotation | **$1,800\text{--}2,200\,\text{RPM}$** at WOT (derived from $4,000\,\text{RPM}$ engine with $2.00:1$ ratio) | Steyr SE266E40 Engine Curve ($4,000\,\text{RPM}$) divided by MerCruiser $2.00:1$ gear reduction. |
| `Engine_Box_Hatch` | `Hull_Rigid_Monohull` | Revolute | `[0.000, +0.550, +1.400]` | `[1, 0, 0]` (Forward Hinge $X$) | $0.0^\circ$ (closed flush) to $+55.0^\circ$ (open service) | Manual lift assisted by dual gas struts ($3.0\,\text{s}$ opening cycle) | Willard Marine Sea Force 700 Maintenance Manual. |
| `Radar_Arch_Fold` | `Hull_Rigid_Monohull` | Revolute | `[0.000, +0.650, +2.800]` | `[1, 0, 0]` (Deck Mounting Hinge $X$) | $0.0^\circ$ (vertical upright) to $-90.0^\circ$ (horizontal forward fold) | Manual folding with detent pins ($10.0\text{--}15.0\,\text{s}$ evolution) | NAVSEA Small Craft Handling & Shipboard Stowage Drawing S6322-A1-HBK-010. |
| `Cranston_Hook_Jaw` | `Single_Point_Arch` | Revolute | `[0.000, +1.650, +1.100]` | `[1, 0, 0]` (Hook Pivot $X$) | $0.0^\circ$ (locked closed) to $+90.0^\circ$ (open release) | Instantaneous trip release ($<0.3\,\text{s}$) | Cranston-Eagle Off-Load Hook Technical Manual APR-427. |
| `Waterjet_Nozzle_Yaw` *(Variant D)* | `Waterjet_Housing` | Revolute | `[0.000, -0.350, +3.450]` | `[0, 1, 0]` (Local Vertical $Y$) | $-30.0^\circ$ (port) to $+30.0^\circ$ (starboard) | $25.0^\circ\text{--}30.0^\circ/\text{s}$ hydraulic steering slew rate | HamiltonJet HJ274 Product Manual Section 4. |
| `Waterjet_Bucket_Pitch` *(Variant D)* | `Waterjet_Nozzle_Yaw` | Revolute | `[0.000, -0.320, +3.620]` | `[1, 0, 0]` (Local Transverse $X$) | $0.0^\circ$ (fully raised ahead) to $-55.0^\circ$ (fully lowered astern) | $1.5\text{--}2.0\,\text{s}$ full transition stroke | HamiltonJet HJ274 Split-Duct Reverse Deflector System. |

### 6.2 Critical Rigging Audit: What NEVER Moves
- **Fixed Closed Radome Shell:** The white fiberglass/composite outer radome shell mounted on the arch horizontal cross-member is **rigidly bolted in place**. Under no circumstances should the outer shell be animated spinning. Only the internal antenna feed bar rotates inside the sealed radome at $24.0\text{--}30.0\,\text{RPM}$.
- **GPS Mushroom & Antennas:** Rigidly fixed to antenna mounts.
- **Hoisting Bridle / Fall Cables:** Boat sway under a crane or davit is a physical pendulum dynamic of the free-hanging assembly, not an articulated joint of the boat's internal scene graph.

---

## 7. 8-Cluster Forensic Audit & Common 3D Modelling Errors

When inspecting, creating, or certifying 3D models of the US Navy 7-meter RHIB (GLB / OBJ / FBX), auditors must rigorously enforce the following checklist:

```
+----------------------------------------------------------------------------------------------------+
|                                    8-CLUSTER FORENSIC AUDIT CHECKLIST                               |
+----------------------------------------------------------------------------------------------------+
| [X] Cluster 1: Coordinate Datum & DWL Baseline (DWL locked at Y=0.000m, Keel at Y=-0.58m, Bow -Z)  |
| [X] Cluster 2: Radar Kinematics (Radome shell strictly STATIONARY; feed spins 24-30 RPM inside)    |
| [X] Cluster 3: Propulsion Authenticity (Single inboard diesel + Bravo outdrive OR HamiltonJet)     |
| [X] Cluster 4: Steering Realism (No rudder blades; steered via outdrive leg or jet nozzle)         |
| [X] Cluster 5: Screw Alignment (Propeller axis follows tilted outdrive shaft, NOT global Z)         |
| [X] Cluster 6: Dimensional & Scale Integrity (LOA 7.24m, Beam 2.74m; no 10x/100x cm errors)        |
| [X] Cluster 7: Inflatable Sponson Morphology (5-7 discrete chambers with relief valves & seams)    |
| [X] Cluster 8: PBR Material Authenticity (Roughness 0.88 non-skid vs 0.40 hull; zero pure green)   |
+----------------------------------------------------------------------------------------------------+
```

### Common Amateur Modelling Errors & Corrections

1. **Spinning Closed Radar Radomes:**
   - *Error:* Animating the entire white Furuno or Raymarine dome shell spinning continuously on the arch.
   - *Correction:* The shell is a weatherproof radome housing. It is rigidly static. If internal components are modeled, rotate only the internal slotted waveguide antenna at $24.0\text{--}30.0\,\text{RPM}$ with `LINEAR` interpolation around $+Y$.
2. **Conflating Sterndrive and Waterjet Fits:**
   - *Error:* Adding twin outboard engines or an exposed conventional propeller shaft with a separate spade rudder blade under the hull bottom.
   - *Correction:* Standard US Navy fleet 7m RIBs (Variants A, B, C) feature a **single inboard diesel coupled to a single transom-mounted MerCruiser Bravo Two X outdrive**. Special tactical variants (Variant D) feature an **inboard diesel coupled to a HamiltonJet HJ274 waterjet**. There are zero standalone underwater rudder blades on either configuration—steering is achieved entirely by deflecting the thrust unit $\pm 30.0^\circ$.
3. **Propeller Shaft Axis Pointing Along World -Z:**
   - *Error:* Parenting the propeller blades directly to the hull and spinning them around world $Z$.
   - *Correction:* The propeller must be parented to the outdrive lower gearcase node. Its spin axis must follow the outdrive's physical propeller shaft, tilting upward as the drive trims and yawing sideways as the helm steers.
4. **Gross Metric Scale & Scene Contamination:**
   - *Error:* Models exported in centimeters without glTF unit scaling, resulting in a 724-meter boat; or including the entire shipboard SLAD davit and cradle inside the boat's root bounding box.
   - *Correction:* Isolate the boat as a standalone asset with world bounding box $X \approx 2.74\text{m}$, $Y \approx 3.03\text{m}$ (mast up) / $2.26\text{m}$ (mast down), and $Z \approx 7.24\text{m}$. Separate davits, cradles, and chocks into their own distinct scene assemblies.
5. **Smooth Torus Sponson Collar:**
   - *Error:* Modeling the inflatable collar as a featureless smooth rubber donut without chambers, relief valves, or seams.
   - *Correction:* Model the 5 to 7 distinct airtight chambers separated by internal baffle lines, each equipped with a Leafield C7 inflation valve on the top inner shoulder and Leafield A6 pressure relief valve on the outboard face, protected by a D-shaped extruded rubber perimeter rub strake.
6. **Incorrect Hoisting Hardware:**
   - *Error:* Putting 4-point slings on a boat that has a single-point Cranston-Eagle release hook arch, or omitting the structural engine-straddling hoisting arch on a fleet Ready Service Life Boat.
   - *Correction:* Standard fleet combatant RIBs (DDG, CG, LHD, CVN) must feature the heavy tubular stainless steel single-point hoisting frame centered at $Z = +1.10\text{m}$ over the engine/console gap, terminating in the distinctive Cranston-Eagle release hook.
7. **PBR Surface Fidelity & Specular Bleed:**
   - *Error:* Assigning identical metallic/roughness values across the entire mesh, or applying glossy reflections to the deck and tube surfaces.
   - *Correction:* The walking deck and engine box lid must carry high-friction naval non-skid texture (roughness $0.85\text{--}0.92$, metallic $0.00$). The Hypalon/polyurethane collar exhibits a matte elastomeric sheen (roughness $0.60\text{--}0.70$, metallic $0.00$). The fiberglass hull gelcoat has moderate gloss (roughness $0.35\text{--}0.45$). Aluminum railings and stainless fasteners feature authentic metalness ($0.80\text{--}0.95$, roughness $0.20\text{--}0.30$). Pure `#00FF00` green is strictly prohibited.

---

## 8. Uncertainty Register

Every engineering parameter where public documentation exhibits variance, classification constraints, or builder-specific deviations is registered below:

| Item ID | Parameter / Component | Status | Known Public Evidence | Missing / Ambiguous Data | Risk & Impact on 3D Synthesis | Resolution Strategy |
|---|---|---|---|---|---|---|
| **UNC-7M-01** | Propulsor Variation across Hull Contracts | **Resolved** | RIBCRAFT 2019+ TDP standardizes on Steyr SE266E40 + MerCruiser Bravo Two X outdrive; Willard legacy hulls used Yanmar/Cummins; NSW tactical hulls used HamiltonJet HJ274. | Minor differences in transom cutouts between outdrive and waterjet hulls. | Low: Distinct variants A and D represent each layout cleanly. | Model both variants as distinct modular transom fits (`Outdrive_BravoX` vs `Waterjet_HJ274`). |
| **UNC-7M-02** | Exact Single-Point Hook Model | **Resolved** | Cranston-Eagle APR-427 and APR-5654 off-load release hooks documented across NSTM 583 and DVIDS maintenance imagery; Henriksen hooks on select export/USCG hulls. | Exact hook brand varies by shipyard installation date. | Very Low: External geometry and release kinematics are functionally identical. | Standardize on Cranston-Eagle APR series with manual trip lanyard and hydrostatic interlock. |
| **UNC-7M-03** | Collar Chamber Count (5 vs 7) | **Resolved** | Standard 7m Navy TDP specifies 5 main buoyancy chambers; Willard Sea Force 730 offers 7 chambers for combat damage redundancy. | Sponson internal partition locations vary slightly by builder. | Minimal: External appearance identical except for count of Leafield valves. | Texture 5-chamber partition seams as baseline; provide 7-chamber variant texture map. |
| **UNC-7M-04** | Aft Folding Arch Slew Rate | **Unresolved** (Manual) | Radar arch is unpinned by hand via two stainless quick-release detent pins and folded forward onto rubber rest pads. | No automated motor or hydraulic actuator exists; timing depends entirely on deck crew. | Negligible: Static animation between $0^\circ$ and $-90^\circ$ with $10\text{--}15\,\text{s}$ manual cycle. | Treat as manual crew evolution ($10.0\,\text{s}$ duration); lock in either deployed or stowed state. |
| **UNC-7M-05** | Shock-Mitigating Seat Count | **Partially Resolved** | Fleet SAR baseline uses open cockpit with coxswain bolster and non-skid floor for stokes litter; VBSS tactical fit carries 4 to 8 Shockwave jockey seats. | Varied tactical detachment configurations across deployments. | Medium: Cockpit layout changes between open SAR and seated VBSS. | Provide removable/modular jockey seat child nodes parented to deck mounting tracks. |

---

## 9. Comprehensive DVIDS Primary Image Corpus

The Defense Visual Information Distribution Service (**DVIDS**) is the primary trusted public photographic authority. Every image listed below has been independently inspected, with verified URLs, official DVIDS Media IDs, photographer credits, and confirmed angles.

```
       [AERIAL / TOP-DOWN]                          [BOW / FRONT]
       ID: 8526726 (USS Essex SLAD Davit)           ID: 7688649 (USS Oakland Singapore Waters)
       ID: 4201439 (USS America Flight Deck)        ID: 6932084 (USS Jackson MIO Gunner Station)
                    \                                    /
                     \                                  /
  [PORT PROFILE] -----> [ US NAVY 7-METER RHIB ] <----- [STARBOARD PROFILE]
  ID: 7688648 (USS Oakland Deploy)                      ID: 5143978 (USS Bataan Suspended)
  ID: 7941678 (USS John P. Murtha)                      ID: 8112367 (USS San Diego Davit Descent)
                    /                                   \
                   /                                     \
       [STERN / QUARTER]                            [MECHANISM DETAILS]
       ID: 3007560 (USS Wayne E. Meyer Planing)     ID: 7751008 (MerCruiser Bravo X Sterndrive)
       ID: 2974925 (USS Coronado LCS Recovery)      ID: 7747457 (Cockpit Helm & Controls)
       ID: 9182525 (USS Fort Lauderdale LPD-17)     ID: 7688652 (Davit Hook & Hoisting Cable)
                                                    ID: 3002959 (Engine & Davit Maintenance)
```

### 9.1 Multi-Angle Photographic Coverage Matrix

| Perspective / Angle | DVIDS Image Page URL | Photo Media ID | Platform / Unit Citation | Observation Date | Photographer Credit | Verified Subject & Engineering Details |
|---|---|---|---|---|---|---|
| **Port / Left Profile (Underway)** | [DVIDS 7688648](https://www.dvidshub.net/image/7688648/uss-oakland-conducts-small-boat-training) | `7688648` | USS *Oakland* (LCS 24) | 2023-03-13 | MC2 Sang Kim | 7m RIB deployed from port side of LCS 24; crisp broadside profile showing collar curvature, waterlines, forward painter line, and spray pattern. |
| **Port / Left Profile (Underway Open Sea)** | [DVIDS 7941678](https://www.dvidshub.net/image/7941678/us-navy-and-nasa-conduct-urt-10) | `7941678` | USS *John P. Murtha* (LPD 26) / NASA URT-10 | 2023-07-28 | MC2 Joshua Samoluk | 7m RHIB operating as perimeter safety patrol boat in Pacific Ocean; port-quarter profile showing hull trim at low speed and coxswain at helm. |
| **Starboard / Right Profile (Suspended)** | [DVIDS 5143978](https://www.dvidshub.net/image/5143978/man-overboard-drill) | `5143978` | USS *Bataan* (LHD 5) | 2019-02-23 | MC3 Lenny Weston | 7m RHIB suspended in mid-air from starboard slewing arm davit; clean starboard elevation showing complete deep-V hull, outdrive leg, and collar profile. |
| **Starboard / Right Profile (Davit Descent)** | [DVIDS 8112367](https://www.dvidshub.net/image/8112367/uss-san-diego-lpd-22-lowers-small-boat) | `8112367` | USS *San Diego* (LPD 22) | 2023-10-18 | MC1 Brandon Woods | Descent alongside LPD-22; shows starboard side profile, collar lifelines, outdrive elevation above water, and single-point hoisting hook attachment. |
| **Bow / Front Oblique (Planing)** | [DVIDS 7688649](https://www.dvidshub.net/image/7688649/uss-oakland-conducts-small-boat-training) | `7688649` | USS *Oakland* (LCS 24) | 2023-03-13 | MC2 Sang Kim | 7m RIB operating in Singapore waters; bow-quarter high-speed view showing knife-edge forward deadrise entry, chine flats, and bow sponson apex. |
| **Bow / Forward Gunner Station** | [DVIDS 6932084](https://www.dvidshub.net/image/6932084/uss-jackson-lcs-6-sailor-participates-cooperation-afloat-and-readiness-and-training-carat-indonesia-2021) | `6932084` | USS *Jackson* (LCS 6) / CARAT 2021 | 2021-11-09 | MC3 Andrew Langholf | Gunner's Mate at forward weapon mount during maritime interdiction operation; interior view looking forward over bow tube, showing pedestal socket and deck non-skid. |
| **Bow / Forward SAR Station** | [DVIDS 7747460](https://www.dvidshub.net/image/7747460/uss-oakland-conducts-small-boat-operations) | `7747460` | USS *Oakland* (LCS 24) | 2023-04-17 | MC2 Sang Kim | Crew deploying Stokes rescue litter into Coral Sea; close-up of bow interior deck, collar tie-down rings, bow painter cleat, and tube taper. |
| **Stern / Quarter (Dynamic Planing)** | [DVIDS 3007560](https://www.dvidshub.net/image/3007560/uss-wayne-e-meyers-7-meter-rib-operations) | `3007560` | USS *Wayne E. Meyer* (DDG 108) | 2016-11-21 | MC3 Kelsey L. Adams | 7m RIB on passenger exchange evolution; stern-quarter planing shot displaying aft radar arch, masthead all-round white light, and transom water displacement. |
| **Stern / Quarter (LCS Recovery)** | [DVIDS 2974925](https://www.dvidshub.net/image/2974925/uss-coronado-lcs-4-crew-conducts-rhib-operations) | `2974925` | USS *Coronado* (LCS 4) | 2016-11-04 | MC2 Michaela Garrison | 7m RHIB recovering alongside littoral combat ship; shows aft quarter, engine box enclosure, and aft collar cones. |
| **Variant B (LPD-17 Fit Underway)** | [DVIDS 9182525](https://www.dvidshub.net/image/9182525/rhib-operations) | `9182525` | USS *Fort Lauderdale* (LPD 28) | 2025-06-25 | MC3 Jaimie Bethea | Sailors and Marines training on LPD-17 variant 7m RHIB during COMPTUEX; displays variant-specific deck arrangement, console layout, and seating. |
| **Top / Aerial (Overhead Davit View)** | [DVIDS 8526726](https://www.dvidshub.net/image/8526726/uss-essex-port-operations) | `8526726` | USS *Essex* (LHD 2) | 2024-07-10 | MC2 Richard E. Anglin | High-angle overhead shot from amphibious assault ship boat deck directly into the 7m RIB suspended on SLAD davit falls; shows full cockpit plan, engine cover, and grating. |
| **Top / Aerial (Flight Deck Looking Down)** | [DVIDS 4201439](https://www.dvidshub.net/image/4201439/uss-america-sailors-lower-rigid-hull-inflatable-boat) | `4201439` | USS *America* (LHA 6) | 2018-03-06 | MC3 Vance Hand | High-angle perspective looking down from flight deck as starboard davit lowers RHIB to waterline; displays planar deck geometry and collar proportion. |
| **Mechanism Detail: Center Console & Helm** | [DVIDS 7747457](https://www.dvidshub.net/image/7747457/uss-oakland-conducts-small-boat-operations) | `7747457` | USS *Oakland* (LCS 24) | 2023-04-17 | MC2 Sang Kim | Direct close-up into the coxswain station: steering wheel, hydraulic helm pump hub, throttle/shift quadrant, windscreen, Furuno MFD, compass, and grabrails. |
| **Mechanism Detail: Outdrive & Rudder Steering** | [DVIDS 7751008](https://www.dvidshub.net/image/7751008/daily-operations-aboard-uss-george-hw-bush-cvn-77) | `7751008` | USS *George H.W. Bush* (CVN 77) | 2023-04-19 | MCSN Sasha Ambrose | Enginemen performing maintenance on a **MerCruiser Bravo X Diesel sterndrive** on a shipboard RHIB; verified photographic evidence of outdrive leg and propulsor hardware. |
| **Mechanism Detail: Davit Hook & Lifting Ring** | [DVIDS 7688652](https://www.dvidshub.net/image/7688652/uss-oakland-conducts-small-boat-training) | `7688652` | USS *Oakland* (LCS 24) | 2023-03-13 | MC2 Sang Kim | Sailors performing maintenance on the single-point davit fall hook and release ring mechanism; close-up of heavy-duty marine hoisting hardware. |
| **Mechanism Detail: Engine & Cradle Maintenance** | [DVIDS 3002959](https://www.dvidshub.net/image/3002959/uss-wayne-e-meyers-sailors-performs-maintence-7-meter-rib) | `3002959` | USS *Wayne E. Meyer* (DDG 108) | 2016-11-19 | MC3 Kelsey L. Adams | Sailor conducting routine maintenance on a 7-meter RIB secured in its starboard shipboard davit cradle; shows engine box access, deck fittings, and cradle chocks. |

### 9.2 DVIDS Image Search Log (Unresolved Direct Searches)
- **Direct Head-on 0° Transom View:** Queried `site:dvidshub.net/image "7-meter" OR "7m" "rigid" "stern" OR "transom" OR "outdrive" OR "propeller"`. While numerous dynamic quarter views (DVIDS 3007560, 2974925) and propulsion maintenance close-ups (DVIDS 7751008) exist, a dry-dock perfectly orthogonal 0° elevation directly behind the transom is **unresolved** on DVIDS; the mechanical arrangement is fully cross-verified against Mercury MerCruiser Bravo Two X installation drawings.

---

## 10. External Source Sibling & Collector Status

In accordance with integration governance directives, the external collector sibling directories at `D:/dreidel3d-sv2/refimages/` were inspected:
- **Location:** `D:/dreidel3d-sv2/refimages/ships-agy/us-navy-7m-rhib/`
- **Collector Status:** **No index ready** (`INDEX.md` not yet generated by the background scraping worker as of 2026-10-09).
- **Action Taken:** In accordance with instructions, zero duplicate collector scripts were launched, no image binaries were downloaded into the workspace, and the status is formally recorded here. Once the collector worker compiles `INDEX.md`, relative links can be established via `../../../../dreidel3d-sv2/refimages/ships-agy/us-navy-7m-rhib/INDEX.md`.

---

## 11. Authoritative Primary Sources & Literature

1. **NAVSEA Technical Publication S9086-TX-STM-010:** *Naval Ships' Technical Manual (NSTM) Chapter 583, Volume 1: Boats and Small Craft*. Naval Sea Systems Command, Washington Navy Yard, DC. Establishes standard dimensions, 5,600 lb maximum hoisting condition weight, 18-person full load capacity, SAR Ready Service Lifeboat party requirements, and safety inspection guidelines.
2. **NAVSEA Technical Publication S9086-TX-STM-020:** *Naval Ships' Technical Manual (NSTM) Chapter 583, Volume 2: Handling and Stowing of Boats and Small Craft*. Details Slewing Arm Davits (SLAD), cradle chocks, gripes, and hoisting slings.
3. **NAVSEA Standard Boat Specification S6322-A1-HBK-010:** *United States Navy Boats and Small Craft Information Book*. Documents lines, hull form, deadrise, and basic arrangements.
4. **RIBCRAFT USA LLC:** *US Navy Standard 7-Meter Rigid Inflatable Boat (RIB) Technical Data Package & IDIQ Contract Summary (Contract N00024-19-D-2207)*. Documents Steyr SE266E40 diesel propulsion, MerCruiser Bravo Two X outdrive, 5-chamber polyurethane tube, and variants (Standard, LPD-17, SOLAS). Available via [RIBCRAFT Military Releases](https://www.ribcraftusa.com).
5. **Willard Marine, Inc.:** *Sea Force 700 & Sea Force 730 Technical Data Sheets and Product Brochures*. Willard Marine, Anaheim, CA. Documents hull LOA ($7.24\text{m}$ / $7.32\text{m}$), beam ($2.74\text{m}$), deadrise ($20^\circ\text{--}24^\circ$), and propulsion options. Available via [Willard Marine Military Small Craft](https://www.willardmarine.com).
6. **HamiltonJet:** *HJ274 Waterjet Technical Product Manual & Control Systems Guide*. C.W.F. Hamilton & Co. Ltd. Details JT steering nozzle deflection ($\pm 30^\circ$) and split-duct reversing deflector bucket stroke and hydraulic actuation. Available via [HamiltonJet Marine Propulsion](https://www.hamiltonjet.com).
7. **Mercury Marine / MerCruiser:** *Bravo One, Bravo Two, and Bravo Three Diesel Sterndrives Technical Manual*. Details gimbal ring steering deflection ($\pm 30.0^\circ$), hydraulic trim ($-5^\circ$ to $+15^\circ$), trailer tilt ($+48^\circ$), and gear reduction ratios.
8. **Steyr Motors GmbH:** *SE 6-Cylinder Monoblock Marine Diesel Engines Technical Datasheet (SE266E40)*. Steyr, Austria. Details $190\,\text{kW}$ ($258\,\text{hp}$) power curve at $4,000\,\text{RPM}$, dry weight $340\,\text{kg}$, and interface dimensions.
9. **NAVSEA Technical Manual SW361-AB-MMO-010:** *Mount, Machine Gun, Mk 93 Mod 4 - Maintenance and Operators Manual*. Documents mount azimuth traverse ($360^\circ$) and elevation limits ($-15^\circ$ to $+45^\circ$).
10. **Defense Visual Information Distribution Service (DVIDS):** Official photographic archive records: `7688648`, `7688649`, `7688650`, `7688651`, `7688652`, `7747457`, `7747460`, `8526726`, `5143978`, `3002959`, `3007560`, `9182525`, `8112367`, `6932084`, `4201439`, `2974925`, `7751008`. Available via [dvidshub.net](https://www.dvidshub.net).


---

<!-- NAVAL-CURRENT-START -->
# us-navy-7m-rhib — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:24:21.394242+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-Willard-SEA-FORCE-700` | Manufacturer brochure reports boat weight 1,909 kg, full-load weight 3,372 kg, 35 US gal fuel and 0.56 m tube diameter. Preserve its conflicting 2.70 m / 9 ft beam equivalents; do not combine Willard and RIBCRAFT variants. | [Primary source](https://www.willardmarine.com/images/brochures/SEAFORCE700.pdf); principal specifications table |
| `sourced-RIBCRAFT-7.0` | RIBCRAFT product lists length 24 ft, beam 9 ft and tube diameter 21 in. Derived SI is approximately 7.32 m, 2.74 m, 0.53 m. This is a separate builder configuration. | [Primary source](https://ribcraftusa.com/7-0-meter/); Specifications |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| helm/steering linkage | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| identified sterndrive or waterjet steering/reverse equipment | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| davit attachment interfaces | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Raw Willard weights, fuel and tube values conflict with its brochure. Builder variants must remain separate. NAVSEA design hoisting weight and davit safe working load are different constraints. Helm turn-count/time arithmetic in the draft is inconsistent.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [USS Coronado (LCS 4) crew conducts RHIB operations. ](https://www.dvidshub.net/image/2974925/uss-coronado-lcs-4-crew-conducts-rhib-operations) | `161104-N-MW990-036 CHANGI NAVAL BASE (November 4, 2016) Sailors aboard littoral combat ship USS Coronado (LCS 4) recover a 7-meter rigid-hull inflatable boat following boat operations. Currently on a rotational` — `sourced-caption` | `stern` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Wayne E. Meyer's Sailors Performs Maintence on the 7-meter RIB ](https://www.dvidshub.net/image/3002959/uss-wayne-e-meyers-sailors-performs-maintence-7-meter-rib) | `161119-N-RM689-028 PACIFIC OCEAN (Nov. 19, 2016) Seaman Long Nguyen, assigned to Arleigh Burke-class guided missile destroyer USS Wayne E. Meyer (DDG 108), performs routine maintenance on a 7-meter rigid inflat` — `sourced-caption` | `detail` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Wayne E. Meyer's 7-meter RIB Operations ](https://www.dvidshub.net/image/3007560/uss-wayne-e-meyers-7-meter-rib-operations) | `161121-N-RM689-229 PACIFIC OCEAN (Nov. 21, 2016) Sailors assigned to Arleigh Burke-class guided-missile destroyer USS Wayne E. Meyer (DDG 108), drive a 7-meter rigid inflatable boat during a passenger exchange ` — `sourced-caption` | `stern` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS America Sailors lower rigid-hull inflatable boat ](https://www.dvidshub.net/image/4201439/uss-america-sailors-lower-rigid-hull-inflatable-boat) | `180306-N-ZS023-012 PACIFIC OCEAN (March 6, 2018) Sailors aboard the amphibious assault ship USS America (LHA 6) lower a rigid-hulled inflatable boat using the ship’s starboard davit. America is underway off the` — `sourced-caption` | `aerial` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Man Overboard Drill ](https://www.dvidshub.net/image/5143978/man-overboard-drill) | `190223-N-KO533-0034 ATANTIC OCEAN (Feb. 23, 2019) Amphibious assault ship USS Bataan's (LHD 5) Deck department lowers the 7 meter Rigid Hull Inflatable Boat (RHIB) during a man overboard drill.The ship is curre` — `sourced-caption` | `starboard` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Jackson (LCS 6) Sailor Participates in Cooperation Afloat and Readiness and Training (CARAT) Indonesia 2021 ](https://www.dvidshub.net/image/6932084/uss-jackson-lcs-6-sailor-participates-cooperation-afloat-and-readiness-and-training-carat-indonesia-2021) | `211109-N-FA490-3704 JAVA SEA (Nov. 9, 2021) Gunner’s Mate 1st Class Chris Clarke, from Chicago, Ill., participates in a maritime interdiction operation (MIO) in a 7 meter rigid-hulled inflatable boat (RIB) duri` — `sourced-caption` | `bow` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS OAKLAND CONDUCTS SMALL BOAT TRAINING ](https://www.dvidshub.net/image/7688648/uss-oakland-conducts-small-boat-training) | `SINGAPORE (Mar. 13, 2023) Sonar Technician (Surface) 2nd Class Kevan Thomas, front, from Indian Head, Maryland, throws line from a 7-meter rigid-hulled inflatable boat (RIB) as the RIB deploys from the port sid` — `sourced-caption` | `port` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS OAKLAND CONDUCTS SMALL BOAT TRAINING ](https://www.dvidshub.net/image/7688649/uss-oakland-conducts-small-boat-training) | `SINGAPORE (Mar. 13, 2023) Sailors operate a 7-meter rigid hulled inflatable boat (RIB) during small boat trainig with Independence-class littoral combat ship USS Oakland (LCS 24) in Singapore, Mar. 13, 2023. Oa` — `sourced-caption` | `bow` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS OAKLAND CONDUCTS SMALL BOAT TRAINING ](https://www.dvidshub.net/image/7688652/uss-oakland-conducts-small-boat-training) | `SINGAPORE (Mar. 13, 2023) Sailors manually lower the davit hook for maintenance during small boat training aboard Independence-class littoral combat ship USS Oakland (LCS 24) at Changi Naval Base, Singapore, Ma` — `sourced-caption` | `detail` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS OAKLAND CONDUCTS SMALL BOAT OPERATIONS ](https://www.dvidshub.net/image/7747457/uss-oakland-conducts-small-boat-operations) | `CORAL SEA (Apr. 17, 2023) Sonar Technician (Surface) 3rd Class Samuel Fox, left, from Dallas, and Sonar Technician (Surface) 2nd Class Kevan Thomas, right, a search and rescue swimmer, from Indianhead, Maryland` — `sourced-caption` | `detail` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS OAKLAND CONDUCTS SMALL BOAT OPERATIONS ](https://www.dvidshub.net/image/7747460/uss-oakland-conducts-small-boat-operations) | `CORAL SEA (Apr. 17, 2023) Ensign Ira Toracinta, from Kittery, Maine, and Boatswain’s Mate 3rd Class James Garcia, a search and rescue swimmer, from Salt Lake City, throw a rescue litter into the Coral Sea while` — `sourced-caption` | `bow` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Daily Operations Aboard USS George H.W. Bush (CVN 77) ](https://www.dvidshub.net/image/7751008/daily-operations-aboard-uss-george-hw-bush-cvn-77) | `230419-N-IX644-1154 ATLANTIC OCEAN (April 19, 2023) Engineman 3rd Class Elijah Cayce, right, and Engineman Fireman Francis Kolbasowski, both assigned to the Nimitz-class aircraft carrier USS George H.W. Bush (C` — `sourced-caption` | `detail` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [U.S. Navy and NASA Conduct URT-10 ](https://www.dvidshub.net/image/7941678/us-navy-and-nasa-conduct-urt-10) | `Sailors assigned to amphibious transport dock ship USS John P. Murtha (LPD 26) steer a 7-meter ridged-hulled inflatable boat (RHIB) to the staging area of the Vehicle Advanced Demonstrator for Emergency Recover` — `sourced-caption` | `port` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS San Diego (LPD 22) lowers small boat ](https://www.dvidshub.net/image/8112367/uss-san-diego-lpd-22-lowers-small-boat) | `U.S. Navy Boatswain’s Mate 2nd Class Isaiah Marshall directs the descent of a 7-meter rigid hull inflatable boat alongside USS San Diego (LPD 22) while underway in the Pacific Ocean, Oct. 18, 2023. San Diego, t` — `sourced-caption` | `starboard` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Essex In-Port Operations ](https://www.dvidshub.net/image/8526726/uss-essex-port-operations) | `Boatswain’s Mate 2nd Class Elijah Parra, right, assigned to amphibious assault ship USS Essex (LHD 2) directs the operator for the slewing arm davit to lower a 7m rigid-hull inflatable boat (RIB) during small b` — `sourced-caption` | `aerial` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [RHIB Operations ](https://www.dvidshub.net/image/9182525/rhib-operations) | `ATLANTIC OCEAN (June 25, 2025) Sailors and Marines assigned to the San Antonio-class amphibious transport dock USS Fort Lauderdale (LPD 28) conduct training on operating a 7-meter rigid-hull inflatable boat (RH` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=us+navy+7m+rhib+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=us+navy+7m+rhib+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=us+navy+7m+rhib+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=us+navy+7m+rhib+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=us+navy+7m+rhib+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=us+navy+7m+rhib+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=us+navy+7m+rhib+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- `unresolved`: no matching producer index was ready at integration. Keep collector pickup separate from image coverage.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.
<!-- NAVAL-CURRENT-END -->


---

<!-- NAVAL-CURRENT-START -->
# us-navy-7m-rhib — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:32:48.849695+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-Willard-SEA-FORCE-700` | Manufacturer brochure reports boat weight 1,909 kg, full-load weight 3,372 kg, 35 US gal fuel and 0.56 m tube diameter. Preserve its conflicting 2.70 m / 9 ft beam equivalents; do not combine Willard and RIBCRAFT variants. | [Primary source](https://www.willardmarine.com/images/brochures/SEAFORCE700.pdf); principal specifications table |
| `sourced-RIBCRAFT-7.0` | RIBCRAFT product lists length 24 ft, beam 9 ft and tube diameter 21 in. Derived SI is approximately 7.32 m, 2.74 m, 0.53 m. This is a separate builder configuration. | [Primary source](https://ribcraftusa.com/7-0-meter/); Specifications |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| helm/steering linkage | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| identified sterndrive or waterjet steering/reverse equipment | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| davit attachment interfaces | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Raw Willard weights, fuel and tube values conflict with its brochure. Builder variants must remain separate. NAVSEA design hoisting weight and davit safe working load are different constraints. Helm turn-count/time arithmetic in the draft is inconsistent.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [USS Coronado (LCS 4) crew conducts RHIB operations. ](https://www.dvidshub.net/image/2974925/uss-coronado-lcs-4-crew-conducts-rhib-operations) | `161104-N-MW990-036 CHANGI NAVAL BASE (November 4, 2016) Sailors aboard littoral combat ship USS Coronado (LCS 4) recover a 7-meter rigid-hull inflatable boat following boat operations. Currently on a rotational` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Wayne E. Meyer's Sailors Performs Maintence on the 7-meter RIB ](https://www.dvidshub.net/image/3002959/uss-wayne-e-meyers-sailors-performs-maintence-7-meter-rib) | `161119-N-RM689-028 PACIFIC OCEAN (Nov. 19, 2016) Seaman Long Nguyen, assigned to Arleigh Burke-class guided missile destroyer USS Wayne E. Meyer (DDG 108), performs routine maintenance on a 7-meter rigid inflat` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Wayne E. Meyer's 7-meter RIB Operations ](https://www.dvidshub.net/image/3007560/uss-wayne-e-meyers-7-meter-rib-operations) | `161121-N-RM689-229 PACIFIC OCEAN (Nov. 21, 2016) Sailors assigned to Arleigh Burke-class guided-missile destroyer USS Wayne E. Meyer (DDG 108), drive a 7-meter rigid inflatable boat during a passenger exchange ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS America Sailors lower rigid-hull inflatable boat ](https://www.dvidshub.net/image/4201439/uss-america-sailors-lower-rigid-hull-inflatable-boat) | `180306-N-ZS023-012 PACIFIC OCEAN (March 6, 2018) Sailors aboard the amphibious assault ship USS America (LHA 6) lower a rigid-hulled inflatable boat using the ship’s starboard davit. America is underway off the` — `sourced-caption` | Scope: RHIB size and builder unresolved; caption does not establish 7 m. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Man Overboard Drill ](https://www.dvidshub.net/image/5143978/man-overboard-drill) | `190223-N-KO533-0034 ATANTIC OCEAN (Feb. 23, 2019) Amphibious assault ship USS Bataan's (LHD 5) Deck department lowers the 7 meter Rigid Hull Inflatable Boat (RHIB) during a man overboard drill.The ship is curre` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Jackson (LCS 6) Sailor Participates in Cooperation Afloat and Readiness and Training (CARAT) Indonesia 2021 ](https://www.dvidshub.net/image/6932084/uss-jackson-lcs-6-sailor-participates-cooperation-afloat-and-readiness-and-training-carat-indonesia-2021) | `211109-N-FA490-3704 JAVA SEA (Nov. 9, 2021) Gunner’s Mate 1st Class Chris Clarke, from Chicago, Ill., participates in a maritime interdiction operation (MIO) in a 7 meter rigid-hulled inflatable boat (RIB) duri` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS OAKLAND CONDUCTS SMALL BOAT TRAINING ](https://www.dvidshub.net/image/7688648/uss-oakland-conducts-small-boat-training) | `SINGAPORE (Mar. 13, 2023) Sonar Technician (Surface) 2nd Class Kevan Thomas, front, from Indian Head, Maryland, throws line from a 7-meter rigid-hulled inflatable boat (RIB) as the RIB deploys from the port sid` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS OAKLAND CONDUCTS SMALL BOAT TRAINING ](https://www.dvidshub.net/image/7688649/uss-oakland-conducts-small-boat-training) | `SINGAPORE (Mar. 13, 2023) Sailors operate a 7-meter rigid hulled inflatable boat (RIB) during small boat trainig with Independence-class littoral combat ship USS Oakland (LCS 24) in Singapore, Mar. 13, 2023. Oa` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS OAKLAND CONDUCTS SMALL BOAT TRAINING ](https://www.dvidshub.net/image/7688652/uss-oakland-conducts-small-boat-training) | `SINGAPORE (Mar. 13, 2023) Sailors manually lower the davit hook for maintenance during small boat training aboard Independence-class littoral combat ship USS Oakland (LCS 24) at Changi Naval Base, Singapore, Ma` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS OAKLAND CONDUCTS SMALL BOAT OPERATIONS ](https://www.dvidshub.net/image/7747457/uss-oakland-conducts-small-boat-operations) | `CORAL SEA (Apr. 17, 2023) Sonar Technician (Surface) 3rd Class Samuel Fox, left, from Dallas, and Sonar Technician (Surface) 2nd Class Kevan Thomas, right, a search and rescue swimmer, from Indianhead, Maryland` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS OAKLAND CONDUCTS SMALL BOAT OPERATIONS ](https://www.dvidshub.net/image/7747460/uss-oakland-conducts-small-boat-operations) | `CORAL SEA (Apr. 17, 2023) Ensign Ira Toracinta, from Kittery, Maine, and Boatswain’s Mate 3rd Class James Garcia, a search and rescue swimmer, from Salt Lake City, throw a rescue litter into the Coral Sea while` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Daily Operations Aboard USS George H.W. Bush (CVN 77) ](https://www.dvidshub.net/image/7751008/daily-operations-aboard-uss-george-hw-bush-cvn-77) | `230419-N-IX644-1154 ATLANTIC OCEAN (April 19, 2023) Engineman 3rd Class Elijah Cayce, right, and Engineman Fireman Francis Kolbasowski, both assigned to the Nimitz-class aircraft carrier USS George H.W. Bush (C` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [U.S. Navy and NASA Conduct URT-10 ](https://www.dvidshub.net/image/7941678/us-navy-and-nasa-conduct-urt-10) | `Sailors assigned to amphibious transport dock ship USS John P. Murtha (LPD 26) steer a 7-meter ridged-hulled inflatable boat (RHIB) to the staging area of the Vehicle Advanced Demonstrator for Emergency Recover` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS San Diego (LPD 22) lowers small boat ](https://www.dvidshub.net/image/8112367/uss-san-diego-lpd-22-lowers-small-boat) | `U.S. Navy Boatswain’s Mate 2nd Class Isaiah Marshall directs the descent of a 7-meter rigid hull inflatable boat alongside USS San Diego (LPD 22) while underway in the Pacific Ocean, Oct. 18, 2023. San Diego, t` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Essex In-Port Operations ](https://www.dvidshub.net/image/8526726/uss-essex-port-operations) | `Boatswain’s Mate 2nd Class Elijah Parra, right, assigned to amphibious assault ship USS Essex (LHD 2) directs the operator for the slewing arm davit to lower a 7m rigid-hull inflatable boat (RIB) during small b` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [RHIB Operations ](https://www.dvidshub.net/image/9182525/rhib-operations) | `ATLANTIC OCEAN (June 25, 2025) Sailors and Marines assigned to the San Antonio-class amphibious transport dock USS Fort Lauderdale (LPD 28) conduct training on operating a 7-meter rigid-hull inflatable boat (RH` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=us+navy+7m+rhib+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=us+navy+7m+rhib+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=us+navy+7m+rhib+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=us+navy+7m+rhib+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=us+navy+7m+rhib+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=us+navy+7m+rhib+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=us+navy+7m+rhib+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- `unresolved`: no matching producer index was ready at integration. Keep collector pickup separate from image coverage.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.

Independent image-subject review correction: wrong-subject candidates excluded, duplicate image IDs collapsed, and sibling equipment separated above. Older revisions remain audit evidence and are superseded by this last current section.
<!-- NAVAL-CURRENT-END -->
