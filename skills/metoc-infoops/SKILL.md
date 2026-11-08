---
name: metoc-infoops
description: >-
  Authoritative engineering and operational standard for Military Meteorology & Oceanography (METOC:
  precipitation, sea state, bathymetry, mud trafficability, sensor/laser attenuation, river hydrology)
  and Information Operations / Public Legitimacy (Law of Armed Conflict, ROE, media/lawfare, coalition export logistics).
---

# Military Meteorology/Oceanography (METOC) & Information Operations Standard

This standard establishes the operational physics, empirical data tables, deterministic mathematical models, and legal-institutional frameworks governing environmental warfare and strategic information operations for deterministic military simulations (30 Hz lockstep).

---

## 1. Military Meteorology & Atmospheric Attenuation

### 1.1 Precipitation & Weather Tiers
Atmospheric water content degrades combat operations across four distinct physical vectors: mechanical traction loss, hydrological river swell, optical/infrared sensor extinction, and directed-energy beam thermal blooming.

| Tier Code | Operational State | Rainfall Rate ($R$) | Water Level Delta ($\Delta h$) | Optical Vis Range | Relative Humidity ($RH$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `clear_dry` | Clear / Arid | $0.0\text{ mm/hr}$ | $-0.85\text{ m}$ ($-2.8\text{ ft}$) | $\ge 20,000\text{ m}$ | $< 35\%$ |
| `temperate` | Baseline Overcast | $0.0 - 0.5\text{ mm/hr}$ | $0.0\text{ m}$ ($0.0\text{ ft}$) | $10,000 - 15,000\text{ m}$ | $50 - 65\%$ |
| `light_rain` | Steady Precipitation | $1.0 - 4.0\text{ mm/hr}$ | $+0.55\text{ m}$ ($+1.8\text{ ft}$) | $4,000 - 7,000\text{ m}$ | $80 - 90\%$ |
| `monsoon_downpour` | Heavy Squall / Storm | $15.0 - 50.0\text{ mm/hr}$ | $+1.28\text{ m}$ ($+4.2\text{ ft}$) | $1,000 - 2,500\text{ m}$ | $95 - 100\%$ |
| `flash_flood` | Torrential / Hydrological Outflow | $> 75.0\text{ mm/hr}$ | $+2.29\text{ m}$ ($+7.5\text{ ft}$) | $< 800\text{ m}$ | $100\%$ |

*Sources: NATO STANAG 4103 (Allied Reliability and Maintainability Guidelines for Climatic Conditions); US Army FM 3-100.4 (Environmental Considerations in Military Operations); World Meteorological Organization (WMO) Technical Regulations No. 49.*

---

### 1.2 Multi-Spectral Sensor Degradation: Visible EO vs. LWIR/FLIR vs. Synthetic Aperture Radar (SAR)
Atmospheric transmission obeys the Beer-Lambert extinction law:
$$I = I_0 \cdot e^{-\gamma(\lambda) \cdot d}$$
where $\gamma(\lambda)$ is the total extinction coefficient (absorption + scattering) at wavelength $\lambda$, and $d$ is path length.

1. **Electro-Optical (EO: Visible Band, $\lambda = 0.4 - 0.7\ \mu\text{m}$):**
   - Mie scattering predominates when aerosol droplet diameter approaches wavelength ($r \approx \lambda$).
   - Dust particles ($r \approx 1 - 10\ \mu\text{m}$) cause catastrophic visible washout (multiplier $\approx 0.35$).
   - Rain droplets ($r \approx 0.5 - 3\text{ mm}$) scatter visible light moderately (multiplier $\approx 0.60$).
2. **Forward-Looking Infrared (FLIR / LWIR: Thermal Band, $\lambda = 8 - 14\ \mu\text{m}$):**
   - Penetrates dry airborne mineral dust effectively due to Rayleigh regime shift ($r \ll \lambda$, multiplier $\approx 0.75$).
   - **Severe Wet Washout:** Liquid water has strong absorption bands in 8–14 $\mu$m. Furthermore, continuous rain causes evaporative cooling and uniform surface water filming, collapsing target-to-background thermal contrast ($\Delta T \to 0$, multiplier $\approx 0.35$).
3. **Synthetic Aperture Radar (SAR: X-band $\approx 3\text{ cm}$, Ku-band $\approx 1.8\text{ cm}$):**
   - Immune to cloud cover and rain extinction; provides all-weather surface and bathymetric reconnaissance.

| Environmental Contaminant | EO Visible Multiplier | LWIR / FLIR Multiplier | SAR Radar Multiplier | Dominant Physical Mechanism |
| :--- | :--- | :--- | :--- | :--- |
| **Clear Atmosphere** | $1.00$ | $1.00$ | $1.00$ | Molecular Rayleigh scattering only |
| **Blowing Sand / Dust Squall** | $0.35$ | $0.75$ | $0.98$ | Mie scattering on mineral particulates |
| **Advection Fog ($>95\%\ RH$)** | $0.15$ | $0.20$ | $0.95$ | Dense small-droplet scattering ($r \approx 2-5\ \mu\text{m}$) |
| **Heavy Rain ($>25\text{ mm/hr}$)** | $0.60$ | $0.35$ | $0.90$ | Large droplet rain scatter + $\Delta T$ thermal contrast collapse |

*Sources: US Naval Research Laboratory (NRL) Report 8345; AFGL-TR-85-0015 (Atmospheric Transmittance/Radiance Computer Code LOWTRAN 6); J.R. Hummel & E.P. Shettle, Effects of Atmospheric Water on Electro-Optical Sensors.*

---

### 1.3 High-Energy Lasers (HEL) & Thermal Blooming
Directed-energy weapons (e.g., Iron Beam, HELIOS, 100–300 kW continuous wave ytterbium fiber lasers operating at $\lambda = 1.064\ \mu\text{m}$) are subject to molecular absorption, aerosol scattering, and **thermal blooming**.

1. **Linear Attenuation:**
   $$\gamma_{\text{ext}} = \alpha_{\text{abs}} + \beta_{\text{scat}}$$
   In heavy rainfall, beam extinction reaches $75\%$ power loss over $1.5\text{ km}$ ($P_{\text{deliv}} = 0.25$). In dense fog, droplet scattering reduces transmitted flux to $<5\%$ ($P_{\text{deliv}} = 0.05$).
2. **Thermal Blooming (Non-Linear Self-Defocusing):**
   Absorption of laser power heats the air cylinder enclosing the beam. Heated air expands, reducing air density and creating a negative refractive index gradient ($dn/dT < 0$). The beam acts as a negative diverging lens, blooming outward and collapsing peak on-target irradiance ($W/\text{cm}^2$).
   - **The Crosswind Mitigation Paradox:** Thermal blooming is **most catastrophic in zero wind (still air)** because heated air remains stationary in the beam channel.
   - **Crosswind ($v_{\perp} > 5\text{ m/s}$)** sweeps heated air out of the optical path, refreshing the channel with cool ambient air and **mitigating thermal blooming**, restoring laser dwell efficiency.

*Sources: Gebhardt, F.G., "Twenty-five years of thermal blooming: an overview", SPIE Vol. 1221; Smith, D.C., "High-Power Laser Propagation: Thermal Blooming", Proc. IEEE 65; DoD Directive 3000.09.*

---

## 2. Terrain Trafficability, Soil Mechanics & Fording

### 2.1 NATO Reference Mobility Model (NRMM) & Cone Index
Vehicle mobility off-road is determined by soil shearing strength, measured via the **Cone Index (CI)** and **Vehicle Cone Index (VCI)**:
- $CI > VCI_1$: Vehicle can traverse 1 pass without immobilizing.
- $CI > VCI_{50}$: Vehicle can sustain 50 passes without severe ruts.
- **Remolding Index (RI):** In cohesive silts and clays, vehicle trafficking destroys soil structure; moisture saturation drops the Rating Cone Index ($RCI = CI \times RI$) below $VCI$, producing immediate bogging.

### 2.2 Wheeled vs. Tracked Trafficability in Mud
1. **Pneumatic Wheeled Vehicles (HMMWV, JLTV, HEMTT, Logistic Vans):**
   - High nominal ground pressure ($180 - 350\text{ kPa}$).
   - Narrow contact patch prone to sinkage ($z > 0.4 \times d_{\text{tire}}$). Once axle housings drag in mud, rolling resistance spikes exponentially ($R_r \propto z / D$).
   - **Off-road speed loss:** $50\%$ in rain, $80\%$ in storm downpour, $90\%$ in flash flood conditions.
   - **Exemption Rule:** Hard paved asphalt, concrete, and engineered military bridges maintain $1.0\times$ speed regardless of rain.
2. **Tracked Armored Fighting Vehicles (M1A2 Abrams, Merkava Mk IV, Namer, Bradley):**
   - Low nominal ground pressure ($70 - 110\text{ kPa}$).
   - Wide track distribution prevents catastrophic belly sinkage but track teeth churn saturated mud into viscous sludge.
   - **Speed loss:** $30\%$ in rain, $45\%$ in storm, $60\%$ in flash flood.
   - **Fuel Consumption Surge:** Track churn and mechanical resistance increase power draw by $1.5\times$ (rain), $2.2\times$ (storm), up to $3.0\times$ (flood).
   - **Mechanical Wear Surge:** Soil quartz abrasives enter final drive seals and track pins, accelerating wear by $+50\%$.

| Vehicle Configuration | Contact Ground Pressure | Clear/Dry Speed | Light Rain Speed | Monsoon Downpour Speed | Mud Fuel Burn Factor |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **All Vehicles (Paved Roads)** | N/A | $1.00\times$ | $1.00\times$ | $1.00\times$ | $1.00\times$ |
| **Tracked MBT / APC (Off-road)** | $80 - 105\text{ kPa}$ | $1.00\times$ | $0.70\times$ | $0.55\times$ | $1.5 - 3.0\times$ |
| **Wheeled 8x8 / 4x4 (Off-road)** | $190 - 320\text{ kPa}$ | $1.00\times$ | $0.50\times$ | $0.20\times$ | $1.2 - 1.8\times$ |
| **Infantry Dismounts (Wet Silt)** | $35 - 50\text{ kPa}$ | $1.00\times$ | $0.80\times$ | $0.65\times$ | $1.35 - 1.50\times$ (Rations) |

*Sources: US Army Engineer Waterways Experiment Station (WES) Technical Report GL-92-19 (NRMM II Development); Bekker, M.G., Introduction to Terrain-Vehicle Systems; Wong, J.Y., Theory of Ground Vehicles.*

---

### 2.3 River Bathymetry & Authoritative Vehicle Fording Standards
Vehicles cannot ford rivers exceeding their maximum safe wading depth. Exceeding unprepared limits without a deep-water fording kit (DWFK) ingests water into turbochargers, air boxes, and combustion chambers, causing catastrophic hydraulic lock ($HP \to 0$, permanent stall).

```
          SURFACE WATERLINE
~~~~~~~~~~~~~~~~~▼~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                 |
  [0.76m - 1.07m]| HMMWV / Paladin Unprepared Safe Ford
                 |---------------------------------------- (Warning Alert)
  [1.14m - 1.38m]| M2 Bradley / D9 / M1A2 / Merkava Unprepared Safe Ford
                 |---------------------------------------- (Critical Threshold)
  [1.52m - 1.98m]| HMMWV (Kit) / Abrams (DWFK Snorkel Kit)
                 |---------------------------------------- (Drown Line)
  [> 2.00m]      | Deep River Channel / Bathymetric Trench (SWAMP / DROWN VEHICLE)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

| Vehicle Platform | Unprepared Safe Depth | Deep Fording Kit (DWFK) | Citations & Technical Manuals |
| :--- | :--- | :--- | :--- |
| **M1A1 / M1A2 Abrams** | $1.22\text{ m}$ ($4.0\text{ ft}$) | $1.98\text{ m}$ ($6.5\text{ ft}$) | US Army FM 3-20.15; TM 9-2350-264-10-1; ATP 3-90.4 §4-12 |
| **Merkava Mk IV** | $1.38\text{ m}$ ($4.5\text{ ft}$) | N/A (Standardized Hull) | IDF MANTAK Technical Directives; Armored Corps Tech Spec |
| **Namer Heavy APC** | $1.30\text{ m}$ ($4.2\text{ ft}$) | N/A (Sealed Hull) | IDF Ordnance Corps Technical Bulletin (Namer CEV/APC) |
| **M2A2/M3A2 Bradley** | $1.14\text{ m}$ ($3.8\text{ ft}$) | **NOT AMPHIBIOUS** | TM 9-2350-252-10-1 (Swim barrier deleted on M2A2+) |
| **HMMWV (M1151)** | $0.76\text{ m}$ ($2.5\text{ ft}$) | $1.52\text{ m}$ ($5.0\text{ ft}$) | US Army TM 9-2320-280-10 §2-14 |
| **HEMTT 8x8 (M977)** | $1.22\text{ m}$ ($4.0\text{ ft}$) | N/A | US Army TM 9-2320-279-10 §2-21 |
| **IDF Caterpillar D9 Doobi** | $1.22\text{ m}$ ($4.0\text{ ft}$) | N/A | CAT D9R/T Manual; final drive seals & lower track shoe limit |
| **M109A6 Paladin SPH** | $1.07\text{ m}$ ($3.5\text{ ft}$) | N/A | US Army TM 9-2350-314-10 |

---

### 2.4 Military Bridging & Military Load Class (MLC)
Military bridging equipment is rated under STANAG 2021 Military Load Classification (MLC). Vehicles whose MLC exceeds bridge capacity cause structural failure or bridge collapse.

| Bridging System | Deploy Time | Span MLC | Max Allowed Armor | Structural HP | Operational Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AVLB Scissor Bridge** | $20.0\text{ s}$ | **MLC 35** | Light/Wheeled, Dismounts | $300\text{ HP}$ | Fast assault deployment; cannot support MBTs ($MLC > 70$). |
| **IRB Ribbon Pontoon** | $45.0\text{ s}$ | **MLC 70** | IFV, Paladin, Medium | $450\text{ HP}$ | Multi-bay floating raft; supports Bradley/Paladin. |
| **MGB Medium Girder** | $90.0\text{ s}$ | **MLC 90** | Heavy MBT (Abrams, Merkava) | $600\text{ HP}$ | Heavy alloy truss; full main battle tank clearance. |
| **Bailey Truss Bridge** | $150.0\text{ s}$ | **MLC 120** | Heavy Transports & Armor | $800\text{ HP}$ | High-capacity semi-permanent steel modular truss. |

*Sources: NATO STANAG 2021 (Military Load Classification of Bridges, Ferries and Vehicles); US Army ATP 3-90.4 / MCWP 3-17.8.*

---

## 3. Naval Oceanography & Sea State Scale

The World Meteorological Organization (WMO) and Douglas Sea State scales define wave spectra, platform pitch/roll accelerations, and naval operational limits.

```
       SEA STATE SPECTRUM & OPERATIONAL ENVELOPES
=====================================================================
SS 0-2 (0.0 - 0.5m) | CALM: Full Flight Ops, Well Deck Wet/Dry Open
SS 3   (0.5 - 1.25m)| SLIGHT: Nominal Fixed/Rotary Flight Ops
SS 4   (1.25 - 2.5m)| MODERATE: Rotary Ops Degraded; Well Deck Swell Warning
SS 5   (2.5 - 4.0m) | ROUGH: LCAC Ops HALTED (Cushion Broaching); STOVL Restr
SS 6   (4.0 - 6.0m) | VERY ROUGH: FLIGHT DECK EMPTY TIEDOWN PROTOCOL
SS 7+  (> 6.0m)     | HIGH/PHENOMENAL: Hull Survival Mode; Sonar Baffled
=====================================================================
```

| Sea State (WMO) | Significant Wave Height ($H_{1/3}$) | Wind Velocity (kts) | Pitch / Roll Accelerations | Naval Aviation Status | Well Deck & LCAC Operations | Acoustic / Sonar Impact |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SS 0–2** | $0.0 - 0.5\text{ m}$ | $0 - 10\text{ kts}$ | $< 1.0^\circ$ roll, $< 0.5^\circ$ pitch | **Full Flight Ops:** Unrestricted launch & trap. | **Full Ops:** Dry/wet well staging; LCAC transit unrestricted. | Optimal acoustic conditions; minimum ambient wave noise. |
| **SS 3** | $0.5 - 1.25\text{ m}$ | $11 - 16\text{ kts}$ | $1.0 - 2.5^\circ$ roll, $< 1.0^\circ$ pitch | **Nominal Flight Ops:** Routine carrier ops. | **Nominal Ops:** LCAC cushion ingress safe. | Baseline Knudsen surface noise curve. |
| **SS 4** | $1.25 - 2.5\text{ m}$ | $17 - 21\text{ kts}$ | $3.0 - 5.5^\circ$ roll, $1.5 - 2.5^\circ$ pitch | **Degraded Rotary:** Helo rotor start/stop envelope restricted. | **Restricted:** Well deck surging; ballast trim carefully monitored. | Ambient sea surface noise $+6\text{ dB}$; bubble sweepdown onset. |
| **SS 5** | $2.5 - 4.0\text{ m}$ | $22 - 27\text{ kts}$ | $6.0 - 9.0^\circ$ roll, $3.0 - 4.5^\circ$ pitch | **Restricted Operations:** STOVL / CATOBAR emergency recovery only. | **HALTED:** Well deck closed; LCAC cushion broaching hazard. | Hull-mounted sonar degraded $-40\%$; cavitation noise elevation. |
| **SS 6** | $4.0 - 6.0\text{ m}$ | $28 - 40\text{ kts}$ | $10.0 - 15.0^\circ$ roll, $5.0 - 7.5^\circ$ pitch | **SHUT DOWN:** Flight deck cleared; aircraft chained to deck tie-downs. | **PROHIBITED:** Stern gate sealed to prevent flooding swamping. | Sonar baffled by surface bubble clouds; towed array depth unstable. |
| **SS 7+** | $> 6.0\text{ m}$ | $> 41\text{ kts}$ | $> 15^\circ$ roll, $> 8^\circ$ pitch | **SURVIVAL MODE:** No flight deck activity permitted. | **SEALED:** Emergency hull watertight integrity. | Total surface acoustic blackout. |

*Sources: NATO STANAG 4194 (Standardised Wave and Wind Environments for Military Equipment); US Navy OPNAVINST 3120.32D; WMO Sea State Code Table 3700.*

---

## 4. Deterministic Weather State Machine Architecture

### 4.1 Replay Determinism & Pseudo-Random Number Generation
A simulation running in 30 Hz lockstep cannot utilize system clock (`Date.now()`) or non-reproducible PRNGs (`Math.random()`). It must rely on a **seeded 32-bit integer PRNG** (e.g. Mulberry32) initialized exclusively from match parameters:
$$\text{Seed} = \text{hash}(\text{MatchSeed}, \text{TheaterId})$$

```typescript
export function createMulberry32(seed: number): () => number {
  let s = seed >>> 0;
  return () => {
    s = (s + 0x6d2b79f5) >>> 0;
    let t = Math.imul(s ^ (s >>> 15), 1 | s);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
```

### 4.2 Deterministic Markov Transition Matrix
Weather cycles progress through a discrete-time Markov chain evaluated at periodic intervals ($T_{\text{cycle}} \approx 90 - 120\text{ seconds}$). State transitions are constrained to adjacent tiers (no direct jump from `clear_dry` to `flash_flood` without progressing through rain):

```
       MARKOV TIER TRANSITION TOPOLOGY
    [clear_dry] <=====> [temperate] <=====> [light_rain]
                                               ^
                                               |
                                               v
    [flash_flood] <==================== [monsoon_downpour]
```

Transition Matrix $P_{ij}$ (Row = Current, Col = Next):
$$P = \begin{pmatrix}
0.65 & 0.35 & 0.00 & 0.00 & 0.00 \\
0.25 & 0.50 & 0.25 & 0.00 & 0.00 \\
0.00 & 0.30 & 0.45 & 0.25 & 0.00 \\
0.00 & 0.00 & 0.30 & 0.50 & 0.20 \\
0.00 & 0.00 & 0.00 & 0.60 & 0.40
\end{pmatrix}$$

### 4.3 Smooth Parameter Interpolation (Lerping)
To avoid abrupt discontinuous physics snaps (e.g. instant speed drops or sudden water level pops), continuous fields ($\Delta h$, optical range, traction penalty) must be linearly interpolated across an authored transition duration ($T_{\text{lerp}} \approx 10\text{ seconds}$):
$$\alpha = \min\left(1.0, \frac{t - t_{\text{trans}}}{T_{\text{lerp}}}\right)$$
$$V_{\text{current}} = V_{\text{prev}} + \alpha \cdot (V_{\text{target}} - V_{\text{prev}})$$

---

## 5. Information Operations & Public Legitimacy Framework

### 5.1 Law of Armed Conflict (LOAC) & Precaution in Attack
Under **Protocol Additional to the Geneva Conventions of 12 August 1949 (Protocol I), Article 57 (Precautions in Attack)**:
1. Planners must verify that targets are military objectives.
2. Means and methods must minimize incidental loss of civilian life and injury to civilians.
3. Attacks must be suspended or aborted if collateral harm is disproportionate to the concrete military advantage expected.

### 5.2 Probabilistic ISR Confidence & The Protected Target Strike Formula
In real operations, target identification is never binary; it is probabilistic based on sensor resolution, dwell time, and multi-INT fusion. Striking a protected or disputed facility without verified intelligence incurs catastrophic public fallout:

$$\text{PR Penalty} = \text{round}\left(B \times (2 - C) \times M_{\text{class}}\right)$$

Where:
- $B$: Base strike penalty constant ($B = 28$).
- $C$: Intelligence, Surveillance, & Reconnaissance (ISR) confidence ($0.0 \le C \le 0.95$). Baseline unverified target $C_0 = 0.30$. High-altitude UAV / GMTI sensor track boosts confidence $+0.35$ up to $0.95$.
- $M_{\text{class}}$: Facility classification tier multiplier:
  - Hospital / School / Religious Facility: $M_{\text{class}} = 2.0$
  - UN Convoy / Humanitarian Depot: $M_{\text{class}} = 1.5$
  - Disputed Dual-Use Infrastructure: $M_{\text{class}} = 1.0$

```
          STRIKE PENALTY VS RECONNAISSANCE CONFIDENCE
  Penalty
    60 |   * (Unverified blind strike: C=0.30, Penalty=48)
    50 |     *
    40 |       *
    30 |         *
    20 |           * (High-ISR verified strike: C=0.95, Penalty=29)
    10 |_____________________________________________
       0.0      0.30     0.50     0.70     0.95 (Confidence C)
```

### 5.3 Asymmetric Victimhood Lawfare Scaling
In cognitive domain warfare, the geopolitical harm of a strike is conditioned by the credibility of the complaining actor. If an insurgent faction's Popular Support collapses due to exposed hostage mistreatment or civilian shielding, its ability to generate international outrage diminishes:
$$\text{Effective JSLC Penalty} = \text{Raw Penalty} \times \left(\frac{\text{AoI Popular Support}}{100}\right)$$

### 5.4 Legitimacy As Pure Logistics: The Owner Directives
Under canonical design directives (**D-006** and **Owner Decision 2026-10-04 23:25**):
1. **Survival Over Popularity:** High-tech sovereigns prioritize survivability over being loved. PR is managed solely because losing it cripples physical logistics.
2. **Never Lock Weapons:** Degraded legitimacy **never jams weapons, never turns off guns mechanically, never slows orbital laser cooldowns, and never triggers an instant game-over defeat**.
3. **Pure Logistical Consequences:**
   - Allied arms export embargoes (missile reload cycles doubled, spare parts cost $+50\%$).
   - Maritime and airport customs delays.
   - Protester base gate blockades (obstructing supply trucks).
   - Funding throttling (credit income throttled to $35\%$ at zero legitimacy).
4. **Logistics Collapse Loss Condition:** A player at zero legitimacy loses **only** after remaining logistically unable to sustain combat (depleted ammunition and fuel) for **30 consecutive seconds**.

### 5.5 Two-Sided Rolling PR Gain Cap
To eliminate abusive "PR farming" (e.g. spamming minor humanitarian actions to whitewash catastrophic war crimes):
- **Positive PR gains** share a strict rolling ceiling of **25 points per 60 seconds**.
- **Negative PR penalties are uncapped** and apply instantly in full.

---

## 6. METOC & Info-Ops Audit Question Bank

When auditing simulation code, game mechanics, or unit assets, evaluate compliance against these 10 authoritative questions:

1. **Determinism Check:** Does any weather transition or PR delta calculation invoke `Math.random()`, `Date.now()`, or unseeded system time? *(Mandate: Zero nondeterminism; strict Mulberry32 seeded PRNG).*
2. **Weapons Lockout Prohibition:** Does zero PR or an ROE event lock any weapon, jam a gun, stretch laser cooldown, or force an instant match defeat? *(Mandate: VIOLATION if true; weapons fire freely, consequences are strictly logistical delays and blockades).*
3. **Paved Exemption Integrity:** Do wheeled vehicles traversing paved roads or bridges suffer off-road mud penalties? *(Mandate: Hard surfaces must maintain 1.0x velocity regardless of rain).*
4. **Bradley Amphibious Integrity:** Is the M2/M3 Bradley marked as amphibious or given deep-fording capabilities? *(Mandate: VIOLATION if amphibious; Bradley swim barrier was removed on M2A2 due to armor weight).*
5. **D9 Doobi Fording Depth:** Is the IDF D9 bulldozer rated above $1.22\text{ m}$ ($4.0\text{ ft}$)? *(Mandate: Fording depth must not exceed $1.22\text{ m}$; water above final drive seals causes axle ruin).*
6. **Thermal Blooming Physics:** Does the directed energy laser model treat crosswinds as degrading beam lethality? *(Mandate: Crosswinds sweep away heated air, mitigating blooming; zero wind is the worst-case blooming condition).*
7. **FLIR Wet Contrast Washout:** Does rain degrade visible EO more than FLIR? *(Mandate: In wet conditions, FLIR must degrade more than EO due to thermal contrast $\Delta T \to 0$ collapse).*
8. **Gain Cap Asymmetry:** Can positive PR recover faster than 25 points in 60 seconds, or are PR penalties capped? *(Mandate: Gains capped at 25/60s; penalties uncapped).*
9. **Sea State Aviation Cleared:** Are aircraft permitted to launch and trap in Sea State 6+? *(Mandate: Sea State 6 requires empty-deck chained tiedown protocol; well decks sealed against swamping).*
10. **MLC Bridging Enforcement:** Can heavy MBTs (Abrams MLC 70+, Merkava) cross an AVLB scissor bridge (MLC 35)? *(Mandate: MLC ratings must be strictly enforced; AVLB accepts only light/wheeled units).*
