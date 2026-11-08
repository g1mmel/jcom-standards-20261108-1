---
name: weapons-terminal-effects
description: Ballistics, warhead taxonomy, terminal effects physics, naval and air weapons systems, and C&C Generals / SAGE damage-type x armor-set matrix design for deterministic RTS engines.
version: 1.0.0
tags:
  - ballistics
  - weapons-systems
  - terminal-effects
  - damage-matrices
  - electronic-warfare
  - naval-weapons
  - air-weapons
  - sage-engine
---

# Weapons, Warheads, and Terminal Effects Engineering Standard

## 1. Scope & Foundational Doctrine

This standard governs the physical modeling, categorization, and engine-level abstraction of modern military weapons systems, warheads, and terminal effects across the `jslcnc-v3` deterministic simulation engine (`C:\cnc_rev\skirmish`).

### 1.1 First Principles of Terminal Ballistics & Game Abstraction
Modern combat is governed by radical physical asymmetries between delivery systems, warhead mechanisms, and target structural protection. A modern warship, armored fighting vehicle, or military aircraft does not possess a single homogeneous hit-point pool, nor does a weapon deliver generic "damage points".

The Command & Conquer / SAGE engine design pattern abstracts real-world terminal physics through a dual-key lookup matrix:
$$\text{Damage Delivered} = \text{Base Weapon Damage} \times \text{DamageMatrix}[\text{DamageType}, \text{ArmorClass}]$$
In `jslcnc-v3`, this pattern is directly coupled to **Selective Damage (Subsystems)** and physical damage routing:
1. **Penetration vs. Surface Stripping:** Heavy kinetic AP and semi-armor-piercing (SAP) munitions pierce external hulls to inflict catastrophic damage on internal machinery, power generation, and ammunition magazines. High-explosive fragmentation (HE-frag) shells and proximity blast munitions detonate on external boundaries, shredding exposed sensors, antennas, radar arrays, weapons mounts, and unarmored personnel while leaving heavy armor intact.
2. **Impulse & Overpressure vs. Hardening:** Blast and thermobaric weapons expend energy in high-impulse shockwaves that crush light enclosures and collapse unfortified masonry, but produce negligible structural perforation against reinforced concrete bunkers or high-yield naval citadels.
3. **Hydrodynamic Cavitation:** Under-keel torpedo detonations bypass side armor entirely, lifting the vessel and snapping its longitudinal keel stringers through steam bubble expansion and collapse.
4. **Electronic Warfare as Non-Destructive Degradation:** Jamming, decoy distraction, GPS denial, and RF spoofing inflict zero physical hull damage ($0\text{ HP}$), instead routing into dynamic degradation meters that corrupt sensor detection, expand missile CEP, sever tactical datalinks, and break radar seeker lock.

---

## 2. Comprehensive Warhead Taxonomy

Modern military ordnance is classified into thirteen distinct warhead families based on their primary damage-infliction physics:

```
                      ┌──────────────────────────────────────┐
                      │      TERMINAL WARHEAD TAXONOMY       │
                      └──────────────────────────────────────┘
                                          │
    ┌──────────────────┬──────────────────┼──────────────────┬──────────────────┐
    ▼                  ▼                  ▼                  ▼                  ▼
 KINETIC           CHEMICAL           IMPULSE &          SPECIALIZED        DIRECTED ENERGY
 PERFORATION      ENERGY JETS        FRAGMENTATION        PHYSICAL            & SPECTRUM
 ├─ AP/APFSDS      └─ HEAT (Monobloc ├─ HE-Frag           ├─ Incendiary       ├─ DEW Laser
 ├─ Autocannon        & Tandem)      ├─ SAP Anti-Ship     ├─ Torpedo Whip     ├─ Electronic War
 └─ Small Arms                       ├─ Blast/Thermo      └─ Cluster Flech.   └─ EMP Pulse
```

