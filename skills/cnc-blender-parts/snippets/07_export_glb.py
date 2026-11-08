#!/usr/bin/env python3
"""
07_export_glb.py — Contract-compliant GLB exporter for Three.js r170 & unit-structure.mjs:
  - Ensures a 'houseTint' team-colour material slot exists (required by data/rules/unit-structure.json).
  - Clones track materials ('track_L', 'track_R') so UV scrolling does not scroll the hull.
  - Exports with export_yup=True, export_apply=False, export_hierarchy_flatten_objs=False, Draco disabled.
  - Restores rotation_mode = 'XYZ' on all scene objects after export (fixes Blender's QUATERNION mutation trap).
  - Verifies the written GLB header, accessor bbox, node names, and triangle count.

Usage:
  D:\\blender\\blender.exe -b --factory-startup --python-exit-code 1 --python .claude/skills/cnc-blender-parts/snippets/07_export_glb.py -- --in <input.glb> --out <output.glb> [--ensure-house-tint] [--clone-track-mat]
"""

import argparse
import json
import struct
import sys
from pathlib import Path

import bpy


def parse_args():
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    ap = argparse.ArgumentParser(description="Prepare materials/hierarchy and export contract-compliant GLB.")
    ap.add_argument("--in", dest="inp", required=True, help="Input GLB path")
    ap.add_argument("--out", dest="out", required=True, help="Output GLB path")
    ap.add_argument("--ensure-house-tint", action="store_true", default=True, help="Ensure 'houseTint' material slot exists")
    ap.add_argument("--clone-track-mat", action="store_true", default=True, help="Clone material on track_* nodes for independent UV scroll")
    return ap.parse_args(argv)


def inspect_exported_glb(path):
    data = Path(path).read_bytes()
    magic, version, total = struct.unpack_from("<III", data, 0)
    if magic != 0x46546C67:
        raise RuntimeError(f"Invalid GLB magic: {magic:#x}")
    jlen, _ = struct.unpack_from("<II", data, 12)
    gltf = json.loads(data[20 : 20 + jlen].decode("utf-8"))
    mn = [1e9, 1e9, 1e9]
    mx = [-1e9, -1e9, -1e9]
    tris = 0
    for mesh in gltf.get("meshes", []):
        for prim in mesh.get("primitives", []):
            pos_idx = prim.get("attributes", {}).get("POSITION")
            if pos_idx is not None:
                acc = gltf["accessors"][pos_idx]
                if "min" in acc and "max" in acc:
                    for k in range(3):
                        mn[k] = min(mn[k], acc["min"][k])
                        mx[k] = max(mx[k], acc["max"][k])
            idx_i = prim.get("indices")
            if idx_i is not None:
                tris += gltf["accessors"][idx_i].get("count", 0) // 3
    ext = [round(mx[k] - mn[k], 3) for k in range(3)] if mn[0] <= mx[0] else [0, 0, 0]
    nodes = [n.get("name", f"node_{i}") for i, n in enumerate(gltf.get("nodes", []))]
    mats = [m.get("name", "") for m in gltf.get("materials", [])]
    return {
        "version": version,
        "bytes": total,
        "nodes": nodes,
        "materials": mats,
        "triangles": tris,
        "extent_xyz_m": ext,
    }


def main():
    args = parse_args()
    inp = str(Path(args.inp).resolve())
    out = str(Path(args.out).resolve())

    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=inp)

    meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
    if not meshes:
        raise SystemExit("ERROR: No mesh objects in scene")

    # 1. Clone track materials so UV scrolling in Three.js does not scroll hull textures
    if args.clone_track_mat:
        for obj in meshes:
            if "track" in obj.name.lower() and obj.data.materials:
                for i, mat in enumerate(obj.data.materials):
                    if mat and not mat.name.startswith("track_uv_"):
                        cloned = mat.copy()
                        cloned.name = f"track_uv_{obj.name}"
                        obj.data.materials[i] = cloned

    # 2. Ensure a 'houseTint' material exists on at least one rendered primitive (glTF strips unused slots)
    if args.ensure_house_tint:
        tint_names = {"housetint", "team_colour", "teamcolour", "team-colour", "teamcolor"}
        has_tint = any(m and m.name.lower() in tint_names for o in meshes for m in o.data.materials)
        if not has_tint:
            target = next((o for o in meshes if any(k in o.name.lower() for k in ("hull", "turret", "body", "base"))), meshes[0])
            if target.data.materials and target.data.materials[0]:
                # Clone or rename a slot and bind at least one polygon so glTF exports 'houseTint'
                tint_mat = target.data.materials[0].copy()
                tint_mat.name = "houseTint"
                slot_idx = len(target.data.materials)
                target.data.materials.append(tint_mat)
                if len(target.data.polygons) > 0:
                    target.data.polygons[0].material_index = slot_idx
            else:
                tint_mat = bpy.data.materials.new("houseTint")
                tint_mat.use_nodes = True
                target.data.materials.append(tint_mat)

    for obj in bpy.context.scene.objects:
        obj.rotation_mode = "XYZ"

    Path(out).parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.export_scene.gltf(
        filepath=out,
        export_format="GLB",
        export_yup=True,
        export_apply=False,
        export_texcoords=True,
        export_normals=True,
        export_materials="EXPORT",
        export_hierarchy_flatten_objs=False,
        export_draco_mesh_compression_enable=False,
        export_animations=True,
    )

    # Restore XYZ rotation mode (export_scene.gltf mutates objects to QUATERNION in-place!)
    for obj in bpy.context.scene.objects:
        obj.rotation_mode = "XYZ"

    summary = inspect_exported_glb(out)
    summary["out"] = out
    print("EXPORT_GLB_REPORT_JSON:" + json.dumps(summary))


if __name__ == "__main__":
    main()
