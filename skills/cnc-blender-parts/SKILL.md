---
name: cnc-blender-parts
description: Headless Blender 4.2 playbook and tested bpy snippets for decomposing, cutting without seams, pivot-fitting, cleaning spaghetti topology, scaling to real metres (NASA VAB cap [OR-025]), and exporting GLBs that pass unit-structure-validator [OR-045]. Read before any Blender or 3D asset work in C:\cnc_rev.
---

# CNC Blender Parts Playbook (`cnc-blender-parts`)

Every Blender lane MUST read this playbook first. Do not re-invent mesh splits, boolean cuts, or pivot guesses. Use the tested snippets in `.claude/skills/cnc-blender-parts/snippets/`.

## 1. Hard Rules & CLI Invocation

- **Binary:** `D:\blender\blender.exe` (Blender 4.2.0 LTS).
- **Headless CLI only:** Always pass `-b --factory-startup --python-exit-code 1 --python <script.py> -- <args>`. Without `--python-exit-code 1`, Blender exits `0` on Python tracebacks.
- **One Blender at a time:** Never run two heavy headless Blender processes concurrently (causes `EXCEPTION_ACCESS_VIOLATION` / `Malloc returns null` in `BLI_array.hh`).
- **No video `[OR-012]`:** Render PNG diagnostic stills only. Never render MP4/WebM.
- **Never edit source assets in place:** Work on scratch copies, then write only your `OWNED` output path. Never run `git commit`, `push`, `checkout`, `reset`, `stash`, or `clean`.
- **Coordinate frame:**
  - **glTF 2.0 / Three.js runtime:** `1 unit = 1 metre`, **Up = `+Y`**, **Forward = `-Z`**, **Right = `+X`**, **Ground = `y = 0`** (ships keep design waterline `y = 0` when `minY < -1 m`).
  - **Blender 4.2 internal (Z-up) before `export_yup=True`:** **Up = `+Z`**, **Forward = `+Y`** (exports to glTF `-Z`), **Aft/Breech = `-Y`** (exports to glTF `+Z`), **Right = `+X`**.

---

## 2. Unit-Structure-Validator Contract (`data/rules/unit-structure.json`) `[OR-045]`

`tools/validators/unit-structure.mjs` scores every GLB (`STRUCTURED` = 100, `PARTIAL`, `STATIC`, `BROKEN`) against `data/rules/unit-structure.json` and `data/rules/unit-dimensions.json`. To earn `STRUCTURED`:

### 2.1 Required Node Names by Class
Node names are tokenized on non-alphanumeric delimiters (`wheel_L1` $\rightarrow$ `["wheel", "l1"]`). Every moving part must be a **separate glTF node** (not welded to `hull`):

| Class | Static Root Node | Required Moving Part Nodes | Notes |
| :--- | :--- | :--- | :--- |
| **`tank`** | `hull` (`body`, `chassis`) | `turret`, `barrel`, `barrel_recoil`, plus (`track_L`, `track_R` + `sprocket_L`, `sprocket_R`) or $\ge 4$ `wheel_*` | Recommended full kit: `wheel_L1..L6`, `wheel_R1..R6`, `sprocket_L/R`, `idler_L/R`, `track_L/R`. |
| **`wheeled`** | `hull` (`body`, `chassis`) | $\ge 4$ `wheel_*` (`wheel_L1..`, `wheel_R1..`) | Optional turret/gun follow tank naming. |
| **`truck`** | `hull` (`body`, `chassis`, `cab`) | $\ge 4$ `wheel_*` | Cargo bed may stay on `hull` unless articulated. |
| **`artillery`** | `hull` (`body`, `chassis`) | ($\ge 4$ `wheel_*` or `track_*`) + (`launcher`/`pod` or `barrel`/`gun`/`cannon`) | Elevate `launcher` or `barrel` around trunnion. |
| **`helicopter`** | `hull` (`fuselage`, `body`) | `rotor_main` + (`rotor_tail` or a 2nd `rotor_main` for coaxial) | Delete opaque `*blur*` / `*spin*` proxy disks first. |
| **`jet`** | `hull` (`fuselage`, `body`, `airframe`) | `gear_*` (`gear_nose`, `gear_L`, `gear_R`, `landing_gear`) | Optional `canopy`, `door_*`, control surfaces. |
| **`ship`** | `hull` (`body`) | At least one of: `prop_*`, `turret`, `launcher`, `radar` | Keep waterline at `y = 0` (`minY < -1 m` allowed). |
| **`submarine`** | `hull` (`body`) | `prop` (`propeller`) + `hatch` | Keep waterline/submerged datum intact. |
| **`infantry`** | Armature skin or `static` | Skinned rig (`minJoints >= 3`, `minClips >= 1`) OR node named `static` | Height must be $1.60\text{–}1.90\text{ m}$ (hard cap $\le 2.2\text{ m}$). |
| **`building`** | `hull` (`body`, `shell`) | `door` (`doors`, `door_leaf_port`, `door_leaf_stbd`) | Height $\le 160.02\text{ m}$ NASA VAB cap `[OR-025]`. |
| **`defence`** | `hull` / base | `turret` + (`barrel`/`gun`/`cannon` or `launcher`) | Base foundation stays static at `y = 0`. |

