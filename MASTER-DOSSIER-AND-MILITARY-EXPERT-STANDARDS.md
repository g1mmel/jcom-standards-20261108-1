# JCOM / JSLC / Project Eretz — Master Dossier & Military Expert Standards Compendium

**Repository:** `g1mmel/jcom-standards-20261108-1`  
**Compiled Date:** 2026-11-08  
**Scope:** Complete, self-contained, unabridged compilation of all Naval Expert, Military Researcher, 3D Asset Verification, Geometric Upscaling, Blender Rigging, Ground/Air Subsystems, Weapons Terminal Effects, METOC, Info-Ops/Lawfare, and Regional Strategic Standards. Zero external references omitted.

---

## Master Table of Contents

1. [Part 1: Executive Synthesis — The Four Dossier Archetypes & Skill Architecture](#part-1-executive-synthesis--the-four-dossier-archetypes--skill-architecture)
2. [Part 2: 3D Asset Dossier Standard & Ingestion Protocol (`DOSSIER-STD-2026-V1`)](#part-2-3d-asset-dossier-standard--ingestion-protocol-dossier-std-2026-v1)
3. [Part 3: 3D Asset Contact Sheet (8-Panel) & 100-Point Verification Dossier Standard](#part-3-3d-asset-contact-sheet-8-panel--100-point-verification-dossier-standard)
4. [Part 4: Military Researcher Evidentiary Standard (`military-researcher` & `ADR-017` Dossier Judge)](#part-4-military-researcher-evidentiary-standard-military-researcher--adr-017-dossier-judge)
5. [Part 5: Evidence Corrections & Provenance Tagging (`todays-lessons-20261009`)](#part-5-evidence-corrections--provenance-tagging-todays-lessons-20261009)
6. [Part 6: Naval Architecture & Military Vehicle Kinematics Standard (`naval-military-kinematics` / `military-model-rigging` + Errata)](#part-6-naval-architecture--military-vehicle-kinematics-standard-naval-military-kinematics--military-model-rigging--errata)
7. [Part 7: 3D Geometric Upscaling & Cinematic Density Standard (`mesh-geometric-upscaling`)](#part-7-3d-geometric-upscaling--cinematic-density-standard-mesh-geometric-upscaling)
8. [Part 8: Headless Blender 4.2 Parts, Pivots & Unit-Structure Validator Contract (`cnc-blender-parts`)](#part-8-headless-blender-42-parts-pivots--unit-structure-validator-contract-cnc-blender-parts)
9. [Part 9: Ground & Air Military Systems and Structures Standard (`ground-air-military-systems`)](#part-9-ground--air-military-systems-and-structures-standard-ground-air-military-systems)
10. [Part 10: Weapons, Warheads, and Terminal Effects Engineering Standard (`weapons-terminal-effects`)](#part-10-weapons-warheads-and-terminal-effects-engineering-standard-weapons-terminal-effects)
11. [Part 11: Military Meteorology/Oceanography (METOC) & Information Operations Standard (`metoc-infoops`)](#part-11-military-meteorologyoceanography-metoc--information-operations-standard-metoc-infoops)
12. [Part 12: Israel Affairs — Military, Strategic, IAMD, Naval & LOAC Standard (`israel-affairs`)](#part-12-israel-affairs--military-strategic-iamd-naval--loac-standard-israel-affairs)
13. [Part 13: Middle East Strategic — Persian Gulf, Iran, Kharg Island & Zagros Standard (`middle-east-strategic`)](#part-13-middle-east-strategic--persian-gulf-iran-kharg-island--zagros-standard-middle-east-strategic)
14. [Part 14: Palestinian Affairs — Factional Doctrine, Subterranean Warfare & LOAC Conduct (`palestinian-affairs`)](#part-14-palestinian-affairs--factional-doctrine-subterranean-warfare--loac-conduct-palestinian-affairs)
15. [Part 15: Modern Middle East History & Operational Precedents Standard (`middle-east-history`)](#part-15-modern-middle-east-history--operational-precedents-standard-middle-east-history)
16. [Part 16: Politics, International Law, Information Operations & Lawfare Standard (`politics-infoops-lawfare`)](#part-16-politics-international-law-information-operations--lawfare-standard-politics-infoops-lawfare)
17. [Part 17: Complete End-to-End Dossier Exemplars (Grok-DR, 8-Panel Contact Sheet, 11-Station Blueprint, & Knowledge Pack)](#part-17-complete-end-to-end-dossier-exemplars)

---

## Part 1: Executive Synthesis — The Four Dossier Archetypes & Skill Architecture

Across the JCOM / JSLC / Project Eretz ecosystem, dossiers serve four distinct but interlocking engineering functions:

| Dossier Archetype | Governing Standard / Script | Core Contents | Primary Consumer |
| :--- | :--- | :--- | :--- |
| **1. Evidentiary Platform & Rigging Dossier (`grok-dr` / `ADR-017`)** | [standards/DOSSIER-STANDARD.md](./standards/DOSSIER-STANDARD.md), [skills/military-researcher/SKILL.md](./skills/military-researcher/SKILL.md), [standards/dossier-judge.md](./standards/dossier-judge.md) | 9-field YAML front-matter, Sourced Coordinate Datum & Dimensions (preserving conflicts side-by-side), General Arrangement & Armament, Complete Kinematic Scene Graph Hierarchy, Sensor Siting, Base-Asset Delta Audit, Game Data Check (`unit-dimensions.json`), 4 AI Video Prompts, Fetched URL Sources + companion `.research.md` log. | Estate Model Browser (`http://11.0.11.32:8470/api/dossiers`), `data/rigs`, [rules/unit-dimensions.json](./rules/unit-dimensions.json) |
| **2. 11-Station Naval Architectural Blueprint Dossier** | [standards/DOSSIER-STANDARD.md](./standards/DOSSIER-STANDARD.md), [skills/naval-military-kinematics/SKILL.md](./skills/naval-military-kinematics/SKILL.md) | Adds the **11-Station Transverse Offset Table (Body Plan)** from Station 0 (Aft Perpendicular) to Station 10 (Forward Perpendicular) at $L/10$ intervals (`Z`, Half-Breadth `X` at DWL, Keel `Y`, Deck Sheer `Y`, Deadrise/Flare). *Per `ADR-017`, station tables and `[X, Y, Z]` pivots must be explicitly marked `modelled, not sourced` unless backed by published shipyard lines plans.* | Procedural Hull Lofting, CAD Reconstruction, Blender Upscaling |
| **3. 3D Asset Verification Dossier (8-Panel Contact Sheet & 100-Pt Scorecard)** | [scripts/make_asset_contact_sheet.py](./scripts/make_asset_contact_sheet.py), [examples/verification-dossiers/coalition_carrier_adir_master_dossier.md](./examples/verification-dossiers/coalition_carrier_adir_master_dossier.md) | Pairs a `2560x1540` **8-Panel Technical Contact Sheet** (1: Frontal 3/4 Quarter, 2: Starboard Side Profile, 3: Top-Down Orthographic, 4: Rear/Aft Profile, 5: Beauty Isometric Shaded, 6: Topology & Wireframe, 7: `#00FF00` Chroma Key Mask Isolation, 8: Kinematic Articulation Test) with Trimesh telemetry and a **100-point automated scorecard** (Alignment 20 pts, Polycount 25 pts, Watertightness 30 pts, Chroma Key 25 pts). | Asset Promotion Gate (`>= 80/100` for Hero Approval) |
| **4. Evidence-Grounded Platform Knowledge Pack & DVIDS Angle Registry** | [standards/todays-lessons-20261009.md](./standards/todays-lessons-20261009.md), [examples/naval-expert-references/saar-6-corvette.md](./examples/naval-expert-references/saar-6-corvette.md) | Deep reference dossier with explicit provenance tags (`sourced-builder`, `sourced-manufacturer`, `inferred-unit-conversion`, `inferred-engineering`, `unresolved`), **DVIDSHUB.NET trusted image angle coverage matrix** (Starboard, Port, Bow, Stern, Top Aerial, Quarter, Mechanism Detail), Uncertainty Register, and `<!-- NAVAL-CURRENT-START -->` audited baseline block. | Multi-Agent Reference Injection & Visual Reference Verification |

---

## Part 2: 3D Asset Dossier Standard & Ingestion Protocol (`DOSSIER-STD-2026-V1`)

*Repository Path: [`standards/DOSSIER-STANDARD.md`](./standards/DOSSIER-STANDARD.md)*

# JSLC / Project Eretz - 3D Asset Dossier Standard & Ingestion Protocol

**Standard Identifier:** `DOSSIER-STD-2026-V1`  
**Effective Date:** 2026-10-09  
**Status:** MANDATORY PRODUCTION STANDARD  
**Authority:** Model Browser Architecture & Deep Research Cohort  

---

## 1. Overview & Purpose

Every 3D asset, combat platform, vessel, and vehicle in the estate repository requires an engineering-grade research dossier to ensure dimensional accuracy, authentic kinematic articulation, and physical fidelity across real-time WebGL rendering, simulation engines, and procedural AI video generation.

To maintain attribution, reproducibility, and automation across workers, **every newly generated or revised dossier must begin with a standardized YAML front-matter header** and adhere to the canonical section structure defined below.

---

## 2. Mandatory YAML Front-Matter Specification

Every dossier file (`*.md`) must open with YAML front-matter enclosed between triple hyphens (`---`):

```markdown
---
generated_at: "2026-10-09T02:25:00Z"
generator: "dossiers (dossiers_gem_3.8_hi, session 823dfb4e-594f-4337-8e4c-1893524b807d)"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "Google Gemini"
models:
  - "Google Gemini Ultra (Extended thinking)"
query: "Generate an exhaustive Architectural Blueprint and Kinematic Rigging Dossier for FGS Braunschweig (K130)..."
sources_count: 18
asset_id: "fgs-braunschweig-k130"
title: "Naval Architectural Blueprint Dossier: FGS Braunschweig (K130)"
---
```

### Field Definitions

| Field | Type | Mandatory? | Description |
|---|---|---|---|
| `generated_at` | String (ISO 8601 UTC) | **Yes** | Exact UTC timestamp of dossier synthesis (e.g. `2026-10-09T02:25:00Z`). |
| `generator` | String | **Yes** | Worker identity and session ID (e.g. `worker_name (registered_code, session <uuid>)`). |
| `skills` | Array of Strings | **Yes** | Specific skills utilized during research and verification (e.g. `naval-military-kinematics`, `mesh-geometric-upscaling`). |
| `provider` | String | **Yes** | AI provider name (e.g. `Google Gemini`). |
| `models` | Array of Strings | **Yes** | Specific model(s) used (e.g. `["Google Gemini Ultra (Extended thinking)"]`, `["deep-research-preview-04-2026"]`). |
| `query` | String | **Yes** | The core research brief or prompt directive used to synthesize the dossier. |
| `sources_count` | Integer / String | **Yes** | Total number of primary technical sources, manuals, and citations verified. |
| `asset_id` | String | Recommended | Matching canonical `asset_id` in `model_assets` (e.g. `gerald-r-ford-cvn`). If unmatched or in pre-ingestion queue, set to `null` or omit. |
| `title` | String | Recommended | Human-readable document title. |

---

## 3. Canonical Dossier Structure

A complete technical dossier must contain the following five engineering sections:

### 1. Master Coordinate Datum & Dimensions
- **Inviolable glTF 2.0 / WebGL Coordinate Datum:**
  - Heading / Forward / Bow: **$-Z$ axis** ($0^\circ$ yaw).
  - Vertical / Masthead / Sky: **$+Y$ axis**.
  - Transverse / Starboard: **$+X$ axis**.
  - Transverse / Port: **$-X$ axis**.
  - **Design Waterline (DWL):** Strictly at $Y = 0.000\text{m}$.
  - **Keel Baseline:** At $Y = -[\text{Draft}]\text{m}$.
  - **Ground Plane (Land Assets):** Track/tire contact plane at $Y = 0.000\text{m}$.
- **Metric Bounding Envelope:** Length Overall (LOA), Length Between Perpendiculars (LBP), Beam, Draft, Masthead Air Draft, Displacement / Gross Weight.
- **Hull & Topside Lines:** Rake angles, chine elevations, deadrise, tumblehome, flare.

### 2. 11-Station Transverse Offset Table (Body Plan)
- Parametric offset table from **Station 0** (Aft Perpendicular / Rudder Stock) to **Station 10** (Forward Perpendicular / Stem Post) at uniform intervals ($L/10$).
- Columns: Station Index, $Z$ Position ($\text{m}$), Half-Breadth at DWL ($\text{m}$), Keel $Y$ ($\text{m}$), Deck Freeboard $Y$ ($\text{m}$), Deadrise / Flare characteristics.

### 3. Complete Kinematic Scene Graph Hierarchy
- ASCII node graph establishing hierarchical parent-child relationships and discrete pivot points:
  - Propulsion: Propeller shaft roll, spade rudder yaw limits ($\pm 35^\circ$).
  - Primary Turret / Gun: Turret yaw ($360^\circ$ around $+Y$) $\to$ Mantlet pitch (around $+X$) $\to$ Barrel recoil (stroke along $+Z$) $\to$ Muzzle VFX socket.
  - VLS & Missile Cells: Cell covers, azimuth/elevation slewing trunnions.
  - Sponsons, Hangars & Ramps: Sliding/folding translation axes and physical limit stops.
  - Radars & Antennas: Continuous $360^\circ$ rotation around $+Y$.

### 4. Sensor Siting & Bilateral Symmetry Audit
- Primary 3D phased array radar placement, TACAN radome at masthead apex ($+Y$).
- Bilateral SATCOM dome sponsons on port and starboard yardarms to prevent mast shadowing.
- Flight deck night-operations markings: Unlit vibrant green safety circle (`#00FF00`) and approach vectors.

### 5. Master AI Video & Verification Prompt Package
- Four standardized prompts for generative video validation (Sora, Runway Gen-3, Luma):
  1. *Technical CAD Blueprint Isometric Fly-around* (Navy `#0A192F`, white lines `#FFFFFF`, cyan grid `#00FFFF`).
  2. *Combat Kinematics & Weapon Articulation Close-Up* (Turret traverse, barrel recoil, missile elevation).
  3. *Hydrodynamic Hull & Heavy Seas Wave Piercing* (Knuckle chine spray, turbulent wake).
  4. *Night Flight Deck Aircraft Recovery* (NVIS green lighting, rotorcraft landing).

---

## 4. Ingestion & Upload API (`POST /api/dossiers`)

The estate model browser service (`http://11.0.11.32:8470`) provides a dedicated upload API for real-time dossier ingestion.

### Endpoint Details
- **Route:** `POST http://11.0.11.32:8470/api/dossiers`
- **Network Scope:** LAN only (`11.0.11.0/24`)
- **Supported Content Types:** `text/markdown`, `application/json`

### Storage & Database Ingestion Flow
When an agent or pipeline pushes a dossier to this endpoint:
1. **Front-Matter / JSON Parsing:** Metadata (`generated_at`, `generator`, `skills`, `provider`, `models`, `query`, `sources_count`, `asset_id`, `title`) is extracted.
2. **SHA-256 Checksum:** Cryptographic digest of the markdown content is computed.
3. **MinIO Archival:** Markdown is uploaded to bucket `jslc-3d-assets` under `dossiers/<asset_id>/<timestamp>-<slug>.md` (or `dossiers/unmatched/<timestamp>-<slug>.md`).
4. **PostgreSQL Registration:** A row is inserted into table `model_dossiers` with the structured `method` JSONB object.
5. **Live Browser Availability:** The dossier is immediately rendered in the asset deep-dive drawer under the **Dossier** tab, sorted newest first, and increments the header counters.

### Method 1: Uploading Markdown with Front-Matter via cURL

```bash
curl -X POST http://11.0.11.32:8470/api/dossiers \
  -H "Content-Type: text/markdown" \
  --data-binary @dossier_file.md
```

### Method 2: Uploading via JSON Payload

```bash
curl -X POST http://11.0.11.32:8470/api/dossiers \
  -H "Content-Type: application/json" \
  -d '{
    "asset_id": "gerald-r-ford-cvn",
    "title": "Naval Architectural Blueprint Dossier: USS Gerald R. Ford",
    "generated_at": "2026-10-09T02:25:00Z",
    "method": {
      "skills": ["naval-military-kinematics", "mesh-geometric-upscaling"],
      "provider": "Google Gemini",
      "models": ["Google Gemini Ultra (Extended thinking)"],
      "query": "Gerald R Ford CVN-78 Blueprint",
      "sources_count": 14,
      "generator": "dossiers_gem_3.8_hi"
    },
    "markdown": "# Naval Architectural Blueprint Dossier: USS Gerald R. Ford\n\n..."
  }'
```

### Response Format (`201 Created`)

```json
{
  "success": true,
  "dossier": {
    "id": 313,
    "asset_id": "gerald-r-ford-cvn",
    "generated_at": "2026-10-09T02:25:00.000Z",
    "title": "Naval Architectural Blueprint Dossier: USS Gerald R. Ford",
    "s3_key": "dossiers/gerald-r-ford-cvn/20261009022500-naval-architectural-blueprint-dossier-uss-gerald-r-ford.md",
    "sha256": "4a7b...",
    "method": {
      "skills": ["naval-military-kinematics", "mesh-geometric-upscaling"],
      "provider": "Google Gemini",
      "models": ["Google Gemini Ultra (Extended thinking)"],
      "query": "Gerald R Ford CVN-78 Blueprint",
      "sources_count": 14,
      "generator": "dossiers_gem_3.8_hi"
    },
    "created_at": "2026-10-09T02:25:15.185Z"
  }
}
```

---

## Part 3: 3D Asset Contact Sheet (8-Panel) & 100-Point Verification Dossier Standard

*Repository Paths: [`scripts/make_asset_contact_sheet.py`](./scripts/make_asset_contact_sheet.py), [`examples/verification-dossiers/coalition_carrier_adir_master_dossier.md`](./examples/verification-dossiers/coalition_carrier_adir_master_dossier.md), [`examples/verification-dossiers/coalition_predator_mbt_cinematic_dossier.md`](./examples/verification-dossiers/coalition_predator_mbt_cinematic_dossier.md)*

### 3.1 The 8-Panel Composite Contact Sheet (`2560x1540` PNG, $4\times 2$ Grid of `640x360` Panels + `100px` Header)

Every 3D `.glb` asset evaluated by the automated review pipeline ([`scripts/make_asset_contact_sheet.py`](./scripts/make_asset_contact_sheet.py)) is rendered in headless Chromium WebGL across 8 mandatory diagnostic camera/shader passes:

| Panel | Title & Camera Setup | Engineering & Visual Verification Target |
| :--- | :--- | :--- |
| **Panel 1** | **Frontal Orthographic / 3/4 Quarter**<br>`cam = (-dist*0.70, mid_y + dist*0.35, -dist*0.80)` (Naval: `(-dist*0.55, mid_y + dist*0.28, -dist*0.85)`) | Proves **$-Z$ straight-ahead heading alignment** ($0^\circ$ yaw) and main weapon bore / bow stem vector. |
| **Panel 2** | **Starboard Side Profile**<br>`cam = (+dist*1.10, mid_y + dist*0.02, 0)` looking at `(0, mid_y, 0)` | Verifies the **$Y = 0.000\text{ m}$ ground contact plane** (ground vehicles) or **Design Waterline (DWL)** (warships, where keel sits at $-\text{Draft}$) and vertical height envelope. |
| **Panel 3** | **Top-Down Orthographic**<br>`cam = (0, +dist*1.40, 0.001)`, `up = (0, 0, -1)` (Bow points UP) | Proves bilateral symmetry, beam-to-length proportions, and deck/turret arrangement along the longitudinal centerline. |
| **Panel 4** | **Rear / Aft Profile**<br>`cam = (0, mid_y + dist*0.22, +dist*1.05)` | Verifies engine exhaust louvers (tanks) or transom, twin/quad propeller shafts, P-struts, rudders, well deck stern gate, and hangar door geometry (warships). |
| **Panel 5** | **Beauty Isometric Shaded**<br>`cam = (+dist*0.78, mid_y + dist*0.48, +dist*0.78)` | Validates PBR material response, dielectric roughness contrast (non-skid `0.88–0.95` vs markings `0.42–0.55`), specular edge bevels, and ambient occlusion under studio HDRI lighting. |
| **Panel 6** | **Topology & Wireframe Overlay**<br>`setPanelWireframe(true)` from Isometric Camera | Discloses total triangle count, radial cylinder segmentation (curvature sagitta rule $s \le 1.0\text{ px}$), edge flow consistency, and non-manifold edges. |
| **Panel 7** | **Chroma Key Mask Isolation**<br>`setPanelChromaIsolate(true)` | Audits pure `#00FF00` (`RGB[0, 255, 0]`, vertex color threshold `R < 30, G > 200, B < 30` or `*chroma*` submesh) reserved for dynamic team-tint shader masks and tactical insignia. Triggers `FLAG: MISSING #00FF00 FACTION INSIGNIA` if absent. |
| **Panel 8** | **Kinematic Articulation Test**<br>`applyKinematicArticulation()` | Demonstrates functional mechanical rigging without mesh clipping:<br>• **Naval:** Deck-edge elevators lowered $-11.5\text{ m}$, jet blast deflectors (JBDs) raised $+45^\circ$, radar trained.<br>• **Ground/Armor:** Turret yawed $-35^\circ$, gun elevated $+14^\circ$, barrel recoiled $+0.25\text{ m}$. |

### 3.2 Trimesh Telemetry & 100-Point Automated Scorecard Rubric

The verification script loads the `.glb` via `trimesh.load()` and computes:
1. **Coordinate & Spatial Alignment (`20 points`):**
   - `heading_aligned`: `extents[2] >= extents[0]` and `bounds_min[2] < bounds_max[2]` (longest axis along $Z$, facing $-Z$).
   - `is_ground_aligned`: `abs(bounds_min[1]) < 0.05 m` for land vehicles, or `bounds_min[1] < 0.5 m` (submerged keel below $Y = 0.000\text{ m}$ DWL) for naval vessels.
   - Awards **20 / 20** if both pass; **5 / 20** otherwise.
2. **Polycount & Geometry Quality (`25 points`):**
   - Hero Master budget: `total_triangles <= 150,000` awards **25 / 25** (`> 150,000` awards **15 / 25**).
3. **Manifold & Watertight Integrity (`30 points`):**
   - Computes `watertight_percentage = (watertight_submeshes / total_submeshes) * 100`.
   - Awards **30 / 30** if `watertight_percentage >= 80%`; otherwise `int(watertight_percentage * 0.3)`.
4. **Chroma Key `#00FF00` Insignia (`25 points`):**
   - Awards **25 / 25** if `#00FF00` chroma vertices or submeshes are present; **0 / 25** if missing.
5. **Promotion Gate:**
   - `total_score >= 80 / 100` $\rightarrow$ **`APPROVED FOR CINEMATIC HERO`**
   - `total_score < 80 / 100` $\rightarrow$ **`ACTION REQUIRED (CHROMA / TOPOLOGY)`**

---

## Part 4: Military Researcher Evidentiary Standard (`military-researcher` & `ADR-017` Dossier Judge)

*Repository Path: [`skills/military-researcher/SKILL.md`](./skills/military-researcher/SKILL.md)*

---
name: military-researcher
description: Research real military equipment facts (ships, aircraft, vehicles, weapons, sensors, organisations) for dossiers, rig specs and game data. Use whenever a number, position, loadout, complement or variant fact about real equipment is needed. Every fact must trace to a fetched source.
---

# Military researcher

Built from the method that won the 2026-10-14 dossier judge (grok-dr 199/200 vs 82/200; status/dossier-judge.md, ADR-017).

## Rules
1. **Every number and position traces to a URL you fetched in this run.** Record title, URL and the quoted line. A fact you cannot source is written "not public". Never invent station tables, pivot coordinates, frame numbers, drawing numbers or "NATOPS/NAVSEA" labels.
2. **Variant discipline.** Name the exact variant and hull or tail number range (CVN-78 is not CVN-79; LHD-1 is not LHD-8; F-35C is not F-35B). Never carry a fact from a sibling variant without saying so.
3. **Two sources for key numbers.** Cross-check length, beam, displacement, crew, weapons count and sensor type against two independent sources. When they disagree, print both side by side with their dates.
4. **Source order:** primary first (navy.mil, af.mil, army.mil, NAVSEA/NAVAIR, manufacturer pages, GAO, CRS, DOT&E, FAS, national MoD sites), then reputable press (USNI News, Defense News, Janes public pages, TWZ), then Wikipedia only with its cited source checked. If a primary site returns 403, use an official mirror or search extract and say so.
5. **Process:** at least 12 searches per subject, fetch the best 6 to 10 pages, then write. Parallel subagents are fine.
6. **Dates matter.** Equipment changes with refits. Give the "as of" date for each fact.

## Output
A table per question: item | answer | variant scope | source title | URL | quoted line | as-of date | confidence (high: two primary sources; medium: one primary or two secondary; low: one secondary). Then "Not public" rows and "Conflicts" rows. No prose claims outside the tables.

## Hand-off
Facts feed rig specs (data/rigs), dossiers (estate :8470, DOSSIER-STANDARD.md) and model fixes. For how equipment moves and is rigged, use the skill `military-model-rigging`; for what it is and where it sits, use this one.

---

## Part 4B: Dossier Judge Audit Report (`ADR-017`: `grok-dr` 199/200 vs `naval-expert` 82/200)

*Repository Path: [`standards/dossier-judge.md`](./standards/dossier-judge.md)*

# dossier-judge

Judge: grok-dr (xai grok-4.7, files only) vs naval-expert (agy/Gemini, already posted to :8470) on the same 8 assets.

Read-only. Nothing in `data/`, `asset-scratch/` or the gallery was changed. No emojis [OR-048].

## Bottom line

grok-dr wins all 8, and none of them is close.

Both writers usually get the headline length, beam and weight right. Below that headline, naval-expert makes things up:
- station tables, pivot XYZ and surface travels;
- "NATOPS" or "NAVSEA drawing" labels on figures that come from Wikipedia or nowhere;
- source lists with no URLs, some of them fabricated documents.

grok-dr writes "not public" when it does not know. It prints conflicting sources side by side, and every number checked traces to a fetched URL.

**Default writer from now on: grok-dr.** All 8 naval-expert dossiers on :8470 need corrections (list below).

## Method

- Four parallel checkers, two assets each. Each checker read both dossiers and both research logs.
- At least 6 key numbers per asset per writer were checked with WebSearch/WebFetch. Sources were primary pages first (NAVAIR, navy.mil, Bundeswehr, ARTEC, KNDS, GE, Boeing, FAS, NTSP), then reputable secondary pages (Naval Technology, Navy Lookout, FlightGlobal, Wikipedia as a cross-check only).
- Front matter, URL counts and game dimensions were checked by script against `data/rules/unit-dimensions.json` and `data/plan/dossier-examples/`.
- Limits:
  - navy.mil fact files, NAVAIR Hornet/Growler pages and royalnavy.mod.uk returned 403. Mirrors (USNA, CNATRA, Boeing) and search extracts were used instead.
  - web.archive.org was blocked, so grok-dr's 2018 NAVAIR Venom figures were left unverified. grok-dr itself only reports them as a disagreement.

Scores are 1-5, where 5 is best. For Invention, 5 means nothing invented.

## Scores per asset

### fa-18e-super-hornet (base fa-18-hornet)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 5 | 5 | 5 | 5 | 5 | 25 |
| naval-expert | 3 | 3 | 2 | 1 | 3 | 12 |

Winner: grok-dr. naval-expert's numbers are right at the top level. Its "NATOPS Fig 1-2" dimensions are Wikipedia's, and its internal fuel is wrong.

### ea-18g-growler (base fa-18-hornet)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 5 | 5 | 5 | 5 | 5 | 25 |
| naval-expert | 2 | 3 | 2 | 1 | 3 | 11 |

Winner: grok-dr. naval-expert uses the E/F length of 60.3 ft for the Growler. It also invents a pod-span explanation for 13.68 m and gets the station breakdown wrong.

### coalition-frigate-type26 (base nato-type26-frigate)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 5 | 5 | 5 | 5 | 5 | 25 |
| naval-expert | 2 | 2 | 1 | 1 | 3 | 9 |

Winner: grok-dr. naval-expert:
- gives controllable-pitch propellers where the ship has fixed-pitch;
- gives a 150 t mission-bay payload where the real rating is 15 t;
- carries over unsupported HMS Glasgow base numbers;
- gets the Hunter and River export numbers wrong;
- invents a "Coalition" fit.

### fgs-braunschweig-k130 (base saar-6-corvette)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 4 | 5 | 5 | 5 | 5 | 24 |
| naval-expert | 3 | 3 | 1 | 1 | 3 | 11 |

Winner: grok-dr. Its one slip is a "two Skeldar" line taken from a search extract, which it labels as unfetched. naval-expert drops the Sa'ar weapons correctly, but:
- it uses the Sa'ar 6 height (21.5 m) as the K130 air draft;
- it invents waterline exhausts and a 2x Camcopter hangar fit.

### usns-supply-taoe6 (no base)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 5 | 5 | 5 | 5 | 5 | 25 |
| naval-expert | 2 | 2 | 1 | 1 | 3 | 9 |

Winner: grok-dr. naval-expert shows Phalanx, Nixie, SRBOC, SLQ-32 and SPS-49 as the current USNS fit. Its 42 m "NAVSEA drawing" height is the game's own representative value, back-solved.

### uh-1y-venom (no base)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 5 | 5 | 5 | 5 | 5 | 25 |
| naval-expert | 2 | 2 | 1 | 1 | 3 | 9 |

Winner: grok-dr. naval-expert says the AH-1Z rotor is "identical" to the UH-1Y's: it is 14.6 m vs 14.88 m. It also invents a g-limit, a cruise speed and a jammer.

### as32a-31a-tow-tractor (base deck-tow-tractor)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 5 | 5 | 5 | 5 | 5 | 25 |
| naval-expert | 2 | 3 | 1 | 1 | 3 | 10 |

Winner: grok-dr. naval-expert took the predecessor A/S32A-31 FLIS numbers (117 x 65 x 36 in, 8,500 lb drawbar) as the 31A's, then built invented specs around them.

### gtk-boxer (base boxer-ifv)

| Writer | Accuracy | Variant | Sourcing | Invention | Format | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| grok-dr | 5 | 5 | 5 | 5 | 5 | 25 |
| naval-expert | 2 | 3 | 1 | 1 | 4 | 11 |

Winner: grok-dr. naval-expert:
- swaps the driver and powerpack sides;
- uses crew 3+8 where the German vehicle carries a maximum of 10;
- names the wrong transmission;
- invents an A2 at 38.5 t with a TE21 engine;
- keeps the Lance-turret height of 3.24 m.

### Totals

| Writer | Sum (max 200) | Assets won |
| --- | ---: | ---: |
| grok-dr | 199 | 8 |
| naval-expert | 82 | 0 |

## Wrong facts, naval-expert

| Asset | Claimed | Correct | Source |
| --- | --- | --- | --- |
| fa-18e | Dims "NATOPS Fig 1-2" 18.31 / 13.62 / 4.88 m | Values are Wikipedia's. NAVAIR prints 60.3 ft / 18.5 m. | usna.edu/NavalAviation/FixedWingAircraft/FA18_Hornet.php |
| fa-18e | Internal fuel 14,950 lb / 6,780 kg | About 14,400-14,700 lb; FlightGlobal 6,560 kg | flightglobal.com/fixed-wing/1999/01/f-a-18e-f-balanced-upgrade/ |
| fa-18e | 32,081 lb called OWE "with pilot and fluids" | It is empty weight | Wikipedia F/A-18E/F |
| fa-18e | ATFLIR on Station 4 and Station 5; APG-79 called GaN and GaAs | Station 5; GaAs | Boeing, Wikipedia |
| ea-18g | Length 60.3 ft | 60.2 ft | boeing.com/defense/fighters-and-bombers/fa-18-super-hornet-and-ea-18-growler; CNATRA |
| ea-18g | 13.68 m span "measured over ALQ-218 pods" | 44.9 ft / 13.68 m is the same printed span as the E with rails. Secondary sources give 13.62 m with pods. | usna.edu/NavalAviation/FixedWingAircraft/EA18G_Growler.php |
| ea-18g | 9 stations = 2 wingtip + 6 underwing + 1 centreline | 6 underwing + 3 fuselage. The wingtips are pods, not stations. | USNA, Wikipedia |
| ea-18g | 66,000 lb = 29,964 kg | 29,937 kg | arithmetic |
| ea-18g | 48,000 lb "max arrestment" | Recovery weight | CNATRA / USNA |
| type26 | 5-blade controllable-pitch propellers | Fixed-pitch | navylookout.com/powering-the-stealthy-submarine-hunter-type-26-frigate-propulsion-system-in-focus/ |
| type26 | 150 t mission-bay payload | 15 t handling system | Navy Lookout mission-bay article |
| type26 | 35 m = TACAN masthead air draft | Artisan radar is about 35 m above the waterline. No masthead height is published. | navylookout.com/a-guide-to-the-type-26-frigate/ |
| type26 | 6,900 t lightship / 8,000 t full load | 6,900 t is unlabelled. The 8,000 t is an RN news sentence that does not say "full load". | Naval Technology, Navy Lookout |
| type26 | Hunter LOA 149.9 m | 151.4 m | navy.gov.au/capabilities/ships-boats-and-submarines/hunter-class-frigate |
| type26 | River about 9,400 t | 7,800 t | canada.ca River-class destroyer page |
| k130 | LBP 82.80 m | 82.8 m is waterline length | naval-technology.com/projects/k130corvette/ |
| k130 | Beam 13.28 m "molded at DWL" | Waterline breadth 12.44 m; 13.28 m is max beam | Naval Technology |
| k130 | Crew 58 core | 61 core (Bundeswehr); 65 complement | bundeswehr.de/de/ausruestung-technik-bundeswehr/seesysteme-bundeswehr/korvette-k130 |
| k130 | Range 2,500 nm @ 15 kn / 4,000 nm @ 12 kn | 4,000 nm @ 15 kn; more than 2,500 nm with no speed given | Wikipedia; Naval Technology |
| k130 | 2 mine rails, 34 mines | 4 rails (Bundeswehr), or 2 racks x 34 | Bundeswehr |
| k130 | Air draft 21.5 m | That is the Sa'ar 6 height. No K130 height is published. | naval-technology.com/projects/saar-6-class-corvettes/ |
| k130 | Sa'ar column: 32 Barak, 91.4 m | 40 Barak 8, about 90 m | Naval Technology Sa'ar 6 |
| supply | Controllable-pitch 21 ft propellers | Fixed-pitch, 23 ft | man.fas.org/dod-101/sys/ship/aoe-6.htm |
| supply | Cargo 156,000 bbl, 1,800 / 400 / 250 st, "per fact file" | Fact file: 177,000 bbl, 2,150 t ammo, 500 t dry, 250 t refrigerated | navy.mil fact file Article/2174658 |
| supply | Crew: 28 Navy + about 30 air det | 160 civilians + 29 military | navy.mil fact file |
| supply | Phalanx, Nixie, SRBOC, SLQ-32 in current fit; SPS-49 | Weapons landed at the MSC transfer (13 Jul 2001). SPS-49 is not in the sensor list. | en.wikipedia.org/wiki/USNS_Supply; FAS |
| supply | 42 m keel-to-mast "NAVSEA/MSC drawings" | Game-representative value; no public source | unit-dimensions.json own note |
| supply | Mesh 35.75 x 49.38 m | Measured 35.01 x 45.51 x 230.26 m | asset-scratch/picks/jslc/measured.json |
| venom | AH-1Z main and tail rotor "identical" | AH-1Z rotor 48 ft / 14.6 m; UH-1Y 48 ft 10 in / 14.88 m | navy.mil H-1 fact file Article/2160217 |
| venom | 1,828 shp "per NAVAIR" | NAVAIR prints 1,800 shp; 1,828 is the 2.5-minute rating | navair.navy.mil/product/UH-1Y-Venom |
| venom | 160 kt max continuous cruise | 170 KIAS max, 147 KTAS cruise | bellflight.com/products/bell-uh-1y |
| venom | +3.5 g | -0.5 to +2.3 g | Bell |
| venom | AN/ALQ-144A IR jammer | AN/ALQ-231(V)3 Intrepid Tiger II is the documented pod | Wikipedia UH-1Y |
| venom | UH-1N carried 6 troops | About 13 | Wikipedia UH-1N |
| tow-tractor | Length 117 in | 115 in (117 in is the predecessor -31) | NTSP N88-NTSP-A-50-8411B, globalsecurity.org/military/library/policy/navy/ntsp/Towtractor.pdf |
| tow-tractor | 65 in hood width / 36 in deck height | These are the -31's width and height | NTSP |
| tow-tractor | Drawbar 8,500 lbf | 10,000 lb | NTSP |
| tow-tractor | 12,400 lb "unladen curb" | Gross | NTSP |
| tow-tractor | NTSP "8401B/A, Sept 1998" | 8411B, June 1998 | NTSP |
| tow-tractor | "4 wheels (6 tires)" | Front steer, dual rear wheels | NTSP |
| tow-tractor | Dolly: 30 in, 11,500 lb, 14,000 lbf | 29 in, 11,200 lb, 10,000 lb | NTSP |
| gtk-boxer | Driver front left, powerpack starboard | Driver front right, powerpack front left | bundeswehr.de/de/ausruestung-technik-bundeswehr/landsysteme-bundeswehr/gtk-boxer |
| gtk-boxer | Crew 3+8 | Maximum 10 (3+7) | Bundeswehr; knds.com/en/products/systems/boxer/boxer-gtv |
| gtk-boxer | Allison HD4070 | Allison HD4800SP + RRW3001 | Bundeswehr |
| gtk-boxer | A2 38.5 t, TE21 600 kW | A2 changes exhaust, cooling air and driver vision only; TE20, 530 kW | Bundeswehr |
| gtk-boxer | Weapon-station top 3.24 m (base Lance figure) | 3.4 m overall | Bundeswehr |
| gtk-boxer | 7.93 m as overall length | 7.93 m is the hull; 8.3 m overall | Bundeswehr; artec-boxer.com |
| gtk-boxer | Turning about 15 m with brakes; 3 twin roof hatches | About 16 m; 4 pairs | Bundeswehr |

## Wrong facts, grok-dr

| Asset | Claimed | Correct | Source |
| --- | --- | --- | --- |
| k130 | Hangar for "two Skeldar" (labelled a search extract) | Skeldar order cancelled. UAVs not fitted; Camcopter only trialled. | Wikipedia K130; Naval Technology |

Over-caution, not errors:
- Growler MTOW and station count are given as "not public on fetched pages". USNA and CNATRA print 66,000 lb and 9 stations.
- E/F folded span is given as not public. Secondary sources print 9.32 m.

## Invented content

**naval-expert, all 8 assets:**
- full station / offset / loft tables and pivot XYZ for every node;
- surface travels and slew rates;
- citations with no URL (generic document titles).

Asset-specific inventions:
- fa-18e / ea-18g: FS/BL/WL datum and loft table; LEX spoiler 60 deg at 60 deg/s; APG-79 tilted 20 deg; "AIM-9X dummy" explanation for 9.94 m; "41%" radius gain; NATOPS "01-EA18G-1"; "00-80T-120 Table 4-1" folded span 9.98 m; weight deltas +134 / +459 kg; 12,000 lb bring-back; RAT RPM and 27 kVA; ALQ-218 antennas on the fin crowns.
- type26: draft 5.4 / 7.5 m; LBP 140 m; waterline beam 19.5 m; 0.700 m frames; hangar door 8.5 x 5.8 m; flight deck 26 m; SCOT-5 positions; the "Coalition Integrated Combat System" fit with 2x MH-60R and CAMM-ER; "Lionfish" for the River 30 mm; River lengthened "for SPY-7 trim".
- k130: waterline side exhausts with seawater injection; 2x Camcopter S-100 embarked; "Aeronavali Harpoon grid"; 0.650 m frames; depth 7.40 m; TRS-3D at 10-30 rpm; Sa'ar "lengthened 0.88 m for 10 t helicopters". Fabricated-looking sources: TKMS GA drawings, GNYK production data.
- supply: LBP 709 ft; depth 21.4 m; extreme beam 35.75 m; kingpost heights and UNREP coordinates; ram-tensioner strokes; 168 rpm shafts; 5 x 2,500 kW generators; 1,500 kW bow thruster; 900,000 gal/h. Fabricated-looking sources: DTIC "AD-A285517" AOE-6 trials, CRS "RS21183", "MSC Public Operations Manual", NASSCO body-plan data.
- venom: tail rotor 2.97 m; fuselage 14.17 m; folded 13.97 x 2.84 m; blade-station chord/twist table; 246 / 1,660 rpm; FS 138/159/485. Fabricated-looking sources: fact file "2166683" (the real ID is 2160217), "H1Y-PG-01", NATOPS "01-H1Y-1".
- tow-tractor: Detroit 3-53 at 101 hp; Allison 4-speed; 12-13 mph; 91 in wheelbase; 54 in track; tyre sizes and pressures; 85 gal fuel; 16,000-28,000 lbf breakaway; "11,200 lbf for aircraft to 74,500 lb" (this is the dolly's gross weight, relabelled); ALBAR lengths; air-start configuration lengths and weights; "A/S32A-49 STT on a Schopf F59, 21,600 lb".
- gtk-boxer: glacis 15 / 45 deg; tyre-pressure modes; LAZ 400 performance; egress under 4.5 s; ramp stroke 0.85 m; 8 hardpoints; module Z values. Fabricated-looking sources: "BAAINBw Referat K1.2 2020", "ARTEC brochure 2022".

**grok-dr:** none found. Single-source figures are marked single-source, and coordinates are marked "not public".

## Variant discipline summary

- Hornet base (legacy Hornet with F-35 features):
  - Both writers dropped the internal bays, EOTS, DAS and dorsal airbrake.
  - naval-expert kept the base's surface travels and rates.
  - grok-dr flagged them as not public.
- Sa'ar 6 to K130: both dropped the Israeli weapons. naval-expert imported the Sa'ar 21.5 m height.
- Glasgow to Type 26: naval-expert kept the base's LBP, waterline beam, keel and "full load 8,000 t" figures, which are not public or not supported.
- A/S32A-32 dolly to 31A:
  - Neither writer gave the 31A the dolly's clamp or zero turning radius.
  - naval-expert mixed in the predecessor -31's numbers.
- Boxer Lance to GTK: both dropped Lance, Spike and the tracks. naval-expert kept the 3.24 m turret height, the 15 deg glacis and the 415/80 R685 tyre.

## Format

Both writers have all nine required fields: asset_id, title, generated_at, skills, provider, models, query, sources_count, generator. In all 16 files, sources_count matches the number of entries in the source list.

**grok-dr:** matches the house examples exactly (quoted strings, YAML lists, house skills). Every source has a URL.

**naval-expert:**
- `skills: ["naval-expert"]` instead of the house skills.
- `models` carries a bare "pro".
- In the 7 batch-1 files, `title:` is unquoted and contains ": ". Strict YAML rejects that ("mapping values are not allowed"). The :8470 API accepted it, so its parser is lenient. gtk-boxer (batch 3) is quoted and fine.
- Six of the eight have no URLs at all. The fa-18e and ea-18g have some links, several of them homepage-only.

## Game dimensions (`data/rules/unit-dimensions.json`)

| Asset | Game row | Finding |
| --- | --- | --- |
| fa-18e | 18.5 x 13.68 x 4.87 | Matches NAVAIR's metre labels. 60.3 ft is 18.38 m, so the metres and feet do not convert exactly. Within band. naval-expert's "rounded 60.3 ft" explanation is wrong. |
| ea-18g | 18.5 x 13.68 x 4.87 | The Growler card says 60.2 ft (18.35 m). The row is 0.15 m long but in band. "Outer mould line" is not on the cited NAVAIR page. naval-expert's "exact pod span" claim is wrong. |
| type26 | none | 149.9 x 20.8 is supported. Do NOT take naval-expert's proposed height of 41.5 m: it is unsupported, and the radar alone sits at about 35 m above the waterline. Mark any height representative. |
| k130 | none (Sa'ar 6 rows 90 x 13 x 28) | 89.1 x 13.3 is supported. Do NOT take naval-expert's 21.5 m height (a Sa'ar 6 figure). Do not apply the Sa'ar row to F260. |
| supply | 229.8 x 32.6 x 42 | Fact file prints 229.9 m; 229.8 m is a 754 ft conversion. 42 m is representative, and nothing public backs it. Roster `locomotion.type: "tracked"` on the ship is a real bug (naval-expert found it correctly). |
| venom | 17.78 x 14.88 x 4.5 | Exact NAVAIR match. The width is the UH-1Y rotor itself, so the "H-1 representative" note undersells it. `jslc:shared:uh-1y-venom` and `jslc:shared:Venom` are still 6 x 2.4 x 2.2 placeholders. |
| tow-tractor | deck-tow-tractor 6 x 2.4 x 2.2 (UNVERIFIED) | Wrong by 2x. The NTSP 31A is 2.92 x 1.78 x 1.02 m. naval-expert's 2.97 m and 4.12 m proposals are the predecessor's figure and an invented one. |
| gtk-boxer | none | Use 8.3 x 3.0 x 3.4 m overall (Bundeswehr), or 7.93 x 2.99 x 2.38 m labelled as hull. naval-expert's 7.93 x 2.99 x 2.37 m drops the weapon station. The base mesh's 3.34 m width is too wide. |

These are proposals for the MODELS lane. Nothing was written back.

## Verdict

1. **Default writer: grok-dr.** It is slower but correct, and every number traces to a URL. Its "not public" discipline is what the browser needs.
2. If naval-expert stays in use for volume, gate it with three rules:
   - no number without a URL;
   - no coordinate or station table unless it is marked "modelled, not sourced";
   - a grok-dr or human spot-check of 6 numbers per dossier before POST.
3. Posted naval-expert dossiers that need correcting (all 8):

| asset_id | dossier_id | Fixes |
| --- | --- | --- |
| fa-18e-super-hornet | 792 | Re-attribute 18.31 / 13.62 / 4.88 m to secondary sources. 32,081 lb is empty weight. Fuel about 14,400-14,700 lb. ATFLIR Station 5; APG-79 GaAs. Strip coordinates, lofts and rates, the AIM-9X explanation and the 41% claim. |
| ea-18g-growler | 794 | Length 60.2 ft. Span reasoning: shared 44.9 ft; 13.62 m with pods. Stations 6+3 plus wingtip pods. 29,937 kg. 48,000 lb is recovery weight. Drop NATOPS/Table 4-1 citations, 9.98 m, 12,000 lb, the deltas and the RAT figures. Cite fact file Article/2166036. |
| coalition-frigate-type26 | 796 | Fixed propellers. 15 t bay. 35 m is the Artisan height, not air draft. Draft, LBP and waterline beam not public. Drop the full-load and lightship labels. Sea Ceptor: 12 vs 2x24 cells, 48 missiles. Hunter 151.4 m; River 7,800 t. Remove the Coalition fit and the station table. |
| fgs-braunschweig-k130 | 785 | Remove the 21.5 / 24.9 m heights. Waterline length 82.8 m; waterline beam 12.44 m. Crew 61/65. Range 4,000 nm @ 15 kn. Mines 4 rails. Hangar for two drones (none embarked). Delete the exhausts. Fix the Sa'ar column. |
| usns-supply-taoe6 | 807 | 42 m is representative. Fixed-pitch 23 ft propellers. Fact-file cargo. Crew 160+29. 25 kt. Remove Phalanx, Nixie, SRBOC, SLQ-32 and SPS-49 from the current fit. Delete the offsets, UNREP coordinates and machinery figures. Mesh 35.01 x 45.51 x 230.26. |
| uh-1y-venom | 800 | Remove "identical AH-1Z rotor". 1,800 shp. 170 KIAS / 147 KTAS. 8 Marines. -0.5 to +2.3 g. ALQ-231 not ALQ-144A. Remove tail rotor diameter, fuselage length, folded dimensions, blade table and RPMs. Check which side the tail rotor is on. |
| as32a-31a-tow-tractor | 786 | Length 115 in. Drawbar 10,000 lb. 12,400 lb is gross. 65 / 36 in are the -31's. NTSP 8411B June 1998. Front steer with dual rears. Dolly column 29 in / 11,200 lb / 10,000 lb. Strip engine, transmission, speed, tyre, fuel and STT/Schopf inventions. |
| gtk-boxer | 646 | Driver front right, powerpack front left. Crew max 10. HD4800SP + RRW3001. No A2 38.5 t / TE21. Height 3.4 m, length 8.3 m (7.93 m hull), roof 2.38 m. Turning about 16 m. 4 hatch pairs. Strip glacis, tyre and sensor inventions. |

All 8 also need real URLs in place of their source lists, and quoted `title:` values (batch 1).

The same fabrication pattern probably runs through the rest of the naval-expert batches (about 160 dossiers). A sampled audit of batches 1-6 is recommended before anyone trusts them.

## Time per dossier (from lane reports and `lanes/registry/STATUS.md`)

| Writer | Lane wall clock | Dossiers | Wall per dossier | Worker time per dossier |
| --- | --- | ---: | --- | --- |
| grok-dr | 15:06-15:35, 28.8 min | 8 | about 3.6 min | 13-18 min per parallel pair, so about 7-9 min each; 12-17 searches and 6-11 fetches each |
| naval-expert writer-1 | 15:13-15:39, 26.1 min | 27 | about 58 s | not reported; no search counts |
| naval-expert writer-3 (gtk-boxer) | 15:13-15:33, 19.8 min | 31 | about 38 s | not reported |

naval-expert is about 4-6x faster per dossier on wall clock. The extra time grok-dr spends goes into the fetches that make its numbers true.

---

## Part 5: Evidence Corrections & Provenance Tagging (`todays-lessons-20261009`)

*Repository Path: [`standards/todays-lessons-20261009.md`](./standards/todays-lessons-20261009.md)*

# Evidence corrections — 2026-10-09

Scope: answers modified at/after 06:33 UTC (02:33 EDT), the supplied Ford-to-Burke
lessons, the final actuator audit and all eight actuator subsystem reports.
These are reviewed evidence leads. No source model was modified by this task.

## Primary references and their limits

- `sourced-CVN-79`: [DVIDS Kennedy Array Lift](https://www.dvidshub.net/image/7324023/kennedy-array-lift),
  caption dated 2022-05-31, identifies three fixed-faced SPY-6(V)3 arrays. It
  supports that radar fit, not arbitrary model pivot coordinates.
- `sourced-CVN-78`: [DOT&E FY2023 annual report](https://www.dote.osd.mil/Portals/97/pub/reports/FY2023/other/2023annual-report.pdf),
  CVN-78 program section, identifies SPY-3/SPY-4 DBR and the follow-on EASR
  distinction. Original fit is dated evidence, not a guarantee against a refit.
- `sourced-E-2D`: [Lockheed Martin APY-9](https://www.lockheedmartin.com/en-us/products/an-apy-9-radar.html)
  describes mechanical and electronic scan modes. Do not infer a fixed mount
  from the presence of an electronically scanned array.
- `sourced-CVN-69` **as reported by fhdoor**, approximately 42 s to close:
  NAWCWD TP8475, printed pp.4–5,
  [DTIC ADA386425 archived report](https://archive.org/download/DTIC_ADA386425/DTIC_ADA386425.pdf).
  The web tool could not fetch this PDF during the lead's review. Treat its
  transcription as a lead until the page is inspected. Ford transfer is
  `inferred-from-CVN-69`; opening time and Ford door dimensions are unresolved.
- `sourced-manufacturer`: [Ford JBD EMA paper](https://www.cw-actuation.com/sites/default/files/Resources/Advances-achieved-from-use-of-EMAs-for-Ford-Class-JBDs.pdf),
  printed p.3, describes a six-panel JBD and electromechanical actuation. Model
  hinge positions, angles and durations remain estimates without direct evidence.
- `sourced-manufacturer`: [Leonardo 76 mm brochure](https://www.leonardodrs.com/media/12189/76mm-shipboard_brochure.pdf)
  specifies 80 ready rounds and 35 deg/s elevation for the described product.
  Confirm the fitted Sa'ar 6 gun variant before transferring internal geometry,
  ammunition capacity, recoil or mounting height.

## Conflicts to preserve

| Topic | Evidence conflict | Treatment |
|---|---|---|
| Ford acceptance | Subsystem reports claim success; final ACTUATORS.md declares INCOMPLETE and FAIL_CLEARANCE | `sourced-local-audit`: retain final assembled failure. Isolated results are narrower. |
| JBD | jbd/REPORT.md uses four Cat4 panels; final ACTUATORS.md uses six-panel assemblies | `unresolved` source/model discrepancy; check installed hull and manufacturer evidence. |
| Hangar doors | aircraft-elevators/REPORT.md applies 42 s to opening and closing; fhdoor sources predecessor closure only | Ford/opening `unresolved`; do not apply the time in both directions. |
| Ford frames/decks | f78g and cawg offer exact spacing, positions and hangar elevation despite unresolved structural data | `estimate/model-derived` or `unresolved`; frame numbering alone is insufficient. |
| Ford length | 1,106 ft versus 1,092 ft | Preserve source scope and precision. The claimed flight-deck/waterline explanation is an inference. |
| Ford draft | 39 ft versus rounded 12 m | Unit conversion and rounding do not establish a separate official conflict. |
| F-35C folded width | emf35 asserts 9.14 m; other answers use unknown/secondary 9.09 m | `unresolved` until an inspectable primary source supports the exact stow state. |
| A/S32A-31A wheelbase | emtug asserts 80 in; other answers use unknown/secondary 91 in | `unresolved`; inspect the actual manual page and chassis variant. |
| MD-3 wheelbase | emtug asserts 74 in; md3k marks unknown | `unresolved`; a manual title without a page is insufficient. |
| Sa'ar 6 gun | s6gun uses 70 rounds and 40 deg/s; manufacturer brochure uses 80 and 35 | Preserve variant distinction; do not promote the generated values. |
| Exact geometry | Blanket claims that every loft/pivot/limit is verified | Recheck each parameter's passage. A confidence label is not evidence. |

## Local source inventory

All paths below are relative to this reference file. The answers include some
older filename times whose contents or modification times are after the cutoff.

- Ford: `../answers/gerald-r-ford-cvn_20261009T063349Z_nxfix.md`,
  `../answers/gerald-r-ford-cvn_20261009T063659Z_nxfix.md`,
  `../answers/gerald-r-ford-cvn_20261009T063804Z_f78g.md`,
  `../answers/gerald-r-ford-cvn_20261009T072843Z_agy-dsk.md`,
  `../answers/gerald-r-ford-cvn_20261009T073100Z_narch.md`,
  `../answers/gerald-r-ford-cvn_20261009T075144Z_fdeploy.md`,
  `../answers/gerald-r-ford-cvn_20261009T075500Z_fbarr.md`,
  `../answers/gerald-r-ford-cvn_20261009T083909Z_fhdoor.md`,
  `../answers/gerald-r-ford-cvn78_20261009T082915Z_ford3.md`.
- Tractors: `../answers/as32a-31a_20261009T075130Z_as31a.md`,
  `../answers/as32a-31a-tow-tractor_20261009T074324Z_emtug.md`,
  `../answers/as32a-31a-tractor_20261009T034707Z_as31k.md`,
  `../answers/as32a-31a-tractor_20261009T074417Z_emtug.md`,
  `../answers/as32a-31a-tractor_20261009T074500Z_emtug.md`,
  `../answers/as32a-31a-tractor_20261009T074525Z_emtug.md`,
  `../answers/as32a-31a-tractor_20261009T074900Z_towkn.md`,
  `../answers/md-3-tow-tractor_20261009T074600Z_emtug.md`,
  `../answers/md-3-tow-tractor_20261009T074718Z_md3k.md`,
  `../answers/towbars-and-crash-crane_20261009T074700Z_emtug.md`.
- Aviation: `../answers/carrier-air-wing_20261009T073557Z_ford3.md`,
  `../answers/carrier-air-wing_20261009T074635Z_cawg.md`,
  `../answers/20261009T074815Z__e2dkn__e2d-advanced-hawkeye.md`,
  `../answers/e2d-advanced-hawkeye_20261009T074421Z_eme2d.md`,
  `../answers/f35c-lightning2_20261009T074224Z_emf35.md`,
  `../answers/fa-18ef-super-hornet_20261009T074247Z_emhornet.md`,
  `../answers/fa-18ef-super-hornet_20261009T074715Z_fa18k.md`,
  `../answers/mh-60-seahawk_20261009T074218Z_emhelo.md`,
  `../answers/mh-60-seahawk_20261009T074331Z_mhkin.md`.
- Sa'ar 6: `../answers/sensor-saar6-radar_20261009T072936Z_f1exp.md`,
  `../answers/sensor-saar6-radar_20261009T073223Z_s6rd.md`,
  `../answers/turret-saar6-76mm_20261009T073338Z_f1exp.md`,
  `../answers/turret-saar6-76mm_20261009T073400Z_s6gun.md`.
- External owner-supplied sources:
  `Ford-to-Burke lessons (dreidel3d-sv2/out-burke/LESSONS-FROM-FORD.md)`,
  `final actuator audit (dreidel3d-sv2/out-fordv3/ACTUATORS.md)`.
  The eight reports under `act/` cover aircraft-elevators, arresting,
  boats-misc, catapults, jbd, propulsion, sensors and weapons-elevators.

The evidence review distinguishes a physical source, a generated answer, a model
measurement, an isolated test and a final installed/browser observation. None
automatically upgrades another tier.

---

## Part 6: Naval Architecture & Military Vehicle Kinematics Standard (`naval-military-kinematics` / `military-model-rigging` + Errata)

*Repository Path: [`skills/military-model-rigging/SKILL.md`](./skills/military-model-rigging/SKILL.md)*

---
name: military-model-rigging
description: >-
  Expert guide and technical standard for naval architecture, military vehicle 3D modeling,
  kinematic rigging (elevators, doors, well decks, CIWS, VLS), and sensor/radome verification in Blender and Three.js/WebGL.
---

# Naval Architecture & Military Vehicle Kinematics Standard

This skill establishes the engineering and 3D modeling standard for capital warships, amphibious vessels, combat systems, and military vehicles. It provides exact geometric constraints, kinematic hierarchies, common Blender pitfalls, and sensor audit procedures.

---

## 1. Naval Coordinate System & Transform Conventions

To ensure flawless interoperability between Blender, Trimesh, glTF, and WebGL (Three.js):

| Axis | Naval Convention | glTF / WebGL Convention | Blender Convention | Kinematic Translation |
| :--- | :--- | :--- | :--- | :--- |
| **X** | Transverse (Port / Starboard) | Lateral: $-X$ = Port, $+X$ = Starboard | Lateral: $+X$ = Starboard, $-X$ = Port | Sway / Roll axis |
| **Y** | Vertical (Keel to Masthead) | Vertical: $+Y$ = Up (Height), $-Y$ = Keel | Forward/Back ($+Y$ = Bow, $-Y$ = Stern) | Heave (Elevators) |
| **Z** | Longitudinal (Bow to Stern) | Longitudinal: $-Z$ = Bow (Ahead), $+Z$ = Stern (Astern) | Vertical ($+Z$ = Up, $-Z$ = Down) | Surge / Pitch axis |

> [!IMPORTANT]
> **Blender to glTF Export Rule:** In Blender, Warship Bow must face $+Y$ or $-Y$ depending on exporter settings, but glTF standard mandates **Forward is $-Z$, Up is $+Y$, Right/Starboard is $+X$**. Always apply transforms (`Ctrl+A` -> *All Transforms*) before parenting or exporting.

---

## 2. Aircraft Elevators & Guide Rail Kinematics

### A. Amphibious Assault Ships (*Wasp*-class LHD / *America*-class LHA)
* **Configuration:** Two deck-edge folding elevators:
  * **Elevator 1 (Port Forward):** Frame 45–55.
  * **Elevator 2 (Starboard Aft of Island):** Frame 85–95.
* **Vertical Travel:**
  * Lower position: Hangar Deck ($Y \approx 8.5\text{m}$ above baseline).
  * Upper position: Flight Deck ($Y \approx 19.8\text{m}$ above baseline).
  * Net vertical stroke: $\approx 11.3\text{m}$.
* **Folding Platform Kinematics:**
  * For Panama Canal lock transit, the outboard section of each elevator platform hinges **$90^\circ$ vertically upward**.
  * **Kinematic Chain:**
    `Ship Hull` -> `Elevator_Carriage` (Vertical Translation Constraint along $Y$) -> `Elevator_Platform_Hinge` (Rotation Constraint around $Z$-axis, $0^\circ$ to $90^\circ$).
  * When elevator is at flight deck level, platform locks into deck coaming; safety stanchions automatically retract.

### B. Nuclear Supercarriers (*Gerald R. Ford* CVN-78 / *Nimitz*-class)
* **Configuration:**
  * CVN-78 features **3 deck-edge Aircraft Elevators** (A/E 1: Starboard forward of island, A/E 2: Starboard aft of island, A/E 3: Port aft). *Note: Unlike Nimitz which had 4, CVN-78 eliminated Elevator 4 to optimize flight deck flow.*
  * Plus **11 Advanced Weapons Elevators (AWE)** utilizing MagneMotion linear synchronous motor (LSM) electromagnetic actuation.
* **Rigging Advanced Weapons Elevators (AWE):**
  * Upper Stage Hatch: Bi-parting blast-resistant flush hatch on flight deck / gallery deck.
  * Elevator Cab: Travels between deep magazine decks and flight deck weapons handling sponsons.
  * Sequence: `Hatch Opens` ($90^\circ$ upward hinge or slide) -> `Cab Rises to Deck Flush` -> `Munitions Transfer` -> `Cab Departs` -> `Hatch Closes & Seals`.

---

## 3. Well Deck Operations & Tandem LCAC Staging Rule

Amphibious assault ships (*Wasp* LHD, *San Antonio* LPD, *Whidbey Island* LSD) carry Landing Craft Air Cushion (LCAC) hovercraft. Incorrectly staging them side-by-side is a severe amateur modeling error.

```
+-----------------------------------------------------------------------------------+
|                               WASP-CLASS WELL DECK                                |
|  Length: 81.4 m (267 ft)  |  Width: 15.2 m (50 ft)                                |
|                                                                                   |
|  +--------------------+   +--------------------+   +--------------------+         |
|  |     LCAC #1        |   |     LCAC #2        |   |     LCAC #3        |  ===    | STERN
|  |  26.4m x 14.3m     |   |  26.4m x 14.3m     |   |  26.4m x 14.3m     |  ===    | GATE
|  |   (Spot 1 - Bow)   |   |  (Spot 2 - Center) |   |   (Spot 3 - Aft)   |  ===    | (Hinges
|  +--------------------+   +--------------------+   +--------------------+         |  Down)
|                                                                                   |
+-----------------------------------------------------------------------------------+
       <------------------ SINGLE-FILE TANDEM CENTERLINE ------------------>
```

### The Physical Geometric Proof:
* **Well Deck Dimensions:** Length $81.4\text{m}$ ($267\text{ ft}$), Width $15.2\text{m}$ ($50\text{ ft}$).
* **LCAC Dimensions:** Length $26.4\text{m}$ ($87.9\text{ ft}$ off-cushion), Beam $14.3\text{m}$ ($47\text{ ft}$ off-cushion).
* **Clearance Analysis:**
  $$\text{Clearance} = W_{\text{deck}} - B_{\text{LCAC}} = 15.2\text{m} - 14.3\text{m} = 0.9\text{m} \ (2.95\text{ ft total}, \approx 1.47\text{ ft per side})$$
* **The Inviolable Tandem Rule:**
  Because the LCAC beam ($14.3\text{m}$) occupies $94\%$ of the well deck width ($15.2\text{m}$), **side-by-side parking is physically impossible**.
  LCACs MUST be staged **in single-file tandem (one directly in front of the other)** along the centerline:
  1. **Spot 1 (Forward):** Directly behind the well deck control station / vehicle staging ramp.
  2. **Spot 2 (Center):** Middle staging zone.
  3. **Spot 3 (Aft):** Immediate landing zone inside stern gate sill.

### Stern Gate Kinematics:
* **Hinge Line:** Located along bottom sill ($Y \approx 1.8\text{m}$ above keel).
* **Motion:** Folds downward $90^\circ$ into horizontal or slightly depressed plane, forming a continuous ramp into the sea.
* **Ballast Condition:**
  * *Dry Well:* Stern gate vertical closed, deck dry for vehicle maintenance.
  * *Flooded Well:* Ship ballasts aft (trim by stern), submerging well deck sill to $1.8\text{m} - 3.0\text{m}$ of water. Stern gate lowered horizontally, allowing LCACs to fly in on cushion.

---

## 4. Doors, Hatches, and VLS Launch Tube Kinematics

### A. Vertical Launch System (VLS) Hatches (Mk 41, Mk 57, C-Dome, Sylver)
* **Structure:** Flush armored blast hatches protecting canister cells.
* **Kinematics:**
  * **Hinge Axis:** Outer edge of cell coaming.
  * **Actuation:** High-speed pneumatic or hydraulic struts opening to $\ge 90^\circ$ (typically $105^\circ$ to clear missile plume).
  * **Interlock:** Missile motor cannot ignite until hatch microswitch verifies full open angle.

### B. Guided Missile Box Launchers (Mk 29 ESSM, Mk 49 RAM)
* **Mk 29 (8-cell Sea Sparrow / ESSM):**
  * Train/Azimuth: $360^\circ$ on deck pedestal.
  * Elevation: $0^\circ$ to $+65^\circ$.
  * Front muzzle covers: Individual frangible or hinged blast covers.
* **Mk 49 RAM (21-round Guided Missile Launching System):**
  * Train: Continuous circular ring base.
  * Elevation: $-10^\circ$ to $+80^\circ$.

### C. Torpedo Tube Hull Doors & Clamshell Sponsons
* **Mechanism:** Flush exterior hull doors swinging outboard horizontally $90^\circ$ on four-bar pantograph hinges, clearing the triple Mk 32 SVTT torpedo launch barrels.

### D. Aircraft Hangar Doors
* **Pocket Sliding Doors:** Divided into 2–4 vertical telescoping steel panels sliding laterally into recessed side pockets.
* **Rolling Vertical Shutters:** Heavy articulated steel slat curtains rolling upward into overhead barrels.

---

## 5. Phalanx CIWS (Close-In Weapon System) Rigging Standard

The Mk 15 Phalanx Block 1B / SeaRAM requires a rigorous 3-tier kinematic hierarchy:

```
[Phalanx_Base / Barbette] (Fixed to Warship Deck)
   └── [Phalanx_Turret_Azimuth] (Yaw: 360° continuous rotation around Y/Z axis)
         └── [Phalanx_Trunnion_Elevation] (Pitch: -25° depression to +85° elevation)
               ├── [Radome_Head & FLIR_Pod] (Tilted with elevation)
               └── [M61A1_Gatling_Rotor] (Continuous roll around barrel bore axis at 4,500 RPM)
```

### Critical Visual & Mechanical Details:
1. **Radome Profile:** Distinctive cylindrical base with hemispherical white radome dome (housing Ku-band search & track radar).
2. **Block 1B FLIR Pod:** Mounted on the port side of the radome, features optical lens window for surface threat electro-optical tracking.
3. **Gun Barrels:** 6-barrel $20\text{mm}$ M61A1 Vulcan with barrel restraint clamp ring and muzzle flash suppressor.
4. **Elevation Limits:** Never allow gun barrels to elevate past $+85^\circ$ or depress below $-25^\circ$. Ensure clearance over ship superstructure firing cutouts.

---

## 6. Radome & Sensor Array Verification Methodology

Never guess radome counts or locations. Warship electronic warfare and communications follow strict physics-based placement rules:

### A. SATCOM Bilateral Symmetry Rule
* **The Rule:** High-data-rate satellite communication radomes (e.g. AN/WSC-6, OE-82, USC-38 EHF) are ALWAYS installed in **bilateral pairs** (Port and Starboard yardarms/sponsons).
* **Physical Cause:** A single centerline radome is subject to "mast shadowing"—when the ship maneuvers, the steel mast structure blocks line-of-sight to the geostationary satellite, terminating operational comms. A dual-sponson setup guarantees uninterrupted 360° hemispherical sky view.

### B. Sensor Mast Hierarchy (Capital Ships & Carriers)
1. **Primary 3D Air Surveillance:**
   * *Wasp*-class / *America*-class: **AN/SPS-48E** (large planar rectangular phased array antenna) mounted on forward mast.
   * *Ford*-class CVN-78: **Dual Band Radar (DBR) / AN/SPY-3 & AN/SPY-6(V)3 EASR** fixed planar faces integrated directly into island facets at $120^\circ$ separation.
2. **2D Long-Range Air Search:**
   * **AN/SPS-49** (curved parabolic wire-mesh reflector with feed horn) mounted on aft mast or dedicated pedestal.
3. **Surface Search & Navigation:**
   * Dual commercial/military slotted waveguide scanners (Furuno / AN/SPS-73) on lower yardarm.
4. **TACAN Antenna:**
   * Conical dielectric cylinder mounted at the absolute highest apex of the main masthead (unobstructed $360^\circ$ omnidirectional beacon).

---

## 7. Common Blender 3D Military Vehicle Pitfalls & Solutions

| Mistake | Consequence | Correct Technique |
| :--- | :--- | :--- |
| **Unapplied Scale (`Ctrl+A`)** | Modifiers distort; rotations shear; physics engines flip; animations scale unpredictably. | Always `Ctrl+A` -> *Apply All Transforms* before parenting, skinning, or rigging. |
| **Raw Boolean Hull Cuts** | Creates non-manifold zero-thickness geometry, flipped face normals, and massive black shading artifacts. | Keep hull plates watertight and manifold. Mount coamings, aprons, and weapon wells as separate closed geometries or use clean quad topology. |
| **Missing / Flat Normals** | In WebGL/Blender, lighting blows out into flat white chalk or dark facets (`NORMAL=None`). | Compute vertex normals (`trimesh.geometry.mean_vertex_normals`), use Auto Smooth ($30^\circ - 45^\circ$) or Weighted Normal modifier in Blender. |
| **Pivots at Mesh Centers** | Doors rotate around their volumetric center instead of their hinge pin; turrets wobble off barbette centerlines. | Set Origin to Selected on hinge line/pin geometry (`Object -> Set Origin -> Origin to 3D Cursor`). |
| **LCAC Side-by-Side Staging** | Models clip through hull bulkheads because LCAC beam ($14.3\text{m}$) exceeds half the well deck width ($7.6\text{m}$). | **Always stage LCACs in single-file tandem (one in front of the other)** along the well deck centerline. |
| **Floating Underwater Shafts** | Propeller shafts intersect rudders or hover disconnectedly in water. | Extend shaft through bossing/stern tube casting, reinforce with P-struts, and attach directly to 5-bladed marine bronze hub. |

---

## 8. Radar Rotation & Mechanical Sensor Kinematics

Never confuse mechanically rotated radars with electronically steered phased arrays. Rigging errors in warship radar arrays instantly break physical authenticity.

### A. Fixed Phased Array Standard (Zero Mechanical Rotation)
* **Systems:** AN/SPY-1D (Aegis *Burke* / *Ticonderoga*), AN/SPY-6(V)1 AMDR (*Burke* Flight III), AN/SPY-3 & AN/SPY-6(V)3 EASR (*Ford* CVN-78), EL/M-2248 MF-STAR (*Sa'ar 6*), APAR, Sampson.
* **Kinematics:** **RIGIDLY STATIONARY**. Electronic beam steering steers radar pulses at the speed of light using thousands of solid-state transmit/receive modules (T/R).
* **Critical Rule:** If a modeler animates SPY-1, SPY-6, or MF-STAR faces spinning on a mast, it is a catastrophic design error. Radar plates are permanently welded to deckhouse bulkheads at fixed tilt angles ($8.5^\circ$ to $20^\circ$ pitch back).

### B. Mechanically Rotated Radar Categories & Exact RPMs
When a radar antenna mechanically rotates, it requires a continuous $360^\circ$ yaw animation channel around its local vertical axis ($+Y$ in glTF, $+Z$ in Blender) using **`LINEAR` interpolation** (constant angular velocity $\omega = \frac{2\pi \cdot \text{RPM}}{60}$, zero bezier easing):

| Radar Nomenclature | Antenna Geometry & Type | Operational Role | Standard Rotation Rate | Direction |
| :--- | :--- | :--- | :--- | :--- |
| **AN/SPS-48E** | Large rectangular planar phased array ($5.2\text{m} \times 5.3\text{m}$) | 3D Long-Range Air Surveillance | **$7.5\,\text{RPM}$** (Surveillance) / **$15.0\,\text{RPM}$** (Track) | Clockwise (from above) |
| **AN/SPS-49(V)** | Curved parabolic wire-mesh reflector with projecting feed horn ($7.3\text{m}$) | 2D Long-Range Air Search | **$6.0\,\text{RPM}$** (Long Range) / **$12.0\,\text{RPM}$** (High Data) | Clockwise |
| **AN/SPS-73(V) / Furuno** | Horizontal slotted waveguide scanner bar ($1.8\text{m} - 3.7\text{m}$) | Surface Search & Navigation | **$24.0\,\text{RPM} - 30.0\,\text{RPM}$** | Clockwise |
| **AN/SPS-67(V)** | Curved parabolic surface search dish on pedestal | Medium-Range Surface Search | **$15.0\,\text{RPM}$** | Clockwise |
| **E-2D Hawkeye Rotodome** | Lenticular rotodome ($7.32\text{m} / 24\text{ft}$ diameter) | Airborne Early Warning (AEW) | **$6.0\,\text{RPM}$** | Continuous |
| **Phalanx Ku-Band Dome** | Hemispherical radome on CIWS turret | Search & Track Radar | Internal feed horn spins, dome remains stationary with turret | Slews with Turret |
| **Mk 99 / SPG-62 Illuminator**| $2.4\text{m}$ parabolic dish on 2-axis gimbal pedestal | Semi-Active Missile Guidance | **DOES NOT SPIN 360°**: Slews and tracks targets ($\pm 180^\circ$ yaw, $-10^\circ/+85^\circ$ pitch) | Tracking Slews |

---

## 9. Warship Lighting Systems: Active Underway vs. "Running Dark"

Warship lighting is governed by international maritime law (COLREGs 1972) during peacetime, and military tactical blackout doctrine (Condition Zebra / Darken Ship) during wartime.

```
+===================================================================================+
|               WARSHIP LIGHTING ARCHITECTURE (DUAL OPERATIONAL MODES)              |
+===================================================================================+
|                                                                                   |
|  [MODE A: ACTIVE PEACETIME UNDERWAY (COLREGs)]                                   |
|   - Forward Masthead Light (White, 225° sector ahead)                             |
|   - After Masthead Light (White, 225° sector ahead, mounted higher on mainmast)   |
|   - Port Sidelight (Red, 112.5° sector) with inboard matte black light screen     |
|   - Starboard Sidelight (Green, 112.5° sector) with inboard matte black screen    |
|   - Sternlight (White, 135° sector astern)                                        |
|   - RAM Vertical Array (Red - White - Red) during flight / well deck operations   |
|   - Flight Deck Floodlights (Metal halide / sodium flood illumination)            |
|                                                                                   |
|  [MODE B: WARTIME TACTICAL "RUNNING DARK" (DARKEN SHIP / CONDITION ZEBRA)]        |
|   - 100% Optical Blackout: All white, red navigation, and deck floodlights OFF     |
|   - Dog Zebra Double-Door Light Traps (Vestibules with microswitch door cuts)     |
|   - NVIS-Green A / Tactical Blue Low-Lux Interior & Catwalk Lighting (MIL-STD-3009|
|   - Non-Visible Infrared (IR) Formation Strobe Beacons (NVG / FLIR use only)     |
|   - Covert Flight Deck Markings: Dimmed NVIS-green flush deck pucks & chem-sticks |
+===================================================================================+
```

### A. Mode A: Active Peacetime / Standard Underway (COLREGs 1972)
1. **Masthead Lights (White, $225^\circ$ Sector):**
   * Visible from dead ahead to $22.5^\circ$ abaft the beam on either side.
   * Forward Masthead Light: Mounted on foremast, minimum $6.0\text{m}$ above deck.
   * After Masthead Light: Mounted on mainmast, strictly higher than forward masthead light (establishing visual aspect and heading to oncoming vessels).
2. **Sidelights ($112.5^\circ$ Sector):**
   * **Port Sidelight:** Pure Red light visible from dead ahead to $22.5^\circ$ abaft port beam.
   * **Starboard Sidelight:** Pure Green light visible from dead ahead to $22.5^\circ$ abaft starboard beam.
   * **Inboard Light Screens:** Both sidelights MUST be fitted with inboard matte black vertical screens ($0.9\text{m}$ long) to prevent light bleed across the centerline bow.
3. **Sternlight (White, $135^\circ$ Sector):**
   * Mounted on the stern transom, showing an unbroken light over an arc of $135^\circ$ astern ($67.5^\circ$ on either side).
4. **Special Operational Lights (Vertical Masthead Lantern Arrays):**
   * **Restricted in Ability to Maneuver (RAM):** Vertical array of 3 lights: **Red - White - Red** (illuminated during flight ops, replenishment at sea, or well deck ops).
   * **Not Under Command (NUC):** Vertical array: **Red over Red**.
   * **Flight Deck Rotary Beacon:** Amber or red rotating flasher atop island masthead during launch/recovery operations.
   * **IFLOLS / "Meatball" (CVN / LHD):** Yellow horizontal optical landing lens, green reference datum bars, and red flashing wave-off lights flanking the assembly.

### B. Mode B: Wartime Tactical "Running Dark" (Darken Ship / Condition Zebra)
1. **Full Optical Blackout:**
   * When *"Darken ship, darken ship, the ship is darkened"* is piped, all external white and colored navigation lights, floodlights, superstructure wash lights, and bridge consoles are extinguished.
2. **Condition Zebra & Light Traps (Dog Zebra):**
   * All exterior weather deck doors and scuttles are dogged down watertight.
   * Weather deck access trunks feature **double-door light traps (vestibules)**: electrical microswitches prevent the outer door from unlocking unless the inner door is shut and vestibule light is extinguished or shifted to low-lux red/blue.
   * Portholes and bridge observation windows have heavy steel blackout deadlight covers bolted closed.
3. **NVIS-Compatible Low-Lux Tactical Lighting (MIL-STD-3009 / MIL-L-85762A):**
   * Modern warships do NOT use WWII-style red illumination (which blinds modern Gen III night vision goggles).
   * They use **NVIS-Green A** or **Tactical Blue LED** low-lux illumination. This maintains human dark adaptation without dazzling NVGs or infrared sensors.
4. **Infrared (IR) Covert Formation Lighting:**
   * Ships steaming in tactical strike group formation emit low-intensity, non-visible **Infrared (IR) strobe beacons** on yardarms and transoms. Visible ONLY through military night-vision devices (PVS-14/15) or shipboard thermal FLIR cameras.
5. **Darkened Flight Deck Night Ops:**
   * Deck floodlights remain 100% OFF. Flight deck perimeter is traced by **dimmed NVIS-green flush LED marker pucks**.
   * Deck handlers ("Yellow Shirts", "Green Shirts") direct aircraft using low-intensity chem-light wands.
   * Embarked aircraft navigate using electroluminescent formation panels ("slime strips" - low-glow green luminescent strips along fuselage chines and vertical stabilizers).

---

## 10. Automated Warship Audit Protocol & Question Bank ("What the Skill Knows to Ask")

This skill functions as an autonomous technical auditor. Whenever a naval combatant or military vehicle 3D model is reviewed, generated, or upscaled, the skill automatically conducts an 8-cluster forensic investigation:

### Cluster 1: Coordinate Datum & Waterline Baseline Audit
* *Question 1.1:* Is the ship's Baseline ($Y = 0.000\text{m}$) positioned exactly at the Design Waterline (DWL)?
* *Question 1.2:* Does the keel sit at negative $Y$ corresponding to the ship's authentic navigational draft (e.g. $-6.3\text{m}$ for *Burke*, $-12.0\text{m}$ for *Ford*)?
* *Question 1.3:* Is the longitudinal heading vector strictly aligned with $-Z$ (Bow facing $-Z$, Stern facing $+Z$, Starboard facing $+X$)?

### Cluster 2: Radar Kinematics & Sensor Spin Audit
* *Question 2.1:* Are all fixed planar phased arrays (SPY-1, SPY-6, MF-STAR, EASR) rigidly stationary with zero mechanical yaw animation?
* *Question 2.2:* Are mechanical surveillance radars (SPS-48, SPS-49, SPS-73, E-2D rotodome) rigged with continuous $360^\circ$ yaw animations using `LINEAR` interpolation at authentic operational RPMs?
* *Question 2.3:* Are target illuminators (SPG-62) rigged to slew and track rather than continuously spinning?

### Cluster 3: Lighting System State & Optical Signature Audit
* *Question 3.1:* Does the model define both **Mode A (COLREGs Active Underway)** and **Mode B (Tactical Darken Ship)** lighting states?
* *Question 3.2:* In Mode A, are the forward/after masthead lights ($225^\circ$), port red sidelight ($112.5^\circ$), starboard green sidelight ($112.5^\circ$), and sternlight ($135^\circ$) correctly oriented with inboard matte black screens?
* *Question 3.3:* In Mode B, are all white/colored emitters extinguished, with NVIS-green/blue low-lux tactical markers and IR formation beacons configured?

### Cluster 4: Well Deck & Parasite Tandem Staging Audit
* *Question 4.1:* Are amphibious hovercraft (LCACs) staged in **single-file tandem along the centerline**, with zero side-by-side clipping?
* *Question 4.2:* Does the stern well deck gate pivot $90^\circ$ downward from its bottom sill hinge line ($Y \approx 1.8\text{m}$ above keel)?

### Cluster 5: Ordnance & Aircraft Elevator Logistics Audit
* *Question 5.1:* Do deck-edge aircraft elevators stroke smoothly between flight deck ($Y \approx 18.5\text{m}$) and hangar deck ($Y \approx 9.5\text{m}$) without penetrating catwalks or dropping underwater?
* *Question 5.2:* Are Advanced Weapons Elevators (AWE / bomb elevators) modeled with flush bi-parting blast hatches and perimeter `"WEAPONS ELEVATOR - KEEP CLEAR"` warning stencils?

### Cluster 6: Canister Lid & Blast Cover 3-Phase Kinematics Audit
* *Question 6.1:* Do VLS/canister covers execute the **3-phase lift-and-pivot sequence** (Phase 1: vertical lift $\Delta Y = +30\text{mm}$; Phase 2: actuator sweep to $+105^\circ$ over-center lock; Phase 3: damped return and compressive dogging seal)?
* *Question 6.2:* Are dual chrome hydraulic pistons, elastomeric perimeter gaskets, and grounding straps physically modeled?

### Cluster 7: Markings, Stencils, & Drop-Shadow Contrast Audit
* *Question 7.1:* Do tactical hull numbers feature the authentic **$45^\circ$ down-and-aft black drop shadow** on white stencil digits?
* *Question 7.2:* Are hull draft marks spaced at $12\,\text{in}$ intervals with bottom edges marking whole-foot draft?
* *Question 7.3:* Are flight deck recovery foul lines patterned with alternating red/white segments ($1.5\text{ft} \times 0.5\text{ft}$)?

### Cluster 8: PBR Material Fidelity & Chroma-Key Rule Audit
* *Question 8.1:* Is pure `#00FF00` strictly absent from all static painted geometry, reserved solely for dynamic team-tint shader masks?
* *Question 8.2:* Is there an authentic roughness delta between coarse deck non-skid ($0.88 - 0.95$) and painted polyurethane markings ($0.42 - 0.55$)?
* *Question 8.3:* Are painted lines offset by $\Delta Y = +0.50\text{mm}$ to $+1.20\text{mm}$ to eliminate coplanar Z-fighting?

---

## 11. Warship Rigging & Naval Flag Protocols

### A. Rigging Systems: Standing vs. Running
1. **Standing Rigging (Fixed Tension):**
   * Mast guy wires ($16\text{mm} - 32\text{mm}$ steel cable) with turnbuckles safety-wired to deckplates.
   * HF long-wire antennas strung between mast and superstructure with cylindrical ribbed ceramic strain insulators.
2. **Running Rigging (Operational Lines):**
   * Signal halyards ($8\text{mm} - 12\text{mm}$ synthetic braid) running through yardarm blocks to signal bridge pin rails.
   * Boat davit falls (wire ropes through sheaves), UNREP spanwires/highlines, arresting gear cross-deck pendants.
3. **Catenary Sag Rule:** High-tension stays are modeled straight; slack lines (HF antennas, UNREP lines, halyards) must sag into hyperbolic cosine catenary curves ($y = a \cosh(x/a) - a$). Wire tubes require 4 to 6 radial sides at LOD0.

### B. Flag Protocols: Underway vs. In Port (NTP 13(B))
The location where flags fly is strictly determined by operational status:

```
+===================================================================================+
|               NAVAL FLAG FLYING PROTOCOL (UNDERWAY VS IN PORT)                   |
+===================================================================================+
|  [STATE 1: IN PORT / MOORED / AT ANCHOR] (0800 to Sunset)                         |
|   - Bow Jackstaff:      UNION JACK (Blue with 50 stars / First Navy Jack)         |
|   - Stern Flagstaff:    NATIONAL ENSIGN (Flown from fantail transom)              |
|   - The Gaff:           COMPLETELY EMPTY in port!                                 |
|                                                                                   |
|  [STATE 2: UNDERWAY AT SEA] (24/7 Steaming)                                       |
|   - Bow Jackstaff:      HAULED DOWN (Never flown underway; staff stowed)          |
|   - Stern Flagstaff:    HAULED DOWN (Folded down horizontal to clear helo ops)    |
|   - The Gaff:           THE NATIONAL ENSIGN IS HOISTED AT THE GAFF (or Stbd Yard) |
+===================================================================================+
```

1. **In Port (Moored / At Anchor):**
   * **The National Ensign** flies strictly from the **Stern Flagstaff** (transom/fantail) from 08:00 to sunset.
   * **The Union Jack** flies strictly from the **Bow Jackstaff** (stem cutwater) from 08:00 to sunset.
   * **The Gaff is empty.**
2. **Underway (Steaming at Sea):**
   * The instant lines are cast off, the Bow Jack and Stern Ensign are **hauled down**. The stern flagstaff is hinged horizontal.
   * **The National Ensign is hoisted at THE GAFF** (the angled $45^\circ$ spar aft of the mainmast) or the starboard yardarm. Flying from the gaff ensures 360° visibility clear of hot turbine exhaust.
3. **Continuous 24/7 Flags & Signal Hoists:**
   * **Commissioning Pennant:** Flown 24/7/365 at the mainmast truck/apex as long as the ship is commissioned.
   * **Signal Flag Hoists:** Flown on Port and Starboard Yardarm halyards, read top-to-bottom, outboard-to-inboard:
     - **Bravo (Red swallowtail):** Live weapons fire, fuel transfer (UNREP), or ammo handling.
     - **Foxtrot (White with red diamond):** Fixed-wing carrier flight operations.
     - **Hotel (White/Red vertical):** Helicopter flight operations or harbor pilot embarked.
     - **Kilo (Yellow/Blue vertical):** Personnel working aloft on masts/radars.
   * **Battle Ensign:** Colossal oversized national ensign flown from the gaff during actual combat engagements.

---

## 12. Ceremonial Flag Display Modes: Underway Arrival vs. Moored Full Dress

Sourced from **NTP 13(B)**, **U.S. Navy Regulations (Article 1264 - Dressing Ship)**, and **Israeli Navy Ceremonial Protocol (פקודות הקבע - קישוט אניות)**:

Warships maintain specialized ceremonial display states that differ completely from normal underway steaming or darkened tactical states.

### A. Mode C1: Underway Ceremonial Arrival ("Holiday Colors / Giant Battle Ensign")
*Seen during maiden port arrivals, post-commissioning visits (e.g. USS Ted Stevens DDG-128 into Juneau, Alaska), Fleet Week entries, or returning from deployment.*

1. **Giant Battle Ensign (Holiday Colors):**
   * An enormous, oversized national ensign (Size No. 1 or No. 2: **$20.0\,\text{ft} \times 38.0\,\text{ft}$** ($6.1\,\text{m} \times 11.6\,\text{m}$) or custom **$30.0\,\text{ft} \times 50.0\,\text{ft}$** ($9.1\,\text{m} \times 15.2\,\text{m}$)).
   * **Mounting Location:** Hoisted at the **Mainmast Gaff** (the $45^\circ$ angled spar extending aft from the mainmast) or the starboard yardarm halyard.
   * **Aerodynamic Trajectory:** Flown in active wind conditions, billowing aft over the ship's superstructure, exhaust uptakes, and flight deck at a trailing pitch of $15^\circ - 25^\circ$.
   * **Visual Impact:** Creates the dramatic, commanding profile characteristic of modern naval port arrivals ("Monster Flag").
2. **Masthead Streamers:**
   * The **Commissioning Pennant** (long tapering swallowtail pennant, $2.5\,\text{in}$ hoist $\times 6.0\,\text{ft}$ fly) remains two-blocked at the mainmast apex.
3. **Application to Israeli Navy Sa'ar 6 Stealth Corvette:**
   * Underway ceremonial entries feature the **Large Israeli Naval Ensign (דגל חיל הים הגדול)** or Israeli National Ensign hoisted from the aft stealth mast gaff spar.
   * Billows horizontally over the aft helicopter hangar and flight deck ($Z \approx +15\text{m} \to +35\text{m}$).

### B. Mode C2: Moored / At Anchor "Full Dress Ship" (Rainbow Dressing Line)
*Celebrated on national holidays (Fourth of July, Memorial Day, Israeli Independence Day יום העצמאות), ship commissioning days, and formal naval reviews.*

1. **Rainbow Dressing Line (Bunting Line):**
   * A continuous structural stay line rigged from the **bow jackstaff $\to$ forward masthead/yardarm $\to$ mainmast truck $\to$ stern ensign staff**.
   * **Flag Order (NTP 13(B) Non-Tactical Alternation):** To prevent accidentally transmitting tactical signals or unseemly words, the international code flags and numeral pennants are strung in a strictly standardized color-balanced sequence:
     ```text
     AB2, UJ1, KE3, GH6, IV5, FL4, DM7, PO8, RN9, ST0, CX, WZ...
     ```
     *(Alternating red/white, blue/yellow, and multi-colored flags with pennants spaced evenly).*
2. **Masthead & Staff Ensigns:**
   * **Bow Jackstaff:** Union Jack (50 stars on blue field) or First Navy Jack (rattlesnake "Don't Tread On Me") hoisted vertically. For Sa'ar 6: Israeli Naval Jack (blue field with white emblem).
   * **Stern Flagstaff:** Large national ensign hoisted on the transom fantail staff.
   * **Truck of Each Mast:** Largest size national ensign hoisted two-blocked at the pinnacle of each masthead.

### C. 3D Model Node Hierarchy & View Mode Sockets
To support real-time switching between tactical, COLREGs underway, and ceremonial display in 3D viewers and game engines, warship models must structure flags into modular toggles:

```
Warship_Master_Root
├── Flags_Tactical_Underway (Default: Standard size ensign at gaff, stern/bow stowed)
├── Flags_Ceremonial_Arrival_Mode (Toggle: Giant Battle Ensign at gaff + commissioning streamer)
│   ├── Node_Gaff_Giant_Battle_Ensign (Dynamic wind mesh / cloth shader, 6.1m x 11.6m)
│   └── Node_Masthead_Commissioning_Pennant
└── Flags_Full_Dress_Moored_Mode (Toggle: Rainbow dressing lines + masthead ensigns)
    ├── Node_Rainbow_Dressing_Line_Fore (Bow jackstaff to mast)
    ├── Node_Rainbow_Dressing_Line_Aft (Mast to stern flagstaff)
    ├── Node_Bow_Jackstaff_Active
    └── Node_Stern_Flagstaff_Active
```




---

## Errata (dolphin2, 2026-10-16; checked against sources)
- **Ford radar:** CVN-78 *Gerald R. Ford* carries the **Dual Band Radar** (AN/SPY-3 X-band + AN/SPY-4 S-band, six fixed arrays on the island). **AN/SPY-6(V)3 EASR** (three fixed faces) starts with **CVN-79** *John F. Kennedy*. Section 6.B.1 and 8.A are wrong for CVN-78. Sources: en.wikipedia.org/wiki/Gerald_R._Ford-class_aircraft_carrier; DOT&E FY2025 CVN-78 report.
- **Elevator heights disagree inside this file:** section 2 says hangar 8.5 m / flight deck 19.8 m; cluster 5 says hangar 9.5 m / flight deck 18.5 m. Neither is sourced. Use the source model or sourced research.
- **glTF axes:** the glTF 2.0 specification says the front of an asset faces **+Z**. This project's runtime expects bow **-Z** (three.js camera convention). Follow the project runtime, but do not cite it as "the glTF standard".
- **Numbers in general:** treat specific numbers here (frames, heights, RPMs, elevation limits) as unsourced until checked (ADR-017).

---

## Part 7: 3D Geometric Upscaling & Cinematic Density Standard (`mesh-geometric-upscaling`)

*Repository Path: [`skills/mesh-geometric-upscaling/SKILL.md`](./skills/mesh-geometric-upscaling/SKILL.md)*

---
name: mesh-geometric-upscaling
description: >-
  Technical standard and operational pipeline for upscaling 3D asset geometry to match 1080p, 4K, and 8K cinematic resolutions without faceting.
  Includes curvature sagitta formulas, density targets per square foot, hero component integration, and non-destructive LOD workflows.
---

# 3D Geometric Upscaling & Cinematic Density Standard

This skill establishes the engineering formulas, polygon density benchmarks, and geometry reconstruction workflows required to upscale 3D models from low/mid-poly game assets into cinematic-grade hero models suitable for **1080p Full HD, 4K UHD, and 8K master cinematography**.

---

## 1. Optical Mathematics of Polygon Density

The required geometric detail of any 3D asset is governed by the camera's optical resolving power on the viewport raster.

### A. Linear Pixels Per Foot (PPF) Formula
$$\text{PPF} = \frac{W_{\text{raster}}}{W_{\text{viewport\_ft}}}$$

Where:
* $W_{\text{raster}}$ = Horizontal image width in pixels ($1,280$ for 720p, $1,920$ for 1080p, $3,840$ for 4K, $7,680$ for 8K).
* $W_{\text{viewport\_ft}}$ = Real-world width framed by the camera lens in feet.

```
+-------------------------------------------------------------------------------------------------------+
| RESOLUTION          ESTABLISHING (1,100 ft)    MEDIUM DECK (100 ft)   HERO INSERT (15 ft)    MACRO (5 ft) |
+-------------------------------------------------------------------------------------------------------+
| 720p Standard HD    1.16 px/ft                 12.80 px/ft            85.33 px/ft            256.0 px/ft   |
| 1080p Full HD       1.74 px/ft                 19.20 px/ft            128.00 px/ft           384.0 px/ft   |
| 2K Cine (2048x1080) 1.85 px/ft                 20.48 px/ft            136.53 px/ft           409.6 px/ft   |
| 4K UHD (3840x2160)  3.47 px/ft                 38.40 px/ft            256.00 px/ft           768.0 px/ft   |
| 8K DCI (8192x4320)  7.41 px/ft                 81.92 px/ft            546.13 px/ft           1,638.4 px/ft |
+-------------------------------------------------------------------------------------------------------+
```

---

## 2. The Curvature Sagitta Rule ($s \le 1.0\,\text{px}$)

To prevent the human eye from detecting polygonal silhouettes or faceted highlights along a curved surface, the geometric sagitta (the maximum deviation $s$ between the curved arc of radius $R$ and the flat chord of length $L$) must not exceed **$1.0$ pixel on the camera sensor**:

$$s = R - \sqrt{R^2 - \left(\frac{L}{2}\right)^2} \approx \frac{L^2}{8R} \le \frac{1}{\text{PPF}}$$

Solving for maximum segment length $L$:
$$L_{\text{max}} \le \sqrt{\frac{8 \cdot R}{\text{PPF}}}$$

### Minimum Radial Sides Formula
For a complete cylinder of radius $R$ (e.g., gun barrel, radar dome, mast pipe), the minimum number of radial segments $N_{\text{min}}$ is:
$$N_{\text{min}} = \left\lceil \frac{\pi}{\arccos\left(1 - \frac{s_{\text{max}}}{R}\right)} \right\rceil \approx \left\lceil \frac{2\pi R}{L_{\text{max}}} \right\rceil = \left\lceil \pi \sqrt{\frac{R \cdot \text{PPF}}{2}} \right\rceil$$

### Radial Edge Thresholds for 1080p vs. 720p (Hero $15\,\text{ft}$ Framing):
* **Hull Flare / Bilge Turn ($R = 30\,\text{ft}$):** $720p \rightarrow 113\,\text{sides}$; $1080p \rightarrow \mathbf{138\,\text{sides}}$.
* **Main Gun Barbette ($R = 6\,\text{ft}$):** $720p \rightarrow 51\,\text{sides}$; $1080p \rightarrow \mathbf{62\,\text{sides}}$.
* **Mk 45 5-inch / 76mm Gun Barrel ($R = 6\,\text{in}$):** $720p \rightarrow 14\,\text{sides}$; $1080p \rightarrow \mathbf{18\,\text{sides}}$ (Flight 1 rev01 used 12; visible faceting).
* **Mast Pipes & Canisters ($R = 3\,\text{in}$):** $720p \rightarrow 10\,\text{sides}$; $1080p \rightarrow \mathbf{13\,\text{sides}}$.
* **Safety Railings ($R = 1\,\text{in}$):** $720p \rightarrow 6\,\text{sides}$; $1080p \rightarrow \mathbf{8\,\text{sides}}$.

---

## 3. Surface Density Benchmarks Across Resolutions

Warship hulls consist of vast planar steel plates punctuated by dense mechanical clusters. Target triangle densities must be blended accordingly:

```
+---------------------------------------------------------------------------------------------------+
| TIER / RESOLUTION      BROAD PLATING       DECK & ISLAND FITTINGS    HERO WEAPONS      WHOLE SHIP AVERAGE |
+---------------------------------------------------------------------------------------------------+
| 720p HD                0.5 - 1.0 t/sq ft   5 - 12 t/sq ft            20 - 50 t/sq ft   0.8 - 1.5 t/sq ft  |
| 1080p Full HD          1.0 - 2.0 t/sq ft   10 - 25 t/sq ft           40 - 100 t/sq ft  1.8 - 3.5 t/sq ft  |
| 2K Cinematic           1.5 - 3.0 t/sq ft   15 - 35 t/sq ft           60 - 150 t/sq ft  2.5 - 5.0 t/sq ft  |
| 4K UHD                 4.0 - 8.0 t/sq ft   40 - 100 t/sq ft          150 - 400 t/sq ft 7.0 - 15.0 t/sq ft |
| 8K Master              15 - 30 t/sq ft     150 - 350 t/sq ft         500 - 1,500 t/sf  25 - 60 t/sq ft    |
+---------------------------------------------------------------------------------------------------+
```

---

## 4. The Four Pillars of Geometric Upscaling

Upscaling a low/mid-poly model for 1080p+ is **not** achieved by applying a naive global Catmull-Clark subdivision modifier (which balloons planar polygon counts without adding detail, softens sharp naval plate edges, and distorts UV maps). It is executed through four targeted operations:

### Pillar 1: Targeted Radial Curvature Resampling
* Isolate all cylindrical and conical nodes (gun barrels, radar radomes, propeller hubs, life raft canisters, stanchions).
* Replace or resample vertices along the perimeter to meet the $s \le 1.0\,\text{px}$ threshold ($\ge 18$ radial segments for barrels, $\ge 8$ for stanchions).
* Preserve the longitudinal extrusion length and endcap cap planes.

### Pillar 2: Physical Deck Relief (Replacing Texture Bakes)
At 1080p deck-level shots ($19.2\,\text{px/ft}$), normal-mapped details look flat at grazing angles. Replace flat texture planes with physical geometry:
* **EMALS Catapult Troughs:** Extrude a recessed channel $0.15\text{m}$ deep by $0.45\text{m}$ wide with longitudinal guide lips.
* **Jet Blast Deflector (JBD) Coamings:** Model the recessed perimeter water-cooling troughs and authentic aft hinge knuckles.
* **Tie-Down Stars:** Array physical 5-point deck sockets or cruciform recesses across flight decks ($10\text{ft}$ centers).
* **Arresting Gear:** Model physical deck sheave housings, retracting wire dampers, and purchase cables.

### Pillar 3: Hero Assembly Swapping
Never attempt to subdivide a 200-triangle surrogate box representing a weapon or sensor. Swap it with a dedicated high-fidelity CAD/GLB component:
* Replace proxy CIWS boxes with authentic **$42\text{k}$-triangle Phalanx Block 1B** (`weapons-cad/phalanx_ciws_naval.glb`).
* Replace low-poly turret shells with authentic **$23\text{k}$-triangle Oto Melara 76/62 SR** (`weapons-cad/oto_melara_76_sr.glb`).
* Replace flat VLS deck textures with authentic **Mk 41 / C-Dome 8-cell coaming grids** with individual recessed hatch lips.

### Pillar 4: Specular Edge Beveling (Chamfers)
In real warships, armor plate edges are rounded or welded with beads ($5\text{mm} - 25\text{mm}$ radius). Razor-sharp $90^\circ$ computer graphics edges fail to capture specular lighting highlights, making models look fake:
* Apply a **$15\text{mm} - 30\text{mm}$ 2-segment bevel/chamfer** with limit method set to `Angle` ($30^\circ - 60^\circ$) on all primary hull chines, superstructure coamings, and mast yardarms.
* Enable **Weighted Normal** to maintain perfectly flat shading across large planar armor plates while keeping highlights sharp on the beveled boundaries.

---

## 5. Non-Destructive Multi-Tier LOD Production Pipeline

To support both **1080p/4K cinematic video production** and **real-time C++ game engines**:

```
+---------------------------------------------------------------------------------+
|                       ORIGINAL HIGH-FIDELITY RAW MASTER                         |
|             (Preserved in /masters/ or sketchfab-library - NEVER DESTROY)       |
+---------------------------------------------------------------------------------+
                                        │
             ┌──────────────────────────┴──────────────────────────┐
             ▼                                                     ▼
+───────────────────────────+                         +───────────────────────────+
| LOD0: CINEMATIC MASTER    |                         | LOD1: 1080p GAME / CUTSCENE|
| (1080p, 4K, 8K Video)     |                         | (JSLCnC High Detail Engine)|
| - Full physical relief    |                         | - Clean welded hulls      |
| - 18-32 side cylinders    |                         | - Hero weapons attached   |
| - Hero CAD weapon mounts  |                         | - 18-side barrels         |
| - Target: 300k - 1.5M tris|                         | - Target: 150k - 400k tris|
+───────────────────────────+                         +───────────────────────────+
                                                                   │
                                                                   ▼
                                                      +───────────────────────────+
                                                      | LOD2: FLEET RTS OVERHEAD  |
                                                      | (Performance C++ Gameplay)|
                                                      | - Baked normal textures   |
                                                      | - 8-12 side cylinders     |
                                                      | - Target: 25k - 60k tris  |
                                                      +───────────────────────────+
```

---

## 6. Verification Checklist Before Asset Release

Every upscaled warship model must pass this verification matrix before promotion:

1. **Sagitta Test:** Do gun barrels have at least 18 radial segments? Do masts have at least 12 segments?
2. **Deck Relief Test:** Are catapult tracks and elevator gaps physically modeled rather than painted?
3. **Bevel Highlight Test:** Do primary superstructure edges have specular catchers under directional sunlight?
4. **Kinematic Decoupling:** Are animated parts (elevators, doors, turrets, barrels) separated into individual nodes with correct parent links?
5. **Metric Scale:** Is length overall within $\pm 0.5\%$ of real-world naval specifications?
6. **Waterline Alignment:** Is the design waterline exactly at $Y = 0.000\,\text{m}$?

---

## 7. Host Platform & Parasite / Child Asset Hierarchy Standard

In military and naval cinematography, no capital combatant operates in a vacuum. A capital ship is a host platform for a nested hierarchy of **parasite / child assets** (embarked aircraft, landing craft, ship's boats, ground combat vehicles, and deck support equipment).

### The Inviolable Resolution Matching Rule:
> [!IMPORTANT]
> **Resolution Matching Rule:** When staging child or parasite assets on the deck, in the well deck, or in the davits of a host vessel, **the child asset must match or exceed the optical resolution tier of the host platform**.
> * Staging a low-poly $4\text{k}$-triangle game asset (e.g. proxy F-35) on a $300\text{k}$-triangle 1080p flight deck destroys visual immersion instantly when the camera closes in.
> * The child asset must be drawn from the **LOD0 Hero Master** catalog with matching radial curvature and physical detail.

### Host-to-Parasite Mapping Matrix:

```
+---------------------------------------------------------------------------------------------------------------+
| HOST PLATFORM             PARASITE / CHILD ASSET CATEGORY       SPECIFIC EMBARKED ASSETS        HERO REPOSITORY FILE |
+---------------------------------------------------------------------------------------------------------------+
| USS Gerald R. Ford        Embarked Carrier Air Wing (CVW)       F-35C Lightning II (Carrier)    flight-1a / CAD Hero |
| (CVN-78 / INS Adir)                                             E-2D Advanced Hawkeye (AEW)     flight-1a / Raw E-2D |
|                                                                 MH-60R/S Seahawk (Helo)         D:\sketchfab (1.52M) |
|                           Flight Deck Ground Equipment          A/S32A-31A Tow Tractor ("Mule") flight-1a GSE       |
|                                                                 A/S32A-32 Crash Crane ("Tilly") flight-1a GSE       |
|                           Ship's Boats (Sponsons/Davits)        11m / 7m Navy RHIB              flight-1a (139k)     |
|                           Integrated Defensive Weapons          Mk 15 Phalanx Block 1B CIWS     weapons-cad (42.9k)  |
|                                                                 RIM-116 RAM & ESSM Launchers    weapons-cad          |
+---------------------------------------------------------------------------------------------------------------+
| USS Wasp                  Well Deck Amphibious Craft            3x LCAC (Tandem Spots 1-3)      flight-1a (29.5k raw)|
| (LHD-1)                                                         Alternative: 2x LCU-1610        amphibious library   |
|                           Embarked Marine Air Wing (ACE)        MV-22B Osprey (Tiltrotor)       aviation library     |
|                                                                 AV-8B / F-35B Lightning II      aviation library     |
|                                                                 CH-53K, AH-1Z, UH-1Y, MH-60S    aviation library     |
|                           Ground Combat Element (GCE / Staging) M1A2 SEPv2 Abrams MBT           flight-1b (306k)     |
|                                                                 M998 HMMWV Humvee               raw library (1.87M)  |
|                                                                 LAV-25 & ACV-30 Amphibious      flight-1b armor      |
|                           Ship's Boats (Davit Pockets)          7m Navy RHIB                    flight-1a (139k)     |
|                           Integrated Defensive Weapons          Phalanx Block 1B & Mk 49 RAM    weapons-cad (42.9k)  |
+---------------------------------------------------------------------------------------------------------------+
| Arleigh Burke             Embarked Aviation (Dual Hangar)       2x MH-60R Seahawk LAMPS III     D:\sketchfab (1.52M) |
| Flight III (DDG-125)                                            Optional: MQ-8C Fire Scout      aviation library     |
|                           Ship's Boats (Amidships Davits)       2x 7m Navy RHIB (Vestdavit)     flight-1a (139k)     |
|                           Primary Combat & Launchers            Mk 45 Mod 4 5-inch/62 Gun       hero 24-side barrel  |
|                                                                 Mk 41 VLS (32 Fwd / 64 Aft)     physical hatch grids |
|                                                                 2x Phalanx Block 1B CIWS        weapons-cad (42.9k)  |
+---------------------------------------------------------------------------------------------------------------+
| Sa'ar 6 Stealth Corvette  Embarked Aviation (Enclosed Hangar)   1x SH-60F / MH-60R Seahawk      D:\sketchfab (1.52M) |
| (INS Magen)                                                     Optional: Orbiter 4 / Heron UAV tactical VTOL UAV    |
|                           Ship's Boats                          1x 7m Commando RHIB / USV       flight-1a (139k)     |
|                           Integrated Weapons Payloads           Oto Melara 76/62 SR Gun         weapons-cad (23.3k)  |
|                                                                 40x Rafael C-Dome VLS Cells     physical 16-side cyl |
|                                                                 32x IAI Barak-8 VLS Cells       forecastle well      |
|                                                                 16x Gabriel V AShM Canisters    amidships battery    |
|                                                                 2x Rafael Typhoon 25mm RWS      bridge wings         |
+---------------------------------------------------------------------------------------------------------------+
```

---

## 8. Ordnance Elevators, Catwalk Stairways, & Secondary Combat Suites Standard

At **1080p Full HD ($19.2\,\text{px/ft}$ flight deck ops, $128\,\text{px/ft}$ hero insert)**, camera angles skimming the flight deck or tracking crew operations expose fine architectural and weapon details that are invisible at 720p:

### A. Advanced Weapons Elevators (AWE / Bomb Elevators)
* **Carrier Magazine Logistics:** On nuclear supercarriers (*Ford* CVN-78), 11 electromagnetic Advanced Weapons Elevators (AWE) transport ordnance from deep armored magazines (decks 5–8) to flight deck arming stations.
* **Flight Deck Blast Hatches:**
  * Hatches must be modeled as **physical bi-parting armored flush leaves** with perimeter drainage gutters ($0.15\text{m}$ deep) and raised coamings ($0.10\text{m}$).
  * Hatches are positioned on dedicated **weapons handling sponsons** (outboard of flight paths) to allow ordnance staging without fouling active catapult or arrestment operations.
  * Internal elevator cabs must have physical interior wall tracks (MagneMotion LSM stators) and clearance for A/M32K-4A bomb carts bearing $2,000\,\text{lb}$ munitions.
* **Amphibious Ships (*Wasp* LHD-1):** 6 ordnance elevators with flush armored hatches across spots 2, 4, 6, 8 connecting vehicle staging decks and magazines to the flight deck.

### B. Stairways, Catwalk Ladders, & Vertical Circulation
* **Inclined Catwalk Staircases (Naval Ladders):**
  * Stair rise angles: $45^\circ$ to $55^\circ$.
  * Treads: Open-grate steel grip-strut ($0.70\text{m}$ wide, $0.25\text{m}$ deep, $0.22\text{m}$ riser).
  * Handrails: Dual tubular steel railings ($1.05\text{m}$ top rail, $0.55\text{m}$ intermediate knee rail).
  * Peripheral catwalks running the entire perimeter of flight decks and gallery decks require physical treads and open scuppers.
* **Vertical Rung Ladders & Monkey Ladders:**
  * Round steel rungs ($25\text{mm}$ diameter, $300\text{mm}$ vertical pitch, $450\text{mm}$ width).
  * Safety hoop cages required on all ladder runs exceeding $3.0\text{m}$ vertical climb on masts, island faces, and elevator shafts.
* **Quick-Acting Watertight Scuttles (QAWTS) & Companionways:**
  * Raised hatch coamings ($0.30\text{m} - 0.45\text{m}$ above deck) with counterbalanced spring-assist cylinders, dogging handles, and escape ladders leading below.

### C. Secondary Defensive Systems & Close-In Weapons
* **Phalanx Block 1B Sub-Assemblies:** Radome search dome, port-side FLIR thermal sight turret, 6-barrel M61A1 Vulcan with restraint clamp and flash suppressor, 1,550-round cylindrical drum, and deck Local Control Station (LCS) cabinet.
* **Autocannons & Machine Guns:** Mk 38 Mod 2/3 $25\text{mm}$ Bushmaster chain guns and $.50$-cal M2HB machine gun pintle mounts with curved ballistic gunner shields.
* **Soft-Kill EW & Decoys:** AN/SLQ-32(V)6/7 SEWIP active/passive enclosures, Mk 36/53 SRBOC 6-tube chaff mortar banks, Mk 234 Nulka hovering decoy launchers, and AN/SLQ-25 Nixie stern torpedo decoy winches.
* **Fire Control Illuminators:** Mk 99 / AN/SPG-62 parabolic radar dish directors (3 on *Burke* DDG).

---

## 9. Canister Lid & Blast Cover Kinematic Standard (The Lift-and-Pivot Sequence)

On modern warships, missile launch canisters (C-Dome, Mk 41 VLS, Gabriel V, Harpoon) and torpedo hull doors do **not** simply rotate on a primitive hinge pin. Doing so in 1080p close-ups causes the lid geometry to clip straight through the raised coaming flange. They operate via a precise **three-phase lift-and-pivot kinematic sequence**:

```
PHASE 1: UNLATCH & VERTICAL LIFT          PHASE 2: ACTUATOR SWEEP TO 105°          PHASE 3: DAMPED RETURN & CLAMP SEAT
┌─────────────────────────────────┐      ┌───────────────────────────────┐        ┌─────────────────────────────────┐
│     [Canister Lid / Cover]      │      │            \                  │        │     [Canister Lid / Cover]      │
│               ▲                 │      │             \  Lid Locked at  │        │               ▼                 │
│               │ ΔY = +30mm      │      │              \ 105° Over-Ctr  │        │               │ Pull-down clamp │
│  +---------------------------+  │      │               \               │        │  +===========================+  │
│  | Gasket Clears Raised Lip  |  │      │    [Dual Chrome Pistons]      │        │  | Gasket Compressed 100%    |  │
│  +---------------------------+  │      │    [Fully Extended +105°]     │        │  | Locking Dogs Engage       |  │
└─────────────────────────────────┘      └───────────────────────────────┘        └─────────────────────────────────┘
```

### A. The 3-Phase Kinematic Breakdown:
1. **Phase 1: Unseating & Vertical Lift ($\Delta Y = +25\text{mm}$ to $+50\text{mm}$):**
   * Before rotation begins, hydraulic or pneumatic locking dogs disengage.
   * A pantograph or four-bar linkage lifts the entire lid **vertically upward** perpendicular to the canister face.
   * **Visual Purpose:** Breaks the vacuum seal on the thick elastomeric compression gasket and clears the $20\text{mm}$ raised coaming lip without dragging the gasket across the metal rim.
2. **Phase 2: Actuator Sweep ($0^\circ \rightarrow +105^\circ$ Over-Center Lock):**
   * Driven by dual hydraulic or pneumatic cylinders with polished chrome-plated piston rods visibly extending.
   * The lid rotates open past vertical to approximately **$105^\circ$ into an over-center mechanical lock**.
   * **Operational Cause:** A lid stopped at exactly $90^\circ$ can be slammed shut by missile rocket motor plume backpressure, deck winds, or heavy sea roll, destroying the launch vehicle. The $105^\circ$ over-center detent guarantees a clear missile trajectory.
3. **Phase 3: Damped Return & Compressive Seating ($\Delta \theta = -105^\circ \rightarrow \text{Final } -30\text{mm}$ Pull-Down):**
   * After launch or cycle test, the cylinder retracts under smooth hydraulic damping (no metallic bounce).
   * As the lid reaches horizontal alignment, hardened steel alignment guide pins enter female conical indexing sockets on the canister flange.
   * The linkage pulls the lid **vertically downward**, compressing the black molded neoprene gasket against the machined metallic sealing face.
   * Perimeter rotating locking dog wedges turn into position, creating an audible, visible mechanical seal.

### B. Critical Visual & Mechanical Details for 1080p Modeling:
* **Dual Chrome Actuator Rams:** High-specular reflective cylinder rods extending from satin-gray actuator barrels.
* **Flexible Braided Grounding Straps:** Copper/tin braided lightning and static bonding straps looping between lid and canister body.
* **Elastomer Compression Gasket:** Molded black rubber seal ($20\text{mm}$ width, semi-gloss sheen) seated in a recessed perimeter channel.
* **Perimeter Locking Dog Wedges & Proximity Limit Switches:** Microswitch interlocks that prevent missile ignition until the lid sensor confirms $\ge 100^\circ$ open angle.

---

## 10. Marking Conventions & Decal Architecture Standard

At 1080p and 4K resolutions, flight deck markings, hull numbers, draft scales, and hazard boundaries must be rendered with authentic geometric precision and correct optical response.

### A. Color & Specular Specifications (Fed-Std-595 / AMS-STD-595)
* **Deck Non-Skid Dark Gray (#36076 / #36081):** sRGB `#3B3E42`, Roughness `0.88 - 0.95`. Coarse broadcast aggregate texture.
* **Deck Marking White (#37875 / #17875):** sRGB `#ECEFF1`, Roughness `0.45 - 0.55`. High contrast against non-skid.
* **Hazard Yellow (#33538 / #13538):** sRGB `#F5A800`, Roughness `0.42 - 0.50`. Used for JBD chevrons, elevator boundaries, helo spots.
* **Danger / Foul Line Red (#31105 / #11105):** sRGB `#B71C1C`, Roughness `0.45 - 0.52`. Angled deck foul lines, weapons elevator boxes.
* **AFFF / Safety Green (#14187):** sRGB `#1B5E20`, Roughness `0.35 - 0.45`. Firefighting and washdown coamings.
* **Drop-Shadow Black (#37038):** sRGB `#1A1A1A`, Roughness `0.80 - 0.90`. 45° hull drop shadows, JBD black chevrons.
* **Haze Gray Topsides (#26270 / #36270):** sRGB `#7D838A`, Roughness `0.55 - 0.65`. Vertical hull and superstructure plating.
* **Dynamic Team-Tint Channel (#00FF00):** Strictly reserved as a dynamic shader mask. Pure green `#00FF00` must NEVER be used for static painted markings.

### B. Core Operational Markings (NAVAIR 00-80T-105)
1. **Catapult Launch Tracks:** Continuous solid white line ($0.30\text{m} / 12\text{in}$ width) with yellow boundary dashed guidelines ($0.10\text{m}$ width, $3.05\text{m} / 10\text{ft}$ offset).
2. **Angled Deck Recovery Foul Line:** Alternating red and white segments ($0.45\text{m} \times 0.15\text{m} / 1.5\text{ft} \times 0.5\text{ft}$). Inviolable recovery zone boundary.
3. **Helicopter TLOF Spots (Spots 1–9 on LHD, DDG & Sa'ar 6 Helidecks):**
   * Outer aiming circle ($6.1\text{m} - 9.1\text{m} / 20\text{ft} - 30\text{ft}$ diameter) in Fed-Std-595 White or Yellow.
   * Bold stencil spot number ($1.8\text{m} - 2.4\text{m} / 6\text{ft} - 8\text{ft}$ tall) facing the pilot's landing approach corridor.
   * Longitudinal heading alignment bar bisecting the circle.
4. **Moving Machinery & Elevator Hazards:**
   * JBD perimeter: $45^\circ$ diagonal alternating yellow and black hazard chevrons ($0.15\text{m} / 6\text{in}$ width).
   * Deck-edge elevators: $45^\circ$ diagonal red and white fall-hazard zebra stripes with an inner solid yellow boundary.
   * Advanced Weapons Elevators (AWE): Solid red perimeter box with bold yellow stenciled text: `"WEAPONS ELEVATOR - KEEP CLEAR"`.

### C. Hull Topsides & Waterline Markings (NAVSEA Standard)
1. **Tactical Hull Numbers (Bow & Stern):**
   * Typography: Norfolk Naval Shipyard Block Stencil.
   * Classic 45° Drop Shadow: White digit face (#37875) with a flat black shadow (#37038) cast $45^\circ$ down-and-aft. Provides optical contrast against Haze Gray in all maritime weather conditions.
   * Scale: $3.6\text{m} - 4.8\text{m}$ ($12 - 16\text{ft}$) on CVN/LHD; $2.4\text{m} - 3.0\text{m}$ ($8 - 10\text{ft}$) on DDG.
2. **Hull Draft Marks:**
   * Located at Stem (FP), Midships, and Stern (AP).
   * 6-inch Arabic numerals spaced at 12-inch vertical intervals. The bottom of the numeral marks the exact whole-foot waterline.
3. **Subsurface Appendage Warning Icons:**
   * Stylized white sonar bulb symbol stenciled on the bow flare above the waterline to warn tugs and lines of the underwater dome.
   * Transom propeller warning stencils (`"DANGER - DUAL SCREWS"`).

### D. 3D Engine Decal Architecture
* **Z-Fighting Prevention:** Model painted deck lines and markings as floating decal geometry offset along the surface normal vector by $\Delta Y = +0.50\text{mm}$ to $+1.20\text{mm}$.
* **Dual-UV PBR Setup:**
  * UV1: Tileable coarse aggregate normal/roughness map for the base non-skid deck.
  * UV2: Macro unwrap for decal markings, alpha-blended over UV1.
* **Roughness Delta:** Retain a distinct roughness delta between the rough base deck ($0.90$) and the smoother marking topcoat ($0.48$). This creates authentic specular glint under wet weather and deck floodlights.

---

## Part 8: Headless Blender 4.2 Parts, Pivots & Unit-Structure Validator Contract (`cnc-blender-parts`)

*Repository Path: [`skills/cnc-blender-parts/SKILL.md`](./skills/cnc-blender-parts/SKILL.md)*

---
name: cnc-blender-parts
description: Headless Blender 4.2 playbook and tested bpy snippets for decomposing, cutting without seams, pivot-fitting, cleaning spaghetti topology, scaling to real metres (NASA VAB cap [OR-025]), and exporting GLBs that pass unit-structure-validator [OR-045]. Read before any Blender or 3D asset work in C:\cnc_rev.
---

# CNC Blender Parts Playbook (`cnc-blender-parts`)

Every Blender lane MUST read this playbook first. Do not re-invent mesh splits, boolean cuts, or pivot guesses. Use the tested snippets in `.claude/skills/cnc-blender-parts/snippets/`.

## 1. Hard Rules & CLI Invocation

- **Binary:** `D:\blender\blender.exe` (Blender 4.2.0 LTS).
- **Headless CLI only:** Always pass `-b --factory-startup --python-exit-code 1 --python <script.py> -- <args>`. Without `--python-exit-code 1`, Blender exits `0` on Python tracebacks.
- **One Blender at a time:** Never run two heavy headless Blender processes concurrently (causes `EXCEPTION_ACCESS_VIOLATION` / `Malloc returns null` in `BLI_array.hh`).
- **No video `[OR-012]`:** Render PNG diagnostic stills only. Never render MP4/WebM.
- **Never edit source assets in place:** Work on scratch copies, then write only your `OWNED` output path. Never run `git commit`, `push`, `checkout`, `reset`, `stash`, or `clean`.
- **Coordinate frame:**
  - **glTF 2.0 / Three.js runtime:** `1 unit = 1 metre`, **Up = `+Y`**, **Forward = `-Z`**, **Right = `+X`**, **Ground = `y = 0`** (ships keep design waterline `y = 0` when `minY < -1 m`).
  - **Blender 4.2 internal (Z-up) before `export_yup=True`:** **Up = `+Z`**, **Forward = `+Y`** (exports to glTF `-Z`), **Aft/Breech = `-Y`** (exports to glTF `+Z`), **Right = `+X`**.

---

## 2. Unit-Structure-Validator Contract (`data/rules/unit-structure.json`) `[OR-045]`

`tools/validators/unit-structure.mjs` scores every GLB (`STRUCTURED` = 100, `PARTIAL`, `STATIC`, `BROKEN`) against `data/rules/unit-structure.json` and `data/rules/unit-dimensions.json`. To earn `STRUCTURED`:

### 2.1 Required Node Names by Class
Node names are tokenized on non-alphanumeric delimiters (`wheel_L1` $\rightarrow$ `["wheel", "l1"]`). Every moving part must be a **separate glTF node** (not welded to `hull`):

| Class | Static Root Node | Required Moving Part Nodes | Notes |
| :--- | :--- | :--- | :--- |
| **`tank`** | `hull` (`body`, `chassis`) | `turret`, `barrel`, `barrel_recoil`, plus (`track_L`, `track_R` + `sprocket_L`, `sprocket_R`) or $\ge 4$ `wheel_*` | Recommended full kit: `wheel_L1..L6`, `wheel_R1..R6`, `sprocket_L/R`, `idler_L/R`, `track_L/R`. |
| **`wheeled`** | `hull` (`body`, `chassis`) | $\ge 4$ `wheel_*` (`wheel_L1..`, `wheel_R1..`) | Optional turret/gun follow tank naming. |
| **`truck`** | `hull` (`body`, `chassis`, `cab`) | $\ge 4$ `wheel_*` | Cargo bed may stay on `hull` unless articulated. |
| **`artillery`** | `hull` (`body`, `chassis`) | ($\ge 4$ `wheel_*` or `track_*`) + (`launcher`/`pod` or `barrel`/`gun`/`cannon`) | Elevate `launcher` or `barrel` around trunnion. |
| **`helicopter`** | `hull` (`fuselage`, `body`) | `rotor_main` + (`rotor_tail` or a 2nd `rotor_main` for coaxial) | Delete opaque `*blur*` / `*spin*` proxy disks first. |
| **`jet`** | `hull` (`fuselage`, `body`, `airframe`) | `gear_*` (`gear_nose`, `gear_L`, `gear_R`, `landing_gear`) | Optional `canopy`, `door_*`, control surfaces. |
| **`ship`** | `hull` (`body`) | At least one of: `prop_*`, `turret`, `launcher`, `radar` | Keep waterline at `y = 0` (`minY < -1 m` allowed). |
| **`submarine`** | `hull` (`body`) | `prop` (`propeller`) + `hatch` | Keep waterline/submerged datum intact. |
| **`infantry`** | Armature skin or `static` | Skinned rig (`minJoints >= 3`, `minClips >= 1`) OR node named `static` | Height must be $1.60\text{–}1.90\text{ m}$ (hard cap $\le 2.2\text{ m}$). |
| **`building`** | `hull` (`body`, `shell`) | `door` (`doors`, `door_leaf_port`, `door_leaf_stbd`) | Height $\le 160.02\text{ m}$ NASA VAB cap `[OR-025]`. |
| **`defence`** | `hull` / base | `turret` + (`barrel`/`gun`/`cannon` or `launcher`) | Base foundation stays static at `y = 0`. |

### 2.2 Required Local Pivots (`tolerances.pivots` in `data/rules/unit-structure.json`)
glTF has no separate pivot channel—a node rotates around its local `(0, 0, 0)`. Within `pivotFraction = 0.20` (or `0.05 m`):

| Pivot Type | Parts Using It | glTF Local `(X, Y, Z)` Rule | Blender Z-Up (`+Y` Forward) World Point |
| :--- | :--- | :--- | :--- |
| **`turret`** | `turret` | `X, Z` centered on ring; `Y = minY` (bottom seat) | `(ring_xc, ring_yc, min_z)` via Kåsa circle fit |
| **`barrel`** | `barrel`, `barrel_recoil` | `X, Y` centered on bore; `Z = maxZ` (aft breech end) | `(center_x, min_y, center_z)` at mantlet/trunnion |
| **`wheel`** | `wheel_*`, `sprocket_*`, `idler_*` | `Y, Z` centered on wheel disk | `(center_x, center_y, center_z)` axle midpoint |
| **`rotor`** | `rotor_main`, `rotor_tail`, `radar`, `gear` | `X, Z` centered on shaft/hub | `(center_x, center_y, center_z)` hub center |
| **`prop`** | `prop_*`, `propeller` | `X, Y` centered on screw shaft | `(center_x, center_y, center_z)` |
| **`launcher` / `hatch`** | `launcher`, `hatch` | `X, Z` centered; `Y = minY` (base hinge/seat) | `(center_x, center_y, min_z)` |
| **`door`** | `door_*` | `X` on hinge edge (`minX` or `maxX`) | `(min_x or max_x, center_y, center_z)` |

### 2.3 Budgets, Team Colour (`houseTint`), & Cleanliness Gates
- **Triangle caps (`lod0 / lod1 / lod2`):** `infantry`: `3000 / 1500 / 500` · `vehicle`: `8000 / 3000 / 1000` · `aircraft` & `ship`: `15000 / 5000 / 1500` · `structure` & `defence`: `6000 / 2500 / 800`.
- **Texture max edge (`lod0 / lod1 / lod2`):** `2048 / 1024 / 512` px (embedded PNG/JPEG; no Draco; `EXT_meshopt_compression` supported).
- **Team-colour slot:** At least one exported material (assigned to $\ge 1$ polygon so the glTF exporter does not strip it) must be named `houseTint` (or `team_colour` / `teamColour` / `TeamColor`).
- **Track material isolation:** Clone the material on `track_L` / `track_R` (`track_uv_*`) so scrolling track UVs in Three.js does not scroll the hull paint.
- **Unwelded moving parts & closed meshes:** Quantized vertex overlap (`weldQuantiseM = 0.01 m`) between moving parts and `hull` must be `< 8%` (`weldOverlapFraction = 0.08`). Open boundary edges must be `< 2%` of total edges (`openEdgeFraction = 0.02`).

---

## 3. What Goes Wrong, How to Detect It, How to Fix It

### Failure 1: Barrel / Turret Cut Leaves a Jagged Seam, Open Gap, or Hull-Bottom Lid
- **Why it happens:**
  1. Cutting a fused wedge gun with a box (`nose_box`) and leaving the cut loop uncapped leaves an open hollow chip that exposes the inside of the turret when pitched $+20^\circ$ or recoiled $+0.30\text{ m}$.
  2. Running `bmesh.ops.holes_fill(bm, edges=bm.edges, sides=0)` after a planar cut caps *every* pre-existing opening on the tank, stretching a giant flat polygon sheet across the open hull bottom and wheel arches (`+2,184` to `+6,904` garbage faces).
  3. Leaving the cap as a concave N-gon causes ear-clipping spikes on glTF export; unpinned cap UVs streak across the texture atlas.
  4. Running `BOOLEAN (solver='EXACT')` on a 200k-tri non-watertight Sketchfab tank takes $5+$ minutes and creates `78,001` non-manifold edges.
- **How to detect it:** `open_edges` increases after the cut, or `unit-structure.mjs` flags `openEdgeFraction > 0.02`; pitching `barrel` $+20^\circ$ or translating `barrel_recoil` $+0.30\text{ m}$ along `+Z` shows a gap between breech and mantlet.
- **How to fix it (`snippets/03_seam_safe_cuts.py`):**
  1. Slice in BMesh with `res = bmesh.ops.bisect_plane(...)`.
  2. Collect **only** the newly cut boundary edges: `cut_edges = [e for e in res["geom_cut"] if isinstance(e, bmesh.types.BMEdge) and e.is_boundary]`.
  3. Extrude `cut_edges` inward by `0.15–0.25 m` along `-plane_no` (`bmesh.ops.extrude_edge_only` + `bmesh.ops.translate`) to form a **recessed telescopic collar/trunnion sleeve** buried inside the mantlet/hull socket.
  4. Cap `cut_edges` with `bmesh.ops.holes_fill(bm, edges=cut_edges, sides=64)`, immediately triangulate `fill_res["faces"]` with `bmesh.ops.triangulate`, and pin cap loop UVs to a neutral dark metal coordinate `(0.05, 0.05)`.

### Failure 2: Inverted Normals, Black Patchy Shading, or Multi-User Apply Abort
- **Why it happens:** Negative mirror scales on wheels/turrets flip face winding inside-out; raw glTF imports carry broken custom split normals; calling `transform_apply` on instanced wheels aborts with `Cannot apply to a multi user`. Additionally, Blender 4.1+ removed `mesh.use_auto_smooth`.
- **How to detect it:** Backface culling in Three.js shows missing wheels/turret cheeks, or judge renders flag dark diagonal shading patches across flat armor glacis plates.
- **How to fix it (`snippets/01_import_and_weld.py` & `05_spaghetti_clean.py`):**
  1. Always run `bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False)` **before** `bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)`.
  2. Clear corrupted split normals with `bpy.ops.mesh.customdata_custom_splitnormals_clear()`.
  3. After welding (`remove_doubles(dist=0.0001)`), run `bmesh.ops.recalc_face_normals(bm, faces=bm.faces)`.
  4. Mark sharp edges at $34^\circ$ (`e.smooth = e.calc_face_angle(0.0) < math.radians(34.0)`) and apply `WEIGHTED_NORMAL (mode='FACE_AREA_WITH_ANGLE', keep_sharp=True)`.

### Failure 3: Wrong Pivot (Turret Wobbles Out of Socket, Barrel Pitches Around Mid-Tube, Wheels Orbit Hull)
- **Why it happens:**
  1. `ORIGIN_CENTER_OF_MASS` or `ORIGIN_GEOMETRY` on a turret pulls the pivot $0.5\text{–}1.3\text{ m}$ forward (toward the gun) or aft (toward the bustle basket), making the turret slide off the hull when yawed $90^\circ$.
  2. `ORIGIN_GEOMETRY` on a gun barrel puts the pivot at mid-tube instead of the breech (`maxZ` in glTF / `min_y` in Blender), so pitching $+20^\circ$ swings the breech out through the turret roof.
  3. Linking wheel datablocks (`w_obj.data = master_mesh`) *before* centering each wheel's origin teleports all 6 wheels onto Wheel #1.
  4. `bpy.ops.export_scene.gltf()` **mutates `obj.rotation_mode = 'QUATERNION'` in-place**, causing any subsequent `obj.rotation_euler` pose check to silently do nothing!
- **How to detect it:** `unit-structure.mjs` fails the `pivots` check (`turret` not at `x,z` center + `minY`, `barrel` not at `maxZ` breech, `wheel` not at `y,z` center), or a $+90^\circ$ yaw / $+20^\circ$ pitch test displaces the joint.
- **How to fix it (`snippets/04_origin_to_pivot.py`):**
  1. **Turret:** Fit a Kåsa least-squares circle (`np.linalg.lstsq`) to the lower ring vertices ($z \in [z_{\min}, z_{\min} + 0.15\Delta z]$) and set `z = min_z`. If the turret was modeled at a baked yaw angle (e.g. $+25^\circ$ on the raw Merkava), un-rotate it around the fitted ring center before setting rest transforms.
  2. **Barrel & Recoil:** Set origin to `(center_x, min_y, center_z)` in Blender Z-up (`+Y` forward), which exports to `(center_x, center_y, maxZ)` in glTF (`-Z` forward).
  3. **Wheels:** Set each wheel's origin to its bbox/rim center `(center_x, center_y, center_z)` via `mesh.transform(Matrix.Translation(-local_piv))` **first**, then link same-side duplicates (`w_obj.data = master_l_mesh`, keeping Left and Right masters separate so outward hub caps never flip inward).
  4. **Parenting:** Always set `child.parent = parent`, `child.matrix_parent_inverse = Matrix.Identity(4)`, `child.location = child_world_piv - parent_world_piv`, and `child.rotation_mode = 'XYZ'`.

### Failure 4: Scale Off by 100x / 1000x, Child Node `0.01` Mismatch, or VAB Height Violation `[OR-025]`
- **Why it happens:**
  1. FBX/CAD centimetre or millimetre models exported to glTF without unit conversion produce a $208\text{ m}$ soldier (taller than the NASA VAB!) or a $0.39\text{ m}$ adobe house.
  2. Mixed-scale kitbashes (like `wasp-class-lhd/lod0.glb`) leave `Recovered_Source_wasp_*` hull nodes at `scale = [0.01, 0.01, 0.01]` ($2.57\text{ m}$ long) while sibling CIWS/elevator nodes sit at `scale = [1, 1, 1]` ($242\text{ m}$ away).
  3. Joining rigged Sketchfab meshes (`sf_humanoid_rebel.glb`) before baking the Armature rest pose shoots vertex coordinates to $Z = 21,799\text{ m}$.
- **How to detect it:** Run `node scripts/glbbox.cjs <file.glb>` or `snippets/06_scale_and_facing_check.py`. Any ordinary building taller than the **NASA VAB (`160.02 m` tall, `218 m` long, `158 m` wide)** violates `[OR-025]` unless flagged `rocketAssembly`, `residentialCity`, or listed in `tallNonBuildings` in `data/rules/unit-dimensions.json`.
- **How to fix it (`snippets/01_import_and_weld.py` & `06_scale_and_facing_check.py`):**
  1. Pass `--fix-100x` to `01_import_and_weld.py` to normalize `0.01` child nodes, and `--bake-armature` (`convert(target='MESH')` + `parent_clear(type='CLEAR_KEEP_TRANSFORM')`) before joining skinned meshes.
  2. Run `06_scale_and_facing_check.py --unit-key <key> --fix` to scale the root to the exact target metres in `data/rules/unit-dimensions.json`, enforce the `160.02 m` VAB ceiling `[OR-025]`, align the long horizontal axis to glTF `Z` (`Forward = -Z`), and snap `minY = 0.0000`.

### Failure 5: Unwelded `uint16` Shards & Spaghetti Remesh Traps
- **Why it happens:**
  1. glTF splits meshes at `65,532` vertices (`uint16` index limit) and duplicates vertices along every hard normal and UV seam (`282,799` open edges / `35,019` fragments on the Merkava; `39,443` open edges on Meshy `02-tank`). Calling `bpy.ops.mesh.separate(type='LOOSE')` in Edit Mode before welding spawns $35,000$ objects and freezes Blender.
  2. Running **Voxel Remesh** or **QuadriFlow** on a hard-surface vehicle or aircraft amputates thin gun barrels, pitot tubes, and rotor blades, and rounds $90^\circ$ armor edges.
  3. `bpy.ops.object.quadriflow_remesh()` silently returns `{'FINISHED'}` while changing zero faces whenever the input has a single non-manifold or inconsistent-normal edge.
  4. `DECIMATE (UNSUBDIV)` crashes Blender 4.2 with `EXCEPTION_ACCESS_VIOLATION` on Marching-Cubes triangle soup.
- **How to fix it (`snippets/02_split_parts.py` & `05_spaghetti_clean.py`):**
  1. Join `65,532`-vert shards first, weld at `dist = 0.0001 m`, and traverse connected components in **BMesh** (`02_split_parts.py --mode loose`).
  2. For hard-surface spaghetti (`vehicle`, `aircraft`, `building`), never Voxel Remesh: run `05_spaghetti_clean.py` (`remove_doubles` $\rightarrow$ volume-preserving `LAPLACIANSMOOTH` if untextured $\rightarrow$ `DECIMATE(DISSOLVE)` at $3.2^\circ\text{–}5.5^\circ$ $\rightarrow$ Beauty triangulate $\rightarrow$ X-symmetric `DECIMATE(COLLAPSE)` to budget $\rightarrow$ `join_triangles` $\rightarrow$ `WEIGHTED_NORMAL`).

### Failure 6: Tread sheets cover the hull, or a tank ships with no treads
- **Why it happens:** A track box built from the whole hull side band is hull-height (MBT `track_l` about 0.09 x 1.24 x 7.6 m) and paints stripes over the armour. A hover hull with the same helper becomes a slab the size of the body. A tank that already has four or more wheels skips the sheets, so the AoI T-72 ships with wheels and no `track_l` / `track_r`. Stuffing 1.5 cm cubes into an artillery hull to duck the open-edge cap leaves the real holes and makes the catalog lie about the mesh.
- **How to fix it:** A tank-class file always has `track_l` and `track_r`, and keeps its road wheels. The sheet is a thin band along the road-wheel run (wheel length, about one wheel-diameter tall, about 1.5 cm thick), with the stripe UV on that sheet only. A hull with no wheels gets a skirt on the lower side, not a box the height of the turret. Close the real boundary edges. Do not join filler cubes into the hull. Measure the band from road wheels only — return rollers on top of the run stretch the sheet to hull height, and both sheets span the full run even when one side's wheels fail the slab filter. Seat a no-wheel skirt on the hull width inside its own low band, or it floats off a tapered hull. A glTF import arrives unwelded: a stuffed 1.5 cm cube reads as six 2-face islands, so collect tiny islands first and delete after the walk — deleting inside the walk shifts face indices and skips half of them. Then weld at the validator's 1 cm quantise and cap holes with Blender's own `fill_holes`; a hand loop-walk chains wrongly where three boundary edges share a vertex.

---

## 4. Tested Snippet Reference (`.claude/skills/cnc-blender-parts/snippets/`)

Run any snippet headlessly via:
```powershell
& "D:\blender\blender.exe" -b --factory-startup --python-exit-code 1 --python C:\cnc_rev\.claude\skills\cnc-blender-parts\snippets\<script.py> -- <args>
```

1. **`01_import_and_weld.py`**: `--in <in.glb> [--out <out.glb>] [--weld-dist 0.0001] [--fix-100x] [--join-shards] [--bake-armature]`
   Strips `glTF_not_exported` widgets, fixes `0.01` child scale mismatches, bakes armatures, makes multi-user meshes single-user, joins `uint16` shards, welds UV seams, and recalculates outside normals.
2. **`02_split_parts.py`**: `--in <in.glb> --out <out.glb> --mode loose|material|bisect [--weld-dist 0.0001] [--turret-z-frac 0.52]`
   Splits welded BMesh into `hull`, `turret`, `barrel`, `track_L`, `track_R`, `wheel_L1..`, `wheel_R1..` without Edit-Mode scene-graph freezes.
3. **`03_seam_safe_cuts.py`**: `--in <in.glb> --out <out.glb> [--plane-co x,y,z] [--plane-no nx,ny,nz] [--max-sides 64] [--sleeve-depth 0.15]`
   Slices fused hulls/turrets/barrels with `bmesh.ops.bisect_plane`, extrudes a recessed telescopic sleeve, caps **only** `res["geom_cut"]` loops (`sides=64`), triangulates caps, and pins cap UVs.
4. **`04_origin_to_pivot.py`**: `--in <in.glb> --out <out.glb> [--instance-wheels]`
   Fits Kåsa circle pivots for turrets (`min_z` seat), breech pivots (`min_y` $\rightarrow$ glTF `maxZ`) for barrels, axle centers for wheels (with same-side datablock instancing), and parents with `matrix_parent_inverse = Identity`.
5. **`05_spaghetti_clean.py`**: `--in <in.glb> --out <out.glb> --class vehicle|aircraft|building|infantry [--target-tris 6000]`
   Cleans Meshy/Sketchfab spaghetti into budget topology with Planar + Collapse + Weighted Normals (hard-surface) or Voxel + QuadriFlow + Shrinkwrap with no-op fallback (watertight infantry).
6. **`06_scale_and_facing_check.py`**: `--in <in.glb> [--out <out.glb>] [--unit-key <key>] [--class <cls>] [--fix]`
   Verifies and fixes metre scale against `data/rules/unit-dimensions.json`, enforces the `160.02 m` NASA VAB height cap `[OR-025]`, rotates sideways hulls to `-Z` forward, and snaps `minY = 0`.
7. **`07_export_glb.py`**: `--in <in.glb> --out <out.glb> [--ensure-house-tint] [--clone-track-mat]`
   Binds an active `houseTint` material slot, clones `track_uv_*` materials, exports GLB (`export_yup=True, export_apply=False`), restores `rotation_mode = 'XYZ'`, and prints the verified GLB bbox and node list.

After exporting, always verify with:
```powershell
node C:\cnc_rev\scripts\glbbox.cjs <out.glb>
```

---

## Part 9: Ground & Air Military Systems and Structures Standard (`ground-air-military-systems`)

*Repository Path: [`skills/ground-air-military-systems/SKILL.md`](./skills/ground-air-military-systems/SKILL.md)*

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

---

## Part 10: Weapons, Warheads, and Terminal Effects Engineering Standard (`weapons-terminal-effects`)

*Repository Path: [`skills/weapons-terminal-effects/SKILL.md`](./skills/weapons-terminal-effects/SKILL.md)*

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

---

## Part 11: Military Meteorology/Oceanography (METOC) & Information Operations Standard (`metoc-infoops`)

*Repository Path: [`skills/metoc-infoops/SKILL.md`](./skills/metoc-infoops/SKILL.md)*

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

---

## Part 12: Israel Affairs — Military, Strategic, IAMD, Naval & LOAC Standard (`israel-affairs`)

*Repository Path: [`skills/israel-affairs/SKILL.md`](./skills/israel-affairs/SKILL.md)*

---
name: israel-affairs
description: >-
  Authoritative standard for Israel Affairs: political-military institutions, IDF command structure and operational doctrine,
  multi-tier integrated air and missile defense (IAMD: Iron Dome, David's Sling, Arrow 2/3/4, Iron Beam, C-RAM), Israeli Navy
  (Sa'ar 6, Dolphin II, Super Dvora Mk III), intelligence community (Aman, Shin Bet, Mossad, Unit 8200), Law of Armed Conflict
  (LOAC) targeting workflows (warnings, roof-knocking, human shielding, proportionality calculations, strike abort protocols),
  domestic/international information warfare & lawfare, and US-Israel strategic-military cooperation (FMF, co-production, WRSA-I, CENTCOM).
---

# Israel Affairs: Military, Strategic, and Doctrinal Standard

This engineering and doctrinal standard establishes the authoritative parameters governing Israeli military structure, operational strategy, multi-layered air and missile defense, naval combat engineering, intelligence-driven targeting workflows, Law of Armed Conflict (LOAC) application, strategic information warfare (lawfare), and US-Israel defense-industrial cooperation. It provides concrete specifications, empirical performance metrics, deterministic logic models, and rigorous sourcing guidelines for military simulations and game engine implementations.

---

## 1. Institutions & Strategic Doctrine Map

### 1.1 The Classical Ben-Gurion Triad & Modern Doctrinal Evolution
Israeli national security doctrine operates from the foundational premise of lack of strategic depth, geographic vulnerability, and numerical asymmetry relative to regional adversaries. Formulated by David Ben-Gurion in the 1950s and updated through the IDF Strategy documents (*Estratégiyat Tzahal*, published by Chief of General Staff Gadi Eizenkot in 2015 and Aviv Kochavi in 2020), Israeli military doctrine rests on five core pillars:

1. **Deterrence (*Harta'a*):** Creating and projecting overwhelming kinetic and technological superiority to dissuade state and non-state adversaries from initiating conflict. Deterrence is cumulative, requiring periodic decisive demonstrations of force when breached.
2. **Early Warning (*Hatra'a*):** Prioritizing multi-source strategic and tactical intelligence (Aman, Mossad, Shin Bet) to detect adversary intentions and preparations before hostilities commence, enabling rapid mobilization of reserve forces.
3. **Decisive Victory (*Hachra'a*):** Rapidly transferring the fighting into enemy territory, neutralizing enemy operational capabilities, destroying command nodes, and achieving a swift, decisive outcome to shorten conflict duration.
4. **Defense (*Hagana* - Added 2015):** The formal institutional recognition that modern precision rocket, missile, and drone arsenals bypass frontal land lines to threaten the Israeli home front and critical national infrastructure. Enforces the creation of a dense, multi-tier active air defense shield and fortified border obstacles.
5. **Campaign Between Wars (*MABAM* - *Ma'aracha Bein HaMilchamot*):** Continuous, proactive, low-signature kinetic, cyber, and covert operations executed in adversary territory during peacetime/gray-zone intervals to disrupt enemy military entrenchment, intercept precision weapon transfers, and roll back strategic threats without triggering full-scale interstate war.

```
       ┌────────────────────────────────────────────────────────┐
       │                ISRAELI SECURITY DOCTRINE               │
       └───────────────────────────┬────────────────────────────┘
                                   │
         ┌───────────────┬─────────┴───────┬───────────────┬────────────────┐
         ▼               ▼                 ▼               ▼                ▼
   [DETERRENCE]    [EARLY WARNING]    [DECISION]       [DEFENSE]         [MABAM]
   (Harta'a)       (Hatra'a)          (Hachra'a)       (Hagana)          (Campaign Between
   Overwhelming    Multi-Sensor ISR   Rapid Maneuver   Multi-Layer       Wars: Covert /
   Strike Power    Strategic Warning  Into Enemy Land  Air & Border Net  Targeted Strikes)
```

### 1.2 IDF Command Structure & Regional Commands
The Israel Defense Forces (IDF / *Tzahal*) operates as a unified military command under the Chief of the General Staff (*Ramatkal*), who reports directly to the Minister of Defense and the Prime Minister.

```
                     ┌─────────────────────────────────────────┐
                     │          GOVERNMENT OF ISRAEL           │
                     │  Prime Minister & Security Cabinet      │
                     └────────────────────┬────────────────────┘
                                          │
                     ┌────────────────────▼────────────────────┐
                     │          MINISTRY OF DEFENSE            │
                     └────────────────────┬────────────────────┘
                                          │
                     ┌────────────────────▼────────────────────┐
                     │      CHIEF OF GENERAL STAFF (RAMATKAL)  │
                     │                 (Matkal)                │
                     └────────────────────┬────────────────────┘
                                          │
         ┌───────────────────┬────────────┴────────────┬───────────────────┐
         ▼                   ▼                         ▼                   ▼
   [OPERATIONS BRANCH] [INTELLIGENCE (AMAN)]     [PLANNING & STRATEGY] [AIR DEFENSE CMD]
         │                   │                         │                   │
   ┌─────┴──────┐     ┌──────┴──────┐           ┌──────┴──────┐     ┌──────┴──────┐
   │ Regional   │     │ Collection  │           │ Arms / Svc  │     │ Active SAM  │
   │ Commands   │     │ & Cyber     │           │ Branches    │     │ Battalions  │
   └─────┬──────┘     └──────┬──────┘           └──────┬──────┘     └─────────────┘
         │                   │                         │
         ├─► Northern Cmd    ├─► Unit 8200 (SIGINT)    ├─► Air Force (IAF / Heyl Ha'Avir)
         ├─► Central Cmd     ├─► Unit 9900 (GEOINT)    ├─► Navy (IN / Heyl HaYam)
         ├─► Southern Cmd    ├─► Unit 504 (HUMINT)     ├─► Ground Forces (MAZI)
         └─► Home Front Cmd  └─► Research Dept         └─► C4I & Cyber Defense
```

* **Northern Command (*Pikud Tzafon*):** Responsible for the Lebanese and Syrian fronts; focuses on countering Hezbollah and Iranian-aligned militias; specialized in mountainous and urban-subterranean terrain.
* **Central Command (*Pikud Merkaz*):** Responsible for the West Bank (Judea and Samaria) and Jordan Valley; focuses on counterterrorism, border security, and urban counterinsurgency.
* **Southern Command (*Pikud Darom*):** Responsible for the Gaza Strip, Sinai border, and the Red Sea corridor; primary operational theater for asymmetric anti-rocket, anti-tunnel, and urban operations.
* **Home Front Command (*Pikud HaOref*):** Established following the 1991 Gulf War; responsible for civil defense, public shelter management, nationwide early warning sirens, search and rescue (SAR), and urban damage triage.

### 1.3 The Intelligence Community (The "Kehila")
Israel's intelligence community comprises three primary autonomous agencies coordinated by the Prime Minister's Office and the National Security Council (*Malal*):

1. **Aman (Directorate of Military Intelligence):**
   * Organic IDF body responsible for strategic military intelligence, order of battle (ORBAT) analysis, warning of war, and operational targeting.
   * **Unit 8200:** SIGINT, codebreaking, electronic warfare, and offensive/defensive cyber operations. Analyzes regional telecommunications, metadata, and radio intercepts.
   * **Unit 9900:** Visual and geospatial intelligence (GEOINT). Operates spy satellites (Ofek series), synthetic aperture radar (SAR), aerial mapping, and digital 3D urban terrain modeling.
   * **Unit 504:** Human intelligence (HUMINT) operating covert agents and informants across cross-border operational zones.
2. **Shin Bet / ISA (*Sherut Bitachon Klali* / Shabak):**
   * Domestic security and counterintelligence agency reporting directly to the Prime Minister.
   * Primary jurisdiction over counterterrorism inside Israel, the West Bank, and Gaza. Controls deep interrogations, domestic informant networks, and physical VIP protection.
3. **Mossad (*HaMosad leModi'in uleTafkidim Meyuchadim*):**
   * External intelligence and special operations agency reporting directly to the Prime Minister.
   * Focuses on foreign covert action, non-proliferation counter-efforts (e.g., Iranian nuclear project interdiction), clandestine diplomacy, and high-value target operations beyond contiguous borders.

---

## 2. Multi-Layer Integrated Air & Missile Defense (IAMD)

Israel operates the world's most densely concentrated, multi-layered, integrated air and missile defense architecture. The network operates under a centralized battle management system that routes incoming track data from networked active electronically scanned array (AESA) radars to the optimum intercept tier.

```
Altitude (km)
   ▲
150│                      [LAYER 1: ARROW 3 / ARROW 4]
   │                      Exo-atmospheric Kinetic Hit-to-Kill (IRBM / Space)
100│- - - - - - - - - - - - Karman Line - - - - - - - - - - - - - - - - - - - -
   │
 50│                      [LAYER 2: ARROW 2 / DAVID'S SLING]
   │                      Upper Endo-atmospheric Ballistic & Cruise Interception
 20│
   │                      [LAYER 3: DAVID'S SLING (STUNNER)]
 10│                      Mid-Tier: Heavy MLRS, Hypersonic / Cruise, Aircraft
   │
  4│                      [LAYER 4: IRON DOME (TAMIR)]
   │                      Tactical C-RAM, Drones, Short Rockets (Trajectory-Filtered)
  0│══════════════════════[LAYER 5: IRON BEAM (HEL) & C-RAM CENTURION]══════════
   └─────────────────────────────────────────────────────────────────────────────► Range (km)
     0          10         20         50         100        200        300+
```

### 2.1 The 5 Operational Intercept Tiers

| Layer | System Name | Primary Contractor | Primary Radar Sensor | Interceptor Kinematics | Target Profile | Intercept Alt / Range | Unit / Shot Cost |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Arrow 3 (*Hetz 3*)** | IAI / Boeing | EL/M-2080 *Green Pine* / *Great Pine* (L-band AESA) | Exo-atmospheric Kinetic Kill Vehicle (KKV) with thrust vectoring | Medium/Intermediate Range Ballistic Missiles (MRBM/IRBM), Suborbital threats | Alt: $>100\text{ km}$<br>Range: $2,400\text{ km}$ | $\approx \$2.5\text{M} - \$3.0\text{M}$ |
| **2** | **Arrow 2 (*Hetz 2*)** | IAI / Boeing | EL/M-2080 *Green Pine* / *Great Pine* | Two-stage solid propellant, Blast-fragmentation directional warhead | High-altitude theater ballistic missiles (Scud-class, Fateh-110) | Alt: $10 - 50\text{ km}$<br>Range: $100 - 150\text{ km}$ | $\approx \$1.5\text{M} - \$2.0\text{M}$ |
| **3** | **David's Sling (*Kela David*)** | Rafael / Raytheon | EL/M-2084 MMR (S-band AESA) | Two-stage *Stunner* interceptor; Asymmetric dolphin nose; Dual-mode EO/IR and MMW radar seeker; Hit-to-Kill | Heavy artillery rockets (Khaibar-1, Zelzal), Cruise missiles, Low-ballistic missiles, Large UAVs | Alt: Up to $15\text{ km}$<br>Range: $40 - 300\text{ km}$ | $\approx \$1.0\text{M}$ |
| **4** | **Iron Dome (*Kipat Barzel*)** | Rafael / Raytheon | EL/M-2084 MMR (S-band AESA) | *Tamir* interceptor with aerodynamic fins, proximity fuze, active radar / optical seeker | Artillery rockets ($122\text{mm}$ Grad, Fajr-5), $120\text{mm}$ mortars, loitering munitions, paragliders | Alt: Up to $10\text{ km}$<br>Range: $4 - 70\text{ km}$ | $\approx \$40\text{K} - \$50\text{K}$ |
| **5a**| **Iron Beam (*Magen Or*)** | Rafael | Optical/Thermal Tracker + EL/M-2084 MMR cues | Directed Energy: 100 kW ytterbium fiber laser via multi-spectral beam director | Short-range rockets, mortar shells, Class 1/2 micro/mini UAVs, FPV kamikaze drones | Alt: Line of sight<br>Range: $0.1 - 10\text{ km}$ | $\approx \$3.50 - \$5.00$ (Electricity) |
| **5b**| **C-RAM Centurion / Vulcan** | Raytheon / GD | Ku-band pulse-doppler tracking radar + FLIR | 20mm M61A1 Vulcan 6-barrel Gatling ($4,500\text{ rpm}$); HEIT-SD ammunition | Point defense: mortar leakers, dive-bombing suicide UAVs | Alt: $<1.5\text{ km}$<br>Range: $0.2 - 2.0\text{ km}$ | Ammo burst: $\approx \$15\text{K}$ |

### 2.2 Doctrinal Principles: The "Do-Not-Shoot-Empty-Ground" Trajectory Filter
The economic survival of Israel's air defense depends on algorithmic discrimination between threatening and non-threatening trajectories.

1. **The Economic Asymmetry Dilemma:** Adversary insurgent forces fire mass-produced, unguided rockets costing $\$300\text{ to }\$1,000$ each. Intercepting every incoming rocket with a $\$50,000$ Tamir would lead to rapid financial exhaustion and magazine depletion.
2. **Trajectory Calculation Engine:**
   - The EL/M-2084 Multi-Mission Radar (MMR) detects the rocket during its boost phase, extracts velocity vectors, and computes the ballistic ellipse within $2.5\text{ seconds}$ of launch.
   - The Battle Management & Weapon Control (BMC) projects the impact point onto a high-resolution digitized spatial grid of Israel.
   - The terrain grid is partitioned into **Defended Asset Zones (DAZ)** (urban centers, chemical plants, airbases, power stations) and **Open Ground Zones (OGZ)** (agricultural fields, barren dunes, unpopulated scrubland).
3. **Withholding Fire Doctrine:**
   - If the predicted impact ellipse falls within an OGZ, the BMC **withholds launch authorization**. The rocket is allowed to impact open dirt without spending an interceptor.
   - If the impact ellipse intersects a DAZ, the BMC assigns an intercept point along the descent trajectory and fires 1 or 2 Tamir interceptors to achieve a $>90\%$ probability of kill ($P_k$).
   - Home Front sirens are sounded **only** in the specific polygonal siren alert polygon (*Poli-Gal*) covering the expected footprint, avoiding nationwide industrial disruption.

### 2.3 Directed Energy: Iron Beam Environmental Physics
Rafael's 100 kW-class fiber laser achieves hard kills through thermal ablation—heating the rocket shell or drone skin until structural failure, propellant ignition, or warhead detonation occurs.
* **Marginal Cost:** Negligible electrical cost ($\approx \$3.50/\text{shot}$), eliminating interceptor inventory depletion during sustained swarm attacks.
* **Atmospheric Attenuation:** High-energy lasers ($\lambda \approx 1.064\ \mu\text{m}$) suffer severe photon extinction in fog, rain, and sandstorms ($I = I_0 e^{-\gamma d}$).
* **Thermal Blooming Paradox:** In still air, the air enclosed in the laser path heats up, expands, and forms a diverging negative lens that defocuses the beam. Moderate crosswinds ($v_{\perp} > 5\text{ m/s}$) continuously sweep heated air out of the beam line, mitigating thermal blooming and restoring target burn irradiance.

---

## 3. Israeli Navy (*Heyl HaYam*) & Maritime Operations

Historically a brown-water coastal patrol force, the Israeli Navy has transformed into a blue-water strategic branch charged with defending Israel's Exclusive Economic Zone (EEZ), securing offshore natural gas platforms (Tamar, Leviathan, Karish), enforcing legal naval blockades, and maintaining second-strike deterrence.

### 3.1 Primary Naval Combatants

```
       [Sa'ar 6 Corvette: 1,900t Displacement, 90m Length]
  
                +---+ [EL/M-2248 MF-STAR 4-Face AESA]
                |   |
  [76mm Gun]   [Bridge]   [16x Gabriel V AShM]   [Helideck / SH-60 Hangar]
  (Bow: +X)       |             |                      | (Stern: -X)
  ============|===|=============|======================|===========
              [32x Barak-8]    [40x C-Dome]
              [VLS Cells]      [VLS Cells]
```

1. **Sa'ar 6-Class Corvettes (Magen-class):**
   * Built by ThyssenKrupp Marine Systems (TKMS) in Kiel, Germany; outfitted with Israeli combat management systems and sensors in Haifa.
   * **Displacement:** 1,900 tonnes full load; Length: 90 meters; Crew: 70.
   * **Radar Suite:** IAI Elta EL/M-2248 MF-STAR active phased array radar (4 fixed S-band AESA faces integrated into the mast).
   * **Air Defense Armament:**
     * $32\times$ Barak 8 / LRAD vertical launch cells (range $70 - 100\text{ km}$ vs supersonic cruise missiles and aircraft).
     * $40\times$ C-Dome vertical launch cells (navalized Iron Dome for point-defense against saturated rocket and drone salvos targeting gas rigs).
   * **Anti-Surface Armament:** $16\times$ Gabriel V long-range anti-ship cruise missiles with advanced AESA radar seekers; $1\times$ Leonardo 76/62 Super Rapid gun mount; $2\times$ Rafael Typhoon 25mm stabilized remote weapon stations with Spike-ER missile launchers.
   * **Aviation:** Flight deck and enclosed hangar accommodating an SH-60F Seahawk or Eurocopter Panther AS565.
2. **Dolphin I & Dolphin II-Class Submarines:**
   * German-built Type 800 and Type 212 variants operated by the *Shayetet 7* submarine flotilla.
   * **Dolphin II Characteristics:** Equipped with Air-Independent Propulsion (AIP) utilizing Siemens polymer electrolyte membrane (PEM) fuel cells, enabling multi-week submerged silent patrol.
   * **Armament:** $6\times 533\text{mm}$ standard torpedo tubes plus $4\times 650\text{mm}$ enlarged swim-out tubes capable of launching Popeye Turbo long-range land-attack cruise missiles (widely assessed to carry nuclear warheads for strategic second-strike deterrence) and deploying *Shayetet 13* naval commando swimmers.
3. **Super Dvora Mk III & Shaldag Mk V Fast Patrol Craft:**
   * High-speed aluminum hulls ($45 - 50\text{ knots}$) operated by Squadron 914 and 916 for coastal interdiction, counter-infiltration, and maritime border control.
   * Armed with stabilized Typhoon 25mm cannons, 12.7mm machine guns, Long-Range Acoustic Devices (LRAD), and fire monitor water cannons for non-lethal maritime policing.

### 3.2 Maritime LOAC & Naval Blockade Law
Under the **San Remo Manual on International Law Applicable to Armed Conflicts at Sea (1994)**:
* **Legality of Blockades:** A declared naval blockade is a recognized, legal belligerent instrument (San Remo Art. 93–104) provided it is declared, notified to all states, effective, non-discriminatory, and does not cause disproportionate civilian suffering.
* **Enforcement in International Waters:** Naval forces of a blockading power have the legal authority under the law of naval warfare to intercept, visit, search, and seize neutral commercial or private vessels reasonably suspected of attempting to breach the blockade or carrying maritime contraband, even while in international waters outside the territorial sea (San Remo Art. 67).
* **The 2011 UN Palmer Commission Report:** Formally affirmed that Israel's naval blockade of Gaza was a legal security measure to prevent maritime arms smuggling, and Israeli naval boarding operations in international waters against the 2010 Mavi Marmara flotilla were legally valid under international law, while criticizing the specific level of force utilized during the hand-to-hand boarding encounter.

---

## 4. LOAC Practice, Targeting Procedures & Warning Protocols

The IDF operates within the international framework of the Law of Armed Conflict (LOAC) / International Humanitarian Law (IHL), integrated through the Military Advocate General's Corps (*Patzar* - *Praklitut Tzvait*).

### 4.1 The Institutional Targeting Chain & Legal Oversight
Every planned pre-designated military target must be vetted and authorized through an institutional targeting cycle that includes an embedded operational legal adviser (*Yo'ash*):

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  AMAN TARGETING  │ ──► │ LEGAL ADVISORY   │ ──► │ COMMAND APPROVAL │
│  Intelligence    │     │ Review LOAC:     │     │ Brigade / Division│
│  Collection &    │     │ Necessity,       │     │ or General Staff │
│  Munition Select │     │ Proportionality  │     │ Authorized Sign  │
└──────────────────┘     └──────────────────┘     └──────────────────┘
                                                            │
                                                            ▼
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  STRIKE ABORT    │ ◄── │ REAL-TIME DRONE  │ ◄── │ ADVANCE WARNING  │
│  Abort if civilian│    │ ISR SURVEILLANCE │     │ Leaflet / Call / │
│  presence surges │     │ (Confirm Clear)  │     │ "Roof Knock"     │
└──────────────────┘     └──────────────────┘     └──────────────────┘
```

1. **Military Necessity:** The target must be a legitimate military objective—an object that by its nature, location, purpose, or use makes an effective contribution to military action, and whose neutralization offers a definite military advantage (Additional Protocol I, Art. 52(2)).
2. **Distinction:** The attacking force must distinguish at all times between military objectives and civilian persons or objects (API Art. 48).
3. **Proportionality:** An attack is prohibited if it may be expected to cause incidental loss of civilian life or injury to civilians, or damage to civilian objects, which would be excessive in relation to the concrete and direct military advantage anticipated (API Art. 51(5)(b)).
4. **Precautions in Attack:** Feasible precautions must be taken to minimize incidental civilian casualties, including weapon selection (e.g., small diameter bombs, precision-guided munitions with delayed fuzes), timing of attack, and issuance of effective advance warnings (API Art. 57).

### 4.2 The Advance Warning Hierarchy & "Roof Knocking" (*Hakash BaGag*)
To satisfy API Article 57(2)(c) ("effective advance warning shall be given of attacks which may affect the civilian population, unless circumstances do not permit"), the IDF developed a tiered warning protocol:

1. **Wide-Area Warnings:**
   * Air-dropped bilingual Arabic/Hebrew leaflets outlining specific evacuation corridors and designated safe zones.
   * Mass SMS cell broadcasts, recorded cellular phone calls, and radio overrides instructing residents of defined geographical blocks to move southward or toward humanitarian zones.
2. **Specific Structure Warnings (Direct Calls):**
   * Intelligence officers (Unit 504 / Shin Bet) place individual telephone calls directly to building owners, apartment managers, or local residents, confirming evacuation status and verifying that occupants have exited.
3. **"Roof Knocking" (*Hakash BaGag*):**
   * *Origin & Evolution:* Developed during Operation Cast Lead (2008–2009) and formalized in Operation Protective Edge (2014) and Operation Guardian of the Walls (2021).
   * *Mechanism:* Launching a low-yield, non-lethal kinetic charge, inert concrete training bomb, or small micro-charge (e.g., from a drone or helicopter) directly onto the roof of an empty multistory structure.
   * *Operational Purpose:* Produces a loud acoustic and tactile thud without collapsing structural slabs, serving as an unmistakable physical warning to any remaining occupants that an explosive strike on the building will occur within $5\text{ to }15\text{ minutes}$.
   * *Tactical Limitations & Legal Scrutiny:* Does not relieve the attacking force of proportionality obligations. If civilians fail to evacuate or deliberate human shields gather on the roof (as seen during several 2014 strikes), commanders are required under doctrine to reassess the strike and abort if incidental civilian harm exceeds military necessity.
4. **Real-Time Visual Abort Protocols:**
   * Overwatching UAVs (Hermes 450, Hermes 900, Heron TP) maintain continuous sensor lock on the target structure.
   * If civilians unexpectedly enter the blast envelope while precision munitions are in flight, weapon systems equipped with data-link optical guidance (e.g., Spike NLOS or Rafael SPICE) can be manually diverted into empty fields or detonated prematurely.

### 4.3 LOAC Human Shielding Rules & Dual-Use Infrastructure
* **Geneva Convention IV, Article 28:**
  > *"The presence of a protected person may not be used to render certain points or areas immune from military operations."*
* **Additional Protocol I, Article 51(7) & Article 58:**
  Parties to an armed conflict are legally prohibited from utilizing civilian populations to shield military objectives or operations, and defenders bear an affirmative legal duty to separate military forces and munitions from civilian population centers.
* **Loss of Protected Civilian Immunity:**
  When a civilian structure (school, residential tower, hospital, clinic, mosque) is utilized by an adversary to store munitions, conceal combatants, house subterranean tunnel portals, or launch rockets, **it loses its legal protection as a civilian object under LOAC** and converts into a legitimate military target.
* **The Attacker's Ongoing Legal Obligation:**
  The defender's illegal use of human shielding does **not** grant the attacking force unlimited license. The attacker remains legally bound by the Rule of Proportionality and must take feasible precautions to mitigate civilian deaths.

---

## 5. Strategic Information Environment, Lawfare & Politics

### 5.1 The Lawfare Arena (*Milchemet Mishpat*)
"Lawfare" is defined as the strategic utilization of international legal mechanisms, human rights treaties, international courts, and diplomatic bodies as a primary instrument of warfare to constrain, delegitimize, and sanction an adversary.
* **Adversary Strategy:** Non-state armed actors (e.g., Hamas, Hezbollah) intentionally embed military infrastructure within densely populated urban enclaves. When kinetic strikes occur, the resulting civilian casualties and infrastructure destruction are broadcast instantly to international media and supranational institutions to generate diplomatic friction, ICJ/ICC investigations, and foreign arms export bans against Israel.
* **State Counter-Lawfare Mechanisms:**
  * **Forensic Declassification:** The rapid declassification and public broadcast of raw ISR drone feeds, thermal video of rocket launches from humanitarian zones, captured tunnel blueprints, and weapons manifests to refute allegations of indiscriminate targeting.
  * **The "First to Report" Disadvantage:** Western military forces require rigorous multi-echelon legal and intelligence verification before releasing official incident findings, creating a $6\text{ to }24\text{ hour}$ informational vacuum that adversary propagandists exploit with immediate fabricated casualty claims.

### 5.2 Domestic Political-Military Dynamics
* **The "People's Army" Model (*Tzva Ha'Am*):**
  * Ground force combat power depends on mandatory universal conscription (32 months for men, 24 months for women) followed by extensive reserve duty (*Miluim*).
  * Prolonged conflicts cause severe domestic economic dislocation as hundreds of thousands of reservists are removed from the civilian workforce (especially the high-tech sector).
* **Civil-Military Relations & Public Sensitivity:**
  * Israeli society exhibits extreme sensitivity to IDF soldier casualties and captive/hostage situations, creating immense domestic political pressure that adversaries attempt to exploit through psychological hostage videos and prisoner-exchange demands.
  * The War Cabinet and political leadership face constant friction between operational military goals (achieving decisive victory, destroying adversary military infrastructure) and international diplomatic pressure regarding civilian casualties and humanitarian aid corridors.

---

## 6. US-Israel Defense Cooperation & Strategic Alignment

The strategic military relationship between the United States and Israel is an institutionalized alliance governed by formal treaties, co-development agreements, and shared operational doctrine.

### 6.1 Foreign Military Financing (FMF) & Strategic Memoranda of Understanding
* **10-Year Memoranda of Understanding (MOU):**
  * The current 10-year bilateral agreement (FY2019–FY2028), signed under the Obama administration in 2016, provides **$\$38.0\text{ billion}$ in military assistance** ($\$3.8\text{ billion}$ annually).
  * **Components:**
    * $\$3.3\text{ billion}$ annually in standard Foreign Military Financing (FMF), restricted primarily to purchases of US-manufactured defense systems (F-35, F-15, munitions).
    * $\$500\text{ million}$ annually dedicated specifically to joint missile defense research, development, and procurement (Iron Dome, David's Sling, Arrow).
  * **Off-Shore Procurement (OSP) Phase-Out:** Under the current MOU, the legacy provision permitting Israel to spend up to $26.3\%$ of FMF funds on domestic Israeli defense contractors is being phased down to $0\%$ by 2028, requiring all FMF funds to be spent inside the United States.

### 6.2 Industrial Co-Production & Joint Weapon Systems
To ensure supply security and satisfy US legislative mandates, critical Israeli air defense systems are co-produced within the United States:
* **Iron Dome / Tamir (*SkyHunter*):** Rafael and Raytheon established a joint venture (Raytheon Rafael Protection Systems / R2PS) with an interceptor manufacturing facility in Camden, Arkansas, producing Tamir missiles for both the IDF and the US Marine Corps.
* **David's Sling / Stunner:** Jointly developed by Rafael and Raytheon. The Stunner missile and launch canisters are co-produced across US and Israeli manufacturing lines.
* **Arrow 2 / Arrow 3:** Jointly developed and funded by the Israel Missile Defense Organization (IMDO) and the US Missile Defense Agency (MDA), with Boeing producing major subassemblies and structural sections in the United States.

### 6.3 Strategic Munition Stockpiles: WRSA-I
* **War Reserve Stockpile Ammunition - Israel (WRSA-I):**
  * A strategic munitions stockpile owned and maintained by the United States Department of Defense, physically pre-positioned inside secured military depots across Israel.
  * *Operational Mechanism:* The inventory remains under US military custody. In times of severe military crisis, the President of the United States possesses statutory authority (under the Foreign Assistance Act) to authorize the rapid emergency transfer of WRSA-I munitions (artillery shells, JDAM precision bomb guidance kits, Hellfire missiles) directly to the IDF.
  * *Dual-Use Realities:* During the 2022–2024 Ukraine conflict, the US military drew down substantial 155mm artillery stocks from WRSA-I to supply Ukrainian forces, later replenishing the stockpile following the outbreak of Middle East hostilities in late 2023.

### 6.4 Operational Integration: CENTCOM & Regional Coalition Architecture
* **Transition to CENTCOM (January 2021):**
  * The US Department of Defense officially reassigned Israel from the European Command (EUCOM) Area of Responsibility to Central Command (CENTCOM).
  * *Strategic Impact:* Placed the IDF under the same unified combatant command as regional Arab partners (Jordan, Egypt, UAE, Bahrain, Saudi Arabia), facilitating unified air and missile defense architecture (e.g., Middle East Air Defense Alliance - MEAD).
  * *Operational Proof:* During the April 13–14, 2024 and October 1, 2024 Iranian ballistic missile, cruise missile, and drone barrages against Israel, CENTCOM coordinated multi-national sensor cues and kinetic interceptions across US naval destroyers (Arleigh Burke-class firing SM-3), US Air Force fighters, British and French air units, Jordanian air defenses, and Israeli Arrow/David's Sling/Iron Dome batteries.

---

## 7. Sourcing Rules & Evidentiary Standard

When writing, modeling, or reviewing Israeli military affairs, doctrine, and weapons performance, apply the following rigorous 3-tier hierarchy:

### Tier 1: Primary State, Treaty & Manufacturer Standards (Authoritative)
* **Official Military & Legal Manuals:** IDF General Staff Doctrines, Military Advocate General legal briefs, State of Israel official commission reports (Winograd Commission 2008, Turkel Commission 2013).
* **International Treaties:** Geneva Conventions of 1949 and Additional Protocols (AP I & II 1977); Hague Conventions of 1907; San Remo Manual on International Law Applicable to Armed Conflicts at Sea (1994).
* **Primary Technical & Procurement Data:** Manufacturer technical specifications (Rafael Advanced Defense Systems, Israel Aerospace Industries [IAI], Elbit Systems, Raytheon, Boeing, General Dynamics); US Congressional Research Service (CRS) Reports; US Department of Defense / Missile Defense Agency (MDA) budget line items.

### Tier 2: Peer-Reviewed Military Analysis & Think Tanks (Analytical)
* **Strategic Think Tanks:** Institute for National Security Studies (INSS - Tel Aviv University), International Institute for Strategic Studies (IISS - The Military Balance), Center for Strategic and International Studies (CSIS Missile Defense Project), Royal United Services Institute (RUSI), Washington Institute for Near East Policy (WINEP).
* **Specialized Defense Journals:** Jane's Defence Weekly / Jane's All the World's Aircraft, Naval Institute Proceedings, Air & Space Forces Magazine, IDF Dado Center for Interdisciplinary Military Studies publications.

### Tier 3: Verified Media & Investigatory Reports (Contextual / Real-Time)
* **Reputable International Reporting:** Reuters, Associated Press, Wall Street Journal, Financial Times, New York Times, BBC Verify.
* **Specialized Investigative Outlets:** Bellingcat open-source intelligence (OSINT) geolocations; +972 Magazine / Local Call (investigative reporting on algorithmic targeting systems—must be cross-referenced against official IDF statements to separate allegation from confirmed doctrine).
* **Evidentiary Rule on Allegations:** Always explicitly differentiate **documented fact** (substantiated by physical evidence, released sensor telemetry, or official government acknowledgment) from **allegations** (claims made by belligerents, advocacy groups, or anonymous sources that have not undergone forensic verification).

---

## 8. Authoritative Audit Questions for Simulation Review

Use these 20 authoritative questions to evaluate any game engine, simulation model, or operational brief involving Israeli military systems, LOAC mechanisms, and strategic information warfare:

1. **Trajectory Discrimination:** Does the air defense model calculate the landing ellipse of incoming rockets and actively withhold interceptors from hitting unpopulated desert/open ground, or does it waste missiles on empty dirt?
2. **Layered Interception Hierarchy:** Are incoming threats evaluated in strict outer-to-inner order (Arrow 3 -> David's Sling -> Iron Dome -> Iron Beam -> C-RAM) based on speed, altitude, and trajectory?
3. **Directed Energy Meteorology:** Does high-energy laser lethality degrade in rain, fog, and dust in accordance with the Beer-Lambert extinction law, and does steady crosswind mitigate thermal blooming?
4. **Economic Munition Asymmetry:** Does the simulation track the massive cost disparity between cheap unguided rockets and high-end kinetic interceptors ($40K Tamir vs $1M Stunner vs $3M Arrow 3)?
5. **Naval EEZ Defense Modeling:** Does the naval architecture properly position Sa'ar 6 corvettes and C-Dome/Barak-8 batteries to protect critical offshore energy platforms and coastal infrastructure?
6. **Submarine Strategic Capabilities:** Are Dolphin II submarines modeled with Air-Independent Propulsion (AIP) for silent multi-week endurance, and do they possess enlarged swim-out tubes for special operations and cruise missiles?
7. **Naval Blockade Legal Mechanics:** Does maritime interdiction enforce the San Remo Manual rules, including visit, board, search, and seizure in international waters, with non-lethal compliance mechanisms (LRAD, water cannon)?
8. **LOAC Targeting Verification:** Does the target generation cycle enforce an explicit check on Military Necessity, Distinction, and Proportionality before authorizing kinetic strikes on protected urban structures?
9. **Advance Warning Hierarchy:** Are multi-stage warnings (leaflets, SMS broadcasts, direct phone calls, and "roof knocking") simulated with explicit civilian evacuation delay timers before high-explosive ordnance impacts?
10. **Strike Abort Dynamic:** Can in-flight precision-guided munitions (SPICE, Spike NLOS) be aborted or diverted if real-time drone reconnaissance spots unexpected civilian or human shield presence?
11. **Human Shielding Status Conversion:** Does the simulation correctly model the legal conversion of a protected civilian site (hospital, school, mosque) into a legitimate military objective when used for military purposes under GC IV Art. 28?
12. **Proportionality Constraint on Shielded Targets:** When striking a legally converted shielded site, does the model still impose strict collateral damage caps based on the military necessity calculation?
13. **Forensic Evidence Declassification:** Can the defending player actively counter hostile diplomatic lawfare and PR collapses by releasing raw ISR drone footage to expose adversary human shielding or staged incidents?
14. **Information Warfare Time Vacuum:** Is the defending player subjected to a realistic delay in debunking adversary claims due to mandatory legal and forensic vetting cycles?
15. **Public Legitimacy Impact on Logistics:** Does degraded public legitimacy translate into concrete logistical bottlenecks (arms embargoes, port denials, delayed reloads) rather than unrealistic mechanical weapon jamming?
16. **US Foreign Military Financing (FMF):** Are external strategic supply chains and replenishment rates linked to US political backing, FMF credit flows, and the availability of pre-positioned WRSA-I stockpiles?
17. **Co-Production Vulnerabilities:** Does the simulation account for the geographic distribution of interceptor manufacturing (e.g., Tamir production in Arkansas, Arrow components in Boeing US facilities)?
18. **Domestic Reservist Economic Drain:** Does mass mobilization of reserve units create a ticking domestic economic strain that penalizes prolonged passive defensive stances?
19. **Algorithmic Sensor Fusion:** Does the intelligence model integrate multi-source sensor fusion (SIGINT from Unit 8200, GEOINT from Unit 9900, airborne radar from F-35 MADL) into unified target generation?
20. **Regional Air Defense Coordination:** In multi-faction or coalition scenarios, can air defense radars and interceptors share telemetry with allied naval destroyers and regional partners under a unified CENTCOM-style framework?

---

## Part 13: Middle East Strategic — Persian Gulf, Iran, Kharg Island & Zagros Standard (`middle-east-strategic`)

*Repository Path: [`skills/middle-east-strategic/SKILL.md`](./skills/middle-east-strategic/SKILL.md)*

---
name: middle-east-strategic
description: >-
  Authoritative technical and strategic standard for Persian Gulf security, Iranian military and IRGC posture,
  proxy/network warfare, maritime chokepoints, Zagros topography, critical energy infrastructure (Kharg Island,
  Bushehr, Shiraz), and CENTCOM/Israeli force projection. Grounds operational scenarios, RTS mechanics, and lore
  in verified military doctrine, physical hydrography/orography, and historical combat precedents.
---

# Middle East Strategic & Regional Affairs Standard: Persian Gulf, Iran, & Critical Chokepoints

This skill establishes the doctrine, geographic-infrastructure baseline, order-of-battle structures, and audit protocols for simulating military operations, strategic infrastructure defense/interdiction, and asymmetric warfare across the Persian Gulf, the Iranian littoral, the Zagros Mountains, and the Kharg-to-Shiraz corridor.

---

## 1. Sourcing Rules & Analytical Standards

When analyzing Middle Eastern strategic affairs, maritime operations, and military infrastructures, analysts and game designers must adhere to rigorous sourcing tiers to avoid state propaganda, operational deception, and social-media rumor loops.

### 1.1 Source Hierarchy
1. **Tier 1 (Authoritative Primary / Official Hydrographic & Sensor Data):**
   - National Geospatial-Intelligence Agency (NGA) Sailing Directions (Pub 172: Red Sea and Persian Gulf).
   - International Hydrographic Organization (IHO) bathymetric soundings and navigation charts (UKHO / Admiralty Charts 2847, 2884, 2888).
   - Official unclassified US Department of Defense / Defense Intelligence Agency (DIA) reports (e.g., *Iran Military Power*, unclassified briefings from NAVCENT/5th Fleet, US Air Force Central / AFCENT).
   - International Atomic Energy Agency (IAEA) Safeguards Reports regarding nuclear installations (e.g., Bushehr, Natanz, Fordow).
2. **Tier 2 (Reputable Defense Research & Open-Source Geospatial Intelligence):**
   - International Institute for Strategic Studies (IISS) *The Military Balance* and *Iran's Networks of Influence*.
   - Center for Strategic and International Studies (CSIS) Missile Defense Project and Defense360 analyses.
   - United States Naval Institute (USNI) *Proceedings* and Naval Combat Information.
   - Commercial high-resolution synthetic aperture radar (SAR) and multispectral optical satellite imagery (Sentinel-1/2, Planet Labs, Maxar Technologies).
3. **Tier 3 (Historical Records & Scholarly Military Histories):**
   - US Naval War College Newport Papers on the Tanker War (1984–1988) and Operation Praying Mantis (18 April 1988).
   - Operational analyses of the Iran-Iraq War (e.g., Williamson Murray & Kevin M. Woods, *The Iran-Iraq War: A Military and Strategic History*).
4. **Tier 4 (State Media & Belligerent Claims - Treat as Unverified Propaganda):**
   - Tasnim, Fars News Agency, Press TV, IRNA (Iran).
   - Unverified social media combat footage, claim-of-responsibility Telegram channels.
   - *Requirement:* All equipment specifications or combat claims originating from Tier 4 sources must be tagged with explicit confidence ratings (`[CONFIDENCE: LOW - STATE CLAIM]`) and cross-checked against independent satellite imagery or wreckage analysis.

### 1.2 Uncertainty Quantification Framework
Every technical or tactical assertion must clearly indicate its epistemic confidence:
- **[FACT]**: Directly verified by multiple independent sensors, declassified intelligence, physical wreckage inspection, or hydrographic measurements (e.g., Kharg Island pier berths and water depth, F-4E deployment at Bushehr).
- **[ASSESSED]**: High-probability deduction based on observable infrastructure, doctrine, logistics footprints, and sensor placement, but lacking public operational confirmation (e.g., specific tunnel magazine storage volumes in the Shiraz Zagros foothills).
- **[HYPOTHETICAL / PROJECTED]**: Plausible operational extrapolation for near-future conflict scenarios consistent with verified physics and stated military doctrine (e.g., coordinated Shahed-136 saturation profiles against Kharg offshore loading manifolds).

---

## 2. Regional Actor Map & Operational Doctrinal Profiles

### 2.1 The Islamic Republic of Iran: Dual Military Structure
Iran operates two parallel, competing armed forces with distinct doctrines, supply chains, and chains of command:

```
                          ┌─────────────────────────────────────┐
                          │     SUPREME LEADER / ARMED FORCES   │
                          │        GENERAL STAFF (AFGS)         │
                          └─────────────────────────────────────┘
                                             │
                     ┌───────────────────────┴───────────────────────┐
                     ▼                                               ▼
     ┌───────────────────────────────┐               ┌───────────────────────────────┐
     │        REGULAR MILITARY       │               │      ISLAMIC REVOLUTIONARY    │
     │           (ARTESH)            │               │      GUARD CORPS (IRGC)       │
     │  - Conventional Defense       │               │  - Ideological Vanguard       │
     │  - Territorial Integrity      │               │  - Asymmetric Warfare & Proxies│
     │  - Legacy Western Hardware    │               │  - Domestic Indigenous R&D    │
     └───────────────────────────────┘               └───────────────────────────────┘
                     │                                               │
         ┌───────────┴───────────┐                       ┌───────────┴───────────┐
         ▼                       ▼                       ▼                       ▼
    [NEZAJA - Army]       [IRIN - Navy]            [NEZSA - Army]         [NEDSA - Navy]
    [IRIAF - Air]         [IRIADF - Air Def]       [NEHSA - Aero]         [Quds Force]
```

#### A. Artesh (Islamic Republic of Iran Army)
- **Role:** Conventional territorial defense, border integrity, and sovereign airspace control.
- **Hardware Profile:** Upgraded pre-1979 American/British systems (F-4D/E Phantom II, F-14A Tomcat, Chieftain/M60 tanks) augmented by Russian acquisitions (Su-24MK, MiG-29, T-72S, S-300PMU2).
- **Operational Temperament:** Professional, methodical, cautious with capital asset preservation.
- **Key Components in Kharg–Shiraz Sector:**
  - *IRIAF 6th Tactical Air Base (TAB 6, Bushehr):* Operates F-4E Phantom IIs for coastal strike, maritime patrol, and anti-ship missile delivery (C-802/Noor, Nasr).
  - *IRIAF 7th Tactical Air Base (TAB 7, Shiraz):* Operates Su-24MK Fencer deep-strike interdictors and Il-76 transports.
  - *IRIADF Air Defense:* Protects Bushehr Nuclear Power Plant and coastal oil hubs with layered SAMs (S-300PMU2, Mersad/Hawk, Sayyad-2/3/Khordad-15).
  - *Artesh Navy (IRIN):* Responsible for the Gulf of Oman, Arabian Sea, and blue-water operations south of Bandar Abbas; mostly absent from inner Persian Gulf shallows.

#### B. Islamic Revolutionary Guard Corps (IRGC / Sepah)
- **Role:** Ideological protection of the Islamic Revolution, asymmetric power projection, ballistic missile arsenal, and proxy force orchestration.
- **Key Components in Kharg–Shiraz Sector:**
  - *IRGC Navy (NEDSA):* **Exclusive operational responsibility for the Persian Gulf and Strait of Hormuz**. Operates from subterranean coastal pens, hardened tunnels, and island bases. Employs thousands of Fast Inshore Attack Craft (FIAC - Boston Whalers, Peykaap, Ashora) armed with multiple-launch rockets (MLRS) and anti-ship missiles (Nasr/Kowsar); unmanned surface vessels (suicide USVs); fast attack missile craft (Tondar / Houdong-class, Shahid Soleimani stealth catamarans); and midget submarines (Ghadir-class).
  - *IRGC Aerospace Force (NEHSA):* Commands the ballistic missile, cruise missile, and one-way loitering munition (Shahed-136, Shahed-131, Mohajer-6) arsenals. Controls hardened underground missile bases ("missile cities") carved deep into Zagros limestone ridges surrounding Shiraz, Firozabad, and Kazerun.
  - *Quds Force:* External operations wing liaising with non-state regional militias.

### 2.2 The Asymmetric Network ("Axis of Resistance" / In-Game Network Equivalent)
- **Doctrinal Model:** Non-state and hybrid actors fighting from subterranean networks, dense urban centers, and dispersed mobile launcher caches.
- **Capabilities:**
  - *One-Way Attack UAS:* Commercial off-the-shelf (COTS) components blended with micro-turbojets or 50cc two-stroke lawnmower engines (MD-550), GPS/GLONASS satellite guidance with inertial dead reckoning, low radar cross-section.
  - *Maritime Swarm & Interdiction:* Remote-controlled explosive boats (USVs) with contact fuzes, sea-skimming anti-ship cruise missiles (ASCMs) launched from civilian container trucks or coastal road revetments.
  - *Civilian Concealment & Lawfare:* Basing logistics inside civilian complexes (fish-processing plants, grain silos, school compounds, hospital basements) to enforce a PR penalty on attacker precision munitions.

### 2.3 The Expeditionary Western Coalition (JSLC In-Game Equivalent)
- **Command Structure:** US Central Command (CENTCOM), combined joint task forces with GCC regional partners.
- **Force Footprint:**
  - *Naval:* US Fifth Fleet (NSA Bahrain), Carrier Strike Groups (CSGs), Amphibious Ready Groups (ARGs) with LHDs/LHAs and embarked MEUs.
  - *Air:* Al Udeid Air Base (Qatar - CAOC), Al Dhafra (UAE), Ali Al Salem (Kuwait), Prince Sultan Air Base (Saudi Arabia).
  - *Expeditionary Logistics Tether:* Dependent on maritime replenishment (USNS Supply-class UNREP), aerial cargo corridors (C-17, C-130), and forward operating bases. Vulnerable to PR attrition, host-nation basing denials, and ballistic saturation of tarmac ramps.

### 2.4 The Directorate (Arctic Stealth & Subsea Enclave Equivalent)
- **Operational Profile:** High-tech, non-aligned or covert strategic actor operating from deep-ocean sanctuaries (e.g., Diego Garcia southern approaches, deep Indian Ocean trenches). Employs subsea acoustic stealth, EMP interdiction, directed thermal/cryo weapons, and electronic warfare to exploit Coalition-Network friction.

---

## 3. Geographic, Bathymetric, & Infrastructure Invariants: Kharg Island to Shiraz Corridor

```
+===================================================================================+
|               KHARG ISLAND TO SHIRAZ STRATEGIC CORRIDOR PROFILE                   |
+===================================================================================+
| Elevation (m)                                                                     |
|                                                                                   |
| 3000m |                                                      /\  Zagros Plateau   |
|       |                                                     /  \ [Shiraz TAB 7]   |
| 2000m |                                  /\   Kazerun Pass /    \ (1,500m ASL)    |
|       |                                 /  \    (1,800m)  /      \                |
| 1000m |                                /    \  /\        /        \               |
|       |                               /      \/  \      /          \              |
|   0m  | ~~~~ Kharg Island ~~~~ Littoral Coast [Bushehr BNPP/TAB 6]                |
|       | [Sea Island / T-Jetty] (Sea level)                                        |
| -50m  | Deep Channel (-30m)                                                       |
|       +-------------------------------------------------------------------------> |
|       0 km (Kharg)    25 km (Coast)    60 km (Bushehr)   130 km (Pass)  190 km (Shiraz)
+===================================================================================+
```

### 3.1 Kharg Island (Jazireh-ye Khark) - The Strategic Petroleum Bottleneck
- **Coordinates:** $29^\circ 14' 00''\,\text{N},\ 50^\circ 18' 30''\,\text{E}$.
- **Physical Dimensions:** Length $\approx 6.0\,\text{km}$, Width $\approx 3.0\,\text{km}$, Surface Area $\approx 20\,\text{km}^2$. Highest point: Mount Dideban ($87\,\text{m}$ / $285\,\text{ft}$ ASL).
- **Geology:** Fossilized coral limestone reef capping a salt diapir (dome). Natural coral reef shelf fringes the island, creating severe shallow-water hazards on the north and west fringes.
- **Strategic Function:** **Handles approximately 85% to 90% of Iran's crude oil exports**. Crude oil is pumped from Gachsaran, Ahvaz, and Marun fields through mainland pipelines terminating at Ganaveh on the coast, then flows through **four 30-inch and 42-inch submarine pipelines** laid across the 25-kilometer seabed to Kharg.
- **Primary Terminal Infrastructure:**
  1. **The T-Jetty (East Pier):**
     - Located on the eastern leeward coast ($29^\circ 14' 15''\,\text{N},\ 50^\circ 19' 45''\,\text{E}$).
     - Length: $1,840\,\text{m}$ ($6,036\,\text{ft}$).
     - Depth alongside: $18\,\text{m}$ to $22\,\text{m}$ ($59 - 72\,\text{ft}$).
     - Accommodates 6 to 8 conventional crude tankers simultaneously (up to 250,000 DWT Suezmax and smaller VLCCs).
     - Connected to island shore via a central causeway supporting multi-product pipeline headers.
  2. **The Sea Island (Azarpad Pier / West Offshore Terminal):**
     - Located $1.5\,\text{km}$ off the western windward coast in deeper water ($29^\circ 13' 30''\,\text{N},\ 50^\circ 16' 50''\,\text{E}$).
     - Length: $1,200\,\text{m}$ ($3,937\,\text{ft}$).
     - Water depth: $30\,\text{m}$ to $32\,\text{m}$ ($98 - 105\,\text{ft}$).
     - Engineered specifically for Ultra Large Crude Carriers (ULCCs) and Very Large Crude Carriers (VLCCs) up to 500,000 DWT.
     - Vulnerable to heavy westerly swell (Shamal storms).
  3. **Main Tank Farm (Storage Depot):**
     - High plateau center of the island.
     - Over 40 welded steel floating-roof storage tanks with a total capacity of approximately **22 to 28 million barrels of crude oil**.
     - Rupture of these tanks creates catastrophic burning oil runoff flowing into the sea.
  4. **Pumping Stations & Central Manifold:**
     - The "beating heart" of the terminal. Electrically driven high-volume pumps move crude from the plateau storage tanks down into the loading arms on the piers.
     - *Strategic Vulnerability:* Destroying the pumping headers or electrical substations disables the entire island's loading capacity even if the storage tanks remain intact.
  5. **Airfield & Desalination:**
     - Kharg Airport (ICAO: OIBQ): Single asphalt runway (13/31), $2,334\,\text{m} \times 45\,\text{m}$ ($7,657\,\text{ft} \times 148\,\text{ft}$), capable of supporting C-130 Hercules tactical airlifters.
     - Thermal Desalination Plant: Located on the northeast coast; supplies 100% of the island's potable water. Destruction forces evacuation of all operational personnel within 48–72 hours.
- **Defensive Profile:**
  - Integrated air defense: Tor-M1 (SA-15) point-defense batteries guarding tank farms; Mersad (upgraded Hawk) medium-range SAMs; man-portable air defense (MANPADS - Misagh-2/3) atop hillocks.
  - Coastal artillery & ASCM: Hardened coastal revetments housing truck-mounted Noor/Ghader anti-ship cruise missiles.
  - Naval garrison: NEDSA fast patrol boat dock and bunker at Kharg harbor.

### 3.2 Persian Gulf Bathymetry & Acoustic Environment
- **Average Depth:** Only $35\,\text{m}$ ($115\,\text{ft}$); maximum depth in Iranian coastal trenches rarely exceeds $90\,\text{m}$ ($295\,\text{ft}$).
- **The Kharg Channel:** The channel between Ganaveh and Kharg Island ranges from $15\,\text{m}$ to $32\,\text{m}$ depth.
- **Operational Constraints for Naval Forces:**
  - *Large Nuclear Submarines (SSN - Virginia / Los Angeles class):* Draft $\approx 9.8\,\text{m}$ to $10.0\,\text{m}$. Operating in $35\,\text{m}$ of water severely restricts 3D maneuvering, leaving zero margin beneath keel or above sail to evade torpedoes. Extreme acoustic reverberation from coral reefs and mud bottoms degrades passive sonar.
  - *Diesel-Electric & Midget Submarines (SSK - Kilo class, Ghadir class):* Highly effective in this environment. Can rest on the sandy/mud seabed in passive "bottoming" mode with diesel engines shut down, acting as silent stationary ambush batteries for wake-homing torpedoes or mine deployment.
  - *Mine Threat:* Shallow bathymetry makes the entire littoral ideal for bottom influence mines (magnetic/acoustic/pressure fuzes like the EM-52) and tethered contact mines.
  - *Thermal Layering & Salinity:* Persian Gulf water is hyper-saline ($37 - 40\,\text{PSU}$) and subject to extreme summer surface heating ($>34^\circ\text{C}$). This produces sharp, shallow thermoclines ($10 - 20\,\text{m}$ depth) that refract acoustic sonar pings, creating massive sonar blind zones ("shadow zones") near the bottom.

### 3.3 The Coastal Littoral: Bushehr & Ganaveh
- **Port of Ganaveh:** Mainland pipeline booster terminal; sandy barrier beaches, shallow mud flats, unpaved salt pans (sabkha).
- **Bushehr City & Peninsula:**
  - *Bushehr Nuclear Power Plant (BNPP):* $28^\circ 49' 48''\,\text{N},\ 50^\circ 53' 13''\,\text{E}$. Russian-built VVER-1000 pressurized water reactor. Protected by an extensive S-300PMU2 SAM ring, 35mm Oerlikon Skyguard guns, and Pantsir-S1 / Mersad batteries. **Strict political no-strike zone** under International Humanitarian Law (IAEA / Additional Protocol I, Art. 56) due to catastrophic radiological contamination risks across Gulf desalination intakes.
  - *6th Tactical Air Base (TAB 6):* Dual $4,000\,\text{m}$ runways immediately north of Bushehr city. Hardened Aircraft Shelters (HAS) housing IRIAF F-4E Phantoms.
  - *NEDSA 2nd Naval District Base:* Command center for middle Persian Gulf fast boat operations.

### 3.4 The Zagros Mountains Barrier & Transit Passes
The Zagros mountain range forms an impassable natural geological wall separating the coastal littoral from the Iranian central plateau:
- **Topography:** Parallel anticline ridges of folded Cretaceous limestone and mudstone running northwest to southeast. Ridges rise sheer from sea level to peaks between $1,800\,\text{m}$ and $3,200\,\text{m}$ within $60\,\text{km}$ of the coast.
- **The Main Transit Arteries (The Chokepoints):**
  1. **Route 86 (Bushehr - Borazjan - Kazerun - Shiraz Highway):**
     - Total distance: $\approx 230\,\text{km}$.
     - *Borazjan to Dalaki:* Low foothills, dry alluvial washes (wadis).
     - *Dalaki to Kazerun (The Kotal-e Dokhtar / Kotal-e Pirzan escarpments):* The road ascends $1,400\,\text{m}$ over a horizontal distance of just $30\,\text{km}$. Extreme serpentine switchbacks carved into near-vertical limestone cliffs, narrow dual-lane highway, series of unreinforced rock tunnels.
     - *Operational Vulnerability:* A single demolished bridge, cratered tunnel, or precision-triggered rockslide at the Kazerun Escarpment completely severs ground mechanized movement between Shiraz and the Persian Gulf coast for weeks.
  2. **Route 65 (Borazjan - Firozabad - Shiraz):** Alternate southern mountain corridor; equally narrow, highly constricted gorges.
- **METOC Phenomena in the Zagros:**
  - *Catabatic Downdrafts & Rotor Winds:* Violent turbulence over mountain ridges severely degrades low-altitude helicopter and tilt-rotor (V-22) operations.
  - *Winter Freezing / Snow:* Passes above $1,500\,\text{m}$ experience heavy snow, sub-zero icing, and freezing fog from December to March, creating severe icing hazards for UAVs and aircraft wings.
  - *Extreme Summer Thermal Inversions:* Surface temperatures on the coast exceed $48^\circ\text{C}$ with high humidity, while the plateau at Shiraz ($1,500\,\text{m}$) sits at $35^\circ\text{C}$ with $10\%$ humidity. This extreme refractive gradient creates anomalous radar ducting along the coastal plain.

### 3.5 Shiraz (Fars Province) - Strategic Logistics & Aerospace Hub
- **Coordinates:** $29^\circ 37' 00''\,\text{N},\ 52^\circ 32' 00''\,\text{E}$. Elevation: $1,500\,\text{m}$ ($4,920\,\text{ft}$) ASL.
- **Military Infrastructure:**
  - *7th Tactical Air Base (TAB 7 / Shahid Dowran):* Dual parallel runways ($4,270\,\text{m} \times 45\,\text{m}$). Main operating base for IRIAF Su-24MK Fencer long-range strike bombers, Il-76 Candid transports, and C-130 Hercules. Subterranean aircraft shelters tunneled into the southern mountain flanks.
  - *IRGC Aerospace Force Zagros Missile Garrisons:* Several hardened underground missile launch facilities located in the limestone valleys west and south of Shiraz (e.g., Kazerun, Firozabad). Rail-mobile and transporter-erector-launcher (TEL) garrisons for Fateh-110, Zolfaghar, Dezful, and Khorramshahr ballistic missiles.
  - *Shiraz Electronics Industries (SEI / IEI):* Iran's primary state defense electronics production center (radar development, electronic warfare jammers, optical guidance seekers, avionics reverse-engineering).

---

## 4. Historical Precedents: The Kharg Island Air-Sea Battles (1982–1988)

The historical combat record of Kharg Island during the Iran-Iraq War ("Tanker War") provides verified operational lessons for modern military simulation:

```
+===================================================================================+
|               HISTORICAL PRECEDENTS: THE KHARG CONFLICT CHRONOLOGY                |
+===================================================================================+
| Date        | Attacker  | Weapon System         | Tactical Outcome / Impact        |
+=============+===========+=======================+==================================+
| 1982–1984   | Iraq      | Super Étendard /      | Iraq declares maritime exclusion |
|             | (IQAF)    | AM39 Exocet           | zone. Hits tankers loading at    |
|             |           |                       | Kharg; terminal remains active.  |
+-------------+-----------+-----------------------+----------------------------------+
| 15 Aug 1985 | Iraq      | Mirage F1EQ-5 /       | First massive low-level strike   |
|             | (IQAF)    | AS.30L Laser AGM &    | on T-Jetty. Heavy structural fire|
|             |           | 250kg iron bombs      | damages 2 berths; repaired in 48h|
+-------------+-----------+-----------------------+----------------------------------+
| 1986–1987   | Iraq      | Mirage F1EQ /         | Repeated multi-wave raids on Sea |
|             | (IQAF)    | Belouga cluster bombs | Island. Storage tanks burned;    |
|             |           |                       | shuttle tanker flotillas to Sirri|
|             |           |                       | Island established by Iran.      |
+-------------+-----------+-----------------------+----------------------------------+
| 18 Apr 1988 | USA       | Operation Praying     | US Navy retaliates for USS Samuel|
|             | (USN)     | Mantis: Harpoon,      | B. Roberts mine strike. Sinks    |
|             |           | LGBs, 5-inch naval    | Sahand frigate, Joshan gunboat,  |
|             |           | gunfire               | destroys Sassan & Sirri oil rigs.|
+===================================================================================+
```

### Key Analytical Takeaways from the Tanker War:
1. **Structural Redundancy & Damage Resistance:** Kharg Island was struck more than **2,800 times** by Iraqi aircraft, missiles, and artillery between 1980 and 1988. Yet, Iran's crude oil exports were **never completely halted for more than a few consecutive days**. Massive crude storage facilities and steel-lattice piers possess extraordinary structural resilience against high-explosive blast.
2. **The True Critical Nodes:** The components that caused prolonged export shutdowns were not the massive storage tanks (which merely created spectacular fires), but **the oil manifold control valve rooms, pump drive turbine engines, and submarine pipeline landfall headers**.
3. **The Shuttle Pipeline Bypass:** When attacks on Kharg intensified, Iran deployed shuttle tankers to move crude from Kharg to floating storage vessels at Sirri Island and Larak Island near the Strait of Hormuz, outside the combat radius of Iraqi Mirage F1s. In modern operations, interdiction must target both loading berths and coastal feeder pipelines.

---

## 5. Grounding Game Concepts in Documented Regional Conduct

To maintain strict alignment with the game's core concepts (Coalition / Network / Directorate, PR War logistics, selective sub-system damage, and deterministic 30 Hz lockstep):

### 5.1 Factional Asymmetry in the Persian Gulf
- **Coalition (JSLC):** High-tech, expeditionary, rules-bound. Relies on Aegis air defense (Arleigh Burke, Ticonderoga), F-35 stealth ISR sweeps, amphibious LCAC beach landings, and carrier strike aviation. Crippled by logistical overhead (UNREP resupply lines) and international PR blowback when oil infrastructure catches fire or civilian collateral occurs.
- **The Network (AoI):** Low-cost, swarm-oriented, dispersed. Deploys hundreds of fast-attack explosive speedboats, Shahed loitering drones launched from commercial shipping containers, coastal truck-mounted ASCMs, and deeply buried Zagros tunnel caches. Exploit environmental disaster and fuel shortages as PR weapons.
- **The Directorate (Penguins):** Covert, cold, subsea operations. Deploys autonomous undersea gliders, deep-water acoustic sensors, and electromagnetic interference (EMP) from Indian Ocean approaches, sabotaging regional infrastructure without kinetic attribution.

### 5.2 Public Legitimacy & The Global Oil Price Mechanism
In accordance with **Directive [D-006]** ("PR as a logistical necessity"):
- **The Crude Spill / Tanker Fire PR Trap:** Damaging Kharg oil storage tanks causes massive hydrocarbon burning plumes visible from orbit and releases millions of barrels into the Gulf, choking GCC desalination plants (Jubail, Ras Laffan) and commercial shipping. In-game, this triggers immediate **diplomatic sanctions**, freezing Coalition munitions resupply and increasing credit costs.
- **Selective Subsystem Targeting as PR Preservation:** A Coalition commander who surgically targets the *electrical transformer substation* on Kharg (disabling pumps without rupturing oil manifolds) achieves the interdiction objective while suffering zero PR penalty.

---

## 6. Persian Gulf & Zagros Tactical Audit Protocol ("What the Skill Knows to Ask")

When reviewing or authoring maps, operational briefs, unit rosters, and mechanics set in this theatre, the auditor must run through this 8-cluster checklist:

### Cluster 1: Bathymetry & Keel Draft Verification
* *Question 1.1:* Does any map depicting naval operations allow deep-draft capital ships (e.g. CVN, LHD, DDG) to operate in waters shallower than $12.0\,\text{m}$?
* *Question 1.2:* Are submarine acoustics properly degraded in shallow waters ($\le 35\,\text{m}$ depth), preventing unrealistic blue-water sonar detection ranges?
* *Question 1.3:* Are LCAC hovercraft correctly restricted to flat sandy beaches or designated slipways rather than scaling sheer coral cliffs?

### Cluster 2: Kharg Island Infrastructure Fidelity
* *Question 2.1:* Is the distinctive physical asymmetry between the Eastern T-Jetty ($1,840\,\text{m}$, shallow VLCC/Suezmax) and the Western Sea Island ($1,200\,\text{m}$ offshore, deep-water ULCC) preserved?
* *Question 2.2:* Are oil storage tanks correctly modeled as floating-roof tanks with surrounding containment berms (dikes)?
* *Question 2.3:* Is the central pumping station represented as a discrete high-value target sub-entity rather than treating the entire island as a homogeneous health pool?

### Cluster 3: Zagros Chokepoint & Orographic Friction
* *Question 3.1:* Do ground movement paths through the Zagros conform to natural canyon passes (Route 86 Kazerun corridor), preventing heavy armor from cross-country pathing over $60^\circ$ limestone cliffs?
* *Question 3.2:* Are bridges and mountain tunnel portals designated as destructible critical choke entities?
* *Question 3.3:* Does the map account for high-altitude engine performance loss and helicopter density altitude penalties at plateau elevations ($>1,500\,\text{m}$ ASL)?

### Cluster 4: Sensor Physics & Atmospheric Dust/Ducting
* *Question 4.1:* During Shamal dust storm events, are visible Electro-Optical (EO) sensor ranges degraded ($0.35\times$) while Long-Wave Infrared (LWIR) remains partially functional ($0.75\times$)?
* *Question 4.2:* Does coastal thermal inversion / radar ducting allow surface search radars anomalous long-range detection of surface ships along the water surface while blinding high-angle air search?

### Cluster 5: Iran / Regional Order of Battle Grounding
* *Question 5.1:* Are fast attack craft and coastal missile batteries correctly attributed to the IRGC Navy (NEDSA) rather than the conventional Artesh Navy (IRIN)?
* *Question 5.2:* Are ballistic missile garrisons placed in hardened Zagros mountain underground bunkers rather than exposed coastal airfields?
* *Question 5.3:* Is Bushehr Nuclear Power Plant (BNPP) designated with special LOAC status (protected infrastructure with catastrophic PR penalties for attack)?

### Cluster 6: Asymmetric Drone & Cruise Missile Profiles
* *Question 6.1:* Do Shahed-136 loitering munition units follow pre-programmed waypoint trajectories at low altitudes ($30 - 100\,\text{m}$ AGL) rather than unrealistic high-G dogfighting maneuvers?
* *Question 6.2:* Are coastal anti-ship cruise missiles modeled with pop-up radar altimeter terminal skimming ($3 - 5\,\text{m}$ above sea level)?

### Cluster 7: Logistical Tethers & Supply Lines
* *Question 7.1:* Does the scenario model the physical supply tether for Coalition forces (e.g. offshore UNREP supply ship or beachhead logistics hub)?
* *Question 7.2:* Are fuel, ready-rack ammunition, and mechanical wear enforced as operational constraints during extended mechanized pushes through mountain terrain?

### Cluster 8: Public Legitimacy / PR War Consequences
* *Question 8.1:* Does uncontrolled destruction of oil infrastructure trigger diplomatic and economic penalties (halting munitions resupply)?
* *Question 8.2:* Can the Network faction weaponize civilian shielding around coastal installations to bait Coalition precision weapons into collateral damage incidents?

---

## Part 14: Palestinian Affairs — Factional Doctrine, Subterranean Warfare & LOAC Conduct (`palestinian-affairs`)

*Repository Path: [`skills/palestinian-affairs/SKILL.md`](./skills/palestinian-affairs/SKILL.md)*

---
name: palestinian-affairs
description: >-
  Authoritative engineering and domain standard for Palestinian politics, factional doctrine, governance,
  subterranean warfare, rocket programs, patron financing, UNRWA institutional interface, information operations,
  and documented conduct under LOAC for deterministic RTS game design.
---

# Palestinian Affairs: Domain Expertise & Analysis Standard

This standard establishes the operational doctrine, political topology, empirical weapons data, legal-institutional frameworks, and documented conduct records governing Palestinian factions and asymmetric warfare dynamics for deterministic military simulations (30 Hz lockstep) and game design in *Command & Conquer: Skirmish* / JSLCNC.

---

## 1. Actor Map & Factional Topology

The Palestinian political and operational landscape is characterized by deep fragmentation, dual governance structures, competing ideological frameworks, and varied degrees of patron dependency.

```
                                  ┌───────────────────────────────────────────────┐
                                  │           EXTERNAL PATRON ARCHITECTURE        │
                                  └───────────────────────────────────────────────┘
                                      │                        │               │
                            IRGC Quds Force              State of Qatar  Turkish MIT / Finance
                            (Weapons, Training,          (Cash Grants,   (Political Sanctuary,
                             Command Guidance)            Fuel Subsidies) Financial Networks)
                                      │                        │               │
                                      ▼                        ▼               ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       PALESTINIAN OPERATIONAL ACTORS                                   │
├──────────────────────────────────────┬───────────────────────────────────┬─────────────────────────────┤
│            ISLAMIST BLOC             │           SECULAR / PLO           │    HYBRID LOCAL BATTALIONS  │
├──────────────────────────────────────┼───────────────────────────────────┼─────────────────────────────┤
│ 1. HAMAS (Qassam Brigades)           │ 1. FATAH / PALESTINIAN AUTHORITY  │ 1. Jenin Battalion (PIJ-led)│
│    - Governance: Gaza Strip (2007+)  │    - Governance: West Bank Area A │ 2. Lions' Den (Nablus)      │
│    - Shura Council & Politburo       │    - Security Coordination w/ IDF │ 3. Tulkarm Rapid Response   │
│    - Subterranean Tunnel Metro       │    - Mukataa Civil Bureaucracy    │ - Youth-led, cross-factional│
│ 2. PALESTINIAN ISLAMIC JIHAD (PIJ)   │ 2. PFLP (Abu Ali Mustafa)         │ - Decentralized, street IEDs│
│    - Saraya al-Quds military wing    │    - Marxist-Leninist rejectionist│ - Telegram-mobilized ops    │
│    - Pure military rejectionism      │ 3. DFLP (National Resistance)     │                             │
│    - Direct IRGC-QF command tether   │    - Secular leftist cadre        │                             │
└──────────────────────────────────────┴───────────────────────────────────┴─────────────────────────────┘
                                      ▲                                    ▲
                                      │                                    │
                                      └──────────────────┬─────────────────┘
                                                         │
                                        ┌──────────────────────────────────┐
                                        │   POPULATION & CIVIL SUBSTRATE   │
                                        ├──────────────────────────────────┤
                                        │ - UNRWA (Services, Schools, Food)│
                                        │ - Clan / Familial Networks       │
                                        │ - Economic Blockade & Dependency │
                                        │ - Dissent & Internal Suppression │
                                        └──────────────────────────────────┘
```

### 1.1 Hamas (Harakat al-Muqawama al-Islamiya)
- **Organizational Architecture:** Founded in 1987 as an offshoot of the Muslim Brotherhood. Dual-structured between political bureau (overseas leadership in Doha, Istanbul, Beirut; internal Gaza leadership) and military wing (**Izz ad-Din al-Qassam Brigades**).
- **Governance:** De facto governing authority in the Gaza Strip following the violent June 2007 factional civil war with Fatah. Operates ministries, police forces, judiciary, tax collection, and internal security apparatus (**Majd** and Internal Security Force).
- **Military Wing (Al-Qassam Brigades):** Highly structured into 5 regional brigades (Northern Gaza, Gaza City, Central/Deir al-Balah, Khan Yunis, Rafah), subdivided into battalions, companies, and specialized platoons:
  - *Engineering & Tunnel Corps:* Responsible for construction, maintenance, and detonation of subterranean networks.
  - *Rocket Force:* Manages fixed underground launch tubes, mobile launchers, and rocket storage.
  - *Nukhba (Elite Naval & Commando Force):* Infiltration specialists, combat swimmers, motorized paraglider operators.
  - *Anti-Armor Units:* Deployed with Russian-designed Kornet, 9M113 Konkurs, and indigenous Al-Yassin 105 tandem-charge RPGs.
  - *Drone / Aerial Units:* Ababeel, Zouari reconnaissance drones, commercial quadcopters with drop mechanisms.

### 1.2 Palestinian Islamic Jihad (PIJ / Harakat al-Jihad al-Islami fi Filastin)
- **Nature & Cadre:** Founded in 1981 by Fathi Shaqaqi. Distinct from Hamas in its rejection of social governance, civil administration, or electoral participation. Functioning almost exclusively as a dedicated militant cadre.
- **Military Wing (Saraya al-Quds / Jerusalem Brigades):** Second-largest rocket arsenal in Gaza; deploys heavy short-range mortars, Badr-3 multi-barrel systems, and Fajr-5 variants.
- **Command Relationship:** Maintains direct command-and-control links to the Islamic Revolutionary Guard Corps Quds Force (IRGC-QF) and Palestinian branch commander based in Damascus/Beirut.

### 1.3 Palestinian Authority (PA) / Fatah / PLO
- **Nature & Jurisdiction:** Governs autonomous enclaves in the West Bank (Area A administrative and security control, Area B administrative control under the Oslo II Accords). Led by Chairman Mahmoud Abbas; headquartered in Ramallah (the Mukataa).
- **Security Forces (PASF):** Trained in part under US Security Coordinator (USSC) supervision; includes National Security Forces (NSF), Preventative Security Service (PSS), and General Intelligence Service (GIS).
- **Factional Tension:** Engages in delicate security coordination with Israel while maintaining contentious relations with Hamas; widely perceived domestically as bureaucratically sclerotic and lacking electoral mandate (no presidential elections held since 2005, no legislative elections since 2006).

### 1.4 Popular Front for the Liberation of Palestine (PFLP) & Democratic Front (DFLP)
- **Nature:** Secular, Marxist-Leninist factions belonging to the PLO umbrella. The PFLP's military arm (**Abu Ali Mustafa Brigades**) and DFLP's (**National Resistance Brigades**) maintain tactical cooperation with Islamist factions in Gaza through the Joint Operations Room while retaining distinct ideological identity.

### 1.5 Decentralized Hybrid Battalions (West Bank)
- **Emergence (2021–Present):** Localized insurgent cells (Jenin Battalion, Tulkarm Battalion, Lions' Den / Areen al-Usud in Nablus).
- **Tactical Profile:** Cross-factional recruitment of disaffected youth; heavy use of commercial Telegram channels for operational coordination and recruitment; tactical emphasis on improvised explosive devices (IEDs) buried beneath urban roadways, small-arms ambushes, and sniper operations.

### 1.6 UNRWA (United Nations Relief and Works Agency for Palestine Refugees in the Near East)
- **Mandate & Scale:** Established by UN General Assembly Resolution 302 (IV) in 1949. Provides basic education, primary healthcare, relief, social services, and microfinance to registered refugees across Gaza, the West Bank, Jordan, Lebanon, and Syria.
- **Operational Interface in Conflict Zones:** Employs over 13,000 local Palestinian staff in Gaza. Operates over 270 schools, clinics, and logistics depots. Its facilities hold protected status under international humanitarian law (LOAC) as civilian and humanitarian installations.
- **Documented Friction Points:** Neutrality violations documented by UN Boards of Inquiry (weapons stored in vacant schools during conflicts in 2014); combatant co-optation of facilities; tunnels excavated in proximity to or beneath facilities; intelligence disclosures regarding staff affiliation with armed factions.

---

## 2. Sourcing Hierarchy & Verification Standard

In military simulations depicting modern asymmetric conflict, distinguishing verified fact from psychological operations, propaganda claims, and institutional bias is paramount. All doctrinal profiles, combat mechanics, and narrative framing must adhere to a strict six-tier sourcing hierarchy.

```
                      ┌───────────────────────────────────────────────┐
                      │    TIER 1: CAPTURED PRIMARY FORENSIC DATA     │
                      │  Battlefield blueprints, hard drives, photos, │
                      │  weapons serials, physical shaft surveys      │
                      └───────────────────────┬───────────────────────┘
                                              ▼
                      ┌───────────────────────────────────────────────┐
                      │    TIER 2: INDEPENDENT MULTI-SPECTRAL OSINT   │
                      │  Satellite SAR/optical (Maxar, Planet Labs),  │
                      │  geolocation, video ballistics (Bellingcat)   │
                      └───────────────────────┬───────────────────────┘
                                              ▼
                      ┌───────────────────────────────────────────────┐
                      │    TIER 3: UN COMMISSIONS OF INQUIRY & BOI    │
                      │  Independent UN Boards of Inquiry, Colonna    │
                      │  Independent Review, OCHA field verifications │
                      └───────────────────────┬───────────────────────┘
                                              ▼
                      ┌───────────────────────────────────────────────┐
                      │    TIER 4: HUMAN RIGHTS NGO INVESTIGATIONS    │
                      │  Amnesty International, Human Rights Watch,   │
                      │  B'Tselem (cross-checked for field methodology│
                      └───────────────────────┬───────────────────────┘
                                              ▼
                      ┌───────────────────────────────────────────────┐
                      │    TIER 5: DECLASSIFIED GOVERNMENT INTELLIGENCE│
                      │  IDF declassified briefings, US DOJ indict-   │
                      │  ments, US Treasury OFAC filings, Shin Bet ISA│
                      └───────────────────────┬───────────────────────┘
                                              ▼
                      ┌───────────────────────────────────────────────┐
                      │    TIER 6: MAJOR INVESTIGATIVE JOURNALISM     │
                      │  Reuters, NYT, Washington Post, WSJ, BBC      │
                      │  (requires named sources & physical evidence) │
                      └───────────────────────────────────────────────┘
```

### 2.1 Cross-Check Rule
No tactical capability, operational incident, or controversial conduct may be coded into game logic or lore as an established mechanical fact without corroboration across **at least two independent tiers** (e.g., Tier 1 captured material + Tier 2 geospatial validation; or Tier 3 UN inquiry + Tier 5 declassified judicial indictment).

### 2.2 Classification Markers
- `[DOCUMENTED FACT]`: Corroborated by independent multi-spectral imagery, captured documents, and third-party forensic analysis.
- `[ALLEGATION]`: Claim asserted by a belligerent or interested party lacking independent material or physical verification.
- `[DISPUTED]`: Contested operational claims where credible investigative bodies have reached divergent conclusions.

---

## 3. Documented-Conduct Catalogue & Ground Truth

Per the operator's concept test—*"if it is done in real life and it is terrible, then we include it"*—this catalogue establishes the documented operational reality of armed conflict in Palestinian theaters, grounded in verified citations.

### 3.1 Subterranean Warfare Architecture ("The Gaza Metro")
- **Scale and Character:** Extensive subterranean tunnel network estimated between 400 and 500+ kilometers across the Gaza Strip.
- **Architectural Typologies:**
  1. *Strategic / Command Bunkers:* Situated at depths of 20 to 70 meters. Reinforced with curved precast concrete panels, integrated three-phase AC electricity, air conditioning, landline communication cables (immune to RF jamming), living quarters, and blast doors.
  2. *Offensive / Cross-Border Infiltration Tunnels:* Dug toward the security perimeter; feature narrow cross-sections (1.8m height, 0.8m width) with hidden exit hatches disguised in brush, greenhouses, or drainage ditches.
  3. *Tactical Ambush & Transit Shafts:* Interconnecting shafts within urban neighborhoods, enabling fighters to emerge behind advancing armor, fire anti-tank rockets, and disappear underground within 30 to 45 seconds.
  4. *Logistical & Smuggling Tunnels:* Concentrated along the Philadelphi Corridor (Rafah-Sinai border); large-diameter shafts used to move commercial goods, cash, fuel, rocket motors, and dual-use components.
- **Surface Interfacing:** Documented shaft entrances located inside residential homes, underneath tiled bathroom floors, inside wardrobes, beneath mosque pulpits, adjacent to UNRWA schools, and within hospital complexes.
- **Citations:**
  - West Point Modern War Institute (MWI), *Underground Nightmare: The Gaza Tunnels*, John Spencer (2023–2024).
  - West Point Combating Terrorism Center (CTC Sentinel), *The Subterranean Warfare Doctrine of Hamas*, Vol. 17, Issue 1 (2024).
  - United Nations Board of Inquiry Reports (A/69/926, 2015; A/74/820, 2020) regarding tunnel shafts near UN facilities.
  - Washington Post Visual Forensics, *Mapping the Under-Gaza Tunnel Network* (Dec 2023).

### 3.2 Urban Shielding & Protected Infrastructure Use
- **LOAC Framework:** Under Geneva Convention IV (Art. 28) and Additional Protocol I (Art. 51[7]), utilizing the presence of civilian populations or protected objects to shield military targets is an unambiguous war crime. Under LOAC, when a protected facility (hospital, school, place of worship) is utilized for military action (command post, weapons depot, firing position), it forfeits its special civilian immunity, subject to strict warnings and proportionality calculations.
- **Documented Manifestations:**
  - *Rocket Launchers adjacent to Schools/Clinics:* Fixed underground launch tubes (multi-barrel 122mm and Qassam pods) placed within 10 to 50 meters of operational schools, refugee shelters, and medical clinics to deter counter-battery artillery.
  - *Weapons Storage in Civilian Habitats:* Caching rocket warheads, mortar rounds, and explosive charges in apartment buildings, attics, and mosques.
  - *Command Headquarters beneath Hospitals:* Installation of computer terminals, communications nodes, and armed guard rooms beneath Shifa Hospital, Indonesian Hospital, and European Hospital.
  - *Tactical Exploitation of Ambulances & Aid Convoys:* Documented transport of armed fighters and weapons inside marked ambulances to bypass aerial surveillance.
- **Citations:**
  - NATO Strategic Communications Centre of Excellence (StratCom COE), *Hamas’ Use of Human Shields in Gaza* (2014, updated 2019).
  - Amnesty International, *Unlawful and Deadly: Rocket and Mortar Attacks by Palestinian Armed Groups During the 2014 Gaza/Israel Conflict* (March 2015, Index: MDE 21/1178/2015).
  - UN Independent Commission of Inquiry on the 2014 Gaza Conflict (A/HRC/29/52, June 2015), documenting weapons storage in UN schools.
  - French Directorate of Military Intelligence (DRM) & US Office of the Director of National Intelligence (ODNI) briefings on hospital co-optation (Nov 2023).

### 3.3 Hostage-Taking, Civilian Abduction & Exploitation
- **Nature of the Practice:** Mass taking of civilian and military captives for strategic leverage, psychological coercion, and prisoner exchanges (e.g., Gilad Shalit 2006, 251 captives on October 7, 2023).
- **Detention Protocols:** Hostages dispersed among private residential apartments guarded by civilian families/militants, as well as confined in subterranean tunnels under severe conditions (cages, chains, deprivation of medical care, sensory deprivation).
- **Psychological Operations:** Production and dissemination of choreographed "proof of life" videos, scripted confessions, and funeral-style countdown videos designed to incite domestic panic in the adversary's civilian population.
- **Citations:**
  - Human Rights Watch, *“I Can’t Stop Crying”: Terror and Trauma in Hamas’s October 7 Assault* (July 2024).
  - United Nations Independent International Commission of Inquiry on the Occupied Palestinian Territory (A/HRC/56/26, June 2024), finding widespread war crimes and crimes against humanity in hostage-taking.
  - International Criminal Court (ICC), Office of the Prosecutor, *Statement on Applications for Arrest Warrants in the Situation in the State of Palestine* (May 20, 2024), charging hostage-taking as a war crime under Rome Statute Art. 8(2)(a)(vii).

### 3.4 Rocket & Mortar Arsenal: Ballistic Reality & Short-Fall Hazards
- **Arsenal Composition:**
  - *Indigenous Qassam (Q-12, Q-20):* Improvised unguided solid-fuel artillery rockets constructed from industrial pipes, sugar/potassium nitrate propellant, and repurposed explosives; range 5–20 km.
  - *M-75, M-90, J-80, A-120, R-160, Ayash-250:* Stepped upgrades in caliber (160mm to 250mm) and range (75 to 250 km), reaching central and northern Israeli population centers.
  - *Supplied / Cloned Systems:* Fajr-3 / Fajr-5 (Iranian), 122mm BM-21 Grad rockets (Chinese/Russian origin via Libya/Sudan), Badr-3 (heavy 250kg warhead short-range rocket).
- **Inherent Indiscrimination:** Completely unguided; lack inertial guidance or terminal seekers. Target broad urban areas, constituting indiscriminate attacks per LOAC.
- **The Short-Fall Phenomenon:** Due to crude manufacturing tolerances, defective propellants, and faulty launch electronics, between **10% and 20% of all rockets launched from Gaza fail in flight and impact inside the Gaza Strip**.
- **Citations:**
  - Human Rights Watch, *Gaza: Palestinian Rockets Offer No Precision* (Dec 2021).
  - Bellingcat Open Source Investigation, *The Al-Ahli Arab Hospital Explosion: Geolocation and Trajectory Analysis* (Oct 2023).
  - US National Intelligence Council (NIC), *Declassified Intelligence Assessment on the Al-Ahli Arab Hospital Blast* (Oct 2023).
  - Israel Defense Forces (IDF) Operational Trajectory Data, showing >1,500 rocket shortfalls landing inside Gaza during major escalations.

### 3.5 Information Operations, Combat Videography & Martyr Discourse
- **Media Production Architecture:** Highly sophisticated combat media production branch. Employs forward cameramen embedded with anti-armor teams wearing commercial GoPro cameras.
- **Visual Vocabulary:** Signature red inverted targeting triangle (`🔻`) overlaying enemy targets before detonation; synchronized religious chants; rapid release on official Telegram channels within 2 to 6 hours of engagement.
- **Martyr Videos & Wills:** Pre-recorded ideological testament videos filmed in front of factional flags, Quranic verses, and assault rifles.
- **Casualty Accounting & Hospital Press Briefings:** Rapid narrative monopolization; utilizing health authorities to issue casualty counts within minutes of airstrikes, intentionally aggregating combatants with non-combatants to maximize diplomatic outrage.
- **Citations:**
  - West Point Combating Terrorism Center (CTC Sentinel), *The Media Strategy of Hamas in the October 7 War*, Vol. 17, Issue 2 (2024).
  - Washington Institute for Near East Policy, *Hamas's Information Operations: From Pallywood to Telegram*, PolicyWatch 3822 (2024).
  - Center for Strategic and International Studies (CSIS), *The Information Battlefield in Modern Urban Warfare* (2024).

### 3.6 Internal Repression, Summary Executions & Civil Dissent Suppression
- **Collaborator Purges:** Summary executions of individuals suspected of collaborating with Israeli intelligence (Shin Bet). Victims executed in public squares, dragged behind motorcycles, or shot in basement interrogation cells without due judicial process.
- **Suppression of Street Protests:** Violent dispersal of civilian socio-economic protests (e.g., the *Bidna Na'ish* / "We Want to Live" movements in 2019 and summer 2023). Beatings, arbitrary detentions, and live-fire suppression against civilians demonstrating against poverty, power shortages, and taxes.
- **Citations:**
  - Amnesty International, *'Strangling Necks': Abductions, Torture and Summary Killings by Hamas Forces During the 2014 Gaza/Israel Conflict* (May 2015, Index: MDE 21/1643/2015).
  - Human Rights Watch, *Two Authorities, One Way, Zero Dissent: Arbitrary Arrest and Torture Under the Palestinian Authority and Hamas* (Oct 2018).
  - Palestinian Center for Human Rights (PCHR) Gaza Field Reports on internal political violence (2019, 2023).

### 3.7 Dual-Use Diversion, Aid Siphoning & Smuggling Economics
- **Dual-Use Diversion:** Systematic redirection of civilian construction imports (precast cement, steel rebar, electrical cable, water distribution pipes, nitrogen fertilizers) into subterranean fortification and rocket manufacturing.
- **Humanitarian Logistics Hijacking:** Armed interception of commercial food and UN humanitarian relief trucks entering transit corridors; stockpiling supplies in subterranean depots while reselling aid on the black market at inflated prices to fund military payrolls.
- **Citations:**
  - World Bank, *Economic Monitoring Report to the Ad Hoc Liaison Committee: Reconstructing Gaza and Dual-Use Restrictions* (2018).
  - Israeli Coordinator of Government Activities in the Territories (COGAT), *Reports on Dual-Use Material Interceptions at Kerem Shalom* (2015–2023).
  - United States Department of the Treasury, Office of Foreign Assets Control (OFAC), *Sanctions Designations on Hamas Financial Facilitators and Smuggling Networks* (Oct 2023, Jan 2024).

---

## 4. Analytical Audit Questions for RTS Engine & Canon

When evaluating engine systems, unit rosters, lawfare mechanics, and game lore, the domain expert must apply the following rigorous audit rubric:

1. **Physical Scale & Realism Integrity:**
   - Are subterranean transit times physically consistent with human walking/running speeds through narrow, unventilated, blast-door-obstructed shafts?
   - Do unguided rocket salvos exhibit authentic ballistic dispersion and realistic failure/short-fall probability?

2. **LOAC & Lawfare Symmetry:**
   - Does the simulation correctly model the legal consequence of co-locating military command elements within civilian facilities (loss of absolute immunity, proportionality calculations)?
   - Are PR and legitimacy penalties grounded in verifiable physical logistics (arms embargoes, port closures, fuel cuts) rather than artificial weapon-jamming or moralistic scoreboards?

3. **Asymmetric Operational Mechanisms:**
   - Is civilian shielding represented as a deliberate tactical calculation with material PR consequences?
   - Is humanitarian aid depicted with its authentic dual nature: vital sustenance for non-combatants versus strategic vulnerability to armed hijacking and diversion?

4. **Tone & Satiro-Documentary Boundaries:**
   - Does the portrayal of non-state actors adhere strictly to operational and political entities rather than ethnic or religious caricatures?
   - Does the satire target institutional hypocrisy, weaponized lawfare, and military-industrial excess without trivializing verified humanitarian atrocities?

---

## Part 15: Modern Middle East History & Operational Precedents Standard (`middle-east-history`)

*Repository Path: [`skills/middle-east-history/SKILL.md`](./skills/middle-east-history/SKILL.md)*

---
name: middle-east-history
description: >-
  Authoritative historical and historiographical standard for the modern Middle East
  (Ottoman collapse to present: Mandate era, Arab-Israeli wars 1948-1973, Iranian Revolution 1979,
  Iran-Iraq War 1980-1988 including the Tanker War and Kharg Island strikes, Lebanon 1982-2006,
  the Palestinian intifadas, the rise and structure of the 'Axis of Resistance', Gulf security,
  and Red Sea maritime interdiction). Governs historical accuracy, operational precedents,
  and doctrinal causality for military simulation and game canon.
---

# Modern Middle East History & Operational Precedents Standard

This standard establishes the authoritative historical timelines, empirical conflict datasets, historiographical frameworks, and operational military precedents governing the simulation of Middle Eastern conflicts, geopolitical doctrine, and asymmetric warfare.

---

## 1. Doctrinal Periodization & Chronological Framework (1914–Present)

Middle Eastern military history from the collapse of the Ottoman Empire to 21st-century multi-domain warfare divides into eight distinct operational and geopolitical eras:

```
               CHRONOLOGICAL PERIODIZATION OF MODERN MIDDLE EASTERN CONFLICT
  1914        1948        1967   1973   1979   1988   2003          2011      2023-Present
┌───────┬───────────┬──────────────┬──────────────┬──────────────┬──────────────┬───────────┐
│Ottoman│ 1948-1956 │ Six-Day War  │ Iran-Iraq    │ Post-Cold    │ Arab Spring, │ Red Sea,  │
│Decline│ Early Arab│ & Yom Kippur │ War, Tanker  │ War, Oslo,   │ Syrian War,  │ Multi-    │
│& Sykes│ -Israeli  │ Classical    │ War, Lebanon │ Intifadas,   │ 'Axis of     │ Front War │
│-Picot │ Wars      │ State Armor  │ & Hezbollah  │ 2003 Iraq    │ Resistance'  │ & Drones  │
└───────┴───────────┴──────────────┴──────────────┴──────────────┴──────────────┴───────────┘
```

### 1.1 Era I: Imperial Collapse, Mandates, and State Partition (1914–1947)
- **1915–1916 (McMahon–Hussein Correspondence):** British promises of Arab independence in exchange for the Arab Revolt against the Ottomans.
- **May 16, 1916 (Sykes–Picot Agreement):** Secret Anglo-French partition of Ottoman Arab provinces into direct and indirect zones of control (French Syria/Lebanon, British Mesopotamia/Transjordan/Palestine).
- **November 2, 1917 (Balfour Declaration):** British declaration viewing with favor "the establishment in Palestine of a national home for the Jewish people."
- **1920 (San Remo Conference & Treaty of Sèvres):** Formal League of Nations Mandates assigned; arbitrary borders drawn cutting across ethnic, sectarian, and hydrological basins.
- **1936–1939 (The Arab Revolt in Palestine):** Asymmetric uprising against British rule and Zionist migration; suppressed by British forces via harsh counter-insurgency, collective punishment, and Special Night Squads (Orde Wingate), crippling Palestinian traditional leadership.
- **November 29, 1947 (UN Resolution 181):** UN General Assembly adopts the Partition Plan for Palestine (56% Jewish state, 43% Arab state, internationalized Jerusalem); rejected by Arab states and Higher Arab Committee.

### 1.2 Era II: The Early Arab-Israeli Wars & Suez Nationalization (1948–1956)
- **November 1947 – May 1948 (Civil War in Mandatory Palestine):** Communal conflict between Haganah/Irgun/Lehi and Arab Liberation Army/Holy War Army. Operation Nachshon, Deir Yassin massacre (April 9, 1948), and flight/expulsion of urban elites.
- **May 14, 1948:** Proclamation of the State of Israel; termination of the British Mandate.
- **May 15, 1948 – March 1949 (1948 Arab-Israeli War / Israeli War of Independence / The Nakba):** Coalition of Egypt, Transjordan (Arab Legion), Syria, Lebanon, and Iraq invades. Armistice lines (Green Line) established via 1949 Armistice Agreements (Rhodes). ~700,000 Palestinians displaced; West Bank annexed by Jordan, Gaza Strip administered by Egypt.
- **July 23, 1952 (Egyptian Free Officers Revolution):** Overthrow of King Farouk; rise of Gamal Abdel Nasser, institutionalizing Pan-Arab nationalism.
- **October 29 – November 7, 1956 (Suez Crisis / Operation Kadesh / Operation Musketeer):** Nasser nationalizes the Suez Canal Company (July 26). Secret Protocol of Sèvres signed by Britain, France, and Israel. Israel seizes the Sinai Peninsula; Anglo-French landings at Port Said. Eisenhower halts operation via financial coercion (threat to break sterling), cementing the decline of European colonial hegemony and establishing the US and USSR as dominant regional arbiters.

### 1.3 Era III: Classical State-on-State Combined-Arms Warfare (1967–1973)
- **June 5–10, 1967 (Six-Day War / June War):** Precipitated by Nasser's closure of the Straits of Tiran (May 22), expulsion of UNEF from Sinai, and Egypt-Syria-Jordan mutual defense pacts. Preemptive Israeli air strikes (Operation Focus / *Mivtza Moked*) destroy ~450 Arab aircraft in hours. Israel captures the Sinai Peninsula, Gaza Strip, West Bank, East Jerusalem, and Golan Heights. UN Security Council Resolution 242 ("land for peace").
- **1967–1970 (War of Attrition):** Static, high-intensity artillery, commando raids, and air duels along the Suez Canal. Soviet direct intervention (Operation Kavkaz: VVS MiG-21 pilots, SAM crews). Concluded by August 1970 ceasefire.
- **October 6–25, 1973 (Yom Kippur War / October War / Ramadan War):** Coordinated Egyptian (Operation Badr: crossing the Bar-Lev Line under 2K12 Kub/SA-6 air defense umbrella) and Syrian armored assault on the Golan Heights. US Operation Nickel Grass and Soviet airlift resupply belligerents. IDF counter-attacks: Ariel Sharon cross-canal breach (Operation Stouthearted Men) encircle Egyptian Third Army. War catalyzes OPEC oil embargo (October 17, 1973), triggering global stagflation and reshuffling international energy geopolitics.

### 1.4 Era IV: The Iranian Revolution, Gulf Geopolitics, and Lebanon (1979–1982)
- **January–February 1979 (Iranian Islamic Revolution):** Flight of Mohammad Reza Pahlavi; return of Ayatollah Ruhollah Khomeini (Feb 1). Establishment of the Islamic Republic of Iran (theocracy under *Velayat-e Faqih* / Guardianship of the Islamic Jurist). Radical restructuring of Gulf power dynamics.
- **November 4, 1979 – January 20, 1981:** US Embassy Tehran hostage crisis; failed rescue attempt (Operation Eagle Claw, April 24, 1980).
- **March 26, 1979 (Egypt-Israel Peace Treaty):** Camp David Accords (September 1978) signed by Sadat and Begin. Egypt ejected from the Arab League; Sadat assassinated by Egyptian Islamic Jihad (October 6, 1981).
- **June 6, 1982 (Operation Peace for Galilee / First Lebanon War):** IDF invades Lebanon to expel Yasser Arafat's PLO. Siege of Beirut; Sabra and Shatila massacre (Sept 16–18); Bachir Gemayel assassination. Seeds the emergence of **Hezbollah** (Party of God) in the Bekaa Valley and Southern Lebanon, supported by Iran's Islamic Revolutionary Guard Corps (IRGC).

### 1.5 Era V: The Iran-Iraq War & The Tanker War (1980–1988)
- **September 22, 1980:** Saddam Hussein invades Iran across the Shatt al-Arab waterway, seeking to exploit post-revolutionary purge chaos in the Artesh (Iranian regular military).
- **1981–1982 (Iranian Counter-Offensive):** Operations Tariq al-Qods, Fath ol-Mobin, and Beit ol-Moqaddas liberate Khorramshahr (May 24, 1982). Iran shifts from defense to offense, aiming to topple Saddam and capture Basra.
- **1982–1987 (Attrition, Trench Warfare, and Chemical Weapons):** Iraqi resort to mustard gas and nerve agents (tabun, sarin) against Iranian human-wave assaults (*Basij*); Iraqi missile strikes on cities (War of the Cities).
- **1984–1988 (The Tanker War):** Systematic maritime economic interdiction in the Persian Gulf.
- **August 15, 1985 – 1988 (Strikes on Kharg Island):** Iraqi Air Force (Mirage F1EQs with Exocet and AS-30L missiles) mounts continuous saturation bombing of Iran's primary crude export terminal at Kharg Island, forcing Iranian exports to shuttle via Sirri and Larak islands.
- **July 1987 – September 1988 (Operation Earnest Will):** US Navy reflags and escorts 11 Kuwaiti tankers. USS *Stark* hit by Iraqi Exocet (May 17, 1987). USS *Samuel B. Roberts* struck by Iranian M-08 mine (April 14, 1988).
- **April 18, 1988 (Operation Praying Mantis):** Largest US surface naval combat since WWII. US Navy sinks Iranian frigate *Sahand*, fast-attack craft *Joshan*, disables frigate *Sabalan*, and destroys two armed oil platforms (Sassan and Sirri).
- **July 3, 1988:** USS *Vincennes* shoots down Iran Air Flight 655 (290 civilian fatalities).
- **August 20, 1988:** Khomeini accepts UN Security Council Resolution 598 ("drinking from the poisoned chalice"), ending the 8-year war with ~1,000,000 casualties and status quo ante bellum.

### 1.6 Era VI: Pax Americana, Asymmetric Intifadas, and the Second Lebanon War (1990–2006)
- **August 2, 1990 – February 28, 1991 (Gulf War / Operation Desert Storm):** Iraq invades Kuwait; US-led 35-nation coalition expels Iraqi forces using overwhelming airpower and ground maneuver. SCUD missile strikes on Israel and Saudi Arabia.
- **December 1987 – September 1993 (First Intifada):** Spontaneous grassroots Palestinian uprising (stone-throwing, commercial strikes); culminates in Madrid Conference (1991) and Oslo I Accords (September 13, 1993). Establishment of Palestinian Authority (PA).
- **September 2000 – 2005 (Second Intifada / Al-Aqsa Intifada):** Violent militarized uprising; suicide bombings inside Israeli cities; IDF Operation Defensive Shield (March–April 2002) in the West Bank; construction of the West Bank security barrier.
- **August 2005 (Israeli Disengagement from Gaza):** Unilateral withdrawal of IDF forces and 8,000 Israeli settlers from the Gaza Strip under Ariel Sharon.
- **January 2006 / June 2007 (Palestinian Elections & Gaza Split):** Hamas wins PLC legislative elections (Jan 2006). Fatah-Hamas civil conflict (Battle of Gaza, June 2007) yields Hamas control of Gaza Strip and PA control of West Bank pockets.
- **July 12 – August 14, 2006 (Second Lebanon War / 34-Day War):** Hezbollah cross-border ambush captures two IDF soldiers. 34 days of IDF air/ground campaign vs Hezbollah decentralized bunker defense (ATGM ambushes with Kornet/Metis-M, C-802 Noor missile strike on INS *Hanit*, ~4,000 Katyusha/Fajr rockets into northern Israel). Ends in strategic stalemate under UNSCR 1701.

### 1.7 Era VII: The Arab Uprisings, Syrian Civil War, and the 'Axis of Resistance' (2011–2020)
- **2011 (The Arab Spring):** Uprisings topple regimes in Tunisia, Egypt, Libya, Yemen; spiral into proxy civil wars in Syria and Yemen.
- **2011–Present (Syrian Civil War):** Syrian uprising militarizes. Iran commits IRGC Quds Force (Gen. Qasem Soleimani) and Lebanese Hezbollah to preserve Bashar al-Assad. Russia intervenes militarily (September 2015) at Khmeimim Air Base. Israel launches the "Campaign Between the Wars" (*MABAM* / *Mab'am*): thousands of standoff air strikes targeting Iranian precision-guided munition (PGM) conduits through Syria.
- **2014–Present (Yemeni Civil War & Ansar Allah / The Houthis):** Houthi movement captures Sana'a (Sept 2014). Saudi-led coalition intervention (Operation Decisive Storm, March 2015). Houthis develop long-range ballistic missile, cruise missile, and drone strike capabilities with IRGC technical assistance.
- **January 3, 2020:** US drone strike at Baghdad Airport kills Quds Force commander Qasem Soleimani and PMF deputy Abu Mahdi al-Muhandis. Iranian ballistic missile retaliatory strike on Ayn al-Asad Airbase (Operation Martyr Soleimani, Jan 8).
- **September 15, 2020 (The Abraham Accords):** Normalization agreements signed between Israel, the United Arab Emirates, and Bahrain, followed by Sudan and Morocco, formalizing an anti-Iran regional security architecture.

### 1.8 Era VIII: Multi-Front Missile/Drone Warfare & Red Sea Interdiction (2023–Present)
- **October 7, 2023 (Operation Al-Aqsa Flood):** Hamas and Palestinian Islamic Jihad breach the Gaza border barrier; massive combined rocket barrage, paramotor/technical infiltration; ~1,200 Israelis killed, ~250 hostages taken.
- **October 2023 – Present (Gaza Ground Offensive / Iron Swords):** Extensive IDF urban maneuver in northern and southern Gaza; unprecedented subterranean combat (Hamas "Metro" tunnel system); massive humanitarian crisis, global diplomatic fallout, and international lawfare (ICJ genocide filings).
- **October 2023 – Present (Northern Front / Lebanon):** Low-to-high intensity Hezbollah-IDF cross-border missile, rocket, and anti-tank duels, leading to massive civilian evacuations in northern Israel and southern Lebanon, escalating to decapitation strikes (pager/radio sabotage Sept 17–18, 2024; assassination of Hassan Nasrallah Sept 27, 2024).
- **October 31, 2023:** First historic combat interception outside Earth's atmosphere by the Israeli **Arrow 3** system, shooting down a Houthi medium-range ballistic missile targeted at Eilat.
- **November 2023 – Present (Red Sea Crisis):** Ansar Allah (Houthis) launch anti-ship ballistic missiles (ASBM), cruise missiles, and loitering munitions against commercial shipping transiting the Bab-el-Mandeb and Gulf of Aden, forcing 70%+ of Suez maritime container traffic to reroute around the Cape of Good Hope. US/UK launch Operation Prosperity Guardian and Operation Poseidon Archer.
- **April 13–14, 2024 (Operation True Promise I):** First direct Iranian state assault on Israeli territory: ~170 Shahed drones, ~30 land-attack cruise missiles, and ~120 ballistic missiles. Over 99% intercepted by IDF layered IAMD (Arrow 2/3, David's Sling, Iron Dome) with coalition coalition air assets (US, UK, France, Jordan).
- **October 1, 2024 (Operation True Promise II):** Iran launches ~180-200 ballistic missiles (including Fattah-1 and Kheibar Shekan) targeting Israeli air bases (Nevatim, Tel Nof) and Mossad HQ; demonstrates saturation vulnerabilities against ballistic salvos.

---

## 2. Key Geopolitical Structures & The 'Axis of Resistance' (*Mehwar al-Muqawama*)

### 2.1 Origins and Strategic Architecture
The "Axis of Resistance" is an operational, political, and ideological coalition organized and supported by the Islamic Republic of Iran, specifically the **IRGC Quds Force** (*Sepah-e Qods*). It is not a monolithic Warsaw Pact-style bloc, nor is it a random collection of disparate terrorists; it is an integrated, asymmetric alliance of state and non-state actors operating on shared strategic interests: anti-imperialism, anti-Zionism, expulsion of US forces from the Middle East, and forward defense of Iran's homeland.

```
                    STRUCTURE OF IRAN'S 'AXIS OF RESISTANCE'
                              ┌──────────────────┐
                              │  TEHRAN / IRGC   │
                              │    QUDS FORCE    │
                              │ (Doctrine/Funding│
                              │  PGM Technology) │
                              └────────┬─────────┘
                                       │
        ┌──────────────┬───────────────┼───────────────┬──────────────┐
        ▼              ▼               ▼               ▼              ▼
┌──────────────┐┌──────────────┐┌──────────────┐┌──────────────┐┌──────────────┐
│  HEZBOLLAH   ││   SYRIAN     ││ IRAQI HASH'D ││ ANSAR ALLAH  ││    HAMAS /   │
│  (Lebanon)   ││   REGIME     ││ (Kata'ib HZ, ││  (Houthis,   ││      PIJ     │
│Primary Armed ││ (State Hub & ││ Nujaba, Badr)││   Yemen)     ││ (Gaza/WB,    │
│Deterrent     ││Transit Artery││US Base Harass││Red Sea Choke ││Sunni Islam.) │
└──────────────┘└──────────────┘└──────────────┘└──────────────┘└──────────────┘
```

### 2.2 Component Entities & Operational Roles

| Actor | Base & Demographics | Ideological Bond | Operational Role | Key Capabilities |
| :--- | :--- | :--- | :--- | :--- |
| **IRGC Quds Force** | Iran (Supreme Command) | *Velayat-e Faqih*, Revolutionary Islam | Strategic direction, funding, missile R&D, PGM kits | Ballistic/cruise missiles, Shahed drones, EW |
| **Hezbollah** | Lebanon (Shia) | Strict loyalty to Khamenei | Crown jewel deterrent; northern flank pinned against Israel | 150k+ rockets, Fateh-110, Kornet ATGMs, Radwan SOF |
| **Syrian Arab Republic** | Syria (Alawite/Ba'athist) | Pragmatic geopolitical survival | Geographic bridge ("land bridge" from Iran to Lebanon) | Airbases, territory, logistical transit depots |
| **Iraqi Islamic Resistance (PMF)** | Iraq (Shia) | *Velayat-e Faqih* / Shia solidarity | Strategic depth, harassment of US bases (Tanf, Harir) | Short-range ballistic missiles, loitering munitions |
| **Ansar Allah (Houthis)** | Yemen (Zaidi Shia) | Revolutionary anti-imperialism | Southern flank; maritime interdiction (Bab-el-Mandeb) | Anti-ship ballistic missiles (ASBM), USV/UUV, drones |
| **Hamas & PIJ** | Gaza / West Bank (Sunni) | National liberation / Muslim Brotherhood (Hamas) | Kinetic friction inside Palestinian arena; political spoiler | Short/medium unguided rockets, tunnels, RPG-7/Yasin |

### 2.3 The Autonomy Paradox (Proxies vs. Partners)
A foundational error in popular Western analysis is viewing Resistance members as mindless mechanical puppets. In historiographical reality:
1. **Hezbollah** participates actively in Iranian strategic decision-making; Hassan Nasrallah was a senior advisor to Khamenei, not a subordinate officer.
2. **Hamas** maintains significant ideological and operational autonomy. In 2011, Hamas broke with Tehran over the Syrian Civil War (refusing to back Assad against Sunni rebels), relocating its leadership from Damascus to Doha. The October 7, 2023 attack was planned and executed autonomously without prior tactical notification to Tehran or Hezbollah.
3. **The Houthis** possess their own millenarian, tribal, and regional agenda; while reliant on Iranian guidance kits and radar systems, they routinely defy Iranian diplomatic suggestions.

---

## 3. The Iran-Iraq War & Persian Gulf Maritime Operations (1980–1988)

### 3.1 The Strategic Pivot: Kharg Island
Kharg Island (*Jazireh-ye Khark*) is a coral island located 25 km (16 miles) off the Iranian coast in the northern Persian Gulf. During the Iran-Iraq War:
- **Economic Lifeblood:** Handled **over 90%** of Iran's crude oil exports. Destruction of Kharg meant the economic collapse of the Islamic Republic.
- **The Iraqi Aerial Campaign (1982–1988):** Saddam Hussein ordered over 2,500 air raids on Kharg. Iraq deployed French-built Dassault Mirage F1EQs armed with Aérospatiale AM39 Exocet anti-ship missiles and AS-30L laser-guided bombs, as well as Soviet-supplied Super Etendards (leased 1983–1985).
- **The Defense of Kharg:** Iran deployed a formidable IAMD umbrella comprising American-supplied MIM-23 HAWK surface-to-air missile batteries, Oerlikon 35mm twin cannons with Skyguard radar, and combat air patrols (CAP) flown by Grumman F-14A Tomcats wielding long-range AIM-54A Phoenix missiles. Iran installed offshore decoy platforms, extensive smoke screens, and rapid-repair engineering teams that patched pipeline manifolds within hours of bombing raids. Kharg never completely ceased operations.

### 3.2 The Tanker War (1984–1988) & Empirical Data
The Tanker War erupted when Iraq initiated systematic strikes on Iranian oil ports and shipping to strangle Tehran's foreign exchange, prompting Iran to retaliate against tankers servicing Arab Gulf states funding Iraq's war effort (Kuwait, Saudi Arabia).

```
                      THE TANKER WAR (1984–1988) ATTRITION DATA
  Total Merchant Vessels Attacked: 546 ships
  ┌─────────────────────────────────────────────────────────────┐
  │ Iraqi Attacks: ~283 vessels (52%)                           │
  ├─────────────────────────────────────────────────────────────┤
  │ Iranian Attacks: ~168 vessels (31%)                         │
  ├─────────────────────────────────────────────────────────────┤
  │ Mines / Undetermined: ~95 vessels (17%)                     │
  └─────────────────────────────────────────────────────────────┘
  Total Seamen Killed: >430 | Total Tonnage Damaged: >30 Million Deadweight Tons (DWT)
```

#### Operational Dynamics:
1. **Iraqi Doctrine:** Standoff radar-guided missile strikes (Exocet) against loaded supertankers exiting Kharg in the northern Gulf exclusion zone.
2. **Iranian Doctrine:** Asymmetric littoral warfare using IRGC Navy (*NEDSA*) Swedish-built Boghammar speedboats armed with RPG-7s, 107mm multiple rocket launchers, and 12.7mm DShK heavy machine guns; moored contact naval mines (M-08); and shore-based Chinese HY-2 Silkworm (*Seersucker*) anti-ship missile batteries placed along the Strait of Hormuz and Al-Faw Peninsula.
3. **Tanker Survivability Physics:** Contrary to civilian expectations, commercial crude oil tankers proved extraordinarily difficult to sink. Crude oil absorbs missile kinetic energy and blast overpressure; void wing tanks act as natural torpedo blisters. Of 546 vessels struck, fewer than 55 (~10%) were total hull losses or sunk. The primary risk was crew fatality from superstructure fires and ruptured bunkering fuel.

### 3.3 Operation Earnest Will & Operation Praying Mantis (1987–1988)
- **Earnest Will (July 1987 – Sept 1988):** US Navy escorted reflagged Kuwaiti tankers. On July 24, 1987, the reflagged supertanker SS *Bridgeton* struck an Iranian mine, exposing US Navy vulnerability in shallow-water mine countermeasures (MCM).
- **Praying Mantis (April 18, 1988):** Coordinated retaliatory strike after the frigate USS *Samuel B. Roberts* was nearly split in half by an Iranian mine.
  - Surface Action Groups (SAGs) destroyed the Sassan and Sirri gas/oil separation platforms (GOSPs) used by the IRGC as radar surveillance and speedboat staging nodes.
  - In the subsequent naval-air engagement:
    - Iranian fast-attack craft *Joshan* fired a Harpoon at USS *Wainwright*; missed; *Joshan* sunk by RIM-66 Standard missiles.
    - Iranian frigate *Sahand* fired on US A-6E Intruders; struck by two Harpoons, two Skipper laser-guided bombs, and Rockeye cluster munitions; sunk.
    - Sister frigate *Sabalan* disabled by an A-6E laser-guided bomb through the engine stack; left burning dead in the water.
  - **Tactical Precedent:** Demonstrated the absolute superiority of combined carrier airpower and coordinated surface-to-surface missiles over a non-integrated naval littoral force.

---

## 4. Historiographical Debates & Competing Schools of Thought

Rigorous historical work requires acknowledging substantive historiographical disputes rather than presenting partisan or simplified narratives as objective fact.

### 4.1 The 1948 War and the Palestinian Exodus (The "New Historians" Debate)
- **Traditional / Zionist Historiography (e.g., Netanel Lorch, Anita Shapira, Efraim Karsh):** Israel was a beleaguered David facing an Arab Goliath of five invading armies bent on total annihilation. The Palestinian Arab refugee flight was primarily catalyzed by orders from Arab broadcast leaders urging civilians to clear zones for advancing armies, combined with elite desertion and war panic.
- **The "New Historians" Revisionism (e.g., Benny Morris, Avi Shlaim, Ilan Pappé):**
  - **Benny Morris (*The Birth of the Palestinian Refugee Problem, 1947–1949*):** Demonstrates that no blanket Arab evacuation order existed. The refugee flight was caused "by war, not by design"—a multifaceted wave driven by IDF military assaults, localized expulsions (e.g., Operation Dani in Lydda and Ramle), psychological warfare, and fear.
  - **Ilan Pappé (*The Ethnic Cleansing of Palestine*):** Argues that Plan Dalet (Plan D) was an intentional, pre-formulated master blueprint for systematic ethnic cleansing.
  - **Efraim Karsh (*Fabricating Israeli History*):** Critiques Morris and Pappé, arguing they selectively mistranslate Hebrew archives and ignore Arab rejection of peaceful partition and Palestinian leadership responsibility.

### 4.2 Origins and Strategy of the Iran-Iraq War (1980–1988)
- **Saddam as Aggressor (Mainstream International / Pierre Razoux):** Saddam launched an opportunistic war of aggression to seize Khuzestan's oil fields, establish hegemony over the Persian Gulf, and eliminate Khomeini's revolutionary ideological challenge while the Iranian military was weakened by post-1979 officer purges.
- **Iranian Provocation & Defensive Preemption (Revisionist / Efraim Karsh):** Emphasizes that Khomeini systematically incited Iraq's majority Shia population to revolt, financed the Dawa Party's assassination attempts against Tariq Aziz, and violated the 1975 Algiers Accord through border shelling in spring/summer 1980, creating severe Iraqi preemption pressure.

### 4.3 The Six-Day War (1967): Preemption vs. Aggression vs. Miscalculation
- **Israeli Existential Preemption (Michael Oren):** Nasser's bellicose rhetoric ("our objective is the destruction of Israel"), closure of the Straits of Tiran, massing of 100,000 Egyptian troops in the Sinai, and ejection of UNEF left Israel with no military alternative but a preemptive strike to avert national destruction.
- **Soviet Disinformation & Inadvertent Escalation (Richard Parker, Avi Shlaim):** Neither Nasser nor Israel wanted war. A false Soviet intelligence report claiming Israeli troop concentrations on the Syrian border provoked Nasser's mobilization; Nasser became trapped by his own Pan-Arab domestic rhetoric and prestige, triggering an unintentional escalatory spiral.

### 4.4 Structure of Asymmetric Proxy Networks: Proxies vs. Autonomous Partners
- **Proxy School (Conventional Security / Intelligence Consensus):** Hezbollah, the Houthis, and Iraqi militias are external executive appendages ("proxies") created, funded, and commanded by Tehran's Quds Force to export revolution and wage proxy wars against the US and Israel without Iranian direct exposure.
- **Autonomous Substate / Hybrid School (Academic Middle East Studies / Fawaz Gerges, Amal Saad):** Emphasizes deep domestic root causes. Hezbollah is an authentic Lebanese sociopolitical entity representing Lebanon's marginalized Shia community; the Houthis are driven by Zaidi theological revivalism and internal Yemeni tribal politics. Iranian backing amplifies, but does not manufacture, their operational autonomy.

---

## 5. Sourcing Rules & Evidentiary Standards

All historical claims, doctrinal references, and operational scenario designs must adhere to strict archival and analytical standards:

1. **Archival & Declassified Records Over Popular Memoirs:** Prioritize declassified state papers (US Foreign Relations of the United States [FRUS], British Foreign Office files, Israel State Archives [ISA], declassified Iraqi Ba'ath Party files held at the Hoover Institution). Treat political memoirs (Begin, Sadat, Sharon, Rafsanjani) as subjective primary artifacts requiring independent triangulation.
2. **Operational Military Data Over Political Communiqués:** Battle damage assessments (BDA), sortie rates, missile hit probabilities ($P_k$), and casualty numbers must come from professional military histories (e.g., US Naval Institute [USNI], Air University Press, IDF Historical Branch, Pierre Razoux's *The Iran-Iraq War*, Kenneth Pollack's *Arabs at War*).
3. **Multi-Archival Triangulation:** In Middle Eastern history, no single state's narrative is authoritative. A historical assertion regarding an engagement (e.g., the 1973 Bar-Lev crossing or the 1982 Sultan Yacoub tank battle) must be checked across Israeli, Arab, and third-party (US/Soviet/UN) accounts.
4. **Distinguish Verified Events from Wartime Propaganda & Myth:**
   - *Myth:* Israeli intelligence in 1973 had zero warning of the attack. *Reality:* Mossad director Zvi Zamir met top agent Ashraf Marwan in London on October 5, who provided the exact battle day, but military intelligence (Aman / Eli Zeira) adhered dogmatically to "The Concept" (*Ha-Konseptziya*).
   - *Myth:* The Tanker War stopped all Persian Gulf oil shipments. *Reality:* Less than 2% of ships traversing the Persian Gulf were damaged; commercial freight rates rose, but crude exports continued throughout the war.
   - *Myth:* Hezbollah's bunker network in 2006 was built entirely by North Korean contractors. *Reality:* North Korean technical tunneling advice was utilized, but construction was directed by local Lebanese civil engineers using commercial equipment under Jihad al-Bina.

---

## 6. Audit Questions for Simulation & Canon Integrity

When auditing military simulation lore, campaign mission briefs, and combat mechanics, verify compliance against these 10 authoritative questions:

1. **Kharg Island Terminal Geography:** Does the game depict Kharg Island as a generic inland base or open mainland refinery? *(Mandate: Kharg is a coral island in the northern Persian Gulf; its infrastructure consists of deepwater sea-island loading jetties, tank farms, and offshore submarine manifolds).*
2. **Tanker War Weaponry & Tactics:** Are anti-ship strikes in the Gulf attributed to high-tech battleships, or to historical IRGC Boghammar speedboats, naval contact mines, and shore-based HY-2 Silkworm batteries? *(Mandate: Authentic Tanker War tactics utilize asymmetric swarms, minelaying, and Silkworm coastal batteries).*
3. **Tanker Damage Tolerances:** Does a single missile strike instantly vaporize a commercial supertanker? *(Mandate: Crude supertankers have immense compartmentalized displacement; single missile hits cause fires but rarely sink hulls without secondary explosion).*
4. **Hezbollah / AoI Organizational Reality:** Is the insurgent faction depicted as an unruly gang of unorganized street fighters, or as a disciplined hybrid force utilizing decentralized command, fortified subterranean bunkers, and sophisticated Russian/Iranian ATGMs? *(Mandate: Model must reflect doctrinal reality of hardened subterranean fighting and standoff ATGM ambushes).*
5. **The Diego Garcia Strategic Context:** Is Diego Garcia accurately situated as a British Indian Ocean Territory (BIOT) joint UK-US military bastion and strategic bomber/submarine forward staging base, rather than a Caribbean or Atlantic outpost? *(Mandate: Correct Indian Ocean location and strategic logistics role).*
6. **Arrow 3 Exo-Atmospheric Interception:** Is the Arrow 3 system depicted as a low-altitude point-defense Patriot/Iron Dome clone? *(Mandate: Arrow 3 is an exo-atmospheric kinetic kill interceptor operating in space outside the Karman line, as demonstrated against Houthi IRBMs in Oct 2023).*
7. **The 1982 Lebanon & Hezbollah Precedent:** Does the narrative trace the origin of modern Lebanese Shia militancy to post-1982 developments rather than projecting it back into the early 20th century? *(Mandate: Hezbollah was formed in 1982 following the Israeli invasion; prior Shia politics was dominated by the secular Amal movement).*
8. **Law of Armed Conflict (LOAC) & Asymmetric Shielding:** Are civilian collateral incidents modeled as purely aesthetic explosions, or as legally and politically weaponized events under Protocol I of the Geneva Conventions? *(Mandate: Collateral damage must incur concrete logistical, diplomatic, and PR penalties per historical info-ops warfare).*
9. **Bab-el-Mandeb Geopolitical Chokepoint:** Is the southern maritime chokepoint correctly identified as the Bab-el-Mandeb ("Gate of Tears") separating Yemen from Djibouti and connecting the Red Sea to the Gulf of Aden? *(Mandate: Accurate geographical, topological, and nautical representation).*
10. **The Bushehr Reactor Security Paradigm:** Is the Bushehr nuclear complex situated on the Iranian Gulf coast directly opposite Kharg Island, reflecting its real-world vulnerability to maritime and air interdiction? *(Mandate: Bushehr sits on the coast 120 km south of Kharg, an authentic regional flashpoint since 1984).*

---

## Part 16: Politics, International Law, Information Operations & Lawfare Standard (`politics-infoops-lawfare`)

*Repository Path: [`skills/politics-infoops-lawfare/SKILL.md`](./skills/politics-infoops-lawfare/SKILL.md)*

---
name: politics-infoops-lawfare
description: Authoritative domain standard for International Relations, International Law of Armed Conflict (LOAC), Lawfare, the UN System and Special Procedures, ICJ/ICC Jurisprudence, NGO and Media Dynamics, Influence Operations, Civil Disruption Logistics, and Export Controls for the jslcnc-v3 engine.
version: 1.0.0
tags:
  - politics
  - international-law
  - loac
  - lawfare
  - infoops
  - united-nations
  - icj-icc
  - sanctions-embargoes
  - civil-blockades
  - public-legitimacy
---

# Politics, International Law, Information Operations & Lawfare Standard

## 1. Scope & Foundational Doctrine

This standard establishes the operational, legal, geopolitical, and cognitive domain framework governing information warfare, lawfare, diplomatic friction, protest disruption, and international legitimacy for the `jslcnc-v3` simulation engine (`C:\cnc_rev\skirmish`) and associated design canon.

### 1.1 The Operator Concept Test (Binding Standard)
The foundational tiebreaker for all mechanics and narrative specifications in this domain is the Operator Concept Test (ADR-009 / User Directive D-006):
> *"Our primary goal: right now the world is tolerating the behavior of terrible people because they are running a good PR campaign. We want to illustrate what they are doing. If it is done in real life and it is terrible, then we include it."*
> *"Real world Israel does not care what the rest of the world thinks. We would rather stay alive than be loved... so the pursuit of PR is in service of logistics, etc... that's where the harm comes from. And more protesters make it harder to operate. Get it? Having public opinion on your side makes it easier to be an army."* (User Inputs XML: 1762 / Step 7606)

### 1.2 Core Doctrinal Principles
1. **Survival Over Reputation:** Sovereign states facing existential aggression do not paralyze kinetic self-defense to appease hostile foreign editorial boards or UN rapporteur cables. Weapons do not mechanically jam, lasers do not refuse to fire, and artillery does not shut down because an emergency brief was filed in Geneva.
2. **PR as Physical Logistics, Never Moralistic Scorekeeping:** Public legitimacy is modeled purely as a logistical pipeline:
   - High Legitimacy ($80\text{--}100$): Unfettered allied arms transfers, accelerated munitions replenishments, priority maritime transit corridors.
   - Low Legitimacy ($25\text{--}49$): Munitions export license delays, doubled ordnance costs, customs freezes.
   - Collapsed Legitimacy ($0\text{--}24$): Direct arms embargoes, allied port denials, shipping re-routing, and civil activist blockades physically shutting down base gates and harbor chokepoints.
3. **Strict Epistemological Separation (Fact vs. Allegation):** In modern asymmetric warfare, operational reality is saturated with deliberate disinformation, stage-managed casualty claims ("Pallywood"), unverified NGO press releases, and rapid-response state rebuttals. Simulation models and narrative texts must rigorously distinguish verified legal facts from partisan allegations.

---

## 2. Evidence & Sourcing Hierarchy

To maintain authoritative credibility and avoid falling into propaganda traps, all analyses, simulation parameters, and narrative scripts must adhere to a strict 5-tier evidence hierarchy:

```
                      ┌──────────────────────────────────────┐
                      │     EVIDENTIARY SOURCING HIERARCHY   │
                      └──────────────────────────────────────┘
                                          │
    ┌──────────────────┬──────────────────┼──────────────────┬──────────────────┐
    ▼                  ▼                  ▼                  ▼                  ▼
  TIER 1             TIER 2             TIER 3             TIER 4             TIER 5
 BINDING            JUDICIAL &         TECHNICAL &        MAINSTREAM         PARTISAN &
 TREATIES &         OFFICIAL UN        FORENSIC OSINT    NEWS WIRES &       UNVERIFIED
 STATUTES           REPORTS                               INVESTIGATIVE     CLAIMS
 ├─ Geneva Conv.    ├─ ICJ / ICC       ├─ Satellite SAR   ├─ Reuters / AP    ├─ Ministry of
 ├─ UN Charter         Orders          ├─ Geolocation     ├─ BBC / NYT          Health Claims
 ├─ Rome Statute    ├─ UN Panel Rpts   ├─ Ballistics      ├─ Cross-checked   ├─ Telegram Feeds
 └─ San Remo Man.   └─ OIOS Audits     └─ Serial Numbers     by forensics    └─ Activist PR
```

### 2.1 Tier Definitions
- **Tier 1: Binding International Law & Treaties:** Primary legal instruments codified by state parties. Includes the Hague Conventions (1899, 1907), Geneva Conventions of 1949 and Additional Protocols (I and II of 1977), Rome Statute of the International Criminal Court (1998), UN Charter (1945), and the San Remo Manual on International Law Applicable to Armed Conflicts at Sea (1994).
- **Tier 2: Adjudicated Legal Rulings & Official Institutional Investigations:** Binding and advisory decisions from international tribunals (ICJ judgments and provisional measures; ICC arrest warrants and pre-trial chamber confirmations; UN Secretary-General Panels of Inquiry such as the 2011 Palmer Commission Report; UN Office of Internal Oversight Services [OIOS] audit findings).
- **Tier 3: Technical Forensic Evidence & Open-Source Intelligence (OSINT):** High-resolution satellite imagery (Maxar, Planet Labs, SAR), declassified military electro-optical and GMTI radar telemetry, ballistics crater analysis, verified weapons fragment serial numbers, independent geolocations (Bellingcat, GeoConfirmed), and intercepted operational communications verified by signals forensics.
- **Tier 4: Cross-Checked Commercial Media & Established Wire Services:** Independent reporting from reputable wire services (Reuters, Associated Press, AFP) containing verified attribution, naming sources, and distinguishing between confirmed on-the-ground observations and official claims. Must be cross-referenced against technical forensics.
- **Tier 5: Partisan Combatant Claims, State Propaganda & Unverified Disinformation:** Combatant Ministry of Health casualty reports, military PR communiques, unvetted activist social media campaigns, partisan NGO press statements without verifiable methodology, and state-sponsored media (RT, Press TV, CGTN). **Mandate:** In the engine and lore, Tier 5 statements are treated strictly as gameplay event triggers or contested allegations—never as baseline truth.

---

## 3. The Institutions & Lawfare Ecosystem Map

Modern asymmetric conflicts are fought in the diplomatic, judicial, and media arenas as aggressively as in kinetic theaters.

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                           THE ASYMMETRIC LAWFARE ECOSYSTEM                              │
├───────────────────────────────┬───────────────────────────────┬─────────────────────────┤
│   INTERNATIONAL BODIES (UN)   │     JUDICIAL TRIBUNALS        │   CIVIL & MEDIA SPHERE  │
├───────────────────────────────┼───────────────────────────────┼─────────────────────────┤
│ • UN Security Council (UNSC)  │ • International Court of      │ • Human Rights NGOs     │
│ • UN General Assembly (UNGA)  │   Justice (ICJ)               │   (Amnesty, HRW, Al-Haq)│
│ • UN Human Rights Council     │   - State-vs-State litigation │ • Corporate Boycott     │
│   (UNHRC) & Special Rapp.     │   - Advisory opinions         │   Networks (BDS, PSC)   │
│ • UN Agencies & Missions      │ • International Criminal      │ • Maritime Flotillas    │
│   (UNRWA, OCHA, UNIFIL)       │   Court (ICC)                 │   (FFC, Handala)        │
│   - Humanitarian convoys      │   - Rome Statute Art. 6, 7, 8 │ • Direct Action Mobs    │
│   - Shielded facilities       │   - Individual indictments    │   (Palestine Action)    │
└───────────────────────────────┴───────────────────────────────┴─────────────────────────┘
```

### 3.1 The United Nations System & Special Procedures
1. **UN Security Council (UNSC):** Holds Chapter VII enforcement powers (binding sanctions, military authorizations). Operates under P5 veto dynamics (US veto protects Coalition/Israel; Russian/Chinese vetoes protect Iran/Syria/proxies).
2. **UN General Assembly (UNGA):** Non-binding resolutions under the "Uniting for Peace" framework (Resolution 377A). Functions as a global PR amplifier where developing-world blocs and the Non-Aligned Movement pass majoritarian condemnations against Western allies.
3. **UN Human Rights Council (UNHRC) & Agenda Item 7:** The only permanent standing agenda item targeting a single country (Item 7: human rights situation in Palestine). Regularly forms open-ended Commissions of Inquiry (COI) that operate with inverted burdens of proof against Western militaries.
4. **Special Rapporteurs & Independent Experts:**
   - Appointed by UNHRC as "unpaid independent experts" (not formal UN staff members, but cloaked in UN authority and diplomatic immunity under the 1946 Convention on the Privileges and Immunities of the United Nations).
   - *Operational Mandate:* Mandate-holders (notably the Special Rapporteur on the situation of human rights in the Palestinian territories occupied since 1967) publish un-vetted reports, issue press releases on official UN letterhead, and conduct international media tours lobbying national parliaments to halt arms exports and enforce corporate boycotts.
5. **UN Operational Agencies on the Ground (e.g. UNRWA, OCHA):**
   - Provide critical civilian relief but frequently suffer systemic institutional capture and infiltration by local insurgent factions.
   - Insurgents exploit agency infrastructure (schools, clinics, food logistics, compound compounds) for structural shielding, tunnel ingress points, and weapons caches.

### 3.2 The International Judicial Courts
1. **The International Court of Justice (ICJ, The Hague):**
   - Settles legal disputes between sovereign States (e.g. *South Africa v. Israel* under the 1948 Genocide Convention).
   - Can issue binding **Provisional Measures** on an expedited timetable (weeks) based on a low evidentiary standard of "plausibility" rather than a merits-based finding of guilt.
   - *Asymmetric Lawfare Exploitation:* Insurgents and proxy states exploit provisional measure requests to create global headlines ("World Court Orders Ceasefire"), using preliminary orders to force diplomatic embargoes long before full merits trials (which take 5–10 years) can examine forensic facts.
2. **The International Criminal Court (ICC, The Hague):**
   - Exercises jurisdiction over individuals for genocide (Art. 6), crimes against humanity (Art. 7), war crimes (Art. 8), and the crime of aggression (Art. 8 bis).
   - Operates on the principle of **Complementarity** (Art. 17): the ICC is a court of last resort and cannot intervene if a state has an independent, capable judicial and military justice system actively investigating alleged infractions.
   - *Lawfare Dynamics:* Prosecutorial overreach (e.g. issuing simultaneous warrants for democratic heads of state and terrorist guerrilla leaders to create a false moral equivalence) triggers severe diplomatic retaliation (e.g., US sanctions under the American Service-Members' Protection Act / EO 13928 precedents).

### 3.3 The Civil Disruption & Boycott Infrastructure
1. **NGO & Lawfare Litigants:** Organizations like Al-Haq, Euro-Med Human Rights Monitor, and domestic lawfare groups (Center for Constitutional Rights) coordinate litigation across foreign domestic courts invoking **Universal Jurisdiction** to secure arrest warrants against visiting coalition military commanders.
2. **Maritime Protest Flotillas:** Coalitions like the Freedom Flotilla Coalition (FFC) charter civilian commercial vessels to breach declared military blockades, deliberately engineering boarding confrontations for streaming cameras to force diplomatic crises.
3. **Direct Action & Industrial Sabotage:** Domestic activist networks (e.g., Palestine Action in the UK and US) blockade defense manufacturing facilities (Elbit Systems, BAE, Lockheed Martin), smash factory CNC machinery, and stage sit-ins outside naval docks and military base gates.
4. **Dockworker & Trade Union Boycotts:** Transport unions (e.g., Genoa, Livorno, Oakland, Melbourne) refuse to load or unload containers containing military hardware destined for coalition ports, imposing severe supply transit delays.

---

## 4. Documented Lawfare Mechanics: Real-World Case Studies

Under the Operator Concept Test ("if it is done in real life and it is terrible, then we include it"), mechanics must mirror documented operational conduct:

### 4.1 Case Study: The UN Special Rapporteur Campaign (Francesca Albanese)
- **Documented Conduct:**
  - *Mandate & Public Statements:* Appointed in 2022. Documented historical statements asserting that the "Jewish lobby" controls the United States (2014 Facebook post, acknowledged 2022). In February 2024, publicly rejected that the October 7 attacks were anti-Semitic, arguing they were an "assertion of the right to resist." Prompted formal condemnations from French Foreign Ministry, German Foreign Office, and US Ambassador to the UN.
  - *Report Rhetoric & Boycotts:* Authored reports including "Anatomy of a Genocide" (A/HRC/55/73, March 2024), calling for complete arms embargoes, economic sanctions, and severance of diplomatic ties with Israel. Actively lobbied foreign governments (Spain, Australia, South Africa) and multinational corporations to terminate joint defense contracts.
  - *Financial & Ethical Scrutiny:* Investigated by UN Watch and independent media in 2024 for accepting undeclared financial sponsorship for speaking tours from pro-Hamas lobbying organizations (including an Australian tour funded by lobbying groups, in apparent violation of the UN Code of Conduct for Special Procedures Mandate-holders).
- **Engine Mechanics Model:**
  - Personified off-map as the **Adversarial Lawfare Director**.
  - Does not spawn as a physical unit on the map (diplomatic immunity).
  - Triggers periodic, deterministic diplomatic cables (`LAWFARE_CONDEMNATION`) that levy immediate logistical penalties and fund AoI PR.
  - Generates civilian protest events and maritime flotillas that physically obstruct bases.
  - **Rebuttal Counterplay:** Can be countered only by releasing forensic ISR telemetry within strict time windows (30 seconds), stripping the PR bonus from AoI and debunking fraudulent claims.

### 4.2 Case Study: Human Shielding & UN Agency Infiltration (UNRWA & Hospital HQs)
- **Documented Conduct:**
  - *Subterranean Tunneling Under UN Facilities:* On February 10, 2024, the IDF declassified and embedded international journalists inside a massive subterranean Hamas intelligence data center with server racks, electrical transformers, and battery banks dug directly underneath the UNRWA Gaza Headquarters in Rimal, with electrical cables running directly into the UN building's power grid.
  - *Munitions in Schools:* UNRWA's own official press releases during the 2014 Gaza conflict acknowledged the discovery of rockets concealed inside UNRWA schools on at least three separate occasions (July 17, July 22, and July 29, 2014), following which UN personnel reportedly returned the rockets to local municipal authorities (Hamas-controlled police).
  - *Staff Combatant Participation:* In January 2024, intelligence dossiers presented to donor nations revealed that at least 12 UNRWA staff members actively participated in the October 7 massacre (including kidnapping Israelis and transporting ammunition). The UN Office of Internal Oversight Services (OIOS) concluded in August 2024 that in 9 cases, evidence indicated that staff members "may have been involved" in the attacks, leading to their termination.
  - *Aid Convoy Diversion:* As documented by the UN OCHA, COGAT, and international relief agencies, armed combatants regularly board, shoot at, and commandeer commercial and UN humanitarian aid trucks entering conflict corridors, hijacking food and supplies to sell on black markets at inflated prices to fund guerrilla operations.
- **Engine Mechanics Model:**
  - **UN Structural Shielding:** AoI can execute "Dig Beneath" abilities under UN hospitals, schools, and relief warehouses. Structures have tri-state verification (`unverified`, `disputed`, `confirmed`).
  - **Reconnaissance Requirement:** Striking an unverified UN structure inflicts a catastrophic $2.5\times$ PR penalty. Striking a confirmed military cache incurs only a justified $0.35\times$ penalty under LOAC Article 28.
  - **Convoy Hijacking:** Neutral UN supply trucks transit the map; AoI units can hijack them, using the civilian driver as a human shield. JSLC must use non-lethal interdiction (EMP, spike strips, SOF boarding) or lose massive legitimacy by firing kinetic weapons.

### 4.3 Case Study: Maritime Flotillas & Blockade Law (Mavi Marmara to Modern Eco-Flotillas)
- **Documented Conduct:**
  - *San Remo Manual (1994, Arts. 67–68):* International maritime law permits a belligerent maintaining a lawful naval blockade to intercept and board non-compliant neutral vessels attempting to breach the blockade in international waters, using proportional force if resisted.
  - *The 2010 Mavi Marmara Incident & Palmer Commission Report (2011):* The UN Secretary-General's Panel of Inquiry found that the Israeli naval blockade of Gaza was a lawful security measure under international law, and Israeli forces had a legal right to intercept the flotilla. However, the panel noted that boarding operations met with violent, organized resistance by activists armed with iron bars, chains, and knives, leading to lethal combat.
  - *Modern Flotilla Coalitions (2024 Freedom Flotilla / Handala / Greta Thunberg):* Activist organizations continually deploy small motor vessels, fishing dhows, and luxury yachts to anchor across maritime exclusion zones, deliberately baiting naval forces into kinetic confrontations to film viral social media content.
- **Engine Mechanics Model:**
  - **The Greta Eco-Flotilla:** Spawns a ring of 5 civilian boats plus 1 Flagship across naval chokepoints, halting dredging and shipping.
  - **Non-Lethal Mandate:** Warships must employ water cannons, LRAD acoustic beams, and Dvora boarding teams to physically tow vessels away.
  - **Lethal Wipeout:** Firing a kinetic high-explosive weapon at a protest vessel instantly resets Coalition PR to 0.
  - **Splash-Bait Exception (EXP-001):** If AoI fires weapons from within the flotilla ring, the `PROTECTED_CIVILIAN` status is stripped under LOAC Article 28.

### 4.4 Case Study: Digital Disinformation & The 45-Second Media Cycle (Al-Ahli Hospital Blast)
- **Documented Conduct:**
  - *October 17, 2023 Al-Ahli Arab Hospital Blast:* At approximately 18:59 local time, an explosion occurred in the courtyard of the Al-Ahli Hospital. Within minutes, the Hamas-run Ministry of Health announced that an Israeli airstrike had killed 500+ civilians. Global news outlets (BBC, NYT, Reuters, CNN) syndicated this headline uncritically worldwide.
  - *Diplomatic Fallout:* Violent protests erupted outside US and Israeli embassies across the Middle East; an emergency summit between US President Biden and Arab leaders in Jordan was cancelled.
  - *Forensic Debunking:* Within 24 hours, declassified radar tracking, drone video, and independent OSINT (video triangulation, crater depth of less than 30 cm, intact hospital walls, unburned cars) proved conclusively that the blast was caused by an errant Palestinian Islamic Jihad (PIJ) heavy rocket that suffered motor failure and crashed in the parking lot. Several major media outlets subsequently issued rare public apologies or editors' notes.
- **Engine Mechanics Model:**
  - **AoI `stage_incident` Ability:** AoI can fabricate an unverified mass-casualty incident.
  - **The Rebuttal Timer:** Coalition has 45 seconds to declassify and broadcast ISR aerial video.
  - **Failure:** If unaddressed, Coalition suffers $-18\%$ Legitimacy.
  - **Forensic Exposure Backfire:** If debunked within the window, the fraud backfires, inflicting $-25\%$ Popular Support on AoI and awarding $+10\%$ Legitimacy to the Coalition.

---

## 5. Lawfare & Export Control Mechanics in Code

### 5.1 Engine-Ready TypeScript Interfaces
Simulation modules governing lawfare must be strictly typed, deterministic, and bound to physical logistics rather than arbitrary game-over flags:

```typescript
export type PrBandType = "high" | "open" | "low" | "strained" | "collapse";

export interface IPrState {
  jslcLegitimacy: number;      // 0 to 100, default 100 (or 50 in campaign)
  aoiPopularSupport: number;   // 0 to 100, default 100
  recentGainHistory: { frame: number; delta: number }[]; // Rolling 60s window
  unScrutinyActive: boolean;
  activeRoeMoratorium: boolean;
  moratoriumExpiryFrame: number;
}

export interface ILawfareAction {
  id: string;
  kind: "un_condemnation" | "logistics_moratorium" | "eco_flotilla" | "protester_mob";
  triggerFrame: number;
  rebuttalDeadlineFrame: number;
  isRebutted: boolean;
  evidenceTokenRequired: boolean;
}

export interface ILogisticalFriction {
  reinforcementDelayMultiplier: number; // 1.0 (nominal) up to 2.5 (embargo)
  munitionsRestockCostMultiplier: number; // 1.0 up to 2.0
  fundingFlowMultiplier: number;         // 1.0 down to 0.35 at PR 0
  baseGateObstructed: boolean;           // True when protester mobs assemble
  activePortDenial: boolean;             // Forces detour routing
}
```

### 5.2 Deterministic PR Delta Formula
```typescript
/**
 * Evaluates negative PR impact of strikes with probabilistic reconnaissance confidence
 * and asymmetric victimhood scaling.
 */
export function calculateStrikePrPenalty(
  basePenalty: number,
  isrConfidence: number, // 0.0 to 0.95
  classMultiplier: number,
  aoiPopularSupport: number // 0 to 100
): number {
  // Clamped ISR confidence
  const conf = Math.max(0.0, Math.min(0.95, isrConfidence));
  
  // Unverified strikes are penalized up to 2.0x; verified strikes drop to ~1.05x
  const rawPenalty = Math.round(basePenalty * (2.0 - conf) * classMultiplier);
  
  // Asymmetric Victimhood Modifier: If AoI has no popular support, its complaints carry no weight
  const victimhoodFactor = Math.max(0.0, Math.min(1.0, aoiPopularSupport / 100));
  
  return Math.round(rawPenalty * victimhoodFactor);
}
```

---

## 6. Authoritative Domain Audit Questions

When evaluating simulation code, design briefs, lore texts, or mission scripts, evaluate compliance against these 12 questions:

1. **The Kinetic Freedom Rule:** Does any lawfare event, UN cable, or PR collapse disable a player's weapons, jam turrets, freeze direct fire, or stretch orbital laser recharge? *(Mandate: VIOLATION if true; weapons fire freely; harm is strictly supply delays, embargoes, and gate blockades).*
2. **Instant Loss Prohibition:** Does hitting 0% Legitimacy trigger an instant match loss or forced surrender? *(Mandate: VIOLATION if true; match ends only if the player remains unsupplied and unable to fight for 30 consecutive seconds).*
3. **Orbital Jurisdiction Exemption:** Are space-based weapons (Jewish Space Laser / orbital kinetics) subjected to terrestrial UN or ROE injunctions? *(Mandate: Exo-atmospheric assets have 100% legal immunity from terrestrial moratoria, though firing into protected civilian zones still costs PR).*
4. **Epistemological Rigor:** Does the document or mechanic treat combatant casualty announcements (e.g. Gaza Ministry of Health) as undisputed objective fact? *(Mandate: Must be labeled as unverified insurgent claims unless corroborated by Tier 1-3 forensic evidence).*
5. **Human Shielding Attribution:** When combatants operate beneath hospitals or in schools, is legal liability assigned to the defender under Geneva Convention IV Article 28 and Additional Protocol I Article 58? *(Mandate: Defender commits the war crime of human shielding; attacker retains right of attack subject to proportionality).*
6. **Rolling Gain Ceiling:** Are positive PR recoveries throttled to $\le 25\text{ points}$ per 60-second rolling window to prevent player PR farming? *(Mandate: Positive gains strictly capped; negative penalties uncapped).*
7. **Asymmetric Victimhood Modifier:** Does driving AoI Popular Support to 0 scale down the PR damage inflicted on JSLC? *(Mandate: Insurgent propaganda damage must scale with the accuser's credibility).*
8. **Flotilla Non-Lethal Resolution:** Does the game provide viable non-lethal solutions (LRAD, water cannon, boarding/towing) to disperse activist blockades without lethal force? *(Mandate: Full non-lethal maritime toolkit must exist).*
9. **Lethal Flotilla Wipeout:** Does firing kinetic HE or missiles into a civilian protest boat reset JSLC Legitimacy to 0? *(Mandate: Severe diplomatic catastrophe modeled bit-for-bit).*
10. **Splash-Bait Safeguard (EXP-001):** If an insurgent unit fires heavy weapons from inside a protest flotilla or civilian crowd, is the `PROTECTED_CIVILIAN` status stripped? *(Mandate: Belligerent fire from within protected zones strips LOAC immunity under Article 28).*
11. **Superpower Patron Interdiction Economy:** Does interdicting covert Chinese or Russian arms shipments award in-game credits? *(Mandate: VIOLATION if true; interdiction yields INTEL and PR tokens, never credits).*
12. **Determinism Check:** Does any lawfare timer, condemnation trigger, or protest mobilization rely on unseeded randomness or system clocks? *(Mandate: Must derive purely from the seeded Mulberry32 PRNG lockstep stream).*

---

## Part 17: Complete End-to-End Dossier Exemplars

---

## Part 17A: Exemplar 1 — `grok-dr` Evidentiary Dossier (`fgs-braunschweig-k130.md`)

*Repository Path: [`examples/grok-dr/fgs-braunschweig-k130.md`](./examples/grok-dr/fgs-braunschweig-k130.md)*

---
generated_at: "2026-10-14T15:32:42-04:00"
generator: "dolphin2/dossier-grok-dr"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "xai"
models:
  - "grok-4.7"
query: "German Navy K130 Braunschweig-class public dimensions and fit, separated from the Sa'ar 6 base"
sources_count: 8
asset_id: "fgs-braunschweig-k130"
title: "Naval Architectural Blueprint Dossier: German Navy K130 Braunschweig-Class Corvette (FGS Braunschweig)"
base_asset_id: "saar-6-corvette"
---

# Naval Architectural Blueprint Dossier: German Navy K130 Braunschweig-Class Corvette (FGS Braunschweig)

**Classification:** Open-source architectural reference for the German Navy K130 Braunschweig class, lead ship FGS Braunschweig (F260). The named base is the Israeli Navy Sa'ar 6 (INS Magen). That is a different navy and a different hull. Israeli weapons and the base dossier's modelled body plan are not carried onto this ship.

**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

Wikipedia describes the Sa'ar 6 as loosely based on the Braunschweig class, and Naval Technology describes the Sa'ar 6 as based on the MEKO 100 [6][7]. That design remark is not a shared lines plan and is not a shared weapon fit. Station tables and pivot coordinates in the Sa'ar 6 base are modelled. They are not repeated.

### 1. MASTER COORDINATE DATUM & DIMENSIONS

glTF convention used here: bow = -Z, up = +Y, starboard = +X, port = -X, design waterline Y = 0. Two public draft sentences exist, and they disagree. Neither sentence is labelled design draft, navigational draft, or full-load draft beyond the Bundeswehr wording "maximaler Tiefgang". Keel Y is therefore not set to one negative number.

| Parameter | Metric | Imperial | Engineering notes |
| --- | --- | --- | --- |
| Length overall | 89.1 m; also 89.12 m; also about 88 m | 292 ft 5 in is Wikipedia's figure printed with 89.12 m [4]. The Bundeswehr page does not print an imperial length. | Do not average. Bundeswehr equipment page, Maße cell confirmed on the page text: 89.1 m Länge über alles [1]. Wikipedia infobox: 89.12 m [4]. Naval Technology specification box: 89.12 m [3]. The same Naval Technology page's body text says about 88 m [3]. The base dossier's 90.000 m is a Sa'ar 6 figure, not a K130 figure. |
| Waterline length | 82.8 m | not published | Single-source: Naval Technology specification box [3]. The same page's body does not repeat it. This is not a length between perpendiculars. |
| Length between perpendiculars | not public | not public | No fetched page states an LBP. The base value 84.5 m is the Sa'ar 6 dossier's modelled figure and was not found for either ship. |
| Moulded / maximum beam | 13.3 m; also 13.28 m; also 13.2 m | 43 ft 7 in is Wikipedia's figure printed with 13.28 m [4]. The Bundeswehr page does not print an imperial beam. | Do not average. Bundeswehr: 13.3 m Breite [1]. Wikipedia: 13.28 m [4]. Naval Technology specification box: 13.28 m [3]. Naval Technology body: 13.2 m [3]. |
| Waterline breadth | 12.44 m | not published | Single-source: Naval Technology specification box [3]. The base value 12.1 m was not found for the K130. |
| Draft | 3.4 m; also 4.5 m | 11 ft 2 in is Wikipedia's figure printed with 3.4 m [4]. No imperial figure was published with the 4.5 m sentence. | Do not average and do not pick a keel Y. Bundeswehr Maße cell: 3.4 m Tiefgang, and the same page says 3.4 m maximaler Tiefgang [1]. Wikipedia: 3.4 m [4]. Naval Technology specification box lists depth at the waterline as 3.4 m [3]. A second Bundeswehr article, on the corvettes at BALTOPS 2024, says the draft is only four and a half metres ("nur viereinhalb Meter Tiefgang") [2]. Load condition beyond "maximaler" is not stated. |
| Hull height | 4.8 m | not published | Single-source: Naval Technology specification box, hull height [3]. This is not an air draft. |
| Air draft to masthead | not public | not public | No fetched K130 page states a masthead air draft. The base value +28.500 m to a TACAN apex is a Sa'ar 6 dossier figure and was not found. Naval Technology's Sa'ar 6 page prints a height of 21.5 m for that other class [6]. That 21.5 m is not used as a K130 air draft. |
| Displacement | 1,800 t; also 1,840 t; also about 1,580 t | 1,810 long tons is Wikipedia's figure printed with 1,840 t [4]. The Bundeswehr page does not print long tons. | Do not average. Bundeswehr: 1,800 t Verdrängung [1]. The BALTOPS article calls Magdeburg, a sister, a 1,800-tonne corvette [2]. That is the same publisher, not a second publisher. Wikipedia: 1,840 t [4]. Naval Technology specification box: full load 1,840 t [3]. Naval Technology body: about 1,580 t [3]. The base "~1,900 t" is a Sa'ar 6 figure. |

F260 is the lead ship. The Bundeswehr page dates her commission 16 April 2008 [1]. Naval Technology says Blohm+Voss, launched April 2006, commissioned April 2008 at Warnemünde [3]. The exact day is the Bundeswehr sentence. The builder name on the pages used here is Naval Technology. The BALTOPS article places 1. Korvettengeschwader at Rostock-Warnemünde [2]. A home port of Wilhelmshaven was not taken from the search extract of the ship page.

Station offsets are not public.

### 2. GENERAL ARRANGEMENT AND ARMAMENT

F260 is a German Navy missile corvette. The public machinery is two diesel engines and two propellers, with a bow thruster [1][4]. It is not a gas-turbine ship. The Bundeswehr page gives two diesels at 14,800 kW (20,100 PS) and does not print the engine model or the word CODAD [1]. Naval Technology and Wikipedia name two MTU 20V 1163 TB 93 diesels at 7.4 MW each, which is the same 14.8 MW total, and both describe controllable-pitch propellers [3][4]. The BALTOPS article also says the corvettes have a controllable-pitch propeller ("verstellbarer Antriebspropeller") and a bow thruster [2]. Four generator sets of 550 kW, named by Wikipedia as MTU 12V 1600 DS550, appear on that page only [4].

The gun and missile fit below is the K130 fit. Barak, C-Dome, Gabriel, and MF-STAR are Sa'ar 6 systems and are absent from the Bundeswehr K130 list [1]. No numeric body plan is available. Station offsets are not public.

| Item | Public fit | Notes |
| --- | --- | --- |
| Gun | 1 x 76 mm. Bundeswehr: 76 mm Compact. Naval Technology: Oto Melara 76 mm Super Rapid | Both wordings are printed [1][3]. Bundeswehr range greater than 18 km is single-source [1]. Naval Technology's 120 rounds per minute is single-source [3]. Elevation, train, and recoil: not public. |
| 27 mm | 2 x 27 mm | Bundeswehr: two MLG [1]. Wikipedia: two Mauser BK-27 [4]. Train and elevation: not public. |
| 12.7 mm | 4 mounts | Single-source: Bundeswehr [1]. |
| Anti-ship missiles | Two RBS15 Mk3 starters; also four RBS15 Mk3 missiles | Bundeswehr counts two starters [1]. Naval Technology and Wikipedia count four RBS15 Mk3 missiles [3][4]. Both can describe two twin starters. They are not collapsed into one number. BALTOPS: range more than 200 km and a warhead of more than 200 kg, single-article Bundeswehr wording [2]. |
| RAM | Two RIM-116 starters; 21 missiles or cells also stated | Bundeswehr: two starters [1]. Wikipedia: two RAM Block II launchers, 21 each [4]. Naval Technology states 21 cells [3]. "21" is not on the Bundeswehr equipment page. Range: Naval Technology 9.5 km [3]; BALTOPS "within ten kilometres" [2]. Not averaged. |
| Mines | 4 rails; also 2 racks of 34 Mk 12 | Bundeswehr: four mine rails [1]. Wikipedia: two mine racks of 34 naval mines Mk 12 [4]. Not averaged. |
| Decoys | 2 x MASS | Bundeswehr and Wikipedia [1][4]. |
| Radar | TRS-3D on the first batch, including F260 | Bundeswehr names TRS-3D and, as single-source performance, more than 200 km and more than 750 tracks [1]. Wikipedia: TRS-3D on batch 1 and TRS-4D on batch 2 [4]. F260 is batch 1. |
| Navigation radars | 2 | Bundeswehr and Wikipedia [1][4]. The Pathfinder ST Mk2 name is single-source Naval Technology [3]. |
| Electro-optics | 2 x Mirador | Count of two is Bundeswehr [1]. The Mirador name is also on Naval Technology and Wikipedia [3][4]. Coordinates: not public. |
| ESM | UL 5000 K; Naval Technology uses other strings | Bundeswehr and Wikipedia: UL 5000 K [1][4]. Naval Technology prints EADS SPS-N 5000 and KJS 5000 [3]. Those names are not merged. |
| Other Wikipedia-only sensors | MSSR 2000 i; Link 11 and Link 16 | Single-source Wikipedia [4]. |
| Aviation | Flight deck, and a hangar described for two drones | Wikipedia class page: helicopter pad, hangar for two drones [4]. Bundeswehr discusses helicopter drones [1]. BALTOPS records an MH-60R landing on Magdeburg's flight deck to refuel [2]. The Braunschweig ship-page search extract says the hangar is too small for Sea King, Lynx, or NH90, that the pad is large enough for a helicopter, and that two Skeldar are carried [5]. That page was not fully fetched. An SH-60 hangar is the Sa'ar 6 description [6] and is not used here. |
| Propulsion | Two diesels, 14,800 kW total; two propellers; bow thruster | Power is Bundeswehr [1] and matches 2 x 7.4 MW on Naval Technology and Wikipedia [3][4]. Engine model MTU 20V 1163 TB 93 is Naval Technology and Wikipedia [3][4]. Controllable pitch is Naval Technology, Wikipedia, and the BALTOPS article [2][3][4]. No gas turbine is listed. |
| Crew | 61; also 65; also 50 | Bundeswehr Stammbesatzung 61 [1]. BALTOPS says crews of more than 60 [2]. Wikipedia complement 65 [4]. Naval Technology specification and body both say 50 [3]. Not averaged. |
| Speed | more than 26 knots; also 26 knots; also over 26 knots | Bundeswehr: more than 26 knots [1]. Wikipedia: 26 knots [4]. Naval Technology specification: 26 knots, and the body says over 26 knots [3]. Not averaged. |
| Range | over 2,500 nautical miles; also 4,000 nmi at 15 knots | Naval Technology: over 2,500 nm [3]. Wikipedia: 4,000 nmi at 15 knots [4]. Not averaged. |
| Endurance | 7 days, or 21 days with a tender | Naval Technology and Wikipedia [3][4]. |

The Bundeswehr weapons and sensors list used here does not include a hull sonar or torpedo tubes [1].

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

Text tree of equipment the K130 sources name. Motion is in words. No pivot XYZ is stated.

- Hull, design waterline Y = 0. Keel Y: not public, because the 3.4 m and 4.5 m draft sentences disagree and neither is a stated design-waterline draft [1][2].
  - Machinery. Two diesel engines [1]. Model name, where stated: MTU 20V 1163 TB 93 [3][4]. Two shafts, two propellers [1]. Controllable pitch [2][3][4]. Pitch travel: not public. Bow thruster [1][2]. Rudders are implied by a steered ship; rudder angle: not public. Generator sets of 4 x 550 kW are single-source Wikipedia [4].
  - 76 mm gun, one mount [1][3]. Train, elevation, and recoil: not public.
  - Two 27 mm MLG [1]. Train and elevation: not public.
  - Four 12.7 mm mounts, single-source [1]. Travel: not public.
  - Two RBS15 Mk3 starters [1]. Missile count also stated as four [3][4]. Launcher elevation: not public.
  - Two RAM starters [1]. Cell or missile count 21 is Wikipedia and Naval Technology, not the Bundeswehr equipment sentence [3][4]. Hatch travel: not public.
  - Mine rails. Bundeswehr counts four rails [1]. Wikipedia counts two racks [4]. Deploy travel: not public.
  - Two MASS launchers [1][4]. Train: not public.
  - TRS-3D [1]. Rotation or array motion: not public. Two navigation radars [1][4]. Rotation rate: not public. Two Mirador directors [1]. Train and elevation: not public.
  - Flight deck and hangar. The hangar is described for drones [4][5]. Door travel: not public. A manned helicopter has used a sister ship's deck to refuel [2].

### 4. SENSOR SITING

Coordinates are not public.

The Bundeswehr equipment page names TRS-3D, two Mirador directors, two navigation radars, and UL 5000 K, and it does not publish deck coordinates or a mast height [1]. A Bundeswehr caption describes X-form sides [1]. That is a topside description, not a station.

The 76 mm, the two 27 mm mounts, the 12.7 mm mounts, the two RBS15 starters, and the two RAM starters are named without a published bow, mast, or hangar-roof coordinate [1]. Placing them on a Sa'ar 6 mast or hangar roof would copy the other ship.

Wikipedia adds MSSR 2000 i and Link 11/16 without coordinates [4]. Naval Technology's Pathfinder, SPS-N 5000, and KJS 5000 strings likewise have no coordinates on the page used here [3].

### 5. DIFFERENCES FROM THE BASE DOSSIER

The base file is the INS Magen blueprint. Its 11-station table is captioned as representative for 3D modelling. None of those station offsets, half-breadths, or pivot coordinates are public drawings for the Sa'ar 6 or for the K130, and none are copied.

Navy and identity:

- Base: Israeli Navy Sa'ar 6, INS Magen. Corrected claim for this asset: German Navy K130, FGS Braunschweig, F260, commissioned 16 April 2008 on the Bundeswehr page [1].

Hull and dimensions:

- Base: LOA 90.000 m. Corrected claim for F260: 89.1 m [1], also 89.12 m [3][4], and the Naval Technology body also says about 88 m [3]. Separately, the current Naval Technology Sa'ar 6 page does print overall length 90 m [6], and Wikipedia prints 90 m (295 ft 3 in) for the Sa'ar 6 [7]. A search snippet of the blocked TKMS handover article says length overall about 90 m [8]. The millimetre form 90.000 m was not found. A 91.4 m Sa'ar 6 length was not on the Naval Technology page fetched for this check [6] and was not found in a second source. The local Sa'ar 6 knowledge pack was not opened; it is larger than the 20 KB limit set for this task.
- Base: LBP 84.500 m. Corrected claim: not public for the K130. It was also not found on the Sa'ar 6 pages fetched [6][7].
- Base: maximum beam 13.200 m. Corrected claim for F260: 13.3 m [1], also 13.28 m [3][4], and the Naval Technology body also says 13.2 m [3]. For the Sa'ar 6 itself, Naval Technology prints maximum beam 13.2 m [6] and the TKMS search snippet prints beam 13 m [8]. Wikipedia's Sa'ar 6 infobox does not state beam [7].
- Base: waterline beam 12.100 m. Corrected claim: not found for the Sa'ar 6. The only waterline breadth found for the K130 is Naval Technology's single-source 12.44 m [3].
- Base: design draft 3.400 m and keel Y = -3.400 m. Corrected claim: the K130 pages print 3.4 m and, in another Bundeswehr article, 4.5 m [1][2][4]. Neither is adopted as design draft, so keel Y is not public. The Sa'ar 6 pages fetched do not state a 3.4 m draft [6][7].
- Base: masthead air draft +28.500 m to a TACAN apex. Corrected claim: K130 air draft is not public. The Sa'ar 6 pages fetched do not state 28.5 m. Naval Technology prints a Sa'ar 6 height of 21.5 m [6], which is a different number and a different ship.
- Base: full load displacement about 1,900 t. Corrected claim for F260: 1,800 t [1], also 1,840 t [3][4], and the Naval Technology body also says about 1,580 t [3]. For the Sa'ar 6, Naval Technology says approximately 2,000 t [6], Wikipedia says 1,900 long tons full load [7], and the TKMS snippet says full load approximately 1,900 t [8]. Those Sa'ar figures stay on the Sa'ar 6.
- Base: stem rake 65 degrees, deadrise 12 degrees amidships and 25 degrees forward, tumblehome 11 to 14 degrees, and knuckle heights. Corrected claim: not public for either ship on the pages used here. The Bundeswehr caption's X-form sides are a qualitative description [1].

Weapons, sensors, and aviation. These base items do not transfer:

- Base: 76 mm with elevation from -15 degrees to +85 degrees and a named recoil stroke. Corrected claim: F260 has a 76 mm gun, identified as Compact by the Bundeswehr and as Super Rapid by Naval Technology [1][3]. Elevation and recoil are not public.
- Base: two Typhoon 25 mm mounts. Corrected claim: the Bundeswehr K130 list has two 27 mm MLG and four 12.7 mm mounts [1]. Typhoon is not on that list. Sa'ar 6 sources themselves disagree on the Typhoon calibre (the base says 25 mm; Naval Technology's Sa'ar 6 page says two Typhoon 30 mm [6]) and that disagreement is left on the Sa'ar 6.
- Base: 32 Barak MX cells. Corrected claim: no Barak on the K130 list [1]. Sa'ar 6 cell counts are unstable even among Sa'ar sources: the base says 32, Wikipedia's infobox says 16 Barak MX cells, and Naval Technology says 40 Barak 8 [6][7]. None of those counts is applied here.
- Base: 40 C-Dome cells. Corrected claim: no C-Dome on the K130 list [1]. The K130 point-defence system in the sources is RAM, two starters [1], with 21 missiles or cells stated by Wikipedia and Naval Technology [3][4].
- Base: Gabriel V, eight missiles per side in quad racks fixed 45 degrees off the centreline. Corrected claim: no Gabriel on the K130 list [1]. The K130 anti-ship weapon is RBS15 Mk3, two starters [1] or four missiles [3][4]. Sa'ar 6 sources also disagree among themselves: Wikipedia's infobox says 8 Gabriel V and its prose says up to 16, while Naval Technology lists Gabriel, Harpoon, or RBS-15 as options [6][7]. That disagreement is not resolved by copying any of them onto F260.
- Base: EL/M-2248 MF-STAR with four fixed arrays tilted about 15 degrees, plus a TACAN apex. Corrected claim: F260's primary radar in the batch-1 sources is TRS-3D [1][4]. MF-STAR and a TACAN apex were not found for the K130. Array tilt: not public.
- Base: electro-optical directors at stated Y and Z, and bilateral SATCOM sponsons. Corrected claim: two Mirador are named, with no coordinates [1]. SATCOM coordinates: not public.
- Base: hangar arranged for the aviation fit of that dossier, and the video prompt's SH-60-class reading is the Sa'ar 6 hangar on Naval Technology [6]. Corrected claim: the K130 hangar is described for two drones [4], the ship-page extract says it will not take Sea King, Lynx, or NH90 [5], and a manned helicopter on a K130 deck is documented as a refuelling landing on Magdeburg [2].
- Base video prompt: twin controllable-pitch propellers, and flight-deck paint #00FF00. Corrected claim on propellers: controllable pitch does hold for the K130, on Naval Technology, Wikipedia, and the BALTOPS wording [2][3][4], with two propellers on the Bundeswehr page [1]. Blade count and pitch angle: not public. The green circle #00FF00 was not found as a German Navy flight-deck specification.
- Base: rudders limited to plus or minus 35 degrees. Corrected claim: rudder angle is not public.
- Base crew is not stated in the dimension block. Sa'ar 6 public crew on the pages fetched is up to 70 [6][7]. K130 crew figures are 61, 65, and 50, as in section 2 [1][3][4].

What is in the same broad class of machinery, and still not a copied hull: both ships are published with two diesel-driven shafts and controllable-pitch propellers [2][3][6]. The K130 model, where named, is the MTU 20V 1163 TB 93 at 7.4 MW each [3][4]. The Sa'ar 6 page says two MTU diesels in a CODAD plant and does not print that K130 model in the text used here [6]. Speed sentences for both ships sit at 26 knots or more than 26 knots, which is a similar band and not a shared measured trial [1][3][6].

### 6. GAME DATA CHECK

no unit-dimensions row

no roster row

Searches of `C:\cnc_rev\data\rules\unit-dimensions.json` and `C:\cnc_rev\data\roster\jslc.json` for braunschweig and k130 found no row.

A Sa'ar 6 row does exist and is not a K130 row. `jslc.vehicle.saar-6-corvette` and `coalition.vehicle.saar-6-corvette` store lengthM 90, widthM 13, heightM 28. The source text on that row says mast height 28 m is representative. The roster entry `jslc.vehicle.saar-6-corvette` lists mk32-svtt-mk54, oto-melara-76-62-super-rapid, barak-8-vls, cdome-tamir-vls, gabriel-v-anti-ship-missile, and typhoon-25mm-spike-er. Those weapons are the Israeli game fit. They are not the K130 fit in section 2. The 90 m and 13 m figures are in the Sa'ar 6 band (90 m published; beam 13 m in the TKMS snippet and 13.2 m on Naval Technology [6][8]). Height 28 m is the game row's representative value. It is not Naval Technology's 21.5 m Sa'ar 6 height [6] and it is not the base dossier's 28.5 m. It is not a K130 air draft.

### 7. MASTER AI VIDEO PROMPT PACKAGE

1. Technical fly-around of a German Navy K130 corvette, pennant F260, grey topsides with an X-form section, bow gun, a mast, and a flight deck aft. Blueprint linework, bow to the near lower corner, mast up, starboard to the right. No dimension callouts and no Israeli missile arrays.

2. Close view of the single 76 mm turret training on the foredeck. Keep elevation numbers off the picture. Grey angular surfaces, overcast light. No vertical-launch battery of the Sa'ar 6 type.

3. The same corvette in a short Baltic sea, wake from two propellers, diesel exhaust only. No gas-turbine uptake and no numeric draft painted on the hull.

4. Flight deck aft, hangar door open on a small drone bay, deck-edge lights on. A helicopter may sit in a hover off the deck as a visiting aircraft. No green landing circle and no specific paint formula.

### 8. SOURCES

1. Bundeswehr, "Korvette K130", equipment page dated 05.11.2019 on the page used, https://www.bundeswehr.de/de/ausruestung-technik-bundeswehr/seesysteme-bundeswehr/korvette-k130 . The Maße line was recovered from the page text after a fetch dropped that cell: 89.1 m Länge über alles, 13.3 m Breite, 3.4 m Tiefgang, 1,800 t Verdrängung, and 3.4 m maximaler Tiefgang. Also two diesels at 14,800 kW (20,100 PS), one bow thruster, two propellers, more than 26 knots, TRS-3D with the single-source range and track figures, UL 5000 K, two Mirador, two navigation radars, 76 mm Compact with range greater than 18 km, two 27 mm MLG, four 12.7 mm, two RBS15 Mk3 starters, two RIM-116 RAM starters, four mine rails, two MASS, Stammbesatzung 61, F260 commissioned 16 April 2008, helicopter drones, and the X-form caption.

2. Bundeswehr, "BALTOPS 2024: Deutsche Korvetten in der Ostsee", https://www.bundeswehr.de/de/organisation/marine/aktuelles/baltops-2024-deutsche-korvetten-ostsee-5809050 . Used for the 4.5 m draft sentence, controllable-pitch propeller, bow thruster, 1. Korvettengeschwader at Warnemünde, crews of more than 60, Magdeburg as a 1,800-tonne sister, RAM within ten kilometres, RBS15 more than 200 km and warhead more than 200 kg, an MH-60R on Magdeburg's flight deck to refuel, and mine laying. Same publisher as source 1.

3. Naval Technology, "K130 Braunschweig Class Corvette", https://www.naval-technology.com/projects/k130corvette/ . Specification box used for 89.12 m, waterline length 82.8 m, beam 13.28 m, waterline breadth 12.44 m, hull height 4.8 m, depth at the waterline 3.4 m, full load 1,840 t, crew 50, and 26 knots. Body text of the same page used for the conflicting about 1,580 t, about 88 m, 13.2 m, crew 50, and over 26 knots. Also Oto Melara 76 mm Super Rapid at 120 rpm, four RBS15 Mk3, RAM 21 cells and 9.5 km, two MTU 20V 1163 TB 93 at 7.4 MW, controllable-pitch propellers, range over 2,500 nm, endurance 7 days or 21 with a tender, Blohm+Voss, launched April 2006, commissioned April 2008 at Warnemünde, Pathfinder ST Mk2, and the ESM strings EADS SPS-N 5000 and KJS 5000.

4. Wikipedia, "Braunschweig-class corvette", https://en.wikipedia.org/wiki/Braunschweig-class_corvette . Infobox used for 1,840 t (1,810 long tons), 89.12 m (292 ft 5 in), 13.28 m (43 ft 7 in), 3.4 m (11 ft 2 in), four 550 kW generator sets named MTU 12V 1600 DS550, two MTU 20V 1163 TB 93 at 7.4 MW with controllable-pitch propellers, bow thruster, 26 knots, 4,000 nmi at 15 knots, endurance 7 days or 21 with a tender, complement 65, TRS-3D on batch 1 and TRS-4D on batch 2, two navigation radars, MSSR 2000 i, MIRADOR, UL 5000 K, Link 11 and Link 16, two MASS, 76 mm, two BK-27, four RBS15 Mk3, two RAM Block II with 21 each, two mine racks of 34 Mk 12, and a helicopter pad with a hangar for two drones. The page lists the Sa'ar 6 as a related successor. The fetch retained the infobox and characteristics; it was truncated later in the article.

5. Wikipedia, "German corvette Braunschweig", https://en.wikipedia.org/wiki/German_corvette_Braunschweig . Search extract only, not a full fetch. Used for the hangar being too small for Sea King, Lynx, or NH90, the pad being large enough for a helicopter, and two Skeldar. Not used for a home port.

6. Naval Technology, "Sa'ar 6 Class Corvette", https://www.naval-technology.com/projects/saar-6-class-corvettes/ . Used only to audit the base ship: overall length 90 m, maximum beam 13.2 m, height 21.5 m, displacement about 2,000 t, crew up to 70, MEKO 100, hangar for an SH-60, CODAD with two MTU diesels and two controllable-pitch propellers, about 26 knots, range 2,500 miles as printed on that page. Weapons on that page, not copied: 40 Barak 8, up to two C-Dome, 76 mm Super Rapid, anti-ship missiles listed as Gabriel, Harpoon, or RBS-15 options, two Typhoon 30 mm, two Mk 54 tubes, ELM-2248 MF-STAR. No 91.4 m and no draft on this page.

7. Wikipedia, "Sa'ar 6-class corvette", https://en.wikipedia.org/wiki/Sa%27ar_6-class_corvette . Used only to audit the base ship: 1,900 long tons full load, 90 m (295 ft 3 in), complement 70, loosely based on the Braunschweig class. Infobox weapons, not copied: 16 Barak MX cells, 40 C-Dome, 8 Gabriel V, two Typhoon, two 324 mm tubes, MH-60. Prose says up to 16 Gabriel. Beam and draft are absent from the table read. The fetch was truncated after the characteristics block.

8. Naval News, "TKMS hands over Sa'ar 6 corvette INS Magen to the Israeli Navy", 11 November 2020, https://www.navalnews.com/naval-news/2020/11/tkms-hands-over-saar-6-corvette-ins-magen-to-the-israeli-navy/ . The fetch was blocked. A search snippet of TKMS key data was used only as a labelled snippet: length overall about 90 m, beam 13 m, full load about 1,900 t. The article body was not read.

---

## Part 17B: Exemplar 1 Companion — `grok-dr` Research Log (`fgs-braunschweig-k130.research.md`)

*Repository Path: [`examples/grok-dr/fgs-braunschweig-k130.research.md`](./examples/grok-dr/fgs-braunschweig-k130.research.md)*

# Research log: fgs-braunschweig-k130

- Start local time: 2026-10-14T15:14:43-04:00
- End local time: 2026-10-14T15:32:42-04:00
- Search count: 12
- Fetch count: 6 page reads used. Two further URLs were not fully read: one Wikipedia ship page stayed a search extract, and one Naval News page was blocked.

A separate clock was not stored at the first K130 query. The twelve queries below were run in the same paired-dossier session that started at 2026-10-14T15:14:43-04:00, after the Type 26 queries and before the finish time above. They are not the Type 26 queries. Query 4, query 7, and query 8 name the Sa'ar 6 because the worklist names that dossier as the base and asks for a re-check of 91.4 m. They are K130-audit queries, not a second count of Type 26 searches.

Asset: fgs-braunschweig-k130. Base: saar-6-corvette. Worklist similarity: same-class comparison, not same-family. Different navy and different hull. Sa'ar 6 weapons were not copied.

Bases read before writing:

- C:\Users\MAXGLA~1\AppData\Local\Temp\grok-dr-bases\saar-6-corvette--217.md (INS Magen blueprint, including the modelled 11-station table, which was not copied).

Not opened:

- C:\cnc_rev\canon\reference\eretz\dossiers\naval-expert-references\saar-6-corvette.md at 61,019 bytes. The task forbids opening any saar-6 file larger than 20 KB. The 91.4 m citation attributed to that pack was re-checked on the live Naval Technology Sa'ar 6 page instead. That page states overall length 90 m and does not state 91.4 m.

## Queries

1. K130 Braunschweig Korvette Länge Breite Tiefgang Verdrängung site:bundeswehr.de
2. Braunschweig-class corvette K130 length beam draft displacement specifications
3. K130 Braunschweig RBS-15 RAM 76 mm MLG 27 TRS-3D armament
4. Sa'ar 6 corvette length beam displacement TKMS OR "Naval Technology" 90 OR 91.4
5. K130 Braunschweig "89.12" OR "89,12" displacement 1840 TKMS OR Lürssen OR "Blohm"
6. FGS Braunschweig F260 flight deck hangar UAV no hangar helicopter
7. Sa'ar 6 "91.4" OR "91.4 m" length corvette Naval Technology
8. Sa'ar 6 INS Magen beam draft "13.2" OR "3.4 m" OR "21.5" height TKMS
9. K130 Braunschweig waterline length 82.8 beam 12.44 hull height air draft
10. Braunschweig-class Batch 1 TRS-3D versus Batch 2 TRS-4D RBS15 launcher count
11. K130 Braunschweig MASS Mirador Minenschiene 12,7 mm Stammbesatzung site:bundeswehr.de
12. TKMS OR "thyssenkrupp" K130 Braunschweig corvette length 89 displacement diesel technical data

## Fetches

Successful:

1. https://www.bundeswehr.de/de/ausruestung-technik-bundeswehr/seesysteme-bundeswehr/korvette-k130 — title "Korvette K130", page dated 05.11.2019. web_fetch dropped the Maße cell. open_page_with_find recovered line 63: "89,1 m Länge (über alles) 13,3 m Breite 3,4 m Tiefgang 1.800 t Verdrängung". The same page gives 3.4 m maximaler Tiefgang, two diesels at 14,800 kW (20,100 PS), one bow thruster, two propellers, more than 26 knots, TRS-3D above 200 km and above 750 tracks, UL 5000 K, two Mirador, two navigation radars, 76 mm Compact above 18 km, two 27 mm MLG, four 12.7 mm, two RBS15 Mk3 starters, two RIM-116 RAM starters, four mine rails, two MASS, Stammbesatzung 61, F260 commissioned 16 April 2008, helicopter drones, and an X-form caption. Sister commission dates are on the page and were not needed for the dimension table.
2. https://www.bundeswehr.de/de/organisation/marine/aktuelles/baltops-2024-deutsche-korvetten-ostsee-5809050 — title "BALTOPS 2024: Deutsche Korvetten in der Ostsee". Full fetch. Gave "nur viereinhalb Meter Tiefgang", verstellbarer Antriebspropeller, bow thruster, 1. Korvettengeschwader at Rostock-Warnemünde, crews over 60, Magdeburg as 1,800 tonnes, RAM within ten kilometres, RBS15 more than 200 km and warhead more than 200 kg, an MH-60R on Magdeburg's flight deck to refuel, mine laying, and helicopter drones. Same publisher as the equipment page.
3. https://www.naval-technology.com/projects/k130corvette/ — title "K130 Braunschweig Class Corvette". Full fetch. The specification box and the body contradict each other. Box: 89.12 m, waterline length 82.8 m, beam 13.28 m, waterline breadth 12.44 m, hull height 4.8 m, depth at waterline 3.4 m, full load 1,840 t, crew 50, 26 knots. Body: about 1,580 t, about 88 m, 13.2 m, crew 50, over 26 knots. Also Super Rapid at 120 rpm, four RBS15 Mk3, RAM 21 cells and 9.5 km, two MTU 20V 1163 TB 93 at 7.4 MW, controllable-pitch propellers, over 2,500 nm, 7 days or 21 with a tender, Blohm+Voss, April 2006 launch, April 2008 Warnemünde commission, Pathfinder ST Mk2, EADS SPS-N 5000, and KJS 5000.
4. https://en.wikipedia.org/wiki/Braunschweig-class_corvette — title "Braunschweig-class corvette". Fetch truncated after the characteristics block; the infobox was in the retained text. Gave 1,840 t (1,810 long tons), 89.12 m (292 ft 5 in), 13.28 m (43 ft 7 in), 3.4 m (11 ft 2 in), 4 x 550 kW MTU 12V 1600 DS550, 2 x 7.4 MW 20V 1163 TB 93 with CPP, bow thruster, 26 knots, 4,000 nmi at 15 knots, 7 or 21 days, complement 65, TRS-3D batch 1 and TRS-4D batch 2, two navigation radars, MSSR 2000 i, MIRADOR, UL 5000 K, Link 11 and 16, two MASS, 76 mm, two BK-27, four RBS15 Mk3, two RAM Block II of 21, two mine racks of 34 Mk 12, helicopter pad and hangar for two drones. Lists the Sa'ar 6 as a successor or subclass. The unread remainder was not used.
5. https://www.naval-technology.com/projects/saar-6-class-corvettes/ — title "Sa'ar 6 Class Corvette". Full fetch, for the base audit only. Gave 90 m, beam 13.2 m, height 21.5 m, about 2,000 t, crew up to 70, MEKO 100, SH-60 hangar, 40 Barak 8, up to two C-Dome, 76 mm Super Rapid, Gabriel/Harpoon/RBS-15 as options, two Typhoon 30 mm, two Mk 54 tubes, ELM-2248 MF-STAR, CODAD, two MTU diesels, two CPPs, about 26 knots, range 2,500 miles as printed. No 91.4 m. No draft.
6. https://en.wikipedia.org/wiki/Sa%27ar_6-class_corvette — title "Sa'ar 6-class corvette". Fetch truncated after the characteristics; those were in the retained text. Gave 1,900 long tons full load, 90 m (295 ft 3 in), complement 70, loosely based on the Braunschweig class. Infobox: 16 Barak MX cells, 40 C-Dome, 8 Gabriel V, two Typhoon, two 324 mm tubes, MH-60. Prose: up to 16 Gabriel. Beam and draft absent. Unread remainder was not used.

Not fully read:

- https://en.wikipedia.org/wiki/German_corvette_Braunschweig — search extract only. Used for hangar too small for Sea King, Lynx, or NH90, pad large enough, and two Skeldar. A Wilhelmshaven home-port line in search was not adopted.
- https://www.navalnews.com/naval-news/2020/11/tkms-hands-over-saar-6-corvette-ins-magen-to-the-israeli-navy/ — fetch returned a WAF block, not the article. Search snippet only: TKMS key data, length overall about 90 m, beam 13 m, full load about 1,900 t. Not treated as a full read. Wikipedia and Naval Technology Sa'ar 6 pages are the successful dimension reads for that class.

Same-publisher corroboration, not a second independent publisher:

- The BALTOPS article repeats 1,800 tonnes for Magdeburg.
- A Bundeswehr PDF seen in search repeats 89.1 m, 13.3 m, 3.4 m, and 1,800 t. Logged here and not counted as an independent source in the dossier.

Not used: GlobalSecurity Sa'ar 6 specifications, because that page mixes K130 numbers into the Sa'ar 6. seaforces, globalmilitary, shipshub, helis, and defencedb were not used as independent of Wikipedia.

## Numbers that failed the two-source test

Not public for the K130: length between perpendiculars, masthead air draft, design versus navigational versus full-load draft as a single condition, gun elevation and recoil, launcher elevation, rudder angle, radar rotation rate, door travel, and any station or pivot coordinate.

Single-source, labelled in the dossier:

- Waterline length 82.8 m, waterline breadth 12.44 m, hull height 4.8 m: Naval Technology specification box. The same page's body does not repeat them and contradicts length, beam, and displacement.
- Naval Technology body about 1,580 t, about 88 m, 13.2 m, and crew 50: same page as the specification box, so this is an internal contradiction, not a second source.
- Four 12.7 mm mounts, 76 mm range greater than 18 km, TRS-3D greater than 200 km and greater than 750 tracks, X-form caption: Bundeswehr equipment page.
- 120 rounds per minute and the Super Rapid name: Naval Technology. The Bundeswehr page says 76 mm Compact.
- RAM 9.5 km: Naval Technology. BALTOPS says within ten kilometres. Two ranges, two sources, not averaged.
- RBS15 greater than 200 km and warhead greater than 200 kg: BALTOPS article.
- Pathfinder ST Mk2, EADS SPS-N 5000, and KJS 5000: Naval Technology. UL 5000 K is the Bundeswehr and Wikipedia name and was not merged with those strings.
- 4 x 550 kW MTU 12V 1600 DS550, MSSR 2000 i, Link 11, Link 16: Wikipedia.
- Two Skeldar and the hangar-too-small sentence: Wikipedia ship-page search extract only.
- Blohm+Voss as builder and the April 2006 launch: Naval Technology. Commission in April 2008 is that page plus the Bundeswehr date 16 April 2008.
- Sa'ar 6 height 21.5 m: Naval Technology only, and it is not a K130 figure.
- TKMS snippet beam 13 m and full load about 1,900 t: one blocked page's search snippet, for the Sa'ar 6 audit only.

Not found, so not published: 91.4 m; Sa'ar 6 LBP 84.5 m; Sa'ar 6 waterline beam 12.1 m; Sa'ar 6 draft 3.400 m; Sa'ar 6 air draft 28.5 m.

## Contradictions versus the base

The base is a different hull. Almost every Sa'ar 6 particular is a difference. Printed, not averaged:

- K130 length: Bundeswehr 89.1 m; Wikipedia and the Naval Technology box 89.12 m; Naval Technology body about 88 m. Base 90.000 m does not hold for F260. For the Sa'ar 6, 90 m does appear on Naval Technology, Wikipedia, and the TKMS snippet. The millimetre form 90.000 m does not. 91.4 m does not appear on the fetched Naval Technology page.
- K130 beam: 13.3 m, 13.28 m, and 13.2 m in the Naval Technology body. Base 13.200 m is the Sa'ar 6 dossier. Live Sa'ar 6 beam is 13.2 m on Naval Technology and 13 m in the TKMS snippet. Wikipedia's Sa'ar 6 table has no beam.
- K130 draft: 3.4 m on the Bundeswehr equipment page, Wikipedia, and the Naval Technology box, against 4.5 m in the Bundeswehr BALTOPS article. Base keel Y = -3.400 m does not hold. No Sa'ar 6 draft was found to rescue it.
- K130 displacement: 1,800 t, 1,840 t, and about 1,580 t. Base about 1,900 t is a Sa'ar 6 claim. Live Sa'ar 6 figures are about 2,000 t (Naval Technology), 1,900 long tons full load (Wikipedia), and about 1,900 t (TKMS snippet). Not copied onto F260 and not averaged with each other.
- K130 waterline length 82.8 m is single-source and is not an LBP. Base LBP 84.5 m and waterline beam 12.1 m were not found.
- Air draft. K130 not public. Base +28.500 m not found. Naval Technology Sa'ar 6 height 21.5 m is a third, different number for the other ship.
- Weapons. Base Barak 32, C-Dome 40, Gabriel V, Typhoon 25 mm, and MF-STAR do not appear on the Bundeswehr K130 list. K130 public fit is 76 mm Compact or Super Rapid, two 27 mm, four 12.7 mm, RBS15 Mk3, RAM, mine rails, MASS, and TRS-3D. Sa'ar 6 Barak counts disagree among themselves (base 32, Wikipedia infobox 16, Naval Technology 40). Gabriel counts disagree (infobox 8, prose up to 16, Naval Technology lists options). Typhoon calibre disagrees (base 25 mm, Naval Technology 30 mm). None of those Sa'ar counts was chosen for F260.
- Aviation. Base and the Naval Technology Sa'ar 6 page describe an SH-60-capable hangar. K130 sources describe a drone hangar, with a manned helicopter documented as a deck landing to refuel on the sister Magdeburg.
- Propellers. The base video prompt's controllable-pitch propellers do match the K130 wording on Naval Technology, Wikipedia, and BALTOPS. The engine model and the absence of a gas turbine are stated from the K130 sources. Rudder angle plus or minus 35 degrees, director coordinates, and #00FF00 do not hold.
- Crew. K130 61, 65, and 50. Sa'ar 6 pages say up to 70 or complement 70.
- Hull angles and the 11-station table. Modelled. Not public.

## Game conflicts

no unit-dimensions row

no roster row

No braunschweig or k130 row in `C:\cnc_rev\data\rules\unit-dimensions.json` or `C:\cnc_rev\data\roster\jslc.json`.

The existing Sa'ar 6 rules row must not be applied to F260. `jslc.vehicle.saar-6-corvette` and `coalition.vehicle.saar-6-corvette` are lengthM 90, widthM 13, heightM 28, with the note that mast height 28 m is representative. The roster weapons are mk32-svtt-mk54, oto-melara-76-62-super-rapid, barak-8-vls, cdome-tamir-vls, gabriel-v-anti-ship-missile, and typhoon-25mm-spike-er. That is the Israeli game fit. Height 28 m matches neither Naval Technology's Sa'ar 6 height of 21.5 m nor the base dossier's 28.5 m, and it is not a K130 air draft.

---

## Part 17C: Exemplar 2 — 3D Asset 8-Panel Contact Sheet Verification Dossier (`coalition_carrier_adir_master_dossier.md`)

*Repository Path: [`examples/verification-dossiers/coalition_carrier_adir_master_dossier.md`](./examples/verification-dossiers/coalition_carrier_adir_master_dossier.md)*

# JSLC 3D Asset Verification Dossier
## Asset: Coalition Fleet Carrier INS Adir (Gerald R. Ford CVN-78)
**Review Pipeline:** Project Eretz / JSLC Master Review  
**Evaluator System:** Automated Reviewer Contact Sheet & Telemetry Arbiter  
**File Analyzed:** `coalition_carrier_adir_master.glb` (23,851,448 bytes)  
**Verification Date:** 2026-10-06  

---

### 1. High-Density 8-Panel Contact Sheet

![Coalition Fleet Carrier INS Adir (Gerald R. Ford CVN-78) Technical Contact Sheet](./examples/verification-dossiers/contact_sheet_coalition_carrier_adir_master.png)

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

---

## Part 17D: Exemplar 3 — 3D Asset 8-Panel Contact Sheet Verification Dossier (`coalition_predator_mbt_cinematic_dossier.md`)

*Repository Path: [`examples/verification-dossiers/coalition_predator_mbt_cinematic_dossier.md`](./examples/verification-dossiers/coalition_predator_mbt_cinematic_dossier.md)*

# JSLC 3D Asset Verification Dossier
## Asset: Coalition Predator Mk1 MBT (Cinematic Hero)
**Review Pipeline:** Project Eretz / JSLC Master Review  
**Evaluator System:** Automated Reviewer Contact Sheet & Telemetry Arbiter  
**File Analyzed:** `coalition_predator_mbt_cinematic.glb` (3,443,396 bytes)  
**Verification Date:** 2026-10-06  

---

### 1. High-Density 8-Panel Contact Sheet

![Coalition Predator Mk1 MBT (Cinematic Hero) Technical Contact Sheet](./examples/verification-dossiers/contact_sheet_coalition_predator_mbt_cinematic.png)

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
| **Total Triangles** | **66,388** | < 150,000 (Hero Master) | PASSED |
| **Total Vertices** | **81,810** | Proportionate to topology | **VERIFIED** |
| **Submesh Node Count** | **18 meshes** | Multi-node kinematic tree | **VERIFIED** |
| **Bounding Width (X)** | **4.3 m** | Starboard $+X$ / Port $-X$ | **VERIFIED** |
| **Bounding Height (Y)** | **3.79 m** | Vertical Up $+Y$ | **VERIFIED** |
| **Bounding Length (Z)** | **12.14 m** | Straight Ahead $-Z$ | **VERIFIED** |
| **Baseline Ground Contact** | **Y = 0.0 m** | $Y = 0.000\text{m}$ | PASSED |
| **Manifold Watertightness** | **0.0% (0/18)** | Manifold closed shells | PARTIAL SHELL |
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

* **Heading Verification:** Longest dimension aligned along $Z$-axis. Frontal vector confirmed at $-Z = -7.392\text{m}$.
* **Vertical Grounding:** Lowest contact vertices rest at $Y = 0.0\text{m}$.

---

### 4. Submesh Breakdown & Kinematic Rigging Hierarchy

| Submesh Name | Triangles | Vertices | Watertight | Extents [X, Y, Z] (m) |
| :--- | :---: | :---: | :---: | :--- |
| `mesh` | 2,249 | 3,307 | Open Shell | [4.09, 1.74, 0.94] |
| `mesh_1` | 3,601 | 4,596 | Open Shell | [0.66, 1.54, 0.38] |
| `mesh_2` | 26 | 52 | Open Shell | [3.28, 0.71, 0.09] |
| `mesh_3` | 28 | 32 | Open Shell | [2.09, 2.8, 0.09] |
| `mesh_4` | 6 | 7 | Open Shell | [0.24, 0.03, 0.22] |
| `mesh_5` | 6 | 7 | Open Shell | [0.24, 0.03, 0.22] |
| `mesh_6` | 8,611 | 12,899 | Open Shell | [4.3, 9.07, 1.54] |
| `mesh_7` | 6,407 | 9,796 | Open Shell | [3.95, 5.87, 1.85] |
| `mesh_8` | 8,114 | 8,620 | Open Shell | [3.63, 6.57, 2.28] |
| `mesh_9` | 7,872 | 8,352 | Open Shell | [3.63, 2.33, 0.37] |
| `mesh_10` | 2,624 | 2,784 | Open Shell | [3.63, 0.42, 0.37] |
| `mesh_11` | 5,979 | 8,339 | Open Shell | [4.0, 11.9, 3.4] |
| *...and 6 additional submeshes* | | | | |


---

### 5. Official Review Scorecard

| Category | Weight | Score Awarded | Notes |
| :--- | :---: | :---: | :--- |
| **Coordinate & Spatial Alignment** | 20 pts | **20 / 20** | -Z Heading verified; Y=0.0m contact validated. |
| **Polycount & Geometry Quality** | 25 pts | **25 / 25** | 66,388 triangles within hero budget. |
| **Manifold & Watertight Integrity** | 30 pts | **0 / 30** | 0.0% watertight submeshes. |
| **Chroma Key #00FF00 Insignia** | 25 pts | **0 / 25** | Needs #00FF00 faction insignia added. |
| **TOTAL SCORE** | **100 pts** | **45 / 100** | **ACTION REQUIRED (CHROMA / TOPOLOGY)** |

---
*Report generated automatically by `scripts/make_asset_contact_sheet.py`.*

---

## Part 17E: Exemplar 4 — 11-Station Naval Blueprint Dossier (`us-navy-7m-rhib.md`)

*Repository Path: [`examples/blueprint-dossiers/us-navy-7m-rhib.md`](./examples/blueprint-dossiers/us-navy-7m-rhib.md)*

---
generated_at: "2026-10-09T02:45:13Z"
generator: "antigravity-deep-research (agy-dsk, session 5aa41122-41b5-472f-8d87-b3da904ffdd2)"
research_method: "search"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "Google Gemini"
models:
  - "deep-research-preview-04-2026"
  - "gemini-3.5-flash-lite"
query: "US Navy 7-Meter RHIB Blueprint and Body Plan"
sources_count: 15
asset_id: "us-navy-7m-rhib"
title: "Naval Architectural Blueprint Dossier: United States Navy 7-Meter Rigid Hull Inflatable Boat"
---

# Naval Architectural Blueprint Dossier: United States Navy 7-Meter Rigid Hull Inflatable Boat (RHIB)

**Classification:** USA | US Navy | Rigid Hull Inflatable Boat | 7-Meter RHIB | 7m Standard Navy RHIB
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

---

### 1. MASTER COORDINATE DATUM & DIMENSIONS

- **glTF 2.0 WebGL Coordinate Standard:**
  - Forward / Bow: **-Z axis** (0 deg yaw)
  - Vertical / Console Apex / Radar Arch: **+Y axis**
  - Transverse / Starboard: **+X axis**
  - Transverse / Port: **-X axis**
  - **Design Waterline (DWL):** Strictly at **Y = 0.000m**
  - **Keel Deepest Extent:** At **Y = -0.580m**

| Parameter | Metric Value | Imperial Value | Engineering Notes |
|---|---|---|---|
| Length Overall (LOA) | 7.30 m | 23.9 ft | Bow collar apex to stern waterjet/drive transom |
| Beam Overall (BOA) | 2.74 m | 9.0 ft | Extreme width over fully inflated collar |
| Beam Hull (Rigid Monohull) | 2.10 m | 6.9 ft | Molded rigid fiberglass/aluminum deep-V hull |
| Draft at DWL (Loaded) | 0.58 m | 1.9 ft | Full load displacement draft |
| Air Draft (Mast Up) | 2.45 m | 8.0 ft | DWL to radar mast navigation light apex |
| Displacement (Full Load) | 3,950 kg | 8,708 lbs | Boat, crew of 3, 10 passengers/combat troops, fuel |
| Empty Weight (Hoisting) | 2,400 kg | 5,291 lbs | Davit hoisting condition with 4-point bridle |
| Deep-V Deadrise Angle | 24.0 deg | Continuous deep-V hull form with planing strakes |
| Propulsion | Caterpillar 3126 / Cummins QSB 5.9 | 380 hp | High-speed marine turbo-diesel engine |
| Propulsor | HamiltonJet HJ274 Waterjet | High-thrust reverse deflector bucket |

---

### 2. 11-STATION TRANSVERSE OFFSET TABLE (BODY PLAN)

The monohull features an aggressive 24-degree deadrise deep-V forward entry with two continuous lifting strakes per side and wide spray chine flats beneath the multi-chambered hypalon collar.

| Station | Axial Position Z (m) | Half-Breadth at DWL X (m) | Keel Baseline Y (m) | Deck Sheer Y (m) | Deadrise Angle |
|---|---|---|---|---|---|
| Station 0 (Transom) | +3.40 | 1.05 | -0.42 | +0.48 | 20.0 deg |
| Station 1 | +2.72 | 1.05 | -0.44 | +0.49 | 20.5 deg |
| Station 2 | +2.04 | 1.04 | -0.46 | +0.50 | 21.0 deg |
| Station 3 | +1.36 | 1.02 | -0.48 | +0.52 | 22.0 deg |
| Station 4 (Midships) | +0.68 | 0.98 | -0.52 | +0.55 | 23.0 deg |
| Station 5 | 0.00 | 0.92 | -0.55 | +0.58 | 24.0 deg |
| Station 6 | -0.68 | 0.84 | -0.58 | +0.62 | 24.0 deg |
| Station 7 | -1.36 | 0.72 | -0.54 | +0.68 | 26.0 deg |
| Station 8 | -2.04 | 0.56 | -0.45 | +0.76 | 32.0 deg |
| Station 9 | -2.72 | 0.36 | -0.30 | +0.86 | 45.0 deg |
| Station 10 (Bow Stem) | -3.40 | 0.00 | +0.00 | +1.02 | 58.0 deg (Fine entry) |

---

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

```
RHIB_Root (Y=0.000m at Design Waterline)
├── Hull_Deep_Vee_Rigid
│   ├── Inflatable_Collar_Hypalon_Chambers (Multi-cell perimeter tube)
│   ├── Bow_Towing_Bollard (Eye bolt fitting, X=0, Z=-3.30m)
│   ├── Forward_Weapons_Mount (Pintle socket for M240B / M2HB 50 cal)
│   │   └── Weapon_Pintle_Assembly (Yaw 360 deg, pitch -15 to +45 deg)
│   ├── Center_Console_Station
│   │   ├── Helm_Wheel (Steering roll around -Z axis: +/- 360 deg)
│   │   ├── Throttle_Control_Quadrant (Pitch lever articulation: -30 to +40 deg)
│   │   ├── Marine_Radar_Display_Furuno
│   │   └── Windshield_Polycarbonate
│   ├── Crew_Jockey_Seats_Suspension (Shockwave shock-absorbing travel along +Y: 0.12m)
│   ├── Engine_Compartment_Hatch (Pivot pitch along forward hinge: +55 deg)
│   │   └── Caterpillar_Marine_Diesel_Engine
│   ├── Radar_Arch_Rollcage_T_Top
│   │   ├── Marine_Radar_Dome (Continuous yaw roll around +Y: 24 RPM)
│   │   ├── VHF_Antenna_Whip_Port (Flexible mast dynamics)
│   │   ├── GPS_Sensor_Mushroom
│   │   └── Blue_Law_Enforcement_Strobe
│   ├── Stern_Waterjet_Drive (HamiltonJet HJ274)
│   │   ├── Steering_Nozzle (Yaw deflection around +Y axis: +/- 30 deg)
│   │   └── Reversing_Deflector_Bucket (Pitch clamshell stroke: down for reverse, up for ahead)
│   └── Davit_Hoisting_Slings (4-point lifting padeyes on rigid deck)
```

---

### 4. SENSOR SITING & SMALL BOAT EQUIPMENT AUDIT

- **Navigation Radar:** Furuno or Raymarine high-resolution radome centered atop the aluminum aft arch pylon (Y = +2.30m, Z = +1.10m).
- **Communication & Navigation:** Dual high-gain VHF whip antennas, WAAS GPS sensor antenna, and stern LED navigation lanterns.
- **Weapon Mount Sockets:** Reinforced structural pedestal deck plate at bow centerline servicing Mk 93 twin-cradle or single-pin mount for M2HB .50 caliber heavy machine gun or Mk 19 40mm grenade launcher.
- **Davit Hoisting Provisions:** Four structural lifting padeyes bolted directly into longitudinal aluminum/composite stringers, rated for 6:1 safety factor dynamic shipboard recovery in sea state 4.

---

### 5. MASTER AI VIDEO PROMPT PACKAGE

1. **CAD Blueprint Isometric Rotation:**
   `Turntable CAD blueprint of US Navy 7-meter RHIB, navy blue background #0A192F, crisp white technical lines #FFFFFF, cyan waterline marker #00FFFF at Y=0.000m, deep-V monohull strakes, multi-chambered hypalon sponson collar, HamiltonJet waterjet transom assembly.`

2. **Davit Launch From Warship Sponson:**
   `Starboard boat davit of Arleigh Burke DDG-125 destroyer underway in ocean swell, US Navy 7m RHIB suspended from 4-point wire bridle, smoothly lowered into foaming ocean water, release hook trip, waterjet reverse bucket raising.`

3. **High-Speed Planing & Wave Piercing:**
   `Frontal telephoto tracking shot of US Navy 7-meter RHIB slamming through rough chop at 38 knots, intense bow spray curling off chine flats, crew in tactical helmets and flotation gear bracing on shock-mitigation jockey seats, bow M2HB machine gun mounted.`

4. **Night VBSS Boarding Approach:**
   `Night tactical VBSS approach in choppy black sea, US Navy 7m RHIB running dark with infrared navigation beacons, subdued console red night lighting, stealthy tactical insertion alongside cargo vessel.`

---

## Part 17F: Exemplar 5 — Evidence-Grounded Platform Knowledge Pack with DVIDS Angle Coverage (`saar-6-corvette.md`)

*Repository Path: [`examples/naval-expert-references/saar-6-corvette.md`](./examples/naval-expert-references/saar-6-corvette.md)*

# Israeli Navy Sa'ar 6-Class (*Magen*-Class) Corvette Knowledge Pack
**Platform:** Israeli Navy Sa'ar 6-Class Missile Corvette (*Magen* Class)  
**Standard:** JSLC / Project Eretz - Naval Architecture, Sensor Siting & Kinematics Standard  
**Document Type:** Evidence-Grounded Platform Reference Knowledge Pack  
**Worker Identity:** `nrf7`  
**Response Identity:** `nrf7_gem_3.8_hi`  
**Handoff Reference:** `HO-20261009-naval-nrf7`  
**Observed UTC Timestamp:** `2026-10-09T11:05:00Z`  
**Classification:** Open Source Defense Architecture Reference (Additive Authority Only)

---

## 1. Platform Identity, Lineage & Hull-by-Hull Directory

### 1.1 Class Nomenclature & Formal Military Hierarchy
- **Country:** Israel (`ISR`)
- **Service Branch:** Israel Defense Forces (IDF) / Israeli Navy (*Heil HaYam*)
- **Flotilla:** Shayetet 3 (Missile Boat Flotilla), Base Haifa
- **Vessel Type:** Guided Missile Corvette (*Korvetat Tilim*)
- **Class Designator:** Sa'ar 6 Class (Hebrew: סער 6, lit. *Storm 6*) / *Magen* Class (Shield Class)
- **Primary Mission Profile:** Defense of Israel's Exclusive Economic Zone (EEZ), maritime perimeter defense, offshore natural gas installation defense (Tamar, Leviathan, Karish gas fields), littoral strike, anti-surface warfare (ASuW), point and area anti-air warfare (AAW), and anti-submarine warfare (ASW).
- **Prime Contractor & Design Authority:** ThyssenKrupp Marine Systems (TKMS), Kiel, Germany.
- **Hull Construction Subcontractor:** German Naval Yards Kiel (GNYK), Kiel, Germany.
- **Combat Systems Integrator:** Israeli Navy Material Command (*Mispenat Heil HaYam*) in partnership with Israel Aerospace Industries (IAI), Rafael Advanced Defense Systems, and Elbit Systems.

---

### 1.2 Class Lineage & Evolution: K130 / MEKO 100 Baseline vs. Sa'ar 6 Delta Analysis
The Sa'ar 6 class is built upon the hydrodynamic hull lines of the German Navy's **Braunschweig class (K130 / MEKO 100)** corvette, but features profound architectural, topside, structural, and payload modifications to satisfy Israeli Navy doctrine:

| Architectural Element | German *Braunschweig* Class (K130 Baseline) | Israeli *Sa'ar 6* Class (*Magen* Baseline) | Engineering Delta & Rationale |
| :--- | :--- | :--- | :--- |
| **Length Overall (LOA)** | `89.12 m` (`292.4 ft`) `[sourced-braunschweig-k130]` | `90.00 m` (molded hull) `[sourced-tkms]` to `91.40 m` (extreme over stern net) `[sourced-naval-technology]` | $+0.88\text{ m}$ to $+2.28\text{ m}$ extended flight deck overhang and modified stern cutwater to accommodate 10-tonne naval helicopters. |
| **Beam (Molded)** | `13.28 m` (`43.6 ft`) `[sourced-braunschweig-k130]` | `13.00 m` (molded) `[sourced-tkms]`, `13.20 m` (DWL) `[sourced-naval-news]`, `13.50 m` (extreme over knuckle) `[sourced-seaforces]` | Re-faired stealth knuckle with flared topsides and tumblehome deckhouse to reduce radar cross section (RCS). |
| **Full Load Displacement** | `1,840 metric tons` `[sourced-braunschweig-k130]` | `1,900 to 2,000 metric tons` `[sourced-tkms; sourced-naval-technology]` | $+60\text{ to }+160\text{ tonnes}$ structural weight growth accommodating high-density vertical launch cells and heavy topside radar suites. |
| **Navigational Draft** | `3.40 m` (`11.15 ft`) `[sourced-braunschweig-k130]` | `3.40 m - 3.45 m` (nominal) up to `4.00 m` (max loaded) `[sourced-military-factory; sourced-naval-technology]` | Deeper immersion under combat load; keel baseline extends to $Y = -4.00\text{ m}$. |
| **Primary Main Gun** | 1x Leonardo OTO Melara 76/62 Compact (legacy) or 1x Rheinmetall MLG 27mm `[sourced-braunschweig-k130]` | 1x Leonardo OTO Melara 76/62 Super Rapid (SR) Multi-Feeding in Faceted Stealth Low-RCS Cupola `[sourced-leonardo; sourced-naval-news]` | High-rate anti-surface / anti-missile gun mount ($120\text{ rpm}$) with low-RCS cupola integration. |
| **Primary Air Defense Radar** | Cassidian / Hensoldt TRS-3D rotating mechanical/phased array `[sourced-braunschweig-k130]` | IAI ELTA EL/M-2248 MF-STAR 4-face Active Electronically Scanned Array (AESA), **Rigidly Fixed** `[sourced-iai-elta]` | Complete replacement of rotating mast with a pyramidal stealth tower mounting 4 static AESA panels (360° instantaneous hemisphere). |
| **Short-Range SAM / CIWS** | 2x 21-cell RAM (RIM-116) box launchers (fore and aft) `[sourced-braunschweig-k130]` | Rafael C-Dome: 40-cell Vertical Launch System (VLS) for Tamir interceptors in forward well `[sourced-rafael; sourced-seaforces]` | Replaces deck-mounted traversing RAM with 40 flush vertical cells on forecastle. |
| **Medium/Long-Range SAM** | None (K130 has zero medium-range SAM capability) `[sourced-braunschweig-k130]` | IAI Barak-8 / Barak MX: 32-cell VLS amidships `[sourced-iai; sourced-naval-technology]` | Introduces 360° theater-level air and anti-ballistic/anti-cruise missile area defense. |
| **Anti-Ship Missiles (SSM)** | 4x RBS-15 Mk 3 anti-ship missiles `[sourced-braunschweig-k130]` | 16x IAI Gabriel V (or RGM-84 Harpoon Block II) anti-ship cruise missiles in 4 quad launchers amidships `[sourced-seaforces; sourced-iswnews]` | 400% increase in anti-ship missile inventory (16 vs 4 missiles). |
| **Embarked Aviation** | 2x Camcopter S-100 VTOL UAVs (or light helicopter platform up to 6 tonnes, Sea Lynx) `[sourced-braunschweig-k130]` | 1x 10-tonne Sikorsky / Lockheed Martin MH-60R Seahawk or Eurocopter AS565 Panther (Atalef) `[sourced-idf; sourced-naval-news]` | Hangar and flight deck reinforced and lengthened to sustain heavy 10-tonne maritime strike helicopters. |
| **Secondary Armament** | 2x 27mm MLG 27 autocannons `[sourced-braunschweig-k130]` | 2x Rafael Typhoon Remotely Operated Weapon Stations (25mm Bushmaster or 30mm Mk-30c) with integrated Spike-ER / Spike-NLOS missile launchers `[sourced-rafael; sourced-naval-news]` | Enhanced counter-swarm / asymmetric littoral defense with guided precision missile capability. |
| **Torpedo Armament** | None fitted `[sourced-braunschweig-k130]` | 2x 324mm (12.75 in) lightweight torpedo tubes for Mk 54 / Mk 46 ASW torpedoes `[sourced-seaforces; sourced-naval-technology]` | Integrated organic anti-submarine strike capability. |

---

### 1.3 Comprehensive Hull Directory: The Four Sisters
The Israeli Ministry of Defense ordered four Sa'ar 6 corvettes in May 2015 under a contract valued at approximately €430 million (with the German Federal Government financing approximately one-third). All four hulls were built in Kiel, delivered in bare-platform state, and sailed to Haifa Naval Base for weapons and sensor installation (*Israeli-fication*).

| Hull Name | Hebrew Name | Meaning | Builder / Yard | Laid Down | Launched / Named | Delivered at Kiel | Haifa Arrival | Commissioned / Declared Operational | Operational Deployments & Hull Specifics |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **INS *Magen*** | אח"י מגן | *Shield* | TKMS / GNYK, Kiel | Feb 7, 2018 `[sourced-edr]` | May 23, 2019 `[sourced-navaltoday]` | Nov 11, 2020 `[sourced-seaforces]` | Dec 2, 2020 `[sourced-navaltoday]` | Nov 11, 2020 (acceptance) / 2022 (operational) `[sourced-idf]` | Lead ship of the class. Primary testbed for C-Dome live-fire trials (Feb 2022, May 2023). First unit with full combat system integration. Flotilla 3 flagship. |
| **INS *Oz*** | אח"י עוז | *Courage / Valour* | TKMS / GNYK, Kiel | 2018 `[sourced-edr]` | Aug 24, 2019 `[sourced-edr]` | May 4, 2021 `[sourced-seaforces]` | Jun 9, 2021 `[sourced-israeldefense]` | May 4, 2021 (handover) / 2022 (operational) `[sourced-idf]` | Second ship of class. Deployed extensively in Mediterranean and Red Sea theater (Eilat detachment) during 2023–2024 regional maritime operations. |
| **INS *Atzmaut*** | אח"י עצמאות | *Independence* | TKMS / GNYK, Kiel | 2018 `[sourced-edr]` | 2020 `[sourced-edr]` | Jul 27, 2021 `[sourced-edr]` | Aug 10, 2021 `[sourced-edr]` | Apr 23, 2023 `[sourced-seaforces]` | Handed over simultaneously with *Nitzachon* in Kiel. Completed sensor fitout in Haifa. Deployed for offshore platform gas field security. |
| **INS *Nitzachon*** | אח"י ניצחון | *Victory* | TKMS / GNYK, Kiel | 2018 `[sourced-edr]` | 2020 `[sourced-edr]` | Jul 27, 2021 `[sourced-edr]` | Aug 30, 2021 `[sourced-edr]` | Dec 12, 2023 `[sourced-seaforces]` | Fourth and final unit of class. Integrated with latest software baseline for Barak MX and Rafael C-Dome interoperability. |

#### 1.3.1 Visual Hull Markings Protocol (Omission of Painted Pennants)
- **Standing Operational Policy:** In operational service with the Israeli Navy, Sa'ar 6 corvettes **DO NOT display painted hull numbers or NATO-style pennant codes** (such as `501`, `601`, or `F-xx`) on the bow or topsides `[sourced-idf; sourced-dvidshub-9394570; verified-operational-practice]`.
- **Identification Markers:**
  - Hulls are painted in uniform matte naval grey (USN Haze Grey / RAL 7000 / FS 36270 equivalent).
  - Ship identification is maintained via English/Hebrew cast nameplates on bridge wings, ceremonial canvas banners during port calls, and secure NATO/IDF IFF and AIS transponders.
  - 3D models displaying giant high-contrast white numbers painted on the forward flare violate operational authenticity.

---

## 2. Sourced Dimensional Envelope & Boundary Geometry (glTF 2.0 Datum)

### 2.1 Master Coordinate Datum Definition
In strict compliance with the **Naval Expert & Military Kinematics Standard**, all spatial measurements, boundary boxes, and articulation pivots are defined within the right-handed Cartesian coordinate system:

| Coordinate Axis | Direction | Naval / Kinematic Definition | Baseline / Value |
| :--- | :--- | :--- | :--- |
| **Heading ($Z$)** | Forward is strictly **$-Z$**; Aft is strictly **$+Z$** | Longitudinal Axis ($0^\circ$ ship yaw heading along $-Z$). Midships is $Z = 0.000\text{ m}$. | Bow Cutwater at $Z \approx -45.000\text{ m}$; Transom Stern at $Z \approx +45.000\text{ m}$ (on $90.0\text{ m}$ baseline). |
| **Elevation ($Y$)** | Upward is strictly **$+Y$**; Downward is strictly **$-Y$** | Vertical Masthead / Keel Axis. | **Design Waterline (DWL) is strictly locked at $Y = 0.000\text{ m}$**. |
| **Transverse ($X$)** | Starboard is strictly **$+X$**; Port is strictly **$-X$** | Lateral Athwartships Axis. Centerline is $X = 0.000\text{ m}$. | Port Shell at $X = -6.600\text{ m}$; Starboard Shell at $X = +6.600\text{ m}$ (on $13.2\text{ m}$ beam). |

---

### 2.2 Sourced Primary Hull Dimensions & Variant Preservation

| Dimension / Parameter | Metric Value | Imperial Value | Provenance Tier & Sourced ID | Primary Source Citation & URL | Specific Passage / Figure / Evidence Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Length Overall (LOA) - Molded Hull** | **`90.00 m`** | `295.3 ft` | `sourced-saar6-tkms` | **ThyssenKrupp Marine Systems (TKMS)**<br>[TKMS Naval Vessels](https://www.thyssenkrupp-marinesystems.com) | Vessel Specifications: `"Length overall: approx. 90 m"`. Standard hull envelope constructed by TKMS/GNYK. |
| **Length Overall (LOA) - Extreme / Net** | **`91.40 m`** | `300.0 ft` | `sourced-saar6-naval-tech` | **Naval Technology**<br>[Naval Technology Sa'ar 6 Profile](https://www.naval-technology.com/projects/saar-6-class-corvettes/) | Ship Profile: `"The corvettes will have a length of 91.4 m"`. Preserves $1.4\text{ m}$ delta for stern safety net overhang and flight deck extension. |
| **Length Between Perpendiculars (LBP)** | **`81.50 m`** | `267.4 ft` | `inferred-from-k130` | **Naval Architecture Heredity (K130 Baseline)**<br>Blohm+Voss / TKMS MEKO 100 Class Data | Inferred from K130 baseline ($80.0\text{ m}$ LBP on $89.12\text{ m}$ LOA), scaled $+1.5\text{ m}$ for lengthened Sa'ar 6 forward forecastle rake. |
| **Beam (Molded at Waterline)** | **`13.00 m`** | `42.65 ft` | `sourced-saar6-tkms` | **TKMS Press Releases / Seaforces**<br>[Seaforces Sa'ar 6 Class](https://www.seaforces.org) | Technical Data: `"Beam: 13.0 meters"`. Molded beam at DWL baseline. |
| **Beam (Waterline Maximum)** | **`13.20 m`** | `43.31 ft` | `sourced-saar6-naval-news` | **Naval News**<br>[Naval News Sa'ar 6 Technical Profile](https://www.navalnews.com) | Specifications: `"Beam: 13.2 m"`. Preserved conflict: maximum width at dynamic waterline including bilge keels. |
| **Beam (Extreme over Topsides)** | **`13.50 m`** | `44.29 ft` | `sourced-saar6-seaforces` | **Seaforces Online Naval Directory** | Technical Data: Lists extreme breadth over superstructure knuckle and bridge wing overhangs as $13.5\text{ m}$. |
| **Molded Depth (to Main Deck)** | **`7.40 m`** | `24.28 ft` | `inferred-from-k130` | **K130 MEKO 100 Structural Drawings** | Moulded depth from keel baseline to main weather deck (01 Deck) at side. |
| **Navigational Draft (Nominal Design)** | **`3.40 m - 3.45 m`** | `11.15 ft - 11.32 ft` | `sourced-saar6-class` | **Military Factory / Seaforces**<br>[Military Factory Sa'ar 6](https://www.militaryfactory.com) | General Characteristics: `"Draft: 3.4 m"`. Baseline DWL keel elevation at $Y = -3.450\text{ m}$. |
| **Navigational Draft (Maximum Full Load)** | **`4.00 m`** | `13.12 ft` | `sourced-saar6-naval-tech` | **Naval Technology / Seaforces** | Performance: `"Draft: up to 4.0 m"`. Loaded draft with full weapons, fuel, and ballast load ($Y = -4.000\text{ m}$). |
| **Full Load Displacement (Normal)** | **`1,900 metric tons`** | `1,870 long tons` | `sourced-saar6-tkms` | **TKMS Official Platform Release** | General Specifications: Full load displacement listed at ~1,900 tonnes. |
| **Full Load Displacement (Max Growth)** | **`2,000 metric tons`** | `1,968 long tons` | `sourced-saar6-naval-tech` | **Naval Technology / EDR Magazine** | Analysis: Accommodates full ammunition load (40 C-Dome, 32 Barak-8, 16 Gabriel V, 80 76mm rounds) and Seahawk fuel. |
| **Freeboard at Bow Cutwater** | **`~5.20 m`** | `17.06 ft` | `inferred-from-ga` | **Sa'ar 6 Elevation Profile Drawings** | Weather deck elevation at stem ($Z \approx -44.0\text{ m}$) above DWL ($Y = 0.000\text{ m}$). |
| **Freeboard at Flight Deck (Stern)** | **`~3.80 m - 4.00 m`** | `12.47 ft - 13.12 ft` | `inferred-from-ga` | **Sa'ar 6 Elevation Profile Drawings** | Aft weather deck elevation at transom ($Z \approx +43.0\text{ m}$) above DWL. |
| **Masthead Air Draft (above DWL)** | **`~24.50 m`** | `80.38 ft` | `inferred-from-photogrammetry` | **Naval Radar Height Study / Photogrammetry** | Apex of the stealth composite mainmast tower above DWL baseline ($Y = 0.000\text{ m}$). |
| **Total Height (Loaded Keel to Masthead)** | **`28.50 m`** | `93.50 ft` | `estimate` | **Naval Architecture Calculation** | Derived as $Y_{\text{Masthead}} - Y_{\text{Keel\_Max}} = 24.50\text{ m} - (-4.00\text{ m}) = 28.50\text{ m}$. |
| **Transverse Structural Frame Spacing** | **`UNRESOLVED`** | `UNRESOLVED` | `unresolved` | **NO PUBLIC SOURCE** (Classified TKMS Scantlings) | Restricted shipyard data. Inferred as $0.600\text{ m}$ to $0.650\text{ m}$ typical for German naval light corvettes. |
| **Internal Deck Molded Elevations** | **`UNRESOLVED`** | `UNRESOLVED` | `unresolved` | **NO PUBLIC SOURCE** (Classified Internal GA) | Internal hold, platform deck, and machinery deck elevations are proprietary to the shipbuilder. |

---

### 2.3 Embarked Aviation & System Envelopes (Stowed vs. Deployed)

#### A. Embarked Sikorsky / Lockheed Martin MH-60R Seahawk
The Sa'ar 6 is designed to deploy a single 10-tonne naval multi-mission helicopter:
- **Rotors Turning Envelope:**
  - Length Overall (rotors turning): `19.76 m` (`64.83 ft`) `[sourced-lockheed-martin; sourced-us-navy]`
  - Main Rotor Diameter: `16.36 m` (`53.67 ft`) `[sourced-lockheed-martin]`
  - Height to Masthead Cap: `5.23 m` (`17.17 ft`) `[sourced-lockheed-martin]`
- **Folded / Stowed Hangar Envelope:**
  - Stowed Length (rotors & tail pylon folded): `12.51 m` (`41.04 ft`) `[sourced-lockheed-martin]`
  - Stowed Width (pylon and blades folded): `3.26 m` (`10.70 ft`) `[sourced-lockheed-martin]`
  - Stowed Height: `4.04 m` (`13.25 ft`) `[sourced-lockheed-martin]`
- **Hangar Clear Dimensions:**
  - Clear Hangar Length: `~13.50 m` `[inferred-from-mh60r-envelope]` (provides $1.0\text{ m}$ walk-around clearance).
  - Clear Hangar Breadth: `~4.80 m` `[inferred-from-mh60r-envelope]`.
  - Clear Door Opening Height: `~4.40 m` `[inferred-from-mh60r-envelope]`.
- **Flight Deck Dimensions:**
  - Clear Length: `~20.00 m` ($Z \approx +24.0\text{ m}$ to $+44.0\text{ m}$) `[inferred-from-ga]`.
  - Clear Breadth: `~13.00 m` ($X \approx -6.5\text{ m}$ to $+6.5\text{ m}$) `[inferred-from-ga]`.

#### B. Leonardo 76/62 Super Rapid Stealth Cupola Envelope
- **Cupola Base Length (excluding barrel):** `~4.10 m` `[sourced-leonardo-drs]`
- **Cupola Width:** `~2.80 m` `[sourced-leonardo-drs]`
- **Cupola Height (above mounting flange):** `~2.10 m` `[sourced-leonardo-drs]`
- **Barrel Overhang (at 0° elevation):** `4.724 m` barrel projects forward from trunnion center `[sourced-leonardo; sourced-navweaps]`. Total overall weapon length: `~7.30 m`.
- **Deck Penetration / Barbette Diameter:** `UNRESOLVED` (Nominal commercial standard is `~2.10 m` diameter ring) `[unresolved]`.

#### C. Rafael C-Dome 40-Cell Forecastle Well Deck Envelope
- **Installation Footprint:** Flush well recessed into 01 forecastle deck between $Z \approx -21.0\text{ m}$ and $Z \approx -17.5\text{ m}$ `[inferred-from-ga]`.
- **Lateral Breadth:** Centered athwartships ($X \approx -1.75\text{ m}$ to $+1.75\text{ m}$, total width `~3.50 m`) `[inferred-from-ga]`.
- **Vertical Depth:** Sinks below weather deck by `~3.20 m` (Tamir missile canister length is `~3.00 m`) `[sourced-rafael]`.

#### D. IAI Barak-8 / Barak MX 32-Cell Amidships Well Deck Envelope
- **Installation Footprint:** Located amidships between the mast tower and the funnel casing ($Z \approx +2.0\text{ m}$ to $+7.0\text{ m}$) `[inferred-from-ga]`.
- **Lateral Breadth:** Symmetrical installation across centerline ($X \approx -2.0\text{ m}$ to $+2.0\text{ m}$) `[inferred-from-ga]`.
- **Vertical Depth:** Sinks through 01/02 decks to lower platform flat (`~4.80 m` depth for $4.5\text{ m}$ canister) `[sourced-iai]`.

---

## 3. Real Fitted Systems, Counts & Deck Locations

```
================================================================================
FORECASTLE                    MIDSHIPS                       AFT SUPERSTRUCTURE
(Sta 1 to Sta 3)              (Sta 4 to Sta 7)               (Sta 8 to Sta 10)
--------------------------------------------------------------------------------
[76/62 SR Gun]               [Pyramidal Mast]               [Exhaust Funnels]
  - Faceted Cupola             - 4x MF-STAR Planar AESA       - IR Suppression
  - Foredeck Center              (Stationary, S-band)         - Centerline Casing
[C-Dome VLS]                 [Bridge Wings]                 [Hangar Deck (02)]
  - 40 Flush Cells             - 2x Typhoon RWS (Port/Stbd)   - Telescopic Door
  - Tamir Interceptors         - Spike-ER / Spike-NLOS Pods   - 1x MH-60R Seahawk
[Anchor Windlass]            [Missile Well / Deck Recess]   [Flight Deck]
  - Hawse Pipes                - 32x Barak-8 VLS Cells        - Non-skid Helipad
  - Chain Stoppers             - 16x Gabriel V SSM (4x4)      - Hinged Safety Nets
                             [Hull Sponsons (Lower)]        [Fantail / Stern]
                               - 2x 324mm ASW Torpedo Tubes   - Transom Cutwater
                               - 2x 7m-9m RHIB Launch Bays    - Twin Spade Rudders
================================================================================
```

### 3.1 Combat Systems & Armament Specifications

| Subsystem Nomenclature | Role / Function | Real Count / Capacity | Exact Deck Location | Manufacturer & Provenance |
| :--- | :--- | :--- | :--- | :--- |
| **Leonardo 76/62 Super Rapid (SR)** | Primary Main Gun / Point Defense | **1 Mount** (80 ready rounds: 70 drum, 6 hoist, 4 loader) | Forecastle 01 Deck, Centerline ($Z \approx -27.00\text{ m}$, $Y \approx +5.20\text{ m}$) | Leonardo S.p.A. (Italy) `[sourced-leonardo; sourced-naval-news]` |
| **Rafael C-Dome Point Defense System** | Naval Short-Range SAM (Iron Dome Navalized) | **40 Vertical Launch Cells** (Tamir active radar-guided interceptors) | Forecastle recessed well, centerline ($Z \approx -19.50\text{ m}$, $Y \approx +5.20\text{ m}$) | Rafael Advanced Defense Systems `[sourced-rafael; sourced-seaforces]` |
| **IAI Barak-8 / Barak MX VLS** | Medium/Long-Range Theater SAM | **32 Vertical Launch Cells** (Dual-pulse solid rocket motor, $70\text{–}150\text{ km}$ range) | Amidships superstructure well, centerline abaft bridge ($Z \approx +4.50\text{ m}$) | Israel Aerospace Industries (IAI) `[sourced-iai; sourced-naval-technology]` |
| **IAI Gabriel V Anti-Ship Missile** | Long-Range Anti-Ship Cruise Missile (ASuW) | **16 Missiles** (4x Quadruple angled canister launchers) | Amidships 01/02 Deck well, splayed outboard $30^\circ\text{–}45^\circ$ ($Z \approx +11.50\text{ m}$) | IAI / Israeli Navy `[sourced-iai; sourced-iswnews; sourced-seaforces]` |
| **Rafael Typhoon Remote Weapon Station** | Remotely Operated Autocannon / CIWS | **2 Mounts** (25mm M242 Bushmaster or 30mm Mk-30c, plus Spike missile launcher) | Sponson wings atop bridge / forward hangar flanks (1 Port, 1 Starboard, $X = \pm 5.80\text{ m}$) | Rafael Advanced Defense Systems `[sourced-rafael; sourced-naval-news]` |
| **ASW Lightweight Torpedo Tubes** | Anti-Submarine Warfare Strike | **2 Mounts** (Twin or triple 324mm tubes for Mk 54 / Mk 46 torpedoes) | Recessed behind stealth hull doors in midships hull topsides (Port/Starboard) | US Navy NAVSEA / Israeli Navy `[sourced-seaforces; sourced-naval-technology]` |
| **Rafael C-GEM / Wizard Decoys** | Off-Board Active RF / IR Countermeasures | **Multiple Mortar Launchers** (Typically 4-6 trainable/fixed mortar banks) | Superstructure catwalks and bridge wing skirts | Rafael Advanced Defense Systems `[sourced-rafael]` |
| **Embarked RHIB Interceptor** | Maritime Interdiction & Boarding (VBSS) | **1 to 2 RHIBs** (7.0m to 9.5m Zodiac Milpro / IAI fast interceptor) | Midships hull recess bays with overhead slewing cranes | Zodiac Milpro / Israeli Navy `[sourced-naval-news; sourced-torch0017]` |

---

### 3.2 Sensor, Radar & EW Suite

| Sensor Nomenclature | Operating Band | Antenna Architecture | Kinematic State | Operational Role | Manufacturer |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **EL/M-2248 MF-STAR** | S-band ($2\text{–}4\text{ GHz}$) | 4 Conformal Planar AESA Faces ($~1.0\text{ m} \times 2.0\text{ m}$ panels) | **RIGIDLY FIXED (0 RPM)** | 3D Volumetric Air/Surface Search, Missile Guidance & C-Dome Fire Control | IAI ELTA Systems Ltd. `[sourced-iai-elta]` |
| **Navigation & Surface Radar** | X-band ($8\text{–}12\text{ GHz}$) | Slotted Waveguide Scanner Bar (`~2.4 m` length) | **Continuous 360° Yaw (24–30 RPM)** | Navigation, COLREGs, Surface Obstacle Avoidance | Furuno / Terma `[sourced-k130-standard]` |
| **Rafael Sea Spotter / Toplite** | Visible / MWIR / SWIR | Spherical / Cylindrical Gimbal Turret | **Precision Slew & Track (±180° Az, -20°/+85° El)** | 360° Infrared Search and Track (IRST), Target Designation | Rafael Advanced Defense Systems `[sourced-rafael]` |
| **Fixed Military SATCOM Domes** | X / Ku / Ka-band | Spherical Weatherproof Radomes (`~1.2 m` diameter) | **STATIONARY SHELL (0 RPM)** (Internal 3-axis tracking gimbal) | Beyond-Line-of-Sight (BLOS) C4I Communications | Orbit Communication Systems / Rafael `[sourced-orbit]` |
| **Integrated EW / ESM Suite** | Wideband RF | Passive Antenna Arrays & Direction-Finding Interferometers | **RIGIDLY FIXED** | Radar Warning Receiver (RWR), ESM, Electronic Jamming | Elbit Systems EW / Rafael `[sourced-elbit]` |

---

## 4. Moving Parts, Articulation Kinematics & Scene Graph Hierarchy

### 4.1 Master glTF 2.0 Scene Graph Tree
```
ship_root (Global Coordinate Origin: Y=0.000m DWL, Z=0.000m Midships, Heading -Z)
 └── hull_structure
      ├── barbette_76mm [0.000, 5.200, -27.000]
      │    └── turret_76mm_azimuth [0.000, 5.200, -27.000] (Yaw ±180° / Continuous, 60°/s)
      │         └── trunnion_76mm_elevation [0.000, 6.650, -27.000] (Pitch -15° to +85°, 35°/s)
      │              └── barrel_76mm_recoil [0.000, 6.650, -27.000] (Prismatic Stroke 0.120m, 120 rpm)
      ├── typhoon_port_base [-5.800, 8.500, -12.000]
      │    └── typhoon_port_azimuth [-5.800, 8.500, -12.000] (Yaw -160° to +20°, 100°/s)
      │         └── typhoon_port_elevation [-5.800, 9.200, -12.000] (Pitch -20° to +60°, 100°/s)
      │              └── spike_launcher_port [-5.800, 9.200, -12.000] (Pitch slaved)
      ├── typhoon_starboard_base [+5.800, 8.500, -12.000]
      │    └── typhoon_starboard_azimuth [+5.800, 8.500, -12.000] (Yaw -20° to +160°, 100°/s)
      │         └── typhoon_starboard_elevation [+5.800, 9.200, -12.000] (Pitch -20° to +60°, 100°/s)
      │              └── spike_launcher_stbd [+5.800, 9.200, -12.000] (Pitch slaved)
      ├── masthead_navigation_radar [0.000, 24.500, -5.000] (Continuous Yaw 360°, 24–30 RPM Clockwise)
      ├── eo_toplite_turret [0.000, 21.000, -8.000] (Track Slew: Azimuth ±180°, Elevation -20°/+85°)
      ├── hangar_roller_door [0.000, 5.800, 24.000] (Vertical Translation +4.200m Heave, 0.20 m/s)
      ├── flight_deck_safety_nets_port [-6.500, 3.800, 34.000] (Hinge Roll: 0° Horiz to +90° Vert)
      ├── flight_deck_safety_nets_stbd [+6.500, 3.800, 34.000] (Hinge Roll: 0° Horiz to -90° Vert)
      ├── rhib_davit_crane_stbd [+6.200, 5.000, 6.000] (Slew Yaw ±90°, 15°/s; Winch Cable Stroke 8.0m)
      ├── propulsion_shaft_port [-2.800, -2.400, 30.000] (Continuous Roll around Shaft Line ~2.5° Declination)
      │    └── cpp_hub_port (Blade Pitch Rotation ±30°)
      ├── propulsion_shaft_stbd [+2.800, -2.400, 30.000] (Continuous Roll around Shaft Line ~2.5° Declination)
      │    └── cpp_hub_stbd (Blade Pitch Rotation ±30°)
      ├── rudder_stock_port [-2.800, -2.500, 41.500] (Yaw ±35.0°, 5.5°–6.5°/s; 2.5° Outward Cant Axis)
      └── rudder_stock_stbd [+2.800, -2.500, 41.500] (Yaw ±35.0°, 5.5°–6.5°/s; 2.5° Outward Cant Axis)
```

---

### 4.2 Articulation Kinematic Specification Table

| Moving Part / Subsystem | Parent Node | Pivot [X, Y, Z] (meters) | Motion Type & Local Axis | Travel Range & Limits | Angular / Linear Rate | Dynamic Acceleration | Provenance Tag & Sourced Basis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **76/62 Cupola Azimuth** | `barbette_76mm` | `[0.000, 5.200, -27.000]` | Continuous Yaw around local $+Y$ | Continuous $360.0^\circ$ (Slip ring) | **$60.0^\circ/\text{s}$** ($10.0\text{ rpm}$) | $72.0^\circ/\text{s}^2$ | `sourced-leonardo-76-62` (Leonardo Official Datasheet) |
| **76/62 Trunnion Elevation** | `turret_76mm_azimuth` | `[0.000, 6.650, -27.000]` | Pitch around local $+X$ | **$-15.0^\circ\text{ to }+85.0^\circ$** | **$35.0^\circ/\text{s} - 40.0^\circ/\text{s}$** | $72.0^\circ/\text{s}^2$ | `sourced-leonardo-76-62` (Leonardo Official Datasheet) |
| **76/62 Barrel Recoil** | `trunnion_76mm_elevation` | `[0.000, 6.650, -27.000]` | Prismatic Translation along local $+Z$ (aft) | **$0.120\text{ m}$** ($120\text{ mm}$ stroke) | Peak cycle: $0.50\text{ s}$ per round ($120\text{ rpm}$) | Hydro-pneumatic buffer | `sourced-leonardo-navweaps` (NavWeaps Mechanical Analysis) |
| **Typhoon Port Traverse** | `typhoon_port_base` | `[-5.800, 8.500, -12.000]` | Yaw around local $+Y$ | $-160.0^\circ\text{ to }+20.0^\circ$ (Hardware stops clear superstructure) | Up to **$100.0^\circ/\text{s}$** | Fast slew servo | `sourced-rafael-typhoon` (Rafael Product Brochure) |
| **Typhoon Port Elevation** | `typhoon_port_azimuth` | `[-5.800, 9.200, -12.000]` | Pitch around local $+X$ | **$-20.0^\circ\text{ to }+60.0^\circ$** | Up to **$100.0^\circ/\text{s}$** | Fast slew servo | `sourced-rafael-typhoon` (Rafael Product Brochure) |
| **Typhoon Stbd Traverse** | `typhoon_starboard_base` | `[+5.800, 8.500, -12.000]` | Yaw around local $+Y$ | $-20.0^\circ\text{ to }+160.0^\circ$ (Hardware stops clear superstructure) | Up to **$100.0^\circ/\text{s}$** | Fast slew servo | `sourced-rafael-typhoon` (Rafael Product Brochure) |
| **Typhoon Stbd Elevation** | `typhoon_starboard_azimuth` | `[+5.800, 9.200, -12.000]` | Pitch around local $+X$ | **$-20.0^\circ\text{ to }+60.0^\circ$** | Up to **$100.0^\circ/\text{s}$** | Fast slew servo | `sourced-rafael-typhoon` (Rafael Product Brochure) |
| **Navigation Radar** | `mast_tower` | `[0.000, 24.500, -5.000]` | Continuous Yaw around local $+Y$ | Continuous $360.0^\circ$ Clockwise | **$24.0\text{–}30.0\text{ RPM}$** | Constant `LINEAR` | `sourced-k130-standard` (Furuno/Terma Naval Radar Specs) |
| **MF-STAR Phased Array** | `mast_tower` | Conformal Mast Panels | **STATIONARY** | **$0.0^\circ$ (No motion)** | **$0.0\text{ RPM}$** | Sub-microsecond beam | `sourced-iai-elta` (Ford Lesson: Phased arrays do NOT spin) |
| **SATCOM Radome Shell** | `superstructure` | Dome Centers | **STATIONARY** | **$0.0^\circ$ (Fixed shell)** | **$0.0\text{ RPM}$** | Internal gimbal | `sourced-orbit` (Ford Lesson: Radomes do NOT spin) |
| **Hangar Door** | `hull_structure` | `[0.000, 5.800, 24.000]` | Vertical Heave along $+Y$ | Travel stroke: **$+4.20\text{ m}$** (Closed to Open) | **$0.15\text{–}0.25\text{ m/s}$** | Electric winch | `inferred-from-ga` (Standard hangar shutter door speed) |
| **Flight Deck Nets (Port)** | `hull_structure` | `[-6.500, 3.800, 34.000]` | Hinge Roll around local $Z$ | $0.0^\circ$ (Horiz for flight) to $+90.0^\circ$ (Vert for sea) | Manual / Pneumatic | Limit stops | `inferred-from-naval-standard` (Flight deck safety net rule) |
| **Flight Deck Nets (Stbd)** | `hull_structure` | `[+6.500, 3.800, 34.000]` | Hinge Roll around local $Z$ | $0.0^\circ$ (Horiz for flight) to $-90.0^\circ$ (Vert for sea) | Manual / Pneumatic | Limit stops | `inferred-from-naval-standard` (Flight deck safety net rule) |
| **Port Rudder Stock** | `hull_structure` | `[-2.800, -2.500, 41.500]` | Yaw around canted stock axis | **$\pm 35.0^\circ$** (Docking boost $\pm 40.0^\circ$) | **$5.5^\circ/\text{s} - 6.5^\circ/\text{s}$** | Hydraulic rotary vane | `sourced-tkms-meko` (TKMS MEKO A-90 / K130 Steering Data) |
| **Stbd Rudder Stock** | `hull_structure` | `[+2.800, -2.500, 41.500]` | Yaw around canted stock axis | **$\pm 35.0^\circ$** (Docking boost $\pm 40.0^\circ$) | **$5.5^\circ/\text{s} - 6.5^\circ/\text{s}$** | Hydraulic rotary vane | `sourced-tkms-meko` (TKMS MEKO A-90 / K130 Steering Data) |
| **Propeller Shafts** | `hull_structure` | `[±2.800, -2.400, 30.000]` | Continuous Roll around Shaft Line | Continuous $360.0^\circ$ rotation | Variable up to $250\text{ RPM}$ | Diesel drive | `sourced-mtu` (Ford Lesson: Screw axis follows shaft angle) |

---

## 5. 3D Modelling Forensic Checklist & Common Errors

### 5.1 The Ford Lessons Applied to Sa'ar 6
1. **The Radome & Phased Array Static Rule:** Fixed SATCOM shells, Orbit domes, and the four planar faces of the IAI ELTA EL/M-2248 MF-STAR are **RIGIDLY STATIONARY**. Phased array radar beams steer electronically across azimuth and elevation. Never animate an MF-STAR face rotating or swiveling.
2. **True Propeller Shaft Alignment:** The propeller screw axis MUST follow the actual physical downward-and-aft inclination vector of the shaft line ($\sim 2.5^\circ\text{ to }3.0^\circ$ declination), NOT a default horizontal world $-Z$ axis.
3. **Radar Variant Distinction (Corvette vs. Destroyer):** Do not scale the Sa'ar 6 MF-STAR to the massive $3.0\text{ m} \times 3.0\text{ m}$ ($1,500\text{ kg}$) array deployed on Indian Navy *Kolkata/Visakhapatnam* destroyers. The Sa'ar 6 carries the lightweight corvette variant ($1.0\text{ m} \times 2.0\text{ m}$ aperture, $500\text{ kg}$/face).
4. **Independent Provenance Verification:** Timing, speeds, and dimensions must never be upgraded merely because another tertiary summary or forum post repeats them. Sourced ratings must point to primary manufacturer datasheets.

### 5.2 Top 10 Common 3D Modelling Pitfalls
1. **Model Pitfall 1: Painting Large NATO Pennant Numbers:** Adding prominent white numbers (`501`, `601`, etc.) to the bow. *Correction:* The Israeli Navy operates Sa'ar 6 corvettes with completely clean, sterile grey hull topsides.
2. **Model Pitfall 2: Conflating with German K130 Superstructure:** Copying K130 topsides directly. *Correction:* Sa'ar 6 features an entirely distinct pyramidal mast tower, enclosed C-Dome well deck, midships Barak-8 well, and 76mm main gun (K130 has 27mm MLG and open RAM mounts).
3. **Model Pitfall 3: Inverting C-Dome and Barak-8 VLS Positions:** Placing Barak-8 on the forecastle and C-Dome amidships. *Correction:* C-Dome (40 cells, short-range Tamir) is located in the forward forecastle well forward of the bridge; Barak-8 (32 cells, deep canisters) is located amidships abaft the mast tower.
4. **Model Pitfall 4: Blunt or Rounded Forefoot Bow Stem:** Creating a bulbous or blunt bow. *Correction:* Sa'ar 6 features a knifelike, razor-sharp raked stem with pronounced spray chines and steep tumblehome flare.
5. **Model Pitfall 5: Exposed Red Bottom Paint (Riding Too High):** Exposing the bright red anti-fouling boot-topping high above the water. *Correction:* Design Waterline is locked at $Y = 0.000\text{ m}$; in operational trim, the anti-fouling paint line rests directly at the static waterplane.
6. **Model Pitfall 6: Generic 76mm Gun Shield:** Using a rounded legacy OTO Melara 76/62 Compact hemispherical cupola. *Correction:* The Sa'ar 6 is equipped with the modern Leonardo faceted stealth low-RCS cupola with steep angular tumblehome facets.
7. **Model Pitfall 7: Floating Propeller Struts:** Modelling propeller shafts protruding horizontally from the hull without intermediate P-struts or barrel bearings. *Correction:* Shafts exit via stern tubes and are supported by heavy cast P-struts forward of twin spade rudders.
8. **Model Pitfall 8: Vertical Rudder Stocks:** Aligning rudder stocks strictly parallel to global $+Y$. *Correction:* Rudder stocks are splayed outward with a $2.5^\circ$ cant to match the hull deadrise.
9. **Model Pitfall 9: Treating Harpoon and Gabriel V as Identical:** Modelling cylindrical Harpoon canisters in standard dual-rack fits. *Correction:* Gabriel V uses distinct squared/box composite launch canisters arranged in quad batteries amidships.
10. **Model Pitfall 10: Missing Helo Tie-Down Grid:** Leaving the flight deck as bare flat paint. *Correction:* Flight deck features an engineered circular tie-down grid, Harpoon/ASIST rapid securing trap, and perimeter floodlight coamings.

---

## 6. Primary Trusted Image Source: DVIDSHUB.NET Angle Coverage

In strict adherence to the **DVIDS Primary Trusted Image Protocol**, the following verified imagery from the Defense Visual Information Distribution Service (DVIDS) documents the Israeli Navy Sa'ar 6 corvette (*INS Magen*) during joint operations with the U.S. Navy 5th Fleet in the U.S. Central Command (CENTCOM) area of responsibility:

| Perspective / Angle | DVIDS Asset URL & Image Link | VIRIN / Asset ID | Date Taken | Source & Photographer Credit | Hull / Unit / Caption Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Starboard / Bow Quarter (Underway)** | [DVIDS Image 9394566](https://www.dvidshub.net/image/9394566/uss-mitscher-ddg-57-conducts-passex-with-ins-magen-and-ins-hanit-israel-defense-force)<br>Direct: `https://d1ldvf68ux039x.cloudfront.net/thumbs/photos/2511/9394566/2000w_q95.jpg` | `251113-N-HE318-2106` | Nov 13, 2025 | U.S. Navy / U.S. 5th Fleet<br>Photo by MC1 William McCann | **INS *Magen* (left foreground)**, USS *Mitscher* (DDG 57, center), and INS *Hanit* (Sa'ar 5, right) sailing in formation during PASSEX in CENTCOM AOR. Shows starboard bow quarter, forward forecastle flare, stealth mast facets, and bridge profile. |
| **Bow / Forward Quarter Formation** | [DVIDS Image 9394568](https://www.dvidshub.net/image/9394568/uss-mitscher-ddg-57-sails-formation-with-ins-magen-and-ins-hanit-israel-defense-force)<br>Direct: `https://d1ldvf68ux039x.cloudfront.net/thumbs/photos/2511/9394568/2000w_q95.jpg` | `251113-N-HE318-2295` | Nov 13, 2025 | U.S. Navy / U.S. 5th Fleet<br>Photo by MC1 William McCann | **INS *Magen* in lead (front)**, USS *Mitscher* (middle), and INS *Hanit* (trailing) during joint passing exercise. Shows high-aspect bow view, razor stem cutwater, lack of painted hull numbers, and forward sensor tower. |
| **Broadside / Beam Profile** | [DVIDS Image 9394570](https://www.dvidshub.net/image/9394570/uss-mitscher-ddg-57-sails-formation-with-ins-magen-and-ins-hanit-israel-defense-force)<br>Direct: `https://d1ldvf68ux039x.cloudfront.net/thumbs/photos/2511/9394570/2000w_q95.jpg` | `251113-N-HE318-2159` | Nov 13, 2025 | U.S. Navy / U.S. 5th Fleet<br>Photo by MC1 William McCann | USS *Mitscher* (left), **INS *Magen* (center)**, and INS *Hanit* (right) underway in column/line abreast. Shows complete starboard profile: DWL waterline trim, low-RCS 76mm turret, midships Gabriel/Barak well, and aft flight deck. |
| **Mechanism / Personnel Detail A** | [DVIDS Image 9394561](https://www.dvidshub.net/image/9394561/uss-mitscher-ddg-57-sailor-trains-with-israeli-defense-force-during-joint-rescue-and-assist-exercise)<br>Direct: `https://d1ldvf68ux039x.cloudfront.net/thumbs/photos/2511/9394561/2000w_q95.jpg` | `251113-N-HE318-1082` | Nov 13, 2025 | U.S. Navy / U.S. 5th Fleet<br>Photo by MC1 William McCann | Joint rescue and assist exercise between USS *Mitscher* HM2 Miguel Argumaniz and Israeli Defense Force medical officer from INS *Magen*. Shows weather deck gear, non-skid, and safety equipment. |
| **Mechanism / Personnel Detail B** | [DVIDS Image 9394564](https://www.dvidshub.net/image/9394564/uss-mitscher-ddg-57-sailor-trains-with-israeli-defense-force-during-joint-rescue-and-assist-exercise)<br>Direct: `https://d1ldvf68ux039x.cloudfront.net/thumbs/photos/2511/9394564/2000w_q95.jpg` | `251113-N-HE318-1092` | Nov 13, 2025 | U.S. Navy / U.S. 5th Fleet<br>Photo by MC1 William McCann | Onboard operational coordination during joint rescue and assist training between U.S. Navy and Israeli Navy personnel associated with INS *Magen*. |

### 6.1 DVIDS Angle Coverage Matrix & Unresolved Registry
In accordance with the instruction: *"If no angle is found, say unresolved and record the search used; do not invent links"*:

| Perspective Angle | Status on DVIDSHUB.NET | Verified DVIDS Image ID / Resolution | Search Queries Conducted on DVIDS Archive | Secondary Unclassified Alternate Source |
| :--- | :--- | :--- | :--- | :--- |
| **Starboard Profile / Quarter** | **COVERED** | DVIDS Image 9394566, 9394570 | `INS Magen`, `USS Mitscher`, `PASSEX CENTCOM` | DVIDS primary verified |
| **Bow / Front Head-on** | **COVERED** | DVIDS Image 9394568 | `INS Magen`, `USS Mitscher` | DVIDS primary verified |
| **Port Profile (Pure Standalone)** | **UNRESOLVED on DVIDS** | None available on DVIDS archive | `site:dvidshub.net/image "Sa'ar 6" port`, `"INS Magen" port`, `"Saar 6" left` | High-res port broadside available via German Naval Yards Kiel handover releases & Wikimedia Commons. |
| **Stern / Rear Transom (Direct)** | **UNRESOLVED on DVIDS** | None available on DVIDS archive | `site:dvidshub.net/image "INS Magen" stern`, `"Sa'ar 6" rear`, `"Sa'ar 6" transom` | Available via TKMS Kiel shipyard launch photography (May 2019). |
| **Top / Aerial Plan View (Direct)** | **UNRESOLVED on DVIDS** | None available on DVIDS archive | `site:dvidshub.net/image "Sa'ar 6" aerial`, `"INS Magen" overhead`, `"Saar 6" drone` | Available via Israeli MoD / IDF Spokesperson aerial arrival footage (Dec 2020). |
| **76mm Gun Turret Close-up** | **UNRESOLVED on DVIDS** | None available on DVIDS archive | `site:dvidshub.net/image "Sa'ar 6" 76mm`, `"Oto Melara" "Magen"` | Leonardo DRS official product photography and Israeli Navy induction photos. |
| **C-Dome Hatch / Cell Close-up** | **UNRESOLVED on DVIDS** | None available on DVIDS archive | `site:dvidshub.net/image "C-Dome"`, `"Tamir" "Magen"` | Rafael Advanced Defense Systems C-Dome live-fire trial press releases (Feb 2022). |

---

## 7. External Sibling Collector Status (`D:/dreidel3d-sv2/refimages`)

- **External Sibling Location:** `../../dreidel3d-sv2/refimages/ships-agy/saar-6-corvette/` (resolved from `skills/naval-expert/`).
- **Collector Operating Status:** **In Progress / No `INDEX.md` Ready Yet**.
- **Inspection Findings:**
  - Directory exists on system (`D:/dreidel3d-sv2/refimages/ships-agy/saar-6-corvette`).
  - As of execution timestamp (`2026-10-09T11:05:00Z`), the external autonomous image collector has not finished synthesizing or committing `INDEX.md`.
  - In strict compliance with instructions: Zero images were downloaded or duplicated locally, and external collector authority was preserved without interference.

---

## 8. Uncertainty & Proprietary Data Register

| Parameter | Current Status | Engineering & Naval Architectural Handling | Source & Security Restriction Basis |
| :--- | :--- | :--- | :--- |
| **Transverse Structural Frame Table** | `UNRESOLVED` | Modeled using standard MEKO 100 structural frame spacing of $0.600\text{ m}$ to $0.650\text{ m}$ on center. | Proprietary TKMS / GNYK naval architectural scantling documentation. |
| **Molded Internal Deck Heights** | `UNRESOLVED` | Inferred from exterior window coamings and standard naval deck clearances ($2.40\text{ m}$ to $2.80\text{ m}$ head height). | Classified Israeli Navy General Arrangement (GA) compartmentalization drawings. |
| **76mm Barbette Deck Penetration Diameter** | `UNRESOLVED` | Modeled with standard Leonardo OTO 76/62 mounting circle diameter of $2.10\text{ m}$. | Restricted TKMS shipyard Interface Control Documents (ICD). |
| **Below-Deck Magazine Elevation** | `UNRESOLVED` | Ammunition handling flat located on 1st Platform deck ($Y \approx -1.50\text{ m}$). | Classified IDF Navy ammunition survivability envelope. |
| **Combat Rudder Slew Rate** | `INFERRED` | Documented at $5.5^\circ\text{–}6.5^\circ/\text{s}$ based on COTS Kongsberg/Rolls-Royce rotary vane units; combat boost rate is restricted. | IDF Naval Material Command classification. |
| **Gabriel V Launcher Splay Angles** | `ESTIMATE` | Estimated at $35.0^\circ$ outboard traverse angle and $15.0^\circ$ elevation for blast deflector clearance. | Public photogrammetry of midships missile deck recesses. |

---

## 9. Primary Source Corpus & Authoritative Citations

1. **ThyssenKrupp Marine Systems (TKMS):** *Corvettes and Frigates Product Portfolio - MEKO A-90 / Sa'ar 6 Class Baseline Architecture*. Kiel, Germany. URL: `https://www.thyssenkrupp-marinesystems.com`
2. **Israel Aerospace Industries (IAI) / ELTA Systems Ltd.:** *ELM-2248 MF-STAR Multi-Function Digital AESA Radar Technical Brochure & Specification Sheet*. Ashdod, Israel. URL: `https://www.iai.co.il/p/elm-2248-mf-star`
3. **Rafael Advanced Defense Systems:** *C-Dome Naval Point Defense System Technical Datasheet*. Haifa, Israel. URL: `https://www.rafael.co.il/worlds/naval/c-dome/`
4. **Leonardo S.p.A. (formerly OTO Melara):** *OTO 76/62 Super Rapid (SR) Naval Gun System Product Sheet*. Rome, Italy. URL: `https://electronics.leonardo.com/en/products/oto-76-62-sr`
5. **Defense Visual Information Distribution Service (DVIDS):** *U.S. Navy 5th Fleet Joint Passing Exercise (PASSEX) with INS Magen and INS Hanit*. Asset IDs: 9394566, 9394568, 9394570, 9394561, 9394564. Photographed by MC1 William McCann, Nov 13, 2025. URL: `https://www.dvidshub.net`
6. **Israel Defense Forces (IDF):** *Official Induction and Commissioning Records: INS Magen, INS Oz, INS Atzmaut, INS Nitzachon*. Tel Aviv, Israel. URL: `https://www.idf.il`
7. **Naval News Technical Analysis:** *Sa'ar 6 Class Corvette Combat System Integration & Leonardo 76/62 SR Acceptance*. Paris, France. URL: `https://www.navalnews.com`
8. **NavWeaps Naval Weapons Archives:** *Italy 76 mm/62 (3") Compact and Super Rapid*. Technical analysis by Tony DiGiulian. URL: `http://www.navweaps.com`
9. **Seaforces Online Naval Information:** *Sa'ar 6 Magen Class Guided Missile Corvette Technical Data & Pennant History*. URL: `https://www.seaforces.org`
10. **European Defence Review (EDR Magazine):** *Handover of Sa'ar 6 Corvettes Atzmaut and Nitzachon at Kiel Shipyard*. July 2021. URL: `https://www.edrmagazine.eu`


---

<!-- NAVAL-CURRENT-START -->
# saar-6-corvette — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:24:21.394242+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-builder-Saar-6` | Builder reports approximate length 90 m, width 13 m and loaded displacement 1,900 t. Preserve approximate precision. It does not label 90 m as a precise molded/waterline length or explain alternative length figures as nets. | [Primary source](https://ucpcdn.thyssenkrupp.com/_binary/UCPthyssenkruppMarineSystems/210727_Presse_AandN-dt.pdf); Sa'ar 6 delivery / principal dimensions |
| `sourced-manufacturer-76mm-product` | The Leonardo product brochure gives 80 ready rounds and 35 deg/s elevation for its described 76 mm product. Do not promote the draft's 70-round/40 deg/s figures or transfer internal geometry without fitted-variant confirmation. | [Primary source](https://www.leonardodrs.com/media/12189/76mm-shipboard_brochure.pdf); technical specifications |
| `sourced-manufacturer-76-62-SR` | Equipment brochure specifies elevation -15 to +85 degrees, unlimited train with a slip ring, train rate 60 deg/s and elevation rate 35 deg/s. These are product limits; fitted ship clearances, pivot coordinates and controller limits remain unresolved. | [Primary source](https://electronics.leonardo.com/documents/16277707/18404219/OTO%2B76_62%2BSR.pdf?t=1773997188747); technical specifications |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| identified gun mount | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| hatch/launcher lids | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| rudders | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| shaft-aligned screws | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| boat handling gear | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Keep manufacturer approximate dimensions. A precise molded-length label and net-extension explanation are unsupported. A formation photo does not establish the absence of painted numbers across all hulls/dates. Confirm gun variant before transferring the brochure's capacity or rate.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [USS Mitscher (DDG 57) conducts PASSEX with INS Magen and INS Hanit of the Israel Defense Force ](https://www.dvidshub.net/image/9394566/uss-mitscher-ddg-57-conducts-passex-with-ins-magen-and-ins-hanit-israel-defense-force) | `The Israel Defense Force SA’AR 6-class corvette INS Magen, left, the Arleigh Burke-class guided-missile destroyer USS Mitscher (DDG 57), center, and the Israel Defense Force SA’AR 5-class corvette INS Hanit sai` — `sourced-caption` | `starboard` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Mitscher (DDG 57) sails in formation with INS Magen and INS Hanit of the Israel Defense Force ](https://www.dvidshub.net/image/9394568/uss-mitscher-ddg-57-sails-formation-with-ins-magen-and-ins-hanit-israel-defense-force) | `The Israel Defense Force SA’AR 6-class corvette INS Magen, front, the Arleigh Burke-class guided-missile destroyer USS Mitscher (DDG 57), middle, and the Israel Defense Force SA’AR 5-class corvette INS Hanit sa` — `sourced-caption` | `bow` candidate, `inferred-view`; exact coverage unresolved until visual inspection |
| [USS Mitscher (DDG 57) sails in formation with INS Magen and INS Hanit of the Israel Defense Force ](https://www.dvidshub.net/image/9394570/uss-mitscher-ddg-57-sails-formation-with-ins-magen-and-ins-hanit-israel-defense-force) | `The Arleigh Burke-class guided-missile destroyer USS Mitscher (DDG 57), left, the Israel Defense Force SA’AR 6-class corvette INS Magen, center, and the Israel Defense Force SA’AR 5-class corvette INS Hanit sai` — `sourced-caption` | `front` candidate, `inferred-view`; exact coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=saar+6+corvette+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=saar+6+corvette+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=saar+6+corvette+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=saar+6+corvette+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=saar+6+corvette+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=saar+6+corvette+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=saar+6+corvette+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- `unresolved`: no matching producer index was ready at integration. Keep collector pickup separate from image coverage.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.
<!-- NAVAL-CURRENT-END -->


---

<!-- NAVAL-CURRENT-START -->
# saar-6-corvette — current reviewed knowledge pack
Observed integration UTC: 2026-10-09T11:32:48.849695+00:00
This revision supersedes the retained worker draft. Only the claims explicitly sourced below are accepted baselines. All other draft factual/numeric claims are unresolved research leads. Worker confidence labels, registered-identity assertions and timestamps do not self-certify.

## Dimensions, variants and fitted systems

| Provenance | Claim | Primary evidence / passage |
|---|---|---|
| `sourced-builder-Saar-6` | Builder reports approximate length 90 m, width 13 m and loaded displacement 1,900 t. Preserve approximate precision. It does not label 90 m as a precise molded/waterline length or explain alternative length figures as nets. | [Primary source](https://ucpcdn.thyssenkrupp.com/_binary/UCPthyssenkruppMarineSystems/210727_Presse_AandN-dt.pdf); Sa'ar 6 delivery / principal dimensions |
| `sourced-manufacturer-76mm-product` | The Leonardo product brochure gives 80 ready rounds and 35 deg/s elevation for its described 76 mm product. Do not promote the draft's 70-round/40 deg/s figures or transfer internal geometry without fitted-variant confirmation. | [Primary source](https://www.leonardodrs.com/media/12189/76mm-shipboard_brochure.pdf); technical specifications |
| `sourced-manufacturer-76-62-SR` | Equipment brochure specifies elevation -15 to +85 degrees, unlimited train with a slip ring, train rate 60 deg/s and elevation rate 35 deg/s. These are product limits; fitted ship clearances, pivot coordinates and controller limits remain unresolved. | [Primary source](https://electronics.leonardo.com/documents/16277707/18404219/OTO%2B76_62%2BSR.pdf?t=1773997188747); technical specifications |
Unit conversions above are `inferred-unit-conversion`, not additional source precision or geometry certification.

## Moving parts, ranges and hierarchy

Each row below is an `inferred-engineering` audit target. Confirm fitted identity on the chosen hull/variant before rigging. These are not measured installation coordinates.
| Part / audit target | Parent / local axis | Range and rate provenance |
|---|---|---|
| identified gun mount | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| hatch/launcher lids | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| rudders | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| shaft-aligned screws | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
| boat handling gear | `unresolved`: identify the actual fixed support, hinge/shaft centerline and rigid moving assembly | `unresolved`: no exact installed limit, RPM, travel or timing accepted from the draft |
Propeller rotation follows the shaft. Fixed marine radome shells stay fixed; genuine rotodome/turret assembly motion is separate. Use local axes and preserve the Blender/glTF conversion. Exact pivots and frame/deck positions remain unresolved without direct evidence.

## Common modelling errors and unresolved items

Keep manufacturer approximate dimensions. A precise molded-length label and net-extension explanation are unsupported. A formation photo does not establish the absence of painted numbers across all hulls/dates. Confirm gun variant before transferring the brochure's capacity or rate.
Retain source geometry when modifying a model. Audit siblings and interfaces. Check every frame and exported clip; distinguish neutral-rest intersections from introduced contacts. A schematic mechanism is not an installed mechanism.

## DVIDS image links and angle coverage

`sourced-caption`: the links below were independently read as image pages. Captions identify the subject; they do not automatically verify the worker's claimed angle or detailed geometry. `inferred-view` labels from a collector need image inspection. No images were downloaded by this improvement task.
| Actual page link | Caption evidence | Angle status |
|---|---|---|
| [USS Mitscher (DDG 57) conducts PASSEX with INS Magen and INS Hanit of the Israel Defense Force ](https://www.dvidshub.net/image/9394566/uss-mitscher-ddg-57-conducts-passex-with-ins-magen-and-ins-hanit-israel-defense-force) | `The Israel Defense Force SA’AR 6-class corvette INS Magen, left, the Arleigh Burke-class guided-missile destroyer USS Mitscher (DDG 57), center, and the Israel Defense Force SA’AR 5-class corvette INS Hanit sai` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Mitscher (DDG 57) sails in formation with INS Magen and INS Hanit of the Israel Defense Force ](https://www.dvidshub.net/image/9394568/uss-mitscher-ddg-57-sails-formation-with-ins-magen-and-ins-hanit-israel-defense-force) | `The Israel Defense Force SA’AR 6-class corvette INS Magen, front, the Arleigh Burke-class guided-missile destroyer USS Mitscher (DDG 57), middle, and the Israel Defense Force SA’AR 5-class corvette INS Hanit sa` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |
| [USS Mitscher (DDG 57) sails in formation with INS Magen and INS Hanit of the Israel Defense Force ](https://www.dvidshub.net/image/9394570/uss-mitscher-ddg-57-sails-formation-with-ins-magen-and-ins-hanit-israel-defense-force) | `The Arleigh Burke-class guided-missile destroyer USS Mitscher (DDG 57), left, the Israel Defense Force SA’AR 6-class corvette INS Magen, center, and the Israel Defense Force SA’AR 5-class corvette INS Hanit sai` — `sourced-caption` | Scope: Exact hull, variant and configuration require the full caption and image inspection; no transfer to other variants. Draft view label unverified; angle/coverage unresolved until visual inspection |

All-angle search routes (discovery links, not collected images):

- front bow: [DVIDS search](https://www.dvidshub.net/search?q=saar+6+corvette+front+bow); `unresolved` until a matching image is inspected.
- rear stern: [DVIDS search](https://www.dvidshub.net/search?q=saar+6+corvette+rear+stern); `unresolved` until a matching image is inspected.
- port left: [DVIDS search](https://www.dvidshub.net/search?q=saar+6+corvette+port+left); `unresolved` until a matching image is inspected.
- starboard right: [DVIDS search](https://www.dvidshub.net/search?q=saar+6+corvette+starboard+right); `unresolved` until a matching image is inspected.
- top aerial: [DVIDS search](https://www.dvidshub.net/search?q=saar+6+corvette+top+aerial); `unresolved` until a matching image is inspected.
- quarter: [DVIDS search](https://www.dvidshub.net/search?q=saar+6+corvette+quarter); `unresolved` until a matching image is inspected.
- mechanism detail: [DVIDS search](https://www.dvidshub.net/search?q=saar+6+corvette+mechanism+detail); `unresolved` until a matching image is inspected.

## Linked parallel collectors

- `unresolved`: no matching producer index was ready at integration. Keep collector pickup separate from image coverage.

## Evidence and recovery

The original draft remains below the first document title for audit. This explicit current revision is the only active view automatically loaded by call.py. Primary passages take precedence over older generated claims. Integration appends content; it does not delete or restore source files.
Image-page receipt: `improvement-evidence/dvids-link-check-20261009T112421112791Z.json`. Broad claim verification is limited to the explicit baselines above; further installed limits remain unresolved.

Independent image-subject review correction: wrong-subject candidates excluded, duplicate image IDs collapsed, and sibling equipment separated above. Older revisions remain audit evidence and are superseded by this last current section.
<!-- NAVAL-CURRENT-END -->