### 2.1 Kinetic Armor-Piercing (AP / APFSDS)
- **Physics:** High-velocity sub-caliber long-rod penetrators (typically depleted uranium alloy or tungsten carbide heavy alloy) propelled at $1,400\text{--}1,750\text{ m/s}$. Operates on hydrodynamic penetration principles (Tate/Odermatt equations), where impact pressures exceed the dynamic yield strength of both projectile and armor ($P_{dyn} = \frac{1}{2}\rho v^2$).
- **Terminal Effects:** Perforates heavy monolithic steel, layered composite ceramic tiles, and reactive armor. Behind-armor effects include high-velocity pyrophoric spalling, fragmented rod debris, and extreme overpressure inside enclosed crew compartments.
- **Key Real-World Systems:** 120mm M829A3/A4 APFSDS (M1A2 Abrams), 125mm 3BM60 Svinets-2 (T-72/T-90), 120mm APAM/APFSDS (Merkava Mk 4).

### 2.2 High-Explosive Anti-Tank / Shaped Charge (HEAT)
- **Physics:** Munroe effect. A precision-machined conical or hemispherical copper liner collapsed by a high-detonation-velocity explosive (Composition B, Octol, CL-20) at $7,000\text{--}9,000\text{ m/s}$. Forms a hypervelocity metallic jet ($v_{tip} \approx 8\text{--}10\text{ km/s}$) that punches through armor via localized hydrodynamic displacement.
- **Countermeasures & Defeat Mechanisms:** Highly vulnerable to standoff disruption, Explosive Reactive Armor (ERA), non-explosive reactive armor (NxRA), composite ceramic air-gaps, and slat/cage standoff screens. Tandem warheads utilize a precursor shaped charge to detonate ERA prior to the main jet.
- **Key Real-World Systems:** AGM-114 Hellfire, BGM-71 TOW, FGM-148 Javelin, RPG-7 / PG-7VR tandem, Spike-MR/LR/ER.

### 2.3 High-Explosive Fragmentation (HE-Frag)
- **Physics:** Cylindrical steel or heavy alloy shell casing filled with secondary high explosive (TNT, Comp B, PBX). Detonation generates a Gurney-driven supersonic expansion of casing fragments ($v_{frag} \approx 1,000\text{--}2,500\text{ m/s}$) and a short-duration shockwave.
- **Terminal Effects:** Devastating against soft tissue, biological targets, exposed tires, aircraft control surfaces, antenna radomes, and unarmored vehicles. Fragment penetration rapidly decays with distance and is arrested by mild structural steel ($>10\text{--}15\text{ mm}$) or NIJ Level IV body armor. Negligible penetration against MBT armor ($<10\%$).
- **Key Real-World Systems:** 155mm M107/M795 artillery projectiles, Mk 82/83/84 GP iron bombs, 122mm Grad rockets, RIM-162 ESSM warhead, Tamir Iron Dome interceptor.

### 2.4 Semi-Armor-Piercing Anti-Ship (SAP / Delayed Action)
- **Physics:** Heavy-walled forged alloy steel casing with a hardened ogive nose cone, carrying a reduced high-explosive burster ($15\text{--}30\%$ of total missile mass, typically insensitive munitions like PBXN-109) coupled to a base-mounted delay fuze (void-sensing accelerometer or pyrotechnic millisecond delay).
- **Terminal Effects:** Designed to penetrate $25\text{--}50\text{ mm}$ of exterior structural steel hull plating, splinter bulkheads, and deck levels before detonating deep within internal compartments (engine rooms, weapon magazines, electrical switchboards). Creates severe catastrophic internal overpressure, bulk fire, and structural compartmental tearing.
- **Key Real-World Systems:** AGM-84 Harpoon (WDU-18/B), AGM-158C LRASM (WDU-42/B), BGM-109 Tomahawk Block V (WDU-36/B unitary), Gabriel V, P-800 Oniks.

### 2.5 Blast / Fuel-Air Explosive / Thermobaric
- **Physics:** High-impulse shock generation. Thermobaric/FAE munitions disperse an aerosol cloud of volatile hydrocarbon fuel or reactive metallic particles (aluminum/magnesium) before detonation, consuming ambient atmospheric oxygen to generate an extended positive overpressure duration ($\Delta t_{pos} \gg \Delta t_{conventional}$) followed by a deep vacuum phase.
- **Terminal Effects:** Severe lethality inside confined spaces, tunnel systems, urban basements, and unreinforced structures. Lacks dense metallic fragments and cannot penetrate armored steel, but structural overpressure shatters load-bearing cinderblock, crushes lungs, and blows out building facades.
- **Key Real-World Systems:** AGM-114N Metal Augmented Charge (MAC) Hellfire, GBU-43/B MOAB, TOS-1A 220mm rocket, RPO-A Shmel.

