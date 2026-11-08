---
name: ground-air-military-systems
description: >-
  Authoritative engineering and military systems standard for ground vehicles, artillery, air defense,
  rotary and fixed-wing aircraft, fortifications, and industrial military structures. Specifies subsystem decomposition,
  vulnerability geometry, degradation cascades, empirical reliability and MTBF distributions, terrain/environmental wear,
  and structural damage zones for high-fidelity simulation.
---

# Ground & Air Military Systems and Structures Standard

This standard establishes the engineering and operational doctrine for modeling ground combat vehicles, artillery, air defense batteries, rotary and fixed-wing aviation, field fortifications, and military/industrial infrastructure. It provides precise subsystem breakdowns, damage degradation functions, empirical reliability data (MTBF/MMBSA), maintenance/recovery doctrine, fuel/ammo logistics parameters, and an audit question bank for deterministic simulation engines.

---

## 1. Subsystem Architecture & Geometric Envelope

### 1.1 Coordinate Frame & Alignment
All military platform subsystems are defined in a platform-centric Cartesian coordinate system matching real-world engineering standards (ISO 8855 / SAE vehicle dynamics):
* **Longitudinal ($X$):** Positive forward ($+X$ = Bow/Nose), negative aft ($-X$ = Stern/Tail).
* **Lateral ($Y$):** Positive starboard/right ($+Y$), negative port/left ($-Y$).
* **Vertical ($Z$):** Positive upward ($+Z$ = Turret/Roof), negative downward ($-Z$ = Keel/Ground contact plane).
* **Scale Invariant:** $1.0\text{ unit} = 1.0\text{ meter}$.

### 1.2 Component Classification Hierarchy
Every subsystem belongs to one of four vulnerability classes:
1. **External Exposed (Unarmored):** Radars, mast-mounted sights (MMS), sensor heads, smoke grenade dischargers, track skirts, antenna masts, external fuel tanks. Armor: $5\text{–}15\text{ mm}$ steel equivalent ($RHA_e$). Vulnerable to fragments, heavy machine gun (HMG) $12.7\text{mm}$, and blast overpressure.
2. **External Armored:** Turret mantlets, main gun barrel/breech assembly, armored cupolas, heavily armored weapon stations (CROWS), ERA cassettes, active protection system (APS) launcher heads. Armor: $25\text{–}80\text{ mm}$ $RHA_e$ or modular composite.
3. **Internal Compartment (Critical):** Crew fighting compartment, automotive engine/pack, transmission/final drives, primary ammunition magazine, fuel cells, auxiliary power unit (APU), hydraulic power unit (HPU). Protected by main hull/turret composite arrays ($300\text{–}1000+\text{ mm}$ vs KE / HEAT). Reached only by piercing penetration or spalling.
4. **Structural Envelope (Hull/Frame):** Welded armored hull, aircraft monocoque fuselage, structural box trusses, reinforced concrete caissons. Carries the overall integrity health pool.

---

## 2. Per-Category Subsystem Templates

### 2.1 Armored Combat Vehicles (MBTs, IFVs, APCs)
*Standard Reference Platforms: M1A2 SEPv3 Abrams, M2A4 Bradley IFV, T-72B3M, Sentinel Siege Tank, Paladin Tank.*

```
       [Primary Sight/CITV] (+Z: 2.8m)
               |
  [Gun/Mantlet]--[Turret/Crew]--[Blowout Ammo Rack]
  (+X: 1.8m)     (0.0m)         (-X: 1.4m)
        |           |                |
  [Final Drive]--[Hull/Driver]--[Engine & Transmission]
  (+X: 3.2m)     (+X: 1.5m)     (-X: 2.2m)
        |           |                |
  [Tracks/Roadwheels L/R] (Y: +/- 1.7m, Z: 0.5m)
```

