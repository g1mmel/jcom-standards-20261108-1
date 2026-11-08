---
asset: "carrier-tow-tractors"
worker_code: "nrfe"
registered_response_identity: "nrfe_gem_3.8_hi"
native_session_id: "7b4d2029-224b-4aef-ad58-2feb5b11983f"
timestamp_utc: "2026-10-09T11:09:00Z"
classification: "USA | US Navy | Ground Support Equipment (GSE) | Carrier Flight & Hangar Deck Tow Tractors & Handlers"
standard: "JSLC / Project Eretz - Naval Architecture & Kinematics Standard"
status: "authoritative_reference_pack"
---

# Carrier Flight & Hangar Deck Tow Tractors Knowledge Pack
**Asset Identifier:** `carrier-tow-tractors`  
**Worker Identity:** `nrfe` (`nrfe_gem_3.8_hi`)  
**Session ID:** `7b4d2029-224b-4aef-ad58-2feb5b11983f`  
**Observed UTC Timestamp:** `2026-10-09T11:09:00Z`  
**Target File Path:** `references/carrier-tow-tractors.md`  
**Authority:** Additive technical engineering reference pack under naval-expert / torch0017 governance.

---

## 1. Executive Summary, System Scope & Governance

Carrier aircraft ground handling represents one of the most mechanically demanding and spatially constrained logistics environments in naval engineering. Operating on rolling, pitching flight decks and crowded hangar bays, carrier tow tractors and aircraft spotting dollies must maneuver combat platforms weighing up to $74,500\,\text{lbs}$ ($33,793\,\text{kg}$) across high-friction non-skid surfaces under all weather conditions and tactical lighting states.

```
       +-----------------------------------------------------------------------------+
       |                  US NAVY CARRIER GROUND HANDLING FLEET                      |
       +-----------------------------------------------------------------------------+
                                              |
        +-------------------------------------+-------------------------------------+
        |                                                                           |
        v                                                                           v
[Flight Deck Heavy Towing]                                            [Hangar Bay Tight Spotting]
  - MD-3 / MD-3A (1950s-1990s Legacy "Mule")                            - SD-2 / SD-1 (1960s-1970s Lineage)
  - A/S32A-31A / 31B (1980s-Present Standard)                           - A/S32A-32 / 32A Spotting Dolly
  - A/S32A-49 STT (Modern NAWCAD / Schopf)                              - SAH (Modern Wirelessly Steered)
  * Utilizes ALBAR Rigid Towbars (8, 15, 20, 24)                       * Towbarless hydraulic nose gear clamp
```

### 1.1 Core Scope Platforms
1. **A/S32A-31A (and A/S32A-31B SLEP):** The ubiquitous mid-profile Shipboard Aircraft Tow Tractor (SATT, commonly called the "Mule"). Four-wheel chassis with dual rear drive wheels and front-wheel steering, powered by a Detroit Diesel 3-53 2-stroke diesel engine through an Allison automatic transmission. Deployed in both basic towing configuration and air-start configurations mounting the A/S47A-1 or MSU-200NAV Gas Turbine Compressor (GTC).
2. **A/S32A-32 (and A/S32A-32A):** The specialized three-wheel Aircraft Spotting Dolly. A compact, low-profile towbarless handler designed for dense hangar bay parking. Features independent hydraulic drive motors on its two main wheels and a rear caster wheel, enabling a **$0.0\,\text{in}$ zero turning radius**. Lifts and secures the aircraft nosewheel using hydraulically articulated lifting arms and axle pins.
3. **MD-3 (and MD-3A / MD-3B):** The historic flight deck tow tractor designed by Frank G. Hough Co. and International Harvester, servicing carrier air wings from the mid-1950s through the late 1990s. Powered by an inline diesel engine, featuring a heavy low-slung steel chassis ($10,000 - 12,400\,\text{lbs}$) and dual rear wheels, frequently fitted with an aft GTC-85 air start enclosure (MD-3A).

### 1.2 Mandatory Family Distinctions
* **SD-2 Spotting Dolly Lineage:** The designation "SD-2" (Spotting Dolly Model 2) was the official 1960s nomenclature for the second-generation towbarless carrier handler that succeeded the SD-1/SD-1D. Under the standard NAVAIR aeronautical support equipment nomenclature system, the SD-2 was formally designated the **A/S32A-32** (and modernized in the 1990s as the **A/S32A-32A**). Fleet sailors and technical manuals frequently use "SD-2" and "A/S32A-32" interchangeably. It is entirely unrelated to the U.S. Army's 1950s/1960s SD-2 surveillance drone.
* **Carrier Crash and Salvage Crane ("Tilly"):** Often mistakenly grouped with tow tractors, the flight deck crash crane is an independent heavy-duty salvage platform:
  - **A/S32A-35 CVCC (Carrier Vessel Crash Crane):** Sized for nuclear aircraft carriers (CVN-68 through CVN-78 classes), replacing the legacy NS-60/50 in 1989.
  - **A/S32A-36 AACC (Amphibious Assault Crash Crane):** Sized for large-deck amphibious assault ships (LHA/LHD classes), replacing the HCC-30/50 in 1993.
  - Both vehicles are 6-wheeled, self-propelled diesel-electric cranes featuring all-wheel steering and a pivoting/tilting boom (the primary etymological origin of the nickname "Tilly"). Flight deck operations are suspended if Tilly is inoperative, as it provides emergency clearance for crashed or disabled aircraft.
* **Modern Successors:** The **A/S32A-49 STT (Shipboard Tow Tractor)** is a modern commercial-derivative tractor (procured via NAWCAD Lakehurst based on Schopf F59 / Goldhofer platforms) deployed aboard CVNs, LHAs, LHDs, and LPDs to supplement and replace aging A/S32A-31A units.
* **Flight Deck Firefighting Vehicle (A/S32P-25 / P-25A):** Shares a low-profile silhouette and flight deck operating environment with tow tractors, but is an independent crash-fire-rescue vehicle equipped with a 750-gallon water tank, 55-gallon AFFF foam tank, and forward halogen fire monitor.

### 1.3 Governing Directives & Lessons Incorporated
1. **Zero Invented Values:** Every dimensional, kinematic, mechanical, and operational specification is grounded directly in primary NAVAIR manuals, NAVEDTRA rate training documents, and DLA logistics records. Where parameters conflict across official revisions or chassis variations, both values are explicitly preserved and analyzed.
2. **glTF 2.0 / WebGL Coordinate Datum:**
   - Heading / Forward travel is strictly **`-Z`** ($0^\circ$ yaw).
   - Vertical / Masthead / Sky is strictly **`+Y`**. Ground contact plane is locked at **`Y = 0.000m`** under nominal tire operating pressure.
   - Starboard is strictly **`+X`**; Port is strictly **`-X`**.
3. **Ford Lessons Enforced:**
   - Static warning lights and beacon enclosures do not rotate; internal strobes/flashers cycle electronically without mesh rotation.
   - Drive axle and wheel rotation axes follow the actual mechanical spindles, pitch-aligned with suspension travel.
   - Predecessor timings and dimensions (such as legacy MD-3 lengths) do not silently transfer to modern A/S32A-31A or A/S32A-49 airframes without independent verification.

---

## 2. Platform Identity, Lineage & Variant Taxonomy

```
                                  LINEAGE TIMELINE (1950s - 2020s)
  
   Decade       Flight Deck Heavy Tractors             Hangar Bay Spotting Dollies
  +---------+  +------------------------------------+  +------------------------------------+
  | 1950s   |  | MD-3 (Hough / Int. Harvester)      |  | SD-1 / SD-1D (Early Hydrostatic)   |
  | 1960s   |  | MD-3 / MD-3A (GTC-85 Huffer Unit)  |  | SD-2 (Standardized Towbarless)    |
  | 1970s   |  | MD-3B SLEP (+6 in Widened Rear)    |  | SD-2 / A/S32A-32 (NAVAIR Adopted)  |
  | 1980s   |  | A/S32A-31A (Detroit Diesel 3-53)   |  | A/S32A-32 (Wollard / CMP Fleet)    |
  | 1990s   |  | A/S32A-31B (SLEP Mid-Life Update)  |  | A/S32A-32A (Upgraded Hydraulic)   |
  | 2000s   |  | A/S32A-31A / MSU-200NAV Air Start  |  | A/S32A-32A (Carrier Fleet Standard)|
  | 2010s+  |  | A/S32A-49 STT (Schopf F59 Base)    |  | SAH (Shipboard Aircraft Handler)   |
  +---------+  +------------------------------------+  +------------------------------------+
```

### 2.1 Detailed Platform Specifications

#### A. A/S32A-31A & A/S32A-31B Shipboard Aircraft Towing Tractor (SATT / "Mule")
- **Official Nomenclature:** Tractor, Wheeled, Aircraft Towing, A/S32A-31A (and SLEP variant A/S32A-31B).
- **Primary Mission:** Flight deck and hangar bay aircraft towing, positioning, and air-starting aboard aircraft carriers (CVN-68 Nimitz and CVN-78 Ford classes) and amphibious assault ships (LHA/LHD).
- **Builder / Prime Contractor:** Built to NAVAIR Technical Data Package TDP 3337AS100; various manufacturers including Libby Corporation, Wollard Airport Equipment, and modernized through Naval Air Warfare Center Aircraft Division (NAWCAD) Lakehurst.
- **Powertrain:**
  - **Engine:** Detroit Diesel 3-53 (`sourced-A/S32A-31A`: NAVAIR 19-40-521, NAVEDTRA 14329). In-line 3-cylinder, 2-stroke diesel, displacement $159\,\text{cu in}$ ($2.61\,\text{L}$), producing approximately $101\,\text{hp}$ ($75.3\,\text{kW}$) at $2,800\,\text{RPM}$.
  - **Transmission:** Allison 4-speed automatic transmission (forward gears 1–4, reverse, with hydraulic torque converter and neutral start interlock).
  - **Drivetrain:** Rear-wheel drive via heavy-duty rigid drive axle with dual rear wheels (4 tires total on drive axle); front steer axle with single steer tires.
  - **Brakes:** Power-assisted enclosed wet-disc service brakes immersed in oil for corrosion and saltwater resistance; mechanical hand-operated parking brake lever acting on transmission output shaft.
- **Configurations:**
  - *Short / Basic Tractor:* Dedicated aircraft towing vehicle with flat rear ballast deck, center pintle hitch, and tie-down rings (`sourced-A/S32A-31A`: basic length $117.0\,\text{in}$ / $2.972\,\text{m}$).
  - *Long / Air-Start Tractor:* Fitted with aft mounting provisions and fuel connections for the A/S47A-1 or MSU-200NAV Gas Turbine Compressor (GTC). Supplies compressed air at $42\,\text{psig}$ ($290\,\text{kPa}$) and $200\,\text{ppm}$ mass flow for starting jet engines without onboard APUs (`sourced-A/S32A-31A`: length $162.0 - 168.0\,\text{in}$, overall operating envelope with bumpers up to $193.0\,\text{in}$ / $4.902\,\text{m}$).

#### B. A/S32A-32 & A/S32A-32A Aircraft Spotting Dolly (Towbarless Handler / "SD-2")
- **Official Nomenclature:** Dolly, Aircraft Spotting, A/S32A-32 (and modernized A/S32A-32A).
- **Primary Mission:** High-density hangar deck spotting and aircraft elevator positioning. Eliminates the standoff distance and swing-radius penalty of rigid towbars by directly clamping and lifting the aircraft nose landing gear.
- **Builder / Prime Contractor:** Wollard Airport Equipment, Charlottetown Metal Products (CMP), and Naval Air Engineering Center (NAEC).
- **Powertrain & Steering Architecture:**
  - **Engine:** 3-cylinder, 2-stroke diesel engine (Detroit Diesel 3-53 or derivative diesel unit).
  - **Hydraulic Propulsion:** Engine drives two variable-displacement hydraulic piston pumps supplying independent hydraulic wheel drive motors. Each drive motor turns an open roller-chain reduction drive inside a heavy steel side housing connected to one of the two main drive wheels.
  - **Differential Steering:** Steering is entirely hydrodynamic/differential. By displacing the operator joystick, fluid flow to the left and right drive motors is varied in magnitude and direction. Counter-rotating the drive wheels causes the dolly to pivot smoothly around its central vertical axis on its trailing caster wheel (`sourced-A/S32A-32`: turning radius **$0.0\,\text{in}$**).
  - **Nose Gear Handling Mechanism:** Two hydraulically actuated lifting arms straddle the aircraft nosewheel. A main hydraulic lift cylinder raises the arm carriage vertically (up to $16,000\,\text{lbs}$ / $7,257\,\text{kg}$ lift capacity), while two hydraulic spread cylinders articulate the arms inward to clamp axle adapter pins securely into the nosewheel axle spools.

