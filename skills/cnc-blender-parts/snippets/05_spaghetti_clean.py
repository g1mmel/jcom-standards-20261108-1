#!/usr/bin/env python3
"""
05_spaghetti_clean.py — Cleans AI-generated (Meshy/Tripo) or scanned spaghetti meshes
into game-ready topology within unit-structure.json triangle budgets:
  - Hard-surface (vehicle / aircraft / building): weld -> volume-preserving Laplacian de-wobble (if untextured)
    -> Planar Decimate (DISSOLVE) -> Beauty triangulate -> X-symmetric Collapse Decimate -> Tris-to-Quads
    -> sharp creases + Weighted Normals.
  - Organic (infantry): if single watertight sculpt (open_edges <= 500), Voxel pre-seal + QuadriFlow + Shrinkwrap
    (with silent no-op guard); if multi-sheet game rip, UV-preserving Collapse Decimate.

Usage:
  D:\\blender\\blender.exe -b --factory-startup --python-exit-code 1 --python .claude/skills/cnc-blender-parts/snippets/05_spaghetti_clean.py -- --in <input.glb> --out <output.glb> [--class vehicle] [--target-tris 6000]
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
    ap = argparse.ArgumentParser(description="Clean spaghetti AI/scanned meshes into RTS budget topology.")
    ap.add_argument("--in", dest="inp", required=True, help="Input GLB path")
    ap.add_argument("--out", dest="out", required=True, help="Output GLB path")
    ap.add_argument("--class", dest="uclass", choices=["vehicle", "aircraft", "building", "infantry"], default="vehicle")
    ap.add_argument("--target-tris", type=int, default=6000, help="Target triangle cap (default: 6000)")
    ap.add_argument("--planar-deg", type=float, default=0.0, help="Override planar dissolve angle in degrees (0 = class default)")
    return ap.parse_args(argv)


def mesh_stats(obj):
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    verts = len(bm.verts)
    faces = len(bm.faces)
    tris = sum(max(0, len(f.verts) - 2) for f in bm.faces)
    quads = sum(1 for f in bm.faces if len(f.verts) == 4)
    open_edges = sum(1 for e in bm.edges if e.is_boundary)
    bm.free()
    return {
        "verts": verts,
        "faces": faces,
        "tris": tris,
        "quad_ratio": round(quads / max(faces, 1), 4),
        "open_edges": open_edges,
    }


def sanitize_bmesh(obj, weld_dist, min_island_verts=12):
    try:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.mesh.customdata_custom_splitnormals_clear()
    except Exception:
        pass
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=weld_dist)

    # Prune tiny floating dust specks
    bm.verts.ensure_lookup_table()
    visited = set()
    to_del = []
    for v in bm.verts:
        if v.index not in visited:
            stack = [v]
            visited.add(v.index)
            comp = []
            while stack:
                cur = stack.pop()
                comp.append(cur)
                for e in cur.link_edges:
                    nb = e.other_vert(cur)
                    if nb.index not in visited:
                        visited.add(nb.index)
                        stack.append(nb)
            if len(comp) < min_island_verts:
                to_del.extend(comp)
    if to_del and len(to_del) < len(bm.verts) * 0.5:
        bmesh.ops.delete(bm, geom=to_del, context="VERTS")

    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(obj.data)
    bm.free()
    obj.data.update()


def main():
    args = parse_args()
    inp = str(Path(args.inp).resolve())
    out = str(Path(args.out).resolve())

    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=inp)

    meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
    if not meshes:
        raise SystemExit("ERROR: No mesh objects in scene")

    # Bake armature rest poses before joining so skinned imports never explode
    bpy.ops.object.select_all(action="DESELECT")
    for o in meshes:
        o.select_set(True)
    bpy.context.view_layer.objects.active = meshes[0]
    bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False)
    bpy.ops.object.convert(target="MESH")
    bpy.ops.object.join()
    obj = bpy.context.active_object
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    before = mesh_stats(obj)
    bbox_corners = [Vector(c) for c in obj.bound_box]
    diag = (max(bbox_corners, key=lambda v: v.length) - min(bbox_corners, key=lambda v: v.length)).length
    height = max(c.z for c in bbox_corners) - min(c.z for c in bbox_corners)

    sanitize_bmesh(obj, weld_dist=max(diag * 0.0002, 1e-5), min_island_verts=6 if args.uclass == "aircraft" else 14)
    post_weld = mesh_stats(obj)
    has_textures = any(m and m.use_nodes and any(n.type == "TEX_IMAGE" for n in m.node_tree.nodes) for m in obj.data.materials)

    method_used = ""
    if args.uclass == "infantry" and post_weld["open_edges"] <= 500:
        # Track D1: Watertight AI humanoid sculpt -> Voxel Pre-Seal + QuadriFlow + Shrinkwrap
        src_copy = obj.copy()
        src_copy.data = obj.data.copy()
        bpy.context.scene.collection.objects.link(src_copy)

        mod_vox = obj.modifiers.new("VoxelSeal", "REMESH")
        mod_vox.mode = "VOXEL"
        mod_vox.voxel_size = max(height * 0.006, 0.008)
        bpy.ops.object.modifier_apply(modifier=mod_vox.name)

        vox_faces = len(obj.data.polygons)
        target_quads = max(args.target_tris // 2, 500)
        bpy.ops.object.quadriflow_remesh(
            use_mesh_symmetry=False,
            use_preserve_sharp=False,
            use_preserve_boundary=False,
            smooth_normals=True,
            mode="FACES",
            target_faces=target_quads,
        )
        # Guard against QuadriFlow silent no-op on non-manifold voxels
        if len(obj.data.polygons) == vox_faces:
            mod_col = obj.modifiers.new("FallbackCollapse", "DECIMATE")
            mod_col.decimate_type = "COLLAPSE"
            mod_col.ratio = min(1.0, float(args.target_tris) / max(vox_faces * 2, 1))
            bpy.ops.object.modifier_apply(modifier=mod_col.name)
            method_used = "voxel_plus_collapse_fallback"
        else:
            method_used = "voxel_quadriflow_shrinkwrap"

        mod_sw = obj.modifiers.new("Shrinkwrap", "SHRINKWRAP")
        mod_sw.target = src_copy
        mod_sw.wrap_method = "NEAREST_SURFACEPOINT"
        bpy.ops.object.modifier_apply(modifier=mod_sw.name)
        bpy.data.objects.remove(src_copy, do_unlink=True)
    else:
        # Hard-surface or multi-sheet textured track (NEVER Voxel Remesh vehicles/aircraft!)
        planar_deg = args.planar_deg if args.planar_deg > 0 else (3.5 if args.uclass == "aircraft" else (3.2 if args.uclass == "building" else 5.5))
        if not has_textures and args.uclass in ("vehicle", "aircraft"):
            mod_sm = obj.modifiers.new("DeWobble", "LAPLACIANSMOOTH")
            mod_sm.iterations = 1
            mod_sm.lambda_factor = 0.12
            mod_sm.lambda_border = 0.01
            mod_sm.use_volume_preserve = True
            bpy.ops.object.modifier_apply(modifier=mod_sm.name)

        mod_pl = obj.modifiers.new("PlanarDissolve", "DECIMATE")
        mod_pl.decimate_type = "DISSOLVE"
        mod_pl.angle_limit = math.radians(planar_deg)
        mod_pl.delimit = {"UV", "MATERIAL", "SHARP", "SEAM"}
        bpy.ops.object.modifier_apply(modifier=mod_pl.name)

        # Triangulate planar N-gons before QEM Collapse
        bm = bmesh.new()
        bm.from_mesh(obj.data)
        bmesh.ops.triangulate(bm, faces=bm.faces, quad_method="BEAUTY", ngon_method="BEAUTY")
        bm.to_mesh(obj.data)
        bm.free()

        cur_tris = len(obj.data.polygons)
        if cur_tris > args.target_tris:
            mod_col = obj.modifiers.new("BudgetCollapse", "DECIMATE")
            mod_col.decimate_type = "COLLAPSE"
            mod_col.ratio = max(0.02, min(1.0, float(args.target_tris) / float(cur_tris)))
            mod_col.use_symmetry = True
            mod_col.symmetry_axis = "X"
            bpy.ops.object.modifier_apply(modifier=mod_col.name)

        # Pair coplanar triangles into clean quads and mark sharp edges
        bm = bmesh.new()
        bm.from_mesh(obj.data)
        bmesh.ops.join_triangles(
            bm,
            faces=bm.faces,
            angle_face_threshold=math.radians(38.0),
            angle_shape_threshold=math.radians(38.0),
        )
        sharp_rad = math.radians(34.0)
        for e in bm.edges:
            if len(e.link_faces) == 2:
                e.smooth = e.calc_face_angle(0.0) < sharp_rad
        for f in bm.faces:
            f.smooth = True
        bm.to_mesh(obj.data)
        bm.free()
        obj.data.update()

        mod_wn = obj.modifiers.new("WeightedNormal", "WEIGHTED_NORMAL")
        mod_wn.mode = "FACE_AREA_WITH_ANGLE"
        mod_wn.keep_sharp = True
        bpy.ops.object.modifier_apply(modifier=mod_wn.name)
        method_used = f"planar_{planar_deg}deg_collapse_weighted_normal"

    after = mesh_stats(obj)
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.export_scene.gltf(
        filepath=out,
        export_format="GLB",
        export_yup=True,
        export_apply=False,
        export_draco_mesh_compression_enable=False,
    )
    print("SPAGHETTI_CLEAN_REPORT_JSON:" + json.dumps({
        "class": args.uclass,
        "method": method_used,
        "before": before,
        "after_weld": post_weld,
        "after_clean": after,
        "out": out,
    }))


if __name__ == "__main__":
    main()