| Subsystem ID | Kind | Location $(X, Y, Z)$ | Volume Type & Half-Size $(x,y,z)$ | Armor ($RHA_e$) | Failure / Degradation Effect |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `engine-pack` | `engine` | $(-2.2, 0.0, 0.2)$ | Box $(0.9, 0.8, 0.6)$ | $45\text{ mm}$ int | Speed reduced by $100\%$ on destruction; fire risk $40\%$ on penetrating hit. |
| `transmission` | `machinery` | $(-3.1, 0.0, 0.0)$ | Box $(0.5, 0.7, 0.5)$ | $40\text{ mm}$ int | Immobilization (`broken_transmission`); steering locked; cannot pivot. |
| `track-left` | `mobility` | $(0.0, -1.7, -0.4)$ | Box $(3.6, 0.35, 0.45)$ | $20\text{ mm}$ ext | Speed capped at $30\%$; turn rate derated by $80\%$; thrown track risk on turn. |
| `track-right`| `mobility` | $(0.0, 1.7, -0.4)$ | Box $(3.6, 0.35, 0.45)$ | $20\text{ mm}$ ext | Speed capped at $30\%$; turn rate derated by $80\%$; asymmetric drift. |
| `final-drives`| `mobility` | $(3.2, \pm 1.6, -0.3)$ | Sphere $r=0.35$ | $35\text{ mm}$ ext | Drive sprocket lockup; instant throw of affected track; total directional freeze. |
| `turret-drive`| `machinery` | $(0.0, 0.0, 0.8)$ | Box $(0.6, 0.6, 0.3)$ | $30\text{ mm}$ int | Traverse speed drops from $40^\circ/\text{s}$ to emergency manual $2^\circ/\text{s}$. |
| `gun-breech`  | `gun` | $(1.2, 0.0, 1.1)$ | Box $(0.8, 0.4, 0.4)$ | $60\text{ mm}$ ext | Main armament disabled; secondary coaxial MG only. |
| `fire-control`| `optics` | $(0.6, 0.7, 1.8)$ | Sphere $r=0.25$ | $15\text{ mm}$ ext | Loss of lead calculation, thermal thermography; dispersion increased by $400\%$. |
| `ammo-rack`   | `magazine` | $(-1.4, 0.0, 1.2)$ | Box $(0.8, 1.1, 0.5)$ | $50\text{ mm}$ int | Blowout panels vent: loss of main gun ammo; without panels: hull catastrophe. |
| `fuel-cells`  | `fuel` | $(-0.5, \pm 1.4, -0.1)$| Box $(1.2, 0.4, 0.5)$ | $30\text{ mm}$ ext/int | Fuel leak ($0.5\%\text{ fuel/s}$); catastrophic fire risk if ignited by HEAT jet. |

### 2.2 Artillery & Rocket Launchers (SPH, MLRS, HIMARS)
*Standard Reference Platforms: M109A7 Paladin, M142 HIMARS, M270 MLRS, 2S19 Msta-S, Seismic Cannon, Grad Truck.*

| Subsystem ID | Kind | Vulnerability / Hit Profile | Failure Impact |
| :--- | :--- | :--- | :--- |
| `elevating-mass` | `gun` | Exposed hydraulic equilibrators & elevation cylinders | Elevation jammed at current angle; cannot adjust range. |
| `loader-rammer` | `machinery` | Internal auto-loader carousel / hydraulic rammer | Cadence drops from 6–8 rounds/min to manual 1 round/min; reload stalls. |
| `recoil-mechanism`| `machinery` | Hydropneumatic recoil recuperators | Firing weapon deals $15\%$ structural hull damage per shot due to unbuffered recoil. |
| `fire-direction-ins`| `optics` | Ring laser gyro / GPS survey antenna / muzzle radar | CEP (Circular Error Probable) increases from $5\text{ m}$ to $75\text{ m}$; dispersion x10. |
| `launch-pod-turntable`| `machinery`| Azimuth ring gear & hydraulic slew motor | Slew jammed; vehicle must traverse entire chassis to aim (wheeled chassis penalty). |
| `ammo-magazine` | `magazine` | Large propellant charge / rocket canister bank | Cookoff produces instantaneous secondary blast destroying adjacent soft units ($25\text{ m}$ radius). |

### 2.3 Air Defense Systems (SHORAD, C-RAM, Long-Range SAM)
*Standard Reference Platforms: Centurion C-RAM, Iron Dome, Skylance M-SHORAD, Rapier Emplacement, Skyfire Array.*

