---
name: sage-modding-formats
description: Authoritative technical standard for Westwood/EA SAGE (SAGE1 and SAGE2) file formats, chunk hierarchies, compression algorithms, StreamFS schemas, map chunk architectures, modding tools, and conversion pipelines.
---

# SAGE and SAGE2 Modding & File Formats: Engineering Standard

This standard specifies the binary structures, serialization algorithms, memory layouts, chunk hierarchies, coordinate conventions, and tool pipelines for Electronic Arts' Strategy Action Game Engine (SAGE1: *Generals*, *Zero Hour*; SAGE2: *Battle for Middle-earth II*, *Command & Conquer 3: Tiberium Wars / Kane's Wrath*, *Red Alert 3*, and *Generals Universe*).

---

## 1. Container & Compression Formats

### 1.1 EA BIG / BIG4 Archive (`.big`)
The `.big` archive format is the primary container for SAGE and SAGE2 assets. It uses a hybrid endian layout: archive-level length is Little-Endian, while archive counts and entry tables are Big-Endian.

#### Header Layout
| Offset | Size (bytes) | Type | Endian | Field | Description |
|---|---|---|---|---|---|
| `0x00` | 4 | `char[4]` | ASCII | `Magic` | `"BIG4"` or `"BIGF"` |
| `0x04` | 4 | `uint32` | Little-Endian | `ArchiveSize` | Total byte size of the `.big` file on disk |
| `0x08` | 4 | `uint32` | Big-Endian | `FileCount` | Total number of embedded files |
| `0x0C` | 4 | `uint32` | Big-Endian | `HeaderSize` | Byte size of the archive header and index table |