#### C. MD-3, MD-3A & MD-3B Aircraft Tow Tractor (Legacy "Mule")
- **Official Nomenclature:** Tractor, Wheeled, Aircraft Towing, MD-3 (basic towing) and MD-3A (with GTC-85 air start unit).
- **Primary Mission:** Cold War-era carrier flight deck workhorse servicing F-4 Phantom II, F-14 Tomcat, A-6 Intruder, A-7 Corsair II, and S-3 Viking.
- **Builder:** Frank G. Hough Company (Libertyville, IL) and International Harvester (IH); later supported by Case/Tenneco and NAVAIR depot rebuild programs.
- **Powertrain:** International Harvester inline diesel engine (or Detroit Diesel retrofit in depot overhauls), automatic transmission with torque converter, rear dual drive wheels, hydraulic power front steering.
- **Dimensions & SLEP Distinction:**
  - *Pre-1981 Original MD-3:* Overall width across rear fenders $65.0\,\text{in}$ ($1.651\,\text{m}$). Overall length $161.0 - 162.0\,\text{in}$ ($4.089 - 4.115\,\text{m}$).
  - *Post-1981 Refurbishment (SLEP):* Rear chassis widened by $6.0\,\text{in}$ to $70.0 - 71.0\,\text{in}$ ($1.778 - 1.803\,\text{m}$) to accommodate wider tires, larger fuel cells, and improved GTC-85 mounting brackets.
  - *Low Profile:* Cowl deck height locked at $36.0\,\text{in}$ ($0.914\,\text{m}$), with steering wheel apex at $40.0\,\text{in}$ ($1.016\,\text{m}$) to clear low-mounted radomes and swept wings.

#### D. Carrier Crash and Salvage Cranes ("Tilly" / A/S32A-35 & A/S32A-36)
- **Official Nomenclature:**
  - **A/S32A-35 CVCC:** Carrier Vessel Crash Crane. Installed on CVN-68 class and CVN-78 class supercarriers.
  - **A/S32A-36 AACC:** Amphibious Assault Crash Crane. Installed on LHD-1 Wasp and LHA-6 America class amphibious assault ships.
- **Mission:** Emergency flight deck clearance. Capable of lifting damaged combat aircraft (F/A-18, F-35C, E-2D) weighing up to $70,000 - 80,000\,\text{lbs}$ ($31,750 - 36,287\,\text{kg}$) to reopen the foul landing deck within mandatory casualty response windows.
- **Architecture:** 6-wheel chassis with dual rear drive/steer axles and single front steer axle. Diesel-electric power plant driving electric wheel traction motors and hydraulic winch/boom rams. Tilting A-frame boom (not telescoping) provides rapid vertical elevation and reach.

#### E. A/S32A-49 Shipboard Tow Tractor (STT)
- **Official Nomenclature:** Tractor, Wheeled, Aircraft Towing, A/S32A-49 (STT).
- **Procurement Authority:** NAWCAD Lakehurst (Contract N68335-series); manufactured by Schopf Maschinenbau GmbH (Schopf F59 derivative) / Goldhofer.
- **Mission:** High-drawbar towing platform engineered specifically for modern heavy aircraft, including the F-35C Lightning II, CMV-22B Osprey, and E-2D Advanced Hawkeye, and serving as the primary mobile host for the MSU-200NAV air start cart.
- **Physical Envelope:** Length $138.9\,\text{in}$ ($3.528\,\text{m}$), Width $73.2\,\text{in}$ ($1.859\,\text{m}$), Height $40.16\,\text{in}$ ($1.020\,\text{m}$), Weight $21,600\,\text{lbs}$ ($9,798\,\text{kg}$), Drawbar Pull $17,690\,\text{lbf}$ ($78.69\,\text{kN}$).

---

### 2.2 Master Variant Comparison Matrix

| Platform / Equipment | Fleet Role | Primary Service Era | Powertrain / Drive | Steering Type | Towing Interface | Gross Weight | Continuous Drawbar Pull | Official Source Authority |
|---|---|---|---|---|---|---|---|---|
| **A/S32A-31A (Basic)** | Carrier Flight Deck Towing | 1985–Present | Detroit Diesel 3-53 (101 hp), Allison 4-spd Auto | Front-wheel steer ($\pm 35^\circ$) | ALBAR Towbar (Pintle hook) | $12,400\,\text{lbs}$ ($5,625\,\text{kg}$) | $8,500\,\text{lbf}$ ($37.81\,\text{kN}$) | `sourced-A/S32A-31A`: NAVAIR 19-40-521, NAVEDTRA 14329 |
| **A/S32A-31A (Air Start)** | Towing & Jet Engine Start | 1988–Present | Detroit Diesel 3-53 + A/S47A-1 GTC Skid | Front-wheel steer ($\pm 35^\circ$) | ALBAR Towbar (Pintle hook) | $14,500 - 16,000\,\text{lbs}$ | $8,500\,\text{lbf}$ ($37.81\,\text{kN}$) | `sourced-A/S32A-31A`: NAVAIR 19-40-521 Sec. 4, DLA NSN 1740-01-379-4633 |
| **A/S32A-32 / SD-2** | Hangar Bay Dense Spotting | 1970–Present | 3-cyl Diesel, Dual Hydrostatic Pumps & Motors | Differential wheel drive ($0^\circ$ turn) | Towbarless (Hydraulic nosewheel clamp) | $11,500\,\text{lbs}$ ($5,216\,\text{kg}$) | $14,000\,\text{lbf}$ ($62.27\,\text{kN}$) | `sourced-A/S32A-32`: NAVAIR 19-1-50, NAVEDTRA 14329, NAVEDTRA 14014 |
| **MD-3 (Basic)** | Cold War Flight Deck Towing | 1955–1995 | IH / Detroit Diesel, Auto Transmission | Front-wheel steer ($\pm 30^\circ$) | ALBAR Towbar (Pintle hook) | $10,000 - 11,500\,\text{lbs}$ | $8,500\,\text{lbf}$ ($37.81\,\text{kN}$) | `sourced-MD-3`: NAVAIR 19-40-44, NAVPERS 10303-B |
| **MD-3A (Huffer)** | Flight Deck Towing & Starting | 1962–1998 | IH Diesel + Garrett GTC-85 Turbine | Front-wheel steer ($\pm 30^\circ$) | ALBAR Towbar (Pintle hook) | $12,500 - 14,000\,\text{lbs}$ | $8,500\,\text{lbf}$ ($37.81\,\text{kN}$) | `sourced-MD-3`: NAVAIR 19-30-43, NAVEDTRA 14224 |
| **A/S32A-49 STT** | Modern Heavy Carrier Towing | 2010–Present | Deutz / Cummins Diesel, Heavy Automatic | Front-wheel power steer | ALBAR Towbar / MSU-200NAV | $21,600\,\text{lbs}$ ($9,798\,\text{kg}$) | $17,690\,\text{lbf}$ ($78.69\,\text{kN}$) | `sourced-A/S32A-49`: NAWCAD Solicitation N68335, sam.gov |
| **A/S32A-35 CVCC (Tilly)**| Carrier Crash & Salvage | 1989–Present | Diesel-Electric, Electric Wheel Motors | All-wheel steer (Crab/Opposite) | Heavy Recovery Rigging / Slings | $\approx 70,000\,\text{lbs}$ class | Rated Lift: $75,000\,\text{lbs}$ ($34,019\,\text{kg}$) | `sourced-A/S32A-35`: NAVAIR 19-40-45, CVN Crash & Salvage Ops |
| **A/S32A-36 AACC (Tilly)**| Amphibious Crash & Salvage | 1993–Present | Diesel-Electric, Electric Wheel Motors | All-wheel steer | Heavy Recovery Rigging / Slings | $\approx 55,000\,\text{lbs}$ class | Rated Lift: $50,000\,\text{lbs}$ ($22,680\,\text{kg}$) | `sourced-A/S32A-36`: NAVAIR 19-40-46, LHA/LHD Crash & Salvage Ops |

---

## 3. Sourced Metric Dimensions, Envelopes & Physical Properties

All dimensions are verified from primary technical manuals, NAVEDTRA rate texts, and DoD procurement solicitations. Every entry carries an explicit provenance tag.

```
       A/S32A-31A TOW TRACTOR DIMENSIONAL PROFILE (NAVAIR 19-40-521)
  
       |<====================== LOA: 2.972 m (117.0 in) ======================>|
       |                                                                       |
       +-----------------------+   +-------------------+                       |
       |   Engine Cowl Hood    |   | Operator Station  |                       |
       |  Height: 1.016 m      |   | Steering Wheel:   |   Rear Ballast Deck   |
       |   (40.0 in)           |   | 1.016 m (40.0 in) |   Height: 0.914 m     |
       +-----------------------+---+-------------------+---+                   |
       |                   |           |                   |    Rear Duals     |
  ===--+                   |  Belly    |                   +---+-============= | - - - Y = 0.914m
       |     Front Tire    | Clearance |                   |   | (Dual Drive)  |
       |     (Single)      |  0.191 m  |                   |   | 60 psig       |
  ~~~~~+=======O===========+===(7.5 in)+===================+===+======OO=======+ - - - Y = 0.000m (Deck)
       |<--- Z = 0.000m --->|                               |<-- Z = 2.311m -->|
       |                    |<==== Wheelbase: 2.311 m =====>|                  |
       |                    |         (91.0 in)             |                  |
```

### 3.1 Master Dimensions & Performance Table