| Subsystem ID | Kind | Function & Geometry | Failure / Degradation Cascade |
| :--- | :--- | :--- | :--- |
| `search-radar` | `radar` | Rotating planar/AESA array atop mast | Loss of target acquisition queue; battery cannot track new incoming tracks beyond optical range ($1.5\text{ km}$). |
| `tracking-radar` | `radar` | Monopulse fire-control dish / illuminator | Loss of terminal guidance; intercept probability ($P_k$) collapses from $0.90$ to $0.05$. |
| `generator-apu` | `power` | Diesel auxiliary generator ($60\text{ kW}$) | Radar and hydraulic drives shut down within $4\text{ seconds}$; battery deadstick. |
| `optical-tracker` | `optics` | FLIR / TV day-night auto-tracker | Fallback sensor; if destroyed alongside radar, battery cannot engage any aerial target. |
| `launcher-canister` | `missile` | Armored canister bank / cell umbilical | Affected bank cannot launch; missile hang-fire danger. |
| `cooling-chiller` | `machinery`| Environmental control unit (ECU) for T/R modules| Transmitter overheats; radar shuts down after $45\text{ s}$ of continuous radiating. |

### 2.4 Rotary-Wing Aircraft (Attack, Heavy Lift, Tiltrotor)
*Standard Reference Platforms: AH-64E Apache, AH-1Z Viper, CH-53K King Stallion, CMV-22B Osprey.*

```
             [Main Rotor Head & Swashplate] (+Z: 2.5m)
                          |
   [Engines 1 & 2]--[Main Transmission]--[Tail Rotor Drive Shaft]
   (Y: +/- 0.9m)    (0.0m, Z: 1.6m)       (-X: 1.0 to 6.5m)
                          |                         |
   [Avionics & Cockpit]--[Fuel Cell & Fuselage]--[Tail Rotor Gearbox]
   (+X: 2.5m, Z: 0.2m)   (0.0m, Z: -0.2m)        (-X: 7.2m, Z: 1.8m)
```

| Subsystem ID | Kind | Location | Vulnerability ($RHA_e$) | Failure / Degradation Cascade |
| :--- | :--- | :--- | :--- | :--- |
| `main-rotor-head` | `propulsion`| $(0.0, 0.0, 2.5)$ | $15\text{ mm}$ titanium | Severe vibration; lift efficiency drops $50\%$; uncontrollable pitch/roll. |
| `swashplate-actuators`| `machinery` | $(0.0, 0.0, 2.1)$| $10\text{ mm}$ ext | Cyclic/collective control severed; craft enters unrecoverable roll within $3\text{ s}$. |
| `turboshaft-engine-0`| `engine` | $(-0.4, -0.9, 1.4)$| $12\text{ mm}$ armored cowl| Single-engine emergency descent; airspeed capped at $55\text{ kts}$; climb rate $0$. |
| `turboshaft-engine-1`| `engine` | $(-0.4, 0.9, 1.4)$ | $12\text{ mm}$ armored cowl| Dual failure results in autorotation descent ($6\text{ s}$ to crash/eject). |
| `main-transmission` | `machinery` | $(0.0, 0.0, 1.6)$ | $20\text{ mm}$ int | Loss of lubrication: run-dry limit $30\text{ minutes}$ (MIL-STD-810H); seizure causes total rotor lockup. |
| `tail-rotor-shaft` | `propulsion`| $(-4.0, 0.0, 0.8)$| $6\text{ mm}$ monocoque | Loss of yaw torque counter; helicopter spins uncontrollably (flat spin) at $120^\circ/\text{s}$. |
| `tail-rotor-gearbox`| `propulsion`| $(-7.2, 0.3, 1.8)$ | $10\text{ mm}$ ext | Instantaneous yaw loss; immediate ground crash unless high-speed forward airflow maintained. |
| `avionics-mms` | `optics` | $(3.2, 0.0, 0.4)$ | $8\text{ mm}$ ext | FLIR/laser designator severed; Hellfire/missiles lose semi-active laser guidance. |
| `wing-pylon-l` | `weapons-station`| $(0.2, -1.8, 0.1)$| $10\text{ mm}$ ext | Station jettisons or misfires; asymmetric drag penalty ($15\%$ speed loss). |

### 2.5 Fixed-Wing Aircraft (Strike, CAS, Gunship, Strategic)
*Standard Reference Platforms: A-10C Warthog, F-35B/C Lightning II, AC-130J Ghostrider, B-1B Lancer.*

