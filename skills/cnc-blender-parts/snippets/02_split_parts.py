#!/usr/bin/env python3
"""
02_split_parts.py — Headless Blender 4.2 mesh splitter:
  - mode 'loose': BMesh connected-component extraction after spatial weld (never raw Edit-Mode separate)
                  with automatic vehicle station classification (hull, turret, barrel, wheel_*, sprocket_*, idler_*, track_*).
  - mode 'material': Split mesh by material slot into separate named objects.
  - mode 'bisect': Split mesh across a cutting plane into two separate objects.

Usage:
  D:\\blender\\blender.exe -b --factory-startup --python-exit-code 1 --python .claude/skills/cnc-blender-parts/snippets/02_split_parts.py -- --in <input.glb> --out <output.glb> --mode loose [--weld-dist 0.0001] [--turret-z-frac 0.55]
"""

import argparse
import json
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Vector


def parse_args():
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    ap = argparse.ArgumentParser(description="Split GLB mesh by loose parts, material, or bisect plane.")
    ap.add_argument("--in", dest="inp", required=True, help="Input GLB path")
    ap.add_argument("--out", dest="out", required=True, help="Output GLB path")
    ap.add_argument("--mode", choices=["loose", "material", "bisect"], default="loose", help="Split mode")
    ap.add_argument("--weld-dist", type=float, default=0.0001, help="Weld distance before loose-part walk (m)")
    ap.add_argument("--turret-z-frac", type=float, default=0.52, help="Height fraction above which centered shells belong to turret")
    ap.add_argument("--plane-co", default="0,0,1.5", help="Bisect plane point x,y,z in Blender space")
    ap.add_argument("--plane-no", default="0,0,1", help="Bisect plane normal nx,ny,nz in Blender space")
    return ap.parse_args(argv)


def extract_bmesh_islands(bm):
    bm.verts.ensure_lookup_table()
    bm.faces.ensure_lookup_table()
    visited = set()
    islands = []
    for v in bm.verts:
        if v.index not in visited:
            stack = [v]
            visited.add(v.index)
            c_verts = []
            c_faces = set()
            while stack:
                cur = stack.pop()
                c_verts.append(cur)
                for f in cur.link_faces:
                    c_faces.add(f)
                for e in cur.link_edges:
                    nb = e.other_vert(cur)
                    if nb.index not in visited:
                        visited.add(nb.index)
                        stack.append(nb)
            if not c_faces:
                continue
            xs = [p.co.x for p in c_verts]
            ys = [p.co.y for p in c_verts]
            zs = [p.co.z for p in c_verts]
            mn = Vector((min(xs), min(ys), min(zs)))
            mx = Vector((max(xs), max(ys), max(zs)))
            sz = mx - mn
            ctr = (mn + mx) * 0.5
            dims = tuple(sorted([round(sz.x, 2), round(sz.y, 2), round(sz.z, 2)]))
            islands.append({
                "faces": [f.index for f in c_faces],
                "vcount": len(c_verts),
                "sig": (len(c_verts), dims),
                "min": mn,
                "max": mx,
                "center": ctr,
                "size": sz,
            })
    return islands