### 2.6 Incendiary & Pyrotechnic
- **Physics:** Chemical combustion reactions generating sustained thermal flux ($>1,200\text{--}2,500^\circ\text{C}$) over an extended time interval. Typical agents include triethylaluminum (TEA), plasticized white phosphorus (PWP), thermite, and zirconium-infused fuels.
- **Terminal Effects:** Low direct impact damage. Initiates persistent fire envelopes (`fire > 0.5`) that propagate into flammable materials (JP-5 aviation fuel, electrical cabling, hydraulic reservoirs, vehicle tires). Forces secondary deflagration of ammunition stowage if fire is not suppressed by automated deluge or Damage Control crews within $15\text{--}30\text{ seconds}$.
- **Key Real-World Systems:** M34 White Phosphorus grenades, CBU-100 incendiary clusters, aviation fuel fire spread.

### 2.7 Cluster / Submunition Flechette (DPICM)
- **Physics:** Cargo dispenser shell or canister missile that ejects dozens or hundreds of independent submunitions at a pre-set altitude above ground level. Submunitions typically combine a miniature shaped-charge cone (downward-facing) with a scored fragmentation steel skirt (dual-purpose).
- **Terminal Effects:** Wide-area footprint coverage ($100\text{--}300\text{ m}$ footprint). Lethal against concentrated light armored vehicles (striking vulnerable top deck armor), parked aircraft, artillery batteries, and personnel in the open. Low lethality against hardened concrete structures.
- **Key Real-World Systems:** M30 GMLRS DPICM, M30A1 Alternative Warhead (182,000 pre-formed tungsten spheres), Mk 20 Rockeye II, CBU-97/105 Sensor Fuzed Weapon.

### 2.8 Small Arms Ball & AP (5.56mm, 7.62mm, 12.7mm)
- **Physics:** Solid lead-core with copper gilding (Ball) or hardened steel/tungsten core (AP) fired from rifled small-arms barrels at $700\text{--}950\text{ m/s}$.
- **Terminal Effects:** Lethal against unprotected personnel. High incapacitation through yawing, cavitation, and tumbling. Stopped by standard vehicular armor plate ($>8\text{ mm}$ RHA), ballistic glass, and ceramic torso plates (NIJ IV). .50 BMG (12.7mm) AP can penetrate light unarmored engine blocks and skin-thick vehicle hulls up to $18\text{--}22\text{ mm}$ RHA.
- **Key Real-World Systems:** 5.56x45mm M855A1 EPR, 7.62x51mm M80A1 / M993 AP, 12.7x99mm (.50 BMG) M2 AP / SLAP.

### 2.9 Autocannon HEI / APDS (20mm, 25mm, 30mm)
- **Physics:** High-rate-of-fire ($200\text{--}6,000\text{ rpm}$) medium-caliber ammunition firing mixed belts of Armor-Piercing Discarding Sabot (APDS/APFSDS) and High-Explosive Incendiary (HEI/SAPHEI).
- **Terminal Effects:** APDS penetrates $30\text{--}70\text{ mm}$ of RHA at close combat ranges, sufficient to perforate IFVs, APCs, and helicopter hulls from any aspect, and MBT flanks/engine grilles. HEI strips topside antennas, optical sights, and thin aircraft skins.
- **Key Real-World Systems:** 20mm M61A1/A2 Vulcan (Phalanx CIWS, F/A-18), 25mm M242 Bushmaster (Bradley, LAV-25, Mk 38), 25mm GAU-22/A (F-35), 30mm Mk 44 Bushmaster II (ACV-30), 30mm GAU-8/A Avenger.

### 2.10 Directed Energy Laser (High-Energy Laser - HEL)
- **Physics:** Continuous-wave or high-repetition pulsed solid-state fiber laser beam emitting at near-infrared wavelengths ($\lambda \approx 1.06\text{ }\mu\text{m}$) with power levels of $30\text{--}300\text{ kW}$.
- **Terminal Effects:** Inflicts damage via thermal deposition and structural ablation. Melts aerodynamic radomes, ruptures pressurized propellant tanks on incoming missiles, and blind/fuses electro-optical seekers. Zero time-of-flight.
- **Environmental Vulnerability:** Subject to severe thermal blooming, aerosol scattering, and absorption in rain, fog, coastal haze, and dense smoke (attenuation factor up to $60\text{--}80\%$).
- **Key Real-World Systems:** Iron Beam (100 kW class), AN/SEQ-3 Laser Weapon System (LaWS), ODIN / HELIOS naval lasers.