| Subsystem ID | Kind | Subsystem Vulnerability | Degradation Dynamics |
| :--- | :--- | :--- | :--- |
| `turbofan-core` | `engine` | FOD/fragment ingestion into compressor/turbine | Thrust drops to zero; engine fire; hydraulic circuit pressure drop. |
| `flight-control-hydraulics`| `machinery`| Triple-redundant lines along wing spar/keel | Pressure bleed: control surfaces lock to neutral; flight envelope shrinks $80\%$. |
| `wing-spar-left` | `structure`| Main load-bearing aluminum/carbon-fiber spar | $G$-limit drops from $9.0\text{ G}$ to $2.5\text{ G}$; structural failure if turn attempted at $>250\text{ kts}$. |
| `internal-weapons-bay` | `weapons-station`| Pneumatic bay doors & ejector trapeze | Bay doors jam open (massive drag, $+300\%$ radar cross section) or jam closed (cannot release). |
| `radar-radome` | `radar` | AESA radar in composite nosecone | Forward situational awareness blinded; radar-guided missiles cannot update datalink. |
| `in-flight-refuel-probe` | `fuel` | Retractable probe / dorsal UARRSI receptacle | Unable to take aerial tanker fuel; mission endurance limited to internal fuel. |
| `stovl-lift-fan` (*F-35B*) | `propulsion`| 29,000 lbf shaft-driven two-stage counter-rotating fan | VTOL/STOVL landing disabled; must divert to full-length conventional runway ($2,000\text{ m}$). |

---

## 3. Structure Damage Zones & Critical Infrastructure Vulnerability

In contrast to crude overall HP reduction, realistic military/industrial structures and fortifications are discrete physical assemblies. Targeting specific zones cripples operational capability without requiring total demolition of the reinforced concrete superstructure.

```
+-----------------------------------------------------------------------------------+
|                        TACTICAL COMMAND CENTER (HQ COMMAND)                       |
|                                                                                   |
|  [Zone 1: SATCOM & Sensor Mast]  ---------> Vulnerable to HE blast / shrapnel      |
|  (Exposed, Height +25m)                     Disables tactical minimap / radar     |
|                                                                                   |
|  [Zone 2: HVAC & NBC Chiller]   ----------> Vulnerable to mortar / strafing        |
|  (Exterior pad, Ground level)               Evacuates personnel within 60s        |
|                                                                                   |
|  [Zone 3: Diesel Gen / Fuel Pad] ---------> Secondary explosion hazard            |
|  (Soft enclosure, Ground level)             Forces HQ to emergency battery (180s) |
|                                                                                   |
|  [Zone 4: Hardened Operations Vault] -----> 2.5m Reinforced Concrete / Earth Berm |
|  (Underground, -5m Depth)                   Requires Bunker-Buster / Heavy Siege  |
+-----------------------------------------------------------------------------------+
```

### 3.1 Structure Damage Zone Decomposition