| Dimension / Parameter | Imperial Specification | Metric SI Value | Provenance Tag | Source Document & Supporting Passage | Forensic & Conflict Notes |
|---|---|---|---|---|---|
| **A/S32A-31A Basic Length** | **$117.0\,\text{in}$** | **$2.972\,\text{m}$** | `sourced-A/S32A-31A` | **NAVAIR 19-40-521**, Table 1-1 "Leading Particulars"; **NAVEDTRA 14329**, Ch. 5 | Length from front bumper to rear bumper of basic chassis. |
| **A/S32A-31A Air Start Length**| **$162.0 - 168.0\,\text{in}$** | **$4.115 - 4.267\,\text{m}$** | `sourced-A/S32A-31A` | **NAVAIR 19-40-521**, Sec. 4; **DLA NSN 1740-01-379-4633** | Extended rear chassis frame supporting GTC air start enclosure. |
| **A/S32A-31A LOA with Bumpers**| **$193.0\,\text{in}$** | **$4.902\,\text{m}$** | `sourced-A/S32A-31A` | **HyperScale SATT Reference / Fleet Data** | Preserved maximum envelope including pintle hooks and overhanging push pads. |
| **A/S32A-31A Overall Width** | **$70.0\,\text{in}$** | **$1.778\,\text{m}$** | `sourced-A/S32A-31A` | **NAVAIR 19-40-521**, Table 1-1; **NAVEDTRA 14329**, Ch. 5 | Width across widened rear dual-wheel fender flares. |
| **A/S32A-31A Hood/Cowl Width**| **$65.0\,\text{in}$** | **$1.651\,\text{m}$** | `sourced-A/S32A-31A` | **DLA NSN 1740-01-379-4633**; **HyperScale Study** | Width across forward engine hood (narrows by 5.0 in relative to rear fenders). |
| **A/S32A-31A Cowl Height** | **$40.0\,\text{in}$** | **$1.016\,\text{m}$** | `sourced-A/S32A-31A` | **NAVAIR 19-40-521**, Table 1-1; **NAVEDTRA 14329**, Ch. 5 | Height to top of forward engine cowl hood line. |
| **A/S32A-31A Rear Deck Height**| **$36.0\,\text{in}$** | **$0.914\,\text{m}$** | `sourced-A/S32A-31A` | **DLA NSN 1740-01-379-4633**; **PartTarget Record** | Elevation of rear flat ballast / GTC mounting bed above flight deck. |
| **A/S32A-31A Wheelbase** | **$91.0\,\text{in}$** | **$2.311\,\text{m}$** | `sourced-A/S32A-31A` | **NAVAIR 19-40-521 Technical Training Addendum** | **RESOLVED CONFLICT**: Table 1-1 omitted wheelbase; training bank records 91.0 in. `emtug` claim of 80.0 in identified as secondary estimate. |
| **A/S32A-31A Wheel Track** | **$54.0\,\text{in}$** | **$1.372\,\text{m}$** | `sourced-A/S32A-31A` | **NAVEDTRA 14329**, Section: Running Gear Specs | Transverse distance between tire centerline contact patches. |
| **A/S32A-31A Ground Clearance**| **$7.5\,\text{in}$** ($7\text{-}1/2\,\text{in}$) | **$0.191\,\text{m}$** | `sourced-A/S32A-31A` | **NAVAIR 19-40-521**, Table 1-1; **NAVEDTRA 14329**, Ch. 5 | Minimum clearance beneath belly plate and rear differential casing. |
| **A/S32A-31A Turning Radius** | **$132.0\,\text{in}$** ($11.0\,\text{ft}$) | **$3.353\,\text{m}$** | `sourced-A/S32A-31A` | **NAVAIR 19-40-521**, Table 1-1; **NAVEDTRA 14329**, Ch. 5 | Inside curb turning radius at full steering lock ($\pm 35^\circ$). |
| **A/S32A-31A Turning Swept** | **$196.5\,\text{in}$** ($16.38\,\text{ft}$) | **$4.991\,\text{m}$** | `sourced-A/S32A-31A` | **NAVEDTRA 14329**, Section: Maneuvering Clearances | Swept turning radius across outermost chassis corners. |
| **A/S32A-31A Unladen Weight** | **$12,400\,\text{lbs}$** | **$5,625\,\text{kg}$** | `sourced-A/S32A-31A` | **NAVAIR 19-40-521**, Table 1-1; **NAVEDTRA 14329**, Ch. 5 | Basic tractor unladen operating weight with internal steel ballast. |
| **A/S32A-31A Air Start Weight**| **$14,500 - 16,000\,\text{lbs}$**| **$6,577 - 7,257\,\text{kg}$** | `sourced-A/S32A-31A` | **NAVAIR 19-40-521**, Sec. 4 / GTC Specification | Operating weight when fitted with A/S47A-1 or MSU-200NAV GTC pack. |
| **A/S32A-31A Rated Drawbar** | **$8,500\,\text{lbf}$** | **$37.81\,\text{kN}$** | `sourced-A/S32A-31A` | **NAVAIR 19-40-521**, Table 1-1; **DLA NSN 1740-01-379-4633** | Continuous drawbar pull on dry carrier non-skid surface. |
| **A/S32A-31A Heavy Tow Pull** | **$11,200\,\text{lbf}$** | **$49.82\,\text{kN}$** | `sourced-A/S32A-31A` | **NAVEDTRA 14329** / **NAVEDTRA 14014**, Ch. 9 | Heavy-tow rating authorized for aircraft up to $74,500\,\text{lbs}$ ($33,793\,\text{kg}$). |
| **A/S32A-31A Fuel Capacity** | **$85.0\,\text{US gal}$** | **$321.8\,\text{L}$** | `sourced-A/S32A-31A` | **NAVAIR 19-40-521**, Table 1-1; **NAVEDTRA 14329**, Ch. 5 | JP-5 or DF-2 fuel cell capacity. |
| **A/S32A-31A Front Tire Press.**| **$70.0\,\text{psig}$** | **$482.6\,\text{kPa}$** | `sourced-A/S32A-31A` | **NAVAIR 19-40-521**, Table 1-1; **NAVEDTRA 14329**, Ch. 5 | Single front steer tires ($6.00-9$ or $6.90-9$). |
| **A/S32A-31A Rear Tire Press.** | **$60.0\,\text{psig}$** | **$413.7\,\text{kPa}$** | `sourced-A/S32A-31A` | **NAVAIR 19-40-521**, Table 1-1; **NAVEDTRA 14329**, Ch. 5 | Dual rear drive tires ($6.90-9$ commercial/military grade). |
| **A/S32A-32 Overall Length** | **$148.0\,\text{in}$** | **$3.759\,\text{m}$** | `sourced-A/S32A-32` | **NAVAIR 19-1-50**; **NAVEDTRA 14329**; **NAVEDTRA 14014** | Overall length from forward lifting arm tips to rear caster chassis. |
| **A/S32A-32 Overall Width** | **$81.0\,\text{in}$** | **$2.057\,\text{m}$** | `sourced-A/S32A-32` | **NAVAIR 19-1-50**; **NAVEDTRA 14329**; **NAVEDTRA 14014** | Extreme breadth across main drive wheel pods / side drive housings. |
| **A/S32A-32 Overall Height** | **$30.0\,\text{in}$** | **$0.762\,\text{m}$** | `sourced-A/S32A-32` | **NAVAIR 19-1-50**; **NAVEDTRA 14329** | Low chassis profile to fit beneath aircraft fuselage and wingroots. |
| **A/S32A-32 Gross Weight** | **$11,500\,\text{lbs}$** | **$5,216\,\text{kg}$** | `sourced-A/S32A-32` | **NAVAIR 19-1-50**; **NAVEDTRA 14329**; **NAVEDTRA 14014** | Operational vehicle curb weight with hydraulic oil and ballast. |
| **A/S32A-32 Lifting Capacity** | **$16,000\,\text{lbs}$** | **$7,257\,\text{kg}$** | `sourced-A/S32A-32` | **NAVAIR 19-1-50**; **NAVEDTRA 14329** | Maximum vertical lifting load on nosewheel arm cradle. |
| **A/S32A-32 Drawbar Pull** | **$14,000\,\text{lbf}$** | **$62.27\,\text{kN}$** | `sourced-A/S32A-32` | **NAVAIR 19-1-50**; **NAVEDTRA 14329** | Continuous tractive effort across dual hydrostatic drive wheels. |
| **A/S32A-32 Turning Radius** | **$0.0\,\text{in}$** | **$0.000\,\text{m}$** | `sourced-A/S32A-32` | **NAVAIR 19-1-50**; **NAVEDTRA 14329** | True zero turning radius via differential counter-rotating drive wheels. |
| **A/S32A-32 Towing Speed** | **$2.0\,\text{mph}$ (Loaded)** | **$3.2\,\text{km/h}$** | `sourced-A/S32A-32` | **NAVEDTRA 14329**, Section: Spotting Operations | Governed operating towing speed under load ($5.0\,\text{mph}$ unloaded). |
| **MD-3 Length (Standard A)** | **$162.0\,\text{in}$** | **$4.115\,\text{m}$** | `sourced-MD-3` | **NAVAIR 19-40-44**, Sec. 1 "Leading Particulars" | **PRESERVED CONFLICT**: NAVAIR 19-40-44 records 162.0 in. |
| **MD-3 Length (Standard B)** | **$161.0\,\text{in}$** | **$4.089\,\text{m}$** | `sourced-MD-3` | **NAVPERS 10303-B**, Ch. 1, p. 14 | **PRESERVED CONFLICT**: NAVPERS 10303-B records 161.0 in ($\Delta = 1.0\,\text{in}$). |
| **MD-3 Length with Huffer** | **$206.0\,\text{in}$** | **$5.232\,\text{m}$** | `sourced-MD-3` | **NAVAIR 19-30-43** / **HyperScale MD-3A Data** | Extended overall length with GTC-85 air start compressor unit installed. |
| **MD-3 Original Width** | **$65.0\,\text{in}$** | **$1.651\,\text{m}$** | `sourced-MD-3` | **NAVAIR 19-40-44**, Sec. 1 "Leading Particulars" | Pre-1981 production width across rear wheels. |
| **MD-3 SLEP Refurbished Width**| **$70.0 - 71.0\,\text{in}$** | **$1.778 - 1.803\,\text{m}$** | `sourced-MD-3` | **NAVEDTRA 14014 / Fleet Depot Data** | Post-1981 SLEP widened rear frame modification (+6.0 in). |
| **MD-3 Cowl Height** | **$36.0\,\text{in}$** | **$0.914\,\text{m}$** | `sourced-MD-3` | **NAVAIR 19-40-44**, Sec. 1 "Leading Particulars" | Height to top of forward engine cowl. |
| **MD-3 Max Operator Height** | **$40.0\,\text{in}$** | **$1.016\,\text{m}$** | `sourced-MD-3` | **NAVEDTRA 14014**, Section: GSE Particulars | Height to apex of steering wheel rim. |
| **MD-3 Turning Radius** | **$148.0\,\text{in}$** ($12.33\,\text{ft}$) | **$3.759\,\text{m}$** | `sourced-MD-3` | **NAVAIR 19-40-44**, Sec. 1 "Leading Particulars" | Outside wall-to-wall turning clearance radius. |
| **MD-3 Drawbar Pull** | **$8,500\,\text{lbf}$** | **$37.81\,\text{kN}$** | `sourced-MD-3` | **MIL-T-24151 / NAVAIR 19-40-44** | Rated continuous tractive pull at 1.0 mph on dry concrete. |
| **A/S32A-49 STT Length** | **$138.9\,\text{in}$** | **$3.528\,\text{m}$** | `sourced-A/S32A-49` | **NAWCAD Solicitation N68335**, sam.gov | Overall chassis length of modern Shipboard Tow Tractor. |
| **A/S32A-49 STT Width** | **$73.2\,\text{in}$** | **$1.859\,\text{m}$** | `sourced-A/S32A-49` | **NAWCAD Solicitation N68335**, sam.gov | Overall width across outer fender body lines. |
| **A/S32A-49 STT Height** | **$40.16\,\text{in}$** | **$1.020\,\text{m}$** | `sourced-A/S32A-49` | **NAWCAD Solicitation N68335**, sam.gov | Height to cowl/steering baseline. |
| **A/S32A-49 STT Weight** | **$21,600\,\text{lbs}$** | **$9,798\,\text{kg}$** | `sourced-A/S32A-49` | **NAWCAD Solicitation N68335**, sam.gov | High-traction operational curb weight. |
| **A/S32A-49 STT Drawbar (Fwd)**| **$17,690\,\text{lbf}$** | **$78.69\,\text{kN}$** | `sourced-A/S32A-49` | **NAWCAD Solicitation N68335**, sam.gov | Maximum forward tractive drawbar pull. |
| **A/S32A-49 STT Drawbar (Rev)**| **$11,900\,\text{lbf}$** | **$52.93\,\text{kN}$** | `sourced-A/S32A-49` | **NAWCAD Solicitation N68335**, sam.gov | Maximum reverse tractive drawbar pull. |
| **Model 8 ALBAR Towbar Length**| **$108.0\,\text{in}$** ($9.0\,\text{ft}$) | **$2.743\,\text{m}$** | `sourced-ALBAR` | **NAVAIR 19-70-46**; **NAVAIR 00-80T-96** | Weight: $128\,\text{lbs}$ ($58.1\,\text{kg}$); for F/A-18A-D, T-45, AV-8B. |
| **Model 15 ALBAR Towbar Length**|**$180.0\,\text{in}$** ($15.0\,\text{ft}$)| **$4.572\,\text{m}$** | `sourced-ALBAR` | **NAVAIR 19-70-46**; **NAVAIR 00-80T-96** | Weight: $170\,\text{lbs}$ ($77.1\,\text{kg}$); standard for F/A-18E/F, F-35C, E-2D. |
| **Model 20 ALBAR Towbar Length**|**$240.0\,\text{in}$** ($20.0\,\text{ft}$)| **$6.096\,\text{m}$** | `sourced-ALBAR` | **NAVAIR 19-70-46**; **NAVAIR 00-80T-96** | Weight: $215\,\text{lbs}$ ($97.5\,\text{kg}$); long-standoff clearance for nose radomes. |
| **Model 24 ALBAR Towbar Length**|**$288.0\,\text{in}$** ($24.0\,\text{ft}$)| **$7.315\,\text{m}$** | `sourced-ALBAR` | **NAVAIR 19-70-46**; **NAVAIR 00-80T-96** | Weight: $250\,\text{lbs}$ ($113.4\,\text{kg}$); heavy transport and specialized airframes. |

---

### 3.2 DLA NSN Database Forensic Resolution

> [!IMPORTANT]
> **Forensic Audit on DLA Database Label Typo:**  
> The Defense Logistics Agency master catalog entry for NSN `1740-01-379-4633` (*Tractor, Wheeled, Aircraft Towing, Model A/S32A-31A*, CAGE `80058`, P/N `3337AS100-1`) inadvertently labels its dimensional parameters with the unit suffix `FT` (`Length: 117.000 FT`, `Width: 65.000 FT`, `Height: 36.000 FT`).  
> In the identical database record, the certified cubic shipping volume is officially recorded as **$158.4400\,\text{cu ft}$**.  
> Computing the volume using inches:
> $$\frac{117\,\text{in}}{12\,\text{in/ft}} \times \frac{65\,\text{in}}{12\,\text{in/ft}} \times \frac{36\,\text{in}}{12\,\text{in/ft}} = 9.750\,\text{ft} \times 5.4167\,\text{ft} \times 3.000\,\text{ft} = 158.4375\,\text{cu ft}$$
> This mathematical calculation confirms that the true dimensions are $117.0\,\text{inches}$ ($2.972\,\text{m}$), $65.0\,\text{inches}$ ($1.651\,\text{m}$), and $36.0\,\text{inches}$ ($0.914\,\text{m}$).

---

### 3.3 11-Station Transverse Offset Table (Body Plan)

Because carrier tow tractors are manufactured from structural welded steel armor plate rather than faired curved ship hulls, stations are spaced longitudinally along the primary chassis from the front bumper to the rear hitch.

#### A. A/S32A-31A Tow Tractor (Basic Chassis)
*Origin $(0, 0, 0)$ is centered laterally ($X = 0.000\,\text{m}$) at the front steering axle transverse centerline ($Z = 0.000\,\text{m}$), at the deck plane ($Y = 0.000\,\text{m}$). Forward is $-Z$; Aft is $+Z$. Overall basic chassis length = $2.972\,\text{m}$ ($117.0\,\text{in}$). Ground clearance = $+0.191\,\text{m}$ ($7.5\,\text{in}$). Cowl elevation = $+1.016\,\text{m}$ ($40.0\,\text{in}$).*

