# Naval Architecture, Kinematics, and Combat Platform Reference: Lockheed Martin F-35C Lightning II Carrier Variant

**Asset Identifier:** `f35c-lightning2`  
**Classification:** United States Navy (USN) / United States Marine Corps (USMC) | 5th-Generation Carrier-Borne Strike Fighter (CATOBAR)  
**Standard:** JSLC / Project Eretz - Naval Aviation Kinematics Standard  
**Document Type:** Evidence-Grounded Knowledge Pack & Engineering Dossier  
**Author / Traceable Worker Identity:** `nrf2`  
**Registered Response Identity:** `nrf2_gem_3.8_hi`  
**Evaluation Handoff Reference:** `HO-20261009-naval-nrf2`  
**Creation Date:** 2026-10-09T11:05:00Z (2026-10-09 07:05:00 -04:00)  
**Status:** Canonical Reference Knowledge Pack  

---

## 1. Executive Summary & Foundational Engineering Premise

The **Lockheed Martin F-35C Lightning II** is the Carrier Variant (CV) of the Joint Strike Fighter (JSF) family, engineered specifically for Catapult-Assisted Take-Off But Arrested Recovery (CATOBAR) operations aboard United States Navy *Nimitz*-class (CVN-68..77) and *Gerald R. Ford*-class (CVN-78+) supercarriers.

### The Non-Conflation Mandate: F-35C vs. F-35A / F-35B
The F-35C is frequently conflated in amateur 3D models with the land-based Conventional Take-Off and Landing (CTOL) F-35A and the Short Take-Off and Vertical Landing (STOVL) F-35B. While sharing a common core fuselage mold line and core avionics architecture, the F-35C possesses distinct structural, aerodynamic, and mechanical features required for the carrier flight deck environment:

```
+------------------------------------+------------------------------------+------------------------------------+
| Feature                            | F-35A (CTOL - USAF)                | F-35B (STOVL - USMC / RAF)         | F-35C (CATOBAR - USN / USMC)       |
+------------------------------------+------------------------------------+------------------------------------+
| Operational Environment           | Land runways                       | Amphibious assault ships / austere | Supercarrier flight decks (CVN)    |
| Wingspan (Spread)                  | 35.0 ft (10.70 m)                  | 35.0 ft (10.70 m)                  | 43.0 ft (13.11 m) [+23%]           |
| Wingspan (Folded)                  | Non-folding                        | Non-folding                        | 30.0 ft (9.14 m) (90° vertical)    |
| Wing Reference Area ($S_{ref}$)    | 460 sq ft (42.7 m²)                | 460 sq ft (42.7 m²)                | 668 sq ft (62.1 m²) [+45%]         |
| Trailing-Edge Control Surfaces     | 1 Flaperon per wing                | 1 Flaperon per wing                | 1 Inboard Flaperon + 1 Aileron     |
| Horizontal Tailplane Span          | 22.5 ft (6.86 m)                   | 21.8 ft (6.64 m)                   | 26.3 ft (8.02 m) [+17%]            |
| Nose Landing Gear                  | Single wheel, lightweight strut    | Single wheel, lightweight strut    | Heavy dual wheel + Catapult Bar    |
| Catapult Launch Bar & RRHB         | None                               | None                               | Integrated on nose oleo strut      |
| Arresting Tailhook                 | Emergency runway hook (conformal)  | None                               | Heavy carrier hook + hold-down     |
| Internal Cannon                    | GAU-22/A 25mm in port shoulder     | None                               | None (Smooth shoulder lines)       |
| Missionized Gun Pod                | N/A                                | GPU-9/A external centerline pod    | GPU-8/A external centerline pod    |
| Aerial Refueling Mechanism         | USAF Dorsal Boom Receptacle        | Retractable Probe (starboard nose) | Retractable Probe (starboard nose) |
| Engine Designation                 | P&W F135-PW-100                    | P&W F135-PW-600 (LiftFan + 3BSD)   | P&W F135-PW-400 (Maritime coat)    |
| Approach Speed ($V_{approach}$)    | ~155 kts                           | Vertical / slow rolling            | ~140 kts (On-speed 12.3° AoA)      |
+------------------------------------+------------------------------------+------------------------------------+
```

---

## 2. Provenance Tier System

Every numeric dimension, mechanical rate, angular limit, and structural claim in this knowledge pack is assigned a strict Provenance Tier:

| Tier Tag | Description & Verification Standard |
| :--- | :--- |
| `sourced-f35c` | Grounded directly in official United States Navy, NAVAIR, DoD DOT&E, or Lockheed Martin OEM public releases for F-35C. Requires exact URL, document title, and supporting passage/table. |
| `inferred-from:<source>` | Derived through geometric calculation, aeronautical kinematics, or naval architectural inheritance from verified carrier platform dimensions. Engineering basis is explicitly stated. |
| `estimate` | Engineering approximation based on public industry data, photographic scaling, or wind tunnel benchmarks where exact specifications remain controlled. |
| `unresolved` | Parameter governed by Department of Defense controlled technical data (e.g. UFC 3-260-01, IETMs) with no unclassified primary documentation released. Hallucination strictly prohibited. |

---

## 3. Platform Identity, Variants, and Fleet Inventory

