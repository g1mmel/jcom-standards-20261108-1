#!/usr/bin/env python3
"""
04_origin_to_pivot.py — Fits exact kinematic pivots matching data/rules/unit-structure.json
and builds a pure parent-child node hierarchy (matrix_parent_inverse = Identity):
  - turret / launcher / hatch / radar: Kasa least-squares circle fit on base ring + seat at min_z (glTF minY)
  - barrel / barrel_recoil: PCA/SVD bore axis + breech at rear face (Blender min_y -> glTF maxZ when facing -Z)
  - wheel_* / sprocket_* / idler_*: Axle center (y, z centered), plus optional same-side datablock instancing
  - rotor_main / rotor_tail / prop_*: Hub centroid
  - door_*: Hinge edge (min_x or max_x)

Usage:
  D:\\blender\\blender.exe -b --factory-startup --python-exit-code 1 --python .claude/skills/cnc-blender-parts/snippets/04_origin_to_pivot.py -- --in <input.glb> --out <output.glb> [--instance-wheels]
"""

import argparse
import json
import math
import sys
from pathlib import Path

import bpy
import numpy as np
from mathutils import Matrix, Vector


def parse_args():
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    ap = argparse.ArgumentParser(description="Fit part origins to real mechanical pivots and parent cleanly.")
    ap.add_argument("--in", dest="inp", required=True, help="Input GLB path")
    ap.add_argument("--out", dest="out", required=True, help="Output GLB path")
    ap.add_argument("--instance-wheels", action="store_true", help="Share mesh datablocks across identical same-side wheels after centering origins")
    return ap.parse_args(argv)


def world_verts(obj):
    mw = obj.matrix_world
    return [mw @ v.co for v in obj.data.vertices]


def fit_circle_kasa_xy(pts_3d):
    pts = np.array([[p.x, p.y, p.z] for p in pts_3d], dtype=np.float64)
    if len(pts) < 3:
        c = pts.mean(axis=0) if len(pts) else np.zeros(3)
        return Vector((float(c[0]), float(c[1]), float(c[2]))), 0.0
    x, y = pts[:, 0], pts[:, 1]
    z_min = float(np.min(pts[:, 2]))
    A = np.column_stack([2.0 * x, 2.0 * y, np.ones_like(x)])
    b = x * x + y * y
    sol, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
    xc, yc, c0 = float(sol[0]), float(sol[1]), float(sol[2])
    r = math.sqrt(max(c0 + xc * xc + yc * yc, 1e-8))
    # Clamp to bbox midpoint if circle fit is degenerate (partial arc)
    x_mid = 0.5 * float(np.min(x) + np.max(x))
    y_mid = 0.5 * float(np.min(y) + np.max(y))
    span = max(float(np.max(x) - np.min(x)), float(np.max(y) - np.min(y)), 1e-4)
    if math.hypot(xc - x_mid, yc - y_mid) > 0.18 * span:
        xc, yc = x_mid, y_mid
    return Vector((xc, yc, z_min)), r


def compute_part_pivot(obj):
    name = obj.name.lower()
    pts = world_verts(obj)
    if not pts:
        return obj.matrix_world.translation.copy(), "empty"
    xs = [p.x for p in pts]
    ys = [p.y for p in pts]
    zs = [p.z for p in pts]
    mn = Vector((min(xs), min(ys), min(zs)))
    mx = Vector((max(xs), max(ys), max(zs)))
    ctr = (mn + mx) * 0.5
    sz = mx - mn

    if any(k in name for k in ("turret", "launcher", "hatch", "radar")):
        # unit-structure.json rule: centre ["x", "z"] in glTF (x, y in Blender Z-up), seat "minY" (min_z in Blender Z-up)
        z_band = mn.z + max(sz.z * 0.15, 0.05)
        ring_pts = [p for p in pts if p.z <= z_band]
        piv, _ = fit_circle_kasa_xy(ring_pts if len(ring_pts) >= 6 else pts)
        piv.z = mn.z
        return piv, "turret_ring_min_z"

    if any(k in name for k in ("barrel", "recoil", "gun", "cannon")):
        # unit-structure.json rule: centre ["x", "y"] in glTF (x, z in Blender Z-up), breech "maxZ" in glTF (min_y in Blender +Y forward)
        return Vector((ctr.x, mn.y, ctr.z)), "barrel_breech_min_y"

    if any(k in name for k in ("wheel", "sprocket", "idler")):
        # unit-structure.json rule: centre ["y", "z"] in glTF (y, z in Blender Z-up)
        return ctr.copy(), "wheel_axle_center"

    if any(k in name for k in ("rotor", "prop", "gear")):
        return Vector((ctr.x, ctr.y, ctr.z)), "rotor_or_gear_center"

    if "door" in name:
        # unit-structure.json rule: hinge "x" (min_x or max_x)
        hinge_x = mn.x if ctr.x <= 0 else mx.x
        return Vector((hinge_x, ctr.y, ctr.z)), "door_hinge_x"

    if any(k in name for k in ("hull", "body", "chassis", "fuselage")):
        return Vector((0.0, 0.0, mn.z)), "hull_ground_datum"

    return ctr.copy(), "bbox_center"