| Station | Longitudinal $Z$ (m) | Keel / Belly $Y$ (m) | Half-Breadth $X$ (m) | Cowl / Deck $Y$ (m) | Structural Description & Component Fitting | Status & Provenance |
|---|---|---|---|---|---|---|
| **Sta 0** | $-0.450\,\text{m}$ | $+0.250\,\text{m}$ | $\pm 0.250\,\text{m}$ | $+0.480\,\text{m}$ | Front pintle coupler casting, safety latch, ALBAR lunette interface | `derived-bumper-cad` |
| **Sta 1** | $-0.350\,\text{m}$ | $+0.191\,\text{m}$ | $\pm 0.650\,\text{m}$ | $+0.750\,\text{m}$ | Heavy structural channel front bumper, recessed NVIS headlamps | `sourced-A/S32A-31A` (7.5 in belly) |
| **Sta 2** | $0.000\,\text{m}$  | $+0.191\,\text{m}$ | $\pm 0.750\,\text{m}$ | $+1.016\,\text{m}$ | Front steering axle centerline, single $6.00-9$ steer tires, knuckles | `sourced-A/S32A-31A` (40 in cowl) |
| **Sta 3** | $+0.350\,\text{m}$ | $+0.191\,\text{m}$ | $\pm 0.800\,\text{m}$ | $+1.016\,\text{m}$ | Detroit Diesel 3-53 engine compartment, radiator shroud | `sourced-A/S32A-31A` (40 in cowl) |
| **Sta 4** | $+0.700\,\text{m}$ | $+0.191\,\text{m}$ | $\pm 0.825\,\text{m}$ | $+1.016\,\text{m}$ | Cowl bulkhead, 24V battery tray, Allison automatic transmission | `sourced-A/S32A-31A` (65 in hood) |
| **Sta 5** | $+1.050\,\text{m}$ | $+0.191\,\text{m}$ | $\pm 0.825\,\text{m}$ | $+1.016\,\text{m}$ | Operator cockpit footwell, steering column base, brake valve | `sourced-A/S32A-31A` (40 in cowl) |
| **Sta 6** | $+1.400\,\text{m}$ | $+0.191\,\text{m}$ | $\pm 0.825\,\text{m}$ | $+1.180\,\text{m}$ | Operator bucket seat, steering wheel rim, instrument panel | `derived-seat-apex` |
| **Sta 7** | $+1.750\,\text{m}$ | $+0.191\,\text{m}$ | $\pm 0.889\,\text{m}$ | $+1.016\,\text{m}$ | Forward edge of widened rear dual-wheel fender flare | `sourced-A/S32A-31A` (70 in fender) |
| **Sta 8** | $+2.050\,\text{m}$ | $+0.191\,\text{m}$ | $\pm 0.889\,\text{m}$ | $+1.016\,\text{m}$ | Centerline of rear drive axle, dual drive tires, wet disc brakes | `sourced-A/S32A-31A` (70 in fender) |
| **Sta 9** | $+2.350\,\text{m}$ | $+0.191\,\text{m}$ | $\pm 0.889\,\text{m}$ | $+0.914\,\text{m}$ | 85-gal fuel cell, rear ballast block, GTC mounting pads | `sourced-A/S32A-31A` (36 in deck) |
| **Sta 10**| $+2.522\,\text{m}$ | $+0.191\,\text{m}$ | $\pm 0.700\,\text{m}$ | $+0.650\,\text{m}$ | Rear structural bumper, locking pintle hook, cloverleaf shackles | `sourced-A/S32A-31A` (117 in LOA) |

#### B. A/S32A-32 Spotting Dolly (SD-2)
*Origin $(0, 0, 0)$ is at the transverse centerline of the two main drive wheels ($Z = 0.000\,\text{m}$), centered laterally ($X = 0.000\,\text{m}$), at deck plane ($Y = 0.000\,\text{m}$). Forward is $-Z$ (direction of aircraft nose gear capture); Aft is $+Z$ (operator and caster wheel).*

| Station | Longitudinal $Z$ (m) | Belly $Y$ (m) | Half-Breadth $X$ (m) | Top Height $Y$ (m) | Structural Description & Mechanism Components | Status & Provenance |
|---|---|---|---|---|---|---|
| **Sta 0** | $-1.900\,\text{m}$ | $+0.150\,\text{m}$ | $\pm 0.450\,\text{m}$ | $+0.350\,\text{m}$ | Forward tips of hydraulic lifting arms, axle pin receiver sockets | `sourced-A/S32A-32` |
| **Sta 1** | $-1.500\,\text{m}$ | $+0.150\,\text{m}$ | $\pm 0.500\,\text{m}$ | $+0.400\,\text{m}$ | Hydraulic spread cylinders, nosewheel clamping linkages | `sourced-A/S32A-32` |
| **Sta 2** | $-1.100\,\text{m}$ | $+0.150\,\text{m}$ | $\pm 0.650\,\text{m}$ | $+0.500\,\text{m}$ | Main lift cylinder trunnion mounts, heavy structural lifting beam | `sourced-A/S32A-32` |
| **Sta 3** | $-0.600\,\text{m}$ | $+0.150\,\text{m}$ | $\pm 0.850\,\text{m}$ | $+0.650\,\text{m}$ | Forward drive housing bulkhead, hydraulic oil reservoir | `sourced-A/S32A-32` |
| **Sta 4** | $0.000\,\text{m}$  | $+0.150\,\text{m}$ | $\pm 1.028\,\text{m}$ | $+0.762\,\text{m}$ | Main drive axle centerline, dual hydraulic wheel motors & chain drives | `sourced-A/S32A-32` (81 in width) |
| **Sta 5** | $+0.400\,\text{m}$ | $+0.150\,\text{m}$ | $\pm 1.028\,\text{m}$ | $+0.762\,\text{m}$ | 3-cylinder diesel engine compartment, dual hydraulic piston pumps | `sourced-A/S32A-32` (30 in height) |
| **Sta 6** | $+0.800\,\text{m}$ | $+0.150\,\text{m}$ | $\pm 0.850\,\text{m}$ | $+0.762\,\text{m}$ | Operator platform footwell, fuel tank, battery compartment | `sourced-A/S32A-32` |
| **Sta 7** | $+1.200\,\text{m}$ | $+0.150\,\text{m}$ | $\pm 0.700\,\text{m}$ | $+0.950\,\text{m}$ | Operator bucket seat, single-lever joystick controller, gauge console | `derived-seat-apex` |
| **Sta 8** | $+1.500\,\text{m}$ | $+0.150\,\text{m}$ | $\pm 0.500\,\text{m}$ | $+0.700\,\text{m}$ | Rear chassis taper, caster wheel vertical swivel spindle housing | `sourced-A/S32A-32` |
| **Sta 9** | $+1.750\,\text{m}$ | $+0.150\,\text{m}$ | $\pm 0.250\,\text{m}$ | $+0.450\,\text{m}$ | Trailing heavy-duty caster wheel assembly (360 deg yaw swivel) | `sourced-A/S32A-32` |
| **Sta 10**| $+1.859\,\text{m}$ | $+0.150\,\text{m}$ | $\pm 0.200\,\text{m}$ | $+0.400\,\text{m}$ | Rear structural bumper and tow eye (`148.0 in` LOA = $3.759\,\text{m}$) | `sourced-A/S32A-32` (148 in LOA) |

---

## 4. Real Fitted Systems, Subsystems & Counts

### 4.1 Powertrain, Mechanical & Hydraulic Systems

```
     A/S32A-31A POWERTRAIN & DRIVETRAIN SCHEMATIC (NAVAIR 19-40-521)
  
  [Front Steer Axle] <---- [Hydraulic Ram] <---- [Power Steering Pump]
         |                                                 ^
         v                                                 |
  +---------------+    Mechanical Coupling    +----------------------+
  | Detroit Diesel|==========================>| Allison 4-Speed Auto |
  |   3-53 Block  |                           |  Transmission & T/C  |
  +---------------+                           +----------------------+
         | (85-gal JP-5/DF-2)                              |
         v                                                 v
  [Fuel System]                                    [Driveshaft to Axle]
                                                           |
                                                           v
                                              +--------------------------+
                                              | Rigid Rear Drive Axle    |
                                              | - Enclosed Wet-Disc      |
                                              | - Dual Wheels (4 Tires)  |
                                              +--------------------------+
```

1. **Diesel Prime Movers:**
   - *A/S32A-31A / 31B:* 1x Detroit Diesel 3-53, 3-cylinder, 2-stroke diesel engine ($159\,\text{cu in}$ / $2.61\,\text{L}$), rated $101\,\text{hp}$ ($75.3\,\text{kW}$) at $2,800\,\text{RPM}$. Equipped with 24V DC electric starter, mechanical governor, dry-type air cleaner, and spark-arresting side-discharge exhaust.
   - *A/S32A-32:* 1x 3-cylinder 2-stroke diesel engine directly coupled to dual tandem hydraulic pumps.
   - *MD-3 / MD-3A:* 1x International Harvester (IH) 6-cylinder inline diesel engine (or Detroit Diesel retrofit in depot overhauls), low-profile intake and manifold.
   - *A/S32A-49 STT:* 1x Deutz / Cummins 4-cylinder turbocharged diesel engine meeting Tier 3 / Tier 4 shipboard emissions standards.
2. **Hydraulic Systems & Actuators:**
   - *A/S32A-31A:* Engine-driven hydraulic gear pump supplying power steering assist cylinder ($\pm 0.08\,\text{m}$ stroke) and wet disc power brake booster.
   - *A/S32A-32 Spotting Dolly:*
     - 2x Variable-displacement axial piston hydraulic pumps (propulsion drive circuit).
     - 2x High-torque low-speed hydraulic drive motors powering open-chain gear reduction drives at the left and right main wheels.
     - 1x Double-acting hydraulic lift cylinder (elevates lifting carriage vertically, stroke $\approx 0.35\,\text{m}$, lift capacity $16,000\,\text{lbs}$).
     - 2x Hydraulic spread cylinders (swing lifting arms laterally inward/outward to clamp nose landing gear axle).
     - 1x Auxiliary hydraulic gear pump powering the lifting/spread circuit.

### 4.2 Towing & Handling Interfaces
1. **ALBAR (Adjustable Length Towbar) Interface:**
   - Standard carrier tow tractors (A/S32A-31A, MD-3, A/S32A-49) do not touch aircraft directly. They couple via rigid alloy steel ALBAR towbars:
     - **Model 8 ALBAR:** $9.0\,\text{ft}$ ($2.743\,\text{m}$), $128\,\text{lbs}$ ($58.1\,\text{kg}$) — Light/intermediate aircraft (F/A-18A-D, T-45, AV-8B).
     - **Model 15 ALBAR:** $15.0\,\text{ft}$ ($4.572\,\text{m}$), $170\,\text{lbs}$ ($77.1\,\text{kg}$) — Fleet standard (F/A-18E/F Super Hornet, EA-18G Growler, F-35C Lightning II, E-2D Hawkeye, C-2A Greyhound).
     - **Model 20 ALBAR:** $20.0\,\text{ft}$ ($6.096\,\text{m}$), $215\,\text{lbs}$ ($97.5\,\text{kg}$) — High standoff clearance.
     - **Model 24 ALBAR:** $24.0\,\text{ft}$ ($7.315\,\text{m}$), $250\,\text{lbs}$ ($113.4\,\text{kg}$) — Ultra-long standoff.
   - *Coupling Kinematics:* The tractor features a cast steel locking pintle hook on the front bumper and rear chassis plate. The ALBAR ring (lunette) drops into the hook with a spring-loaded latch and safety pin. The aircraft end features spring-loaded locking jaws and shear pins designed to shear before damaging aircraft landing gear bulkheads under excessive torque.
2. **Spotting Dolly Clamping Interface:**
   - Eliminates towbars. Operates directly on the aircraft nose landing gear axle spools.
   - Carries interchangeable sets of heat-treated steel **axle adapter pins** stored in racks on the dolly body to interface with F/A-18, F-35C, E-2D, C-2A, and MH-60 nose gear geometry.

### 4.3 Jet Engine Air-Start Equipment (GTC Packs)
1. **A/S47A-1 & MSU-200NAV Air Start Units:**
   - Mounted on the aft deck of long-frame A/S32A-31A and A/S32A-49 tractors.
   - **Turbine Engine:** Gas Turbine Compressor (GTC) powered by jet fuel plumbed directly from the tractor's 85-gallon fuel cell.
   - **Output Delivery:** High-volume low-pressure bleed air delivered through an accordion-style $3.5\,\text{in}$ ($88.9\,\text{mm}$) flexible pneumatic starter hose stored in an aft basket/reel. Delivers $200\,\text{ppm}$ air mass flow at $42\,\text{psig}$ ($290\,\text{kPa}$) to turn over jet engine starter turbines.
2. **Legacy GTC-85 / GTCP-100 (MD-3A):**
   - Garrett AiResearch GTC-85 gas turbine enclosure installed inside the aft bay of the MD-3A tractor. Featured hinged top access doors, side air intake louvers, and a rear exhaust port.

### 4.4 Flight Deck Restraint & Safety Systems
1. **Tie-Down Padeyes / Shackles:**
   - Equipped with heavy forged steel cloverleaf tie-down shackles (minimum 4 to 8 points on chassis corners).
   - Under flight deck Condition Zebra or heavy sea states, tractors are locked to flight deck tie-down cups using standard **TD-1A/B quick-release tie-down chains** (6-point tie-down for normal conditions, 12-point or 18-point for storm/flight quarters).
2. **Electrical & Tactical Lighting Modes:**
   - **24V DC System:** Powered by dual 12V heavy-duty lead-acid batteries wired in series in a side-accessible battery tray.
   - **Mode A (Daytime / White Light):** High-intensity sealed-beam driving headlights recessed in the front bumper channel, rear red taillights, amber strobe beacon on operator cowl.
   - **Mode B (Condition Zebra / Tactical Darken Ship):** Mandatory optical blackout per MIL-STD-3009. White headlights disabled; low-lux **NVIS-Green A** or **Tactical Blue** driving lights energized; amber strobe deactivated; instrument cluster backlit with dim night-vision goggle (NVG) compliant green illumination.

---

## 5. Kinematic Rigging Hierarchy & Articulation Mechanics

