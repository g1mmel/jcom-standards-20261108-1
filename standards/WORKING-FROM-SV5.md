# Working with 3D Assets from SV5 (Central Estate Repository)

**Document Version:** 1.1.0  
**Effective Date:** 2026-10-08  
**Author:** Antigravity CLI (`agy-dsk`)  
**Principal Authority:** Agent Kopter  

---

## 1. Overview & Infrastructure Architecture

The entire 3D asset pipeline, geometry store, and revision history are hosted as containerized, LAN-isolated services on **SV5 (`estate-vm` / `11.0.11.32`)** mounted on a dedicated 393 GB disk (`/dev/sdc1` mounted at `/srv/assets`). This ensures complete data persistence and allows working from any machine across the estate network (SV2, SV5, DSK, or portable workstations) independently of local drive state.

```
                           +-----------------------------------------------+
                           |        SV5 (`estate-vm` / 11.0.11.32)         |
                           |                                               |
                           |  [Dedicated 393 GB Mount: /srv/assets]        |
                           |                                               |
                           |  [Bare Git Repository]                        |
                           |    /srv/assets/git/jslc-3d-models.git         |
                           |                                               |
                           |  [MinIO S3 Object Store] (Port 9000 / 9001)   |
                           |    Volume: /srv/assets/store                  |
                           |    Image: RELEASE.2026-09-22T19-25-18Z        |
                           |    Bucket: jslc-3d-assets                     |
                           |                                               |
                           |  [PostgreSQL 16 + pgvector] (Port 5432)       |
                           |    Volume: /srv/assets/db                     |
                           |    Database: assets                           |
                           |                                               |
                           |  [Nightly Cloudflare R2 Backups]              |
                           |    MinIO Mirror: r2://jslc-3d-assets          |
                           |    Postgres Dumps: r2://assets-db-backups     |
                           |    Local Cache: /srv/assets/backups/db        |
                           |    Timer: assets-backup-r2.timer (03:30 UTC)  |
                           |                                               |
                           |  [Estate Operator Switchboard] (Port 8460)    |
                           +-----------------------------------------------+
                                      ^                      ^
                                      |                      |
             Git Push / MinIO Sync    |                      | Git Clone / Work
            (Every 15 min daemon)     |                      |
                                      v                      v
                       +----------------------+      +----------------------+
                       |    DSK (Primary)     |      |    SV2 / Workstation |
                       |    11.0.11.253       |      |    11.0.11.62        |
                       +----------------------+      +----------------------+
```

---

## 2. Quickstart: Setting Up a Working Copy

### Step 2.1: Clone the Git Repository
On any workstation with LAN access and SSH configured for `estate@11.0.11.32`:
```bash
git clone estate@11.0.11.32:/srv/assets/git/jslc-3d-models.git
cd jslc-3d-models
```

### Step 2.2: Verify Remote Configuration
```bash
git remote -v
# origin  estate@11.0.11.32:/srv/assets/git/jslc-3d-models.git (fetch)
# origin  estate@11.0.11.32:/srv/assets/git/jslc-3d-models.git (push)
```

---

## 3. Pulling & Syncing Binary Assets from MinIO

Binary models (GLBs), high-resolution textures, and schematic boards are preserved content-addressably in MinIO on the dedicated disk.

### Option A: Using AWS CLI / S3cmd
```bash
# Configure endpoint
export AWS_ENDPOINT_URL="http://11.0.11.32:9000"

# List assets in the repository bucket
aws --endpoint-url http://11.0.11.32:9000 s3 ls s3://jslc-3d-assets/models/

# Download a specific model (e.g. Ford CVN-78 Operational Master)
aws --endpoint-url http://11.0.11.32:9000 s3 cp \
  s3://jslc-3d-assets/models/flight-a/ford_cvn_operational_master.glb \
  ./flight-a/ford_cvn_operational_master.glb

# Sync all binary assets into local working tree
aws --endpoint-url http://11.0.11.32:9000 s3 sync \
  s3://jslc-3d-assets/models/ ./
```

### Option B: Using Python (`boto3`)
```python
import boto3
from botocore.client import Config

s3 = boto3.client(
    's3',
    endpoint_url='http://11.0.11.32:9000',
    aws_access_key_id='<VAULT_ACCESS_KEY>',
    aws_secret_access_key='<VAULT_SECRET_KEY>',
    config=Config(signature_version='s3v4')
)

# Download binary asset
s3.download_file('jslc-3d-assets', 'models/flight-a/burke_ddg_operational_master.glb', 'burke_ddg_operational_master.glb')
```

---

## 4. Normal Development Workflow

### Step 4.1: Edit & Validate
1. Update geometry, animations, or materials using Blender, Trimesh, or pipeline scripts.
2. Update metadata in `CATALOG.json` and revisions in `revisions/REVISIONS.md`.
3. Generate proof render boards in `renders/`.

### Step 4.2: Commit & Push to SV5
```bash
# Stage code, catalog, and documentation
git add CATALOG.json revisions/REVISIONS.md flight-a/ renders/
git commit -m "feat(flight-a): update Arleigh Burke VLS cell articulation"

# Push all commits and tags to SV5
git push origin main --tags
```

### Step 4.3: Sync New Binaries to MinIO & Database
Run the asset sync tool:
```bash
python tools/sync_assets_to_sv5.py
```
This automatically:
- Computes SHA-256 for all modified GLBs and renders.
- Uploads binaries to MinIO (`s3://jslc-3d-assets/`).
- Upserts triangle counts, dimensional bounds, nodes, and revisions into PostgreSQL.

---

## 5. DSK Automated Synchronization & Data Safety Policy

1. **Automated 15-Minute Sync Task (`Assets-Sync-SV5`)**:
   - DSK runs an automated scheduled task every 15 minutes that executes `git push sv5 --all --tags` and syncs all changed binaries to MinIO.
   - Any work committed on DSK is immediately protected on SV5 within 15 minutes.
2. **Local Retention Policy**:
   - **Zero deletion rule**: No local files or working directories on DSK shall be deleted or freed without explicit authorization from **Agent Kopter**.
   - DSK remains a fully functional live primary mirror.

---

## 6. Service Management & Troubleshooting

| Service | Host | LAN Port | Location / Healthcheck |
| :--- | :--- | :--- | :--- |
| **Git Remote** | `11.0.11.32` | 22 (SSH) | `/srv/assets/git/jslc-3d-models.git` |
| **MinIO API** | `11.0.11.32` | 9000 | `/srv/assets/store` (`http://11.0.11.32:9000/minio/health/live`) |
| **MinIO Web Console**| `11.0.11.32` | 9001 | Browser access via `http://11.0.11.32:9001` |
| **PostgreSQL 16** | `11.0.11.32` | 5432 | `/srv/assets/db` (`pg_isready -h 11.0.11.32 -p 5432 -U assets_user -d assets`) |
| **Nightly R2 Backup**| `11.0.11.32` | Systemd | `systemctl status assets-backup-r2.timer` |
| **Operator Switchboard** | `11.0.11.32` | 8460 | `http://11.0.11.32:8460/clients` |

Credentials are encrypted in the estate vault at `D:/z4yin/secrets/assets-credentials.enc.yaml`.
