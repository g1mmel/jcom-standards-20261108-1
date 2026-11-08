#!/usr/bin/env python3
"""
06_scale_and_facing_check.py — Real-scale, NASA VAB height cap [OR-025], ground datum (y=0),
and forward facing (-Z in glTF / +Y in Blender Z-up) checker & fixer.

Reads C:\\cnc_rev\\data\\rules\\unit-dimensions.json (ADR-010).
Enforces [OR-025]: ordinary buildings cannot exceed NASA VAB height (160.02 m) unless
rocketAssembly, residentialCity, or listed in tallNonBuildings.

Usage:
  D:\\blender\\blender.exe -b --factory-startup --python-exit-code 1 --python .claude/skills/cnc-blender-parts/snippets/06_scale_and_facing_check.py -- --in <input.glb> [--out <output.glb>] [--unit-key jslc.vehicle.deck-tow-tractor] [--class vehicle] [--fix]
"""

import argparse
import json
import sys
from pathlib import Path

import bpy
from mathutils import Matrix, Vector

VAB_HEIGHT_CAP_M = 160.02
VAB_LENGTH_CAP_M = 218.0
VAB_WIDTH_CAP_M = 158.0


def parse_args():
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    ap = argparse.ArgumentParser(description="Check and optionally fix real-world scale, VAB cap [OR-025], ground datum, and facing.")
    ap.add_argument("--in", dest="inp", required=True, help="Input GLB path")
    ap.add_argument("--out", dest="out", default="", help="Optional output GLB path")
    ap.add_argument("--rules", default=r"C:\cnc_rev\data\rules\unit-dimensions.json", help="Path to unit-dimensions.json")
    ap.add_argument("--unit-key", default="", help="Key in unit-dimensions.json entries or classes (e.g. Tank, Structure)")
    ap.add_argument("--class", dest="uclass", default="vehicle", help="Fallback category: vehicle, infantry, aircraft, ship, building, defense")
    ap.add_argument("--fix", action="store_true", help="Apply uniform/footprint scale fix, rotate sideways hull to +Y, and ground min_z=0")
    return ap.parse_args(argv)


def compute_scene_bounds(meshes):
    mn = Vector((1e9, 1e9, 1e9))
    mx = Vector((-1e9, -1e9, -1e9))
    for obj in meshes:
        mw = obj.matrix_world
        for v in obj.data.vertices:
            w = mw @ v.co
            mn.x = min(mn.x, w.x)
            mn.y = min(mn.y, w.y)
            mn.z = min(mn.z, w.z)
            mx.x = max(mx.x, w.x)
            mx.y = max(mx.y, w.y)
            mx.z = max(mx.z, w.z)
    return mn, mx, mx - mn


def lookup_target_dims(rules_path, unit_key, uclass):
    p = Path(rules_path)
    if not p.exists():
        return None, False
    data = json.loads(p.read_text(encoding="utf-8"))
    tall_non = set(data.get("tallNonBuildings", []))
    entries = data.get("entries", {})
    classes = data.get("classes", {})
    row = entries.get(unit_key) or classes.get(unit_key)
    if not row:
        cmap = {
            "infantry": "Rifleman",
            "vehicle": "Tank",
            "tank": "Tank",
            "aircraft": "Aircraft",
            "building": "Structure",
            "structure": "Structure",
            "defense": "DefenceTurret",
            "defence": "DefenceTurret",
        }
        row = classes.get(cmap.get(uclass.lower(), "Tank"))
    is_exempt = (
        unit_key in tall_non
        or bool(row and (row.get("rocketAssembly") or row.get("residentialCity") or row.get("category") == "tallNonBuilding"))
    )
    return row, is_exempt


