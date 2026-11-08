---
generated_at: "2026-10-09T02:45:13Z"
generator: "antigravity-deep-research (agy-dsk, session 5aa41122-41b5-472f-8d87-b3da904ffdd2)"
research_method: "search"
skills:
  - "naval-military-kinematics"
  - "mesh-geometric-upscaling"
provider: "Google Gemini"
models:
  - "deep-research-preview-04-2026"
  - "gemini-3.5-flash-lite"
query: "BAE Systems Mk 45 Mod 4 5-inch Naval Gun Blueprint"
sources_count: 16
asset_id: "mk45-mod4-5inch-gun"
title: "Naval Architectural Blueprint Dossier: BAE Systems Mk 45 Mod 4 5-Inch/62-Caliber Naval Gun"
---

# Naval Architectural Blueprint Dossier: BAE Systems Mk 45 Mod 4 5-Inch/62-Caliber Naval Gun

**Classification:** USA | US Navy | Naval Gun System | Mk 45 | Mk 45 Mod 4
**Standard:** JSLC / Project Eretz - Naval Architecture & Kinematics Standard

---

### 1. MASTER COORDINATE DATUM & DIMENSIONS

- **glTF 2.0 WebGL Coordinate Standard:**
  - Forward / Bore Axis (at 0 deg elevation): **-Z axis**
  - Vertical / Turret Crown / Trunnion Apex: **+Y axis**
  - Transverse / Starboard: **+X axis**
  - Transverse / Port: **-X axis**
  - **Turret Deck Ring Mounting Baseline:** Strictly at **Y = 0.000m**

| Parameter | Metric Value | Imperial Value | Engineering Notes |
|---|---|---|---|
| Caliber | 127 mm | 5.0 inches | Standard US Navy naval artillery bore diameter |
| Barrel Length | 7.874 m | 310.0 inches | 62-caliber barrel length (L/62) |
| Total System Weight | 24,545 kg | 54,112 lbs | Above and below-deck mechanism dry weight |
| Turret Above-Deck Height | 2.54 m | 8.3 ft | Deck mounting plane to faceted stealth cupola apex |
| Turret Width (Cupola) | 3.38 m | 11.1 ft | Faceted low radar cross section (RCS) shield |
| Rate of Fire | 16 - 20 rounds/min | Fully automated drum feed from lower hoist |
| Maximum Range (Conventional) | 37,000 m | 20.0 nautical miles | High-explosive fragmentation (HE-FRAG) rounds |
| Maximum Range (Guided/ERGM) | > 100,000 m | > 54.0 nautical miles | Extended-range guided munitions |
| Recoil Stroke | 0.38 m | 15.0 inches | Hydraulic brake and pneumatic counter-recoil cylinder |

---

### 2. ELEVATION, TRAVERSE, AND BALLISTIC LIMITS

The Mk 45 Mod 4 gun mount incorporates a low-radar-cross-section (low-RCS) faceted fiberglass shield designed to preserve the stealth characteristics of Arleigh Burke Flight III destroyers.

| Operational Axis | Angular Range | Slew Rate | Kinematic Limit Mechanism |
|---|---|---|---|
| Turret Traverse (Azimuth) | +/- 170.0 deg | 30.0 deg/sec | Continuous electromechanical deck ring gear |
| Barrel Elevation (Pitch) | -15.0 deg to +65.0 deg | 20.0 deg/sec | Hydraulic trunnion elevation cylinders |
| Barrel Recoil (Surge) | 0.00m to -0.38m | Peak recoil 0.04s | Hydraulic buffer sleeve and pneumatic recuperator |
| Lower Ammunition Hoist | Vertical translation | 20 rounds/min | Dual-drum carousel to breech cradle hoist |

---

### 3. COMPLETE KINEMATIC SCENE GRAPH HIERARCHY

```
Mk45_Base_Mount (Y=0.000m at main deck ring)
├── Lower_Deck_Mechanism (Below deck)
│   ├── Ammunition_Handling_Room
│   ├── Revolving_Lower_Hoist (Rotates with turret azimuth)
│   └── 20_Round_Automated_Drum_Loader
├── Turret_Faceted_Cupola (Azimuth yaw rotation around +Y axis: +/- 170 deg)
│   ├── Gun_Shield_Stealth_Faces (Composite low-RCS panels)
│   ├── Access_Hatch_Aft (Maintenance entry door)
│   ├── Muzzle_Boresight_Camera_Window
│   └── Gun_Trunnion_Support
│       └── Barrel_Elevating_Mass (Pitch articulation around +X axis: -15 to +65 deg)
│           ├── Gun_Slide_Housing
│           ├── Barrel_Recoil_Group (Surge translation along bore axis -Z: stroke -0.38m)
│           │   ├── Barrel_L62_Rifled (5-inch/62-caliber rifled tube)
│           │   ├── Muzzle_Brake_Thermal_Jacket
│           │   └── Muzzle_Blast_VFX_Socket (Point of origin for flame/smoke nodes)
│           └── Breech_Block_Mechanism (Vertical sliding wedge breech block)
```

---

### 4. RADAR CROSS SECTION & STEALTH FACETING AUDIT

- **Shield Faceting Architecture:** The Mod 4 stealth cupola utilizes 15 flat planar faces inclined between 10 and 35 degrees to redirect incoming enemy radar energy upward into the sky or downward into the sea, matching the DDG-125 superstructure deckhouse rake angles.
- **Muzzle Flush Seal:** When stowed horizontally (-Z), a flush inflatable RF collar seals the trunnion aperture to prevent radar cavity resonance inside the gun slide housing.
- **Automated Operations:** Completely unmanned above-deck turret during combat firing; ammunition transfer and loading are executed via electro-hydraulic automated hoists monitored from the ship's Combat Information Center (CIC).

---

### 5. MASTER AI VIDEO PROMPT PACKAGE

1. **CAD Blueprint Isometric Rotation:**
   `Turntable CAD blueprint of BAE Systems Mk 45 Mod 4 5-inch/62-caliber naval gun, dark navy environment #0A192F, stark white vector geometry #FFFFFF, cyan coordinate grid #00FFFF, 62-caliber barrel, faceted stealth cupola, interior lower-deck ammo hoist diagram.`

2. **Rapid Surface Fire Articulation:**
   `Close-up slow motion of Mk 45 Mod 4 on forward deck of DDG-125 Arleigh Burke destroyer, turret slewing 30 degrees right, 62-caliber gun barrel elevating to +25 degrees, explosive muzzle blast, barrel kicking back 15 inches into hydraulic recoil brake with rapid pneumatic return.`

3. **High-Angle Anti-Air Engagement:**
   `Night naval combat action, forward forecastle of guided missile destroyer, Mk 45 Mod 4 gun elevated to +60 degrees firing rapid high-velocity rounds into dark sky, brilliant yellow-orange muzzle flash illuminating faceted stealth turret faces.`

4. **Heavy Weather Wave Slamming:**
   `Bow forecastle of destroyer plunging through towering North Atlantic swells, green ocean water cascading over the faceted stealth cupola of the Mk 45 Mod 4 naval gun, pristine water-shedding surfaces, gun securely stowed in centerline travel lock.`