### 2.11 Electronic Warfare / Jamming (Spectrum Attack)
- **Physics:** High-power active radio-frequency (RF) emission, digital radio frequency memory (DRFM) deception, and optical/infrared decoy deployment. Operates across radar, communications, and satellite navigation frequency bands.
- **Terminal Effects:** Inflicts **$0\text{ HP}$ structural damage**. Drives temporary system degradation:
  1. *Radar Noise & Deception Jamming:* Injects synthetic false targets or elevated thermal noise, slashing radar target acquisition range and fire-control track quality.
  2. *Communications & Datalink Severance:* Jams VHF/UHF tactical radio, Link-16, and MADL mesh networks, increasing command latency and preventing automated cooperative targeting.
  3. *GPS / GNSS Denial:* Corrupts satellite navigation signals, causing JDAM and SDB glide weapons to revert to pure inertial guidance (INS drift, CEP inflating from $5\text{ m}$ to $30\text{--}50\text{ m}$).
  4. *Decoy Break-Lock:* Soft-kill seduction (Nulka hovering rocket, chaff clouds, flares, towed RF decoys) enticing active radar and IR seekers away from the parent hull.
  5. *Burn-Through Range:* The critical distance where radar target echo ($P_r \propto 1/R^4$) overcomes jammer power ($P_j \propto 1/R^2$), restoring radar tracking at close range.
- **Key Real-World Systems:** AN/ALQ-99 & NGJ-MB (EA-18G Growler), AN/SLQ-32(V)6/7 SEWIP (Arleigh Burke, Ford), Mk 53 Nulka decoy.

### 2.12 Torpedo Under-Keel (Bubble Cavitation & Whipping)
- **Physics:** High-explosive detonation positioned $5\text{--}10\text{ meters}$ directly beneath a warship's keel. Detonation creates a high-pressure primary shock pulse followed by an expanding and collapsing gaseous steam bubble.
- **Terminal Effects:** As the gas cavity expands, it lifts the hull amidships ("hogging"). When the bubble collapses, support is removed and hydrostatic suction pulls the hull downward ("sagging"). This cyclical whipping exceeds the hull girder's ultimate section modulus, snapping the longitudinal structural keel, inducing massive bilge flooding, and disabling propulsion/electrical generation instantly.
- **Key Real-World Systems:** Mk 48 Mod 7 ADCAP heavyweight torpedo (SSN), Mk 54 Mod 0 lightweight torpedo (MH-60R, SVTT, VL-ASROC), DM2A4 Seahake.

### 2.13 High-Altitude Electromagnetic Pulse (EMP)
- **Physics:** High-altitude detonation or flux-compression generator emitting a high-voltage, fast-rise-time electromagnetic pulse ($E_1$ prompt pulse $<10\text{ ns}$, $E_2$ intermediate, $E_3$ magneto-hydrodynamic).
- **Terminal Effects:** Induces high electrical currents in unshielded wiring, microwave antennas, and power buses, dielectric breakdown of microchips, computer system reboots, and tripping circuit breakers. Leaves vehicle structures physically intact while rendering fire-control computers and active radar arrays completely non-functional.
- **Key Real-World Systems:** High-power microwave (HPM) munitions, non-nuclear EMP warheads, Fulgurite EMP emitter.

---

## 3. Terminal Effects vs. Target Classes

