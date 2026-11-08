# Estate Catalogue & DSK Project Inventory

**Authority:** KOPTER  
**Document Version:** 1.0.0  
**Effective Date:** 2026-10-08  
**Generator:** Antigravity CLI (`agy-dsk`)  
**Storage Destination:** SV5 Dedicated Storage Disk (`/srv/assets` on `estate-vm`)  

---

## 1. Inventory Summary

This catalogue details every project, 3D asset store, CAD reference, script repository, and working data folder created or utilized on the DSK (`11.0.11.253`).

| Folder / Store Path | Category | File Count | Size (MB) | Size (GB) | Description & Contents |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `C:\.ai\20261006\jslc-3d-models` | `3d-models-primary` | 378 | 715.07 MB | 0.70 GB | Primary 3D Naval & Military Asset Repository: GLB operational masters, animations, blueprints, render proof boards, catalog, revisions, and tools. |
| `C:\.ai\20261006\asset-builder` | `asset-builder` | 1,026 | 743.69 MB | 0.73 GB | Combat platform modeling workspace, weapon CAD integration dossiers, rigging scripts, and raw candidate GLB models. |
| `C:\.ai\20261006\z4yin-holdco-legal` | `legal-holdco` | 230 | 5.47 MB | 0.01 GB | Z4YIN corporate structure, legal entity dossiers, operations, directives, and regulatory models. |
| `C:\.ai261006\semantic-executor` | `analytics-semantic` | 28 | 0.06 MB | <0.01 GB | Semantic execution engine, discourse discontinuity analysis pipelines, and evaluation harnesses. |
| `D:\sketchfab-library\models` | `sketchfab-models` | 201 | 9,012.16 MB | 8.80 GB | Standardized military & naval 3D model library (201 GLBs classified under strict `[type]` taxonomy). |
| `D:\sketchfab-library\metadata` | `sketchfab-metadata` | 6 | 0.14 MB | <0.01 GB | Machine-readable manifests (`library_manifest.json`), Sketchfab v3 API dumps, and pre-ingestion queues. |
| `D:\sketchfab-library\sketchfab-mcp` | `mcp-server-tooling` | 52 | 0.64 MB | <0.01 GB | Headless Model Context Protocol (MCP) server, CLI downloader, and WebAssembly descrambler. |
| `D:\.google-drive-local\.projects\working-claude` | `agent-workspace` | 225 | 409.43 MB | 0.40 GB | Active agent workspace: operational rigging scripts, render scripts, sessions scratch, and test caches. |
| `D:\torch-staging-boy-george` | `media-investigation` | 64 | 11.65 MB | 0.01 GB | Staging materials: receipts, presentations, alternate takes, video snippets, and transcripts. |
| `C:\z4yin\tools\operator` | `infrastructure-operator` | 15 | 0.11 MB | <0.01 GB | DSK Operator adapter, sync daemon, service credentials, and scheduled task scripts. |
| **TOTAL** | — | **2,225** | **10,898.42 MB** | **10.65 GB** | **Complete DSK Working Footprint** |

---

## 2. Granular Store Details

### 2.1 Primary 3D Naval & Military Models (`C:\.ai\20261006\jslc-3d-models`)
* **Purpose**: Core asset repository containing production-ready, kinematic-rigged military platforms.
* **Key Subdirectories**:
  * `flight-a/`: Capital combatants (USS Gerald R. Ford CVN-78, USS Wasp LHD-1, Arleigh Burke Flight III, Sa'ar 6 Stealth Corvette).
  * `flight-1a/`: Embarked naval aviation (E-2D Hawkeye, F-35C Lightning II, MH-60R Seahawk, LCAC hovercraft, 7m RHIB).
  * `flight-1b/`: Armored combat systems (M1A2 SEPv2 Abrams MBT, AbramsX Demonstrator, HMMWV).
  * `ground-armor/`: Benchmark combat vehicles (Bulwark tank, Predator MBT, K9 Thunder).
  * `weapons-cad/`: High-fidelity weapon sub-assemblies (Mk 45 5-inch, Oto Melara 76mm, Phalanx Block 1B, C-Dome VLS, Barak-8).
  * `renders/`: High-resolution proof boards and verification plates.
  * `schematics/`: Technical blueprint orthographic schematics.
  * `docs/`: Technical standards, rigging specs, NTP 13(B) flag protocols, and parasite craft manifests.
  * `revisions/`: Red team audit reports and revision tracking.

### 2.2 Asset Builder Workspace (`C:\.ai\20261006\asset-builder`)
* **Purpose**: Active construction laboratory where models are disassembled, re-rigged, normal-mapped, and animated before being promoted to `jslc-3d-models`.
* **Key Subdirectories**:
  * `models/`: 112 raw and intermediate GLBs.
  * `scripts/`: Python animation injectors, coordinate transform calculators, and trimesh validators.
  * `reports/`: Weapons CAD integration dossiers and red team audit logs.
  * `dossiers/`: Platform subsystem specifications and dimensional blueprints.
  * `renders/`: Component isolation proof renders.

### 2.3 Sketchfab Standardized Model Library (`D:\sketchfab-library`)
* **Purpose**: Central content-addressable warehouse of 201 identified, standardized, and tagged military GLB models.
* **Key Subdirectories**:
  * `models/`: 201 GLBs ($8.80\,\text{GB}$) strictly adhering to the `[type]-country-unit_name-unit_code–hash.glb` taxonomy.
  * `metadata/`: Structured JSON manifest with polygon counts, vertex counts, author credits, and original URLs.
  * `sketchfab-mcp/`: Standalone Node.js MCP server providing tool access for model inspection and retrieval.

### 2.4 HoldCo Legal Dossiers (`C:\.ai\20261006\z4yin-holdco-legal`)
* **Purpose**: Corporate governance, legal structure, asset ownership, and regulatory documentation for Z4YIN HoldCo.
* **Key Subdirectories**:
  * `directives/`: Strategic and operational guidance.
  * `facilities/`: Real property and physical installation dossiers.
  * `regulatory/`: Regulatory filings, compliance matrices, and jurisdictional treaties.
  * `models/`: Organizational schema and ownership models.

### 2.5 Agent Working Workspace (`D:\.google-drive-local\.projects\working-claude`)
* **Purpose**: Real-time scratch pad, execution harness, and active tools.
* **Key Subdirectories**:
  * `scratch/`: One-off procedural generation scripts, render engines, and pipeline validators.
  * Session databases and log attachments.

---

## 3. Migration Plan to SV5 Dedicated Storage (`/srv/assets`)

1. **Git Repositories**:
   * Stored under `/srv/assets/git/`:
     * `/srv/assets/git/jslc-3d-models.git` (Active)
     * `/srv/assets/git/asset-builder.git` (To be created & pushed)
     * `/srv/assets/git/z4yin-holdco-legal.git` (To be created & pushed)
2. **Binary Assets & Model Warehouses**:
   * MinIO Object Store (`/srv/assets/store`):
     * Bucket `jslc-3d-assets`: Production GLBs and renders.
     * Bucket `sketchfab-library`: Warehouse of all 201 library models and raw archives.
3. **Verification Ledger**:
   * Every file tracked in PostgreSQL database `assets` under table `catalogue_ledger`.
   * Status tracked through: `pending` -> `copied` -> `verified` -> `kopter_approved_to_free`.
   * **Rule**: Delete or free **NOTHING** on DSK without explicit command from **KOPTER**.