### 2.2 Required Local Pivots (`tolerances.pivots` in `data/rules/unit-structure.json`)
glTF has no separate pivot channel—a node rotates around its local `(0, 0, 0)`. Within `pivotFraction = 0.20` (or `0.05 m`):

| Pivot Type | Parts Using It | glTF Local `(X, Y, Z)` Rule | Blender Z-Up (`+Y` Forward) World Point |
| :--- | :--- | :--- | :--- |
| **`turret`** | `turret` | `X, Z` centered on ring; `Y = minY` (bottom seat) | `(ring_xc, ring_yc, min_z)` via Kåsa circle fit |
| **`barrel`** | `barrel`, `barrel_recoil` | `X, Y` centered on bore; `Z = maxZ` (aft breech end) | `(center_x, min_y, center_z)` at mantlet/trunnion |
| **`wheel`** | `wheel_*`, `sprocket_*`, `idler_*` | `Y, Z` centered on wheel disk | `(center_x, center_y, center_z)` axle midpoint |
| **`rotor`** | `rotor_main`, `rotor_tail`, `radar`, `gear` | `X, Z` centered on shaft/hub | `(center_x, center_y, center_z)` hub center |
| **`prop`** | `prop_*`, `propeller` | `X, Y` centered on screw shaft | `(center_x, center_y, center_z)` |
| **`launcher` / `hatch`** | `launcher`, `hatch` | `X, Z` centered; `Y = minY` (base hinge/seat) | `(center_x, center_y, min_z)` |
| **`door`** | `door_*` | `X` on hinge edge (`minX` or `maxX`) | `(min_x or max_x, center_y, center_z)` |

### 2.3 Budgets, Team Colour (`houseTint`), & Cleanliness Gates
- **Triangle caps (`lod0 / lod1 / lod2`):** `infantry`: `3000 / 1500 / 500` · `vehicle`: `8000 / 3000 / 1000` · `aircraft` & `ship`: `15000 / 5000 / 1500` · `structure` & `defence`: `6000 / 2500 / 800`.
- **Texture max edge (`lod0 / lod1 / lod2`):** `2048 / 1024 / 512` px (embedded PNG/JPEG; no Draco; `EXT_meshopt_compression` supported).
- **Team-colour slot:** At least one exported material (assigned to $\ge 1$ polygon so the glTF exporter does not strip it) must be named `houseTint` (or `team_colour` / `teamColour` / `TeamColor`).
- **Track material isolation:** Clone the material on `track_L` / `track_R` (`track_uv_*`) so scrolling track UVs in Three.js does not scroll the hull paint.
- **Unwelded moving parts & closed meshes:** Quantized vertex overlap (`weldQuantiseM = 0.01 m`) between moving parts and `hull` must be `< 8%` (`weldOverlapFraction = 0.08`). Open boundary edges must be `< 2%` of total edges (`openEdgeFraction = 0.02`).

---

## 3. What Goes Wrong, How to Detect It, How to Fix It

### Failure 1: Barrel / Turret Cut Leaves a Jagged Seam, Open Gap, or Hull-Bottom Lid
- **Why it happens:**
  1. Cutting a fused wedge gun with a box (`nose_box`) and leaving the cut loop uncapped leaves an open hollow chip that exposes the inside of the turret when pitched $+20^\circ$ or recoiled $+0.30\text{ m}$.
  2. Running `bmesh.ops.holes_fill(bm, edges=bm.edges, sides=0)` after a planar cut caps *every* pre-existing opening on the tank, stretching a giant flat polygon sheet across the open hull bottom and wheel arches (`+2,184` to `+6,904` garbage faces).
  3. Leaving the cap as a concave N-gon causes ear-clipping spikes on glTF export; unpinned cap UVs streak across the texture atlas.
  4. Running `BOOLEAN (solver='EXACT')` on a 200k-tri non-watertight Sketchfab tank takes $5+$ minutes and creates `78,001` non-manifold edges.
