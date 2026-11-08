#!/usr/bin/env python3
"""
03_seam_safe_cuts.py — Seam-safe planar cut + surgical cut-loop capping + neutral UV pinning
+ optional recessed telescopic collar so barrel pitch/recoil and turret yaw never expose a seam gap.

Usage:
  D:\\blender\\blender.exe -b --factory-startup --python-exit-code 1 --python .claude/skills/cnc-blender-parts/snippets/03_seam_safe_cuts.py -- --in <input.glb> --out <output.glb> [--plane-co 0,0,1.2] [--plane-no 0,0,1] [--max-sides 64] [--sleeve-depth 0.20]
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
    ap = argparse.ArgumentParser(description="Seam-safe planar cut with cut-only hole fill, triangulation, UV pinning, and telescopic sleeve.")
    ap.add_argument("--in", dest="inp", required=True, help="Input GLB path")
    ap.add_argument("--out", dest="out", required=True, help="Output GLB path")
    ap.add_argument("--plane-co", default="", help="Cut plane origin x,y,z (default: auto mid-height)")
    ap.add_argument("--plane-no", default="0,0,1", help="Cut plane normal nx,ny,nz (default: 0,0,1)")
    ap.add_argument("--lower-name", default="hull", help="Name for inner/lower half (default: hull)")
    ap.add_argument("--upper-name", default="turret", help="Name for outer/upper half (default: turret)")
    ap.add_argument("--max-sides", type=int, default=64, help="Max boundary loop sides to cap (never 0 on open hulls)")
    ap.add_argument("--neutral-uv", default="0.05,0.05", help="UV coordinate for new cap faces to prevent atlas smearing")
    ap.add_argument("--sleeve-depth", type=float, default=0.15, help="Depth (m) to extrude a recessed telescopic collar into the socket (0 to disable)")
    return ap.parse_args(argv)


def slice_and_cap_bmesh(src_mesh, name, plane_co, plane_no, clear_inner, clear_outer, max_sides, neutral_uv, sleeve_vec=None):
    bm = bmesh.new()
    bm.from_mesh(src_mesh)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0002)
    uv_layer = bm.loops.layers.uv.active

    geom = bm.verts[:] + bm.edges[:] + bm.faces[:]
    res = bmesh.ops.bisect_plane(
        bm,
        geom=geom,
        dist=0.0001,
        plane_co=plane_co,
        plane_no=plane_no,
        clear_inner=clear_inner,
        clear_outer=clear_outer,
    )

    # CRITICAL: Filter ONLY to edges created by the cut (res["geom_cut"]) that are now boundary edges.
    # Never run holes_fill on all bm.edges or with sides=0, or open hull bottoms get lidded!
    cut_edges = [e for e in res.get("geom_cut", []) if isinstance(e, bmesh.types.BMEdge) and e.is_boundary]
    cut_edge_count = len(cut_edges)

    # Optional telescopic sleeve extrusion before capping so pitching/recoiling parts never show a gap
    if cut_edges and sleeve_vec is not None and sleeve_vec.length > 1e-5:
        ext_res = bmesh.ops.extrude_edge_only(bm, edges=cut_edges)
        ext_verts = [g for g in ext_res.get("geom", []) if isinstance(g, bmesh.types.BMVert)]
        bmesh.ops.translate(bm, verts=ext_verts, vec=sleeve_vec)
        if uv_layer:
            for f in [g for g in ext_res.get("geom", []) if isinstance(g, bmesh.types.BMFace)]:
                for loop in f.loops:
                    loop[uv_layer].uv = neutral_uv
        cut_edges = [g for g in ext_res.get("geom", []) if isinstance(g, bmesh.types.BMEdge) and g.is_boundary]

    cap_tris_added = 0
    if cut_edges and max_sides > 0:
        fill_res = bmesh.ops.holes_fill(bm, edges=cut_edges, sides=max_sides)
        new_faces = fill_res.get("faces", [])
        if new_faces:
            # Always triangulate cap N-gons so concave turret rings never ear-clip on glTF export
            tri_res = bmesh.ops.triangulate(bm, faces=new_faces, quad_method="BEAUTY", ngon_method="BEAUTY")
            tri_faces = tri_res.get("faces", [])
            cap_tris_added = len(tri_faces)
            if uv_layer:
                for f in tri_faces:
                    for loop in f.loops:
                        loop[uv_layer].uv = neutral_uv

    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    open_after = sum(1 for e in bm.edges if e.is_boundary)
    tris_after = sum(max(0, len(f.verts) - 2) for f in bm.faces)

    new_me = src_mesh.copy()
    new_me.name = f"{name}_mesh"
    bm.to_mesh(new_me)
    bm.free()
    new_me.update()

    new_obj = bpy.data.objects.new(name, new_me)
    bpy.context.scene.collection.objects.link(new_obj)
    return new_obj, {
        "name": name,
        "tris": tris_after,
        "cut_edges_detected": cut_edge_count,
        "cap_tris_added": cap_tris_added,
        "open_edges_after": open_after,
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

    bpy.ops.object.select_all(action="DESELECT")
    for o in meshes:
        o.select_set(True)
    bpy.context.view_layer.objects.active = meshes[0]
    bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False)
    bpy.ops.object.join()
    joined = bpy.context.active_object
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    zs = [v.co.z for v in joined.data.vertices]
    xs = [v.co.x for v in joined.data.vertices]
    ys = [v.co.y for v in joined.data.vertices]
    if args.plane_co:
        plane_co = Vector(tuple(float(v) for v in args.plane_co.split(",")))
    else:
        z_cut = min(zs) + (max(zs) - min(zs)) * 0.55
        plane_co = Vector(((min(xs) + max(xs)) * 0.5, (min(ys) + max(ys)) * 0.5, z_cut))

    plane_no = Vector(tuple(float(v) for v in args.plane_no.split(","))).normalized()
    uv_pt = tuple(float(v) for v in args.neutral_uv.split(","))
    sleeve_vec = -plane_no * float(args.sleeve_depth) if args.sleeve_depth > 0 else None

    lower_obj, lower_stats = slice_and_cap_bmesh(
        joined.data, args.lower_name, plane_co, plane_no,
        clear_inner=False, clear_outer=True,
        max_sides=args.max_sides, neutral_uv=uv_pt, sleeve_vec=None,
    )
    upper_obj, upper_stats = slice_and_cap_bmesh(
        joined.data, args.upper_name, plane_co, plane_no,
        clear_inner=True, clear_outer=False,
        max_sides=args.max_sides, neutral_uv=uv_pt, sleeve_vec=sleeve_vec,
    )

    bpy.data.objects.remove(joined, do_unlink=True)

    Path(out).parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.export_scene.gltf(
        filepath=out,
        export_format="GLB",
        export_yup=True,
        export_apply=False,
        export_draco_mesh_compression_enable=False,
    )
    print("SEAM_SAFE_CUT_REPORT_JSON:" + json.dumps({
        "plane_co": [round(v, 4) for v in plane_co],
        "plane_no": [round(v, 4) for v in plane_no],
        "sleeve_depth_m": args.sleeve_depth,
        "lower": lower_stats,
        "upper": upper_stats,
        "out": out,
    }))


if __name__ == "__main__":
    main()
