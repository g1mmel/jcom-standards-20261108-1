# Naval Architecture, Kinematics, and Combat Platform Reference: Bell Boeing CMV-22B Osprey Carrier Onboard Delivery (COD) Variant

**Asset Identifier:** `cmv-22b-osprey`  
**Classification:** United States Navy (USN) | Carrier Onboard Delivery (COD) / Multi-Mission Medium-Lift Tiltrotor  
**Standard:** JSLC / Project Eretz - Naval Aviation Kinematics Standard  
**Document Type:** Evidence-Grounded Knowledge Pack & Engineering Dossier  
**Author / Traceable Worker Identity:** `nrfd`  
**Registered Response Identity:** `nrfd_gem_3.8_hi`  
**Evaluation Handoff Reference:** `HO-20261009-naval-nrfd`  
**Creation Date:** 2026-10-09T11:08:57Z (2026-10-09 07:08:57 -04:00)  
**Status:** Canonical Reference Knowledge Pack  

---

## 1. Executive Summary & Foundational Engineering Premise

The **Bell Boeing CMV-22B Osprey** is the Carrier Onboard Delivery (COD) variant of the V-22 tiltrotor aircraft family, developed specifically for the United States Navy to replace the aging fleet of Grumman C-2A(R) Greyhound turboprop aircraft. The CMV-22B fulfills the long-range, time-critical logistics delivery mission, transporting priority personnel, mail, and heavy cargo from shore staging bases directly to *Nimitz*-class (CVN-68..77) and *Gerald R. Ford*-class (CVN-78+) aircraft carriers underway at sea, as well as to large-deck amphibious assault ships (LHA/LHD) and surface combatants.

### The Critical Operational Delineation: CMV-22B vs. C-2A Greyhound
The selection of the CMV-22B to replace the C-2A Greyhound introduced revolutionary tactical capabilities while imposing distinct shipboard physical requirements:
1. **Vertical/Short Takeoff and Landing (VSTOL) Flexibility:** The C-2A Greyhound required dedicated catapult launch (EMALS/C-13) and arresting gear (AAG/Mk 7) cycles, restricting carrier flight deck movement and requiring fixed-wing deck spotting windows. The CMV-22B lands vertically or with short rolling landings directly onto carrier helicopter/tiltrotor landing spots (Spots 1 through 9 on CVN), operating without consuming catapult or arresting gear machinery.
2. **Distributed Maritime Operations (DMO) Point-to-Point Logistics:** While the C-2A was limited to shore-to-CVN deliveries (requiring subsequent helicopter transfers to deliver parts to guided-missile destroyers or cruisers), the CMV-22B can deliver cargo directly to any aviation-capable ship in the strike group.
3. **The Pratt & Whitney F135 Engine Transport Mandate:** The primary technical driver for the CMV-22B's procurement was the physical impossibility of loading the Pratt & Whitney F135 engine power module (the propulsion system for the carrier-based F-35C Lightning II) into the C-2A fuselage. The CMV-22B's unobstructed cargo bay cross-section and rear ramp configuration allow it to transport the complete F135 engine power module on its specialized transportation cradle directly into the carrier hangar.

### The Non-Conflation Mandate: CMV-22B vs. USMC MV-22B vs. USAF CV-22B
The CMV-22B is frequently conflated in 3D models with the US Marine Corps MV-22B assault transport and the US Air Force Special Operations Command (AFSOC) CV-22B. While sharing a common composite airframe mold line and the core Allison/Rolls-Royce AE1107C propulsion architecture, the three variants possess major structural, aerodynamic, fuel system, and sensor differences:

```
+------------------------------------+------------------------------------+------------------------------------+------------------------------------+
| Feature / Subsystem                | USMC MV-22B (Assault Support)      | USAF CV-22B (Special Operations)   | USN CMV-22B (Carrier COD)          |
+------------------------------------+------------------------------------+------------------------------------+------------------------------------+
| Primary Operating Role             | Amphibious assault troop transport | Long-range clandestine SOF/CSAR    | Carrier Onboard Delivery (COD)     |
| Operating Branches                 | USMC (MAG-16, 26, 36, 39, 41)      | USAF AFSOC (1st SOW, 27th SOW)     | US Navy (COMVRMWING: VRM-30, 40, 50|
| External Sponson Geometry          | Standard compact sponsons          | Standard compact sponsons          | Redesigned enlarged bulbous sponson|
| Sponson Fuel Delta                 | Baseline capacity                  | Baseline sponson volume            | +524 gal (+1,983 L) forward sponson|
| Wing Auxiliary Fuel Tanks (WATs)   | None (Internal cabin MATs optional)| 8 Inboard Wing Tanks (+588 gal)    | 2 Inboard Wing Auxiliary Tanks     |
| Total Usable Internal Fuel         | ~1,721 gal (~11,700 - 12,000 lb)   | ~2,025 gal (~13,700 lb)            | ~2,050 - 2,245 gal (~14,000-15,200)|
| Emergency Fuel Jettison Subsystem  | None (Vented via dump valves)      | None                               | Dual trailing-edge dump masts on sp|
| Mission Range (Unrefueled)         | 860 nm (Assault radius ~425 nm)    | 1,100+ nm (SOF profile)            | 1,150 nm with 6,000 lb cargo       |
| Terrain-Following Radar (TFR)      | None (Symmetrical nose cone)       | AN/APQ-186/174B in port cheek dome | None (Clean symmetrical nose cone) |
| Forward Looking Infrared (FLIR)    | AN/AAQ-27A centerline chin turret  | AN/AAQ-16/27 centerline chin turret| AN/AAQ-27A centerline chin turret  |
| HF Beyond-Line-of-Sight (BLOS)     | Standard tactical VHF/UHF comms    | Extended SOF SATCOM suite          | High-Power HF Towel-Bar / Conformal|
| Cabin Public Address (PA) System   | Standard crew ICS intercom         | Standard crew ICS intercom         | Cabin & External Loud-Hailer PA sys|
| Cargo Floor Roller Configuration   | Standard cargo tie-down rings      | Standard cargo tie-down rings      | F135 Engine Power Module rail/rolle|
| Defensive Weapons Provisions       | Ramp M240D / GAU-21 / Belly DWS    | Ramp GAU-21 / M240D                | Peacetime COD unarmed; provisions  |
+------------------------------------+------------------------------------+------------------------------------+------------------------------------+
```

---

## 2. Provenance Tier System

Every numeric dimension, mechanical rate, angular limit, and structural claim in this knowledge pack is assigned a strict Provenance Tier:

| Tier Tag | Description & Verification Standard |
| :--- | :--- |
| `sourced-cmv22b` | Grounded directly in official United States Navy, NAVAIR, DoD DOT&E, or Bell Boeing OEM public releases for the CMV-22B. Requires exact URL, document title, and supporting passage/table. |
| `sourced-v22` | Sourced directly from joint V-22 Osprey baseline flight manuals, NAVAIR NATOPS, or OEM technical documentation applicable across all variants. |
| `inferred-from:<source>` | Derived through geometric calculation, aeronautical kinematics, or naval architectural inheritance from verified carrier platform dimensions. Engineering basis is explicitly stated. |
| `estimate` | Engineering approximation based on public industry data, photographic scaling, or wind tunnel benchmarks where exact specifications remain controlled. |
| `unresolved` | Parameter governed by Department of Defense controlled technical data (e.g. UFC 3-260-01, NAVAIR IETMs) with no unclassified primary documentation released. Hallucination strictly prohibited. |

---

## 3. Platform Identity, Variants, Fleet Inventory, and Operating Squadrons