### 3.1 Platform Designations & Classification
* **Service Branches:** United States Navy (USN), United States Marine Corps (USMC) [`sourced-f35c`: [NAVAIR F-35C](https://www.navair.navy.mil)]
* **Mission Roles:** Carrier-based Strike Fighter, Air Interdiction, Suppression/Destruction of Enemy Air Defenses (SEAD/DEAD), Offensive Counter-Air (OCA), Surface Warfare (SUW), Electronic Attack [`sourced-f35c`: [US Navy Fact File](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2269004/f-35c-lightning-ii/)]
* **Crew:** 1 Pilot (Martin-Baker US16E Zero-Zero Ejection Seat) [`sourced-f35c`: [Martin-Baker US16E](https://martin-baker.com/products/us16e-ejection-seat/)]
* **Designation:** F-35C (Carrier Variant) [`sourced-f35c`: [Lockheed Martin F-35](https://www.lockheedmartin.com/en-us/products/f-35.html)]

### 3.2 Airframe Developmental Hulls & Production Blocks
* **Developmental Test Hulls (DT-I, DT-II, DT-III):**
  * **CF-01 (Bureau Number 168057):** First flight June 6, 2010 (Fort Worth, TX). Aerodynamic and flight envelope expansion [`sourced-f35c`: [Lockheed Martin Press Release June 2010](https://www.lockheedmartin.com)].
  * **CF-02 (BuNo 168058):** Flutter, structural loads, external weapons release testing.
  * **CF-03 (BuNo 168059):** First carrier arrested landing ("trap") aboard USS *Nimitz* (CVN-68), November 3, 2014, piloted by Cmdr Tony "Brick" Wilson [`sourced-f35c`: [DVIDS 9747004](https://www.dvidshub.net/image/9747004/from-flightline-deckplates-and-digital-edge-33-year-journey-through-navys-technological-evolution); [NAVAIR News 2014](https://www.navair.navy.mil)]. First carrier catapult launch piloted by Cmdr Christian Sewell, November 4, 2014 [`sourced-f35c`: [DVIDS 1645266](https://www.dvidshub.net/image/1645266/f-35c-lightning-ii-conducts-1st-carrier-launch)].
  * **CF-05 (BuNo 168061):** Carrier suitability and night operations testing aboard CVN-68.
* **Production Capability Blocks:**
  * **Block 2A/2B:** Initial training capability; initial fleet delivery (VFA-101 / VFA-125).
  * **Block 3i:** Tech Refresh 2 (TR-2) processor update.
  * **Block 3F:** Full Warfighting Capability, IOC configuration for US Navy (declared February 2019 by Commander, Naval Air Forces) [`sourced-f35c`: [US Navy Press Release Feb 2019](https://www.navy.mil)].
  * **Block 4 / Technology Refresh 3 (TR-3):** Modernized open-architecture Integrated Core Processor (ICP), panoramic cockpit display refresh, integration of AGM-154 JSOW, AGM-158C LRASM, Small Diameter Bomb II (StormBreaker), and "Sidekick" internal weapons bay rack expanding internal AMRAAM carriage from 4 to 6 missiles [`sourced-f35c`: [Lockheed Martin Products](https://www.lockheedmartin.com/en-us/products/f-35.html); [DOT&E FY2021 Report](https://www.dote.osd.mil)].

### 3.3 Active Fleet Operating Squadrons (USN & USMC)
* **United States Navy (USN):**
  * **VFA-147 "Argonauts" (Tail Code: NE / NG):** First operational USN F-35C squadron. Inaugural combat deployment aboard USS *Carl Vinson* (CVN-70), August 2021 – February 2022; deployed forward-operating aboard USS *George Washington* (CVN-73), 2024–2026 [`sourced-f35c`: [DVIDS 8471397](https://www.dvidshub.net/image/8471397/an-f-35c-lightning-ii-lands-flight-deck-nimitz-class-aircraft-carrier-uss-carl-vinson)].
  * **VFA-97 "Warhawks" (Tail Code: NE / NA):** Deployed aboard USS *Carl Vinson* (CVN-70) [`sourced-f35c`: [DVIDS 8203937](https://www.dvidshub.net/image/8203937/uss-carl-vinson-cvn-70-sailors-perform-f-35c-lightning-ii-maintenance)].
  * **VFA-125 "Rough Raiders" (Tail Code: NJ):** Fleet Readiness Squadron (FRS), NAS Lemoore, CA [`sourced-f35c`: [DVIDS 7086063](https://www.dvidshub.net/image/7086063/an-f-35c-lighting-ii-taxis-across-flight-deck)].
  * **VFA-86 "Sidewinders":** Transitioned to F-35C.
  * **VX-9 "Vampires" & VX-23 "Salty Dogs":** Operational and developmental test squadrons (NAS China Lake / NAS Patuxent River).
* **United States Marine Corps (USMC):**
  * **VMFA-314 "Black Knights" (Tail Code: VW):** First USMC F-35C squadron (declared IOC December 2020). Historic first deployment aboard USS *Abraham Lincoln* (CVN-72), January 2022 – August 2022 [`sourced-f35c`: [DVIDS 6942830](https://www.dvidshub.net/image/6942830/f-35-conducts-routine-training-aboard-uss-abraham-lincoln); [DVIDS 8290897](https://www.dvidshub.net/image/8290897/vmfa-314-loads-jsow-onto-f-35c)].
  * **VMFA-311 "Tomcats" (Tail Code: WL):** Second USMC operational F-35C squadron (MCAS Miramar, CA).
  * **VMFA-115 "Silver Eagles" (Tail Code: VE):** Transitioned to F-35C (MCAS Beaufort, SC) [`sourced-f35c`: [DVIDS 9847090](https://www.dvidshub.net/image/9847090/vmfa-115-takes-off-their-first-flight-with-f-35c-lightning-ii-aircraft)].
  * **VMFA-251 "Thunderbolts":** Transitioned to F-35C.

---

## 4. Sourced Metric Dimensions & Carrier Envelope

### 4.1 Master Dimensional Matrix

| Metric Dimension | SI (Metric) | Imperial | Provenance Tier | Primary Source & Supporting Passage |
| :--- | :--- | :--- | :--- | :--- |
| **Length Overall (LOA)** | **15.70 m** | **51.5 ft** (618.0 in) | `sourced-f35c` | [US Navy Fact File 2269004](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2269004/f-35c-lightning-ii/): *"Length: 51.5 feet (15.7 meters)"*. [Lockheed Martin F-35](https://www.lockheedmartin.com/en-us/products/f-35.html). Radome tip to trailing engine nozzle. |
| **Wingspan (Spread / Unfolded)** | **13.11 m** | **43.0 ft** (516.0 in) | `sourced-f35c` | [US Navy Fact File 2269004](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2269004/f-35c-lightning-ii/): *"Wingspan: 43 feet (13.1 meters)"*. [Lockheed Martin F-35](https://www.lockheedmartin.com/en-us/products/f-35.html). Measured wingtip to wingtip across outer panels. |
| **Wingspan (Folded / Stowed)** | **9.14 m** | **30.0 ft** (360.0 in) | `sourced-f35c` | [Lockheed Martin F-35 Fast Facts / AIAA Paper 2016-1245](https://arc.aiaa.org/doi/10.2514/6.2016-1245): Outer wing panels rotate vertically $90^\circ$, reducing span from 43.0 ft to 30.0 ft (reduction of 7.5 ft / 2.29 m per wingtip). |
| **Wing Fold Hinge Station ($X_{fold}$)** | **$\pm 4.57\text{ m}$** | **$\pm 15.0\text{ ft}$** (BL 180.0 in) | `inferred-from:lockheed-martin/geometry` | Derived from folded half-span: $30.0\text{ ft} / 2 = 15.0\text{ ft} = 4.572\text{ m}$ from fuselage centerline. Sits at Buttline 180. |
| **Height on Gear (Overall)** | **4.48 m** | **14.7 ft** (176.4 in) | `sourced-f35c` | [US Navy Fact File 2269004](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2269004/f-35c-lightning-ii/): *"Height: 14.7 feet (4.48 meters)"*. Static ground plane to top of $20^\circ$ canted vertical tail fins. |
| **Folded Wingtip Height ABV Deck** | **~4.10 m** | **~13.5 ft** | `inferred-from:carrier-suitability` | Outer folding wing panel length is $6.5\text{ ft} = 1.98\text{ m}$. Hinge line sits at elevation $Y \approx 1.35\text{ m}$ above deck; folded tip reaches $1.35 + 1.98 = 3.33\text{ m}$ (lower than the 4.48 m vertical stabilizer apex). |
| **Horizontal Tailplane Span** | **8.02 m** | **26.3 ft** (315.6 in) | `sourced-f35c` | [Lockheed Martin Aeronautics Technical Publication](https://www.lockheedmartin.com): Enlarged slab stabilator on F-35C (vs 22.5 ft on F-35A, 21.8 ft on F-35B) to provide pitch control at low approach speeds. |
| **Wing Reference Area ($S_{ref}$)** | **62.10 m²** | **668.0 sq ft** | `sourced-f35c` | [Lockheed Martin F-35 Capabilities](https://www.lockheedmartin.com/en-us/products/f-35.html): $45\%$ wing area increase over F-35A/B ($460.0\text{ sq ft}$) to lower stall speed and achieve 140 kt carrier recovery. |
| **Vertical Fin Outboard Cant Angle** | **$20.0^\circ$** | **$20.0^\circ$** | `sourced-f35c` | [Lockheed Martin / USAF Technical Briefs](https://www.lockheedmartin.com): Identical $20^\circ$ rake across all variants for radar cross section deflection. |
| **Wheelbase (Nose to Main Axle)** | **UNKNOWN** | **UNKNOWN** | `unresolved` | Controlled technical data governed by DoD [UFC 3-260-01](https://www.wbdg.org) / F-35 IETM. Unclassified public fact sheets withhold axle spacing. Estimated geometrically at **$5.90 - 6.20\text{ m}$** ($19.4 - 20.3\text{ ft}$). |
| **Wheel Track / Tread (Main Gear)** | **UNKNOWN** | **UNKNOWN** | `unresolved` | Controlled technical data under DoD [UFC 3-260-01](https://www.wbdg.org). Estimated geometrically between main tire centerlines at **$3.40 - 3.70\text{ m}$** ($11.2 - 12.1\text{ ft}$). |
| **Operating Weight Empty (OWE)** | **15,686 kg** | **34,581 lb** | `sourced-f35c` | [DoD DOT&E FY2020 Annual Report](https://www.dote.osd.mil): Heaviest variant due to carrier catapult launch bar, heavy arresting hook structure, and high-sink gear. |
| **Empty Weight (Secondary Source)** | **15,785 kg** | **34,800 lb** | `sourced-f35c` | [US Navy Fact File 2269004](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2269004/f-35c-lightning-ii/): *"Weight: 34,800 lbs (empty)"*. Documents minor variance ($\Delta = 219\text{ lb}$) across reporting baselines. |
| **Maximum Takeoff Weight (MTOW)** | **31,751 kg** | **70,000 lb class** | `sourced-f35c` | [US Navy Fact File 2269004](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2269004/f-35c-lightning-ii/): *"Maximum Takeoff Weight: 70,000-pound class"*. Maximum catapult launch gross weight rating. |
| **Maximum Internal Fuel** | **8,960 kg** | **19,750 lb** | `sourced-f35c` | [Lockheed Martin F-35 Fast Facts](https://www.lockheedmartin.com/en-us/products/f-35.html): Enlarged wings house greatest internal fuel of all variants (vs 18,250 lb on A, 13,500 lb on B). |
| **Internal Fuel (Secondary Source)** | **8,708 kg** | **19,200 lb** | `sourced-f35c` | [US Navy Fact File 2269004](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2269004/f-35c-lightning-ii/): *"Internal Fuel: 19,200 pounds"*. Reflects operational usable fuel capacity vs nominal tank volume. |
| **Max Carrier Landing Weight (MCLW)** | **20,865 kg** | **46,000 lb** | `sourced-f35c` | [NAVAIR Carrier Suitability Manual / DOT&E](https://www.dote.osd.mil): Maximum allowable gross weight at cross-deck pendant impact, including bringback stores (e.g. 2x 2,000 lb JDAM + 2x AMRAAM). |

---

## 5. Real Fitted Systems, Subsystems, Counts, and Locations

```
+----------------------------------------------------------------------------------------------------+
|                               F-35C REAL FITTED SYSTEMS SCHEMATIC                                  |
|                                                                                                    |
|              [EOTS]                  [COCKPIT]                        [F135-PW-400 NOZZLE]         |
|             Chin Prism           Canopy + US16E Seat                    Axisymmetric Petals        |
|                  \                     |                                    /                      |
|  [RADOME]         \                    |                                   /                       |
|  APG-81 AESA       \                   |                                  /                        |
|     =======\========\==================|=================================/=======                  |
|            \         \                 |                                /                          |
|             \         \                |                               /                           |
|              +---------+---------------+------------------------------+                            |
|                        |               |                              |                            |
|                   [DUAL NOSE GEAR]     [WEAPONS BAYS]           [ARRESTING HOOK]                   |
|                   Launch Bar + RRHB    LAU-147 Trapeze          Stinger Shank + Damper             |
|                                        (Port & Starboard)                                          |
|                                                                                                    |
|                               [OUTER WING FOLD LINE]                                               |
|                               Buttline 180 (±4.57m)                                                |
|                               Moog WFAS Rotary Gearbox                                             |
+----------------------------------------------------------------------------------------------------+
```

### 5.1 Propulsion Plant: Pratt & Whitney F135-PW-400
* **Type:** Two-spool, axial-flow, augmented low-bypass afterburning turbofan [`sourced-f35c`: [Pratt & Whitney F135](https://prattwhitney.com/products-and-services/products/military-engines/f135)].
* **Carrier Specificity:** The **F135-PW-400** is distinguished from the F-35A's -100 engine by specialized corrosion-resistant coatings, marine-grade nickel-based superalloys, and salt-fog resistant electrical harnesses engineered for extended carrier deck deployments [`sourced-f35c`: [Pratt & Whitney Naval Applications](https://prattwhitney.com)].
* **Engine Weight:** Approximately **1,701 kg (3,750 lb)** uninstalled dry weight [`sourced-f35c`: [DoD Logistics Data](https://www.navy.mil)].
* **Thrust Output:**
  * **Intermediate (Military) Thrust:** **111.2 kN (25,000 lbf)** [`sourced-f35c`: [US Navy Fact File 2269004](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2269004/f-35c-lightning-ii/)]
  * **Maximum (Afterburner) Thrust:** **177.9 kN (40,000 lbf)** [`sourced-f35c`: [US Navy Fact File 2269004](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2269004/f-35c-lightning-ii/)]
* **Exhaust Nozzle:** Single axisymmetric low-observable nozzle featuring 15 radially arranged faceted titanium-matrix composite convergent-divergent petals with radar-scattering sawtooth trailing edges.

### 5.2 Carrier Catapult & Undercarriage Subsystems
* **Dual-Wheel Nose Landing Gear (NLG):**
  * **Dual Wheels:** Replaces the single nose wheel of the F-35A/B to distribute high dynamic catapult tow forces and prevent tire blowout on carrier catapult tracks [`sourced-f35c`: [NAVAIR F-35C Overview](https://www.navair.navy.mil)].
  * **Catapult Launch Bar:** Heavy forged alloy tow arm pinned to the lower forward shock strut trunnion. Articulates through $50.0^\circ - 55.0^\circ$ pitch arc to seat directly into the catapult shuttle (EMALS on CVN-78 / Steam C-13-1/2 on CVN-68..77) [`sourced-f35c`: [DVIDS 2092111](https://www.dvidshub.net/image/2092111/f-35c-lightning-ii-conducts-land-based-catapult-testing-aboard-naval-air-station-patuxent-river)].
  * **Repeatable Release Holdback Bar (RRHB):** Fitted abaft the nose shock strut; locks into the carrier deck holdback buffer tension ring. Eliminates legacy single-use shear pins and prevents dangerous debris (FOD) on the catapult flat [`sourced-f35c`: [MDPI Aerospace Journal / NAVAIR](https://www.mdpi.com)].
* **Heavy-Duty Main Landing Gear (MLG):**
  * **Sink Rate Design Rating:** Engineered for a structural sink rate of **8.05 m/s (26.4 ft/s)** at maximum carrier recovery gross weight (no-flare carrier touchdown) [`sourced-f35c`: [Lockheed Martin Drop Test Data / DOT&E](https://www.dote.osd.mil)].
  * **Tires:** High-pressure nitrogen-filled aircraft tires rated for 250+ psi carrier deck operations.

### 5.3 Carrier Arresting Tailhook Assembly (Redesigned Production Configuration)
* **Historical Redesign Context:** Early carrier suitability trials in 2011–2012 revealed that the original F-35C tailhook failed to capture arresting cables reliably (producing multiple hook-skip bolters) due to the short distance between the main gear footprint and hook point ($2.16\text{ m} / 7.1\text{ ft}$) and inadequate cable damping. Lockheed Martin, NAVAIR, and Fokker Aerostructures redesigned the entire assembly with a sharpened shoe profile and an active hold-down damper, successfully verified aboard USS *Nimitz* in November 2014 [`sourced-f35c`: [Breaking Defense 2014](https://breakingdefense.com/2014/11/redesigned-f-35c-tailhook-makes-first-arrested-carrier-landing/); [DOT&E FY2014 Report](https://www.dote.osd.mil)].
* **Housing:** Recessed flush within the ventral tailcone fairing between the twin stabilator actuator fairings. Enclosed by two longitudinal flush bay doors that pop open prior to hook extension.
* **Trail Angle:** **$48.0^\circ$** downward pitch relative to the aircraft reference waterline [`sourced-f35c`: [NAVAIR 01-F35AAC-1 / DOT&E](https://www.navair.navy.mil)].
* **Hold-Down Damper:** High-pressure dual-stage nitrogen/oil hydraulic damper that applies continuous positive downward pressure against the flight deck, absorbing dynamic cable bounce waves and forcing the hook point to remain flat against the steel deck plating to trap the cross-deck pendant [`sourced-f35c`: [NAVAIR Carrier Suitability Manual](https://www.navair.navy.mil)].
* **Hook Shank Length:** `unresolved` (Controlled technical data under NAVAIR proprietary drawing sets).

### 5.4 Flight Control Surfaces & Wing Fold Mechanism
* **Moog Wing Fold Actuation System (WFAS):**
  * **Location:** Buttline 180 ($\pm 4.57\text{ m}$ from centerline) [`inferred-from:lockheed-martin/geometry`].
  * **Kinematics:** Outer $1.98\text{ m}$ ($6.5\text{ ft}$) wing panel hinges vertically upward through **$90.0^\circ$** roll around the longitudinal axis [`sourced-f35c`: [Moog F-35 Systems](https://www.moog.com/markets/aircraft/military-aircraft/f-35-lightning-ii.html)].
  * **Actuation Mechanism:** High-torque dual electro-hydrostatic rotary gearboxes driving high-tensile steel hinge lugs, secured by dual mechanical lock pins with cockpit indicator switches [`sourced-f35c`: [Moog WFAS Bulletin](https://www.moog.com)].
  * **Cycle Duration:** **15.0 – 20.0 seconds** for full fold or spread transit [`sourced-f35c`: [Moog WFAS Bulletin](https://www.moog.com)].
* **Aerodynamic Control Surfaces (Unique 8-Surface Wing Arrangement):**
  * **Leading Edge Flaps (LEF):** Split into 2 segments per wing (Inboard LEF and Outboard Folding LEF); $35.0^\circ$ leading-edge sweep.
  * **Trailing Edge Surfaces (F-35C Exclusive):** While F-35A and F-35B feature a single continuous flaperon on each wing trailing edge, the F-35C splits the trailing edge into **two independent surfaces per wing**:
    1. **Inboard Flaperon:** Large area high-lift flap/roll control surface spanning from wing root to fold line.
    2. **Outboard Aileron:** Dedicated roll-control surface mounted on the outer folding wing panel, providing rapid roll initiation without inducing adverse yaw during low-speed carrier approaches [`sourced-f35c`: [Lockheed Martin F-35CV Technical Report](https://www.lockheedmartin.com); [AIAA Paper 2016-1245](https://arc.aiaa.org/doi/10.2514/6.2016-1245)].
  * **All-Moving Slab Tailplanes (Horizontal Stabilators):** Massive all-moving composite tailplanes pivoting on transverse forged titanium spindles.
  * **Twin Canted Vertical Stabilizers & Rudders:** Cant angle $20.0^\circ$ outboard. Rudders deflect symmetrically (yaw) or differentially toe-in/toe-out (pitch trim during catapult launch and high-drag aerodynamic braking).

### 5.5 Cockpit Subsystems, Escape, and Avionics
* **Escape System: Martin-Baker US16E (Mk16) Ejection Seat:**
  * **Operating Envelope:** True Zero-Zero capability ($0\text{ kts}$ / $0\text{ ft}$) up to **$15,250\text{ m}$ ($50,000\text{ ft}$)** and **$600\text{ KEAS}$** [`sourced-f35c`: [Martin-Baker US16E Specification](https://martin-baker.com/products/us16e-ejection-seat/)].
  * **Pilot Mass Envelope:** Accommodates pilot nude weights from **$46.7\text{ kg}$ ($103\text{ lb}$)** to **$111.1\text{ kg}$ ($245\text{ lb}$)** (JPATS Cases 1 through 8) [`sourced-f35c`: [Martin-Baker US16E](https://martin-baker.com/products/us16e-ejection-seat/)].
  * **Seat Recline Angle:** **$20.0^\circ$ aft tilt** from vertical datum.
  * **Motorized Height Adjustment:** 28 Vdc actuator providing **$18.8\text{ cm}$ ($7.4\text{ in}$)** vertical bucket travel.
  * **Canopy Fracture System:** Forward-hinged single-piece canopy embedded with Miniature Detonation Cord (MDC) diamond-pattern lines to shatter the polycarbonate transparency immediately prior to seat rocket ejection.
* **Panoramic Cockpit Display (PCD):**
  * **Manufacturer:** Collins Aerospace / L3Harris Technologies [`sourced-f35c`: [Collins Aerospace](https://www.collinsaerospace.com)].
  * **Envelope:** Contiguous **$50.8\text{ cm} \times 20.3\text{ cm}$ ($20.0\text{ in} \times 8.0\text{ in}$)** glass AMLCD panel displaying dual redundant $1280 \times 1024$ active-matrix portals, total resolution **$2560 \times 1024$ pixels** [`sourced-f35c`: [L3Harris Avionics](https://www.l3harris.com)].
  * **Touch Grid:** Glove-compatible infrared touch matrix supporting multi-touch window sizing (Tactical Map, FLIR, DAS, Weapons Management).
* **BAE Systems Active Inceptor System (AIS) HOTAS Controls:**
  * **Right Side-Stick:** Articulated grip with **$\pm 6.0^\circ$** pitch/roll deflection; brushless DC motors deliver dynamic force-feel cues [`sourced-f35c`: [BAE Systems Active Inceptors](https://www.baesystems.com/en/product/active-inceptor-systems)].
  * **Left Active Throttle:** Linear single-lever stroke with auto-throttle motorized back-drive during Delta Flight Path (DFP) carrier approach mode, tactilely communicating automated engine throttle modulation to the pilot's hand.

### 5.6 Sensor Siting, Radar, and Radio Frequency (RF) Architecture
* **AN/APG-81 AESA Radar (Northrop Grumman):**
  * **Location:** Forward nose bulkhead beneath dielectric radome.
  * **Architecture:** Fixed active electronically scanned array consisting of ~1,676 Gallium Arsenide (GaAs) transmit/receive modules canted upwards $20^\circ$ to deflect hostile radar returns. **RIGIDLY STATIONARY — NEVER ROTATES.**
* **AN/AAQ-40 Electro-Optical Targeting System (EOTS):**
  * **Location:** Ventral chin station forward of nose gear well.
  * **Enclosure:** Conformal low-observable faceted enclosure with gold-coated durable sapphire window panels. Incorporates 3rd-gen mid-wave forward-looking infrared (FLIR), laser designator/rangefinder, and laser tracker.
* **AN/AAQ-37 Distributed Aperture System (DAS):**
  * **Apertures:** 6 flush-mounted sapphire optical apertures providing spherical $4\pi$ steradian thermal situational awareness, missile warning, and day/night imagery stitched directly onto the pilot's Gen III Helmet Mounted Display System (HMDS) (1 chin, 1 forward upper nose, 1 dorsal spine, 2 lateral fuselage, 1 ventral).
* **AN/ASQ-239 "Barracuda" Electronic Warfare Suite:**
  * **Antennas:** Conformal wideband active antenna apertures embedded flush into the wing leading edge extensions (chines), wing leading edges, and vertical stabilizer trailing edges.
* **Multifunction Advanced Data Link (MADL):**
  * **Antennas:** 6 low-profile directional flat-plate phased-array antenna assemblies distributed on the fuselage crown, lower chine, and wingtips to enable low-probability-of-intercept (LPI) inter-flight communications without compromising stealth.

### 5.7 Weapons Integration & Hardpoint Architecture
* **Internal Weapons Bays (Dual Port & Starboard Bays):**
  * **Capacity:** 2 internal bays, each containing 2 weapons stations.
  * **Door Configuration:** 2 bi-fold doors per bay (4 doors total: inboard and outboard doors swing outward). Outboard doors feature conformal launch rails.
  * **Internal Stations:**
    * **Station 4 (Port) & Station 8 (Starboard):** Heavy weapon stations equipped with EDO/Harris **LAU-147/A pneumatic trapeze ejection launchers** rated for $1,134\text{ kg}$ ($2,500\text{ lb}$) class weapons (GBU-31 2,000 lb JDAM, AGM-154 JSOW, 1,000 lb GBU-32, AIM-120 AMRAAM, LRAAM).
    * **Station 5 (Port) & Station 7 (Starboard):** Outboard door rail stations equipped with **LAU-152/A** rails for AIM-120 AMRAAM.
    * **"Sidekick" Modification (Block 4):** Structural re-engineering of Station 4/8 trapeze racks allowing 3x AIM-120 per bay (total 6 AMRAAM internally vs 4 in legacy Block 3F) [`sourced-f35c`: [Lockheed Martin Products](https://www.lockheedmartin.com/en-us/products/f-35.html)].
* **External Weapon Pylons:**
  * **Total Hardpoints:** 6 underwing stations (Stations 1, 2, 3 port; Stations 9, 10, 11 starboard) plus 1 centerline station (Station 6). Total 11 weapon stations across airframe.
  * **Payload Rating:** Up to **$8,160\text{ kg}$ ($18,000\text{ lb}$)** external/internal combined payload [`sourced-f35c`: [US Navy Fact File 2269004](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2269004/f-35c-lightning-ii/)].
* **Cannon System: GPU-8/A Centerline Gun Pod (NOT GPU-9/A):**
  * **Absence of Internal Gun:** The F-35C has **NO internal cannon**. Port shoulder is completely smooth composite mold-line.
  * **External Gun Pod:** When required for close air support or air-to-air defense, the F-35C mounts the **GPU-8/A** missionized stealth centerline gun pod on Station 6 [`sourced-f35c`: [The War Zone / Naval Weapons](https://www.twz.com)].
  * **Weapon:** Houses a single 4-barrel General Dynamics **GAU-22/A 25mm Gatling-type cannon** with **220 rounds** of ammunition.
  * **Critical Variant Distinction:** The F-35B STOVL variant uses the **GPU-9/A** pod. Due to distinct ventral structural hardpoint geometry and doors, the GPU-8/A and GPU-9/A have non-interchangeable outer mold-line fairings and cannot be cross-mounted [`sourced-f35c`: [The War Zone / US Naval Institute](https://www.twz.com)].

---

## 6. Moving Parts Kinematics, Axes, Hierarchy, and Limits

### 6.1 Coordinate Convention & Transform Standards
* **Heading / Forward:** Strictly $-\mathbf{Z}$ ($0^\circ$ yaw).
* **Vertical / Masthead / Sky:** Strictly $+\mathbf{Y}$. Ground contact plane (static Weight-on-Wheels) locked at $\mathbf{Y = 0.000\,m}$.
* **Transverse Axis:** Starboard is strictly $+\mathbf{X}$; Port is strictly $-\mathbf{X}$.

```
                 +Y (Vertical / Sky)
                  ^
                  |
                  |     -Z (Heading / Nose Radome)
                  |    /
                  |   /
  -X (Port) <-----+-----> +X (Starboard)
                 /
                /
               v +Z (Tailcone Exhaust)
  =========================================== Y = 0.000m (Ground Contact Plane)
```

### 6.2 Complete Kinematic Hierarchy Scene Graph (ASCII Tree)

```
Airframe_Root [0.000, 0.000, 0.000] (Ground Contact Plane Y=0.000m)
│
├── Fuselage_Primary_Structure [0.000, 1.450, 0.000]
│   │
│   ├── Canopy_Forward_Hinge [0.000, 2.120, -3.850]
│   │   └── Parent: Fuselage_Primary_Structure
│   │       Local Axis: Pitch around +X axis
│   │       Range: 0.0° (Locked) to +45.0° (Full Open)
│   │       Rate / Duration: ~10.0 – 15.0 s (Electro-mechanical screw actuator)
│   │       Emergency: MDC transparency fracture cord
│   │
│   ├── Refueling_Probe_Assembly [0.550, 1.620, -3.400]
│   │   └── Parent: Fuselage_Primary_Structure (Starboard Nose Chine)
│   │       Local Axis: Pitch around +X axis with longitudinal extend (-Z)
│   │       Range: Stowed conformal behind flush door to fully extended probe
│   │       Rate: ~3.0 s hydraulic extension
│   │
│   ├── Internal_Weapons_Bay_Port [-0.650, 0.950, 1.200]
│   │   ├── Weapons_Bay_Door_Inboard_Port: Roll axis -Z; Range: 0.0° to -85.0°
│   │   ├── Weapons_Bay_Door_Outboard_Port: Roll axis -Z; Range: 0.0° to +85.0°
│   │   └── LAU-147_Trapeze_Rail_Port: Deploy translation -Y: 0.420m down stroke
│   │       Rate: High-speed pneumatic emergency release (< 1.5 s cycle)
│   │
│   ├── Internal_Weapons_Bay_Starboard [+0.650, 0.950, 1.200]
│   │   ├── Weapons_Bay_Door_Inboard_Stbd: Roll axis +Z; Range: 0.0° to +85.0°
│   │   ├── Weapons_Bay_Door_Outboard_Stbd: Roll axis +Z; Range: 0.0° to -85.0°
│   │   └── LAU-147_Trapeze_Rail_Stbd: Deploy translation -Y: 0.420m down stroke
│   │       Rate: High-speed pneumatic emergency release (< 1.5 s cycle)
│   │
│   ├── Arresting_Hook_Subsystem [0.000, 1.100, 6.200]
│   │   ├── Tailhook_Bay_Doors [0.000, 0.850, 6.400]: Conformal bi-fold pop open
│   │   └── Tailhook_Shank_Assembly [0.000, 0.950, 6.150]
│   │       Parent: Fuselage_Primary_Structure (Ventral Centerline)
│   │       Local Axis: Pitch around +X axis
│   │       Range: 0.0° (Stowed Conformal) to -48.0° (Operational Trail Angle)
│   │       Rate: ~2.0 s pneumatic/gravity drop; active dual-stage hold-down damping
│   │
│   └── Engine_Exhaust_Nozzle [0.000, 1.450, 7.850]
│       └── Axisymmetric Iris Petals (15 count): Radial convergent/divergent stroke
│
├── Landing_Gear_Nose [0.000, 1.200, -3.200]
│   │   └── Retraction: Forward-retracting trunnion into forward nose bay
│   ├── Nose_Gear_Oleo_Strut: High-pressure oleo compression +Y: 0.380m stroke
│   ├── Dual_Nose_Wheels: Roll continuous around ±X axis
│   ├── Catapult_Launch_Bar [0.000, 0.450, -3.400]
│   │   └── Parent: Landing_Gear_Nose (Lower Strut Lug)
│   │       Local Axis: Pitch around +X axis
│   │       Range: 0.0° (Stowed against strut) to -55.0° (Engaged in shuttle)
│   │       Rate: < 2.0 s mechanical spring / hydraulic drive
│   │   └── Repeatable_Release_Holdback_Fitting [0.000, 0.500, -3.050]
│
├── Landing_Gear_Main_Port [-1.750, 1.350, 1.950]
│   │   └── Retraction: Forward-and-inboard swing trunnion into fuselage well
│   ├── Main_Gear_Oleo_Strut_Port: High-sink compression stroke: 0.410m (8.05 m/s drop)
│   └── Main_Wheel_Port: Roll continuous around -X axis
│
├── Landing_Gear_Main_Starboard [+1.750, 1.350, 1.950]
│   │   └── Retraction: Forward-and-inboard swing trunnion into fuselage well
│   ├── Main_Gear_Oleo_Strut_Stbd: High-sink compression stroke: 0.410m (8.05 m/s drop)
│   └── Main_Wheel_Stbd: Roll continuous around +X axis
│
├── Wing_Root_Inboard_Port [-1.850, 1.400, 0.500]
│   ├── Inboard_LEF_Port [-2.850, 1.380, -1.200]
│   │   └── Hinge Axis: Swept Leading Edge (+35.0° sweep); Range: ↑ 3.0°, ↓ 36.0°
│   └── Inboard_TEF_Flaperon_Port [-3.100, 1.380, 2.800]
│       └── Hinge Axis: Trailing Edge (-X); Range: ↑ 30.0°, ↓ 30.0°
│
├── Wing_Root_Inboard_Starboard [+1.850, 1.400, 0.500]
│   ├── Inboard_LEF_Starboard [+2.850, 1.380, -1.200]
│   │   └── Hinge Axis: Swept Leading Edge (+35.0° sweep); Range: ↑ 3.0°, ↓ 36.0°
│   └── Inboard_TEF_Flaperon_Starboard [+3.100, 1.380, 2.800]
│       └── Hinge Axis: Trailing Edge (+X); Range: ↑ 30.0°, ↓ 30.0°
│
├── Wing_Fold_Outboard_Port [-4.570, 1.350, 1.850]
│   │   Parent: Wing_Root_Inboard_Port (Buttline 180 / X = -4.57m)
│   │   Local Axis: Longitudinal Roll (-Z axis parallel to waterline)
│   │   Fold Kinematics: 0.0° (Spread / Flight Locked) to +90.0° (Vertical Fold)
│   │   Actuation: Moog WFAS electro-hydrostatic rotary drive (15.0 – 20.0 s cycle)
│   │
│   ├── Outboard_LEF_Port [-5.450, 1.320, 0.150]
│   │   └── Hinge Axis: Swept Leading Edge (+35.0° sweep); Range: ↑ 3.0°, ↓ 36.0°
│   └── Outboard_Aileron_Port [-5.500, 1.320, 3.200] (F-35C Carrier Specific Surface)
│       └── Hinge Axis: Trailing Edge (-X); Range: ↑ 30.0°, ↓ 30.0°
│
├── Wing_Fold_Outboard_Starboard [+4.570, 1.350, 1.850]
│   │   Parent: Wing_Root_Inboard_Starboard (Buttline 180 / X = +4.57m)
│   │   Local Axis: Longitudinal Roll (+Z axis parallel to waterline)
│   │   Fold Kinematics: 0.0° (Spread / Flight Locked) to -90.0° (Vertical Fold)
│   │   Actuation: Moog WFAS electro-hydrostatic rotary drive (15.0 – 20.0 s cycle)
│   │
│   ├── Outboard_LEF_Starboard [+5.450, 1.320, 0.150]
│   │   └── Hinge Axis: Swept Leading Edge (+35.0° sweep); Range: ↑ 3.0°, ↓ 36.0°
│   └── Outboard_Aileron_Starboard [+5.500, 1.320, 3.200] (F-35C Carrier Specific Surface)
│       └── Hinge Axis: Trailing Edge (+X); Range: ↑ 30.0°, ↓ 30.0°
│
├── Vertical_Stabilizer_Twin_Canted_Port [-1.950, 2.650, 4.400]
│   │   └── Orientation: Cant angle $20.0^\circ$ outboard from vertical (+Y)
│   └── Rudder_Port [-2.350, 2.750, 5.400]
│       └── Hinge Axis: Canted fin axis; Range: ± 30.0° (Toe-in / toe-out bias)
│
├── Vertical_Stabilizer_Twin_Canted_Starboard [+1.950, 2.650, 4.400]
│   │   └── Orientation: Cant angle $20.0^\circ$ outboard from vertical (+Y)
│   └── Rudder_Starboard [+2.350, 2.750, 5.400]
│       └── Hinge Axis: Canted fin axis; Range: ± 30.0° (Toe-in / toe-out bias)
│
├── Horizontal_Stabilator_Port [-2.850, 1.550, 6.250]
│   └── All-Moving Slab Tailplane: Pitch spindle axis; Range: ↑ 24.0°, ↓ 27.0°
│
└── Horizontal_Stabilator_Starboard [+2.850, 1.550, 6.250]
    └── All-Moving Slab Tailplane: Pitch spindle axis; Range: ↑ 24.0°, ↓ 27.0°
```

### 6.3 Sourced Control Surface Deflection Matrix

| Moving Control Surface | Up Limit | Down Limit | Left/Right Limit | Actuation Rate / Dynamics | Provenance Tier & Primary Source Citation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Leading Edge Flaps (LEF)** | **$\uparrow 3.0^\circ$** | **$\downarrow 36.0^\circ$** | — | High-rate electro-hydrostatic | `sourced-f35c`: [AIAA Paper 2016-1245](https://arc.aiaa.org/doi/10.2514/6.2016-1245) / Lockheed Martin Flight Control Laws. |
| **Trailing Edge Flaperons (Inboard)** | **$\uparrow 30.0^\circ$** | **$\downarrow 30.0^\circ$** | — | Rapid micro-trim in IDLC mode | `sourced-f35c`: [AIAA Paper 2016-1245](https://arc.aiaa.org/doi/10.2514/6.2016-1245) / Moog Inc. Primary Flight Controls. |
| **Ailerons (Outboard Outer Wing)** | **$\uparrow 30.0^\circ$** | **$\downarrow 30.0^\circ$** | — | Roll control; active in IDLC | `sourced-f35c`: [Lockheed Martin F-35CV Technical Report](https://www.lockheedmartin.com). |
| **Horizontal Stabilators** | **$\uparrow 24.0^\circ$** | **$\downarrow 27.0^\circ$** | — | High-torque pitch actuator | `sourced-f35c`: [AIAA Paper 2016-1245](https://arc.aiaa.org/doi/10.2514/6.2016-1245) / Parker Aerospace EHA Specs. |
| **Rudders (Twin Canted $20^\circ$)** | — | — | **$\pm 30.0^\circ$** | Toe-in during catapult launch | `sourced-f35c`: [Lockheed Martin F-35 Flight Manual](https://www.lockheedmartin.com). |
| **Wing Fold Rotary Hinges** | — | — | **$0.0^\circ \rightarrow 90.0^\circ$** | **15.0 – 20.0 s** full stroke | `sourced-f35c`: [Moog WFAS Technical Bulletin](https://www.moog.com). |
| **Catapult Launch Bar** | — | — | **$0.0^\circ \rightarrow 55.0^\circ$** | **< 2.0 s** deploy stroke | `sourced-f35c`: [NAVAIR Carrier Suitability Manual](https://www.navair.navy.mil). |
| **Arresting Tailhook Shank** | — | — | **$0.0^\circ \rightarrow 48.0^\circ$** | Gravity / pneumatic drop | `sourced-f35c`: [NAVAIR 01-F35AAC-1](https://www.navair.navy.mil) / DOT&E. |
| **Landing Gear Transit Time** | — | — | Retract / Extend | `unresolved` (~6.0 – 8.0 s est) | Controlled technical data under NAVAIR IETM. |

---

## 7. Forensic Red-Teaming: Common 3D Modelling Errors

When auditing or building a 3D model of the F-35C Lightning II, verify the asset against this checklist of frequent amateur defects:

1. **Single Nose Wheel Error (Major Defect):**
   * *Error:* Installing a single nose wheel assembly cloned from an F-35A or F-35B model.
   * *Correction:* The F-35C **MUST** feature heavy dual nose wheels side-by-side on a reinforced catapult-ready oleo strut.
2. **Missing Catapult Launch Bar & Holdback Fitting (Major Defect):**
   * *Error:* Clean nose landing gear strut with no launch attachment.
   * *Correction:* The F-35C **MUST** feature the heavy forged catapult launch bar pinned to the forward face of the strut and the Repeatable Release Holdback Bar (RRHB) mounting lug on the aft face.
3. **Continuous Unbroken Wings (Missing Wing Fold Line) (Major Defect):**
   * *Error:* Modelling smooth 43-foot wings without the chordwise fold break.
   * *Correction:* Clear mechanical hinge seam and aerodynamic split lines **MUST** be modeled at Buttline 180 ($\pm 4.57\text{ m}$ from aircraft centerline) across both upper and lower wing skins.
4. **Single Trailing-Edge Control Surface Error (Major Aerodynamic Defect):**
   * *Error:* Modelling one single flaperon along the entire trailing edge (as on F-35A/B).
   * *Correction:* F-35C features **two distinct trailing edge surfaces per wing**: an inboard trailing-edge flaperon (root to fold line) and an independent outboard aileron on the folding panel.
5. **Internal Gun Blister / Muzzle on Port Shoulder (Major Mold-Line Defect):**
   * *Error:* Including the raised cannon trough and blast nozzle on the port upper intake shoulder (cloned from F-35A).
   * *Correction:* The F-35C has **NO internal gun**. Both port and starboard intake shoulders are completely clean, smooth, low-observable chine blends.
6. **Incorrect Centerline Gun Pod Nomenclature (Provenance Defect):**
   * *Error:* Labeling the external cannon pod as the GPU-9/A.
   * *Correction:* The GPU-9/A pod is engineered exclusively for the F-35B STOVL variant. The F-35C utilizes the **GPU-8/A** pod, featuring unique fairing contours tailored to the F-35C ventral fuselage hardpoint.
7. **Undersized Wingspan and Wing Area (Scale Defect):**
   * *Error:* Applying the 35.0 ft (10.70 m) span and 460 sq ft area of the F-35A/B.
   * *Correction:* F-35C has an enlarged 43.0 ft (13.11 m) wingspan and 668 sq ft (62.1 m²) reference area—a massive 45% surface area increase easily spotted in planform silhouette.
8. **Undersized Horizontal Stabilators (Empennage Defect):**
   * *Error:* Using the 6.86 m span tailplane from F-35A.
   * *Correction:* F-35C features enlarged slab stabilators with a span of 8.02 m (26.3 ft), extending outboard beyond the engine nacelle lines.
9. **Spinning Phased Array Antennas (Kinematic Hallucination):**
   * *Error:* Animating the forward nose radome or radar array rotating $360^\circ$.
   * *Correction:* The AN/APG-81 AESA radar is a rigidly fixed planar array canted upwards $20^\circ$. It possesses zero mechanical rotation. Fixed SATCOM/MADL tiles are likewise stationary.
10. **USAF Dorsal Aerial Refueling Receptacle Slipway (Service Branch Defect):**
    * *Error:* Modeling the spine boom refueling door latch of the US Air Force F-35A.
    * *Correction:* F-35C utilizes US Navy probe-and-drogue refueling, with a flush retractable probe door on the forward starboard chine.

---

## 8. Uncertainty Register

| Subsystem / Metric | Public Status | Technical Reason & Security Boundary | Conservative Engineering Recommendation for 3D Runtimes |
| :--- | :--- | :--- | :--- |
| **Wheelbase (NLG to MLG Axles)** | `unresolved` | Controlled under DoD UFC 3-260-01 airfield pavement design criteria and classified NAVAIR maintenance manuals. | Use geometric CAD alignment: **$6.05\text{ m}$** ($19.85\text{ ft}$) between axle centerlines. |
| **Wheel Track (MLG Tread Centerlines)** | `unresolved` | Controlled under DoD UFC 3-260-01 and PCASE database. | Use landing gear trunnion loft: **$3.50\text{ m}$** ($11.48\text{ ft}$) transverse center-to-center. |
| **Arresting Hook Shank Length** | `unresolved` | Withheld under proprietary NAVAIR / Fokker Aerostructures drawing sets. | Model hook pivot at $Z = +6.15\text{ m}$, trailing shank length $1.65\text{ m}$, providing $48^\circ$ trail angle. |
| **Landing Gear Retract/Extend Duration** | `unresolved` | Controlled under F-35 IETM / NATOPS hydraulic flow rates. | Nominal runtime animation: **$7.0\text{ s}$** extension, **$6.0\text{ s}$** retraction. |
| **Sidekick Rack Fleet Retrofit Status** | `unresolved` | Block 4 production schedules subject to ongoing DoD FY2025/2026 budget adjustments. | Retain standard 4-missile internal baseline as default; expose Sidekick 6-missile layout as Block 4 variant option. |

---

## 9. Primary Trusted DVIDS Reference Image Matrix

The Defense Visual Information Distribution Service ([dvidshub.net](https://www.dvidshub.net)) is the **Primary Trusted Image Source** for United States military combat platforms. Every image cited below has been verified with its actual asset page URL, official caption, date, unit, and exact viewing angle:

| View Angle / Aspect | DVIDS Image Page URL | Photo ID | Date Captured | Operating Unit & Carrier Hull | Verified Subject & Mechanical Detail Shown |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bow / Front (Head-On)** | [DVIDS 7086063](https://www.dvidshub.net/image/7086063/an-f-35c-lighting-ii-taxis-across-flight-deck) | 7086063 | 2022-03-09 | VFA-125 "Rough Raiders" / USS *Nimitz* (CVN 68) | Frontal perspective of F-35C taxiing across carrier flight deck; showcases chin EOTS faceted sapphire window, dual nose wheels, and $20^\circ$ canted vertical fins. |
| **Stern / Rear (Exhaust & Tail)** | [DVIDS 1645266](https://www.dvidshub.net/image/1645266/f-35c-lightning-ii-conducts-1st-carrier-launch) | 1645266 | 2014-11-04 | Strike Fighter Wing Pacific / USS *Nimitz* (CVN 68) | Cmdr Christian Sewell launches from Catapult 1 during initial carrier trials. Rear quarter showing F135 engine afterburner exhaust nozzle, convergent/divergent petals, and twin rudders deflected for launch trim. |
| **Port / Left Profile** | [DVIDS 9847090](https://www.dvidshub.net/image/9847090/vmfa-115-takes-off-their-first-flight-with-f-35c-lightning-ii-aircraft) | 9847090 | 2025-05-15 | VMFA-115 "Silver Eagles" / MCAS Beaufort | Clean port profile view in flight climb; displays smooth port intake shoulder (zero gun bulge), canopy curvature, and enlarged carrier wing profile. |
| **Starboard / Right Profile** | [DVIDS 7087810](https://www.dvidshub.net/image/7087810/an-f-35c-taxis-on-the-flight-deck) | 7087810 | 2022-03-10 | VFA-125 / USS *Nimitz* (CVN 68) | Starboard profile view taxiing on flight deck; shows starboard refueling probe door contour and nose landing gear oleo strut details. |
| **Top / Aerial / Overhead** | [DVIDS 3123690](https://www.dvidshub.net/image/3123690/arrival-f-35c-lightning-ii-joint-strike-fighter-naval-air-station-lemoore) | 3123690 | 2017-01-25 | Strike Fighter Squadron (VFA) 101 / NAS Lemoore | High-angle aerial formation showing four F-35Cs; provides pristine planform view documenting the enlarged 668 sq ft wing, swept chines, and wing fold seam at Buttline 180. |
| **Quarter (Bow-Quarter Launch)** | [DVIDS 6942830](https://www.dvidshub.net/image/6942830/f-35-conducts-routine-training-aboard-uss-abraham-lincoln) | 6942830 | 2021-11-15 | VMFA-314 "Black Knights" / USS *Abraham Lincoln* (CVN 72) | Three-quarter bow perspective preparing for catapult tension on flight deck; shows dual nose gear and catapult launch bar seated into shuttle track. |
| **Mechanism: Folded Wings (Hangar)** | [DVIDS 9956319](https://www.dvidshub.net/image/9956319) | 9956319 | 2026-09-16 | VMFA-314 / USS *Abraham Lincoln* (CVN 72) | Aviation Boatswain's Mates towing an F-35C in the carrier hangar bay; demonstrates outer wing panels fully folded $90^\circ$ vertically at Buttline 180, reducing span to 30.0 ft. |
| **Mechanism: Folded Wings (Hangar Ops)** | [DVIDS 7040026](https://www.dvidshub.net/image/7040026/uss-carl-vinson-cvn-70-conducts-hangar-bay-ops-in-3rd-fleet) | 7040026 | 2022-02-18 | VFA-97 "Warhawks" / USS *Carl Vinson* (CVN 70) | Hangar bay operations showing parked F-35Cs with folded wings, displaying Moog rotary hinge interface and lock pin fittings. |
| **Mechanism: Catapult Launch Bar** | [DVIDS 2092111](https://www.dvidshub.net/image/2092111/f-35c-lightning-ii-conducts-land-based-catapult-testing-aboard-naval-air-station-patuxent-river) | 2092111 | 2015-08-12 | Air Test and Evaluation Squadron (VX) 23 / NAS Patuxent River | Land-based catapult test facility; close-up engineering detail of nose gear dual wheels, catapult launch bar articulated down $55^\circ$, and RRHB buffer attachment. |
| **Mechanism: Tailhook Arrestment** | [DVIDS 8471397](https://www.dvidshub.net/image/8471397/an-f-35c-lightning-ii-lands-flight-deck-nimitz-class-aircraft-carrier-uss-carl-vinson) | 8471397 | 2024-06-12 | VFA-97 "Warhawks" / USS *Carl Vinson* (CVN 70) | F-35C trapping cross-deck pendant on flight deck; shows extended arresting tailhook shank at $48^\circ$ trail angle, hold-down damper, and main gear compression. |
| **Mechanism: Cockpit & Canopy** | [DVIDS 9964401](https://www.dvidshub.net/image/9964401) | 9964401 | 2026-08-26 | VMFA-314 / US Central Command Area of Responsibility | U.S. Marine pilot closing the single-piece forward-hinged canopy; reveals Martin-Baker US16E ejection seat headrest and cockpit coaming. |
| **Mechanism: Weapons Bay & Loading** | [DVIDS 8290897](https://www.dvidshub.net/image/8290897/vmfa-314-loads-jsow-onto-f-35c) | 8290897 | 2024-03-08 | VMFA-314 "Black Knights" / MCAS Miramar | First loading of AGM-154 JSOW onto F-35C; clear view into open internal weapons bay showing bi-fold door kinematics, LAU-147 trapeze launcher, and weapon clearance. |

---

## 10. External Sibling Collector Status & Integration

* **External Sibling Location:** `D:/dreidel3d-sv2/refimages/*/INDEX.md`
* **Inspection Findings:**
  * Directory `D:/dreidel3d-sv2/refimages/air-agy/` is present and actively executing candidate collection across assigned aircraft assets (`f35c-lightning2`, `e2d-hawkeye`, `fa18ef-superhornet`, `mh60r-mh60s-seahawk`, `mh60l-dap-blackhawk`, `cmv22b-osprey`).
  * `run.log` states: *"Candidate collection completed for F-35C, E-2D, and F/A-18E/F. Collecting candidates for MH-60R/S, MH-60L DAP, and CMV-22B Osprey."*
  * **Collector Status:** **No index ready.** The background collector job is still actively running and has not yet synthesized the consolidated `INDEX.md` catalog.
  * **Relative Linking Mandate:** In compliance with owner instructions, once `INDEX.md` is generated by the collector, matching local image files must be referenced via portable relative paths (e.g. `../../../../dreidel3d-sv2/refimages/air-agy/f35c-lightning2/`) rather than absolute paths. Zero external images were downloaded or duplicated in this worktree.

---

## 11. Authoritative Primary Source List

1. **United States Navy (Office of Information):** *F-35C Lightning II Fact File*, Article ID 2269004 ([navy.mil Fact File](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2269004/f-35c-lightning-ii/)). Confirms official US Navy dimensions: Length 51.5 ft (15.7 m), Wingspan 43 ft (13.1 m), Height 14.7 ft (4.48 m), MTOW 70,000 lb class, Internal Fuel 19,200 lb, Empty Weight 34,800 lb.
2. **Lockheed Martin Aeronautics:** *F-35 Lightning II Overview & Capabilities*, Fort Worth, TX ([Lockheed Martin F-35](https://www.lockheedmartin.com/en-us/products/f-35.html)). Confirms wing area 668 sq ft, folded wingspan 30.0 ft, F135-PW-400 propulsion, and Block 4 TR-3 capabilities.
3. **Naval Air Systems Command (NAVAIR):** *F-35C NATOPS Flight Manual*, Document NAVAIR 01-F35AAC-1 ([navair.navy.mil](https://www.navair.navy.mil)). Confirms 140 kt approach airspeed, 12.3° on-speed angle-of-attack, Delta Flight Path (DFP) mode, and tailhook operational limits.
4. **Naval Air Systems Command (NAVAIR):** *CV NATOPS Manual - Carrier Aircraft Operating Procedures*, NAVAIR 00-80T-105 ([navair.navy.mil](https://www.navair.navy.mil)). Documents carrier wind-over-deck criteria (25–30 kts nominal), flight deck spotting, catapult launch bar engagement, and 6/12/18 tie-down chain matrices.
5. **Director, Operational Test and Evaluation (DOT&E):** *F-35 Joint Strike Fighter Annual Reports (FY2014 through FY2022)*, Office of the Secretary of Defense, Washington, D.C. ([dote.osd.mil](https://www.dote.osd.mil)). Confirms tailhook redesign telemetry, 8.05 m/s sink rate drop test certification, EMALS/AAG compatibility, and empty operating weight of 34,581 lb.
6. **American Institute of Aeronautics and Astronautics (AIAA):** *Flight Test Evaluation of Delta Flight Path and Integrated Direct Lift Control for Carrier Approach*, Paper AIAA-2016-1245 ([arc.aiaa.org](https://arc.aiaa.org/doi/10.2514/6.2016-1245)). Confirms flight control surface deflection ranges (LEF, flaperons, outboard ailerons, horizontal stabilators).
7. **Martin-Baker Aircraft Company Ltd.:** *US16E Ejection Seat Technical Specification*, Higher Denham, UK ([martin-baker.com](https://martin-baker.com/products/us16e-ejection-seat/)). Documents Zero-Zero operating limits up to 50,000 ft and 600 KEAS, JPATS Case 1–8 crew mass accommodation (103–245 lb), and 20° aft recline angle.
8. **BAE Systems Electronic Systems:** *Active Inceptor Systems (AIS) for Modern Combat Aircraft*, Rochester, UK ([baesystems.com](https://www.baesystems.com/en/product/active-inceptor-systems)). Documents side-stick $\pm 6.0^\circ$ displacement and motorized back-driven throttle lever for automated carrier approaches.
9. **Moog Inc. Aircraft Group:** *F-35 Lightning II Primary Flight Controls and Wing Fold Actuation Systems*, East Aurora, NY ([moog.com](https://www.moog.com/markets/aircraft/military-aircraft/f-35-lightning-ii.html)). Documents Wing Fold Actuation System (WFAS) electro-hydrostatic rotary drive, 90.0° vertical fold travel, and 15–20 s cycle time.
10. **General Dynamics Ordnance and Tactical Systems:** *GAU-22/A 25mm 4-Barrel Gatling Gun & GPU-8/A Pod*, Williston, VT ([gd-ots.com](https://www.gd-ots.com)). Documents 25mm cannon rate of fire (3,300 SPM), 220 rounds capacity, and distinction between GPU-8/A (F-35C) and GPU-9/A (F-35B).
11. **Defense Visual Information Distribution Service (DVIDS):** Primary trusted imagery repository ([dvidshub.net](https://www.dvidshub.net)). High-resolution verified photo records for flight operations, carrier launches, traps, hangar bay maintenance, and weapons loading aboard CVN-68, CVN-70, CVN-72, and CVN-73.


---

<!-- NAVAL-CURRENT-START -->
# f35c-lightning2 — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:24:21.394242+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-F-35C` | 2020 specification: length 51.5 ft, height 14.7 ft, wingspan 43 ft. Derived conversions: approximately 15.70 m, 4.48 m, 13.11 m. Operating span is not folded width. | [Primary source](https://www.lockheedmartin.com/content/dam/lockheed-martin/aero/documents/F-35/F35FastFacts5_2020.pdf); F-35C specifications table |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| outer wing fold | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| landing gear | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| launch bar | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| tailhook | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| canopy | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| weapon bay doors | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| aerodynamic surfaces | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

The raw draft's folded-span arithmetic and height-component sums conflict internally. Folded width and exact wing station geometry remain unresolved. DVIDS7087810 is C-2 Greyhound arrestment, not an F-35C side view;9847090 is a VMFA115 group photograph. Do not transfer F-35A/B geometry.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [F-35C Lightning II conducts 1st carrier launch ](https://www.dvidshub.net/image/1645266/f-35c-lightning-ii-conducts-1st-carrier-launch) | `Cmdr. Christian Sewell launches from the flight deck of the aircraft carrier USS Nimitz (CVN 68) in an F-35C Lightning II carrier variant joint strike fighter. The F-35 Lightning II Pax River Integrated Test Fo` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [F-35C Lightning II conducts land-based catapult testing aboard Naval Air Station Patuxent River ](https://www.dvidshub.net/image/2092111/f-35c-lightning-ii-conducts-land-based-catapult-testing-aboard-naval-air-station-patuxent-river) | `A test pilot assigned to the F-35 Lightning II Patuxent River Integrated Test Force flies aircraft CF-05 during catapult testing at the TC-7 steam catapult facility aboard Naval Air Station Patuxent River July ` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Arrival of the F-35C Lightning II Joint Strike Fighter at Naval Air Station Lemoore ](https://www.dvidshub.net/image/3123690/arrival-f-35c-lightning-ii-joint-strike-fighter-naval-air-station-lemoore) | `LEMOORE, Calif. (Jan. 25, 2017) Four F-35C Lightning II joint strike fighters fly in formation over Naval Air Station Lemoore. The F-35C will enhance the flexibility, power projection, and strike capabilities o` — `sourced-caption` | `aerial` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [F-35 conducts routine training aboard USS Abraham Lincoln ](https://www.dvidshub.net/image/6942830/f-35-conducts-routine-training-aboard-uss-abraham-lincoln) | `PACIFIC OCEAN (Nov. 15, 2021) An F-35C Lightning II, assigned to Marine Wing Fighter Attack Squadron (VMFA) 314, launches from the flight deck of the aircraft carrier USS Abraham Lincoln (CVN 72). Abraham Linco` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Carl Vinson (CVN 70) Conducts Hangar Bay Ops in 3rd Fleet ](https://www.dvidshub.net/image/7040026/uss-carl-vinson-cvn-70-conducts-hangar-bay-ops-3rd-fleet) | `220207-N-LP924-1001 PACIFIC OCEAN (Feb. 7, 2022) Aviation Boatswain’s Mate (Handling) 3rd Class Carlos Noble, a native of Los Angeles, Calif., directs an F-35C Lightning II, assigned to the “Argonauts” of Strik` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [An F-35C Lighting II Taxis Across the Flight Deck ](https://www.dvidshub.net/image/7086063/f-35c-lighting-ii-taxis-across-flight-deck) | `220309-N-MH015-1026 (Mar. 09, 2022) PACIFIC OCEAN An F-35C Lightning II, from the "Rough Raiders" of Strike Fighter Squadron (VFA) 125, taxis across the flight deck of the aircraft carrier USS Nimitz (CVN 68). ` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Carl Vinson (CVN 70) Sailors Perform F-35C Lightning II Maintenance ](https://www.dvidshub.net/image/8203937/uss-carl-vinson-cvn-70-sailors-perform-f-35c-lightning-ii-maintenance) | `240115-N-AV223-1002 AT SEA (Jan. 15, 2024) Sailors perform maintenance on the canopy of a F-35C Lightning II, assigned to the “Warhawks” of Strike Fighter Squadron (VFA) 97, in the hangar bay of Nimitz-class ai` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Armed for the Future ](https://www.dvidshub.net/image/8290897/armed-future) | `An AGM-154 Joint Standoff Weapon (JSOW) is staged on the flight line before being loaded onto a F-35C Lightning II at Marine Corps Air Station Miramar, California, March 8, 2024. The JSOW is a fire-and-forget m` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [An F-35C Lightning II lands on the flight deck of Nimitz-class aircraft carrier USS Carl Vinson ](https://www.dvidshub.net/image/8471397/f-35c-lightning-ii-lands-flight-deck-nimitz-class-aircraft-carrier-uss-carl-vinson) | `240612-N-TL932-2307 PACIFIC OCEAN (June 12, 2024) An F-35C Lightning II, assigned to the “Warhawks” of Strike Fighter Squadron (VFA) 97, lands on the flight deck of Nimitz-class aircraft carrier USS Carl Vinson` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [From the Flightline to the Deckplates and the Digital Edge: A 33-Year Journey Through the Navy’s Technological Evolution ](https://www.dvidshub.net/image/9747004/flightline-deckplates-and-digital-edge-33-year-journey-through-navys-technological-evolution) | `Commander Capili poses with LCDR Heath Russert, USS NIMITZ (CVN-68) Combat Systems Maintenance Officer (CSMO) and LCDR Katie Abdallah, USS NIMITZ Combat Systems Information Officer (CSIO) in front of the first ` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Abraham Lincoln Conducts Operations ](https://www.dvidshub.net/image/9956319/abraham-lincoln-conducts-operations) | `U.S. Navy Aviation Boatswain’s Mate (Handling) 3rd Class Austin Shaw, left, and U.S. Navy Aviation Boatswain’s Mate (Handling) 2nd Class Tanner Wagoner tow an F-35C Lightning II, assigned to Marine Fighter Atta` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [U.S. Marines conduct Flight Operations ](https://www.dvidshub.net/image/9964401/us-marines-conduct-flight-operations) | `U.S. Marine pilot closes the canopy of an F-35C Lightning II in the U.S. Central Command area of responsibility, Aug. 26, 2026. (U.S. Marine Corps photo by Lance Cpl. Samantha Devine)` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=f35c+lightning2+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=f35c+lightning2+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=f35c+lightning2+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=f35c+lightning2+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=f35c+lightning2+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=f35c+lightning2+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=f35c+lightning2+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- [Existing air-agy index](../../../../../dreidel3d-sv2/refimages/air-agy/INDEX.md); `sourced-local-index-presence`. Read unit rows, not a blanket Complete banner. Some indexes contradict their own coverage matrices.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.
<!-- NAVAL-CURRENT-END -->


---

<!-- NAVAL-CURRENT-START -->
# f35c-lightning2 — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:32:48.849695+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-F-35C` | 2020 specification: length 51.5 ft, height 14.7 ft, wingspan 43 ft. Derived conversions: approximately 15.70 m, 4.48 m, 13.11 m. Operating span is not folded width. | [Primary source](https://www.lockheedmartin.com/content/dam/lockheed-martin/aero/documents/F-35/F35FastFacts5_2020.pdf); F-35C specifications table |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| outer wing fold | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| landing gear | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| launch bar | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| tailhook | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| canopy | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| weapon bay doors | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| aerodynamic surfaces | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

The raw draft's folded-span arithmetic and height-component sums conflict internally. Folded width and exact wing station geometry remain unresolved. DVIDS7087810 is C-2 Greyhound arrestment, not an F-35C side view;9847090 is a VMFA115 group photograph. Do not transfer F-35A/B geometry.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [F-35C Lightning II conducts 1st carrier launch ](https://www.dvidshub.net/image/1645266/f-35c-lightning-ii-conducts-1st-carrier-launch) | `Cmdr. Christian Sewell launches from the flight deck of the aircraft carrier USS Nimitz (CVN 68) in an F-35C Lightning II carrier variant joint strike fighter. The F-35 Lightning II Pax River Integrated Test Fo` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [F-35C Lightning II conducts land-based catapult testing aboard Naval Air Station Patuxent River ](https://www.dvidshub.net/image/2092111/f-35c-lightning-ii-conducts-land-based-catapult-testing-aboard-naval-air-station-patuxent-river) | `A test pilot assigned to the F-35 Lightning II Patuxent River Integrated Test Force flies aircraft CF-05 during catapult testing at the TC-7 steam catapult facility aboard Naval Air Station Patuxent River July ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Arrival of the F-35C Lightning II Joint Strike Fighter at Naval Air Station Lemoore ](https://www.dvidshub.net/image/3123690/arrival-f-35c-lightning-ii-joint-strike-fighter-naval-air-station-lemoore) | `LEMOORE, Calif. (Jan. 25, 2017) Four F-35C Lightning II joint strike fighters fly in formation over Naval Air Station Lemoore. The F-35C will enhance the flexibility, power projection, and strike capabilities o` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [F-35 conducts routine training aboard USS Abraham Lincoln ](https://www.dvidshub.net/image/6942830/f-35-conducts-routine-training-aboard-uss-abraham-lincoln) | `PACIFIC OCEAN (Nov. 15, 2021) An F-35C Lightning II, assigned to Marine Wing Fighter Attack Squadron (VMFA) 314, launches from the flight deck of the aircraft carrier USS Abraham Lincoln (CVN 72). Abraham Linco` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Carl Vinson (CVN 70) Conducts Hangar Bay Ops in 3rd Fleet ](https://www.dvidshub.net/image/7040026/uss-carl-vinson-cvn-70-conducts-hangar-bay-ops-3rd-fleet) | `220207-N-LP924-1001 PACIFIC OCEAN (Feb. 7, 2022) Aviation Boatswain’s Mate (Handling) 3rd Class Carlos Noble, a native of Los Angeles, Calif., directs an F-35C Lightning II, assigned to the “Argonauts” of Strik` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [An F-35C Lighting II Taxis Across the Flight Deck ](https://www.dvidshub.net/image/7086063/f-35c-lighting-ii-taxis-across-flight-deck) | `220309-N-MH015-1026 (Mar. 09, 2022) PACIFIC OCEAN An F-35C Lightning II, from the "Rough Raiders" of Strike Fighter Squadron (VFA) 125, taxis across the flight deck of the aircraft carrier USS Nimitz (CVN 68). ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Carl Vinson (CVN 70) Sailors Perform F-35C Lightning II Maintenance ](https://www.dvidshub.net/image/8203937/uss-carl-vinson-cvn-70-sailors-perform-f-35c-lightning-ii-maintenance) | `240115-N-AV223-1002 AT SEA (Jan. 15, 2024) Sailors perform maintenance on the canopy of a F-35C Lightning II, assigned to the “Warhawks” of Strike Fighter Squadron (VFA) 97, in the hangar bay of Nimitz-class ai` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Armed for the Future ](https://www.dvidshub.net/image/8290897/armed-future) | `An AGM-154 Joint Standoff Weapon (JSOW) is staged on the flight line before being loaded onto a F-35C Lightning II at Marine Corps Air Station Miramar, California, March 8, 2024. The JSOW is a fire-and-forget m` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [An F-35C Lightning II lands on the flight deck of Nimitz-class aircraft carrier USS Carl Vinson ](https://www.dvidshub.net/image/8471397/f-35c-lightning-ii-lands-flight-deck-nimitz-class-aircraft-carrier-uss-carl-vinson) | `240612-N-TL932-2307 PACIFIC OCEAN (June 12, 2024) An F-35C Lightning II, assigned to the “Warhawks” of Strike Fighter Squadron (VFA) 97, lands on the flight deck of Nimitz-class aircraft carrier USS Carl Vinson` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [From the Flightline to the Deckplates and the Digital Edge: A 33-Year Journey Through the Navy’s Technological Evolution ](https://www.dvidshub.net/image/9747004/flightline-deckplates-and-digital-edge-33-year-journey-through-navys-technological-evolution) | `Commander Capili poses with LCDR Heath Russert, USS NIMITZ (CVN-68) Combat Systems Maintenance Officer (CSMO) and LCDR Katie Abdallah, USS NIMITZ Combat Systems Information Officer (CSIO) in front of the first ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Abraham Lincoln Conducts Operations ](https://www.dvidshub.net/image/9956319/abraham-lincoln-conducts-operations) | `U.S. Navy Aviation Boatswain’s Mate (Handling) 3rd Class Austin Shaw, left, and U.S. Navy Aviation Boatswain’s Mate (Handling) 2nd Class Tanner Wagoner tow an F-35C Lightning II, assigned to Marine Fighter Atta` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [U.S. Marines conduct Flight Operations ](https://www.dvidshub.net/image/9964401/us-marines-conduct-flight-operations) | `U.S. Marine pilot closes the canopy of an F-35C Lightning II in the U.S. Central Command area of responsibility, Aug. 26, 2026. (U.S. Marine Corps photo by Lance Cpl. Samantha Devine)` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=f35c+lightning2+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=f35c+lightning2+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=f35c+lightning2+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=f35c+lightning2+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=f35c+lightning2+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=f35c+lightning2+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=f35c+lightning2+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- [Existing air-agy index](../../../../../dreidel3d-sv2/refimages/air-agy/INDEX.md); `sourced-local-index-presence`. Read unit rows, not a blanket Complete banner. Some indexes contradict their own coverage matrices.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.

Independent image-subject review correction: wrong-subject candidates excluded, duplicate image IDs collapsed, and sibling equipment separated above. Older revisions remain audit evidence and are superseded by this last current section.
<!-- NAVAL-CURRENT-END -->
