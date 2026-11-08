#!/usr/bin/env python3
"""
01_import_and_weld.py — Headless Blender 4.2 GLB importer, scale-mismatch fixer,
uint16 chunk joiner, UV-seam welder, and topology diagnostician.

Usage:
  D:\\blender\\blender.exe -b --factory-startup --python-exit-code 1 --python .claude/skills/cnc-blender-parts/snippets/01_import_and_weld.py -- --in <input.glb> [--out <output.glb>] [--weld-dist 0.0001] [--fix-100x] [--join-shards] [--bake-armature]
"""

import argparse
import json
import math
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Vector


def parse_args():
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    ap = argparse.ArgumentParser(description="Import GLB, fix scale/users, weld UV splits, diagnose topology.")
    ap.add_argument("--in", dest="inp", required=True, help="Input GLB path")
    ap.add_argument("--out", dest="out", default="", help="Optional output GLB path")
    ap.add_argument("--weld-dist", type=float, default=0.0001, help="Merge-by-distance threshold in metres (default 0.0001)")
    ap.add_argument("--fix-100x", action="store_true", help="Reset child/mesh nodes with ~0.01 scale to 1.0 when siblings are 1.0")
    ap.add_argument("--join-shards", action="store_true", help="Join 65532-vert uint16 split meshes into one mesh")
    ap.add_argument("--bake-armature", action="store_true", help="Convert skinned meshes to static rest-pose meshes and strip bone widgets")
    return ap.parse_args(argv)


def mesh_diagnostics(obj):
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    verts = len(bm.verts)
    faces = sum(1 for f in bm.faces)
    tris = sum(max(0, len(f.verts) - 2) for f in bm.faces)
    open_edges = sum(1 for e in bm.edges if e.is_boundary)
    non_manifold = sum(1 for e in bm.edges if not e.is_manifold and not e.is_boundary)

    # Count vertex-connected islands in BMesh (never Edit Mode separate)
    bm.verts.ensure_lookup_table()
    visited = set()
    islands = 0
    for v in bm.verts:
        if v.index not in visited:
            islands += 1
            stack = [v]
            visited.add(v.index)
            while stack:
                cur = stack.pop()
                for e in cur.link_edges:
                    nb = e.other_vert(cur)
                    if nb.index not in visited:
                        visited.add(nb.index)
                        stack.append(nb)
    bm.free()
    return {
        "verts": verts,
        "faces": faces,
        "tris": tris,
        "open_edges": open_edges,
        "non_manifold_edges": non_manifold,
        "islands": islands,
    }


def scene_world_bbox(meshes):
    mn = [1e9, 1e9, 1e9]
    mx = [-1e9, -1e9, -1e9]
    for obj in meshes:
        mw = obj.matrix_world
        for corner in obj.bound_box:
            w = mw @ Vector(corner)
            for i in range(3):
                mn[i] = min(mn[i], w[i])
                mx[i] = max(mx[i], w[i])
    if mn[0] > mx[0]:
        return [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]
    size = [round(mx[i] - mn[i], 4) for i in range(3)]
    return [round(v, 4) for v in mn], [round(v, 4) for v in mx], size


def main():
    args = parse_args()
    inp = str(Path(args.inp).resolve())
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=inp)

    # 1. Strip hidden glTF_not_exported bone custom-shape widgets (e.g. Icosphere)
    removed_widgets = []
    for obj in list(bpy.data.objects):
        if "glTF_not_exported" in obj.name or obj.name.startswith("Icosphere"):
            if obj.users_collection and all("glTF_not_exported" in c.name for c in obj.users_collection):
                removed_widgets.append(obj.name)
                bpy.data.objects.remove(obj, do_unlink=True)

    # 2. Detect 100x child scale mismatch (e.g. wasp-class-lhd Recovered_Source_wasp_* at 0.01 vs 1.0 siblings)
    scale_anomalies = []
    for obj in bpy.context.scene.objects:
        sx, sy, sz = obj.scale
        s_avg = (abs(sx) + abs(sy) + abs(sz)) / 3.0
        if 0.005 <= s_avg <= 0.02 or 50.0 <= s_avg <= 200.0:
            scale_anomalies.append({"object": obj.name, "scale": [round(sx, 5), round(sy, 5), round(sz, 5)]})
            if args.fix_100x:
                obj.scale = (1.0, 1.0, 1.0)
    bpy.context.view_layer.update()

    meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
    if not meshes:
        raise SystemExit(f"ERROR: No MESH objects found in {inp}")

    # 3. Optional armature rest-pose bake (prevents Z=21,799 explosion when joining rigged Sketchfab rips)
    if args.bake_armature:
        bpy.ops.object.select_all(action="DESELECT")
        for obj in meshes:
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.convert(target="MESH")
            bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")
        for arm in [o for o in list(bpy.data.objects) if o.type == "ARMATURE"]:
            bpy.data.objects.remove(arm, do_unlink=True)
        meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]

    # 4. Make shared mesh datablocks single-user before transform_apply (prevents multi-user abort on instanced wheels)
    bpy.ops.object.select_all(action="DESELECT")
    for obj in meshes:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = meshes[0]
    bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

    # 5. Detect 65,532-vert uint16 index shards and optionally join
    uint16_shards = [o.name for o in meshes if len(o.data.vertices) >= 65000]
    if args.join_shards and len(meshes) > 1:
        bpy.ops.object.select_all(action="DESELECT")
        for obj in meshes:
            obj.select_set(True)
        bpy.context.view_layer.objects.active = meshes[0]
        bpy.ops.object.join()
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        meshes = [bpy.context.active_object]

    before_totals = {"verts": 0, "tris": 0, "open_edges": 0, "non_manifold_edges": 0, "islands": 0}
    after_totals = {"verts": 0, "tris": 0, "open_edges": 0, "non_manifold_edges": 0, "islands": 0}

    for obj in meshes:
        d_pre = mesh_diagnostics(obj)
        for k in before_totals:
            before_totals[k] += d_pre[k]

        bm = bmesh.new()
        bm.from_mesh(obj.data)
        if args.weld_dist > 0:
            bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=args.weld_dist)
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        bm.to_mesh(obj.data)
        bm.free()
        obj.data.update()

        d_post = mesh_diagnostics(obj)
        for k in after_totals:
            after_totals[k] += d_post[k]

    mn, mx, sz = scene_world_bbox(meshes)

    if args.out:
        out_path = Path(args.out).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        bpy.ops.export_scene.gltf(
            filepath=str(out_path),
            export_format="GLB",
            export_yup=True,
            export_apply=False,
            export_draco_mesh_compression_enable=False,
        )
        for obj in bpy.context.scene.objects:
            obj.rotation_mode = "XYZ"

    report = {
        "file": inp,
        "mesh_objects": len(meshes),
        "uint16_shards_detected": uint16_shards,
        "scale_anomalies_detected": scale_anomalies,
        "scale_anomalies_fixed": bool(args.fix_100x and scale_anomalies),
        "removed_widgets": removed_widgets,
        "bbox_min_blender": mn,
        "bbox_max_blender": mx,
        "bbox_size_m": sz,
        "before_weld": before_totals,
        "after_weld": after_totals,
    }
    print("IMPORT_AND_WELD_REPORT_JSON:" + json.dumps(report))


if __name__ == "__main__":
    main()
