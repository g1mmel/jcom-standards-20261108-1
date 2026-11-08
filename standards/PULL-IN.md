# Standing Procedure: 3D Model Pull-In and Repository Ingestion

**Document**: `docs/assets/PULL-IN.md`  
**Owner Role**: Orchestrator / Estate Asset Custodian  
**Classification**: Unclassified // Internal Standing Operational Procedure  
**Effective Date**: 2026-10-08  
**Tag**: `pulled-in`  

---

## 1. Executive Summary & Policy

Any 3D asset (meshes in formats `.glb`, `.gltf`, `.blend`, `.fbx`, `.stl`, `.obj`, or archive bundles `.zip`) discovered outside the canonical Estate repository MUST be pulled in, verified, ingested into MinIO, registered in the PostgreSQL assets database, and tagged `pulled-in`.

This procedure establishes the immutable discovery, de-duplication, storage, indexing, and serving standards for external models.

---

## 2. Discovery Sources & Scope

When scouting for external models, audit the following locations systematically:

1. **Public Sites & Web Endpoints**:
   - Vessel specs and manifest pages (e.g. `https://jewishspacelasercommand.com/eretz/vessels/<vessel-slug>/`).
   - Extract `.glb`/`.gltf` asset links referenced in 3D viewers, cards, or bundled javascript/JSON.
2. **Local Workspaces and Repositories**:
   - Workspaces under `D:/z4yin/` (including `jcom_v0bb_shell_jslc`, `cic`, and staging folders).
   - Project workspaces such as `D:/battlestar3d/` (e.g. `source-galactica.glb`, `test_anim.glb`).
3. **Agent Brains & Upload Caches**:
   - Claude and Gemini session artifacts: `~/.claude/uploads/<uuid>/` and `<appDataDir>/brain/<conversation-id>/`.
4. **Network Storage & SMB File Shares (NAI-DSK)**:
   - Hosts inventory: `docs/network/hosts.json` (`11.0.11.253`).
   - Read-only SMB shares: `\\11.0.11.253\C$` and `\\11.0.11.253\D$`.
   - Key locations on DSK:
     - Brain dumps: `C:\Users\MaxGlasser\.gemini\antigravity\brain\<uuid>\`
     - Desktop and Downloads caches: `D:\_DesktopEXT\_Home_Downloads\`

> [!WARNING]
> Access to SMB file shares on NAI-DSK (`11.0.11.253`) is strictly **read-only**. Never execute write, delete, or modify commands on NAI-DSK shares.

---

## 3. Cryptographic Verification & De-Duplication Gate

Before initiating an ingestion or upload, compute the SHA-256 hash of the candidate file and compare it against the assets database:

```sql
SELECT id, filename, s3_key, sha256 
FROM model_files 
WHERE sha256 = '<candidate-sha256>';

SELECT id, source_path, sv5_location, sha256 
FROM catalogue_ledger 
WHERE sha256 = '<candidate-sha256>';
```

- **If SHA-256 matches**: The model is already ingested. Skip re-uploading duplicate object binaries. If existing metadata lacks the tag, append `'pulled-in'` to `tags` additively.
- **If SHA-256 is absent**: Proceed with full ingestion below.

---

## 4. Object Storage Conventions (MinIO)

- **Target Bucket**: `jslc-3d-assets`
- **Internal Host**: `11.0.11.32:9000` (Estate VM)
- **Target Key Pattern**: `pulled-in/<source-slug>/<filename>`
  - `<source-slug>` groups assets by source origin, vessel class, or lineage (e.g. `battlestar-zion`, `turrets`, `weapons`, `sensors`, `external-meshy`, `space-dreidel`, `bsg-archive`).
  - Example: `pulled-in/battlestar-zion/01_deliverable.glb`
- **Content Types**:
  - `.glb`: `model/gltf-binary`
  - `.gltf`: `model/gltf+json`
  - `.blend`: `application/x-blender`
  - `.zip`: `application/zip`

Credentials reside exclusively in `/opt/assets-store/.env` on Estate VM. Secrets MUST NEVER be printed, echoed, or logged to console/transcripts.

---

## 5. Relational Database Ledger & Registration (PostgreSQL)

Target Database: `assets` on `11.0.11.32:5432` (`assets-db` container).  
All relevant tables (`catalogue_ledger`, `model_assets`, `model_files`, `assets`) support the `tags text[]` column.

### 5.1 Ingestion into `catalogue_ledger`

Record the physical source and verification record:
```sql
INSERT INTO catalogue_ledger (
  source_path,
  sha256,
  size,
  sv5_location,
  category,
  status,
  verified_at,
  notes,
  tags
) VALUES (
  '<source-path-or-smb-uri>',
  '<sha256-hex>',
  <size-in-bytes>,
  'pulled-in/<source-slug>/<filename>',
  'pulled-in',
  'pulled-in',
  NOW(),
  '<descriptive-notes> pulled-in',
  ARRAY['pulled-in']
)
ON CONFLICT (source_path) DO UPDATE SET
  sha256 = EXCLUDED.sha256,
  size = EXCLUDED.size,
  sv5_location = EXCLUDED.sv5_location,
  status = EXCLUDED.status,
  tags = array_append(COALESCE(catalogue_ledger.tags, ARRAY[]::text[]), 'pulled-in'),
  updated_at = NOW();
