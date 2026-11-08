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