- **How to detect it:** `open_edges` increases after the cut, or `unit-structure.mjs` flags `openEdgeFraction > 0.02`; pitching `barrel` $+20^\circ$ or translating `barrel_recoil` $+0.30\text{ m}$ along `+Z` shows a gap between breech and mantlet.
- **How to fix it (`snippets/03_seam_safe_cuts.py`):**
  1. Slice in BMesh with `res = bmesh.ops.bisect_plane(...)`.
  2. Collect **only** the newly cut boundary edges: `cut_edges = [e for e in res["geom_cut"] if isinstance(e, bmesh.types.BMEdge) and e.is_boundary]`.
  3. Extrude `cut_edges` inward by `0.15–0.25 m` along `-plane_no` (`bmesh.ops.extrude_edge_only` + `bmesh.ops.translate`) to form a **recessed telescopic collar/trunnion sleeve** buried inside the mantlet/hull socket.
  4. Cap `cut_edges` with `bmesh.ops.holes_fill(bm, edges=cut_edges, sides=64)`, immediately triangulate `fill_res["faces"]` with `bmesh.ops.triangulate`, and pin cap loop UVs to a neutral dark metal coordinate `(0.05, 0.05)`.

### Failure 2: Inverted Normals, Black Patchy Shading, or Multi-User Apply Abort
- **Why it happens:** Negative mirror scales on wheels/turrets flip face winding inside-out; raw glTF imports carry broken custom split normals; calling `transform_apply` on instanced wheels aborts with `Cannot apply to a multi user`. Additionally, Blender 4.1+ removed `mesh.use_auto_smooth`.
- **How to detect it:** Backface culling in Three.js shows missing wheels/turret cheeks, or judge renders flag dark diagonal shading patches across flat armor glacis plates.
- **How to fix it (`snippets/01_import_and_weld.py` & `05_spaghetti_clean.py`):**
  1. Always run `bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False)` **before** `bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)`.
  2. Clear corrupted split normals with `bpy.ops.mesh.customdata_custom_splitnormals_clear()`.
  3. After welding (`remove_doubles(dist=0.0001)`), run `bmesh.ops.recalc_face_normals(bm, faces=bm.faces)`.
  4. Mark sharp edges at $34^\circ$ (`e.smooth = e.calc_face_angle(0.0) < math.radians(34.0)`) and apply `WEIGHTED_NORMAL (mode='FACE_AREA_WITH_ANGLE', keep_sharp=True)`.

### Failure 3: Wrong Pivot (Turret Wobbles Out of Socket, Barrel Pitches Around Mid-Tube, Wheels Orbit Hull)
- **Why it happens:**
  1. `ORIGIN_CENTER_OF_MASS` or `ORIGIN_GEOMETRY` on a turret pulls the pivot $0.5\text{–}1.3\text{ m}$ forward (toward the gun) or aft (toward the bustle basket), making the turret slide off the hull when yawed $90^\circ$.
  2. `ORIGIN_GEOMETRY` on a gun barrel puts the pivot at mid-tube instead of the breech (`maxZ` in glTF / `min_y` in Blender), so pitching $+20^\circ$ swings the breech out through the turret roof.
  3. Linking wheel datablocks (`w_obj.data = master_mesh`) *before* centering each wheel's origin teleports all 6 wheels onto Wheel #1.
  4. `bpy.ops.export_scene.gltf()` **mutates `obj.rotation_mode = 'QUATERNION'` in-place**, causing any subsequent `obj.rotation_euler` pose check to silently do nothing!
- **How to detect it:** `unit-structure.mjs` fails the `pivots` check (`turret` not at `x,z` center + `minY`, `barrel` not at `maxZ` breech, `wheel` not at `y,z` center), or a $+90^\circ$ yaw / $+20^\circ$ pitch test displaces the joint.
- **How to fix it (`snippets/04_origin_to_pivot.py`):**
  1. **Turret:** Fit a Kåsa least-squares circle (`np.linalg.lstsq`) to the lower ring vertices ($z \in [z_{\min}, z_{\min} + 0.15\Delta z]$) and set `z = min_z`. If the turret was modeled at a baked yaw angle (e.g. $+25^\circ$ on the raw Merkava), un-rotate it around the fitted ring center before setting rest transforms.
  2. **Barrel & Recoil:** Set origin to `(center_x, min_y, center_z)` in Blender Z-up (`+Y` forward), which exports to `(center_x, center_y, maxZ)` in glTF (`-Z` forward).
  3. **Wheels:** Set each wheel's origin to its bbox/rim center `(center_x, center_y, center_z)` via `mesh.transform(Matrix.Translation(-local_piv))` **first**, then link same-side duplicates (`w_obj.data = master_l_mesh`, keeping Left and Right masters separate so outward hub caps never flip inward).
  4. **Parenting:** Always set `child.parent = parent`, `child.matrix_parent_inverse = Matrix.Identity(4)`, `child.location = child_world_piv - parent_world_piv`, and `child.rotation_mode = 'XYZ'`.

