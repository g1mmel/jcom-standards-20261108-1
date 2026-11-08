# JSLC 3D Asset Verification Dossier
## Asset: Coalition Fleet Carrier INS Adir (Gerald R. Ford CVN-78)
**Review Pipeline:** Project Eretz / JSLC Master Review  
**Evaluator System:** Automated Reviewer Contact Sheet & Telemetry Arbiter  
**File Analyzed:** `coalition_carrier_adir_master.glb` (23,851,448 bytes)  
**Verification Date:** 2026-10-06  

---

### 1. High-Density 8-Panel Contact Sheet

![Coalition Fleet Carrier INS Adir (Gerald R. Ford CVN-78) Technical Contact Sheet](./contact_sheet_coalition_carrier_adir_master.png)

*The 8-panel composite contact sheet above verifies all critical visual, geometric, and kinematic criteria:*
* **Panel 1 (Frontal 3/4 Quarter):** Proves $-Z$ heading alignment and main weapon/bow bore vector.
* **Panel 2 (Starboard Side Profile):** Verifies the $Y = 0.00\text{m}$ ground plane (tanks) or design waterline (warships) and vertical clearance envelope.
* **Panel 3 (Top-Down Orthographic):** Proves symmetry, beam proportions, and deck arrangement along the longitudinal centerline.
* **Panel 4 (Rear / Aft Profile):** Verifies engine exhaust louvers, propeller shafts, rudders, and transom geometry.
* **Panel 5 (Beauty Isometric Shaded):** Validates PBR material response, dielectric roughness, and ambient occlusion under studio lighting.
* **Panel 6 (Topology & Wireframe):** Discloses triangle density, edge flow consistency, and mesh subdivision.
* **Panel 7 (Chroma Key Mask Isolation):** Audits pure `#00FF00` (`RGB[0, 255, 0]`) faction insignia and tactical markings.
* **Panel 8 (Kinematic Articulation Test):** Demonstrates functional mechanical actuation (turret traverse, gun elevation, barrel recoil damper, or deck-edge elevator stroke).

---

### 2. Measured Geometry & Telemetry Matrix

| Specification | Measured Value | Standard Target | Status |
| :--- | :--- | :--- | :---: |
| **Total Triangles** | **116,316** | < 150,000 (Hero Master) | PASSED |
| **Total Vertices** | **132,646** | Proportionate to topology | **VERIFIED** |
| **Submesh Node Count** | **158 meshes** | Multi-node kinematic tree | **VERIFIED** |
| **Bounding Width (X)** | **90.45 m** | Starboard $+X$ / Port $-X$ | **VERIFIED** |
| **Bounding Height (Y)** | **73.75 m** | Vertical Up $+Y$ | **VERIFIED** |
| **Bounding Length (Z)** | **337.0 m** | Straight Ahead $-Z$ | **VERIFIED** |
| **Baseline Ground Contact** | **Y = -12.0 m** | $Y = 0.000\text{m}$ | PASSED |
| **Manifold Watertightness** | **0.0% (0/158)** | Manifold closed shells | PARTIAL SHELL |
| **Chroma Key Green (#00FF00)** | **MISSING** | Mandatory `#00FF00` Insignia | FLAG: MISSING INSIGNIA |

---

### 3. Coordinate System & Transform Compliance

$$\begin{aligned}
\mathbf{Straight\ Ahead\ (0^\circ\ 0^\circ)} &\equiv \mathbf{-Z}\ [0, 0, -1] \quad \text{(Bow / Gun Muzzle pointing -Z)} \\
\mathbf{Vertical\ Up\ (0^\circ\ 90^\circ)} &\equiv \mathbf{+Y}\ [0, 1, 0] \quad \text{(Masthead / Turret Roof pointing +Y)} \\
\mathbf{Starboard\ /\ Right} &\equiv \mathbf{+X}\ [1, 0, 0] \\
\mathbf{Port\ /\ Left} &\equiv \mathbf{-X}\ [-1, 0, 0] \\
\mathbf{Ground\ /\ Waterline} &\equiv \mathbf{Y = 0.000m}
\end{aligned}$$

* **Heading Verification:** Longest dimension aligned along $Z$-axis. Frontal vector confirmed at $-Z = -167.243\text{m}$.
* **Vertical Grounding:** Lowest contact vertices rest at $Y = -12.0\text{m}$.

---

### 4. Submesh Breakdown & Kinematic Rigging Hierarchy

| Submesh Name | Triangles | Vertices | Watertight | Extents [X, Y, Z] (m) |
| :--- | :---: | :---: | :---: | :--- |
| `ship_deck_deck side walks_0` | 554 | 749 | Open Shell | [10.02, 0.21, 40.15] |
| `ship_deck_ship_0` | 340 | 293 | Open Shell | [10.02, 0.21, 40.15] |
| `stairs_vertical_lambert1_0` | 2,172 | 3,264 | Open Shell | [7.86, 1.28, 25.84] |
| `stairs_vertical_ship_interiors_0` | 12 | 24 | Open Shell | [0.11, 0.04, 0.12] |
| `radar_holders_radars_0` | 1,184 | 1,070 | Open Shell | [0.81, 0.8, 0.58] |
| `left_radar_holder_lambert1_0` | 36 | 72 | Open Shell | [1.25, 0.37, 0.37] |
| `right_back_radar_holder_ship rest_0` | 132 | 242 | Open Shell | [1.04, 0.9, 0.58] |
| `right_radar_holder_lambert1_0` | 48 | 96 | Open Shell | [1.28, 0.37, 0.45] |
| `ship_bridge_ship_bridge1_0` | 1,595 | 1,916 | Open Shell | [2.32, 2.58, 2.72] |
| `inflatable_rings_lambert1_0` | 12,800 | 10,280 | Open Shell | [9.63, 1.32, 31.61] |
| `pCube222_radars_0` | 1,120 | 1,177 | Open Shell | [2.61, 35.31, 3.96] |
| `pCube106_ship_0` | 92 | 104 | Open Shell | [1.0, 1.0, 1.0] |
| *...and 146 additional submeshes* | | | | |


---

### 5. Official Review Scorecard

| Category | Weight | Score Awarded | Notes |
| :--- | :---: | :---: | :--- |
| **Coordinate & Spatial Alignment** | 20 pts | **20 / 20** | -Z Heading verified; Y=0.0m contact validated. |
| **Polycount & Geometry Quality** | 25 pts | **25 / 25** | 116,316 triangles within hero budget. |
| **Manifold & Watertight Integrity** | 30 pts | **0 / 30** | 0.0% watertight submeshes. |
| **Chroma Key #00FF00 Insignia** | 25 pts | **0 / 25** | Needs #00FF00 faction insignia added. |
| **TOTAL SCORE** | **100 pts** | **45 / 100** | **ACTION REQUIRED (CHROMA / TOPOLOGY)** |

---
*Report generated automatically by `scripts/make_asset_contact_sheet.py`.*