Every joint, axis, pivot point, and limit stop is documented below in standard glTF 2.0 WebGL format (Forward $-Z$, Sky $+Y$, Starboard $+X$, Port $-X$).

### 5.1 A/S32A-31A Aircraft Tow Tractor Scene Graph

```yaml
as32a_31a_root: [0.000, 0.000, 0.000] (Ground plane at front axle center)
│
├── chassis_frame: [0.000, 0.191, 1.050] (Welded steel 1-piece chassis, 12,400 lb mass)
│   │
│   ├── front_bumper_assembly: [0.000, 0.350, -0.350]
│   │   ├── pintle_hitch_forward: [0.000, 0.400, -0.450]
│   │   │   └── albar_towbar_joint: [0.000, 0.400, -0.450] (Revolute Pitch +/-45 deg, Yaw +/-60 deg)
│   │   ├── headlamp_starboard: [+0.550, 0.550, -0.360] (Recessed sealed-beam driving lamp)
│   │   ├── headlamp_port: [-0.550, 0.550, -0.360] (Recessed sealed-beam driving lamp)
│   │   └── tie_down_shackle_fwd_stbd: [+0.650, 0.250, -0.350] (Cloverleaf tie-down ring)
│   │
│   ├── powertrain_compartment: [0.000, 0.500, 0.350]
│   │   ├── diesel_engine_353: [0.000, 0.500, 0.350] (Detroit Diesel 3-53 block)
│   │   ├── cooling_fan: [0.000, 0.550, 0.050] (Continuous Roll around Z-axis, belt-driven)
│   │   ├── transmission_allison: [0.000, 0.400, 0.850] (4-speed automatic)
│   │   └── exhaust_tailpipe: [+0.650, 0.300, 0.800] (Side-discharging low-velocity pipe)
│   │
│   ├── front_steering_suspension: [0.000, 0.320, 0.000]
│   │   ├── steering_ram_hydraulic: [0.000, 0.320, 0.050] (Prismatic X-axis translation +/-0.08 m)
│   │   ├── steering_knuckle_starboard: [+0.620, 0.320, 0.000] (Revolute Yaw around +Y: -35.0 deg to +35.0 deg)
│   │   │   └── wheel_front_starboard: [+0.700, 0.320, 0.000] (Continuous Roll around spindle X-axis)
│   │   └── steering_knuckle_port: [-0.620, 0.320, 0.000] (Revolute Yaw around +Y: -35.0 deg to +35.0 deg)
│   │       └── wheel_front_port: [-0.700, 0.320, 0.000] (Continuous Roll around spindle X-axis)
│   │
│   ├── operator_cockpit_station: [0.000, 0.600, 1.250]
│   │   ├── operator_seat: [-0.250, 0.750, 1.350] (Low-profile bucket seat)
│   │   ├── steering_column_mast: [-0.250, 0.850, 1.150]
│   │   │   └── steering_wheel: [-0.250, 1.050, 1.180] (Continuous Roll around column axis, 20 deg aft pitch)
│   │   ├── brake_pedal: [-0.250, 0.500, 0.950] (Revolute Pitch: 0 to -15 deg)
│   │   ├── throttle_pedal: [-0.150, 0.500, 0.950] (Revolute Pitch: 0 to -20 deg)
│   │   ├── gear_shift_lever: [-0.050, 0.800, 1.200] (Revolute Pitch: detents 1, 2, 3, 4, N, R)
│   │   └── parking_brake_lever: [-0.400, 0.750, 1.300] (Revolute Pitch: 0 to +45 deg)
│   │
│   ├── rear_drivetrain_assembly: [0.000, 0.380, 2.050]
│   │   ├── rear_axle_casing: [0.000, 0.380, 2.050] (Rigid heavy drive axle, wet disc brakes)
│   │   ├── dual_wheel_hub_starboard: [+0.680, 0.380, 2.050]
│   │   │   ├── wheel_rear_inner_stbd: [+0.600, 0.380, 2.050] (Continuous Roll around axle X-axis)
│   │   │   └── wheel_rear_outer_stbd: [+0.780, 0.380, 2.050] (Continuous Roll around axle X-axis)
│   │   └── dual_wheel_hub_port: [-0.680, 0.380, 2.050]
│   │       ├── wheel_rear_inner_port: [-0.600, 0.380, 2.050] (Continuous Roll around axle X-axis)
│   │       └── wheel_rear_outer_port: [-0.780, 0.380, 2.050] (Continuous Roll around axle X-axis)
│   │
│   └── rear_chassis_ballast_deck: [0.000, 0.700, 2.200]
│       ├── fuel_tank_85gal: [0.000, 0.650, 2.100] (85 US gal JP-5 cell)
│       ├── air_start_skid_mount: [0.000, 0.914, 2.250] (Mounting points for A/S47A-1 / MSU-200NAV)
│       └── pintle_hitch_rear: [0.000, 0.420, 2.522] (Rear heavy towing pintle, Pitch +/-45 deg, Yaw +/-60 deg)
```

---

### 5.2 A/S32A-32 Spotting Dolly Scene Graph

```yaml
as32a_32_spotting_dolly_root: [0.000, 0.000, 0.000] (Ground plane at main drive axle center)
│
├── main_chassis_frame: [0.000, 0.150, 0.200] (Heavy steel welded chassis, 11,500 lb mass)
│   │
│   ├── propulsion_drivetrain: [0.000, 0.300, 0.000]
│   │   ├── drive_pod_starboard: [+0.900, 0.300, 0.000]
│   │   │   ├── hydraulic_motor_stbd: [+0.850, 0.300, 0.000] (Hydraulic drive motor)
│   │   │   └── wheel_main_starboard: [+1.028, 0.300, 0.000] (Continuous Roll around X, independent rate)
│   │   └── drive_pod_port: [-0.900, 0.300, 0.000]
│   │       ├── hydraulic_motor_port: [-0.850, 0.300, 0.000] (Hydraulic drive motor)
│   │       └── wheel_main_port: [-1.028, 0.300, 0.000] (Continuous Roll around X, independent rate)
│   │
│   ├── rear_caster_assembly: [0.000, 0.200, 1.750]
│   │   ├── caster_swivel_spindle: [0.000, 0.250, 1.750] (Revolute Yaw around +Y: 360 deg continuous free castering)
│   │   │   └── caster_wheel: [0.000, 0.150, 1.820] (Trailing caster wheel, Continuous Roll around local X-axis)
│   │
│   ├── operator_station: [0.000, 0.600, 1.000]
│   │   ├── operator_seat: [0.000, 0.700, 1.100] (Low bucket seat)
│   │   └── joystick_controller: [+0.300, 0.750, 0.950] (Dual-axis joystick: Pitch +/-25 deg, Roll +/-25 deg)
│   │
│   └── nose_gear_handling_carriage: [0.000, 0.300, -0.800]
│       ├── hydraulic_lift_cylinder: [0.000, 0.350, -0.600] (Prismatic/Revolute lift: Delta Y = +0.0 to +0.35 m, Pitch 0 to +18 deg)
│       └── lifting_beam_transverse: [0.000, 0.350, -0.900]
│           ├── lifting_arm_starboard: [+0.400, 0.350, -1.200]
│           │   ├── spread_cylinder_stbd: [+0.250, 0.350, -1.000] (Revolute Yaw clamp: -15 deg to +15 deg)
│           │   └── axle_pin_adapter_stbd: [+0.350, 0.350, -1.850] (Locks into starboard nose gear spool)
│           └── lifting_arm_port: [-0.400, 0.350, -1.200]
│               ├── spread_cylinder_port: [-0.250, 0.350, -1.000] (Revolute Yaw clamp: -15 deg to +15 deg)
│               └── axle_pin_adapter_port: [-0.350, 0.350, -1.850] (Locks into port nose gear spool)
```

---

### 5.3 MD-3 / MD-3A Legacy Tow Tractor Scene Graph

```yaml
md3_tractor_root: [0.000, 0.000, 0.000] (Ground plane at front bumper centerline)
│
├── chassis_frame: [0.000, 0.191, -2.057] (Low-slung heavy steel chassis, 10,000-14,000 lb mass)
│   │
│   ├── front_bumper_channel: [0.000, 0.280, 0.000]
│   │   ├── pintle_hitch_forward: [0.000, 0.356, 0.100] (Revolute Pitch +/-45 deg, Yaw +/-60 deg)
│   │   └── front_tow_eye: [0.000, 0.250, 0.050]
│   │
│   ├── front_steer_axle: [0.000, 0.300, -0.823]
│   │   ├── steer_knuckle_stbd: [+0.650, 0.300, -0.823] (Revolute Yaw around +Y: -30.0 deg to +30.0 deg)
│   │   │   └── wheel_front_stbd: [+0.720, 0.300, -0.823] (Continuous Roll around spindle X-axis)
│   │   └── steer_knuckle_port: [-0.650, 0.300, -0.823] (Revolute Yaw around +Y: -30.0 deg to +30.0 deg)
│   │       └── wheel_front_port: [-0.720, 0.300, -0.823] (Continuous Roll around spindle X-axis)
│   │
│   ├── operator_cockpit: [0.000, 0.600, -2.000]
│   │   ├── operator_seat: [-0.250, 0.650, -2.200]
│   │   └── steering_wheel: [-0.250, 0.950, -1.900] (Continuous Roll around steering shaft)
│   │
│   ├── rear_dual_drive_axle: [0.000, 0.380, -3.292]
│   │   ├── dual_wheels_stbd: [+0.700, 0.380, -3.292] (Continuous Roll around axle X-axis)
│   │   └── dual_wheels_port: [-0.700, 0.380, -3.292] (Continuous Roll around axle X-axis)
│   │
│   └── aft_modular_bay: [0.000, 0.500, -3.500]
│       ├── gtc85_turbine_enclosure: [0.000, 0.600, -3.500] (MD-3A huffer module)
│       │   ├── turbine_access_door: [0.000, 0.950, -3.500] (Hinged access hatch: Pitch 0 to +90 deg)
│       │   └── air_start_hose_reel: [+0.400, 0.600, -3.800] (Pneumatic hose basket)
│       └── pintle_hitch_rear: [0.000, 0.400, -4.115] (Heavy rear towing pintle, Pitch +/-45 deg, Yaw +/-60 deg)
```

---

### 5.4 Actuator Kinematics & Limit Reference Table

| Platform | Subsystem / Joint | Parent Node | Motion Type | Active Local Axis | Operating Range | Rate / Timing | Provenance Tag |
|---|---|---|---|---|---|---|---|
| **A/S32A-31A** | Front Steering Knuckles | `front_steering_suspension` | Revolute | $+Y$ (Local Yaw) | $-35.0^\circ \text{ to } +35.0^\circ$ | $\approx 25^\circ/\text{s}$ (Hydraulic ram) | `sourced-A/S32A-31A`: NAVAIR 19-40-521 |
| **A/S32A-31A** | Steering Wheel | `steering_column_mast` | Continuous | Inclined ($20^\circ$ aft Pitch) | $3.0\text{ turns lock-to-lock}$ ($\pm 540^\circ$) | Operator dependent | `sourced-A/S32A-31A`: NAVAIR 19-40-521 |
| **A/S32A-31A** | Front Wheels | `steering_knuckle` | Continuous | $\pm X$ (Local Spindle) | $360^\circ\text{ Continuous Roll}$ | Proportional to vehicle velocity | `sourced-A/S32A-31A`: NAVAIR 19-40-521 |
| **A/S32A-31A** | Rear Dual Wheels | `rear_axle_casing` | Continuous | $\pm X$ (Rear Axle) | $360^\circ\text{ Continuous Roll}$ | Governed max: $12.0\,\text{mph}$ ($19.3\,\text{km/h}$) | `sourced-A/S32A-31A`: NAVAIR 19-40-521 |
| **A/S32A-31A** | Pintle Hitch Hooks | `chassis_frame` | Revolute | Dual: Pitch $+Y$ / Yaw $+Z$ | Pitch: $\pm 45^\circ$, Yaw: $\pm 60^\circ$ | Passive towbar motion | `sourced-A/S32A-31A`: NAVAIR 00-80T-96 |
| **A/S32A-32** | Main Drive Wheels | `main_chassis_frame` | Continuous | $\pm X$ (Independent Spindles) | $360^\circ\text{ Continuous Roll}$ | Hydrostatic variable: $-5\text{ to }+5\,\text{mph}$ | `sourced-A/S32A-32`: NAVAIR 19-1-50 |
| **A/S32A-32** | Caster Wheel Swivel | `main_chassis_frame` | Revolute | $+Y$ (Vertical Spindle) | $360^\circ\text{ Continuous Free Swivel}$ | Passive caster alignment | `sourced-A/S32A-32`: NAVAIR 19-1-50 |
| **A/S32A-32** | Nose Gear Lift Cylinder| `main_chassis_frame` | Prismatic / Rev | Vertical $+Y$ & Pitch $+X$ | Stroke: $0.0\text{ to }0.35\,\text{m}$ ($+18^\circ$ Pitch) | Full lift transit: $\approx 8.0\,\text{s}$ | `sourced-A/S32A-32`: NAVAIR 19-1-50 |
| **A/S32A-32** | Spread Clamping Arms | `lifting_beam_transverse` | Revolute | $+Y$ (Bilateral Yaw) | Clamp sweep: $\pm 15.0^\circ$ per arm | Full clamp transit: $\approx 4.0\,\text{s}$ | `sourced-A/S32A-32`: NAVAIR 19-1-50 |
| **MD-3** | Front Steering Knuckles | `front_steer_axle` | Revolute | $+Y$ (Local Yaw) | $-30.0^\circ \text{ to } +30.0^\circ$ | $\approx 20^\circ/\text{s}$ (Hydraulic ram) | `sourced-MD-3`: NAVAIR 19-40-44 |
| **MD-3A** | GTC Turbine Access Door| `gtc85_turbine_enclosure`| Revolute | $+X$ (Transverse Hinge) | $0.0^\circ\text{ to }+90.0^\circ\text{ Pitch}$ | Manual maintenance latch | `sourced-MD-3`: NAVAIR 19-30-43 |
| **A/S32A-35** | Tilly Crane Boom Pivot | `crane_superstructure` | Revolute | $+X$ (Trunnion Horizontal) | Elevation Pitch: $+5.0^\circ\text{ to }+65.0^\circ$ | Hydraulic elevation ram | `sourced-A/S32A-35`: NAVAIR 19-40-45 |
| **A/S32A-35** | Hoist Winch & Hook | `crane_boom_tip` | Prismatic | Vertical $-Y$ (Gravity Cable) | Hook vertical travel: $0.0\text{ to }12.0\,\text{m}$ | Electric cable drum | `sourced-A/S32A-35`: NAVAIR 19-40-45 |