def build_submesh_obj(bm_master, template_mesh, name, face_indices):
    keep = set(face_indices)
    sub = bm_master.copy()
    sub.faces.ensure_lookup_table()
    del_faces = [f for f in sub.faces if f.index not in keep]
    if del_faces:
        bmesh.ops.delete(sub, geom=del_faces, context="FACES")
    iso_verts = [v for v in sub.verts if not v.link_faces]
    if iso_verts:
        bmesh.ops.delete(sub, geom=iso_verts, context="VERTS")
    me = template_mesh.copy()
    me.name = f"{name}_mesh"
    sub.to_mesh(me)
    sub.free()
    me.update()
    obj = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(obj)
    return obj


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
    bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")
    bpy.ops.object.join()
    joined = bpy.context.active_object
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    for extra in [o for o in list(bpy.data.objects) if o != joined]:
        bpy.data.objects.remove(extra, do_unlink=True)

    created_names = []

    if args.mode == "material":
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.mesh.separate(type="MATERIAL")
        bpy.ops.object.mode_set(mode="OBJECT")
        for idx, o in enumerate([x for x in bpy.context.scene.objects if x.type == "MESH"]):
            mat_name = o.data.materials[0].name if o.data.materials and o.data.materials[0] else f"part_{idx}"
            o.name = f"mat_{idx}_{mat_name}"
            created_names.append(o.name)

    elif args.mode == "bisect":
        p_co = tuple(float(x) for x in args.plane_co.split(","))
        p_no = tuple(float(x) for x in args.plane_no.split(","))
        for part_name, c_in, c_out in [("hull", False, True), ("turret", True, False)]:
            bm = bmesh.new()
            bm.from_mesh(joined.data)
            geom = bm.verts[:] + bm.edges[:] + bm.faces[:]
            bmesh.ops.bisect_plane(
                bm, geom=geom, dist=0.0001,
                plane_co=p_co, plane_no=p_no,
                clear_inner=c_in, clear_outer=c_out,
            )
            me = joined.data.copy()
            me.name = f"{part_name}_mesh"
            bm.to_mesh(me)
            bm.free()
            me.update()
            o = bpy.data.objects.new(part_name, me)
            bpy.context.scene.collection.objects.link(o)
            created_names.append(o.name)
        bpy.data.objects.remove(joined, do_unlink=True)

    else:  # loose
        bm = bmesh.new()
        bm.from_mesh(joined.data)
        if args.weld_dist > 0:
            bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=args.weld_dist)
        islands = extract_bmesh_islands(bm)

        all_min = Vector((min(i["min"].x for i in islands), min(i["min"].y for i in islands), min(i["min"].z for i in islands)))
        all_max = Vector((max(i["max"].x for i in islands), max(i["max"].y for i in islands), max(i["max"].z for i in islands)))
        span = all_max - all_min
        turret_z = all_min.z + span.z * args.turret_z_frac

        # Detect repeated wheel shells in lower running-gear zone
        sig_groups = {}
        for isl in islands:
            if isl["vcount"] >= 24 and isl["max"].z < all_min.z + span.z * 0.50 and abs(isl["center"].x) > span.x * 0.22:
                sig_groups.setdefault(isl["sig"], []).append(isl)
        wheel_groups = [
            grp for grp in sig_groups.values()
            if len(grp) >= 4 and len(grp) % 2 == 0 and max(grp[0]["size"].y, grp[0]["size"].z) > span.z * 0.12
        ]
        wheel_groups.sort(key=lambda g: (len(g), max(g[0]["size"].y, g[0]["size"].z)), reverse=True)
        wheels = wheel_groups[0] if wheel_groups else []
        wheel_ids = {id(w) for w in wheels}

        buckets = {"hull": [], "turret": [], "barrel": [], "track_L": [], "track_R": []}
        for isl in islands:
            if id(isl) in wheel_ids:
                continue
            c, mn, mx, sz = isl["center"], isl["min"], isl["max"], isl["size"]
            # Barrel protrudes forward (+Y in Blender Z-up, or -Y depending on raw facing)
            if c.z >= turret_z and sz.y > sz.x * 2.2 and abs(c.x) < span.x * 0.22 and (mx.y > all_max.y - span.y * 0.18 or mn.y < all_min.y + span.y * 0.18):
                buckets["barrel"].append(isl)
            elif c.z >= turret_z and abs(c.x) < span.x * 0.38:
                buckets["turret"].append(isl)
            elif mx.z < turret_z and c.x < -span.x * 0.28:
                buckets["track_L"].append(isl)
            elif mx.z < turret_z and c.x > span.x * 0.28:
                buckets["track_R"].append(isl)
            else:
                buckets["hull"].append(isl)

        for b_name, isl_list in buckets.items():
            if isl_list:
                f_idx = [f for isl in isl_list for f in isl["faces"]]
                o = build_submesh_obj(bm, joined.data, b_name, f_idx)
                created_names.append(o.name)

        left_w = sorted([w for w in wheels if w["center"].x < 0], key=lambda w: w["center"].y, reverse=True)
        right_w = sorted([w for w in wheels if w["center"].x >= 0], key=lambda w: w["center"].y, reverse=True)
        for side, wlist in [("L", left_w), ("R", right_w)]:
            for idx, w in enumerate(wlist, start=1):
                o = build_submesh_obj(bm, joined.data, f"wheel_{side}{idx}", w["faces"])
                created_names.append(o.name)

        bm.free()
        bpy.data.objects.remove(joined, do_unlink=True)

    Path(out).parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.export_scene.gltf(
        filepath=out,
        export_format="GLB",
        export_yup=True,
        export_apply=False,
        export_draco_mesh_compression_enable=False,
    )
    print("SPLIT_PARTS_REPORT_JSON:" + json.dumps({
        "mode": args.mode,
        "parts_created": created_names,
        "count": len(created_names),
        "out": out,
    }))


if __name__ == "__main__":
    main()