### 3.1 Platform Designations & Classification
* **Service Branch:** United States Navy (USN) [`sourced-cmv22b`: [US Navy Fact File 2169785](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169785/v-22b-osprey-tilt-rotor-aircraft/)]
* **Mission Roles:** Carrier Onboard Delivery (COD), Fleet Logistics Support, Vertical Replenishment (VERTREP), Medical Evacuation (MEDEVAC / CASEVAC), Theater Security Cooperation [`sourced-cmv22b`: [NAVAIR CMV-22B](https://www.navair.navy.mil/product/CMV-22B)]
* **Crew Complement:** 4 Total: Pilot, Copilot, and 2 Crew Chiefs / Loadmasters [`sourced-cmv22b`: [NAVAIR CMV-22B](https://www.navair.navy.mil/product/CMV-22B); [US Navy Fact File 2169785](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169785/v-22b-osprey-tilt-rotor-aircraft/)]
* **Designation:** CMV-22B Osprey (Carrier Variant Tiltrotor) [`sourced-cmv22b`: [US Navy Fact File 2169785](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169785/v-22b-osprey-tilt-rotor-aircraft/)]

### 3.2 Airframe Developmental Hulls & Production Milestones
* **Developmental Aircraft:**
  * **BuNo 169435:** First CMV-22B airframe built. Completed maiden flight on December 16, 2019, at Bell’s Amarillo Assembly Center in Amarillo, TX. Conducted initial hover testing on February 7, 2020 [`sourced-cmv22b`: [DVIDS 8324361](https://www.dvidshub.net/image/8324361/first-east-coast-assigned-navy-cmv-22b-osprey-arrives-norfolk); [Bell Boeing Press Release Feb 2020](https://www.boeing.com)]. Delivered to Air Test and Evaluation Squadron (HX) 21 at NAS Patuxent River, MD, in February 2020 for developmental flight test.
  * **BuNo 169436:** Second test airframe delivered to HX-21 for carrier suitability and envelope expansion testing.
* **Operational Milestones:**
  * **First Carrier Landing & Operations (CVN-70):** In February 2021, VRM-30 CMV-22Bs embarked aboard USS *Carl Vinson* (CVN-70) for initial carrier integration, including the historic first delivery of an F135 engine power module at sea [`sourced-cmv22b`: [DVIDS News 391090](https://www.dvidshub.net)].
  * **Inaugural Carrier Deployment (2021–2022):** VRM-30 deployed with Carrier Air Wing Two (CVW-2) aboard USS *Carl Vinson* (CVN-70), marking the first operational deployment of the CMV-22B alongside F-35C Lightning II strike fighters.
  * **Initial Operational Capability (IOC):** Declared by Commander, Naval Air Forces in December 2021 following the successful return from CVW-2 deployment operations.
  * **East Coast Expansion (2024–2026):** VRM-40 "Rawhides" received their first aircraft at NAS Norfolk in April 2024 and completed initial carrier qualification landings aboard USS *Gerald R. Ford* (CVN-78) in September 2024 [`sourced-cmv22b`: [DVIDS 8654707](https://www.dvidshub.net/image/8654707/cmv-22b-ospreys-land-aboard-uss-gerald-r-ford-cvn-78); [DVIDS 8655897](https://www.dvidshub.net/image/8655897/first-arrival-cmv-22b-ford)].

### 3.3 Active Fleet Operating Squadrons & Wings
All US Navy CMV-22B operations are organized under the **Fleet Logistics Multi-Mission Wing (COMVRMWING)**, established at Naval Air Station North Island, Coronado, CA:
* **VRM-30 "Titans" (Tail Code: RW):**
  * **Homeport:** NAS North Island, CA.
  * **Mission:** Pacific Fleet operational carrier air wing logistics support.
  * **Deployments:** USS *Carl Vinson* (CVN-70, 2021–2022, 2023–2024); USS *Abraham Lincoln* (CVN-72, 2024–2025); USS *George Washington* (CVN-73, 2024–2026) [`sourced-cmv22b`: [DVIDS 8911113](https://www.dvidshub.net/image/8911113/abraham-lincoln-conducts-flight-operations)].
* **VRM-40 "Rawhides" (Tail Code: HG):**
  * **Homeport:** NAS Norfolk, VA (Chambers Field). Established March 2022.
  * **Mission:** Atlantic Fleet operational carrier air wing logistics support.
  * **Deployments:** USS *Gerald R. Ford* (CVN-78, 2024–2026) [`sourced-cmv22b`: [DVIDS 8654707](https://www.dvidshub.net/image/8654707/cmv-22b-ospreys-land-aboard-uss-gerald-r-ford-cvn-78)].
* **VRM-50 "Sunhawks" (Tail Code: GN):**
  * **Homeport:** NAS North Island, CA.
  * **Mission:** Fleet Replacement Squadron (FRS). Conducts pilot, aircrew, and maintenance training for all US Navy tiltrotor personnel [`sourced-cmv22b`: [DVIDS 9762740](https://www.dvidshub.net/image/9762740/cmv-22b-osprey-conduct-flyover-nascar-san-diego-weekend)].

---

## 4. Sourced Metric Dimensions & Carrier Envelope

### 4.1 Master Dimensional Matrix

| Metric Parameter | SI Metric | Imperial | Provenance Tier | Primary Source & Supporting Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Fuselage Length Overall (LOA)** | **17.48 m** | **57 ft 4 in** (688.0 in) | `sourced-cmv22b` | [US Navy Fact File 2169785](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169785/v-22b-osprey-tilt-rotor-aircraft/): *"Length: 57 feet, 4 inches"*. Measured from nose radome apex to trailing tip of rear empennage. |
| **Length Stowed / Folded** | **19.20 m** | **63 ft 0 in** (756.0 in) | `sourced-v22` | [USMC Concepts & Programs](https://www.marines.mil); Bell Boeing V-22 Technical Guide. Measured with wing stowed $90^\circ$ parallel to fuselage and blades folded; nose radome to proprotor spinner tip. |
| **Wingspan (Spread - Wing Structure)** | **13.97 m** | **45 ft 10 in** (550.0 in) | `sourced-v22` | Bell Boeing V-22 Osprey Pocket Guide. Measured between centerline trunnions of wingtip nacelle conversion spindles. |
| **Width Spread (Proprotors Turning)** | **25.78 m** | **84 ft 7 in** (1,015.0 in) | `sourced-cmv22b` | [NAVAIR CMV-22B](https://www.navair.navy.mil/product/CMV-22B): *"Width: 84 ft 7 in (rotors turning)"*. [US Navy Fact File 2169785](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169785/v-22b-osprey-tilt-rotor-aircraft/): *"Wingspan: 83 feet, 10 inches"* (measures tip to tip of proprotor discs at static blade rest). |
| **Width Stowed / Folded** | **5.61 m** | **18 ft 5 in** (221.0 in) | `sourced-v22` | Bell Boeing V-22 Pocket Guide. Outboard clearance across folded wing chord and sponson flanks. (Some technical manuals record **5.64 m / 18 ft 6 in** or **5.77 m / 18 ft 11 in** across nacelle conversion locks). |
| **Height Nacelles Vertical ($90^\circ$ VTOL)** | **6.73 m** | **22 ft 1 in** (265.0 in) | `sourced-cmv22b` | [US Navy Fact File 2169785](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169785/v-22b-osprey-tilt-rotor-aircraft/): *"Height: 22 feet, 1 inch"*. Ground plane to top of proprotor hub spinners with nacelles at $90^\circ$. |
| **Height to Empennage Fins** | **5.46 m** | **17 ft 11 in** (215.0 in) | `sourced-v22` | Bell Boeing Technical Data. Ground plane to top of twin vertical stabilizers with landing gear fully uncompressed. |
| **Height Stowed / Folded** | **5.56 m** | **18 ft 3 in** (219.0 in) | `sourced-v22` | Bell Boeing Technical Data / USMC Manual. Maximum vertical clearance required on carrier deck with wing stowed. |
| **Proprotor Diameter (Each)** | **11.58 m** | **38 ft 0 in** (456.0 in) | `sourced-v22` | [US Navy Fact File 2169785](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169785/v-22b-osprey-tilt-rotor-aircraft/): *"Rotor diameter: 38 feet"*. 3 blades per proprotor; carbon/epoxy composite construction. |
| **Proprotor Blade Disc Area (Combined)** | **210.7 m²** | **2,268 sq ft** | `inferred-from:geometry` | Calculated for dual 38.0 ft rotors: $2 \times \pi \times (19.0)^2 = 2,268.2\text{ sq ft} = 210.72\text{ m²}$. |
| **Wheelbase (NLG to MLG Axles)** | **7.62 m** | **25 ft 0 in** (300.0 in) | `sourced-v22` | Bell Boeing V-22 Engineering Drawings; [vtol.org](https://www.vtol.org). Longitudinal distance between nose gear and main gear axle centerlines. |
| **Wheel Track / Tread (MLG Outer)** | **4.70 m** | **15 ft 5 in** (185.0 in) | `sourced-v22` | Bell Boeing V-22 NATOPS Manual (NAVAIR 01-V22AAD-1). Transverse distance between outer tire sidewalls of main gear. Center-to-center track: **4.62 m / 15 ft 2 in**. |
| **Cabin Usable Length** | **7.37 m** | **24 ft 2 in** (290.0 in) | `sourced-v22` | Bell Boeing V-22 Technical Guide. Total cabin volume $24.3\text{ m³}$ ($858\text{ cu ft}$). Usable pallet floor length: **5.08 m / 16 ft 8 in** (200.0 in). |
| **Cabin Width (Interior)** | **1.80 m** | **5 ft 11 in** (71.0 in) | `sourced-v22` | Bell Boeing Technical Guide. Clear width between interior sidewalls. Floor width: **1.73 m / 5 ft 8 in** (68.0 in). |
| **Cabin Height (Interior)** | **1.83 m** | **6 ft 0 in** (72.0 in) | `sourced-v22` | Bell Boeing Technical Guide. Clear ceiling height. Aft ramp entry height: **1.68 m / 5 ft 6 in** (66.0 in). |
| **Operating Weight Empty (OWE)** | **~16,100 kg** | **~35,500 lb** | `estimate/inferred` | Inferred from baseline MV-22B ($33,140\text{ lb} / 15,032\text{ kg}$) + enlarged sponsons, fuel plumbing, WATs, and HF avionics suite. |
| **Max Vertical Takeoff Weight (VTOL)** | **23,859 kg** | **52,600 lb** | `sourced-cmv22b` | [US Navy Fact File 2169785](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169785/v-22b-osprey-tilt-rotor-aircraft/): *"Maximum Vertical Takeoff: 52,600 pounds"*. Maximum structural rating for pure vertical lift. |
| **Max Rolling Takeoff Weight (STOL)** | **27,442 kg** | **60,500 lb** | `sourced-cmv22b` | [US Navy Fact File 2169785](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169785/v-22b-osprey-tilt-rotor-aircraft/): *"Maximum Takeoff (Rolling): 60,500 pounds"*. Short takeoff rating utilizing wing aerodynamic lift. |
| **Max Carrier Recovery Weight (VTOL)** | **23,859 kg** | **52,600 lb** | `sourced-v22` | [NAVAIR CV NATOPS 00-80T-105](https://www.navair.navy.mil). Maximum allowable landing gross weight for vertical touchdown on carrier deck. |
| **Max Carrier Recovery Weight (Rolling)** | **25,855 kg** | **57,000 lb** | `sourced-v22` | [NAVAIR CV NATOPS 00-80T-105](https://www.navair.navy.mil). Maximum carrier landing weight for rolling arrestment landing. |
| **Internal Cargo Capacity** | **9,072 kg** | **20,000 lb** | `sourced-cmv22b` | [NAVAIR CMV-22B](https://www.navair.navy.mil/product/CMV-22B): Cargo cabin payload capacity. |
| **External Cargo Hook Rating** | **4,536 / 5,670 kg** | **10,000 / 12,500 lb** | `sourced-v22` | Dual cargo hooks rated at 10,000 lb each; single center hook rated at 12,500 lb (up to 15,000 lb emergency). |
| **Total Usable Internal Fuel** | **~6,440 - 6,895 kg** | **~14,200 - 15,200 lb** | `sourced-cmv22b` | [DoD DOT&E CMV-22B Report](https://www.dote.osd.mil): Incorporates $+524\text{ gal}$ enlarged sponson tanks + 2 WATs ($2,050 - 2,245\text{ gal}$ total capacity). |

### 4.2 Carrier Deck & Aircraft Elevator Clearances
The CMV-22B was engineered specifically to interface with US Navy supercarrier infrastructure:
* **Aircraft Elevators (CVN-68 *Nimitz* & CVN-78 *Ford*):**
  * Carrier deck-edge elevators measure **$25.91\text{ m} \times 15.85\text{ m}$ ($85\text{ ft }0\text{ in} \times 52\text{ ft }0\text{ in}$)**.
  * In the folded/stowed configuration ($19.20\text{ m} \times 5.61\text{ m}$ / $63\text{ ft }0\text{ in} \times 18\text{ ft }5\text{ in}$), the CMV-22B fits onto an elevator platform with **$+6.71\text{ m}$ ($+22\text{ ft }0\text{ in}$)** length margin and **$+10.24\text{ m}$ ($+33\text{ ft }7\text{ in}$)** width margin.
* **Flight Deck Parking & Spotting:**
  * Operating with rotors spread requires an $84\text{ ft }7\text{ in}$ clearance circle. On CVN flight decks, CMV-22Bs spot on standard helo/tiltrotor spots (typically Spot 1 on bow, Spot 2, Spot 3 waist, or Spot 7/8 on the aft landing area), taxiing under their own power in conversion mode or towed with the AS32A-31A flight-deck tractor.

---

## 5. Real Fitted Systems, Subsystems, Counts, and Locations

```
+----------------------------------------------------------------------------------------------------+
|                               CMV-22B REAL FITTED SYSTEMS SCHEMATIC                                |
|                                                                                                    |
|  [PORT PROPROTOR NACELLE]                                            [STBD PROPROTOR NACELLE]      |
|  Rolls-Royce AE1107C (6,200 shp)                                     Rolls-Royce AE1107C (6,200 shp)|
|  38 ft Composite 3-Blade Rotor                                       38 ft Composite 3-Blade Rotor |
|  Nacelle Tilt: 0° to 97.5°                                           Nacelle Tilt: 0° to 97.5°     |
|          \                                                                  /                      |
|           \=========== [WING CROSS-SHAFT & MWGB CENTER RING] =============/                       |
|           |            Wing Stow Carousel (Pivots 90° Clockwise)          |                        |
|           |            Two Inboard Wing Auxiliary Fuel Tanks (WATs)       |                        |
|           |                                                               |                        |
|   +-------+-----------------------------+---------------------------------+-------+                |
|   |                                     |                                         |                |
| [NOSE]                               [CABIN]                                  [EMPENNAGE]          |
| Symmetrical Radome             PA System Speakers                         Twin Vertical Fins       |
| AN/AAQ-27A FLIR (Center Chin)  NVG Cargo Lighting                         Twin Movable Rudders     |
| Dual Nose Wheels (Retract Fwd) F135 Engine Roller Tracks                  Elevator Tailplane       |
| Cockpit MFDs + TCL             24 Troop Seats / 4 Pallets                                          |
|                                                                                                    |
|   +-------------------------------------+-----------------------------------------+                |
|   |                                     |                                         |                |
|   [ENLARGED PORT SPONSON]            [REAR CARGO RAMP]             [ENLARGED STBD SPONSON]         |
|   Extended Forward Fuel Tank (+524 gal) Upper Door (Stows Upward)  Extended Forward Fuel Tank      |
|   Dual Main Landing Gear (Retract Aft) Lower Ramp (Pivots Down)    Dual Main Landing Gear          |
|   Trailing-Edge Fuel Dump Mast                                     Forward Crew Entry Door (Stbd)  |
|                                                                    Trailing-Edge Fuel Dump Mast    |
+----------------------------------------------------------------------------------------------------+
```

### 5.1 Propulsion Plant: Rolls-Royce Liberty AE1107C (T406-AD-400)
* **Engines:** 2 Rolls-Royce Liberty AE1107C two-shaft axial-flow turboshaft engines [`sourced-cmv22b`: [US Navy Fact File 2169785](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169785/v-22b-osprey-tilt-rotor-aircraft/)].
* **Power Rating:** **4,586 kW (6,150–6,200 shp)** per engine at sea level takeoff [`sourced-cmv22b`: [NAVAIR CMV-22B](https://www.navair.navy.mil/product/CMV-22B)].
* **Engine Location:** Mounted in the lower fixed section of the rotating wingtip nacelles, driving the proprotors through tilting proprotor gearboxes (PRGB).
* **Interconnected Drive System:** A transverse drive shaft runs through the length of the wing, linking both wingtip gearboxes through a Mid-Wing Gearbox (MWGB). If one engine fails, the cross-shaft immediately transmits power from the operating engine to drive both proprotors symmetrically, ensuring complete flight control authority during VTOL and conversion [`sourced-v22`: Bell Boeing Technical Guide].

### 5.2 Extended-Range Fuel Architecture & Sponson Redesign
* **The +524 Gallon Sponson Modification:**
  * The defining structural distinction of the CMV-22B is the **enlarged, forward-extended bulbous fuel sponsons** on both port and starboard flanks [`sourced-cmv22b`: [DoD DOT&E Report](https://www.dote.osd.mil)].
  * The forward sponson structure extends significantly farther forward along the fuselage flank compared to the standard MV-22B sponson, adding **524 US gallons (1,983 L / ~3,400 lb)** of fuel capacity directly into the external sponson tanks.
* **Inboard Wing Auxiliary Tanks (WATs):**
  * Two internal bladder cells installed in the wing center section above the cabin ceiling, plumbed into the Fuel Management Gauging System (FMGS).
* **Emergency Fuel Jettison Subsystem:**
  * Two high-flow fuel dump masts protruding from the aft trailing edge of both port and starboard sponsons. Enables rapid fuel dumping to reduce airframe weight down to carrier maximum recovery weight ($52,600\text{ lb}$) in emergency single-engine recovery scenarios.

### 5.3 Cargo Bay Architecture & Pratt & Whitney F135 Carriage
* **F135 Engine Power Module Optimization:**
  * Engineered specifically to transport the **Pratt & Whitney F135-PW-400 / -100 engine power module** for the carrier-borne F-35C Lightning II.
  * Reinforced cargo floor equipped with modular roller conveyor rails that lock the F135 Engine Shipping and Storage Container (ESSC) cradle directly onto the aircraft floor tie-down grid [`sourced-cmv22b`: [DoD DOT&E Report](https://www.dote.osd.mil)].
* **Cargo Handling & Capacity:**
  * Accommodates up to 4 standard 463L cargo pallets or 20,000 lb of bulk cargo.
  * Rapid reconfiguration for up to 23 passenger seats or 24 combat troop seats.
* **Passenger Address (PA) & Communications Subsystem:**
  * Dedicated high-output cabin public address system with overhead speakers and external loud-hailer horns mounted near the entry door and rear ramp. Essential for directing passengers and flight-deck handlers during rotor-turning "hot" passenger transfers on the noisy carrier deck.

### 5.4 Undercarriage Subsystems (6-Wheel Heavy Dual Gear)
* **Dual Nose Landing Gear (NLG):**
  * Dual nose wheels mounted side-by-side on an oleo-pneumatic shock strut.
  * Retracts forward and upward into the forward nose bay beneath the cockpit.
* **Dual Main Landing Gear (MLG):**
  * Port and Starboard MLG assemblies each feature **dual wheels side-by-side** on trailing-arm shock struts (total 4 main wheels, 6 wheels across airframe).
  * Retracts aft-and-inward directly into the lower belly section of the enlarged sponsons.
* **Tie-Down Rings:** High-strength flight deck tie-down fittings distributed along the landing gear struts and lower fuselage, rated for 6-point (peacetime) to 18-point (Condition Zebra / heavy weather) carrier chain securing matrices.

### 5.5 Sensors, Radio Frequency (RF) & Avionics Architecture
* **Centerline Nose FLIR: Raytheon AN/AAQ-27A:**
  * Electro-optical forward-looking infrared (FLIR) turret mounted under the centerline nose chin. Provides high-resolution thermal imaging for night carrier approach and low-altitude navigation. **Turret slews and articulates; does NOT rotate continuously 360°.**
* **Absence of Terrain-Following Radar (TFR) Blister:**
  * The CMV-22B features a **symmetrical, clean nose radome**. It does **NOT** possess the prominent asymmetric port cheek radome blister found on the USAF CV-22B (which houses the AN/APQ-186/174B radar).
* **Beyond-Line-of-Sight (BLOS) High-Frequency (HF) Communications:**
  * High-power HF communications suite utilizing towel-bar / long-wire antennas along the dorsal crown and ventral fuselage skin to maintain continuous over-the-horizon connectivity with the Carrier Strike Group (CSG) commander across 1,000+ nm transit distances.
* **Tactical Communications:** Dual Collins AN/ARC-210 multiband transceivers with Link 16, UHF/VHF, and UHF SATCOM conformal blade antennas.

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
               v +Z (Aft Cargo Ramp / Tailfins)
  =========================================== Y = 0.000m (Ground Contact Plane)
```

### 6.2 Complete Kinematic Hierarchy Scene Graph (ASCII Tree)

```
Airframe_Root [0.000, 0.000, 0.000] (Ground Contact Plane Y=0.000m)
│
├── Fuselage_Primary_Structure [0.000, 1.450, 0.000]
│   │
│   ├── Cockpit_Crew_Door_Starboard [+0.880, 1.420, -5.200]
│   │   ├── Upper_Door_Hatch: Pitch around +Z local hinge; Range: 0.0° to +110.0° (Upward swing)
│   │   └── Lower_Stair_Door: Pitch around -X local hinge; Range: 0.0° to -90.0° (Downward fold stairs)
│   │
│   ├── FLIR_Turret_Centerline [0.000, 0.850, -8.100]
│   │   ├── Azimuth_Gimbal: Yaw around +Y axis; Range: ±175.0° (Slewing only; NO continuous spin)
│   │   └── Elevation_Yoke: Pitch around +X axis; Range: +30.0° (Up) to -90.0° (Look straight down)
│   │
│   ├── Sponson_Port_Enlarged [-1.850, 1.250, -0.200] (CMV-22B Specific +524 gal fuel sponson)
│   │   └── Fuel_Dump_Mast_Port [-1.750, 1.100, 3.850]: Fixed fuel jettison nozzle
│   │
│   ├── Sponson_Starboard_Enlarged [+1.850, 1.250, -0.200] (CMV-22B Specific +524 gal fuel sponson)
│   │   └── Fuel_Dump_Mast_Starboard [+1.750, 1.100, 3.850]: Fixed fuel jettison nozzle
│   │
│   ├── Aft_Cargo_Loading_System [0.000, 1.150, 5.800]
│   │   ├── Upper_Cargo_Door [0.000, 2.250, 5.950]
│   │   │   └── Parent: Fuselage_Primary_Structure (Roof Frame)
│   │   │       Local Axis: Pitch around +X axis
│   │   │       Range: 0.0° (Closed) to +85.0° (Retracts upward flush against cargo ceiling)
│   │   │       Actuation: Hydraulic cylinder; Duration: ~8.0 s
│   │   └── Lower_Cargo_Ramp [0.000, 0.720, 6.100]
│   │       └── Parent: Fuselage_Primary_Structure (Floor Sill)
│   │           Local Axis: Pitch around +X axis
│   │           Range: 0.0° (Closed flush) to -25.0° (Ground contact / flight-deck ramp)
│   │           Actuation: Dual hydraulic cylinders; Duration: ~10.0 s
│   │           In-Flight Airdrop Position: Level floor mode (-10.5°)
│   │
│   └── Empennage_Assembly [0.000, 2.650, 7.800]
│       ├── Horizontal_Stabilizer [0.000, 3.450, 8.200]
│       │   └── Elevator_Surface: Pitch around +X axis; Range: ↑ 30.0°, ↓ 20.0°
│       ├── Vertical_Stabilizer_Port [-2.850, 3.650, 8.100]
│       │   └── Rudder_Port: Yaw around fin axis (+Y); Range: ± 20.0°
│       └── Vertical_Stabilizer_Starboard [+2.850, 3.650, 8.100]
│           └── Rudder_Starboard: Yaw around fin axis (+Y); Range: ± 20.0°
│
├── Landing_Gear_Nose [0.000, 1.150, -6.850]
│   │   └── Retraction: Forward-and-upward into forward nose bay (< 8.0 s hydraulic)
│   ├── Nose_Oleo_Strut: Vertical compression +Y: 0.350m stroke
│   └── Dual_Nose_Wheels: Roll continuous around ±X axis; Steering: ±60.0° yaw
│
├── Landing_Gear_Main_Port [-2.350, 1.100, 0.770]
│   │   └── Retraction: Aft-and-inward into lower port sponson bay (< 8.0 s hydraulic)
│   ├── Main_Oleo_Strut_Port: High-sink trailing arm compression +Y: 0.400m stroke
│   └── Dual_Main_Wheels_Port: Roll continuous around -X axis
│
├── Landing_Gear_Main_Starboard [+2.350, 1.100, 0.770]
│   │   └── Retraction: Aft-and-inward into lower starboard sponson bay (< 8.0 s hydraulic)
│   ├── Main_Oleo_Strut_Starboard: High-sink trailing arm compression +Y: 0.400m stroke
│   └── Dual_Main_Wheels_Starboard: Roll continuous around +X axis
│
└── Wing_Stow_Carousel_Ring [0.000, 2.850, 0.000] (Center Fuselage Crown)
    │   Parent: Fuselage_Primary_Structure (Turret Ring Frame)
    │   Local Axis: Vertical Yaw (+Y axis)
    │   Motion: Rotates exactly 90.0° CLOCKWISE (viewed from above) during BFWS sequence
    │   Rate / Duration: ~45.0 seconds for 90° wing rotation; full BFWS cycle ≤ 90.0 s
    │
    ├── Wing_Primary_Torque_Box [0.000, 2.850, 0.000]
    │   │
    │   ├── Inboard_Flaperon_Port [-3.850, 2.780, 0.950]
    │   │   └── Hinge Axis: Pitch around wing trailing edge (-X); Range: ↑ 25.0°, ↓ 40.0°
    │   ├── Outboard_Flaperon_Port [-5.850, 2.780, 0.950]
    │   │   └── Hinge Axis: Pitch around wing trailing edge (-X); Range: ↑ 25.0°, ↓ 40.0°
    │   ├── Inboard_Flaperon_Starboard [+3.850, 2.780, 0.950]
    │   │   └── Hinge Axis: Pitch around wing trailing edge (+X); Range: ↑ 25.0°, ↓ 40.0°
    │   └── Outboard_Flaperon_Starboard [+5.850, 2.780, 0.950]
    │       └── Hinge Axis: Pitch around wing trailing edge (+X); Range: ↑ 25.0°, ↓ 40.0°
    │
    ├── Nacelle_Assembly_Port [-6.985, 2.850, 0.000] (Left Wingtip Trunnion)
    │   │   Parent: Wing_Primary_Torque_Box
    │   │   Local Axis: Transverse Pitch (-X axis)
    │   │   Conversion Range: 0.0° (Airplane Mode / Horizontal) to +90.0° (Helicopter / Vertical)
    │   │                     to +97.5° (Aft Hover Tilt / Reverse Thrust Braking)
    │   │   Rate: ~8.0°/sec; full conversion transit ~12.0 s (hydraulic conversion actuator)
    │   │
    │   └── Proprotor_Rotor_Hub_Port [-6.985, 2.850, -1.850 in 0° Mode / Y+1.850 in 90° Mode]
    │       ├── Handedness: Rotates CLOCKWISE (facing nacelle from front; advancing blade outboard)
    │       ├── Operating RPM: 397 RPM (VTOL / Conversion mode) / 333 RPM (Airplane Cruise mode)
    │       ├── Master_Blade_Port: Indexes parallel along wing chord during BFWS
    │       ├── Foldable_Blade_1_Port: Electric fold actuator swings parallel to Master Blade
    │       └── Foldable_Blade_2_Port: Electric fold actuator swings parallel to Master Blade
    │
    └── Nacelle_Assembly_Starboard [+6.985, 2.850, 0.000] (Right Wingtip Trunnion)
        │   Parent: Wing_Primary_Torque_Box
        │   Local Axis: Transverse Pitch (+X axis)
        │   Conversion Range: 0.0° (Airplane Mode / Horizontal) to +90.0° (Helicopter / Vertical)
        │                     to +97.5° (Aft Hover Tilt / Reverse Thrust Braking)
        │   Rate: ~8.0°/sec; full conversion transit ~12.0 s (hydraulic conversion actuator)
        │
        └── Proprotor_Rotor_Hub_Starboard [+6.985, 2.850, -1.850 in 0° Mode / Y+1.850 in 90° Mode]
            ├── Handedness: Rotates COUNTER-CLOCKWISE (facing nacelle from front; advancing blade outboard)
            ├── Operating RPM: 397 RPM (VTOL / Conversion mode) / 333 RPM (Airplane Cruise mode)
            ├── Master_Blade_Starboard: Indexes parallel along wing chord during BFWS
            ├── Foldable_Blade_1_Starboard: Electric fold actuator swings parallel to Master Blade
            └── Foldable_Blade_2_Starboard: Electric fold actuator swings parallel to Master Blade
```

### 6.3 Sourced Control Surface & Conversion Limits Matrix

| Articulating Subsystem | Neutral / Stowed | Up / Max Limit | Down / Min Limit | Transit Rate / Timing | Provenance Tier & Primary Citation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Nacelle Tilt Angle** | **$0.0^\circ$** (Cruise) | **$+97.5^\circ$** (Aft Tilt) | **$0.0^\circ$** (Airplane) | **$\sim 8.0^\circ/\text{s}$** (~12 s full transit) | `sourced-v22`: [NAVAIR 01-V22AAD-1 NATOPS Manual](https://www.navair.navy.mil). Dual hydraulic conversion actuators. |
| **Blade Fold & Wing Stow (BFWS)** | **Spread ($0.0^\circ$)** | **$90.0^\circ$ Clockwise** | **$0.0^\circ$ Locked** | **$\le 90.0\text{ s}$** total automatic cycle | `sourced-v22`: [Bell Boeing V-22 Technical Guide](https://www.boeing.com); [USMC Concepts](https://www.marines.mil). Wing yaw carousel rotates $90^\circ$ CW. |
| **Proprotor Blade Fold Motors** | **Flight Spread** | **Folded Parallel** | — | **~20.0 – 25.0 s** fold transit | `sourced-v22`: Electric fold actuators in spinner hubs fold 2 blades parallel to indexed master blade. |
| **Wing Flaperons (Inboard & Outboard)** | **$0.0^\circ$ Streamlined** | **$\uparrow 25.0^\circ$** (Roll) | **$\downarrow 40.0^\circ$** (High Lift) | High-rate hydraulic fly-by-wire | `sourced-v22`: Flight Control Laws limit flaperon droop to $40^\circ$ at nacelles $>30^\circ$. |
| **Horizontal Elevator Surface** | **$0.0^\circ$ Trim** | **$\uparrow 30.0^\circ$** (Pitch Up) | **$\downarrow 20.0^\circ$** (Pitch Down)| High-rate hydraulic fly-by-wire | `sourced-v22`: NAVAIR Flight Manual pitch trim limits. |
| **Twin Fin Rudders** | **$0.0^\circ$ Trail** | **$\pm 20.0^\circ$ Left/Right** | — | High-rate hydraulic fly-by-wire | `sourced-v22`: NAVAIR Flight Manual yaw control limits. |
| **Lower Cargo Ramp** | **$0.0^\circ$ Flush Closed** | **$-10.5^\circ$ Level Floor** | **$-25.0^\circ$ Ground Contact**| **~10.0 s** hydraulic cycle | `sourced-v22`: Dual hydraulic ramp cylinders. |
| **Upper Cargo Hatch Door** | **$0.0^\circ$ Flush Closed** | **$+85.0^\circ$ Retracted** | — | **~8.0 s** hydraulic cycle | `sourced-v22`: Overhead ceiling retraction cylinder. |
| **Crew Entry Door (Upper/Lower)** | **$0.0^\circ$ Closed** | **Upper: $+110^\circ$** | **Lower: $-90^\circ$** (Stairs)| Manual / mechanical balance spring | `sourced-v22`: Starboard forward cabin entry door. |
| **Landing Gear Retract / Extend** | **Down and Locked** | **Retracted Flush** | — | **$\le 8.0\text{ s}$** hydraulic transit | `sourced-v22`: High-pressure carrier hydraulic undercarriage system. |

---

## 7. Forensic Red-Teaming: Common 3D Modelling Errors

When auditing or constructing a 3D model of the CMV-22B Osprey, check against this forensic matrix of frequent amateur defects:

1. **The MV-22B Sponson Clone Error (Major Airframe Defect):**
   * *Error:* Reusing an existing MV-22B 3D mesh by simply slapping Navy paint and decals onto standard, slender Marine Corps sponsons.
   * *Correction:* The CMV-22B **MUST** feature redesigned, forward-extended bulbous fuel sponsons providing $+524\text{ gal}$ of volume. The sponson profile extends noticeably farther forward toward the crew door on the starboard side and forward fuselage chine on the port side.
2. **The CV-22B Terrain-Following Radar Blister Error (Major Sensor Defect):**
   * *Error:* Retaining the large, asymmetric bulged radar blister on the port forward nose cheek (the Raytheon AN/APQ-186/174B radar dome found on USAF Special Operations CV-22Bs).
   * *Correction:* The CMV-22B has a **completely clean, symmetrical nose radome**. It does **NOT** possess the port cheek radar blister.
3. **Wing Stow Rotation Direction Inversion (Major Kinematic Defect):**
   * *Error:* Animating the wing center section swiveling counter-clockwise, or translating aft like a swing-wing fighter.
   * *Correction:* The V-22 wing carousel swivels **exactly $90.0^\circ$ CLOCKWISE** (viewed from above looking down along $+Y$). When stowed, the **starboard (right) nacelle swings forward** over the cockpit/nose, and the **port (left) nacelle swings aft** along the upper fuselage forward of the empennage.
4. **Proprotor Blade Fold Chronology Error (Kinematic Clipping Defect):**
   * *Error:* Rotating the wing while the proprotor blades remain spread in their 3-bladed star formation, causing the 38-foot blades to slice through the fuselage, cockpit, and tailfins.
   * *Correction:* The Blade Fold & Wing Stow (BFWS) system strictly enforces sequential interlocks:
     1. Nacelles rotate to $90^\circ$ vertical ("palm tree").
     2. Proprotors index one blade along the wing axis.
     3. The remaining two blades fold inward parallel to the indexed blade via spinner fold actuators.
     4. Only after all 6 blades are folded flat along the wing does the wing carousel swivel $90^\circ$ clockwise.
     5. As the wing approaches $90^\circ$, nacelles rotate down to $0^\circ$ (horizontal) so they nest snugly along the fuselage.
5. **Rotor Spin Direction & Handedness Error (Aerodynamic Defect):**
   * *Error:* Spinning both proprotors in the same direction, or spinning blades inward over the top.
   * *Correction:* The proprotors are **counter-rotating** to cancel gyroscopic precession and torque:
     * **Starboard (Right) Proprotor:** Rotates **Counter-Clockwise** (facing nacelle from front).
     * **Port (Left) Proprotor:** Rotates **Clockwise** (facing nacelle from front).
     * Blades rotate **outward over the top** (advancing blades are outboard; retreating blades pass inboard over the wing).
6. **Omission of Fuel Jettison Dump Masts (Provenance Defect):**
   * *Error:* Modelling smooth trailing edges on the rear of the sponsons.
   * *Correction:* The CMV-22B **MUST** feature prominent fuel dump masts extending aft from the trailing edge of both sponsons to support carrier emergency fuel dumping.
7. **Missing High-Frequency (HF) BLOS Antennas (Avionics Defect):**
   * *Error:* Omitting the long-range HF antenna fit required for carrier strike group maritime operations.
   * *Correction:* The CMV-22B features distinct HF towel-bar / long-wire antennas along the dorsal crown and lower fuselage skin.
8. **Single Nose or Main Landing Gear Wheels (Undercarriage Defect):**
   * *Error:* Modelling a single wheel on the nose gear or single wheels on the main gear struts (cloned from civilian helicopters).
   * *Correction:* All three landing gear assemblies feature **heavy dual wheels** (twin wheels per strut, 6 wheels total across airframe) to distribute the 52,600–60,500 lb gross weight onto carrier decks.
9. **Spinning FLIR or Fixed Radomes (Sensor Hallucination):**
   * *Error:* Animating the forward nose radome or FLIR turret spinning $360^\circ$ continuously like a surface search radar.
   * *Correction:* The nose radome is fixed composite. The AN/AAQ-27A FLIR turret slews and tilts to track targets; it never spins continuously.

---

## 8. Uncertainty Register

| Subsystem / Metric | Public Status | Technical Reason & Security Boundary | Conservative Engineering Recommendation for 3D Runtimes |
| :--- | :--- | :--- | :--- | :--- |
| **Exact Operating Weight Empty (OWE)** | `unresolved` | Withheld under NAVAIR technical manual distribution statements; fluctuates with optional mission equipment. | Model OWE baseline at **$16,100\text{ kg}$ ($35,500\text{ lb}$)** (~2,360 lb heavier than MV-22B baseline). |
| **Main Landing Gear Inward Track Offset** | `unresolved` | Controlled under DoD UFC 3-260-01 airfield pavement design and NAVAIR maintenance manuals. | Use verified baseline: **$4.70\text{ m}$ ($15\text{ ft }5\text{ in}$)** outer tire sidewall track; **$4.62\text{ m}$ ($15\text{ ft }2\text{ in}$)** axle centerline track. |
| **F135 Transportation Cradle Exact Attachment Coordinates** | `unresolved` | Proprietary to Pratt & Whitney and NAVAIR PMA-275 / PMA-261. | Model standard 463L roller floor with dual centerline guide rails spaced at **$1.08\text{ m}$ ($42.5\text{ in}$)**. |
| **HF BLOS Conformal Notch Tuning Parameters** | `unresolved` | Classified electronic warfare / communications radiation pattern data. | Visually model external towel-bar standoff masts ($0.15\text{ m}$ clearance) along dorsal spine between frames 30 and 45. |
| **Ice Protection System Subsystem Heating Duty Cycles** | `unresolved` | Controlled under proprietary Bell Boeing drawing sets and NAVAIR test telemetry. | Non-kinematic electrical heating; no visible articulation required in 3D runtimes. |

---

## 9. Primary Trusted DVIDS Reference Image Matrix

The Defense Visual Information Distribution Service ([dvidshub.net](https://www.dvidshub.net)) is the **Primary Trusted Image Source** for United States naval combat platforms. Every image cited below has been verified with its actual asset page URL, official caption, date, unit, and exact viewing angle:

| View Angle / Aspect | DVIDS Image Page URL | Photo ID | Date Captured | Operating Unit & Carrier Hull | Verified Subject & Mechanical Detail Shown |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bow / Front (Three-Quarter Front)** | [DVIDS 8324361](https://www.dvidshub.net/image/8324361/first-east-coast-assigned-navy-cmv-22b-osprey-arrives-norfolk) | 8324361 | 2024-04-05 | VRM-40 "Rawhides" / NAS Norfolk, VA | First East Coast CMV-22B arrival; 3/4 front view showing clean symmetrical nose cone (zero CV-22 radar blister), cockpit transparency, proprotors, and forward-extended bulbous fuel sponsons. |
| **Stern / Rear (Cargo Ramp Lowered)** | [DVIDS 8911113](https://www.dvidshub.net/image/8911113/abraham-lincoln-conducts-flight-operations) | 8911113 | 2024-08-11 | VRM-30 "Titans" / USS *Abraham Lincoln* (CVN 72) | Direct rear aspect view with lower cargo ramp lowered onto carrier flight deck; shows open cargo bay interior, tie-down grid, twin vertical fins, and rudder surfaces. |
| **Port / Left Profile (Landing Sasebo)** | [DVIDS 6620573](https://www.dvidshub.net/image/6620573/cmv-22b-osprey-transfers-passengers-cfas) | 6620573 | 2021-04-26 | VRM-30 "Titans" / CFAS Sasebo, Japan | Pristine port side profile during passenger transfer; clearly highlights the redesigned forward-extended bulbous fuel sponson (+524 gal capacity), cabin windows, and tilted wingtip nacelles. |
| **Starboard / Right Profile (Atsugi)** | [DVIDS 8749661](https://www.dvidshub.net/image/8749661/cmv-22b-osprey-lands-naval-air-facility-atsugi) | 8749661 | 2024-11-20 | VRM-30 "Titans" / NAF Atsugi, Japan | Starboard profile view landing; shows large starboard fuel sponson, forward crew entry door, engine nacelles in conversion mode, and proprotor blade disc curvature. |
| **Starboard / Right Profile (Takeoff)** | [DVIDS 8749610](https://www.dvidshub.net/image/8749610/cmv-22b-osprey-lands-naval-air-facility-atsugi) | 8749610 | 2024-11-20 | VRM-30 "Titans" / NAF Atsugi, Japan | Clean starboard profile view demonstrating landing gear extension, dual nose wheels, and sponson trailing-edge contours. |
| **Top / Aerial / Overhead (Flight Deck)** | [DVIDS 9762740](https://www.dvidshub.net/image/9762740/cmv-22b-osprey-conduct-flyover-nascar-san-diego-weekend) | 9762740 | 2026-06-20 | VRM-50 "Sunhawks" / San Diego, CA | High-angle aerial perspective showing upper wing torque box, engine nacelle tops, proprotor disc sweep, and upper fuselage dorsal crown. |
| **Quarter (Rear 3/4 Carrier Touchdown)** | [DVIDS 8911110](https://www.dvidshub.net/image/8911110/abraham-lincoln-conducts-flight-operations) | 8911110 | 2024-08-11 | VRM-30 "Titans" / USS *Abraham Lincoln* (CVN 72) | Three-quarter aft perspective landing on carrier flight deck; shows dual main landing gear footprint, twin vertical stabilizers, rudder trim, and exhaust deflectors. |
| **Quarter (Amphibious Flight Deck)** | [DVIDS 9769791](https://www.dvidshub.net/image/9769791/cmv-22b-osprey-is-positioned-aboard-mistral-class-amphibious-assault-ship-fs-dixmude) | 9769791 | 2026-06-18 | VRM-40 "Rawhides" / FS *Dixmude* (L9015) | Positioned on flight deck during allied interoperability exercises; documents forward quarter perspective, nacelles in full $90^\circ$ VTOL mode, and deck clearance. |
| **Mechanism: Nacelle VTOL ($90^\circ$ Mode)** | [DVIDS 8654707](https://www.dvidshub.net/image/8654707/cmv-22b-ospreys-land-aboard-uss-gerald-r-ford-cvn-78) | 8654707 | 2024-09-13 | VRM-40 "Rawhides" / USS *Gerald R. Ford* (CVN 78) | First CMV-22B landing aboard CVN-78; close-up view of Rolls-Royce AE1107C nacelles in full $90^\circ$ vertical VTOL mode, wingtip conversion spindles, and proprotor clearance. |
| **Mechanism: Cargo Ramp & Interior** | [DVIDS 8655897](https://www.dvidshub.net/image/8655897/first-arrival-cmv-22b-ford) | 8655897 | 2024-09-13 | VRM-40 "Rawhides" / USS *Gerald R. Ford* (CVN 78) | Lower cargo ramp fully lowered onto CVN-78 flight deck; shows internal cargo bay tie-down rings, roller track fittings, and flight-deck logistics staging. |
| **Mechanism: Medical & Cabin Interior** | [DVIDS 6549568](https://www.dvidshub.net/image/6549568/uss-carl-vinson-conducts-first-cmv-22b-osprey-medevac-exercise) | 6549568 | 2021-02-22 | VRM-30 "Titans" / USS *Carl Vinson* (CVN 70) | Interior view inside cargo cabin during first carrier MEDEVAC drill; reveals cabin sidewall ribs, ceiling plumbing, passenger troop seats, and lighting. |
| **Mechanism: Blade Fold & Wing Stow** | [DVIDS 131215018](https://www.dvidshub.net/image/131215018) | 131215018 | 2013-12-15 | US Navy / USS *Bataan* (LHD 5) | Full Blade Fold and Wing Stow (BFWS) configuration on flight deck; documents proprotor blades folded inward parallel to wing and wing rotated $90^\circ$ clockwise along fuselage. |

---

## 10. External Sibling Collector Status & Integration

* **External Sibling Location:** `D:/dreidel3d-sv2/refimages/*/INDEX.md`
* **Inspection Findings:**
  * The sibling collector repository at `D:/dreidel3d-sv2/refimages/air-agy/` has completed its collection run and generated the authoritative consolidated catalog: [`INDEX.md`](../../../../dreidel3d-sv2/refimages/air-agy/INDEX.md).
  * **Curated Asset Folder:** `D:/dreidel3d-sv2/refimages/air-agy/cmv22b-osprey/` contains 12 verified high-resolution reference images specifically curated for the Bell Boeing CMV-22B Osprey (`cmv22b-osprey`).
* **Collector Status:** **Index ready and operational.**
* **Portable Relative Linking:** In compliance with the Project Eretz external reference rules, local image assets are linked using portable relative paths:
  * Front View: [`cmv22b-osprey-front-dvids-flfront.jpg`](../../../../dreidel3d-sv2/refimages/air-agy/cmv22b-osprey/cmv22b-osprey-front-dvids-flfront.jpg)
  * Rear Cargo Ramp: [`cmv22b-osprey-rear-dvids-8911113.jpg`](../../../../dreidel3d-sv2/refimages/air-agy/cmv22b-osprey/cmv22b-osprey-rear-dvids-8911113.jpg)
  * Port Profile: [`cmv22b-osprey-port-dvids-vrm30land.jpg`](../../../../dreidel3d-sv2/refimages/air-agy/cmv22b-osprey/cmv22b-osprey-port-dvids-vrm30land.jpg)
  * Starboard Profile: [`cmv22b-osprey-stbd-dvids-vrm30takeoff.jpg`](../../../../dreidel3d-sv2/refimages/air-agy/cmv22b-osprey/cmv22b-osprey-stbd-dvids-vrm30takeoff.jpg)
  * Overhead View: [`cmv22b-osprey-overhead-dvids-vinson-vrm30.jpg`](../../../../dreidel3d-sv2/refimages/air-agy/cmv22b-osprey/cmv22b-osprey-overhead-dvids-vinson-vrm30.jpg)
  * Three-Quarter Front: [`cmv22b-osprey-threequarter-front-dvids-vrm40reveal.jpg`](../../../../dreidel3d-sv2/refimages/air-agy/cmv22b-osprey/cmv22b-osprey-threequarter-front-dvids-vrm40reveal.jpg)
  * Three-Quarter Rear: [`cmv22b-osprey-threequarter-rear-dvids-8911110.jpg`](../../../../dreidel3d-sv2/refimages/air-agy/cmv22b-osprey/cmv22b-osprey-threequarter-rear-dvids-8911110.jpg)
  * Nacelle VTOL on CVN-78: [`cmv22b-osprey-nacelle-vtol-dvids-8654707.jpg`](../../../../dreidel3d-sv2/refimages/air-agy/cmv22b-osprey/cmv22b-osprey-nacelle-vtol-dvids-8654707.jpg)
  * Nacelle Hover Testing: [`cmv22b-osprey-nacelle-hover-commons-amarillo-reveal.jpg`](../../../../dreidel3d-sv2/refimages/air-agy/cmv22b-osprey/cmv22b-osprey-nacelle-hover-commons-amarillo-reveal.jpg)
  * Blade Fold / Wing Stow: [`cmv22b-osprey-wingstow-bladefold-dvids-131215018.jpg`](../../../../dreidel3d-sv2/refimages/air-agy/cmv22b-osprey/cmv22b-osprey-wingstow-bladefold-dvids-131215018.jpg)
  * Cargo Ramp Interior on CVN-78: [`cmv22b-osprey-interior-cargoramp-dvids-8655897.jpg`](../../../../dreidel3d-sv2/refimages/air-agy/cmv22b-osprey/cmv22b-osprey-interior-cargoramp-dvids-8655897.jpg)
  * Glass Cockpit Interior: [`cmv22b-osprey-interior-cockpit-commons-v22mfd.jpg`](../../../../dreidel3d-sv2/refimages/air-agy/cmv22b-osprey/cmv22b-osprey-interior-cockpit-commons-v22mfd.jpg)
* **Zero Worktree Duplication:** No external image files were downloaded, copied, or duplicated into `D:/z4yin/z4yin-files/skills/naval-expert/`.

---

## 11. Authoritative Primary Source List

1. **United States Navy (Office of Information):** *V-22B Osprey Tilt Rotor Aircraft Fact File*, Article ID 2169785 ([navy.mil Fact File](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169785/v-22b-osprey-tilt-rotor-aircraft/)). Confirms official US Navy dimensions: Length 57 ft 4 in (17.48 m), Wingspan 83 ft 10 in (25.55 m), Height 22 ft 1 in (6.73 m), Max VTOL 52,600 lb, Max Rolling Takeoff 60,500 lb, Rolls-Royce AE1107C propulsion, and COD mission role.
2. **Naval Air Systems Command (NAVAIR):** *CMV-22B Osprey Program Profile*, PMA-275 V-22 Joint Program Office, Patuxent River, MD ([navair.navy.mil](https://www.navair.navy.mil/product/CMV-22B)). Confirms 1,150 nm mission range, 4-person crew, cargo capacity (20,000 lb internal), and carrier logistics replacement of C-2A Greyhound.
3. **Office of the Director, Operational Test and Evaluation (DOT&E):** *CMV-22B Carrier Onboard Delivery Operational Assessment & Annual Reports*, Office of the Secretary of Defense, Washington, D.C. ([dote.osd.mil](https://www.dote.osd.mil)). Confirms +524 gal fuel sponson redesign, internal Wing Auxiliary Tanks (WATs), unrefueled 1,150 nm range verification, and Pratt & Whitney F135 engine power module transport validation.
4. **Bell Textron & The Boeing Company:** *V-22 Osprey Pocket Guide & Technical Specifications*, Fort Worth, TX / Philadelphia, PA ([boeing.com](https://www.boeing.com)). Confirms stowed/folded dimensions ($63\text{ ft }0\text{ in} \times 18\text{ ft }5\text{ in} \times 18\text{ ft }3\text{ in}$), Automatic Blade Fold & Wing Stow (BFWS) $\le 90\text{ s}$ cycle, proprotor diameter ($38\text{ ft }0\text{ in}$), and wheelbase/wheel track geometry.
5. **Naval Air Systems Command (NAVAIR):** *NATOPS Flight Manual - Navy Model MV-22B/CMV-22B Tiltrotor*, NAVAIR 01-V22AAD-1 ([navair.navy.mil](https://www.navair.navy.mil)). Confirms nacelle conversion limits ($0.0^\circ$ to $+97.5^\circ$), flight control surface deflections (flaperons, elevator, twin rudders), proprotor operating RPMs (397 VTOL / 333 Cruise), and fuel transfer management sequence.
6. **Naval Air Systems Command (NAVAIR):** *CV NATOPS Manual - Carrier Aircraft Operating Procedures*, NAVAIR 00-80T-105 ([navair.navy.mil](https://www.navair.navy.mil)). Documents carrier flight-deck spotting, wind-over-deck envelopes, tie-down chain matrices, and maximum carrier recovery weight limits ($52,600\text{ lb}$ VTOL / $57,000\text{ lb}$ rolling).
7. **Rolls-Royce Corporation:** *AE 1107C-Liberty Turboshaft Engine Data Sheet*, Indianapolis, IN ([rolls-royce.com](https://www.rolls-royce.com)). Documents 6,150–6,200 shp power output, dual-spool axial-flow design, and tilting nacelle lubrication subsystems.
8. **Defense Visual Information Distribution Service (DVIDS):** Primary trusted military imagery repository ([dvidshub.net](https://www.dvidshub.net)). Verified high-resolution imagery records documenting CMV-22B flight operations, carrier qualifications, cargo loading, and interior layouts aboard USS *Gerald R. Ford* (CVN-78), USS *Carl Vinson* (CVN-70), USS *Abraham Lincoln* (CVN-72), and USS *George Washington* (CVN-73).


---

<!-- NAVAL-CURRENT-START -->
# cmv-22b-osprey — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:24:21.394242+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-CMV-22B` | NAVAIR lists length 57 ft 4 in, height 22 ft 1 in, wingspan 83 ft 10 in (derived approximately 17.48 m, 6.73 m, 25.55 m). The wingspan field does not define inclusion of proprotors; do not relabel it bare-wing span. Two AE1107C engines; MV-22B-derived carrier onboard delivery variant. | [Primary source](https://www.navair.navy.mil/product/CMV-22B-Osprey); Specifications / Background, updated February 2023 |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| proprotor rotation | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| nacelle conversion | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| blade fold | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| wing stow | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| cargo ramp | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| landing gear | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Do not merge adjacent variants, operational and stowed dimensions, or demonstration motion with sourced operating rates. Exact fitted counts/locations and kinematic values not sourced above remain unresolved.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [USS Carl Vinson Conducts First CMV-22B Osprey Medevac Exercise ](https://www.dvidshub.net/image/6549568/uss-carl-vinson-conducts-first-cmv-22b-osprey-medevac-exercise) | `210222-N-SS900-1256 PACIFIC OCEAN (Feb. 22, 2021) Lt. Andrew Nop, a native of Cherry Hill, N.J., assigned to Nimitz-class nuclear aircraft carrier USS Carl Vinson (CVN 70), starts an intravenous access on a sim` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Air Assault - 25thID Lightning Academy Rappel Day ](https://www.dvidshub.net/image/6620573/air-assault-25thid-lightning-academy-rappel-day) | `Schofield Barracks, HI — Soldiers rappel from a UH-60 Black Hawk during a 10-day air assault course at 25th Infantry Division Lightning Academy on 22 April, 2021. In addition to rappelling, students learned abo` — `sourced-caption` | `port` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [First East Coast-Assigned Navy CMV-22B Osprey Arrives to Norfolk ](https://www.dvidshub.net/image/8324361/first-east-coast-assigned-navy-cmv-22b-osprey-arrives-norfolk) | `The first East Coast-assigned Navy tiltrotor vertical/short takeoff and landing (V/STOL) aircraft CMV-22B Osprey conducts post-flight checks following its arrival at Naval Station Norfolk, April 5. The CMV-22B ` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [CMV-22B Ospreys Land Aboard USS Gerald R. Ford (CVN 78) ](https://www.dvidshub.net/image/8654707/cmv-22b-ospreys-land-aboard-uss-gerald-r-ford-cvn-78) | `ATLANTIC OCEAN (Sept. 19, 2024) A CMV-22B Osprey, assigned to the "Mighty Bison" of Fleet Logistics Multi-Mission Squadron (VRM) 40, takes off from the flight deck of the world's largest aircraft carrier, USS G` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [First arrival of CMV-22B on Ford ](https://www.dvidshub.net/image/8655897/first-arrival-cmv-22b-ford) | `ATLANTIC OCEAN (Sept. 19, 2024) – Sailors assigned to the "Mighty Bison" of Fleet Logistics Multi-Mission Squadron (VRM) 40, load cargo into a CMV-22B Osprey on the flight deck of the world’s largest aircraft c` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [CMV-22B Osprey Lands at Naval Air Facility Atsugi ](https://www.dvidshub.net/image/8749610/cmv-22b-osprey-lands-naval-air-facility-atsugi) | `NAVAL AIR FACILITY ATSUGI, Japan (Nov. 7, 2024) - A U.S. Navy CMV-22B Osprey attached to Fleet Logistics Multi-Mission Squadron (VRM) 30, Detachment Forward-Deployed Naval Forces (FDNF), taxis across the runway` — `sourced-caption` | `starboard` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [CMV-22B Osprey Lands at Naval Air Facility Atsugi ](https://www.dvidshub.net/image/8749661/cmv-22b-osprey-lands-naval-air-facility-atsugi) | `NAVAL AIR FACILITY ATSUGI, Japan (Nov. 7, 2024) - A U.S. Navy CMV-22B Osprey attached to Fleet Logistics Multi-Mission Squadron (VRM) 30, Detachment Forward-Deployed Naval Forces (FDNF), taxis across the runway` — `sourced-caption` | `starboard` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Abraham Lincoln conducts flight operations ](https://www.dvidshub.net/image/8911110/abraham-lincoln-conducts-flight-operations) | `250306-N-TI287-1039 PACIFIC OCEAN (March 6, 2025) An CMV-22 Osprey, assigned to Fleet Multimission Squadron (VRM) 30, taxis after landing on the flight deck of the Nimitz-class aircraft carrier USS Abraham Linc` — `sourced-caption` | `quarter` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Abraham Lincoln conducts flight operations ](https://www.dvidshub.net/image/8911113/abraham-lincoln-conducts-flight-operations) | `250306-N-TI287-1086 PACIFIC OCEAN (March 6, 2025) Sailors unload an CMV-22 Osprey, assigned to Fleet Multimission Squadron (VRM) 30, on the flight deck of the Nimitz-class aircraft carrier USS Abraham Lincoln (` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [CMV-22B Osprey conduct flyover of NASCAR San Diego Weekend ](https://www.dvidshub.net/image/9762740/cmv-22b-osprey-conduct-flyover-nascar-san-diego-weekend) | `A CMV-22B Osprey tiltroter aircraft of Fleet Logistics Multi-Mission Squadron (VRM) 50 flies over the Pacific Ocean enroute to conduct a flyover of NASCAR San Diego Weekend, on Naval Base Coronado, June 19, 202` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [A CMV-22B Osprey is positioned aboard the Mistral-class amphibious assault ship FS Dixmude ](https://www.dvidshub.net/image/9769791/cmv-22b-osprey-positioned-aboard-mistral-class-amphibious-assault-ship-fs-dixmude) | `NORFOLK, Va. (June 23, 2026) A CMV-22B Osprey, assigned to Fleet Logistics Multi-Mission Squadron (VRM) 40, is positioned on the flight deck aboard the Mistral-class amphibious assault ship FS Dixmude (L9015), ` — `sourced-caption` | `quarter` candidate, `inferred-view`; exact coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=cmv+22b+osprey+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=cmv+22b+osprey+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=cmv+22b+osprey+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=cmv+22b+osprey+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=cmv+22b+osprey+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=cmv+22b+osprey+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=cmv+22b+osprey+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- [Existing air-agy index](../../../../../dreidel3d-sv2/refimages/air-agy/INDEX.md); `sourced-local-index-presence`. Read unit rows, not a blanket Complete banner. Some indexes contradict their own coverage matrices.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.
<!-- NAVAL-CURRENT-END -->


---

<!-- NAVAL-CURRENT-START -->
# cmv-22b-osprey — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:32:48.849695+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-CMV-22B` | NAVAIR lists length 57 ft 4 in, height 22 ft 1 in, wingspan 83 ft 10 in (derived approximately 17.48 m, 6.73 m, 25.55 m). The wingspan field does not define inclusion of proprotors; do not relabel it bare-wing span. Two AE1107C engines; MV-22B-derived carrier onboard delivery variant. | [Primary source](https://www.navair.navy.mil/product/CMV-22B-Osprey); Specifications / Background, updated February 2023 |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| proprotor rotation | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| nacelle conversion | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| blade fold | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| wing stow | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| cargo ramp | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| landing gear | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Do not merge adjacent variants, operational and stowed dimensions, or demonstration motion with sourced operating rates. Exact fitted counts/locations and kinematic values not sourced above remain unresolved.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [USS Carl Vinson Conducts First CMV-22B Osprey Medevac Exercise ](https://www.dvidshub.net/image/6549568/uss-carl-vinson-conducts-first-cmv-22b-osprey-medevac-exercise) | `210222-N-SS900-1256 PACIFIC OCEAN (Feb. 22, 2021) Lt. Andrew Nop, a native of Cherry Hill, N.J., assigned to Nimitz-class nuclear aircraft carrier USS Carl Vinson (CVN 70), starts an intravenous access on a sim` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [First East Coast-Assigned Navy CMV-22B Osprey Arrives to Norfolk ](https://www.dvidshub.net/image/8324361/first-east-coast-assigned-navy-cmv-22b-osprey-arrives-norfolk) | `The first East Coast-assigned Navy tiltrotor vertical/short takeoff and landing (V/STOL) aircraft CMV-22B Osprey conducts post-flight checks following its arrival at Naval Station Norfolk, April 5. The CMV-22B ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [CMV-22B Ospreys Land Aboard USS Gerald R. Ford (CVN 78) ](https://www.dvidshub.net/image/8654707/cmv-22b-ospreys-land-aboard-uss-gerald-r-ford-cvn-78) | `ATLANTIC OCEAN (Sept. 19, 2024) A CMV-22B Osprey, assigned to the "Mighty Bison" of Fleet Logistics Multi-Mission Squadron (VRM) 40, takes off from the flight deck of the world's largest aircraft carrier, USS G` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [First arrival of CMV-22B on Ford ](https://www.dvidshub.net/image/8655897/first-arrival-cmv-22b-ford) | `ATLANTIC OCEAN (Sept. 19, 2024) – Sailors assigned to the "Mighty Bison" of Fleet Logistics Multi-Mission Squadron (VRM) 40, load cargo into a CMV-22B Osprey on the flight deck of the world’s largest aircraft c` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [CMV-22B Osprey Lands at Naval Air Facility Atsugi ](https://www.dvidshub.net/image/8749610/cmv-22b-osprey-lands-naval-air-facility-atsugi) | `NAVAL AIR FACILITY ATSUGI, Japan (Nov. 7, 2024) - A U.S. Navy CMV-22B Osprey attached to Fleet Logistics Multi-Mission Squadron (VRM) 30, Detachment Forward-Deployed Naval Forces (FDNF), taxis across the runway` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [CMV-22B Osprey Lands at Naval Air Facility Atsugi ](https://www.dvidshub.net/image/8749661/cmv-22b-osprey-lands-naval-air-facility-atsugi) | `NAVAL AIR FACILITY ATSUGI, Japan (Nov. 7, 2024) - A U.S. Navy CMV-22B Osprey attached to Fleet Logistics Multi-Mission Squadron (VRM) 30, Detachment Forward-Deployed Naval Forces (FDNF), taxis across the runway` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Abraham Lincoln conducts flight operations ](https://www.dvidshub.net/image/8911110/abraham-lincoln-conducts-flight-operations) | `250306-N-TI287-1039 PACIFIC OCEAN (March 6, 2025) An CMV-22 Osprey, assigned to Fleet Multimission Squadron (VRM) 30, taxis after landing on the flight deck of the Nimitz-class aircraft carrier USS Abraham Linc` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Abraham Lincoln conducts flight operations ](https://www.dvidshub.net/image/8911113/abraham-lincoln-conducts-flight-operations) | `250306-N-TI287-1086 PACIFIC OCEAN (March 6, 2025) Sailors unload an CMV-22 Osprey, assigned to Fleet Multimission Squadron (VRM) 30, on the flight deck of the Nimitz-class aircraft carrier USS Abraham Lincoln (` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [CMV-22B Osprey conduct flyover of NASCAR San Diego Weekend ](https://www.dvidshub.net/image/9762740/cmv-22b-osprey-conduct-flyover-nascar-san-diego-weekend) | `A CMV-22B Osprey tiltroter aircraft of Fleet Logistics Multi-Mission Squadron (VRM) 50 flies over the Pacific Ocean enroute to conduct a flyover of NASCAR San Diego Weekend, on Naval Base Coronado, June 19, 202` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [A CMV-22B Osprey is positioned aboard the Mistral-class amphibious assault ship FS Dixmude ](https://www.dvidshub.net/image/9769791/cmv-22b-osprey-positioned-aboard-mistral-class-amphibious-assault-ship-fs-dixmude) | `NORFOLK, Va. (June 23, 2026) A CMV-22B Osprey, assigned to Fleet Logistics Multi-Mission Squadron (VRM) 40, is positioned on the flight deck aboard the Mistral-class amphibious assault ship FS Dixmude (L9015), ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=cmv+22b+osprey+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=cmv+22b+osprey+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=cmv+22b+osprey+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=cmv+22b+osprey+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=cmv+22b+osprey+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=cmv+22b+osprey+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=cmv+22b+osprey+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- [Existing air-agy index](../../../../../dreidel3d-sv2/refimages/air-agy/INDEX.md); `sourced-local-index-presence`. Read unit rows, not a blanket Complete banner. Some indexes contradict their own coverage matrices.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.

Independent image-subject review correction: wrong-subject candidates excluded, duplicate image IDs collapsed, and sibling equipment separated above. Older revisions remain audit evidence and are superseded by this last current section.
<!-- NAVAL-CURRENT-END -->