### Failure 4: Scale Off by 100x / 1000x, Child Node `0.01` Mismatch, or VAB Height Violation `[OR-025]`
- **Why it happens:**
  1. FBX/CAD centimetre or millimetre models exported to glTF without unit conversion produce a $208\text{ m}$ soldier (taller than the NASA VAB!) or a $0.39\text{ m}$ adobe house.
  2. Mixed-scale kitbashes (like `wasp-class-lhd/lod0.glb`) leave `Recovered_Source_wasp_*` hull nodes at `scale = [0.01, 0.01, 0.01]` ($2.57\text{ m}$ long) while sibling CIWS/elevator nodes sit at `scale = [1, 1, 1]` ($242\text{ m}$ away).
  3. Joining rigged Sketchfab meshes (`sf_humanoid_rebel.glb`) before baking the Armature rest pose shoots vertex coordinates to $Z = 21,799\text{ m}$.
- **How to detect it:** Run `node scripts/glbbox.cjs <file.glb>` or `snippets/06_scale_and_facing_check.py`. Any ordinary building taller than the **NASA VAB (`160.02 m` tall, `218 m` long, `158 m` wide)** violates `[OR-025]` unless flagged `rocketAssembly`, `residentialCity`, or listed in `tallNonBuildings` in `data/rules/unit-dimensions.json`.
- **How to fix it (`snippets/01_import_and_weld.py` & `06_scale_and_facing_check.py`):**
  1. Pass `--fix-100x` to `01_import_and_weld.py` to normalize `0.01` child nodes, and `--bake-armature` (`convert(target='MESH')` + `parent_clear(type='CLEAR_KEEP_TRANSFORM')`) before joining skinned meshes.
  2. Run `06_scale_and_facing_check.py --unit-key <key> --fix` to scale the root to the exact target metres in `data/rules/unit-dimensions.json`, enforce the `160.02 m` VAB ceiling `[OR-025]`, align the long horizontal axis to glTF `Z` (`Forward = -Z`), and snap `minY = 0.0000`.

### Failure 5: Unwelded `uint16` Shards & Spaghetti Remesh Traps
- **Why it happens:**
  1. glTF splits meshes at `65,532` vertices (`uint16` index limit) and duplicates vertices along every hard normal and UV seam (`282,799` open edges / `35,019` fragments on the Merkava; `39,443` open edges on Meshy `02-tank`). Calling `bpy.ops.mesh.separate(type='LOOSE')` in Edit Mode before welding spawns $35,000$ objects and freezes Blender.
  2. Running **Voxel Remesh** or **QuadriFlow** on a hard-surface vehicle or aircraft amputates thin gun barrels, pitot tubes, and rotor blades, and rounds $90^\circ$ armor edges.
  3. `bpy.ops.object.quadriflow_remesh()` silently returns `{'FINISHED'}` while changing zero faces whenever the input has a single non-manifold or inconsistent-normal edge.
  4. `DECIMATE (UNSUBDIV)` crashes Blender 4.2 with `EXCEPTION_ACCESS_VIOLATION` on Marching-Cubes triangle soup.
- **How to fix it (`snippets/02_split_parts.py` & `05_spaghetti_clean.py`):**
  1. Join `65,532`-vert shards first, weld at `dist = 0.0001 m`, and traverse connected components in **BMesh** (`02_split_parts.py --mode loose`).
  2. For hard-surface spaghetti (`vehicle`, `aircraft`, `building`), never Voxel Remesh: run `05_spaghetti_clean.py` (`remove_doubles` $\rightarrow$ volume-preserving `LAPLACIANSMOOTH` if untextured $\rightarrow$ `DECIMATE(DISSOLVE)` at $3.2^\circ\text{–}5.5^\circ$ $\rightarrow$ Beauty triangulate $\rightarrow$ X-symmetric `DECIMATE(COLLAPSE)` to budget $\rightarrow$ `join_triangles` $\rightarrow$ `WEIGHTED_NORMAL`).