| Structure Type | Zone ID | Vulnerability Zone | Armor ($RHA_e$ / Concrete) | Failure / Incapacitation Effect |
| :--- | :--- | :--- | :--- | :--- |
| **Power Plant** *(Reactor Block / Fusion Yard / Generator Shed)* | `turbine-hall` | Turbine steam pipes & generator stator | $30\text{ mm}$ steel | High-pressure steam rupture ($8\text{ HP/s}$ AOE damage to nearby infantry); power output drops $100\%$. |
| | `transformer-yard` | High-voltage step-up transformers | $12\text{ mm}$ steel | Instant transformer oil fireball; total grid blackout for player faction in sector. |
| | `cooling-loop` | Cooling towers / heat exchangers | $15\text{ cm}$ concrete | Emergency thermal scram triggered within $60\text{ s}$; power generation throttles to $0$. |
| **Factory / Foundry** *(Motor Pool / Armored Works / Automated Foundry)* | `assembly-crane` | Overhead bridge crane & gantry rails | $25\text{ mm}$ structural | Heavy vehicle production paused; units currently in queue frozen at build stage. |
| | `tooling-line` | CNC milling centers & robotic weld cells | $20\text{ mm}$ internal | Vehicle build time increased by $+150\%$; unit spawn health starts at $70\%$. |
| | `material-hopper`| Raw titanium/steel ingots & slag feed | $50\text{ mm}$ steel | Ingot hopper breach blocks exit apron; manufactured vehicles cannot roll out. |
| **Airfield / Base** *(Flight Wing / Forward Airstrip / Helipad)* | `runway-strip` | Cratered asphalt/concrete runway slab | $40\text{ cm}$ concrete | Fixed-wing operations suspended; taxiing jets take $100\%$ catastrophic gear collapse. |
| | `fuel-farm` | Above-ground POL bladder / steel tanks | $8\text{ mm}$ steel | Massive fuel deflagration ($50\text{ m}$ radius); stops all aircraft refuel operations. |
| | `radar-atc-mast` | Air traffic control tower & TACAN array | $10\text{ mm}$ composite | Aircraft landing cadence throttled; airborne assets enter holding pattern ($+200\text{ kts}$ burn). |
| | `hardened-shelter` | Earth-bermed concrete revetment / HAS | $1.8\text{ m}$ rebar conc | Protects parked aircraft from cluster bombs and submunitions up to $1,000\text{ lb}$. |
| **Command & Control** *(HQ Command / Central Directorate / Deep Command Post)* | `c2-antenna-mast` | High-frequency / SATCOM parabolic arrays | $10\text{ mm}$ exposed | Tactical uplink lost: radar coverage blinded, off-map artillery call-ins disabled. |
| | `backup-gen` | Backup diesel generators & battery banks | $15\text{ mm}$ steel | Emergency power cuts after $90\text{ s}$; mini-map fog-of-war returns to total blackout. |
| | `command-vault` | Underground command staff bunker | $3.0\text{ m}$ rebar conc | Loss of structure eliminates faction command presence; field morale collapses. |
| **Fortification / Ammo Depot** *(Strategic Vault / Service Bunker / Earthshaker Vault)* | `magazine-bunker` | High-explosive ordnance storage revetment | $2.2\text{ m}$ rebar conc | Catastrophic sympathetic detonation: $150\text{ m}$ shockwave destroys adjacent buildings. |
| | `blast-doors` | Heavy hydraulic rolling steel blast doors | $120\text{ mm}$ RHA steel | Doors jam shut: trapped units cannot egress; or blast doors breached, exposing interior. |
| | `tunnel-portal` | Underground access shaft / rail link | $1.5\text{ m}$ rock/conc | Portal collapse traps subterranean units; ventilation airflow drops ($2\text{ HP/s}$ suffocation). |

---

## 4. Empirical Mechanical Reliability, Wear, and MTBF Standards

Military vehicle mechanical reliability is governed by rigorous statistical distributions (Weibull and log-normal distributions) derived from operational test data.

### 4.1 Authoritative Failure Rates & MTBF Metrics
*Primary Sources: US Army Materiel Systems Analysis Activity (AMSAA), Operational Test and Evaluation (DOT&E) Annual Reports, US Army Field Manual FM 4-30, RAND Corporation Arroyo Center Heavy Armor Studies.*