def main():
    args = parse_args()
    inp = str(Path(args.inp).resolve())

    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=inp)

    meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
    if not meshes:
        raise SystemExit("ERROR: No mesh objects in scene")

    mn, mx, sz = compute_scene_bounds(meshes)
    # In Blender Z-up: X = width, Y = length (maps to glTF -Z forward), Z = height (maps to glTF +Y up)
    width_m, length_m, height_m = float(sz.x), float(sz.y), float(sz.z)

    row, vab_exempt = lookup_target_dims(args.rules, args.unit_key, args.uclass)
    issues = []
    fixes_applied = []

    # 1. Detect 100x / 0.01x scale errors (e.g. 208 m soldier or 0.39 m house)
    max_span = max(width_m, length_m, height_m)
    scale_factor = 1.0
    if row:
        fit_axis = row.get("fit", "length")
        target_val = float(row.get("heightM", 1.85) if fit_axis == "height" else row.get("lengthM", 9.7))
        measured_val = height_m if fit_axis == "height" else max(width_m, length_m)
        ratio = measured_val / max(target_val, 1e-4)
        if ratio > 50.0 or ratio < 0.02:
            issues.append(f"100x scale bug: measured {measured_val:.2f}m vs target {target_val:.2f}m (ratio {ratio:.2f}x)")
            scale_factor = target_val / max(measured_val, 1e-6)
        elif ratio < 0.5 or ratio > 2.0:
            issues.append(f"Scale off target: measured {measured_val:.2f}m vs target {target_val:.2f}m (ratio {ratio:.2f}x)")
            scale_factor = target_val / max(measured_val, 1e-6)

    # 2. Enforce NASA VAB height cap [OR-025] (160.02 m)
    cat = (row.get("category") if row else args.uclass).lower()
    if cat in ("building", "structure", "defense", "defence") and not vab_exempt:
        check_h = height_m * (scale_factor if args.fix else 1.0)
        if check_h > VAB_HEIGHT_CAP_M:
            issues.append(f"[OR-025] VAB height cap exceeded: {check_h:.2f}m > {VAB_HEIGHT_CAP_M}m (NASA VAB ceiling)")
            if args.fix:
                scale_factor = VAB_HEIGHT_CAP_M / max(height_m, 1e-6)

    # 3. Check facing: for non-buildings, length along Blender Y (glTF Z) should exceed width along X (unless winged aircraft)
    sideways = False
    if cat in ("vehicle", "tank", "ship") and width_m > length_m * 1.15:
        sideways = True
        issues.append(f"Sideways orientation: X extent ({width_m:.2f}m) > Y extent ({length_m:.2f}m); glTF forward must be -Z (Blender +Y)")

    # 4. Check ground datum (min_z should be 0.0 within 0.05m, except ships with underwater hull draft min_z < -1.0m)
    is_waterline_ship = cat in ("ship", "naval") and mn.z < -1.0
    ground_err = float(mn.z)
    if not is_waterline_ship and abs(ground_err) > 0.05:
        issues.append(f"Ground offset error: min_z = {ground_err:.4f}m (expected 0.0000m)")

    if args.fix:
        bpy.ops.object.select_all(action="DESELECT")
        for o in meshes:
            o.select_set(True)
        bpy.context.view_layer.objects.active = meshes[0]
        bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False)

        if sideways:
            rot_z = Matrix.Rotation(1.57079632679, 4, "Z")
            for o in [x for x in bpy.context.scene.objects if x.parent is None]:
                o.matrix_world = rot_z @ o.matrix_world
            fixes_applied.append("rotated_90deg_Z_to_align_forward_plus_Y")

        if abs(scale_factor - 1.0) > 0.01:
            s_mat = Matrix.Scale(scale_factor, 4)
            for o in [x for x in bpy.context.scene.objects if x.parent is None]:
                o.matrix_world = s_mat @ o.matrix_world
            fixes_applied.append(f"scaled_by_{scale_factor:.4f}")

        bpy.context.view_layer.update()
        mn, mx, sz = compute_scene_bounds(meshes)
        if not is_waterline_ship and abs(mn.z) > 1e-4:
            dz = -mn.z
            for o in [x for x in bpy.context.scene.objects if x.parent is None]:
                o.location.z += dz
            bpy.context.view_layer.update()
            fixes_applied.append(f"grounded_by_{dz:.4f}m")
            mn, mx, sz = compute_scene_bounds(meshes)

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

    report = {
        "file": inp,
        "unit_key": args.unit_key or args.uclass,
        "category": cat,
        "vab_cap_m": VAB_HEIGHT_CAP_M,
        "vab_exempt": vab_exempt,
        "extents_gltf_xyz_m": [round(float(sz.x), 3), round(float(sz.z), 3), round(float(sz.y), 3)],
        "ground_min_y_m": round(float(mn.z), 4),
        "long_horizontal_axis": "Z (ok)" if sz.y >= sz.x else "X (SIDEWAYS)",
        "issues": issues,
        "fixes_applied": fixes_applied,
    }
    print("SCALE_AND_FACING_REPORT_JSON:" + json.dumps(report))


if __name__ == "__main__":
    main()