#### Index Entry Layout (Repeated `FileCount` times)
| Offset | Size (bytes) | Type | Endian | Field | Description |
|---|---|---|---|---|---|
| `0x00` | 4 | `uint32` | Big-Endian | `DataOffset` | Absolute byte offset of file payload from start of archive |
| `0x04` | 4 | `uint32` | Big-Endian | `DataSize` | Uncompressed byte length of file payload |
| `0x08` | Variable | `char[]` | ASCII | `FilePath` | Relative file path terminated with null byte `0x00` (`\` separated) |

Entries are alphabetically sorted case-insensitively. Payloads follow immediately after `HeaderSize`.

---

### 1.2 EA RefPack (LZ77/LZSS Derivative) Compression
RefPack is EA's standard LZ77-based compression algorithm used across SAGE `.map` files, textures, and archives.

#### Header Signatures
1. **EAR Wrapper (`.map` files):**
   - Bytes `0x00..0x03`: ASCII `"EAR\0"` (`0x45 0x41 0x52 0x00`).
   - Bytes `0x04..0x07`: `uint32` Little-Endian uncompressed size.
   - Byte `0x08..`: The raw RefPack compressed stream.
2. **RefPack Stream Header:**
   - Byte 0: Flags (typically `0x10`, `0x30`, `0x32`, `0x34`). Bit 0 (`0x01`) specifies a 4-byte uncompressed size if set, 3-byte if clear.
   - Byte 1: Magic byte `0xFB`.
   - Bytes 2..4 (or 2..5): Uncompressed payload size in **Big-Endian**.

#### Decompression Opcode State Machine
The decompressor maintains a sliding window over the reconstructed output buffer.

```python
def decompress_refpack(data: bytes) -> bytes:
    """Decompress EA RefPack stream (starting at the 0x10 0xFB header)."""
    flags = data[0]
    pos = 2
    if (flags & 0x01) != 0:
        uncompressed_sz = int.from_bytes(data[pos:pos+4], "big")
        pos += 4
    else:
        uncompressed_sz = int.from_bytes(data[pos:pos+3], "big")
        pos += 3
        
    out = bytearray()
    while pos < len(data):
        opcode = data[pos]
        pos += 1
        
        # Stop code (0xFC .. 0xFF)
        if opcode >= 0xFC:
            literal_run = opcode & 0x03
            if literal_run > 0:
                out.extend(data[pos:pos + literal_run])
                pos += literal_run
            break
            
        # 1. 2-byte command (Opcode < 0x80): 0xxxxxxx
        if (opcode & 0x80) == 0:
            b2 = data[pos]
            pos += 1
            literal_run = opcode & 0x03
            copy_len = ((opcode & 0x1C) >> 2) + 3
            offset = (((opcode & 0x60) << 3) | b2) + 1
            if literal_run > 0:
                out.extend(data[pos:pos + literal_run])
                pos += literal_run
            for _ in range(copy_len):
                out.append(out[-offset])
                
        # 2. 3-byte command (0x80 <= Opcode < 0xC0): 10xxxxxx
        elif (opcode & 0x40) == 0:
            b2 = data[pos]
            b3 = data[pos + 1]
            pos += 2
            literal_run = b2 >> 6
            copy_len = (opcode & 0x3F) + 4
            offset = (((b2 & 0x3F) << 8) | b3) + 1
            if literal_run > 0:
                out.extend(data[pos:pos + literal_run])
                pos += literal_run
            for _ in range(copy_len):
                out.append(out[-offset])
                
        # 3. 4-byte command (0xC0 <= Opcode < 0xE0): 110xxxxx
        elif (opcode & 0x20) == 0:
            b2 = data[pos]
            b3 = data[pos + 1]
            b4 = data[pos + 2]
            pos += 3
            literal_run = opcode & 0x03
            copy_len = ((opcode & 0x0C) << 6) + b4 + 5
            offset = (((opcode & 0x10) << 12) | (b2 << 8) | b3) + 1
            if literal_run > 0:
                out.extend(data[pos:pos + literal_run])
                pos += literal_run
            for _ in range(copy_len):
                out.append(out[-offset])
                
        # 4. Large literal block (0xE0 <= Opcode < 0xFC): 111xxxxx
        else:
            literal_run = (opcode & 0x1F) * 4 + 4
            out.extend(data[pos:pos + literal_run])
            pos += literal_run
            
    return bytes(out)
```

---

## 2. Westwood 3D (W3D) Format (SAGE1)

W3D files consist of hierarchically nested chunks. All multi-byte values in SAGE1 W3D are **32-bit Little-Endian**.

### 2.1 Chunk Framing
Every chunk starts with an 8-byte header:
| Offset | Size (bytes) | Type | Field | Description |
|---|---|---|---|---|
| `0x00` | 4 | `uint32` | `ChunkType` | Numeric Chunk ID from enumeration |
| `0x04` | 4 | `uint32` | `ChunkSize` | Payload size. Bit 31 (`0x80000000`) indicates sub-chunks follow (`HasSubChunks = (ChunkSize & 0x80000000) != 0; RealSize = ChunkSize & ~0x80000000`) |

### 2.2 Key W3D Chunk Taxonomy
| Chunk ID (Hex) | Enumeration | Description |
|---|---|---|
| `0x00000000` | `W3D_CHUNK_MESH` | Top-level container for a renderable mesh |
| `0x00000001` | `W3D_CHUNK_VERTICES` | Vertex positions array (`Vector3[N]`, 12 bytes each) |
| `0x00000002` | `W3D_CHUNK_VERTEX_NORMALS` | Vertex normals array (`Vector3[N]`, 12 bytes each) |
| `0x0000000C` | `W3D_CHUNK_MESH_USER_TEXT` | String containing proxy bones, collision tags, etc. |
| `0x0000000E` | `W3D_CHUNK_VERTEX_INFLUENCES`| Bone rigging weights (`uint16 boneIdx`, `uint16 padding`, `float weight`) |
| `0x0000001F` | `W3D_CHUNK_MESH_HEADER3` | Mesh metadata: Version, Attributes, Name[32], ContainerName[32], NumTris, NumVertices, NumMaterials |
| `0x00000020` | `W3D_CHUNK_TRIANGLES` | Triangle face array: 3x `uint32` vertex indices, attributes, surface normal |
| `0x00000022` | `W3D_CHUNK_VERTEX_SHADE_INDICES`| Mapping of shade vertex to geometric vertex |
| `0x00000028` | `W3D_CHUNK_MATERIAL_INFO` | Pass count, vertex material count, texture count |
| `0x00000029` | `W3D_CHUNK_SHADERS` | Shading passes and blend mode definitions |
| `0x0000002A` | `W3D_CHUNK_VERTEX_MATERIALS`| Material properties (Ambient, Diffuse, Specular, Emissive, Opacity) |
| `0x00000030` | `W3D_CHUNK_TEXTURES` | Texture file names (`TextureName[32]`) |
| `0x00000038` | `W3D_CHUNK_MATERIAL_PASS` | Container for pass details, texture stages |
| `0x00000039` | `W3D_CHUNK_VERTEX_MATERIAL_IDS`| Per-triangle material ID assignment |
| `0x0000003A` | `W3D_CHUNK_SHADER_IDS` | Per-triangle shader ID assignment |
| `0x00000048` | `W3D_CHUNK_STAGE_TEXCOORDS` | UV coordinates array (`Vector2[N]`, 8 bytes each: U, V) |
| `0x00000100` | `W3D_CHUNK_HIERARCHY` | Skeletal hierarchy definition |
| `0x00000101` | `W3D_CHUNK_HIERARCHY_HEADER` | Hierarchy name, num pivots, root pivot index |
| `0x00000102` | `W3D_CHUNK_PIVOTS` | Array of pivot/bone structures (Name, ParentIdx, Translation, Euler/Quat) |
| `0x00000103` | `W3D_CHUNK_PIVOT_FIXUPS` | Inverse bind pose transform matrices (4x3 or 4x4) |
| `0x00000200` | `W3D_CHUNK_ANIMATION` | Skeletal keyframe animation stream |
| `0x00000280` | `W3D_CHUNK_COMPRESSED_ANIMATION`| Bit-packed or vector-quantized animation channels |
| `0x00000700` | `W3D_CHUNK_HLOD` | Hierarchical Level of Detail container |
| `0x00000740` | `W3D_CHUNK_BOX` | Collision bounding volume (`BoxMinMax`, `Name[32]`) |

---

## 3. SAGE2 StreamFS Format (C&C3, RA3, Generals Universe)

SAGE2 compiles game XML and assets into unified binary streams consisting of linked chunk files (`.manifest`, `.bin` / `cdata`, `.relo`, `.imp`).

### 3.1 Manifest Header (`ManifestHeader`, 48 Bytes)
Pack = 4, Little-Endian (or Big-Endian on Xbox 360 Xenon):

| Offset | Size (bytes) | Type | Field | Description |
|---|---|---|---|---|
| `0x00` | 1 | `bool` | `IsBigEndian` | `0` = x86 Little-Endian, `1` = Xenon Big-Endian |
| `0x01` | 1 | `bool` | `IsLinked` | `1` = monolithic concatenated stream, `0` = loose chunks |
| `0x02` | 2 | `uint16` | `Version` | Stream version (Version 5 in TW/KW/RA3/Generals Universe) |
| `0x04` | 4 | `uint32` | `StreamChecksum` | Cyclic redundancy check of compilation run |
| `0x08` | 4 | `uint32` | `AllTypesHash` | Schema consistency hash |
| `0x0C` | 4 | `uint32` | `AssetCount` | Total number of asset entries in manifest |
| `0x10` | 4 | `uint32` | `TotalInstanceDataSize`| Total combined byte size of `.bin` / `cdata` payload |
| `0x14` | 4 | `uint32` | `MaxInstanceChunkSize`| Largest individual asset payload |
| `0x18` | 4 | `uint32` | `MaxRelocationChunkSize`| Largest individual relocation chunk |
| `0x1C` | 4 | `uint32` | `MaxImportsChunkSize`| Largest individual imports chunk |
| `0x20` | 4 | `uint32` | `AssetReferenceBufferSize`| Size of asset reference buffer in bytes |
| `0x24` | 4 | `uint32` | `ReferenceManifestNameBufferSize`| Size of referenced manifest string table |
| `0x28` | 4 | `uint32` | `AssetNameBufferSize`| Size of null-terminated asset names table |
| `0x2C` | 4 | `uint32` | `SourceFileNameBufferSize`| Size of source file path names table |

### 3.2 Asset Entry (`AssetEntry`, Version 5 = 44 Bytes)
Follows immediately after `ManifestHeader` at offset `48`:

| Offset | Size (bytes) | Type | Field | Description |
|---|---|---|---|---|
| `0x00` | 4 | `uint32` | `TypeId` | Asset Type Identifier (e.g. W3DContainer, W3DMesh, Texture) |
| `0x04` | 4 | `uint32` | `InstanceId` | Unique ID of asset instance |
| `0x08` | 4 | `uint32` | `TypeHash` | FNV/CRC hash of type name string |
| `0x0C` | 4 | `uint32` | `InstanceHash`| Hash of asset instance name |
| `0x10` | 4 | `int32` | `AssetReferenceOffset`| Byte offset into `AssetReferenceBuffer` |
| `0x14` | 4 | `int32` | `AssetReferenceCount` | Count of referenced asset entries |
| `0x18` | 4 | `int32` | `NameOffset` | Byte offset into `AssetNameBuffer` (null-terminated string) |
| `0x1C` | 4 | `int32` | `SourceFileNameOffset`| Byte offset into `SourceFileNameBuffer` |
| `0x20` | 4 | `int32` | `InstanceDataSize` | Byte size of raw payload in `.bin` |
| `0x24` | 4 | `int32` | `RelocationDataSize` | Byte size of relocation data in `.relo` |
| `0x28` | 4 | `int32` | `ImportsDataSize` | Byte size of import patch table in `.imp` |

In linked mode (`IsLinked == true`), `bin_offset` for asset `i` starts at byte `4` and advances by `InstanceDataSize` for each entry:
$$\text{Offset}_{i+1} = \text{Offset}_i + \text{InstanceDataSize}_i$$

### 3.3 Memory Relocations (`.relo`)
SAGE2 compiles C++ structs directly as memory dumps. Pointers inside structs are serialized as offsets from the base of the asset instance block.
- The `.relo` table consists of an array of `uint32` offsets terminated by `0xFFFFFFFF`.
- Each offset identifies a pointer field in the instance data.
- **Runtime Resolution:**
  $$\text{PointerValue} = \text{BaseInstanceAddress} + *(\text{uint32}*)(\text{BaseInstanceAddress} + \text{ReloOffset})$$

### 3.4 SAGE2 W3D Render Asset Memory Structures
Inside `.bin`, meshes and skeletons follow strict C-struct alignments:

#### `W3DMesh` Structure
```cpp
struct W3DMesh {
    void* vtable;                        // BaseRenderAssetType (4 bytes)
    W3DMeshVertexData* VertexData;       // Pointer to vertex buffer descriptor (4 bytes)
    uint32_t GeometryType;               // 0=Normal, 1=Skin, 2=CameraAligned, 3=CameraOriented (4 bytes)
    Vector3 BoundingBoxMin;              // 12 bytes
    Vector3 BoundingBoxMax;              // 12 bytes
    float BoundingSphereRadius;          // 4 bytes
    Vector3 BoundingSphereCenter;        // 12 bytes
    Relo::List<Triangle> Triangles;      // Count (4 bytes) + Triangle* Items (4 bytes)
    FXShaderMaterial FXShader;           // Shader metadata, constants, textures
    void* AABTree;                       // Spatial tree for raycasting / collision
    uint8_t Hidden;                      // 1 byte
    uint8_t CastShadow;                  // 1 byte
    uint8_t SortLevel;                   // 1 byte
    uint8_t Padding;
};
```

#### `W3DMeshVertexData` Structure
```cpp
struct W3DMeshVertexData {
    int32_t NumVertices;                 // Vertex count (4 bytes)
    Relo::List<uint8_t> VertexElementData;// Raw vertex buffer bytes (8 bytes: Count, Items*)
    Relo::List<uint8_t> VertexDeclaration;// D3DVertexElement9 array (8 bytes: Count, Items*)
    Relo::List<uint16_t> Bones;          // Rigging bone lookup table (8 bytes: Count, Items*)
};
```

#### `D3DVertexElement9` Layout (8 Bytes per Element)
| Offset | Size | Type | Field | Description |
|---|---|---|---|---|
| `0x00` | 2 | `int16` | `Stream` | Stream index (`0xFF` indicates terminator) |
| `0x02` | 2 | `int16` | `Offset` | Byte offset of vertex attribute inside vertex stride |
| `0x04` | 1 | `uint8` | `Type` | Data type: `FLOAT3`=2 (12B), `FLOAT2`=1 (8B), `D3DCOLOR`=4 (4B), `FLOAT16_2`=15 (4B) |
| `0x05` | 1 | `uint8` | `Method` | Tessellation / evaluation method (`DEFAULT` = 0) |
| `0x06` | 1 | `uint8` | `Usage` | `POSITION`=0, `BLENDWEIGHT`=1, `BLENDINDICES`=2, `NORMAL`=3, `TEXCOORD`=5, `TANGENT`=6, `BINORMAL`=7, `COLOR`=10 |
| `0x07` | 1 | `uint8` | `UsageIndex` | Attribute index (e.g. UV channel 0 or 1) |

#### `W3DContainer` and `W3DHierarchy`
A unit or building model is assembled via a `W3DContainer`:
- Points to a `W3DHierarchy` containing an array of `HierarchyPivot` structures:
  `Name` (AnsiString), `Parent` (`int32`, `-1` for root), `Translation` (`Vector3`), `Rotation` (`Quaternion`: x, y, z, w), and `FixupMatrix` (`float[16]`).
- Contains a `List<SubObject>`:
  `uint32 BoneIndex`, `SubObjectID` (AnsiString), `AssetReference RenderObject` (points to the target `W3DMesh`).

---

## 4. SAGE `.map` Chunk Architecture (`CkMp`)

SAGE and SAGE2 binary `.map` files store the terrain mesh, elevation grid, tile blend layers, water bodies, and camera parameters. The `.map` payload is RefPack-compressed inside an `EAR\0` container.

### 4.1 Master Dictionary Header
Upon RefPack inflation, the stream starts with a string dictionary mapping chunk names to sequential integer IDs:
1. Bytes `0x00..0x03`: Magic ASCII `"CkMp"`.
2. Bytes `0x04..0x07`: `uint32` `DictionaryCount` ($N$).
3. $N$ sequential dictionary records:
   - 1 byte: `StringLength` ($L$).
   - $L$ bytes: `ChunkName` (ASCII string).
   - 4 bytes: `uint32` `ChunkId` (1, 2, 3, ...).

### 4.2 Sequential Chunk Framing
Directly following the dictionary table, sequential chunk frames begin. Each frame has a fixed **10-byte header**:

| Offset | Size (bytes) | Type | Field | Description |
|---|---|---|---|---|
| `0x00` | 4 | `uint32` | `ChunkId` | Numerical Chunk ID resolving to Dictionary name |
| `0x04` | 2 | `uint16` | `Version` | Chunk format version (e.g., HeightMapData = 6, BlendTileData = 24) |
| `0x06` | 4 | `uint32` | `PayloadSize` | Byte length of the chunk data payload |

Payload follows immediately for `PayloadSize` bytes, followed by the next chunk header.

### 4.3 Terrain Elevation Chunk (`HeightMapData`, ID 2, Version 6)
Stores the elevation grid as 16-bit integers.

#### Header Layout (36 Bytes)
| Offset | Size | Type | Field | Value / Description |
|---|---|---|---|---|
| `0x00` | 4 | `uint32` | `Width` | Total terrain grid width in tiles (e.g. `440`) |
| `0x04` | 4 | `uint32` | `Height` | Total terrain grid height in tiles (e.g. `440`) |
| `0x08` | 4 | `uint32` | `BorderSize` | Inaccessible map border in tiles (e.g. `70`) |
| `0x0C` | 4 | `uint32` | `Flags` | Elevation flags (`1`) |
| `0x10` | 8 | `uint32[2]` | `Reserved` | Zero padding |
| `0x18` | 4 | `uint32` | `PlayableWidth` | `Width - 2 * BorderSize` (e.g. `300`) |
| `0x1C` | 4 | `uint32` | `PlayableHeight`| `Height - 2 * BorderSize` (e.g. `300`) |
| `0x20` | 4 | `uint32` | `SampleCount` | Total height vertices = `Width * Height` (e.g. `193,600`) |

#### Elevation Data Payload
Immediately follows at byte `36`:
- Array of `SampleCount` `uint16` values in Little-Endian.
- Stored row-major ($y \in [0, \text{Height}-1], x \in [0, \text{Width}-1]$).
- **Scale:** In SAGE coordinate space, 1 tile = 10 world units (metres). Height values are stored in 1/10th world units:
  $$\text{HeightMetres} = \frac{\text{RawHeight}}{10.0}$$

### 4.4 Tile Blend Chunk (`BlendTileData`, ID 3, Version 24)
Stores terrain texture splatting, quad indices, and multi-layer texture blending.
- Offset `0x00`: `uint32 TileCount` (`Width * Height`).
- Offset `0x04`: Array of base tile quad indices and material indices.
- Offset tables for secondary texture layers, alpha blend splatting masks, and edge transitions, terminating with `0xFFFFFFFF`.

---

## 5. Tool Catalog & CLI Usage

### 5.1 Tool Matrix
| Tool | Purpose | Source / URL | Status |
|---|---|---|---|
| **Bibber's C&C Asset Extractor** | Extraction of StreamFS, manifests, BIG archives, EALayer3 audio, DDS textures | Community (Bibber) | Shipped at `C:\cnc_rev\sage2-extract\tools\asset_extractor\` |
| **BigTool** | CLI creation/extraction of BIG4 / BIGF archives | [GitHub: BigTool](https://github.com/OpenSAGE/OpenSAGE) | Cross-platform |
| **OpenSAGE Blender Add-on (`io_mesh_w3d`)** | Blender 3.x/4.x plugin for import/export of W3D meshes, bones, animations | [OpenSAGE: io_mesh_w3d](https://github.com/OpenSAGE/OpenSAGE) | Shipped at `C:\cnc_rev\sage2-extract\tools\io_mesh_w3d.zip` |
| **FinalBIG** | GUI editor for `.big` files across all SAGE games | Matthias Hartung / Community | Standard modding utility |
| **EA WorldBuilder** | Official terrain editor producing `.map` and `map.xml` | Shipped in C&C3/KW/RA3 root directories | Available in `D:\ea\Command and Conquer 3 TW and KW\` |
| **EA Mod SDK Assimilator** | Official XML to SAGE2 binary compiler | EA Mod SDKs (C&C3 / RA3) | Uses XML schema validation (`.xsd`) |

### 5.2 CLI Extraction Commands
```bash
# Extracting a .big archive with BigTool:
bigtool -x -i "C:\Program Files\EA Games\Command and Conquer Red Alert 3\Red Alert 3\Data\GlobalStream.big" -o "./extracted"

# Batch extracting models via Bibber Asset Extractor:
"C:\cnc_rev\sage2-extract\tools\asset_extractor\C&C Asset Extractor.exe" -manifest "mod.manifest" -out "./assets"
```

---

## 6. Conversion Pipelines to glTF 2.0 / GLB

### 6.1 Coordinate Space Transformations
SAGE/W3D uses a **Right-Handed Z-Up** coordinate system ($+X$ right, $+Y$ forward, $+Z$ up). glTF 2.0 strictly requires a **Right-Handed Y-Up** coordinate system ($+X$ right, $+Y$ up, $+Z$ forward / $-Z$ forward camera).

#### Transform Matrix (Z-Up to glTF Y-Up):
$$\begin{bmatrix} X_{\text{gltf}} \\ Y_{\text{gltf}} \\ Z_{\text{gltf}} \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{bmatrix} \begin{bmatrix} X_{\text{sage}} \\ Y_{\text{sage}} \\ Z_{\text{sage}} \end{bmatrix}$$
- $X_{\text{gltf}} = X_{\text{sage}}$
- $Y_{\text{gltf}} = Z_{\text{sage}}$
- $Z_{\text{gltf}} = -Y_{\text{sage}}$

#### Facing Convention:
- SAGE units face $+Y$ by default.
- In Three.js and glTF standard, models face **$-Z$**. The transformation above naturally maps $+Y$ into $-Z$, aligning with the Wave 2 contract without yaw corrections.

### 6.2 UV Coordinates
- DirectX 9 / SAGE textures use $V=0$ at top-left.
- glTF 2.0 specifies $V=0$ at bottom-left.
- **Conversion:** $V_{\text{gltf}} = 1.0 - V_{\text{sage}}$.

### 6.3 Skinning & Vertex Limits
- glTF skins use 4 bone weights per attribute (`JOINTS_0`, `WEIGHTS_0`).
- SAGE models typically use 1 to 4 bone influences per vertex (`W3DMeshProcessor.cs`).
- Normalization requirement: $\sum_{k=0}^{3} \text{weight}_k = 1.0$.

---

## 7. Critical Pitfalls & Engineering Gotchas

1. **RefPack Overrun on Corrupted Length:** Always bound sliding-window backward copies (`offset <= len(out)`). If `offset > len(out)`, the stream is corrupt.
2. **D3DCOLOR Byte Swizzle:** In DirectX 9, `D3DCOLOR` stores packed bytes as `ARGB` or `BGRA`. When extracting vertex colors or bone indices packed as `D3DCOLOR`, do not read as raw integers without unpacking channel bytes.
3. **Half-Float UVs:** When vertex declarations specify `FLOAT16_2` (`Type = 15`), coordinates are IEEE 754 16-bit half floats. Reading them as 32-bit floats produces invalid UV projections.
4. **16-bit Heightfield Clamp:** SAGE height values are `uint16` (0..65535). Do not cast directly to `int16` or heights above 3276.7 metres will wrap to negative numbers.
5. **Relocation Buffer Alignment:** SAGE2 `.bin` structs rely on 4-byte pointer alignment. Offsets inside `.relo` must always point to 4-byte aligned addresses.

---

## 8. Audit Question Bank

When evaluating any SAGE/SAGE2 importer, decoder, or mod pipeline, verify:
- [ ] **Archive Big-Endian Check:** Does the BIG unpacker parse `ArchiveSize` as Little-Endian, but `FileCount`, `HeaderSize`, `DataOffset`, and `DataSize` as Big-Endian?
- [ ] **RefPack Stop Codes:** Does the RefPack decompressor correctly handle stop codes `0xFC..0xFF` and append the trailing literal bytes (`opcode & 0x03`)?
- [ ] **W3D Sub-chunk Bit:** Does the chunk reader test bit 31 (`0x80000000`) of `ChunkSize` to recurse into child chunks rather than parsing sub-chunks as flat data?
- [ ] **StreamFS Linked Mode:** Does the StreamFS loader properly compute cumulative offsets across linked `.bin` chunks rather than assuming individual file bounds?
- [ ] **Coordinate Transform:** Are mesh vertices and skeleton pivots converted from Z-up to Y-up via $(x, z, -y)$?
- [ ] **Heightfield Border Clipping:** Does the terrain generator distinguish between total grid dimensions (`Width`, `Height`) and playable bounds (`PlayableWidth`, `PlayableHeight`), accounting for `BorderSize`?
- [ ] **Normal Normalization:** Are transformed vertex normals re-normalized after coordinate space conversion?