| Platform Category | Representative Systems | Mean Miles Between System Abort (MMBSA) | Mean Time Between Critical Failure (MTBCF) | Scheduled Depot Inspection Interval | Engine Run-Life Before Rebuild |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Heavy MBT (Gas Turbine)** | M1A2 SEPv3 Abrams | $320\text{ miles}$ ($515\text{ km}$) | $42\text{ operating hours}$ | $1,200\text{ miles}$ ($1,930\text{ km}$) | $1,000\text{ engine hours}$ |
| **Heavy MBT (Diesel)** | Leopard 2A7, T-72B3M | $480\text{ miles}$ ($772\text{ km}$) | $58\text{ operating hours}$ | $1,500\text{ miles}$ ($2,414\text{ km}$) | $1,500\text{ engine hours}$ |
| **Tracked IFV** | M2A4 Bradley | $360\text{ miles}$ ($579\text{ km}$) | $48\text{ operating hours}$ | $1,000\text{ miles}$ ($1,609\text{ km}$) | $1,200\text{ engine hours}$ |
| **Wheeled 8x8 APC** | Stryker, LAV-25, Jackal | $1,050\text{ miles}$ ($1,690\text{ km}$) | $110\text{ operating hours}$ | $3,500\text{ miles}$ ($5,632\text{ km}$) | $3,000\text{ engine hours}$ |
| **Wheeled Tactical 4x4** | JLTV, Humvee, Technical | $1,400\text{ miles}$ ($2,253\text{ km}$) | $145\text{ operating hours}$ | $4,500\text{ miles}$ ($7,242\text{ km}$) | $4,000\text{ engine hours}$ |
| **Attack Helicopter** | AH-64E, AH-1Z | N/A ($140\text{ flight hrs}$) | $12.5\text{ flight hours}$ | $250\text{ flight hours}$ (Phase) | $1,200\text{ engine hours}$ |
| **Heavy Lift Helicopter** | CH-53K, CH-47F | N/A ($180\text{ flight hrs}$) | $14.2\text{ flight hours}$ | $200\text{ flight hours}$ (Phase) | $1,500\text{ engine hours}$ |
| **Strike Jet (Conventional)** | A-10C, F-16C | N/A ($210\text{ flight hrs}$) | $18.0\text{ flight hours}$ | $300\text{ flight hours}$ (Depot) | $2,000\text{ engine hours}$ |
| **5th Gen STOVL Strike Jet** | F-35B Lightning II | N/A ($95\text{ flight hrs}$) | $6.8\text{ flight hours}$ | $150\text{ flight hours}$ (Special) | $800\text{ engine hours}$ |

### 4.2 Terrain & Environmental Wear Multipliers
Mechanical degradation is an exponential function of surface resistance, abrasive particulates, and thermal stress. The base mechanical wear rate $W_{\text{base}}$ ($0.02\%\text{ per second of continuous travel}$) is modified by:

$$\dot{W} = W_{\text{base}} \times M_{\text{terrain}} \times M_{\text{weather}} \times M_{\text{load}}$$

| Surface / Terrain Type | Tracked Vehicle Multiplier ($M_{\text{terrain}}$) | Wheeled Vehicle Multiplier ($M_{\text{terrain}}$) | Primary Mechanical Failure Mode |
| :--- | :--- | :--- | :--- |
| **Paved Road / Concrete** | $0.25\times$ | $0.20\times$ | Track pad rubber peeling / tire tread wear |
| **Hardpacked Dirt / Gravel** | $1.00\times$ (Baseline) | $1.00\times$ (Baseline) | Shock absorber fatigue, air filter dust loading |
| **Fine Desert Sand / Dunes** | $2.80\times$ | $2.20\times$ | Turbine blade erosion, seal scouring, cooling clogging |
| **Rocky / Talus / Broken Slag** | $3.50\times$ | $4.20\times$ | Thrown track, torn tire sidewalls, steering arm fracture |
| **Deep Mud / Bog / Silt** | $4.50\times$ | $8.50\times$ | Transmission clutch slip, differential overheat, hub seal breach |
| **River Fording (>1.2m Depth)** | $3.00\times$ | $5.00\times$ | Water ingestion, alternator short, axle oil emulsion |

| Weather Tier | Dust / Salt Index | Cooling Stress | Aircraft Wear Multiplier | Ground Wear Multiplier ($M_{\text{weather}}$) |
| :--- | :--- | :--- | :--- | :--- |
| `clear_dry` | Minimal | Baseline ($25^\circ\text{C}$) | $1.0\times$ | $1.0\times$ |
| `extreme_heat` ($>45^\circ\text{C}$) | Moderate | Severe ($+40\%\text{ coolant temp}$) | $1.8\times$ | $1.6\times$ (Vapor lock, hydraulic oil foaming) |
| `sandstorm` (Khamaseen) | Extreme silica | Blocked air pre-cleaners | $6.5\times$ (Turbine erosion) | $3.8\times$ (Clogged intakes, seized bearings) |
| `monsoon_downpour` | Zero dust | Washout | $1.3\times$ (Pitot ice/sensor wash) | $2.4\times$ (Deep mud immersion) |
| `freezing_ice` ($<-20^\circ\text{C}$) | Zero dust | Extreme brittleness | $2.5\times$ (Rotor icing, seal cracks)| $2.2\times$ (Frozen roadwheels, battery $-60\%$) |

---

## 5. Failure Taxonomy and Progressive Degradation States

In place of arbitrary instant immobilization, mechanical wear manifests through three progressive degradation tiers prior to terminal failure:

```
+-------------------+      +-------------------+      +-------------------+      +-------------------+
|  OPTIMAL (100-80%) | ===> | DEGRADED (80-40%) | ===> | CRITICAL (40-1%)  | ===> | STALLED (0%)      |
|  Full performance |      | -15% Speed        |      | -50% Speed        |      | Total Immobile    |
|  No derating      |      | Minor track squeal|      | Severe overheating|      | Repair required   |
+-------------------+      +-------------------+      +-------------------+      +-------------------+
```

### 5.1 Degradation States
1. **Tier 1: Nominal ($100\%\text{ to }80\%$ Reliability):**
   * Top speed $100\%$, acceleration $100\%$, fuel burn nominal.
2. **Tier 2: Worn ($79\%\text{ to }40\%$ Reliability):**
   * Transmission hunting / clutch shudder: top speed capped at $85\%$.
   * Engine running hot: fuel consumption increased by $+25\%$.
   * Track tension loose: turning radius widened by $+35\%$.
3. **Tier 3: Critical / Failure Imminent ($39\%\text{ to }1\%$ Reliability):**
   * Thermal derating: engine governor clamps output to $50\%$.
   * Sputtering / misfire: occasional $0.5\text{ s}$ power interruptions during hill climb.
   * Suspension bottoming out: accuracy on the move degrades by $50\%$.
4. **Tier 4: Mechanical Failure ($0\%$ Reliability or Catastrophic Event):**
   * Platform immobilized (`isStalled = true`).
   * Specific failure reason determined by platform automotive architecture:
     * **Tracked Vehicles:** `thrown_track` ($65\%$), `broken_transmission` ($25\%$), `final_drive_seizure` ($10\%$).
     * **Wheeled Vehicles:** `blown_differential` ($45\%$), `sheared_axle` ($35\%$), `engine_hydrolock` ($20\%$).
     * **Rotary Aviation:** `transmission_loss_of_lubrication` ($50\%$), `compressor_stall` ($50\%$).
     * **Fixed-Wing:** `hydraulic_dual_bleed` ($40\%$), `turbine_flameout` ($60\%$).

---

## 6. Maintenance, Recovery, and Logistics Doctrine

### 6.1 Echelons of Maintenance (FM 4-30 / NATO Standard)
* **Crew Maintenance (O-Level - 1st Echelon):**
  * Performed by vehicle crew in the field.
  * *Permitted Operations:* Track retensioning, clearing jammed roadwheel stones, basic fluid top-off, changing tires on wheeled vehicles, clearing weapon feed jams.
  * *Constraints:* Vehicle must be stationary; cannot be under fire ($8\text{ s}$ quiet window); restores reliability up to maximum ceiling of $65\%$; cannot fix broken transmission or thrown track without external parts.
* **Field Maintenance (I-Level - 2nd Echelon):**
  * Performed by dedicated recovery and repair assets (Atlas Recovery Rig, Convoy Repairer, D9 Bulldozer, Wandering Engineer, Repair Depot).
  * *Permitted Operations:* Breaking and re-pinning thrown tracks, pulling and swapping power packs (engine/transmission drop), replacing main gun barrels, structural patch welding.
  * *Cost & Timing:* Requires $1\text{ to }2$ spare part crates; consumes $15\text{–}30\text{ seconds}$; restores vehicle to $95\%$ reliability.
* **Depot Maintenance (D-Level - 3rd Echelon):**
  * Performed at dedicated bases (Motor Pool, Armored Works, Repair Depot).
  * *Permitted Operations:* Complete overhaul, internal blowout magazine refit, composite armor module replacement, sensor realignment. Restores vehicle to $100\%$ pristine factory state.

### 6.2 Ammunition Stowage & Ready-Rack Dynamics
* **Ready-Rack vs Hull Stowage:**
  * Modern combat vehicles divide ammo between the **Ready Rack** (turret bustle / autoloader magazine) and **Hull Reserve Stowage**.
  * Ready Rack provides maximum cadence ($1\text{ round every 5 s}$). When depleted, firing stops while crew transfers rounds from hull stowage ($1\text{ round transferred every 18 s}$ under armor).