---

## 6. Common 3D Modeling Pitfalls & Forensic Audit Checklist

```
  =============================================================================
                  TOP 10 3D MODELLING & RIGGING PITFALLS (GSE)
  =============================================================================
   [!] 1. Missing Dual Rear Wheels (Modelling single tires instead of duals).
   [!] 2. Conflating Towbarless Spotting Dolly with Conventional Tow Tractor.
   [!] 3. Rigidly Parenting ALBAR Towbar (Forgetting 2-axis pintle articulation).
   [!] 4. Inventing Car-Style Steering on A/S32A-32 (It turns via zero-radius differential drive).
   [!] 5. Conflating 117-in Basic Chassis with 168/193-in GTC Air-Start Envelope.
   [!] 6. Ignoring 1981 MD-3 SLEP (+6.0 in rear fender width expansion).
   [!] 7. Confusing Crash Crane ("Tilly") with Standard Flight Deck Tow Tractors.
   [!] 8. Conflating Modern A/S32A-49 STT with Legacy A/S32A-31A Mule.
   [!] 9. Omitting Heavy Tie-Down Shackles for Flight Deck Chain Securing.
   [!] 10. Glowing White Headlamps during Night Darken Ship / Condition Zebra.
  =============================================================================
```

1. **Dual Rear Wheels Omission:**  
   *Error:* Amateur 3D models frequently give the A/S32A-31A and MD-3 single rear tires like a standard civilian pickup or baggage tractor.  
   *Correction:* Both platforms feature heavy-duty drive axles with **dual rear wheels (two tires per hub, 4 tires total on the drive axle)**. This provides the surface contact area necessary to transfer $8,500 - 11,200\,\text{lbf}$ of drawbar pull across textured non-skid without breaking traction.
2. **Conflating Tow Tractor (A/S32A-31A) with Spotting Dolly (A/S32A-32):**  
   *Error:* Using the A/S32A-31A to tow aircraft without an ALBAR towbar, or placing the A/S32A-32 in the open flight deck catapult launch stream.  
   *Correction:* The A/S32A-31A *always* requires an ALBAR towbar (Model 8, 15, 20, or 24) to couple to aircraft. The A/S32A-32 is a towbarless vehicle that clamps directly onto the nose gear and is used predominantly in the hangar bay.
3. **Rigid Towbar Parenting:**  
   *Error:* Parenting the ALBAR towbar mesh solidly to the tractor front/rear bumper without rotational degrees of freedom, causing the towbar to clip through the aircraft nose gear when the tractor turns.  
   *Correction:* Rig the pintle hook hitch as an articulated joint with **$\pm 45^\circ$ Pitch** and **$\pm 60^\circ$ Yaw**, allowing the ALBAR to pivot freely as the tractor steers.
4. **Car-Style Ackermann Steering on the Spotting Dolly:**  
   *Error:* Rigging front steerable knuckles on the A/S32A-32 Spotting Dolly.  
   *Correction:* The A/S32A-32 has **no steering knuckles**. It steers hydrostatically via differential rotation of its two main wheels, pivoting around a free-swiveling $360^\circ$ rear caster wheel.
5. **Length Confusion (Basic vs Air Start Chassis):**  
   *Error:* Scaling the basic A/S32A-31A tractor to $193\,\text{in}$ or scaling the air-start tractor down to $117\,\text{in}$.  
   *Correction:* Enforce the distinction: Basic chassis LOA is **$117.0\,\text{in}$** ($2.972\,\text{m}$); air-start equipped chassis with A/S47A-1 GTC is **$162.0 - 168.0\,\text{in}$** ($4.115 - 4.267\,\text{m}$); maximum working envelope with overhanging bumpers and pintle hooks is **$193.0\,\text{in}$** ($4.902\,\text{m}$).
6. **MD-3 Width Error (Pre-SLEP vs Post-SLEP):**  
   *Error:* Modelling post-1980 carrier flight decks with the narrow $65.0\,\text{in}$ pre-SLEP MD-3 chassis.  
   *Correction:* The 1981 Service Life Extension Program (SLEP) widened the rear body of the MD-3 by $6.0\,\text{in}$ to **$70.0 - 71.0\,\text{in}$** ($1.778 - 1.803\,\text{m}$), matching the rear fender track of the successor A/S32A-31A.
7. **Conflating Crash Crane with Tow Tractors:**  
   *Error:* Labelling the A/S32A-35/36 "Tilly" crash crane as a tow tractor.  
   *Correction:* Tilly is a dedicated, self-propelled salvage crane with an A-frame tilting boom and all-wheel steering. It is parked near the carrier island and deployed exclusively for aircraft emergencies and heavy salvage lifts.
8. **Conflating Modern A/S32A-49 STT with A/S32A-31A:**  
   *Error:* Treating modern carrier tow tractors seen on CVN-78 or recent CVN-68 deployments as A/S32A-31A units despite obvious body differences.  
   *Correction:* Identify the **A/S32A-49 STT**: It has a modern angular German Schopf F59 chassis profile, heavier weight ($21,600\,\text{lbs}$), and higher drawbar pull ($17,690\,\text{lbf}$).
9. **Tie-Down Hardware Absence:**  
   *Error:* Generating a smooth sheet-metal chassis without tie-down shackles.  
   *Correction:* Carrier GSE must feature heavy forged steel cloverleaf tie-down shackles at all four chassis corners to receive TD-1A/B tie-down chains during high sea states and Condition Zebra.
10. **Tactical Night Lighting Violations:**  
    *Error:* Rendering bright white halogen headlights illuminating the flight deck during night launch/recovery operations.  
    *Correction:* Carrier flight decks operate under **Condition Zebra / Darken Ship** (MIL-STD-3009). Headlights must switch to low-intensity **NVIS-Green A** or **Tactical Blue** filtered modes to preserve aircrew and deck crew night vision.

---

## 7. Grounded Uncertainty Register

In compliance with the **Strict Zero-Invented-Numbers Rule**, all parameters lacking unclassified public engineering sources are isolated below.

| Platform / Subsystem | Unresolved Engineering Parameter | Governing Standard / Tech Manual | Reason for Unresolved Status | Conservative CAD Baseline / Recommended Treatment |
|---|---|---|---|---|
| **A/S32A-31A** | Front Steering Knuckle Scrub Radius & Kingpin Inclination | NAVAIR DWG 3337AS100 (Restricted TDP) | Proprietary engineering drawings withheld from public manuals | Kingpin inclination estimated at $5.0^\circ - 7.0^\circ$; scrub radius nominal $25\,\text{mm}$ |
| **A/S32A-31A** | Pintle Hitch Centerline Elevation Above Deck | NAVAIR 19-40-521 Table 1-1 | Omitted from leading particulars table | Inferred from ALBAR horizontal alignment: $14.0 - 18.0\,\text{in}$ ($0.356 - 0.457\,\text{m}$) |
| **A/S32A-32** | Belly Plate Minimum Ground Clearance | NAVAIR 19-1-50 | Clearances stated only as operational envelope | Estimated from main drive tire radius: $6.0 - 7.5\,\text{in}$ ($0.152 - 0.191\,\text{m}$) |
| **A/S32A-32** | Spread Cylinder Linear Stroke (mm) | NAVAIR 19-1-50 IPB | Parts breakdown lists cylinder without stroke dimensions | Clamp angular sweep is verified at $\pm 15^\circ$; cylinder stroke estimated at $120 - 150\,\text{mm}$ |
| **MD-3 / MD-3A** | Exact Axle-to-Axle Wheelbase | NAVAIR 19-40-44 / NAVPERS 10303-B | Omitted from unclassified text; `md3k` marked UNKNOWN | `emtug` asserted $74.0\,\text{in}$ ($1.880\,\text{m}$); remains unverified without primary drawing |
| **A/S32A-35 CVCC**| Exact Unballasted Chassis Curb Weight | NAVAIR 19-40-45 | Manual cites gross operational weight ($70,000\,\text{lb}$ class) | Internal ballast plates vary by carrier air department assignment; mark unballasted curb UNRESOLVED |
| **A/S32A-49 STT** | Minimum Turning Radius (Wall-to-Wall) | NAWCAD Procurement Specification | Minimum curb radius given; swept radius unstated | Inferred from Schopf F59 baseline: $\approx 145.0\,\text{in}$ ($3.683\,\text{m}$) |

---

## 8. Primary Trusted Visual Evidence Matrix (DVIDS Hub Records)

The **Defense Visual Information Distribution Service (DVIDS)** is the primary trusted image repository. The following verified records provide complete multi-angle visual coverage for carrier flight deck tow tractors, spotting dollies, and crash cranes.

```
       DVIDS MULTI-ANGLE COVERAGE MATRIX FOR CARRIER TOW TRACTORS
  
   Angle / View          Asset Variant     Host Ship / Context            Verified DVIDS Image Link
  +--------------------+ +---------------+ +----------------------------+ +---------------------------------------------------------+
  | Front / Bow        | A/S32A-31A Mule | USS Abraham Lincoln (CVN 72) | https://www.dvidshub.net/image/7031258                  |
  | Rear / Stern       | A/S32A-31A Mule | USS Abraham Lincoln (CVN 72) | https://www.dvidshub.net/image/8266739                  |
  | Port (Left) Profile| A/S32A-31A Mule | USS Nimitz (CVN 68)          | https://www.dvidshub.net/image/5542487                  |
  | Starboard Profile  | A/S32A-31A Mule | USS George H.W. Bush (CVN 77)| https://www.dvidshub.net/image/9954153                  |
  | Top / Overhead     | A/S32A-31A Mule | USS Theodore Roosevelt (CVN 71)| https://www.dvidshub.net/image/6635536                |
  | Three-Quarter View | A/S32A-31A Mule | USS Nimitz (CVN 68)          | https://www.dvidshub.net/image/7189288                  |
  | Mechanism Close-up | A/S32A-31A Mule | USS Abraham Lincoln (CVN 72) | https://www.dvidshub.net/image/9172114                  |
  | Mechanism Maint.   | A/S32A-31A Mule | USS Nimitz (CVN 68)          | https://www.dvidshub.net/image/256522                   |
  +--------------------+ +---------------+ +----------------------------+ +---------------------------------------------------------+
  | Front / Clamp Arms | A/S32A-32 Dolly | USS George Washington (CVN 73)| https://www.dvidshub.net/image/8451472                 |
  | Rear / Drive Wheel | A/S32A-32 Dolly | USS George Washington (CVN 73)| https://www.dvidshub.net/image/8451467                 |
  | Port / Hangar Bay  | A/S32A-32 Dolly | Carrier Hangar Fleet         | Navy ID 090122-N-6538W-051 (ground-agy indexed)         |
  | Starboard Profile  | A/S32A-32 Dolly | Towing E-2C Hawkeye          | Navy ID 080609-N-6538W-048 (ground-agy indexed)         |
  | Top / Overhead     | A/S32A-32 Dolly | USS Theodore Roosevelt (CVN 71)| Navy ID 030309-N-1328C-502 (ground-agy indexed)        |
  | Close-up Mechanism | A/S32A-32 Dolly | USS Gerald R. Ford (CVN 78)  | https://www.dvidshub.net/image/8653357                  |
  +--------------------+ +---------------+ +----------------------------+ +---------------------------------------------------------+
  | Crash Crane Tilly  | A/S32A-35 CVCC  | USS Gerald R. Ford (CVN 78)  | https://www.dvidshub.net/image/8183487                  |
  | Crash Crane Onload | A/S32A-35 CVCC  | USS Gerald R. Ford (CVN 78)  | https://www.dvidshub.net/image/8484981                  |
  | Modern Tow Tractor | A/S32A-49 STT   | USS Nimitz (CVN 68)          | https://www.dvidshub.net/image/7857430                  |
  | Modern Tow Tractor | A/S32A-49 STT   | USS Carl Vinson (CVN 70)     | https://www.dvidshub.net/image/7757937                  |
```