### Failure 6: Tread sheets cover the hull, or a tank ships with no treads
- **Why it happens:** A track box built from the whole hull side band is hull-height (MBT `track_l` about 0.09 x 1.24 x 7.6 m) and paints stripes over the armour. A hover hull with the same helper becomes a slab the size of the body. A tank that already has four or more wheels skips the sheets, so the AoI T-72 ships with wheels and no `track_l` / `track_r`. Stuffing 1.5 cm cubes into an artillery hull to duck the open-edge cap leaves the real holes and makes the catalog lie about the mesh.
- **How to fix it:** A tank-class file always has `track_l` and `track_r`, and keeps its road wheels. The sheet is a thin band along the road-wheel run (wheel length, about one wheel-diameter tall, about 1.5 cm thick), with the stripe UV on that sheet only. A hull with no wheels gets a skirt on the lower side, not a box the height of the turret. Close the real boundary edges. Do not join filler cubes into the hull. Measure the band from road wheels only — return rollers on top of the run stretch the sheet to hull height, and both sheets span the full run even when one side's wheels fail the slab filter. Seat a no-wheel skirt on the hull width inside its own low band, or it floats off a tapered hull. A glTF import arrives unwelded: a stuffed 1.5 cm cube reads as six 2-face islands, so collect tiny islands first and delete after the walk — deleting inside the walk shifts face indices and skips half of them. Then weld at the validator's 1 cm quantise and cap holes with Blender's own `fill_holes`; a hand loop-walk chains wrongly where three boundary edges share a vertex.

---

## 4. Tested Snippet Reference (`.claude/skills/cnc-blender-parts/snippets/`)

Run any snippet headlessly via:
```powershell
& "D:\blender\blender.exe" -b --factory-startup --python-exit-code 1 --python C:\cnc_rev\.claude\skills\cnc-blender-parts\snippets\<script.py> -- <args>
```

1. **`01_import_and_weld.py`**: `--in <in.glb> [--out <out.glb>] [--weld-dist 0.0001] [--fix-100x] [--join-shards] [--bake-armature]`
   Strips `glTF_not_exported` widgets, fixes `0.01` child scale mismatches, bakes armatures, makes multi-user meshes single-user, joins `uint16` shards, welds UV seams, and recalculates outside normals.
2. **`02_split_parts.py`**: `--in <in.glb> --out <out.glb> --mode loose|material|bisect [--weld-dist 0.0001] [--turret-z-frac 0.52]`
   Splits welded BMesh into `hull`, `turret`, `barrel`, `track_L`, `track_R`, `wheel_L1..`, `wheel_R1..` without Edit-Mode scene-graph freezes.
3. **`03_seam_safe_cuts.py`**: `--in <in.glb> --out <out.glb> [--plane-co x,y,z] [--plane-no nx,ny,nz] [--max-sides 64] [--sleeve-depth 0.15]`
   Slices fused hulls/turrets/barrels with `bmesh.ops.bisect_plane`, extrudes a recessed telescopic sleeve, caps **only** `res["geom_cut"]` loops (`sides=64`), triangulates caps, and pins cap UVs.
4. **`04_origin_to_pivot.py`**: `--in <in.glb> --out <out.glb> [--instance-wheels]`
   Fits Kåsa circle pivots for turrets (`min_z` seat), breech pivots (`min_y` $\rightarrow$ glTF `maxZ`) for barrels, axle centers for wheels (with same-side datablock instancing), and parents with `matrix_parent_inverse = Identity`.
5. **`05_spaghetti_clean.py`**: `--in <in.glb> --out <out.glb> --class vehicle|aircraft|building|infantry [--target-tris 6000]`
   Cleans Meshy/Sketchfab spaghetti into budget topology with Planar + Collapse + Weighted Normals (hard-surface) or Voxel + QuadriFlow + Shrinkwrap with no-op fallback (watertight infantry).
6. **`06_scale_and_facing_check.py`**: `--in <in.glb> [--out <out.glb>] [--unit-key <key>] [--class <cls>] [--fix]`
   Verifies and fixes metre scale against `data/rules/unit-dimensions.json`, enforces the `160.02 m` NASA VAB height cap `[OR-025]`, rotates sideways hulls to `-Z` forward, and snaps `minY = 0`.
7. **`07_export_glb.py`**: `--in <in.glb> --out <out.glb> [--ensure-house-tint] [--clone-track-mat]`
   Binds an active `houseTint` material slot, clones `track_uv_*` materials, exports GLB (`export_yup=True, export_apply=False`), restores `rotation_mode = 'XYZ'`, and prints the verified GLB bbox and node list.

After exporting, always verify with:
```powershell
node C:\cnc_rev\scripts\glbbox.cjs <out.glb>
```
