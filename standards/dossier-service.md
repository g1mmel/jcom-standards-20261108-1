---
name: dossier-service
description: "unit dossiers live mainly on the estate dossier service (313 assets), not in the repo; most were never linked to roster models"
metadata:
  node_type: memory
  type: reference
  originSessionId: 531a63cb-68ff-4c00-a484-66c51b2bdd07
  modified: 2026-10-16T19:58:15.706Z
---

Main dossier store: estate dossier service GET http://11.0.11.32:8470/api/dossiers (2026-10-16: 643 records, 313 distinct asset_id; fields id, asset_id, title, s3_key, sha256, method; upload POST /api/dossiers per canon/reference/eretz/dossiers/docs-assets/DOSSIER-STANDARD.md section 4). Also 179 drafts in C:\cnc_rev\asset-scratch\dossiers\ and 13 in canon/.../docs-assets/dossiers. Only 14 matched roster ids by name on 2026-10-16; many are subsystem dossiers (gear, wing fold, turrets, rudders) = the kinematic parts list ("what actuates") for rigs. Standard section 3 = kinematic scene graph = rig spec.

Owner had to remind me ("i think we had a LOT of dossiers") after I counted only the repo's 13. Check the service first. Related: [[archive-term]].