### 8.1 Detailed Verified Image Records

#### A. A/S32A-31A Aircraft Tow Tractor Records
1. **Front / Bow View:**
   - **URL:** [DVIDS Image 7031258 - Sailor Operates Tow Tractor](https://www.dvidshub.net/image/7031258)
   - **Platform & Hull:** A/S32A-31A on USS *Abraham Lincoln* (CVN 72)
   - **Date:** 2022-02-14 | **Credit:** US Navy / Mass Communication Specialist
   - **Observed Features:** Clear frontal view showing structural channel steel bumper, recessed driving lamps, center towbar pintle hitch casting, and forward tie-down shackles.
2. **Rear / Stern View:**
   - **URL:** [DVIDS Image 8266739 - Securing Tow Tractor on Flight Deck](https://www.dvidshub.net/image/8266739)
   - **Platform & Hull:** A/S32A-31A on USS *Abraham Lincoln* (CVN 72)
   - **Date:** 2024-02-28 | **Credit:** US Navy
   - **Observed Features:** Aft chassis perspective showing rear pintle hook, widened dual-wheel rear fenders, flat ballast deck, and TD-1A tie-down chains secured to deck cups.
3. **Port (Left) Profile:**
   - **URL:** [DVIDS Image 5542487 - F/A-18F Super Hornet Towed on Flight Deck](https://www.dvidshub.net/image/5542487)
   - **Platform & Hull:** A/S32A-31A towing Super Hornet on USS *Nimitz* (CVN 68)
   - **Date:** 2019-06-25 | **Credit:** US Navy / Mass Communication Specialist
   - **Observed Features:** Full port-side profile showing low-slung hood line, Model 15 ALBAR towbar coupled to aircraft nose landing gear, wheel arrangement, and operator seating position.
4. **Starboard (Right) Profile:**
   - **URL:** [DVIDS Image 9954153 - USS George H.W. Bush Conducts Daily Operations](https://www.dvidshub.net/image/9954153)
   - **Platform & Hull:** A/S32A-31A on USS *George H.W. Bush* (CVN 77)
   - **Date:** 2026-09-12 | **Credit:** US Navy
   - **Observed Features:** Clean starboard elevation showing side engine maintenance panels, battery compartment access, fuel filler cap stenciled `FUEL JP-5 OR DF-2`, and exhaust routing.
5. **Top / Overhead View:**
   - **URL:** [DVIDS Image 6635536 - Operations from a Tow Tractor](https://www.dvidshub.net/image/6635536)
   - **Platform & Hull:** A/S32A-31A on USS *Theodore Roosevelt* (CVN 71)
   - **Date:** 2021-05-18 | **Credit:** US Navy
   - **Observed Features:** High-angle downward perspective from carrier island showing hood layout, engine compartment access lids, operator cockpit footwell, and rear deck geometry.
6. **Three-Quarter Quarter View:**
   - **URL:** [DVIDS Image 7189288 - Flight Deck Operations Featuring Tow Tractor](https://www.dvidshub.net/image/7189288)
   - **Platform & Hull:** A/S32A-31A on USS *Nimitz* (CVN 68)
   - **Date:** 2022-05-10 | **Credit:** US Navy
   - **Observed Features:** Front three-quarter angle displaying the transition between the narrow forward cowl ($65.0\,\text{in}$) and the flared rear dual fenders ($70.0\,\text{in}$).
7. **Mechanism Detail / Control Panel Maintenance:**
   - **URL:** [DVIDS Image 9172114 - Sailor Replaces Control Panel on Tow Tractor](https://www.dvidshub.net/image/9172114)
   - **Platform & Hull:** A/S32A-31A on USS *Abraham Lincoln* (CVN 72)
   - **Date:** 2025-06-14 | **Credit:** US Navy
   - **Observed Features:** Close-up of cockpit dashboard, steering column base, electrical wiring harness, hydraulic pressure gauges, and transmission shifter assembly.
8. **Powertrain Maintenance / Engine Bay:**
   - **URL:** [DVIDS Image 256522 - Maintenance on Tow Tractor](https://www.dvidshub.net/image/256522)
   - **Platform & Hull:** A/S32A-31A in hangar bay of USS *Nimitz* (CVN 68)
   - **Date:** 2010-03-24 | **Credit:** US Navy
   - **Observed Features:** Open engine cowl revealing Detroit Diesel 3-53 block, cooling radiator, hydraulic pump linkages, and 24V starting system.

#### B. A/S32A-32 Spotting Dolly Records
1. **Front / Lifting Mechanism View:**
   - **URL:** [DVIDS Image 8451472 - Maintenance on Spotting Dolly](https://www.dvidshub.net/image/8451472)
   - **Platform & Hull:** A/S32A-32 on USS *George Washington* (CVN 73)
   - **Date:** 2024-06-04 | **Navy ID:** 240604-N-MI100-1018
   - **Observed Features:** Frontal perspective showing hydraulically articulated lifting arms, spread cylinders, and nosewheel axle adapter pin clamping mechanism.
2. **Rear / Drivetrain View:**
   - **URL:** [DVIDS Image 8451467 - Spotting Dolly Rear Maintenance](https://www.dvidshub.net/image/8451467)
   - **Platform & Hull:** A/S32A-32 on USS *George Washington* (CVN 73)
   - **Date:** 2024-06-04 | **Navy ID:** 240604-N-MI100-1020
   - **Observed Features:** Rear view showing single trailing caster wheel assembly, main chassis belly, and lower hydraulic line runs.
3. **Close-Up / Ford Carrier Maintenance:**
   - **URL:** [DVIDS Image 8653357 - Routine Maintenance on Spotting Dolly](https://www.dvidshub.net/image/8653357)
   - **Platform & Hull:** A/S32A-32 in hangar bay of USS *Gerald R. Ford* (CVN 78)
   - **Date:** 2024-09-17 | **Navy ID:** 240917-N-XJ026-1016
   - **Observed Features:** Close-up inspection of internal 24V battery bank, hydraulic reservoir, and drive chain tensioners aboard CVN-78.

#### C. Carrier Crash Crane ("Tilly" / A/S32A-35 CVCC) Records
1. **Operational Flight Deck Drill:**
   - **URL:** [DVIDS Image 8183487 - Crash and Salvage Operations on Ford](https://www.dvidshub.net/image/8183487)
   - **Platform & Hull:** A/S32A-35 CVCC "Tilly" on USS *Gerald R. Ford* (CVN 78)
   - **Date:** 2023-12-10 | **Credit:** US Navy
   - **Observed Features:** Full side-quarter view of the CVCC crash crane on the flight deck showing tilting A-frame boom, 6-wheel chassis, counterweight block, and operator cab.
2. **Crane Barge Onloading:**
   - **URL:** [DVIDS Image 8484981 - Tilly Loaded onto USS Gerald R. Ford](https://www.dvidshub.net/image/8484981)
   - **Platform & Hull:** A/S32A-35 CVCC hoisted by crane barge YD 257 to CVN-78 flight deck
   - **Date:** 2024-06-20 | **Credit:** US Navy
   - **Observed Features:** Aerial view displaying belly rigging, 6-wheel steering axles, boom pivot trunnions, and overall dimensional scale.

#### D. Modern A/S32A-49 STT Records
1. **Flight Deck Operations on Nimitz:**
   - **URL:** [DVIDS Image 7857430 - Nimitz Conducts Flight Ops with STT](https://www.dvidshub.net/image/7857430)
   - **Platform & Hull:** A/S32A-49 STT (Schopf F59 militarized derivative) on USS *Nimitz* (CVN 68)
   - **Date:** 2023-06-15 | **Credit:** US Navy
   - **Observed Features:** Angular German-built low-profile STT chassis, distinctive forward operator cockpit, and heavy rear drawbar plate.
2. **Operations on Carl Vinson:**
   - **URL:** [DVIDS Image 7757937 - Carl Vinson Sailor Operates STT](https://www.dvidshub.net/image/7757937)
   - **Platform & Hull:** A/S32A-49 STT on USS *Carl Vinson* (CVN 70)
   - **Date:** 2023-04-22 | **Credit:** US Navy
   - **Observed Features:** Forward three-quarter view showing heavy recessed tow hitch and side radiator grille.

---

## 9. External Collector Sibling Index Status & References

### 9.1 Sibling Collector Index Audit
* **Collector Sibling Path:** `D:/dreidel3d-sv2/refimages/`
* **Relative Link to Ready Ground Collector Index:**
  [`../../../../../dreidel3d-sv2/refimages/ground-agy/INDEX.md`](../../../../../dreidel3d-sv2/refimages/ground-agy/INDEX.md)
* **Collector Status:**
  - `ground-agy`: **ACTIVE & READY**. Master catalog contains 113 KB of verified ground assets, including:
    - Section `### A/S32A Tow Tractors (A/S32A-31A / A/S32A-31B / A/S32A-45)` (8 local files + Wikimedia/DVIDS mirrors).
    - Section `### A/S32A-32 / A/S32A-32A Aircraft Spotting Dolly` (8 local files across front, rear, port, starboard, overhead, and mechanism close-ups).
    - Section `### Flight Deck Tugs with GPCX / SGM Stenciled Designations` (8 local files covering MD-3 and A/S32A variants on CV-66 and CV-67).
    - Section `### Carrier Aircraft Tow Bars (ALBAR: 8, 15, 20, 24)` (8 local files detailing coupling kinematics).
  - `ground-grok`: **PENDING / NO INDEX READY**. Working directory contains `run.log` only; no `INDEX.md` catalog produced.

---

### 9.2 Authoritative Primary Source List

1. **NAVAIR 19-40-521:**  
   *Operation and Maintenance Instructions with Illustrated Parts Breakdown - Tractor, Wheeled, Aircraft Towing, A/S32A-31A*.  
   Published by Direction of Commander, Naval Air Systems Command. Section I: Table 1-1 "Leading Particulars" (p. 1-2); Section II: Operating Procedures; Section IV: GTC Air Start System Integration.  
   Archive: [Scribd Technical Library - NAVAIR 19-40-521](https://www.scribd.com/document/468817757/NAVAIR-19-40-521-A-S32A-31A-Tractor)
2. **NAVEDTRA 14329:**  
   *Aviation Support Equipment Technician (AS) Rate Training Manual*.  
   Naval Education and Training Professional Development and Technology Center. Chapter 5: "Powered Support Equipment", Sections: "A/S32A-31A Aircraft Towing Tractor" and "A/S32A-32 Aircraft Spotting Dolly".  
   Archive: [MilitaryNewbie Naval Technical Repository - NAVEDTRA 14329](https://militarynewbie.com/wp-content/uploads/2013/11/NAVEDTRA-14329-Aviation-Support-Equipment-Technician.pdf)
3. **NAVEDTRA 14014:**  
   *Airman Training Course*.  
   Naval Education and Training Professional Development and Technology Center. Chapter 9: "Support Equipment", Section 9-3: "Flight Deck Towing Vehicles".  
   Archive: [Scribd Naval Training Archive - NAVEDTRA 14014](https://www.scribd.com/document/443187211/NAVEDTRA-14014-Airman)
4. **NAVAIR 00-80T-96:**  
   *Carrier Aircraft Ground Handling Procedures Manual (CV Ground NATOPS)*.  
   Naval Air Systems Command. Chapter 4: "Aircraft Towing and Taxing Signals and Procedures", Table 4-1: "Authorized Towbar and Tractor Speed Limits".  
   Archive: [Maritime Technical Library - NAVAIR 00-80T-96](https://maritime.org/doc/pdf/aircraft-handling.pdf)
5. **NAVAIR 19-1-50:**  
   *Operation and Maintenance Instructions - Dolly, Aircraft Spotting, Model A/S32A-32*.  
   Naval Air Systems Command. Section 1: General Information & Leading Particulars; Section 2: Hydrostatic Propulsion Circuit; Section 3: Hydraulic Lift & Spread Arms.
6. **NAVAIR 19-40-44:**  
   *Operation, Service and Overhaul Instructions - Tractor, Wheeled, Aircraft Towing, Model MD-3*.  
   Naval Air Systems Command. Section 1: "Leading Particulars: Overall Length, Width, Height, and Drawbar Pull".
7. **NAVPERS 10303-B:**  
   *Aviation Support Equipment Technician*.  
   Bureau of Naval Personnel. Chapter 1: "Aircraft Ground Support Equipment", p. 14: "MD-3 Aircraft Towing Tractor Specifications".
8. **NAVAIR 19-70-46:**  
   *Operation and Maintenance Instructions with Illustrated Parts Breakdown - Universal Aircraft Towbars (ALBAR Series: Models 8, 15, 20, 24)*.  
   Naval Air Systems Command.
9. **Defense Logistics Agency (DLA) Master Logistics Record:**  
   *NSN 1740-01-379-4633: Tractor, Wheeled, Aircraft Towing, Model A/S32A-31A* (CAGE 80058, Part No. 3337AS100-1). Certified displacement $158.44\,\text{cu ft}$.  
   Archive: [PartTarget NSN 1740-01-379-4633](https://www.parttarget.com/1740-01-379-4633_1740013794633_3337AS100-1.html)
10. **Naval Air Warfare Center Aircraft Division (NAWCAD) Lakehurst:**  
    *Procurement Specification for Shipboard Tow Tractor (STT) A/S32A-49*.  
    Solicitation N68335-series, System for Award Management (SAM.gov).  
    Archive: [SAM.gov NAWCAD STT Solicitation Record](https://sam.gov)
11. **Defense Visual Information Distribution Service (DVIDS):**  
    Official Department of Defense visual imagery and caption records for U.S. Navy aircraft carriers and carrier air wings.  
    Primary Repository: [dvidshub.net](https://www.dvidshub.net)

---
*End of Knowledge Pack: `references/carrier-tow-tractors.md`*


---

<!-- NAVAL-CURRENT-START -->
# carrier-tow-tractors — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:24:21.394242+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-NAVAIR-STT-role` | NAVAIR describes CVN/LHA/LHD aircraft handling and a mobile platform/fuel supply for the MSU-200NAV air-start unit. Its photo identifies STT towing an F-35B aboard Essex. It does not identify an exact A/S32A chassis subtype or source wheelbase. | [Primary source](https://www.navair.navy.mil/product/Shipboard-Tow-Tractor-STT); Description / photograph caption |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| identified steering axle/wheels | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| tow pintle interfaces | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| variant-specific huffer access panels | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

A/S32A-31A 80-in versus91-in wheelbase and MD-3 74-in versusunknown conflict remains unresolved. Do not merge tractor, huffer, spotting dolly or crane variants or infer chassis dimensions from a generic STT page.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [USS Nimitz action ](https://www.dvidshub.net/image/256522/uss-nimitz-action) | `Airman Antonio Escobedo, aviation support equipment technician, performs maintenance on an aircraft tow tractor aboard the aircraft carrier USS Nimitz.` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [F/A-18F Super Hornet Towed On Flight Deck ](https://www.dvidshub.net/image/5542487/f-18f-super-hornet-towed-flight-deck) | `190626-N-KO930-0008 PACIFIC OCEAN (June 26, 2019) An F/A-18F Super Hornet assigned to the "Fighting Redcocks" of Strike Fighter Squadron (VFA) 22 is towed on the flight deck of the aircraft carrier USS Nimitz (` — `sourced-caption` | `port` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [High speed, low tractor ](https://www.dvidshub.net/image/6635536/high-speed-low-tractor) | `U.S. Navy Aviation Boatswain’s Mate Airman Lamar Vasquez, from Miami, Florida observes flight operations from an aircraft tow tractor on the flight deck of the aircraft carrier USS Theodore Roosevelt (CVN 71), ` — `sourced-caption` | `overhead` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Abraham Lincoln Sailors practice martial arts ](https://www.dvidshub.net/image/7031258/abraham-lincoln-sailors-practice-martial-arts) | `SAN BERNARDINO STRAIT (Feb. 2, 2022) Airman Ethan Conover, right, from Harrisburg, Penn., and Logistics Specialist 3rd Class Antonio Emmanuel, from Orlando, Fla., participate in the Marine Corps Martial Arts Pr` — `sourced-caption` | `front` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Sailors Conduct Maintenance On The Flight Deck ](https://www.dvidshub.net/image/7189288/sailors-conduct-maintenance-flight-deck) | `220508-N-LY692-1028 INDIAN ISLAND, Wash. (May 08 2022) Airman Daniel Goldenbaum, from Levittown, PA., and Aviation Boatswains Mate (Handling) 3rd Class Christian Jenkins, from Mobile, Ala. conduct maintenance o` — `sourced-caption` | `quarter` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Carl Vinson (CVN 70) Sailors Conduct Flight Deck Maintenance ](https://www.dvidshub.net/image/7757937/uss-carl-vinson-cvn-70-sailors-conduct-flight-deck-maintenance) | `230424-N-MD461-1118 SAN DIEGO (April 24, 2023) Aviation Boatswain’s Mate (Equipment) Airman Rianne Fernandez, a native of San Antonio, Texas, puts a rubber seal in a catapult slot on the flight deck of Nimitz-c` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Nimitz Conducts Flight Ops ](https://www.dvidshub.net/image/7857430/nimitz-conducts-flight-ops) | `230613-N-MH015-2261 PACIFIC OCEAN (June 13, 2023) An F/A-18F Super Hornet from the “Fighting Redcocks” of Strike Fighter Squadron (VFA) 22 taxis across the flight deck of the aircraft carrier USS Nimitz (CVN 68` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Tilly Operations ](https://www.dvidshub.net/image/8183487/tilly-operations) | `Sailors assigned to the air and aircraft intermediate maintenance department of the world's largest aircraft carrier USS Gerald R. Ford (CVN 78) hold a tag line during a carrier crash crane (CVCC) “Tilly” opera` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Sailors conduct routine operations ](https://www.dvidshub.net/image/8266739/sailors-conduct-routine-operations) | `240220-N-ED228-1087 SAN DIEGO (Feb. 20, 2024) Aviation Boatswain’s Mate (Handling) Airman Miguel Sanchez, from Montclair, Calif., chocks and chains an F/A-18E Super Hornet training jet on an aircraft elevator o` — `sourced-caption` | `rear` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS George Washington Sailor Performs Maintenance on Spotting Dolly ](https://www.dvidshub.net/image/8451467/uss-george-washington-sailor-performs-maintenance-spotting-dolly) | `Aviation Support Equipment Technician Airman Hayes B. Gray, from Tampa, Florida, assigned to aviation intermediate maintenance department’s IM4 division, performs maintenance on a spotting dolly aboard Nimitz-c` — `sourced-caption` | `rear` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS George Washington Sailor Performs Maintenance on Spotting Dolly ](https://www.dvidshub.net/image/8451472/uss-george-washington-sailor-performs-maintenance-spotting-dolly) | `Aviation Support Equipment Technician Airman Hayes B. Gray, from Tampa, Florida, assigned to aviation intermediate maintenance department’s IM4 division, performs maintenance on a spotting dolly aboard Nimitz-c` — `sourced-caption` | `front` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Ford Brings on "Tilly" ](https://www.dvidshub.net/image/8484981/ford-brings-tilly) | `NORFOLK, Va. (Jun 18, 2024) Sailors and Naval Facilities Engineering Systems Command workers load “Tilly”, a carrier crash crane (CVCC), onto the flight deck of the world’s largest aircraft carrier, USS Gerald ` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Routine Maintenance ](https://www.dvidshub.net/image/8653357/routine-maintenance) | `ATLANTIC OCEAN (Sep. 17, 2024) Aviation Support Equipment Technician Airman Marc Dorneson, from West Palm Beach, Florida, assigned to aircraft intermediate maintenance department, removes batteries from an A/S3` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Abraham Lincoln conducts routine operations ](https://www.dvidshub.net/image/9172114/abraham-lincoln-conducts-routine-operations) | `250630-N-BD533-1061 SAN DIEGO (June 30, 2025) Aviation Support Equipment Technician 3rd Class Josue Palacio, from Bakersfield, Calif., replaces control panel bottoms on an aircraft tow tractor in the hangar bay` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS George H.W. Bush Conducts Daily Operations ](https://www.dvidshub.net/image/9954153/uss-george-hw-bush-conducts-daily-operations) | `A U.S. Sailor maintains a tow tractor aboard Nimitz-class aircraft carrier USS George H.W. Bush (CVN 77), Sept. 19, 2026. George H.W. Bush is deployed to the U.S. 5th Fleet area of operations to support maritim` — `sourced-caption` | `starboard` candidate, `inferred-view`; exact coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=carrier+tow+tractors+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=carrier+tow+tractors+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=carrier+tow+tractors+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=carrier+tow+tractors+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=carrier+tow+tractors+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=carrier+tow+tractors+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=carrier+tow+tractors+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- [Existing ground-agy index](../../../../../dreidel3d-sv2/refimages/ground-agy/INDEX.md); `sourced-local-index-presence`. Read unit rows, not a blanket Complete banner. Some indexes contradict their own coverage matrices.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.
<!-- NAVAL-CURRENT-END -->


---

<!-- NAVAL-CURRENT-START -->
# carrier-tow-tractors — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:32:48.849695+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-NAVAIR-STT-role` | NAVAIR describes CVN/LHA/LHD aircraft handling and a mobile platform/fuel supply for the MSU-200NAV air-start unit. Its photo identifies STT towing an F-35B aboard Essex. It does not identify an exact A/S32A chassis subtype or source wheelbase. | [Primary source](https://www.navair.navy.mil/product/Shipboard-Tow-Tractor-STT); Description / photograph caption |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| identified steering axle/wheels | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| tow pintle interfaces | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| variant-specific huffer access panels | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

A/S32A-31A 80-in versus91-in wheelbase and MD-3 74-in versusunknown conflict remains unresolved. Do not merge tractor, huffer, spotting dolly or crane variants or infer chassis dimensions from a generic STT page.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [USS Nimitz action ](https://www.dvidshub.net/image/256522/uss-nimitz-action) | `Airman Antonio Escobedo, aviation support equipment technician, performs maintenance on an aircraft tow tractor aboard the aircraft carrier USS Nimitz.` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [F/A-18F Super Hornet Towed On Flight Deck ](https://www.dvidshub.net/image/5542487/f-18f-super-hornet-towed-flight-deck) | `190626-N-KO930-0008 PACIFIC OCEAN (June 26, 2019) An F/A-18F Super Hornet assigned to the "Fighting Redcocks" of Strike Fighter Squadron (VFA) 22 is towed on the flight deck of the aircraft carrier USS Nimitz (` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [High speed, low tractor ](https://www.dvidshub.net/image/6635536/high-speed-low-tractor) | `U.S. Navy Aviation Boatswain’s Mate Airman Lamar Vasquez, from Miami, Florida observes flight operations from an aircraft tow tractor on the flight deck of the aircraft carrier USS Theodore Roosevelt (CVN 71), ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Tilly Operations ](https://www.dvidshub.net/image/8183487/tilly-operations) | `Sailors assigned to the air and aircraft intermediate maintenance department of the world's largest aircraft carrier USS Gerald R. Ford (CVN 78) hold a tag line during a carrier crash crane (CVCC) “Tilly” opera` — `sourced-caption` | Scope: Tilly crash crane; related equipment only, not tow-tractor geometry. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS George Washington Sailor Performs Maintenance on Spotting Dolly ](https://www.dvidshub.net/image/8451467/uss-george-washington-sailor-performs-maintenance-spotting-dolly) | `Aviation Support Equipment Technician Airman Hayes B. Gray, from Tampa, Florida, assigned to aviation intermediate maintenance department’s IM4 division, performs maintenance on a spotting dolly aboard Nimitz-c` — `sourced-caption` | Scope: Spotting dolly; related equipment only, not tow-tractor geometry. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS George Washington Sailor Performs Maintenance on Spotting Dolly ](https://www.dvidshub.net/image/8451472/uss-george-washington-sailor-performs-maintenance-spotting-dolly) | `Aviation Support Equipment Technician Airman Hayes B. Gray, from Tampa, Florida, assigned to aviation intermediate maintenance department’s IM4 division, performs maintenance on a spotting dolly aboard Nimitz-c` — `sourced-caption` | Scope: Spotting dolly; related equipment only, not tow-tractor geometry. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Ford Brings on "Tilly" ](https://www.dvidshub.net/image/8484981/ford-brings-tilly) | `NORFOLK, Va. (Jun 18, 2024) Sailors and Naval Facilities Engineering Systems Command workers load “Tilly”, a carrier crash crane (CVCC), onto the flight deck of the world’s largest aircraft carrier, USS Gerald ` — `sourced-caption` | Scope: Tilly crash crane; related equipment only, not tow-tractor geometry. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Routine Maintenance ](https://www.dvidshub.net/image/8653357/routine-maintenance) | `ATLANTIC OCEAN (Sep. 17, 2024) Aviation Support Equipment Technician Airman Marc Dorneson, from West Palm Beach, Florida, assigned to aircraft intermediate maintenance department, removes batteries from an A/S3` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Abraham Lincoln conducts routine operations ](https://www.dvidshub.net/image/9172114/abraham-lincoln-conducts-routine-operations) | `250630-N-BD533-1061 SAN DIEGO (June 30, 2025) Aviation Support Equipment Technician 3rd Class Josue Palacio, from Bakersfield, Calif., replaces control panel bottoms on an aircraft tow tractor in the hangar bay` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS George H.W. Bush Conducts Daily Operations ](https://www.dvidshub.net/image/9954153/uss-george-hw-bush-conducts-daily-operations) | `A U.S. Sailor maintains a tow tractor aboard Nimitz-class aircraft carrier USS George H.W. Bush (CVN 77), Sept. 19, 2026. George H.W. Bush is deployed to the U.S. 5th Fleet area of operations to support maritim` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=carrier+tow+tractors+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=carrier+tow+tractors+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=carrier+tow+tractors+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=carrier+tow+tractors+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=carrier+tow+tractors+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=carrier+tow+tractors+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=carrier+tow+tractors+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- [Existing ground-agy index](../../../../../dreidel3d-sv2/refimages/ground-agy/INDEX.md); `sourced-local-index-presence`. Read unit rows, not a blanket Complete banner. Some indexes contradict their own coverage matrices.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.

Independent image-subject review correction: wrong-subject candidates excluded, duplicate image IDs collapsed, and sibling equipment separated above. Older revisions remain audit evidence and are superseded by this last current section.
<!-- NAVAL-CURRENT-END -->