| Target Class | Representative Platforms | High-Effectiveness Warheads | Low-Effectiveness Warheads | Dominant Failure Modes |
| :--- | :--- | :--- | :--- | :--- |
| **Personnel** | Infantry, weapons crews, deck watch | HE-frag, Small Arms, DPICM, Thermobaric | APFSDS, SAP Anti-Ship | Shrapnel perforation, pulmonary blast overpressure, thermal burns. |
| **Unarmored Vehicle** | Technicals, utility trucks, JLTV baseline | Small Arms AP, Autocannon HEI, HE-frag | Torpedo, EMP | Engine block fracture, tire rupture, driver kill, instant fuel tank fire. |
| **Light Armor** | LAV-25, AAV-7A1, ACV, Stryker | HEAT shaped charge, Autocannon APDS, DPICM | Small Arms Ball, HE-frag (non-direct) | Hull perforation, ammunition cookoff, suspension shearing. |
| **MBT Heavy Armor** | M1A1/M1A2 Abrams, Merkava Mk 4, T-72 | APFSDS kinetic rod, Tandem HEAT | HE-frag, Small Arms, Autocannon HEI | Spall cone behind armor, blowout panel activation, engine immobilization. |
| **Aircraft (Airborne)** | F-35, F/A-18, EA-18G | Autocannon HEI, Blast-frag SAM, Laser ablation | Heavy APFSDS, Torpedo, SAP Anti-ship | Wing spar separation, turbine blade ingestion, flight control loss. |
| **Aircraft (Parked)** | Flight deck / tarmac aircraft | HE-frag, Cluster DPICM, Incendiary | Heavy APFSDS, Torpedo | Skin puncturing, JP-5 fuel ignition, chain-reaction deck fires. |
| **Rotary-Wing** | AH-1Z, UH-1Y, MH-60, MV-22 | Autocannon HEI, Proximity HE-frag, Manpads IR | Small Arms Ball, Torpedo | Rotor blade fracture, tail boom severance, gearbox seizure. |
| **Structure (Unfortified)**| Cinderblock, hangars, civilian buildings | Blast/Thermobaric, HE-frag, Heavy SAP | Small Arms Ball, Autocannon APDS | Facade collapse, structural frame shearing, internal fire spread. |
| **Structure (Fortified)** | Hardened shelters (HAS), bunkers | Kinetic penetrators (BLU-109), Heavy SAP | HE-frag, Cluster DPICM, Small Arms | Delayed internal detonation, roof spalling, shock isolation failure. |
| **Ship Topside Sensors** | Phased arrays (SPY-6), antennas, CIWS | HE-frag, Autocannon HEI, Laser | Heavy APFSDS (passes through) | Antenna waveguide shearing, radome melting, sensor blind spots. |
| **Ship Hull & Waterline** | Exterior shell steel (15-30mm) | SAP Anti-Ship, Heavy Naval Gun HE | Small Arms, HE-frag | Waterline tearing, free-surface flooding, list, speed loss. |
| **Ship Armored Citadel** | Reactor space, MMR, deep magazine | Heavy SAP (delayed burster), Heavy AP | HE-frag, Autocannon HEI, Small Arms | Internal compartment detonation, loss of electrical power, magazine blowout. |

---

## 4. Physical Penetration, Overpressure & Fragmentation Formulas

In the `jslcnc-v3` engine, terminal calculations follow deterministic mathematical formulations:

### 4.1 Kinetic Penetration (De Marre / Odermatt Hydrodynamic Model)
For high-velocity kinetic rods ($v > 1,200\text{ m/s}$):
$$\frac{P}{L} = \sqrt{\frac{\rho_{proj}}{\rho_{target}}} \cdot \left(1 - \frac{H_{dynamic}}{\frac{1}{2}\rho_{proj} v^2}\right)$$
Where:
- $P$ is penetration depth in millimeters of RHA.
- $L$ is penetrator rod length ($m$).
- $\rho_{proj}, \rho_{target}$ are projectile and armor densities (e.g. DU: $19,050\text{ kg/m}^3$, RHA: $7,850\text{ kg/m}^3$).
- $H_{dynamic}$ is the target's hydrodynamic resistance hardness.

### 4.2 Blast Overpressure Scaling (Hopkinson-Cranz Law)
Peak side-on overpressure $\Delta P_{so}$ at standoff distance $R$ from explosive mass $W$ (TNT equivalent):
$$Z = \frac{R}{\sqrt[3]{W}}$$
$$\Delta P_{so}(Z) = \frac{100}{Z^3} + \frac{20}{Z^2} + \frac{5}{Z} \quad (\text{kPa for } Z \ge 1.0)$$
In game terms:
- Target distance $R$ scales exponentially in damage: overpressure falls off as $1/R^3$ in the near field.