```

### 5.2 Upsert into `model_assets`

Ensure the parent asset category exists:
```sql
INSERT INTO model_assets (
  asset_id,
  display_name,
  faction,
  country,
  vessel_class,
  vessel_type,
  designation,
  domain,
  notes,
  tags
) VALUES (
  '<asset-id>',
  '<display-name>',
  '<faction>',
  '<faction-or-country>',
  '<vessel-class>',
  '<vessel-type>',
  '<designation>',
  '<domain: space|sea|air|land>',
  '<notes> pulled-in',
  ARRAY['pulled-in']
)
ON CONFLICT (asset_id) DO UPDATE SET
  updated_at = NOW(),
  notes = CASE 
    WHEN model_assets.notes LIKE '%pulled-in%' THEN model_assets.notes 
    ELSE model_assets.notes || ' (pulled-in)' 
  END,
  tags = CASE
    WHEN 'pulled-in' = ANY(COALESCE(model_assets.tags, ARRAY[]::text[])) THEN model_assets.tags
    ELSE array_append(COALESCE(model_assets.tags, ARRAY[]::text[]), 'pulled-in')
  END;
```

### 5.3 Ingestion into `model_files`

Insert the model file entry linking to MinIO:
```sql
INSERT INTO model_files (
  id,
  asset_id,
  filename,
  s3_bucket,
  s3_key,
  sha256,
  size_bytes,
  revision,
  status,
  folder,
  source_path,
  notes,
  tags,
  timestamp
) VALUES (
  gen_random_uuid(),
  '<asset-id>',
  '<filename>',
  'jslc-3d-assets',
  'pulled-in/<source-slug>/<filename>',
  '<sha256-hex>',
  <size-in-bytes>,
  '<revision-tag>',
  'pulled-in',
  'pulled-in',
  '<source-path>',
  '<notes> pulled-in',
  ARRAY['pulled-in'],
  NOW()
);
```

---

## 6. Model Browser Integration

1. **Backend API (`/opt/model-browser/server.js`)**:
   - `GET /api/assets`: Exposes `a.tags` on assets and `f.tags` on versions.
   - Query Parameter Filtering: Supports `?tag=pulled-in` to return assets matching the requested tag.
   - Text Search Integration: The API and frontend index search `notes`, ensuring any query for `pulled-in` displays all pulled-in models.
2. **Frontend UI (`/opt/model-browser/public/index.html`)**:
   - Filter Chip: Workers managing the frontend UI can add a dedicated `[🏷️ Pulled In]` filter chip alongside domain and review status filters that activates `tag=pulled-in` or sets `filterState.q = 'pulled-in'`.

---

## 7. Model Ingestion Summary (Initial 19 Assets)

| Filename | Source Slug | S3 Key | Size (Bytes) | SHA-256 (Prefix) |
| :--- | :--- | :--- | :--- | :--- |
| `01_deliverable.glb` | battlestar-zion | `pulled-in/battlestar-zion/01_deliverable.glb` | 3,947,708 | `921c8b562740b8ae` |
| `02_geom.glb` | battlestar-zion | `pulled-in/battlestar-zion/02_geom.glb` | 90,555,644 | `3b09aa6ebfca66c3` |
| `03_geom.glb` | battlestar-zion | `pulled-in/battlestar-zion/03_geom.glb` | 90,421,584 | `5b22aa3ecebd0288` |
| `04_geom.glb` | battlestar-zion | `pulled-in/battlestar-zion/04_geom.glb` | 89,970,360 | `96d4a153091724ca` |
| `05_manual_01.glb` | battlestar-zion | `pulled-in/battlestar-zion/05_manual_01.glb` | 18,479,268 | `f229b981369cc593` |
| `06_manual_02.glb` | battlestar-zion | `pulled-in/battlestar-zion/06_manual_02.glb` | 19,449,120 | `77646df43aeb44a6` |
| `07_meshy.glb` | battlestar-zion | `pulled-in/battlestar-zion/07_meshy.glb` | 51,744,696 | `77b3d0debe9cd7b4` |
| `08_blockout.glb` | battlestar-zion | `pulled-in/battlestar-zion/08_blockout.glb` | 5,096,780 | `57a24017c03eee41` |
| `saar6_turret_76mm.glb` | turrets | `pulled-in/turrets/saar6_turret_76mm.glb` | 32,980 | `1354657a0f0b9615` |
| `saar6_turret_standalone.glb` | turrets | `pulled-in/turrets/saar6_turret_standalone.glb` | 32,992 | `54602abcd379a94d` |
| `oto_melara_76_gun.glb` | weapons | `pulled-in/weapons/oto_melara_76_gun.glb` | 441,364 | `4e6be01779f64533` |
| `saar6_radar_array.glb` | sensors | `pulled-in/sensors/saar6_radar_array.glb` | 14,488 | `cfb6c1c8e7808387` |
| `saar6_radar_standalone.glb` | sensors | `pulled-in/sensors/saar6_radar_standalone.glb` | 14,468 | `d5ccb964428d2a16` |
| `Meshy_AI_Steel_Sentinel_at_Sea_1006081732_generate.glb` | external-meshy | `pulled-in/external-meshy/...` | 11,783,552 | `1c85fff06a3fad0a` |
| `space_dreidel.blend` | space-dreidel | `pulled-in/space-dreidel/space_dreidel.blend` | 928,572 | `65608c0628053183` |
| `space-dreidel-astra-v1.glb` | space-dreidel | `pulled-in/space-dreidel/space-dreidel-astra-v1.glb` | 3,636,044 | `869f2713311be314` |
| `dreidel3d-model-20261008T2228Z-blender-sv2.blend` | space-dreidel | `pulled-in/space-dreidel/...` | 856,536 | `c5abeeb4ae63e813` |
| `source-galactica.glb` | galactica-generic | `pulled-in/galactica-generic/source-galactica.glb` | 564,036 | `78324616632e571c` |
| `battlestar-galactica-bsg.zip` | bsg-archive | `pulled-in/bsg-archive/battlestar-galactica-bsg.zip` | 80,270,712 | `6fcc78a28cf5fc0b` |