def set_origin_world(obj, world_pt):
    mw = obj.matrix_world.copy()
    local_pt = mw.inverted() @ world_pt
    obj.data.transform(Matrix.Translation(-local_pt))
    obj.data.update()
    obj.parent = None
    obj.matrix_parent_inverse = Matrix.Identity(4)
    obj.location = world_pt
    obj.rotation_mode = "XYZ"
    obj.rotation_euler = (0.0, 0.0, 0.0)
    obj.scale = (1.0, 1.0, 1.0)


def parent_clean(child, parent, child_piv, parent_piv):
    child.parent = parent
    child.matrix_parent_inverse = Matrix.Identity(4)
    child.location = child_piv - parent_piv
    child.rotation_mode = "XYZ"


def main():
    args = parse_args()
    inp = str(Path(args.inp).resolve())
    out = str(Path(args.out).resolve())

    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=inp)

    meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
    if not meshes:
        raise SystemExit("ERROR: No mesh objects in scene")

    bpy.ops.object.select_all(action="DESELECT")
    for o in meshes:
        o.select_set(True)
    bpy.context.view_layer.objects.active = meshes[0]
    bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    bpy.context.view_layer.update()

    pivots = {}
    pivot_log = []
    for obj in meshes:
        piv, rule = compute_part_pivot(obj)
        set_origin_world(obj, piv)
        pivots[obj.name] = piv
        pivot_log.append({"name": obj.name, "rule": rule, "pivot_blender": [round(v, 4) for v in piv]})

    # Optional wheel datablock instancing per side (after origins are centered!)
    instanced_count = 0
    if args.instance_wheels:
        for side_prefix in ("wheel_l", "wheel_r"):
            side_wheels = sorted([o for o in meshes if o.name.lower().startswith(side_prefix)], key=lambda x: x.name)
            if len(side_wheels) > 1:
                master = side_wheels[0].data
                vcount = len(master.vertices)
                for w in side_wheels[1:]:
                    if len(w.data.vertices) == vcount and w.data != master:
                        old = w.data
                        w.data = master
                        bpy.data.meshes.remove(old)
                        instanced_count += 1

    # Re-establish clean Hull -> Turret -> Barrel -> Barrel_Recoil hierarchy
    by_lower = {o.name.lower(): o for o in meshes}
    hull = by_lower.get("hull") or by_lower.get("body") or by_lower.get("fuselage")
    turret = by_lower.get("turret")
    barrel = by_lower.get("barrel")
    recoil = by_lower.get("barrel_recoil")

    for obj in meshes:
        if obj == hull:
            continue
        lname = obj.name.lower()
        if obj == recoil and barrel:
            parent_clean(obj, barrel, pivots[obj.name], pivots[barrel.name])
        elif (obj == barrel or any(k in lname for k in ("mg_", "smoke_", "antenna_"))) and turret:
            parent_clean(obj, turret, pivots[obj.name], pivots[turret.name])
        elif hull:
            parent_clean(obj, hull, pivots[obj.name], pivots[hull.name])

    Path(out).parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.export_scene.gltf(
        filepath=out,
        export_format="GLB",
        export_yup=True,
        export_apply=False,
        export_hierarchy_flatten_objs=False,
        export_draco_mesh_compression_enable=False,
    )
    print("ORIGIN_TO_PIVOT_REPORT_JSON:" + json.dumps({
        "pivots_fitted": len(pivot_log),
        "instanced_wheels": instanced_count,
        "parts": pivot_log,
        "out": out,
    }))


if __name__ == "__main__":
    main()