* **Blowout Panels & Survivability:**
  * If ready rack is penetrated, blowout panels vent detonation upward and rearward away from the fighting compartment, venting ammunition without killing the crew or destroying the hull. Vehicle loses all ammo but retains mobility and communications.
  * Soviet-style carousel autoloaders (T-72 / T-90) lack blowout isolation; any penetrating hull hit to the carousel produces immediate catastrophic turret separation (Jack-in-the-box effect) and total crew destruction.

---

## 7. Audit Question Bank for Simulation Review

Use these 20 authoritative questions to evaluate any game engine or RTS implementation of subsystems, mechanical wear, logistics, and structures:

1. **Dimensional Scaling:** Are hit volumes, blast radiuses, and weapon ranges modeled in true $1\text{ unit} = 1\text{ meter}$ scale, or are vehicles compressed into abstract collision points?
2. **Internal vs External Partition:** Does the projectile raycast explicitly distinguish between external exposed appendages (optics, antennas, tracks) and internal core compartments (ammo, engine, crew)?
3. **Overkill Spillover:** Does subsystem damage subtract directly from platform hull health, or is hull health independently evaluated with bounded fire/spall bleed?
4. **Wheeled vs Tracked Differentiation:** Does the mobility model distinguish between a multi-axle wheeled vehicle (which can run with 1–2 flat tires) and a tracked vehicle (which becomes instantly disabled upon losing a single track pin)?
5. **Progressive vs Binary Degradation:** Does mechanical wear degrade vehicle speed and handling continuously, or does the unit operate at $100\%$ until an arbitrary zero-reliability cliff creates instant freezing?
6. **Terrain Impact on Automotive Powertrain:** Are tracked vehicles subjected to higher fuel consumption ($2\text{–}3\times$) and transmission wear in deep mud compared to highway transit?
7. **Autoloader Vulnerability vs Bustle Blowout:** Does penetrating an isolated bustle magazine trigger blowout venting, or does the entire vehicle instantaneously explode?
8. **Structure Zone Decomposition:** Can a high-value industrial structure (Power Plant, Factory) be neutralized by targeting soft external support zones (cooling towers, transformer yard, gantry cranes) without demolishing the reinforced concrete frame?
9. **Secondary Explosion Physics:** Does the destruction of an ammunition storage bunker, MLRS battery, or fuel farm generate realistic area-of-effect blast waves that damage proximate friendly units?
10. **Hydraulic vs Electrical Degradation:** Does a hit to an aircraft or tank hydraulic circuit disable high-speed powered slew while retaining emergency manual mechanical backup?
11. **Sensor vs Armament Decoupling:** When a platform's primary mast sight or radar is knocked out, does the weapon still fire with gross unguided dispersion, or does the platform magically forget how to shoot?
12. **Flight Envelope Integrity:** Does structural damage to an aircraft wing spar impose dynamic $G$-force limits that snap the wing if violent maneuvers are executed?
13. **Engine Run-Dry Endurance:** Does an oil leak or radiator puncture cause instant engine seizure, or does the platform have a realistic $3\text{–}5\text{ minute}$ run-dry thermal window before total catastrophic lockup?
14. **Recovery Asset Requirements:** Can a stranded tank with a thrown track repair itself in the open desert, or does it require an engineering recovery vehicle (ARV/M88/Atlas) with winch and spare track links?
15. **Ammunition Ready-Rack Transfer:** Is ready-rack replenishment modeled with a realistic throughput bottleneck when drawing from deep hull storage?
16. **Thermal Blooming & METOC Interaction:** Does atmospheric moisture, rain, or dust attenuate directed energy weapons (lasers) in accordance with the Beer-Lambert law?
17. **Deterministic Randomness:** Are mechanical breakdown probabilities evaluated using seeded, replay-safe pseudo-random sequences rather than unseeded `Math.random()` calls?
18. **Continuous vs Discrete Fire Spread:** Does fire spread between adjacent internal compartments on synchronized, fixed-step sub-ticks rather than frame-rate-dependent update delta loops?
19. **Field Maintenance Ceilings:** Are field crew repairs capped at a realistic field expedient limit ($60\text{–}70\%$), requiring return to a dedicated depot for complete $100\%$ restoration?
20. **Runway Denial Operations:** Does cratering an airfield runway physically prohibit fixed-wing flight operations until combat engineering units lay crater-repair mats?
