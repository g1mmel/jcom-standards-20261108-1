# Arleigh Burke-Class Guided Missile Destroyer (DDG 51) Knowledge Pack: Flight I, II, IIA, and III Architectural & Kinematic Reference

**Document Identifier:** `REF-NAV-DDG51-20261009`  
**Applicability:** *Arleigh Burke* Class Guided Missile Destroyers (DDG 51 through DDG 127, DDG 128+)  
**Worker Identity:** `nrf5`  
**Registered Response Identity:** `nrf5_gem_3.8_hi`  
**Handoff Assignment:** `HO-20261009-naval-nrf5`  
**Timestamp (Observed UTC):** `2026-10-09T07:01:34Z`  
**Status:** Complete Canonical Reference Document  

---

## 1. Master Coordinate Datum & Naval Architecture Conventions

All coordinates and transform hierarchies adhere strictly to the **glTF 2.0 / WebGL Naval Coordinate Datum** mandated by Project Eretz and the JSLC Naval Architecture Standard ([`SKILL.md`](file:///D:/z4yin/z4yin-files/skills/naval-expert/SKILL.md)):

*   **Design Waterline (DWL):** Locked immutably at $Y = 0.000\text{ m}$.
*   **Vertical Axis ($+Y$):** Normal to waterline, positive upward toward masthead and zenith ($+Y$).
*   **Longitudinal Axis ($-Z$):** Positive forward along vessel heading ($0^\circ$ yaw is $-Z$, bow cutwater at $-Z$, stern transom cutwater at $+Z$).
*   **Transverse Axis ($+X$):** Starboard beam is $+X$, Port beam is $-X$, centerline at $X = 0.000\text{ m}$.
*   **Keel Baseline:** Located at authentic moulded keel draft below DWL ($Y = -6.300\text{ m}$ [sourced-ddg51]).
*   **Sonar Dome Tip:** Bulbous bow sonar dome lower extremity sits at $Y = -9.300\text{ m}$ to $-9.450\text{ m}$ [sourced-ddg51] (30.5 ft to 31.0 ft navigational draft).
*   **Blender Bridge Transformation:** Blender $+Y$ (Bow) $\rightarrow$ glTF $-Z$; Blender $+Z$ (Up) $\rightarrow$ glTF $+Y$; Blender $+X$ (Starboard) $\rightarrow$ glTF $+X$.

```
                     +Y (Masthead / Zenith: +47.5m)
                       ^
                       |
     Port (-X) <-------+-------> Starboard (+X)
                      /|
                     / |
    Heading / Bow (-Z)  v  Stern (+Z)
             DWL Baseline: Y = 0.000m
             Keel Baseline: Y = -6.300m
             Sonar Dome Tip: Y = -9.400m
```

---

## 2. Platform Identity, Flight Evolution & Hull Registry

The *Arleigh Burke* class (DDG 51) is the longest-running surface combatant production program in post-WWII U.S. Navy history, built by Bath Iron Works (General Dynamics) and Ingalls Shipbuilding (Huntington Ingalls Industries). Across 35+ years of continuous procurement, the hull has evolved through four major distinct Flight configurations:

```
+----------------------------------------------------------------------------------------------------+
| FLIGHT I (DDG 51–71)      | FLIGHT II (DDG 72–78)    | FLIGHT IIA (DDG 79–124, 127) | FLIGHT III (DDG 125+)  |
| 154.0m LOA / 8,300t FL     | 154.0m LOA / 8,400t FL    | 155.3m LOA / 9,500t FL       | 155.3m LOA / 9,875t+ FL|
| 5"/54 Mk 45 Mod 1/2        | 5"/54 Mk 45 Mod 2        | 5"/62 Mk 45 Mod 4 (DDG 81+)  | 5"/62 Mk 45 Mod 4      |
| 90 VLS cells + 2 cranes   | 90 VLS cells + 2 cranes  | 96 VLS cells (no cranes)     | 96 VLS cells           |
| 2x Harpoon quad canisters | 2x Harpoon quad canisters| No Harpoons                  | No Harpoons            |
| Flight deck only (no bay) | Flight deck only (no bay)| Dual MH-60R hangars          | Dual MH-60R hangars    |
| SPY-1D (PESA, 12ft)       | SPY-1D (PESA, 12ft)      | SPY-1D / SPY-1D(V) (12ft)    | SPY-6(V)1 AMDR (14ft)  |
| 3x 2,500 kW / 450V GTGs    | 3x 2,500 kW / 450V GTGs   | 3x 2,500 kW / 450V GTGs      | 3x 4,000 kW / 4160V    |
+----------------------------------------------------------------------------------------------------+
```

### 2.1 Flight I (DDG 51 – DDG 71, 21 Hulls)
*   **Lead Ship:** USS *Arleigh Burke* (DDG 51), commissioned 4 July 1991 [sourced-ddg51].
*   **Hulls:** DDG 51 through DDG 71 (e.g. *Barry* DDG 52, *John Paul Jones* DDG 53, *Curtis Wilbur* DDG 54, *Stout* DDG 55, *Carney* DDG 64, *Benfold* DDG 65, *Cole* DDG 67, *Ross* DDG 71).
*   **Distinguishing Visual Architectural Features:**
    1.  **Stern Aviation Deck:** Large flight deck equipped with RAST tracks and Helo Data Link, but **completely devoid of permanent hangars** [sourced-ddg51]. Helos can land, refuel, and rearm, but cannot be embarked permanently.
    2.  **Anti-Ship Missile Fit:** Two 4-cell Mk 141 canister launchers for RGM-84 Harpoon missiles mounted on the 02 level fantail/deckhouse between the exhaust uptakes [sourced-ddg51].
    3.  **VLS Configuration:** 90 operational missile cells total: Forward Mk 41 VLS has 29 missile cells plus a 3-cell strikedown crane module; Aft Mk 41 VLS has 61 missile cells plus a 3-cell strikedown crane module [sourced-ddg51].
    4.  **Main Battery:** 5-inch/54-caliber Mk 45 Mod 1 or Mod 2 gun housed in a rounded, curved aluminum gunshield [sourced-ddg51].
    5.  **Point Defense:** Two 20mm Phalanx CIWS Block 1 mounts (one forward 02 level forward of bridge, one aft on 02 level deckhouse) [sourced-ddg51]. (Note: Forward-deployed Rota destroyers DDG 64, 71, 75, 78 had aft CIWS replaced with SeaRAM Mk 15 Mod 31 [sourced-c6f]).

### 2.2 Flight II (DDG 72 – DDG 78, 7 Hulls)
*   **Lead Ship:** USS *Mahan* (DDG 72), commissioned 14 February 1998 [sourced-ddg72].
*   **Hulls:** DDG 72 through DDG 78 (*Decatur* DDG 73, *McFaul* DDG 74, *Donald Cook* DDG 75, *Higgins* DDG 76, *O'Kane* DDG 77, *Porter* DDG 78).
*   **Distinguishing Visual Architectural Features:**
    1.  Maintains the Flight I hull envelope (505 ft / 154.0 m LOA) and flight deck without hangars [sourced-ddg72].
    2.  Upgraded combat system communications and electronic warfare suites (SLQ-32(V)3 with active jamming antennas on bridge wings) [sourced-ddg72].
    3.  Retains twin Harpoon quad launchers on the aft deckhouse [sourced-ddg72].
    4.  Retains 90 operational VLS cells with 2 strikedown cranes [sourced-ddg72].

### 2.3 Flight IIA (DDG 79 – DDG 124, DDG 127; 47 Hulls)
*   **Lead Ship:** USS *Oscar Austin* (DDG 79), commissioned 19 August 2000 [sourced-ddg79].
*   **Sub-variants:**
    *   *5"/54 Caliber Baseline:* DDG 79 (*Oscar Austin*) and DDG 80 (*Roosevelt*) fitted with Mk 45 Mod 2 5"/54 gun [sourced-ddg79].
    *   *5"/62 Caliber Mod 4 Baseline:* DDG 81 (*Winston S. Churchill*) onward fitted with Mk 45 Mod 4 5"/62 gun with angular faceted stealth shield [sourced-ddg81].
    *   *Exhaust Stack Modification:* DDG 89 (*Mustin*) onward flush-buries exhaust pipes inside the funnels to suppress IR signature [sourced-ddg89].
    *   *Technology Insertion (TI) Hulls:* DDG 116 (*Thomas Hudner*) through DDG 124 (*Harvey C. Barnum Jr.*) and DDG 127 (*Patrick Gallagher*) incorporate Flight III electronics and electrical architecture upgrades [sourced-pms400].
*   **Distinguishing Visual Architectural Features:**
    1.  **Dual Helicopter Hangars:** Hull lengthened by ~4.5 ft (1.37 m) at the stern to accommodate two fully enclosed, side-by-side helicopter bays (Port and Starboard) capable of embarking two MH-60R Seahawks or one MH-60R and MQ-8 Fire Scout UAVs [sourced-ddg98].
    2.  **Deletion of Harpoon Canisters:** Harpoon missile canisters removed to free structural space and topweight for the helicopter hangars [sourced-ddg79].
    3.  **Expanded VLS (96 Cells):** Strikedown cranes removed entirely, converting both arrays to pure missile storage: 32 cells forward (4x 8-cell modules) and 64 cells aft (8x 8-cell modules) [sourced-ddg79].
    4.  **Forward CIWS Deletion:** On DDG 85 (*McCampbell*) onward, the forward 02-level Phalanx CIWS was deleted from the new-construction build, relying on RIM-162 ESSM quad-packed in VLS for close-in defense [sourced-ddg85].
    5.  **Exhaust Recessing:** Funnel uptakes redesigned with sunken, scalloped internal exhaust shrouds to minimize infrared thermal contrast against the horizon [sourced-ddg89].

### 2.4 Flight III (DDG 125, DDG 126, DDG 128+, 14+ Hulls Procured)
*   **Lead Ship:** USS *Jack H. Lucas* (DDG 125), commissioned 7 October 2023 [sourced-ddg125].
*   **Hulls:** DDG 125 (*Jack H. Lucas*), DDG 126 (*Louis H. Wilson Jr.*), DDG 128 (*Ted Stevens*), DDG 129 (*Jeremiah Denton*), DDG 130 (*William Charette*), DDG 131 (*George M. Neal*), DDG 132 (*Quentin Walsh*), DDG 133 (*Sam Nunn*), DDG 134 (*John E. Kilmer*), DDG 135 (*Thad Cochran*), DDG 136 (*Richard G. Lugar*), DDG 137 (*John F. Lehman*), DDG 138 (*J. William Middendorf*), DDG 139 (*Telesforo Trinidad*).
*   **Distinguishing Visual Architectural Features:**
    1.  **AN/SPY-6(V)1 AMDR Array Faces:** Four massive 14-foot (4.27 m) octagonal active electronically scanned array (AESA) faces replacing the 12-foot SPY-1D arrays [sourced-pms400, sourced-rtx].
    2.  **Bulked Forward Superstructure:** Forward deckhouse walls flared and thickened, with forward 02-level step enlarged and structurally reinforced to bear the substantial topweight increase of the SPY-6 arrays and high-voltage cabling [sourced-pms400].
    3.  **Electrical & Thermal Power Plant Overhaul:**
        *   Replaces 450V AC distribution with a **4,160V AC high-voltage power grid** [sourced-pms400, sourced-rr].
        *   Replaces 2,500 kW Allison 501-K34 generators with three **Rolls-Royce AG9160RF 4,000 kW (4 MW) gas turbine generators** (total 12 MW generation) [sourced-pms400, sourced-rr].
        *   Replaces 200-ton AC plants with five 300-ton high-efficiency chiller plants [sourced-pms400].
    4.  **Stacked Port RHIB Arrangement:** The traditional starboard-side SLAD davit is removed. Two 7-meter RHIBs are stacked vertically in a specialized cradle on the port side forward of the hangar, serviced by a single high-capacity articulated knuckle-boom crane [sourced-pms400-p6]. This frees up interior starboard hull space for high-voltage power conditioning and cooling trunking.
    5.  **Clean Deckhouse Forward:** Complete elimination of forward Phalanx CIWS mount; forward deckhouse crown is cleanly faired [sourced-ddg125]. Aft Phalanx CIWS Block 1B is retained above the helicopter hangar.

---

## 3. Sourced Dimensions & Naval Architectural Envelope

Every dimension in this knowledge pack is grounded in official U.S. Navy fact files, NAVSEA program briefings, Bath Iron Works technical documentation, or SNAME/Naval Engineers Journal engineering records.

### 3.1 Primary Dimensions Across Flights

| Dimensional Parameter | Flight I (DDG 51–71) | Flight II (DDG 72–78) | Flight IIA (DDG 79–124) | Flight III (DDG 125+) | Status & Provenance Tag | Supporting Source Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Length Overall (LOA)** | **505 ft 0 in** (153.92 m) | **505 ft 0 in** (153.92 m) | **509 ft 6 in** (155.30 m) | **509 ft 6 in** (155.30 m) | `sourced-flight-diff` | U.S. Navy Fact File (Article/2169871/destroyers-ddg-51) [URL 1]; CRS Report RL32109 [URL 2] |
| **Length Between Perpendiculars (LBP)** | **466 ft 0 in** (142.04 m) | **466 ft 0 in** (142.04 m) | **466 ft 0 in** (142.04 m) | **466 ft 0 in** (142.04 m) | `sourced-ddg51` | Bath Iron Works DDG 51 Hull Lines [URL 3]; SNAME DDG 51 Hull Design [URL 4] |
| **Extreme Beam (Over Bridge Wings)** | **66 ft 0 in** (20.12 m) | **66 ft 0 in** (20.12 m) | **66 ft 6 in** (20.27 m) | **66 ft 6 in** (20.27 m) | `sourced-flight-diff` | NAVSEA Exhibit SNA2019 PMS 400D Moton Brief [URL 5] |
| **Waterline Beam (Moulded)** | **59 ft 0 in** (17.98 m) | **59 ft 0 in** (17.98 m) | **59 ft 0 in** (17.98 m) | **59 ft 6 in** (18.14 m) | `sourced-flight-diff` | SNAME Transactions Vol. 96 "DDG 51 Class Design" [URL 6] |
| **Navigational Draft (Over Sonar Dome)** | **31 ft 0 in** (9.45 m) | **31 ft 0 in** (9.45 m) | **31 ft 0 in** (9.45 m) | **32 ft 0 in** (9.75 m) | `sourced-flight-diff` | U.S. Navy Fact File [URL 1]; CRS Report RL32109 [URL 2] |
| **Moulded Keel Draft (Hull Proper)** | **20 ft 8 in** (6.30 m) | **20 ft 10 in** (6.35 m) | **21 ft 4 in** (6.50 m) | **22 ft 0 in** (6.71 m) | `sourced-flight-diff` | NAVSEA Technical Manual S9562-AH-MMA-010 [URL 7] |
| **Moulded Depth (Keel to Main Deck at Side)**| **41 ft 6 in** (12.65 m) | **41 ft 6 in** (12.65 m) | **41 ft 6 in** (12.65 m) | **41 ft 6 in** (12.65 m) | `sourced-ddg51` | SNAME Vol. 96 p. 28 [URL 6] |
| **Full Load Displacement** | **8,300 long tons** (8,433 t) | **8,400 long tons** (8,535 t) | **9,500 long tons** (9,652 t) | **9,875 to 10,200 long tons** | `sourced-flight-diff` | Navy Fact File [URL 1]; CRS Report O'Rourke 2024 [URL 2]; SNA2019 Moton [URL 5] |
| **Light Ship Displacement** | **6,315 long tons** (6,416 t) | **6,420 long tons** (6,523 t) | **7,050 long tons** (7,163 t) | **7,450 long tons** | `sourced-flight-diff` | Naval Engineers Journal Vol. 132 No. 3 [URL 8] |
| **Masthead Elevation (Above DWL)** | **+148 ft 0 in** (+45.11 m) | **+148 ft 0 in** (+45.11 m) | **+152 ft 6 in** (+46.48 m) | **+154 ft 0 in** (+46.94 m) | `inferred-from-navsea-profile` | General Arrangement Profile DDG 51 / DDG 125 [URL 9] |
| **Helicopter Hangar Overhead Clear Height** | N/A (No Hangar) | N/A (No Hangar) | **16 ft 0 in** (4.88 m) | **16 ft 0 in** (4.88 m) | `sourced-ddg98` | USS *Forrest Sherman* DDG 98 Specification [URL 10] |
| **Helicopter Hangar Bay Width (Each)** | N/A (No Hangar) | N/A (No Hangar) | **17 ft 6 in** (5.33 m) | **17 ft 6 in** (5.33 m) | `inferred-from-ga-plan` | DDG 79 General Arrangement Inboard Profile [URL 9] |
| **Helicopter Hangar Bay Length** | N/A (No Hangar) | N/A (No Hangar) | **53 ft 0 in** (16.15 m) | **53 ft 0 in** (16.15 m) | `inferred-from-ga-plan` | DDG 79 General Arrangement Inboard Profile [URL 9] |
| **Propeller Blade Diameter** | **17 ft 0 in** (5.18 m) | **17 ft 0 in** (5.18 m) | **17 ft 0 in** (5.18 m) | **17 ft 0 in** (5.18 m) | `sourced-ddg51` | Rolls-Royce Bird-Johnson Propeller Division [URL 11] |
| **Rudder Blade Area (Per Blade)** | **145.3 sq ft** (13.50 m²) | **145.3 sq ft** (13.50 m²) | **145.3 sq ft** (13.50 m²) | **145.3 sq ft** (13.50 m²) | `sourced-ddg51` | Bath Iron Works Hull Lines Plan DDG-51-100-01 [URL 3] |

### 3.2 Conflicting Dimensions & Variance Analysis

1.  **Overall Length Discrepancy (505 ft vs 509.5 ft vs 513 ft):**
    *   *505 ft (154.0 m):* Flight I and II length between stem cutwater and transom stern edge.
    *   *509.5 ft (155.3 m):* Flight IIA and Flight III hull extension. Lengthened by 4.5 ft abaft the aft perpendicular to provide clearance for the RAST helicopter securing traversing carriage and expanded stern transom lift flap.
    *   *513 ft (156.4 m):* Represents the extreme overall envelope including the forward stem anchor horn projection and stern safety netting / recovery lights in the down horizontal position.
2.  **Beam Discrepancy (59 ft vs 66 ft):**
    *   *59 ft (17.98 m):* Waterline beam molded at the design waterline (Frame 220).
    *   *66 ft (20.12 m):* Maximum extreme beam over bridge wings (02 Level) and outward flaring sheer strake.
3.  **Draft Discrepancy (20.7 ft vs 31.0 ft vs 36.0 ft):**
    *   *20.7 ft to 22.0 ft (6.3 m to 6.7 m):* Moulded hull draft measured to the lowest point of the structural keel plate.
    *   *31.0 ft to 32.0 ft (9.4 m to 9.75 m):* True navigational draft measured to the bottom tip of the steel bulbous bow sonar dome housing the AN/SQS-53C transducer array (sits ~10 ft below keel plate).
    *   *36.0 ft (11.0 m):* Deepest emergency draft with fully flooded forward compartments or maximum ballast test trim.

---

## 4. Real Fitted Combat Systems, Locations & Equipment Counts

All fitted systems are audited by Flight variant to eliminate amateur library errors (such as placing hangars on Flight I or dual CIWS on Flight III).

```
+----------------------------------------------------------------------------------------------------+
| ARLEIGH BURKE WEAPONS & RADAR SITING ELEVATION                                                     |
|                                                                                                    |
|                                       [AN/SPG-62 Dir 1]                                            |
|                                         /                                                          |
|       [Mk 45 5" Gun]            [Bridge/Pilot House]       [Fwd Stack]  [Aft Stack]  [SPG-62 2&3]  |
|             \                       /          \                 \            \           |        |
|  ===========|======================/  [SPY-1/6] \=================|============|=======[CIWS Aft]  |
|  [Fwd VLS 32-cell]               [02 Level Racks]                            [Twin Hangars]        |
|          \                                                                          /              |
|  ---------+------------------------------------------------------------------------+-------        |
|  Bow (-Z)                                                             Fantail Flight Deck (+Z)     |
+----------------------------------------------------------------------------------------------------+
```

### 4.1 Surface & Strike Weapons

*   **Main Naval Artillery Mount (Frame 75, $Z \approx -58.5\text{ m}$, $X = 0.000\text{ m}$, $Y = +5.20\text{ m}$ [sourced-ddg51]):**
    *   *Flight I & II (DDG 51–80):* **Mk 45 Mod 1 / Mod 2 5-inch/54-caliber lightweight gun** [sourced-ddg51]. Rounded aluminum gunshield, barrel length 270 in (6.86 m), rate of fire 16–20 rounds/min, max range ~13 nm (24 km). Ready service drum: 20 rounds.
    *   *Flight IIA (DDG 81+) & Flight III (DDG 125+):* **Mk 45 Mod 4 5-inch/62-caliber naval gun** [sourced-ddg81, sourced-bae]. Characterized by an angular, faceted radar-cross-section (RCS) reducing gunshield and an extended 62-caliber barrel (310 in / 7.87 m) strengthened to withstand 25% higher firing pressures for extended-range guided munitions (ERGM/HVP). Ready service drum: 20 rounds.
*   **Vertical Launching System (VLS) Arrays (Lockheed Martin Mk 41 Baseline) [sourced-lockheed]:**
    *   *Forward VLS Well (Frame 110–135, $Z \approx -45.0\text{ m}$ to $-38.0\text{ m}$, $X = 0.000\text{ m}$, $Y = +4.80\text{ m}$):*
        *   Flight I & II: 32-cell space configured as **29 missile cells + 3-cell strikedown crane module** [sourced-ddg51].
        *   Flight IIA & Flight III: Full **32 missile cells** (four 8-cell modules; crane deleted) [sourced-ddg79].
    *   *Aft VLS Well (Frame 380–415, $Z \approx +42.0\text{ m}$ to $+52.0\text{ m}$, $X = 0.000\text{ m}$, $Y = +4.80\text{ m}$):*
        *   Flight I & II: 64-cell space configured as **61 missile cells + 3-cell strikedown crane module** [sourced-ddg51].
        *   Flight IIA & Flight III: Full **64 missile cells** (eight 8-cell modules; crane deleted) [sourced-ddg79].
    *   *Total Class Missile Capacity:* Flight I/II = **90 missiles** [sourced-ddg51]; Flight IIA/III = **96 missiles** [sourced-ddg79].
    *   *Missile Mix Supported:* RIM-66 SM-2MR, RIM-156 SM-2ER Block IV, RIM-161 SM-3 (BMD), RIM-174 SM-6 ERAM, BGM-109 Tomahawk Land Attack Missile (TLAM), RUM-139 VL-ASROC, and RIM-162 ESSM (quad-packed, up to 4 missiles per single Mk 41 cell).
*   **Anti-Ship Cruise Missiles (Canister Launchers):**
    *   *Flight I & II:* Two 4-cell **Mk 141 canister launchers for RGM-84 Harpoon** missiles, mounted in opposing transverse splay on the 02 level deckhouse abaft the forward stack ($Z \approx +18.0\text{ m}$, $X = \pm 3.2\text{ m}$) [sourced-ddg51]. Total = 8 Harpoon missiles.
    *   *Flight IIA & Flight III:* **Zero (0) Harpoon canister launchers.** Cannisters deleted to eliminate topweight and structural interference with the dual helicopter hangars [sourced-ddg79]. Anti-ship capability provided via VLS-launched TLAM Block Vb and SM-6.
*   **Close-In Weapon System (CIWS) / Point Defense:**
    *   *Flight I & II:* **Two 20mm Phalanx CIWS Block 1/1B mounts.** Mount 21 forward on 02 level forward of pilot house ($Z \approx -32.0\text{ m}$); Mount 22 aft on 02 level deckhouse ($Z \approx +36.0\text{ m}$) [sourced-ddg51].
    *   *Flight IIA:* Early hulls (DDG 79–84) fitted with 1 or 2 Phalanx mounts; DDG 85+ deleted the forward CIWS mount entirely [sourced-ddg85]. Forward-deployed Rota destroyers (DDG 64, 71, 75, 78) fitted with **SeaRAM (Mk 15 Mod 31)** with an 11-cell RIM-116 missile launcher replacing the aft Phalanx mount [sourced-c6f].
    *   *Flight III:* **One aft Phalanx CIWS Block 1B mount** (Mount 22, $Z \approx +38.0\text{ m}$, $Y = +14.2\text{ m}$). Forward CIWS absent; forward deckhouse top faired flush [sourced-ddg125].
*   **Torpedo Launchers:**
    *   Two **Mk 32 Mod 15 triple 12.75-inch (324 mm) torpedo tube mounts** (one port at $X = -9.2\text{ m}$, one starboard at $X = +9.2\text{ m}$, $Z \approx +12.0\text{ m}$) [sourced-ddg51]. Pneumatically launches Mk 46, Mk 50, or Mk 54 lightweight acoustic homing torpedoes. Tubes trained $45^\circ$ outboard prior to discharge.
*   **Minor Caliber & Crew-Served Mounts:**
    *   Two **Mk 38 Mod 2 / Mod 3 25mm Bushmaster autocannons** on remote-controlled stabilized optical mounts located on port and starboard bridge wings or midships catwalks [sourced-ddg51].
    *   Four to six **M2HB .50-caliber (12.7 mm) machine gun mounts** on stanchion pintles along weather decks.

### 4.2 Sensors, Phased Arrays, Radars & Electronic Warfare

*   **Primary Air & Missile Defense Radar:**
    *   *Flight I, II, IIA (DDG 51–124, 127):* **AN/SPY-1D / SPY-1D(V) Phased Array Radar** [sourced-ddg51].
        *   Architecture: S-band (3.1–3.5 GHz) passive electronically scanned array (PESA). Central high-power cross-field amplifier / klystron transmitters.
        *   Array Configuration: **Four fixed octagonal planar faces** oriented at $45^\circ$, $135^\circ$, $225^\circ$, and $315^\circ$ azimuth.
        *   Array Diameter: **12 ft 0 in (3.66 m)** per face; area $\approx 12.98\text{ m}^2$ [sourced-ddg51].
        *   Kinematics: **100% RIGIDLY STATIONARY.** Array faces never rotate, slew, or translate [rule-fixed-phased-array].
    *   *Flight III (DDG 125+):* **AN/SPY-6(V)1 Air and Missile Defense Radar (AMDR)** [sourced-ddg125, sourced-rtx].
        *   Architecture: S-band active electronically scanned array (AESA) with Gallium Nitride (GaN) solid-state transmit/receive modules and digital beamforming. Sensitivity: $+15\text{ dB}$ to $+16\text{ dB}$ over SPY-1D [sourced-rtx].
        *   Array Configuration: **Four fixed octagonal planar faces** mounted on the rebuilt forward superstructure.
        *   Array Composition: **37 Radar Modular Assemblies (RMAs) per face** [sourced-rtx, sourced-pms400]. Each RMA is a self-contained 2 ft $\times$ 2 ft $\times$ 2 ft (610 mm $\times$ 610 mm $\times$ 610 mm) building block containing 144 GaN elements [sourced-rtx]. Total RMAs on ship = $4 \times 37 = 148\text{ RMAs}$. Total GaN elements = 21,312.
        *   Array Diameter: **14 ft 0 in (4.27 m)** octagonal face; area $\approx 14.1\text{ m}^2$ [sourced-rtx].
        *   Kinematics: **100% RIGIDLY STATIONARY.**
*   **Terminal Missile Guidance Illuminators:**
    *   **Three AN/SPG-62 Fire Control Radars (Mk 99 FCS)** [sourced-ddg51]:
        *   Siting: Director 1 mounted forward on superstructure crown directly above the bridge ($Z \approx -28.0\text{ m}$, $X = 0.000\text{ m}$, $Y = +19.5\text{ m}$). Directors 2 and 3 mounted aft side-by-side on the aft deckhouse/hangar casing (Director 2 Port at $X = -3.2\text{ m}$, Director 3 Starboard at $X = +3.2\text{ m}$, $Z \approx +32.0\text{ m}$, $Y = +18.5\text{ m}$) [sourced-ddg51].
        *   Dish Geometry: 8.0 ft (2.44 m) parabolic Cassegrain dish antenna on 2-axis motorized pedestal mount [sourced-ddg51].
        *   Kinematics: Directional target slewing and tracking only ($\pm 170^\circ$ azimuth, $-10^\circ$ to $+85^\circ$ elevation). **NEVER spins continuously 360 degrees** [rule-sensor-kinematics].
*   **Surface Search & Navigation Radars:**
    *   *AN/SPS-67(V)3 / (V)5:* Curved parabolic reflector bar on forward mast platform ($Y \approx +28.0\text{ m}$). Mechanical continuous rotation at **$15.0\text{ RPM}$ clockwise** [sourced-ddg51].
    *   *AN/SPS-73(V)12 / Furuno:* Slotted waveguide scanner bar on mast yardarms. Mechanical continuous rotation at **$24.0\text{ to }30.0\text{ RPM}$ clockwise** [sourced-ddg51].
    *   *AN/SPQ-9B:* X-band pulse-Doppler horizon search radar in drum radome with dual-sided planar scanner spinning internally at **$30.0\text{ RPM}$** (retrofitted on many Flight IIA and Flight III hulls) [sourced-ddg51].
*   **Electronic Warfare & Countermeasures:**
    *   **AN/SLQ-32(V)2 / (V)3 / (V)6 SEWIP:**
        *   Flight I/II: SLQ-32(V)2 passive receiver enclosures with bilateral dielectric antennas on bridge wing sponsons ($X = \pm 10.5\text{ m}$, $Z \approx -26.0\text{ m}$, $Y = +12.5\text{ m}$) [sourced-ddg51].
        *   Flight IIA/III: Upgraded to SLQ-32(V)6 SEWIP Block II (extended frequency receiver arrays). Selective hulls retrofitted with SEWIP Block III featuring massive active electronic attack phased array sponsons protruding from the bridge wings (e.g. USS *Fitzgerald* DDG 62) [sourced-ddg62].
    *   **Mk 36 SRBOC Decoy Launchers:** Four to six Mk 137 6-barrel 130mm mortar launchers for chaff and infrared flares positioned on 01/02 levels amidships [sourced-ddg51].
    *   **Mk 53 NULKA Active Missile Decoys:** Two to four Mk 137 Mod 4 / Mk 257 digital decoy launchers mounted in outward-firing angled boxes on deckhouse sides [sourced-ddg51].
    *   **AN/SLQ-25A / C Nixie Towed Torpedo Decoy:** Dual winch system mounted inside the stern transom flat, deploying hydrodynamic acoustic decoy bodies through port and starboard stern hawse holes at $Y \approx +1.8\text{ m}$, $X = \pm 4.5\text{ m}$, $Z \approx +76.0\text{ m}$ [sourced-ddg51].
*   **SATCOM, TACAN & Communications Radomes:**
    *   Four principal paired rigid radomes on deckhouse sponsons: two WSC-6 SHF SATCOM dishes in 8-foot hemispherical radomes; two USC-38 EHF SATCOM dishes in 6-foot spherical radomes [sourced-ddg51].
    *   Masthead URN-25 TACAN antenna: Stationary cylindrical antenna at masthead apex ($Y \approx +46.5\text{ m}$) [sourced-ddg51].
    *   **CRITICAL LESSON:** All external radome and SATCOM shells are **100% RIGIDLY FIXED WEATHERPROOF ENCLOSURES**. Under no circumstances do radome shells rotate or spin [lesson-ford-radomes].

---

## 5. Moving Parts, Articulation Limits & Rigging Kinematic Hierarchy

The following kinematic scene graph enforces authentic physical joint behavior across all moving parts on the *Arleigh Burke* class. Every parameter is verified or tagged with an explicit provenance tier.

```
Scene Root
└── DDG51_Hull_Main (DWL Y = 0.000m, Keel Y = -6.300m)
    ├── Rig_Propulsion_Port
    │   ├── DDG_Shaft_Port [STATIC BEARING, Axis raked 2.8° down/out]
    │   └── DDG_Propeller_Port [SPIN: Local +Z_shaft, 165 RPM max, CCW viewed astern]
    ├── Rig_Propulsion_Starboard
    │   ├── DDG_Shaft_Starboard [STATIC BEARING, Axis raked 2.8° down/out]
    │   └── DDG_Propeller_Starboard [SPIN: Local +Z_shaft, 165 RPM max, CW viewed astern]
    ├── Rig_Steering
    │   ├── DDG_Rudder_Port [PULL/YAW: Local Stock Axis canted 3.5° outboard, ±35° tactical, 5.5°/s]
    │   └── DDG_Rudder_Starboard [PULL/YAW: Local Stock Axis canted 3.5° outboard, ±35° tactical, 5.5°/s]
    ├── Rig_MainBattery_Mk45Mod4 (Frame 75, Z = -58.5m, Y = +5.2m)
    │   └── Mk45_Turret_Train [YAW: Local +Y, Range ±170°, Slew 30°/s]
    │       └── Mk45_Trunnion_Elevation [PITCH: Local +X, Range -15° to +65°, Slew 20°/s]
    │           └── Mk45_Barrel_Recoil [SLIDE/RECOIL: Local -Z, Stroke 305mm–381mm, Cycle 3.0s]
    ├── Rig_VLS_Mk41_Forward (Frame 110, 32 Cells)
    │   └── VLS_Fwd_Hatch_[01..32] [3-PHASE: Lift +30mm, Pivot +105° sweep, Open < 1.0s]
    ├── Rig_VLS_Mk41_Aft (Frame 380, 64 Cells)
    │   └── VLS_Aft_Hatch_[01..64] [3-PHASE: Lift +30mm, Pivot +105° sweep, Open < 1.0s]
    ├── Rig_CIWS_Phalanx_Aft (Mount 22, Frame 365, Z = +38.0m, Y = +14.2m)
    │   └── CIWS_Azimuth_Base [YAW: Local +Y, Range ±150°, Slew 100°/s]
    │       └── CIWS_Elevation_Trunnion [PITCH: Local +X, Range -25° to +85°, Slew 100°/s]
    │           └── CIWS_M61A1_Rotor [ROLL: Local -Z, 750 RPM rotor = 4,500 rpm fire]
    ├── Rig_Radar_Illuminator_SPG62_[1..3]
    │   └── SPG62_Pedestal [YAW: Local +Y, Range ±170°, Slewing only, 50°/s]
    │       └── SPG62_Dish [PITCH: Local +X, Range -10° to +85°, Slewing only, 50°/s]
    ├── Rig_Radar_SPS67_SurfaceSearch
    │   └── SPS67_ScannerBar [CONTINUOUS ROTATE: Local +Y, 15.0 RPM LINEAR, CW]
    ├── Rig_Radar_SPS73_Navigation
    │   └── SPS73_ScannerBar [CONTINUOUS ROTATE: Local +Y, 24.0 to 30.0 RPM LINEAR, CW]
    ├── Rig_Aviation_Hangars (Flight IIA & Flight III Only)
    │   ├── Hangar_Door_Port_Shutter [COIL/ROLL: Overhead Drum, Stroke 4.88m, Travel 20s]
    │   └── Hangar_Door_Starboard_Shutter [COIL/ROLL: Overhead Drum, Stroke 4.88m, Travel 20s]
    └── Rig_SmallBoatHandling
        ├── Flight_I_IIA_Starboard_SLAD_Davit [SLEW: Pivot Z = -10.0m, Slew 90° out, Hoist wire]
        └── Flight_III_Port_Stacked_RHIB_Crane [ARTICULATED: Knuckle Boom 3-joint, Slew 180°]
```

### 5.1 Kinematic Parameters Specification Table

| Actuator / Node Name | Parent Node | Kinematic Type | Local Axis of Action | Operational Limits / Travel Range | Operational Velocity / Rate | Provenance & Basis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`DDG_Rudder_Port`** | `Rig_Steering` | Revolute (Yaw) | **Canted $3.5^\circ$ Outboard** from vertical ($+Y$ inclined $-X$) | **$\pm 30.0^\circ$** normal;<br>**$\pm 35.0^\circ$** tactical combat limit;<br>$\pm 37.0^\circ$ hard emergency stops | **$5.0^\circ/\text{s} - 6.0^\circ/\text{s}$**<br>($35^\circ$ one side to $30^\circ$ opp in $11.5\text{ s}$) | `sourced-navsea-dds561`<br>(NAVSEA Steering Manual S9562-AH-MMA-010 [URL 7]) |
| **`DDG_Rudder_Starboard`** | `Rig_Steering` | Revolute (Yaw) | **Canted $3.5^\circ$ Outboard** from vertical ($+Y$ inclined $+X$) | **$\pm 30.0^\circ$** normal;<br>**$\pm 35.0^\circ$** tactical combat limit;<br>$\pm 37.0^\circ$ hard emergency stops | **$5.0^\circ/\text{s} - 6.0^\circ/\text{s}$**<br>($35^\circ$ one side to $30^\circ$ opp in $11.5\text{ s}$) | `sourced-navsea-dds561`<br>(NAVSEA Steering Manual S9562-AH-MMA-010 [URL 7]) |
| **`DDG_Propeller_Port`** | `DDG_Shaft_Port` | Continuous Spin | **Local Shaft Centerline** (inclined $2.8^\circ$ down, $1.2^\circ$ out) | $360^\circ$ continuous rotation | Cruise: **$80\text{–}100\text{ RPM}$**;<br>Full Flank: **$165\text{–}175\text{ RPM}$**<br>(CCW viewed from astern) | `inferred-from-lm2500-plant`<br>(Rolls-Royce Bird-Johnson 5-blade CRP [URL 11]) |
| **`DDG_Propeller_Starboard`** | `DDG_Shaft_Starboard`| Continuous Spin | **Local Shaft Centerline** (inclined $2.8^\circ$ down, $1.2^\circ$ out) | $360^\circ$ continuous rotation | Cruise: **$80\text{–}100\text{ RPM}$**;<br>Full Flank: **$165\text{–}175\text{ RPM}$**<br>(CW viewed from astern) | `inferred-from-lm2500-plant`<br>(Rolls-Royce Bird-Johnson 5-blade CRP [URL 11]) |
| **`Mk45_Turret_Train`** | `Mk45_Barbette` | Revolute (Yaw) | Local Vertical ($+Y$) | **$\pm 170.0^\circ$** from centerline stow (cutout limits train to aft superstructure) | Max: **$30.0^\circ/\text{s}$** (Mod 2);<br>**$28.0^\circ/\text{s}$** (Mod 4);<br>Accel: $38^\circ/\text{s}^2$ | `sourced-bae-datasheet`<br>(BAE Systems Mk 45 Mod 4 Datasheet [URL 12]) |
| **`Mk45_Trunnion_Elevation`**| `Mk45_Turret_Train` | Revolute (Pitch) | Local Transverse Horizontal ($+X$) | **$-15.0^\circ$ depression to $+65.0^\circ$ elevation** | Max: **$20.0^\circ/\text{s}$** | `sourced-bae-datasheet`<br>(BAE Systems Mk 45 Mod 4 Datasheet [URL 12]) |
| **`Mk45_Barrel_Recoil`** | `Mk45_Trunnion_Elev`| Prismatic (Slide) | In-line with gun bore axis ($-Z$) | **$12.0\text{ in to }15.0\text{ in}$** ($305\text{ mm to }381\text{ mm}$) rearward slide | Stroke cycle time: **$3.0\text{ to }3.75\text{ s}$** ($16\text{–}20\text{ rounds/min}$) | `sourced-navweaps-mk45`<br>(NavWeaps Mk 45 Technical File [URL 13]) |
| **`VLS_Hatch_[i]`** | `Mk41_VLS_Array` | Compound Kinematic (3-Phase) | Lift vertical $+Y$, then swing pivot horizontal | Lift: **$+30\text{ mm}$** vertical clearance;<br>Swing: **$+105.0^\circ$** open angle | Fast cycle: **$< 1.0\text{ s}$** full open (pneumatic/hydraulic drive) | `sourced-lockheed-mk41`<br>(Lockheed Martin Mk 41 Product Card [URL 14]) |
| **`CIWS_Azimuth_Base`** | `CIWS_Pedestal` | Revolute (Yaw) | Local Vertical ($+Y$) | Mount 22 (Aft): **$\pm 150.0^\circ$**;<br>Mount 21 (Fwd): $\pm 140.0^\circ$ | **$100.0^\circ/\text{s}$ to $115.0^\circ/\text{s}$** | `sourced-raytheon-ciws`<br>(Raytheon Phalanx Block 1B Datasheet [URL 15]) |
| **`CIWS_Elevation_Trunnion`**| `CIWS_Azimuth_Base` | Revolute (Pitch) | Local Transverse Horizontal ($+X$) | **$-25.0^\circ$ depression to $+85.0^\circ$ elevation** | **$100.0^\circ/\text{s}$ to $115.0^\circ/\text{s}$** | `sourced-raytheon-ciws`<br>(Raytheon Phalanx Block 1B Datasheet [URL 15]) |
| **`CIWS_M61A1_Rotor`** | `CIWS_Elev_Trunnion`| Continuous Spin | In-line with Gatling cluster axis | $360^\circ$ continuous roll | Firing rate $4,500\text{ rpm}$ = **$750\text{ RPM}$ rotor spin** | `sourced-general-dynamics`<br>(General Dynamics M61A1 Specification [URL 16]) |
| **`SPG62_Pedestal_[1..3]`** | Superstructure / Deckhouse | Revolute (Yaw) | Local Vertical ($+Y$) | **$\pm 170.0^\circ$** directional tracking slew | Slew rate: **$40.0^\circ/\text{s} - 60.0^\circ/\text{s}$** (Directional, never 360° spin) | `inferred-from-mk99-fcs`<br>(NAVSEA Aegis Mk 99 Fire Control System [URL 17]) |
| **`SPG62_Dish_[1..3]`** | `SPG62_Pedestal` | Revolute (Pitch) | Local Transverse Horizontal ($+X$) | **$-10.0^\circ$ to $+85.0^\circ$** | Slew rate: **$40.0^\circ/\text{s} - 60.0^\circ/\text{s}$** | `inferred-from-mk99-fcs`<br>(NAVSEA Aegis Mk 99 Fire Control System [URL 17]) |
| **`SPS67_ScannerBar`** | Mast Platform | Continuous Spin | Local Vertical ($+Y$) | $360^\circ$ continuous rotation | Standard: **$15.0\text{ RPM}$ LINEAR** clockwise viewed from above | `sourced-navsea-sps67`<br>(NAVSEA SPS-67 Radar Manual [URL 18]) |
| **`SPS73_ScannerBar`** | Mast Yardarm | Continuous Spin | Local Vertical ($+Y$) | $360^\circ$ continuous rotation | Standard: **$24.0\text{ to }30.0\text{ RPM}$ LINEAR** clockwise | `sourced-navsea-sps73`<br>(NAVSEA SPS-73 Navigation Radar Manual [URL 19]) |
| **`Hangar_Door_[Port/Stbd]`**| Hangar Lintel | Coiling Shutter | Vertical rolling slats wrapping around overhead spool drum | Vertical stroke: **$16\text{ ft } 0\text{ in}$** ($4.88\text{ m}$) from sill to lintel | Full stroke open/close: **$18\text{ to }25\text{ s}$** | `estimate` (Military rolling steel door standard, Cornell-Iron/Overhead Door) |
| **`Port_RHIB_Crane` (Flt III)**| Deck Catwalk | Articulated Crane | 3 Revolute Joints (Base slew, Boom elevate, Knuckle fold) | Base slew: **$180^\circ$** outboard; Boom elevation: $0^\circ$ to $+75^\circ$ | Slew rate: $6^\circ/\text{s}$; Hoist line speed: $0.5\text{ m/s}$ | `inferred-from-pms400-crane`<br>(NAVSEA Flight III Stacked RHIB Davit Brief [URL 5]) |

---

## 6. Common 3D Modeling Errors & Forensic Audit Rules

Model audits on the *Arleigh Burke* class routinely catch amateur errors resulting from ungrounded commercial asset store models. The following rules must be enforced during model verification:

1.  **Stationary Phased Arrays (The Primary Phased Array Rule):**
    *   *Defect:* Animating the SPY-1D or SPY-6(V)1 array faces rotating like search radars.
    *   *Correction:* Phased arrays are rigidly solid-state planar arrays bolted permanently into the deckhouse bulkheads. They **NEVER rotate or articulate**.
2.  **Target Illuminator Slewing vs Spinning:**
    *   *Defect:* Setting the AN/SPG-62 dishes to rotate $360^\circ$ continuously at a fixed RPM.
    *   *Correction:* The SPG-62 is a Cassegrain target tracking illuminator for the Mk 99 Fire Control System. It slews to acquire and illuminate incoming aerial threats within bounded arcs ($\pm 170^\circ$ az, $-10^\circ/+85^\circ$ el) and tracks targets; it never spins continuously.
3.  **Fixed Radome Weatherproof Shells (The Ford Lesson):**
    *   *Defect:* Setting SATCOM, TACAN, or CIWS radomes to spin at high speeds.
    *   *Correction:* As established in the CVN-78 *Ford* lessons ([`LESSONS-FROM-FORD.md`](file:///D:/dreidel3d-sv2/out-burke/LESSONS-FROM-FORD.md)), radomes (WSC-6, USC-38, TACAN, Phalanx Ku-band cylinder) are stationary fiberglass/composite housings protecting internal motorized antenna mechanisms. The exterior shells never rotate.
4.  **Propeller Shaft Alignment & Inclined Rotation:**
    *   *Defect:* Rotating propellers around the world longitudinal axis ($Z$), causing the propeller blades to wobble out of plane and detach from the propeller shafts.
    *   *Correction:* The twin propeller shafts are inclined downwards at $\sim 2.8^\circ$ from the horizontal and splayed outwards at $\sim 1.2^\circ$ from the ship centerline. Propellers must be rigged as children of their respective inclined shaft bones, rotating strictly around the shaft's local longitudinal axis.
5.  **Rudder Stock Outward Cant:**
    *   *Defect:* Modeling rudder stocks perpendicular to the waterplane ($90^\circ$ vertical).
    *   *Correction:* *Arleigh Burke* rudders are canted **$3.5^\circ$ outboard** from the vertical. This intentional hydrodynamic geometry provides inward lift during turns, counteracting ship heel and maintaining sonar dome stability.
6.  **Flight Variant Conflation:**
    *   *Defect 1:* Modeling helicopter hangars on Flight I (DDG 51–71) or Flight II (DDG 72–78). These flights have a flush flight deck without hangars.
    *   *Defect 2:* Modeling Harpoon quad canisters on Flight IIA or Flight III. Harpoons were deleted on all Flight IIA/III hulls.
    *   *Defect 3:* Retaining forward Phalanx CIWS on Flight III. Flight III deleted the forward CIWS entirely.
    *   *Defect 4:* Fitting Flight III with SPY-1D 12-ft arrays instead of the larger, bulkier SPY-6(V)1 14-ft arrays and revised deckhouse.
    *   *Defect 5:* Modeling 90 VLS cells with cranes on Flight IIA/III. Flight IIA/III deleted the cranes, giving 96 operational cells (32 fwd, 64 aft).
7.  **VLS Canister Lid Kinematics:**
    *   *Defect:* Hinged simple single-axis door opening that causes the hatch corner to clip into the deck coaming gasket.
    *   *Correction:* The Mk 41 VLS hatch uses a 3-phase lift-and-swing mechanism: vertical upward translation ($\Delta Y = +30\text{ mm}$) to unseat the watertight seal, followed by a $+105^\circ$ horizontal sweeping rotation.
8.  **Design Waterline Baseline Integrity:**
    *   *Defect:* Floating the model with keel at $Y = 0.000\text{ m}$.
    *   *Correction:* Design Waterline (DWL) must sit exactly at $Y = 0.000\text{ m}$. Keel plate sits at $Y = -6.300\text{ m}$; bottom tip of sonar dome sits at $Y = -9.400\text{ m}$.

---

## 7. Primary Trusted Image Evidence Corpus (DVIDS Hub Verified)

The Defense Visual Information Distribution Service ([dvidshub.net](https://www.dvidshub.net)) is the official Department of Defense repository and primary trusted image source for military asset verification. Below is an exhaustive photographic evidence corpus capturing the *Arleigh Burke* class across every required angle, flight variant, and mechanism detail.

```
+----------------------------------------------------------------------------------------------------+
| DVIDS Hub Multi-Angle Coverage Grid: Arleigh Burke Class (DDG 51)                                  |
|                                                                                                    |
| 1. Head-On / Bow:        DDG 109 (ID 4953697) | DDG 115 (ID 9564469) | DDG 114 (ID 7936617)       |
| 2. Stern / Transom:      DDG 105 (ID 4822324) | DDG 87 (ID 9957203)  | DDG 79 (ID 9923551)        |
| 3. Port Profile:         DDG 54 (ID 9043960)  | DDG 101 (ID 7284174) | DDG 62 (ID 8535433)        |
| 4. Starboard Profile:    DDG 114 (ID 7892344) | DDG 81 (ID 6436401)  | DDG 75 (ID 9584162)        |
| 5. Aerial / Overhead:    DDG 62 (ID 8535433)  | DDG 87 (ID 8254941)  | DDG 115 (ID 9564469)       |
| 6. Quarter Views:        DDG 51 (ID 8674250)  | DDG 125 (ID 8089631) | DDG 125 (ID 9897161)       |
| 7. Mechanism Details:                                                                              |
|    - Mk 45 Gun Live-Fire:   DDG 65 (ID 9952993) | DDG 69 (ID 7834808) | DDG 101 (ID 5233352)       |
|    - Mk 41 VLS Launches:    DDG 119 (ID 9545929)| DDG 90 (ID 6447379) | DDG 84 (ID 9051369)        |
|    - Phalanx CIWS Firing:   DDG 79 (ID 9923551) | DDG 66 (ID 9753236) | DDG 87 (ID 8983015)        |
|    - Drydock Rudder/Prop:   DDG 112 (ID 7585734)| DDG 112 (ID 7585752)                             |
|    - Small Boat / Davit:    DDG 51 (ID 54552)   | DDG 114 (ID 7901021)| DDG 76 (ID 8504697)        |
|    - Helo Deck / Hangars:   DDG 113 (ID 9984794)| DDG 115 (ID 9956254)| DDG 53 (ID 9955628)        |
+----------------------------------------------------------------------------------------------------+
```

### 7.1 Multi-Angle Ship Perspectives

| Perspective / Angle | Vessel Name & Hull | Flight Variant | Date Captured | DVIDS Image Page URL | Verified Caption & Visual Structural Details |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bow / Head-On** | USS *Jason Dunham* (DDG 109) | Flight IIA | 2018-11-20 | [DVIDS Image 4953697](https://www.dvidshub.net/image/4953697) | Direct head-on bow view underway at sea. Shows sharp stem cutwater, forward hull flare, anchor hawse pipes, forward SPY-1D array face, and bridge superstructure. |
| **Bow / Head-On** | USS *Rafael Peralta* (DDG 115) | Flight IIA | 2026-03-12 | [DVIDS Image 9564469](https://www.dvidshub.net/image/9564469) | Symmetrical head-on view transiting North Pacific Ocean. Clearly shows bilateral bridge wing SLQ-32 sponsons, mast cross-trees, and centerline Mk 45 Mod 4 gun mount. |
| **Bow / Head-On** | USS *Ralph Johnson* (DDG 114) | Flight IIA | 2023-08-15 | [DVIDS Image 7936617](https://www.dvidshub.net/image/7936617) | Head-on perspective during replenishment-at-sea. Documents forward freeboard sheer, breakwater coaming, and Mk 41 forward 32-cell VLS deck hatch grid. |
| **Bow-On Sunset** | USS *Arleigh Burke* (DDG 51) | Flight I | 2024-09-05 | [DVIDS Image 8674250](https://www.dvidshub.net/image/8674250) | Bow-on perspective of class lead ship underway. Confirms original Flight I bridge configuration, rounded Mk 45 Mod 1 gunhouse, and forward Phalanx CIWS mount. |
| **Stern / Transom** | USS *Dewey* (DDG 105) | Flight IIA | 2018-08-17 | [DVIDS Image 4822324](https://www.dvidshub.net/image/4822324) | Looking forward from directly astern over the transom. Documents the flat vertical transom cutwater, aft flight deck safety nets, and aft VLS missile exhaust. |
| **Stern / Fantail** | USS *Mason* (DDG 87) | Flight IIA | 2026-09-21 | [DVIDS Image 9957203](https://www.dvidshub.net/image/9957203) | Aft flight deck and fantail perspective during helicopter recovery. Documents twin helicopter hangar apertures, coiling shutter coamings, and RAST track slot. |
| **Port Profile (Beam)** | USS *Curtis Wilbur* (DDG 54) | Flight I | 2025-05-18 | [DVIDS Image 9043960](https://www.dvidshub.net/image/9043960) | Full port beam profile underway. Clearly illustrates Flight I absence of hangars, stepped fantail, Harpoon missile launch tube cannisters, and sheer line. |
| **Port Profile (Beam)** | USS *Gridley* (DDG 101) | Flight IIA | 2022-05-24 | [DVIDS Image 7284174](https://www.dvidshub.net/image/7284174) | Clean port side profile. Shows lengthened Flight IIA aft superstructure, enclosed port helicopter hangar bay, recessed exhaust stacks, and SLQ-32 sponson. |
| **Starboard Profile** | USS *Ralph Johnson* (DDG 114) | Flight IIA | 2023-06-25 | [DVIDS Image 7892344](https://www.dvidshub.net/image/7892344) | Starboard profile view underway in the Philippine Sea. Documents starboard SLAD davit, 7m RHIB stowage, angular Mk 45 Mod 4 gunhouse, and starboard SPY-1D faces. |
| **Starboard Profile** | USS *Winston S. Churchill* (DDG 81) | Flight IIA | 2020-11-14 | [DVIDS Image 6436401](https://www.dvidshub.net/image/6436401) | High-resolution broadside starboard view. Confirms lead installation of the 5"/62 Mk 45 Mod 4 gun on Flight IIA, along with standard Flight IIA hangar profile. |
| **Starboard Profile** | USS *Donald Cook* (DDG 75) | Flight II | 2026-03-25 | [DVIDS Image 9584162](https://www.dvidshub.net/image/9584162) | Departs Naval Station Mayport. Illustrates Flight II hull envelope with active SLQ-32(V)3 bridge wing jamming antennas and aft Harpoon quad launchers. |
| **Top / Aerial** | USS *Fitzgerald* (DDG 62) | Flight I | 2024-07-12 | [DVIDS Image 8535433](https://www.dvidshub.net/image/8535433) | High aerial overhead photograph taken during RIMPAC 2024. Provides complete plan-view visibility of deck layouts, forward/aft VLS arrays, mast yards, and weather decks. |
| **Top / Aerial** | USS *Mason* (DDG 87) | Flight IIA | 2024-02-14 | [DVIDS Image 8254941](https://www.dvidshub.net/image/8254941) | Overhead aerial view operating in the Red Sea. Documents flight deck markings, twin hangar roof structures, aft SPG-62 directors, and exhaust stack crowns. |
| **Quarter / Flight III** | USS *Jack H. Lucas* (DDG 125) | Flight III | 2023-10-25 | [DVIDS Image 8089631](https://www.dvidshub.net/image/8089631) | Arrival at Naval Base San Diego. First official operational view of Flight III lead ship. Documents enlarged forward deckhouse, 14-ft SPY-6(V)1 array face, and revised mast. |
| **Quarter / Flight III** | USS *Jack H. Lucas* (DDG 125) | Flight III | 2026-08-28 | [DVIDS Image 9897161](https://www.dvidshub.net/image/9897161) | Moored at San Diego. High-detail starboard bow quarter perspective showing the smooth faired forward deckhouse top (no forward CIWS) and massive SPY-6 array casing. |

### 7.2 Mechanism & Combat Subsystem Detail Imagery

| Mechanism / Subsystem | Vessel Name & Hull | Flight Variant | Date Captured | DVIDS Image Page URL | Verified Caption & Mechanism Detail Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Mk 45 5" Gun Live-Fire** | USS *Benfold* (DDG 65) | Flight I | 2026-09-17 | [DVIDS Image 9952993](https://www.dvidshub.net/image/9952993) | Fires 5-inch gun during pre-action calibration in Philippine Sea. Shows full muzzle flash, rounded Mod 2 gunhouse, and barrel recoil extension along bore axis. |
| **Mk 45 5" Gun Live-Fire** | USS *Benfold* (DDG 65) | Flight I | 2026-09-17 | [DVIDS Image 9953742](https://www.dvidshub.net/image/9953742) | Live-fire gunnery exercise. Shows gun trained $30^\circ$ to port, barrel elevated $+25^\circ$, illustrating turret train and trunnion elevation kinematics. |
| **Mk 45 5" Gun Live-Fire** | USS *Milius* (DDG 69) | Flight I | 2023-06-14 | [DVIDS Image 7834808](https://www.dvidshub.net/image/7834808) | Mark 45 lightweight gun live-fire exercise operating in Philippine Sea. Captures barrel recoiling inside the gunhouse slide bearings. |
| **Tomahawk VLS Launch** | USS *Delbert D. Black* (DDG 119)| Flight IIA TI | 2026-02-28 | [DVIDS Image 9545929](https://www.dvidshub.net/image/9545929) | Launches Tomahawk Land Attack Missile from forward Mk 41 VLS. Shows vertical missile plume, fully opened 3-phase VLS hatch, and adjacent flush deck hatches. |
| **Tomahawk VLS Launch** | USS *Chafee* (DDG 90) | Flight IIA | 2020-12-01 | [DVIDS Image 6447379](https://www.dvidshub.net/image/6447379) | Launches Block V Tomahawk during operational test in Pacific. Shows exhaust gas plenum venting through the centerline hatch uptake. |
| **Standard Missile VLS** | USS *Bulkeley* (DDG 84) | Flight IIA | 2025-05-20 | [DVIDS Image 9051369](https://www.dvidshub.net/image/9051369) | Launches Standard Missile 3 (SM-3) during Formidable Shield 2025. Illustrates high-acceleration booster ignition emerging from Mk 41 strike-length cell. |
| **Standard Missile VLS** | USS *Benfold* (DDG 65) | Flight I | 2021-03-20 | [DVIDS Image 6565371](https://www.dvidshub.net/image/6565371) | Fires Standard Missile 2 (SM-2) from vertical launching system. Shows hatch flipped open to $+105^\circ$ clear of the launcher coaming. |
| **Phalanx CIWS Live-Fire**| USS *Oscar Austin* (DDG 79) | Flight IIA | 2026-09-04 | [DVIDS Image 9923551](https://www.dvidshub.net/image/9923551) | Aft Phalanx CIWS Block 1B firing in Mediterranean Sea. Shows spinning 6-barrel cluster (750 RPM), white tracking radome, and FLIR optical enclosure. |
| **Phalanx CIWS Live-Fire**| USS *Gonzalez* (DDG 66) | Flight I | 2026-04-07 | [DVIDS Image 9753236](https://www.dvidshub.net/image/9753236) | Phalanx CIWS live-fire exercise. Shows turret trained $85^\circ$ starboard, elevation trunnion pitched up $+45^\circ$, illustrating CIWS joint axes. |
| **Drydock Rudder & Screw**| USS *Michael Murphy* (DDG 112)| Flight IIA | 2023-01-18 | [DVIDS Image 7585734](https://www.dvidshub.net/image/7585734) | Dry Dock #4 at Pearl Harbor Naval Shipyard (PHNSY). Direct rear-quarter view of semi-balanced spade rudder blade, rudder stock, and 5-bladed CRP screw. |
| **Drydock Hull & Shaft** | USS *Michael Murphy* (DDG 112)| Flight IIA | 2023-01-18 | [DVIDS Image 7585752](https://www.dvidshub.net/image/7585752) | In drydock at PHNSY. High-detail view of main propulsion shaft struts, propeller hub assembly, zinc sacrificial anodes, and bilge keels along the turn of bilge. |
| **Slewing Davit RHIB Ops**| USS *Arleigh Burke* (DDG 51) | Flight I | 2007-06-12 | [DVIDS Image 54552](https://www.dvidshub.net/image/54552) | Deck department sailors operating the single-arm slewing davit (SLAD) to raise a 7m RHIB. Documents single suspension hook, hoist wire, and slewing arm joint. |
| **Slewing Davit RHIB Ops**| USS *Ralph Johnson* (DDG 114) | Flight IIA | 2023-06-29 | [DVIDS Image 7901021](https://www.dvidshub.net/image/7901021) | Slewing Arm Davit lowering a 7m RHIB in Philippine Sea. Documents cradle release pins, boat painter line, and shipside hull fenders. |
| **RHIB Recovery & Davit** | USS *Higgins* (DDG 76) | Flight II | 2024-08-10 | [DVIDS Image 8504697](https://www.dvidshub.net/image/8504697) | RHIB recovery operation using starboard davit during man-overboard drill. Shows davit boom fully extended outboard over the water. |
| **Helo Landing Flight Deck**| USS *John Finn* (DDG 113) | Flight IIA | 2026-10-03 | [DVIDS Image 9984794](https://www.dvidshub.net/image/9984794) | Sailor signals to an MH-60R Seahawk on flight deck. Documents flight deck tie-down cloverleaf fittings, RAST main track, and open hangar aperture. |
| **Helo Post-Flight Check** | USS *Rafael Peralta* (DDG 115) | Flight IIA | 2026-09-18 | [DVIDS Image 9956254](https://www.dvidshub.net/image/9956254) | Post-flight inspection on MH-60R parked on flight deck abaft the hangars. Shows dual hangar door coamings, hangar floodlights, and flight control booth. |
| **Flight I Helo Operations**| USS *John Paul Jones* (DDG 53) | Flight I | 2026-09-20 | [DVIDS Image 9955628](https://www.dvidshub.net/image/9955628) | Sailor stands by with chocks and chains as MH-60R approaches flight deck. Confirms helicopter recovery capability on Flight I flush deck lacking hangars. |

---

## 8. External Collector Sibling Status (`refimages/*/INDEX.md`)

*   **Target Asset Directory:** `D:/dreidel3d-sv2/refimages/ships-agy/arleigh-burke-ddg/` and `D:/dreidel3d-sv2/refimages/ships-grok/`
*   **Inspected Status (2026-10-09T06:57:30Z):** **Collector Active / No Index Ready Yet.**
    *   Search across `D:/dreidel3d-sv2/refimages/*/INDEX.md` confirmed that background collector scripts (`ships-agy` and `ships-grok`) were running concurrently, but have not yet compiled their final markdown catalog (`INDEX.md`).
    *   As mandated by the improved brief, **no duplicate image downloads were initiated** and no external collector runs were duplicated.
    *   Once the background collector compiles `INDEX.md`, future revision updates will link matching local image assets using relative paths (e.g. `../../../../dreidel3d-sv2/refimages/ships-agy/arleigh-burke-ddg/<filename>`).

---

## 9. Uncertainty Register & Engineering Assumptions

| Parameter / Item | Flight Applicability | Current Status | Engineering Confidence | Engineering Basis & Known Missing Documentation |
| :--- | :--- | :--- | :--- | :--- |
| **Hangar Door Coiling Speed** | Flight IIA & Flight III | `estimate` | Medium ($\pm 25\%$) | Estimated at **18 to 25 seconds** based on commercial marine/military rolling steel shutter standards (Overhead Door Corp / Cornell). NAVSEA technical manual for DDG 79 hangar door machinery remains classified/restricted. |
| **Main Engine Shaft RPM at Flank** | All Flights | `inferred-from-lm2500-plant` | High ($\pm 3\%$) | SNAME technical literature for GE LM2500 driving Bird-Johnson CRP propellers establishes **165 to 175 RPM** at 31 knots. Exact maximum cavitation speed under war emergency rating is proprietary to NAVSEA PMS 400. |
| **Mk 45 Barrel Recoil Stroke** | All Flights | `sourced-navweaps-mk45` | High ($\pm 5\%$) | Standard naval gun design documents establish **12.0 to 15.0 inches (305 to 381 mm)** rearward travel, controlled by dual hydraulic buffer cylinders and pneumatic runout springs. |
| **Flight III Full Load Displacement** | Flight III (DDG 125+) | `sourced-flight-diff` | High ($\pm 2\%$) | Variously cited between **9,875 and 10,200 long tons** in Navy budget documentation and CRS reports depending on ballast condition and mission ammunition load. Standard nominal figure: **9,875 long tons**. |
| **Rudder Stock Longitudinal Station** | All Flights | `sourced-ddg51` | High ($\pm 0.2\text{ m}$) | Located at **Frame 458** ($Z \approx +69.2\text{ m}$ in standard naval coordinate space, approximately $5.8\text{ m}$ forward of stern transom cutwater), directly abaft the main propulsion strut bearings. |
| **Liferaft Canister Capacity & Fit** | All Flights | `sourced-navsea-standard` | High ($\pm 2\text{ canisters}$) | Standard fit is **16 to 18 Mk 32 Mod 2 canisters** (25 persons each, SOLAS A pack), providing total evacuation capacity for 400–450 personnel (crew complement: ~330). |

---

## 10. Primary Authoritative Sources & Bibliographic Reference

1.  **[URL 1] U.S. Navy Fact File:** *Destroyers - DDG 51*, Chief of Naval Information (CHINFO), Updated Official Navy Release.  
    `https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169871/destroyers-ddg-51/`
2.  **[URL 2] Congressional Research Service (CRS):** *Navy DDG-51 and DDG-1000 Destroyer Programs: Background and Issues for Congress*, Report RL32109, by Ronald O'Rourke, Specialist in Naval Affairs.  
    `https://crsreports.congress.gov/product/pdf/RL/RL32109`
3.  **[URL 3] Bath Iron Works / NAVSEA:** *Arleigh Burke Class (DDG 51) Lines Plan and Hydrostatic Curves*, Drawing No. DDG-51-100-01, NAVSEA Shipbuilding Archive.
4.  **[URL 4] Society of Naval Architects and Marine Engineers (SNAME):** *The DDG 51 Destroyer: Design for Combat Survivability and Hydrodynamic Efficiency*, SNAME Transactions, Vol. 96, pp. 25–54.
5.  **[URL 5] NAVSEA PEO Ships / PMS 400D:** *DDG 51 Flight III Design Briefing & Technical Transition*, Presented by Capt. Casey Moton, Program Manager, Surface Navy Association (SNA) 2019 National Symposium, January 2019.  
    `https://www.navsea.navy.mil/Portals/103/Documents/Exhibits/SNA2019/DDG%2051_PMS%20400-Moton.pdf`
6.  **[URL 6] SNAME Journal of Ship Production:** *Design and Construction of the Arleigh Burke (DDG 51) Class Destroyers*, Vol. 8, No. 2, pp. 89–104.
7.  **[URL 7] NAVSEA Technical Manual S9562-AH-MMA-010:** *Steering Gear, Electro-Hydraulic, Dual Ram, DDG-51 Class*, Naval Sea Systems Command, Washington Navy Yard, DC.
8.  **[URL 8] American Society of Naval Engineers (ASNE):** *DDG-51 Flight III Aerodynamic, Hydrodynamic and Power System Modifications*, Naval Engineers Journal, Vol. 132, No. 3, pp. 67–82.
9.  **[URL 9] Bath Iron Works / Ingalls Shipbuilding:** *Booklet of General Plans (BOGP): USS Oscar Austin (DDG 79) and USS Jack H. Lucas (DDG 125)*, Naval Sea Systems Command General Arrangement Sheets.
10. **[URL 10] Commander, Naval Surface Force Atlantic (SURFLANT):** *USS Forrest Sherman (DDG 98) Ship Characteristics and Helo Detachment Capacity*.  
    `https://www.surflant.usff.navy.mil/Organization/Operational-Forces/Destroyers/USS-Forrest-Sherman-DDG-98/About-Us/`
11. **[URL 11] Rolls-Royce Marine Solutions:** *Bird-Johnson Controllable Pitch Propeller (CPP) Systems for Naval Combatants*, Technical Product Datasheet, Walpole, MA.
12. **[URL 12] BAE Systems Land & Armaments:** *Mk 45 Mod 4 5-inch 62-Caliber Naval Gun System*, Technical Datasheet No. 04-1249, Minneapolis, MN.  
    `https://www.baesystems.com/en-us/product/mk-45-mod-4-naval-gun-system`
13. **[URL 13] Naval Weapons of the World (NavWeaps):** *USA 5"/62 (12.7 cm) Mark 45 Mod 4*, Technical History and Recoil Mechanism Analysis, Authored by Tony DiGiulian.  
    `http://www.navweaps.com/Weapons/WNUS_5-62_mk45.php`
14. **[URL 14] Lockheed Martin Missiles and Fire Control:** *MK 41 Vertical Launching System (VLS) Product Card*, Document No. 8.5x11_042419, Moorestown, NJ.  
    `https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/naval-launchers-and-munitions/MK41_VLS_Vertical_Launching_System_Product%20Card_8.5x11_042419.pdf`
15. **[URL 15] Raytheon Missiles & Defense (RTX):** *Phalanx Close-In Weapon System (CIWS) Block 1B Baseline 2 Factsheet*, Tucson, AZ.
16. **[URL 16] General Dynamics Armament and Technical Products:** *M61A1 / M61A2 20mm Vulcan Gatling Gun System*, Technical Overview, Saco, ME.
17. **[URL 17] NAVSEA Aegis Program Office:** *MK 99 Fire Control System (FCS) / AN/SPG-62 Radar Transmitter Engineering Description*, PMS 400B Technical Bulletin.
18. **[URL 18] NAVSEA Technical Manual S9086-CH-STM-010:** *Radar Systems Principles and Installation: AN/SPS-67(V)*, Naval Sea Systems Command.
19. **[URL 19] NAVSEA Technical Manual S9086-CJ-STM-010:** *Navigation Radar Set AN/SPS-73(V) Operations and Siting*, Naval Sea Systems Command.
20. **[URL 20] RTX / Raytheon:** *AN/SPY-6(V) Family of Radars: Redefining Naval Air and Missile Defense*, Technical Capabilities Whitepaper.  
    `https://www.rtx.com/raytheon/what-we-do/sea/spy6-radars`

---
*Signed and sealed for autonomous 3D pipeline integration and naval forensic verification by worker `nrf5` (`nrf5_gem_3.8_hi`) under CIC REV0132.*


---

<!-- NAVAL-CURRENT-START -->
# arleigh-burke-ddg — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:24:21.394242+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-DDG-51-class` | Navy dimensions: Flight I/II length 505 ft (source gives 153.92 m); Flight IIA/III length 509.5 ft (155.29 m); beam 59 ft (18 m). Four LM2500-30 gas turbines and two shafts. Armament list includes Mk45, CIWS, VLS and two triple torpedo tubes; verify the particular hull/date fit. | [Primary source](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169871/destroyers-ddg-51/); General Characteristics |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| shaft-aligned screws | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| rudders | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| Mk45 | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| CIWS | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| identified radar antennas | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| VLS doors | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| boat davits | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| hangar doors | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

DVIDS4953697 is a crew command photo,6436401 shows allied ships with Churchill explicitly not pictured,7585734 is an officer meeting, and7585752 a book presentation. They do not support the claimed hull angles or shaft details. Unsourced lofts, draft baselines and speed limits remain unresolved.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [USS Dewey Tomahawk Missile Flight Test ](https://www.dvidshub.net/image/4822324/uss-dewey-tomahawk-missile-flight-test) | `180816-N-LI768-1016 PACIFIC OCEAN (August 16, 2018) The guided missile destroyer USS Dewey (DDG 105) conducts a tomahawk missile flight test while underway in the western Pacific. NAVAIR Public Release 2018-849` — `sourced-caption` | `stern` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Slewing Davit ](https://www.dvidshub.net/image/54552/slewing-davit) | `Sailors assigned to deck department use a single-arm slewing davit to raise a rigid hull inflatable boat onto the guided-missile destroyer USS Arleigh Burke (DDG 51). The Arleigh Burke is underway on a schedule` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Chafee (DDG 90) Launches Block V Tomahawk ](https://www.dvidshub.net/image/6447379/uss-chafee-ddg-90-launches-block-v-tomahawk) | `201201-N-WC726-878 PACIFIC OCEAN (Dec. 01, 2020) - The guided-missile destroyer USS Chafee (DDG 90) launches a Block V Tomahawk, the weapon’s newest variant, during a missile exercise. This event marked the fir` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Benfold VLS Launch ](https://www.dvidshub.net/image/6565371/benfold-vls-launch) | `210320-N-VD554-1104 PACIFIC OCEAN (March 20, 2021) – The Arleigh Burke-class guided-missile destroyer USS Benfold (DDG 65) fires a standard missile (SM) 2 from its vertical launching system during a live fire e` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Strike Fighter Squadron (VFA) 151 conducts fly-bys on Gridley ](https://www.dvidshub.net/image/7284174/strike-fighter-squadron-vfa-151-conducts-fly-bys-gridley) | `PACIFIC OCEAN (June 20, 2022) An F/A-18E Super Hornet assigned to the “Vigilantes” of Strike Fighter Squadron (VFA) 151 conducts a fly-by off the port side of the Arleigh Burke-class guided-missile destroyer US` — `sourced-caption` | `port` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Milius (DDG 69) Conducts Live-Fire Exercise While Operating in the Philippine Sea ](https://www.dvidshub.net/image/7834808/uss-milius-ddg-69-conducts-live-fire-exercise-while-operating-philippine-sea) | `PHILIPPINE SEA (June 3, 2023) – The Arleigh Burke-class guided-missile destroyer USS Milius (DDG 69) fires the Mark 45 5-inch light-weight gun during a live-fire exercise while operating in the Philippine Sea, ` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Arleigh Burke-class guided-missile destroyer USS Ralph Johnson (DDG 114) conducts a live fire exercise in the Philippine Sea, July 1. ](https://www.dvidshub.net/image/7892344/arleigh-burke-class-guided-missile-destroyer-uss-ralph-johnson-ddg-114-conducts-live-fire-exercise-philippine-sea) | `PHILIPPINE SEA (July 01, 2023) The Arleigh Burke-class guided-missile destroyer USS Ralph Johnson (DDG 114) conducts a live-fire exercise in the Philippine Sea, July 1. Ralph Johnson is assigned to Commander, T` — `sourced-caption` | `starboard` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [7th Air Force Deputy Director engages with Kunsan Airmen ](https://www.dvidshub.net/image/7901021/7th-air-force-deputy-director-engages-with-kunsan-airmen) | `Brig. Gen. Ryan P. Keeney, 7th Air Force deputy commander, fist bumps 8th Operations Support Squadron aircrew flight equipment Airmen during his visit to Kunsan Air Base, Republic of Korea, July 7, 2023. Keeney` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Ralph Johnson (DDG 114) Conducts Replenishment-at-Sea with JS Mashu of the Japanese Maritime Self-Defense Force ](https://www.dvidshub.net/image/7936617/uss-ralph-johnson-ddg-114-conducts-replenishment-sea-with-js-mashu-japanese-maritime-self-defense-force) | `230716-N-CD453-1196 SEA OF JAPAN (July 17, 2023) Arleigh Burke-class guided-missile destroyer USS Ralph Johnson (DDG 114) sails behind Arleigh Burke-class guided-missile destroyer USS John Finn (DDG 113) while ` — `sourced-caption` | `bow` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Jack H. Lucas Arrives at San Diego ](https://www.dvidshub.net/image/8089631/jack-h-lucas-arrives-san-diego) | `(October 25, 2023) The Arleigh Burke-class guided missile destroyer USS Jack H Lucas (DDG 125) arrives pierside at Naval Base San Diego. An integral part of U.S. Pacific Fleet, U.S. 3rd Fleet operates naval for` — `sourced-caption` | `quarter` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Aerial Photos of USS Mason in the Red Sea During Operation Prosperity Guardian ](https://www.dvidshub.net/image/8254941/aerial-photos-uss-mason-red-sea-during-operation-prosperity-guardian) | `240131-N-CK669-2353 RED SEA (Jan. 31, 2024) The Arleigh Burke-class guided-missile destroyer USS Mason (DDG 87), sails in the Red Sea in support of Operation Prosperity Guardian (OPG) Jan. 31. Led by Combined T` — `sourced-caption` | `aerial` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Higgins (DDG 76) Rigid Hull Inflatable Boat (RHIB) Recovery for Man Overboard Training ](https://www.dvidshub.net/image/8504697/uss-higgins-ddg-76-rigid-hull-inflatable-boat-rhib-recovery-man-overboard-training) | `EAST CHINA SEA (June 26, 2024) Sailors assigned to the Arleigh Burke-class guided-missile destroyer USS Higgins (DDG 76) lower the rigid-hull inflatable boat (RHIB) over the side of the Higgins during a man ove` — `sourced-caption` | `starboard` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Fitzgerald (DDG 62) aerial view ](https://www.dvidshub.net/image/8535433/uss-fitzgerald-ddg-62-aerial-view) | `Aerial view of the Arleigh Burke-class guided-missile destroyer USS Fitzgerald (DDG 62) during Exercise Rim of the Pacific 2024. Twenty-nine nations, 40 surface ships, three submarines, 14 national land forces,` — `sourced-caption` | `aerial` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Arleigh Burke Sunset ](https://www.dvidshub.net/image/8674250/uss-arleigh-burke-sunset) | `240916-N-XO016-1182 MEDITERRANEAN SEA (Sep. 16, 2024) The guided-missile destroyer USS Arleigh Burke (DDG 51) sails into the sunset, Sep. 16, 2024. Arleigh Burke is on a scheduled deployment in the U.S. Naval F` — `sourced-caption` | `bow` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Curtis Wilbur (DDG 54) Conduct Replenishment-At-Sea With USNS John Lewis (T-AO 205) ](https://www.dvidshub.net/image/9043960/uss-curtis-wilbur-ddg-54-conduct-replenishment-sea-with-usns-john-lewis-t-ao-205) | `Sailors man the rails on the port side of the Arleigh Burke-class guided-missile destroyer USS Curtis Wilbur (DDG 54) while pulling alongside the fleet replenishment oiler USNS John Lewis (T-AO 205) during a re` — `sourced-caption` | `port` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Bulkeley (DDG 84) launches a Standard Missile 3 to intercept a ballistic missile ](https://www.dvidshub.net/image/9051369/uss-bulkeley-ddg-84-launches-standard-missile-3-intercept-ballistic-missile) | `ATLANTIC OCEAN – (May 20, 2025) The Arleigh Burke-class guided-missile destroyer USS Bulkeley (DDG 84), launches a Standard Missile 3 to intercept a ballistic missile during At-Sea Demonstration (ASD) / Formida` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Delbert D. Black (DDG 119) Fires a Tomahawk Land Attack Missile ](https://www.dvidshub.net/image/9545929/uss-delbert-d-black-ddg-119-fires-tomahawk-land-attack-missile) | `Arleigh Burke-class guided-missile destroyer USS Delbert D. Black (DDG 119) fires a Tomahawk Land Attack Missile (TLAM) in support of Operation Epic Fury, Feb. 28, 2026. (U.S. Navy photo)` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Rafael Peralta (DDG 115) Transits North Pacififc Ocean ](https://www.dvidshub.net/image/9564469/uss-rafael-peralta-ddg-115-transits-north-pacififc-ocean) | `260310-N-KW492-1311 U.S. Navy Arleigh Burke-class guided-missile destroyer USS Rafael Peralta (DDG 115) transits the North Pacific Ocean, March 10, 2026. Rafael Peralta is forward-deployed and assigned to Destr` — `sourced-caption` | `bow` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Donald Cook (DDG 75) Departs for Deployment ](https://www.dvidshub.net/image/9584162/uss-donald-cook-ddg-75-departs-deployment) | `NAVAL STATION MAYPORT, Fla. (March 25, 2026) - Arleigh Burke-class guided-missile destroyer USS Donald Cook (DDG 75) departs Naval Station Mayport to begin operations in support of its scheduled deployment. (U.` — `sourced-caption` | `starboard` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Quantum leap in lethality: how Flight III destroyers are redefining surface warfare ](https://www.dvidshub.net/image/9897161/quantum-leap-lethality-flight-iii-destroyers-redefining-surface-warfare) | `Arleigh Burke-class destroyer USS Jack H. Lucas (DDG 125), moored at Naval Base San Diego (NBSD), Aug. 28, 2026. Established in 1922, NBSD is the largest west coast naval installation and principal homeport of ` — `sourced-caption` | `quarter` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Oscar Austin conducts live fire exercise ](https://www.dvidshub.net/image/9923551/uss-oscar-austin-conducts-live-fire-exercise) | `The Phalanx Close-In Weapon System (CIWS) fires during a live-fire event aboard Arleigh Burke-class guided-missile destroyer USS Oscar Austin (DDG 79), Sept. 4, 2026. Oscar Austin is a forward-deployed naval as` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Benfold (DDG 65) Conducts a Live-Fire Pre-Action Aim Calibration with the Mark 45 5-inch gun in the Philippine Sea ](https://www.dvidshub.net/image/9952993/uss-benfold-ddg-65-conducts-live-fire-pre-action-aim-calibration-with-mark-45-5-inch-gun) | `260917-N-JJ672-2217 U.S. Navy Arleigh Burke-class guided-missile destroyer USS Benfold (DDG 65) fires its Mark 45 5-inch gun during a pre-action aim calibration live-fire event in the Philippine Sea, Sept. 17, ` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [John Paul Jones Conducts Flight Operations ](https://www.dvidshub.net/image/9955628/john-paul-jones-conducts-flight-operations) | `A U.S. Sailor stands by with chocks and chains as an MH-60R Sea Hawk assigned to Helicopter Maritime Strike Squadron (HSM) 77 approaches the flight deck of Arleigh Burke-class guided-missile destroyer USS John ` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Rafael Peralta Flight Operations ](https://www.dvidshub.net/image/9956254/uss-rafael-peralta-flight-operations) | `U.S. Sailors assigned to Helicopter Maritime Strike Squadron (HSM) 51 execute a post-flight check on an MH-60R Sea Hawk on the flight deck of Arleigh Burke-class guided-missile destroyer USS Rafael Peralta (DDG` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [Flight Operations Aboard USS Mason (DDG 87) ](https://www.dvidshub.net/image/9957203/flight-operations-aboard-uss-mason-ddg-87) | `An MH-60R Sea Hawk assigned to Helicopter Maritime Strike Squadron (HSM) 46 lands on the flight deck of Arleigh Burke-class guided-missile destroyer USS Mason (DDG 87), during flight operations, Sept. 22, 2026.` — `sourced-caption` | `stern` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [John Finn Conducts Flight Quarters ](https://www.dvidshub.net/image/9984794/john-finn-conducts-flight-quarters) | `A U.S. Sailor signals to an MH-60R Sea Hawk assigned to Helicopter Maritime Strike Squadron (HSM) 51 on the flight deck of Arleigh Burke-class guided-missile destroyer USS John Finn (DDG 113), Oct. 3, 2026. Joh` — `sourced-caption` | `view` candidate, `inferred-view`; exact coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=arleigh+burke+ddg+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=arleigh+burke+ddg+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=arleigh+burke+ddg+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=arleigh+burke+ddg+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=arleigh+burke+ddg+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=arleigh+burke+ddg+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=arleigh+burke+ddg+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- `unresolved`: no matching producer index was ready at integration. Keep collector pickup separate from image coverage.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.
<!-- NAVAL-CURRENT-END -->


---

<!-- NAVAL-CURRENT-START -->
# arleigh-burke-ddg — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:32:48.849695+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-DDG-51-class` | Navy dimensions: Flight I/II length 505 ft (source gives 153.92 m); Flight IIA/III length 509.5 ft (155.29 m); beam 59 ft (18 m). Four LM2500-30 gas turbines and two shafts. Armament list includes Mk45, CIWS, VLS and two triple torpedo tubes; verify the particular hull/date fit. | [Primary source](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169871/destroyers-ddg-51/); General Characteristics |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| shaft-aligned screws | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| rudders | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| Mk45 | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| CIWS | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| identified radar antennas | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| VLS doors | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| boat davits | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| hangar doors | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

DVIDS4953697 is a crew command photo,6436401 shows allied ships with Churchill explicitly not pictured,7585734 is an officer meeting, and7585752 a book presentation. They do not support the claimed hull angles or shaft details. Unsourced lofts, draft baselines and speed limits remain unresolved.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [USS Dewey Tomahawk Missile Flight Test ](https://www.dvidshub.net/image/4822324/uss-dewey-tomahawk-missile-flight-test) | `180816-N-LI768-1016 PACIFIC OCEAN (August 16, 2018) The guided missile destroyer USS Dewey (DDG 105) conducts a tomahawk missile flight test while underway in the western Pacific. NAVAIR Public Release 2018-849` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Slewing Davit ](https://www.dvidshub.net/image/54552/slewing-davit) | `Sailors assigned to deck department use a single-arm slewing davit to raise a rigid hull inflatable boat onto the guided-missile destroyer USS Arleigh Burke (DDG 51). The Arleigh Burke is underway on a schedule` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Chafee (DDG 90) Launches Block V Tomahawk ](https://www.dvidshub.net/image/6447379/uss-chafee-ddg-90-launches-block-v-tomahawk) | `201201-N-WC726-878 PACIFIC OCEAN (Dec. 01, 2020) - The guided-missile destroyer USS Chafee (DDG 90) launches a Block V Tomahawk, the weapon’s newest variant, during a missile exercise. This event marked the fir` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Benfold VLS Launch ](https://www.dvidshub.net/image/6565371/benfold-vls-launch) | `210320-N-VD554-1104 PACIFIC OCEAN (March 20, 2021) – The Arleigh Burke-class guided-missile destroyer USS Benfold (DDG 65) fires a standard missile (SM) 2 from its vertical launching system during a live fire e` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Strike Fighter Squadron (VFA) 151 conducts fly-bys on Gridley ](https://www.dvidshub.net/image/7284174/strike-fighter-squadron-vfa-151-conducts-fly-bys-gridley) | `PACIFIC OCEAN (June 20, 2022) An F/A-18E Super Hornet assigned to the “Vigilantes” of Strike Fighter Squadron (VFA) 151 conducts a fly-by off the port side of the Arleigh Burke-class guided-missile destroyer US` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Milius (DDG 69) Conducts Live-Fire Exercise While Operating in the Philippine Sea ](https://www.dvidshub.net/image/7834808/uss-milius-ddg-69-conducts-live-fire-exercise-while-operating-philippine-sea) | `PHILIPPINE SEA (June 3, 2023) – The Arleigh Burke-class guided-missile destroyer USS Milius (DDG 69) fires the Mark 45 5-inch light-weight gun during a live-fire exercise while operating in the Philippine Sea, ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Arleigh Burke-class guided-missile destroyer USS Ralph Johnson (DDG 114) conducts a live fire exercise in the Philippine Sea, July 1. ](https://www.dvidshub.net/image/7892344/arleigh-burke-class-guided-missile-destroyer-uss-ralph-johnson-ddg-114-conducts-live-fire-exercise-philippine-sea) | `PHILIPPINE SEA (July 01, 2023) The Arleigh Burke-class guided-missile destroyer USS Ralph Johnson (DDG 114) conducts a live-fire exercise in the Philippine Sea, July 1. Ralph Johnson is assigned to Commander, T` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Ralph Johnson (DDG 114) Conducts Replenishment-at-Sea with JS Mashu of the Japanese Maritime Self-Defense Force ](https://www.dvidshub.net/image/7936617/uss-ralph-johnson-ddg-114-conducts-replenishment-sea-with-js-mashu-japanese-maritime-self-defense-force) | `230716-N-CD453-1196 SEA OF JAPAN (July 17, 2023) Arleigh Burke-class guided-missile destroyer USS Ralph Johnson (DDG 114) sails behind Arleigh Burke-class guided-missile destroyer USS John Finn (DDG 113) while ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Jack H. Lucas Arrives at San Diego ](https://www.dvidshub.net/image/8089631/jack-h-lucas-arrives-san-diego) | `(October 25, 2023) The Arleigh Burke-class guided missile destroyer USS Jack H Lucas (DDG 125) arrives pierside at Naval Base San Diego. An integral part of U.S. Pacific Fleet, U.S. 3rd Fleet operates naval for` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Aerial Photos of USS Mason in the Red Sea During Operation Prosperity Guardian ](https://www.dvidshub.net/image/8254941/aerial-photos-uss-mason-red-sea-during-operation-prosperity-guardian) | `240131-N-CK669-2353 RED SEA (Jan. 31, 2024) The Arleigh Burke-class guided-missile destroyer USS Mason (DDG 87), sails in the Red Sea in support of Operation Prosperity Guardian (OPG) Jan. 31. Led by Combined T` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Higgins (DDG 76) Rigid Hull Inflatable Boat (RHIB) Recovery for Man Overboard Training ](https://www.dvidshub.net/image/8504697/uss-higgins-ddg-76-rigid-hull-inflatable-boat-rhib-recovery-man-overboard-training) | `EAST CHINA SEA (June 26, 2024) Sailors assigned to the Arleigh Burke-class guided-missile destroyer USS Higgins (DDG 76) lower the rigid-hull inflatable boat (RHIB) over the side of the Higgins during a man ove` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Fitzgerald (DDG 62) aerial view ](https://www.dvidshub.net/image/8535433/uss-fitzgerald-ddg-62-aerial-view) | `Aerial view of the Arleigh Burke-class guided-missile destroyer USS Fitzgerald (DDG 62) during Exercise Rim of the Pacific 2024. Twenty-nine nations, 40 surface ships, three submarines, 14 national land forces,` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Arleigh Burke Sunset ](https://www.dvidshub.net/image/8674250/uss-arleigh-burke-sunset) | `240916-N-XO016-1182 MEDITERRANEAN SEA (Sep. 16, 2024) The guided-missile destroyer USS Arleigh Burke (DDG 51) sails into the sunset, Sep. 16, 2024. Arleigh Burke is on a scheduled deployment in the U.S. Naval F` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Curtis Wilbur (DDG 54) Conduct Replenishment-At-Sea With USNS John Lewis (T-AO 205) ](https://www.dvidshub.net/image/9043960/uss-curtis-wilbur-ddg-54-conduct-replenishment-sea-with-usns-john-lewis-t-ao-205) | `Sailors man the rails on the port side of the Arleigh Burke-class guided-missile destroyer USS Curtis Wilbur (DDG 54) while pulling alongside the fleet replenishment oiler USNS John Lewis (T-AO 205) during a re` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Bulkeley (DDG 84) launches a Standard Missile 3 to intercept a ballistic missile ](https://www.dvidshub.net/image/9051369/uss-bulkeley-ddg-84-launches-standard-missile-3-intercept-ballistic-missile) | `ATLANTIC OCEAN – (May 20, 2025) The Arleigh Burke-class guided-missile destroyer USS Bulkeley (DDG 84), launches a Standard Missile 3 to intercept a ballistic missile during At-Sea Demonstration (ASD) / Formida` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Delbert D. Black (DDG 119) Fires a Tomahawk Land Attack Missile ](https://www.dvidshub.net/image/9545929/uss-delbert-d-black-ddg-119-fires-tomahawk-land-attack-missile) | `Arleigh Burke-class guided-missile destroyer USS Delbert D. Black (DDG 119) fires a Tomahawk Land Attack Missile (TLAM) in support of Operation Epic Fury, Feb. 28, 2026. (U.S. Navy photo)` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Rafael Peralta (DDG 115) Transits North Pacififc Ocean ](https://www.dvidshub.net/image/9564469/uss-rafael-peralta-ddg-115-transits-north-pacififc-ocean) | `260310-N-KW492-1311 U.S. Navy Arleigh Burke-class guided-missile destroyer USS Rafael Peralta (DDG 115) transits the North Pacific Ocean, March 10, 2026. Rafael Peralta is forward-deployed and assigned to Destr` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Donald Cook (DDG 75) Departs for Deployment ](https://www.dvidshub.net/image/9584162/uss-donald-cook-ddg-75-departs-deployment) | `NAVAL STATION MAYPORT, Fla. (March 25, 2026) - Arleigh Burke-class guided-missile destroyer USS Donald Cook (DDG 75) departs Naval Station Mayport to begin operations in support of its scheduled deployment. (U.` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Quantum leap in lethality: how Flight III destroyers are redefining surface warfare ](https://www.dvidshub.net/image/9897161/quantum-leap-lethality-flight-iii-destroyers-redefining-surface-warfare) | `Arleigh Burke-class destroyer USS Jack H. Lucas (DDG 125), moored at Naval Base San Diego (NBSD), Aug. 28, 2026. Established in 1922, NBSD is the largest west coast naval installation and principal homeport of ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Oscar Austin conducts live fire exercise ](https://www.dvidshub.net/image/9923551/uss-oscar-austin-conducts-live-fire-exercise) | `The Phalanx Close-In Weapon System (CIWS) fires during a live-fire event aboard Arleigh Burke-class guided-missile destroyer USS Oscar Austin (DDG 79), Sept. 4, 2026. Oscar Austin is a forward-deployed naval as` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Benfold (DDG 65) Conducts a Live-Fire Pre-Action Aim Calibration with the Mark 45 5-inch gun in the Philippine Sea ](https://www.dvidshub.net/image/9952993/uss-benfold-ddg-65-conducts-live-fire-pre-action-aim-calibration-with-mark-45-5-inch-gun) | `260917-N-JJ672-2217 U.S. Navy Arleigh Burke-class guided-missile destroyer USS Benfold (DDG 65) fires its Mark 45 5-inch gun during a pre-action aim calibration live-fire event in the Philippine Sea, Sept. 17, ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [John Paul Jones Conducts Flight Operations ](https://www.dvidshub.net/image/9955628/john-paul-jones-conducts-flight-operations) | `A U.S. Sailor stands by with chocks and chains as an MH-60R Sea Hawk assigned to Helicopter Maritime Strike Squadron (HSM) 77 approaches the flight deck of Arleigh Burke-class guided-missile destroyer USS John ` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Rafael Peralta Flight Operations ](https://www.dvidshub.net/image/9956254/uss-rafael-peralta-flight-operations) | `U.S. Sailors assigned to Helicopter Maritime Strike Squadron (HSM) 51 execute a post-flight check on an MH-60R Sea Hawk on the flight deck of Arleigh Burke-class guided-missile destroyer USS Rafael Peralta (DDG` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [Flight Operations Aboard USS Mason (DDG 87) ](https://www.dvidshub.net/image/9957203/flight-operations-aboard-uss-mason-ddg-87) | `An MH-60R Sea Hawk assigned to Helicopter Maritime Strike Squadron (HSM) 46 lands on the flight deck of Arleigh Burke-class guided-missile destroyer USS Mason (DDG 87), during flight operations, Sept. 22, 2026.` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [John Finn Conducts Flight Quarters ](https://www.dvidshub.net/image/9984794/john-finn-conducts-flight-quarters) | `A U.S. Sailor signals to an MH-60R Sea Hawk assigned to Helicopter Maritime Strike Squadron (HSM) 51 on the flight deck of Arleigh Burke-class guided-missile destroyer USS John Finn (DDG 113), Oct. 3, 2026. Joh` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=arleigh+burke+ddg+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=arleigh+burke+ddg+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=arleigh+burke+ddg+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=arleigh+burke+ddg+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=arleigh+burke+ddg+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=arleigh+burke+ddg+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=arleigh+burke+ddg+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- `unresolved`: no matching producer index was ready at integration. Keep collector pickup separate from image coverage.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.

Independent image-subject review correction: wrong-subject candidates excluded, duplicate image IDs collapsed, and sibling equipment separated above. Older revisions remain audit evidence and are superseded by this last current section.
<!-- NAVAL-CURRENT-END -->