### 4.3 Gurney Fragmentation Velocity
Supersonic fragment initial velocity $v_{frag}$ for a steel casing filled with explosive:
$$v_{frag} = \sqrt{2E} \cdot \left( \frac{M}{C} + \frac{1}{2} \right)^{-1/2}$$
Where:
- $\sqrt{2E}$ is the Gurney energy constant of the explosive ($2,700\text{ m/s}$ for Comp B).
- $M/C$ is the mass ratio of casing metal to explosive filler.

---

## 5. Electronic Warfare Math: Radar Jamming & Burn-Through Range

### 5.1 Radar Range Equation under Noise Jamming
For a radar with transmitter power $P_t$, antenna gain $G$, wavelength $\lambda$, target radar cross section (RCS) $\sigma$, and jammer with effective radiated power (ERP) $P_j G_j$ at bandwidth $B_j$:
$$\text{Target Echo Received Power:} \quad S = \frac{P_t G^2 \lambda^2 \sigma}{(4\pi)^3 R^4}$$
$$\text{Jammer Noise Received Power:} \quad J = \frac{(P_j G_j) G \lambda^2}{(4\pi)^2 R_j^2 B_j}$$
The **Burn-Through Range** $R_{bt}$ (where signal-to-noise ratio $S/J$ equals the radar detection threshold $SNR_{thresh}$):
$$R_{bt} = \sqrt{\frac{P_t G \sigma B_j}{4\pi (P_j G_j) SNR_{thresh}}}$$
When target distance $R > R_{bt}$, the target is completely masked by noise (`radarFactor` drops to near zero). When $R \le R_{bt}$, target echo burns through the jamming and normal track acquisition resumes.

---

## 6. SAGE Engine Matrix Pattern: DamageType x ArmorClass

The classic SAGE engine (`Zero Hour`) represents combat through an explicit percentage matrix. In `jslcnc-v3`, multipliers are normalized from $0.00$ ($0\%$, total immunity) to $2.00+$ ($200\%+$, lethal vulnerability).

$$\text{Effective Damage} = \text{RawDamage} \times \text{Multiplier}(\text{DamageType}, \text{ArmorClass}) \times \frac{100}{100 + \text{ArmorRating}}$$

This matrix is fully externalized to `data/weapons/damage-matrix.json`.

---

## 7. Audit & Verification Questions

When reviewing weapon implementations or balancing damage curves, ask:
1. **Physical Soundness:** Does an HE-frag bomb striking an M1A2 Abrams turret destroy the tank, or does it correctly strip external machine guns and optics while leaving the composite armor intact ($<10\%$ hull damage)?
2. **Selective Damage Routing:** Does an anti-ship missile with an SAP warhead penetrate the outer hull and damage internal machinery and power generation rooms?
3. **Decoupled EW:** Does electronic attack inflict zero hull HP damage, instead degrading detection sectors and introducing probabilistic miss rolls for guided seekers?
4. **Keel Physics:** Does an under-keel torpedo hit properly trigger the hull hogging/sagging whipping model and fatal flooding, rather than behaving like a topside missile impact?
5. **Weather Coupling:** Are directed energy weapons (lasers) properly degraded in high-humidity, foggy, or raining weather tiers?
6. **Determinism:** Are hit calculations and decoy distraction rolls evaluated using the deterministic seeded PRNG stream rather than non-deterministic system calls?

---

## 8. Authoritative References & Sourced Standards
- **Ballistics Research Laboratory (BRL) Technical Reports:** BRL-TR-2870, *Hydrodynamic Models of Long Rod Armor Penetration*.
- **NAVSEA NSTM Chapter 079, Volume 2:** *Damage Control — Compartmentation, Firefighting, and Flooding Control*.
- **MIL-HDBK-708:** *Terminal Ballistics & Warhead Design*.
- **Jane's Weapons: Naval (2024--2025 Edition):** Mk 45 5"/62, Mk 41 VLS, Mk 15 Phalanx, ESSM, RAM, SM-6, Harpoon, Tomahawk, LRASM.
- **Jane's All the World's Aircraft (2024--2025 Edition):** F-35 Lightning II, F/A-18E/F Super Hornet, EA-18G Growler, E-2D Hawkeye, MH-60R/S, MV-22B, AH-1Z.
- **C&C Generals: Zero Hour INI Reference:** `Armor.ini`, `Weapon.ini`, `DamageType` and `ArmorSet` architectural definitions.
