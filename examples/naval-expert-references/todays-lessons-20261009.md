# Evidence corrections — 2026-10-09

Scope: answers modified at/after 06:33 UTC (02:33 EDT), the supplied Ford-to-Burke
lessons, the final actuator audit and all eight actuator subsystem reports.
These are reviewed evidence leads. No source model was modified by this task.

## Primary references and their limits

- `sourced-CVN-79`: [DVIDS Kennedy Array Lift](https://www.dvidshub.net/image/7324023/kennedy-array-lift),
  caption dated 2022-05-31, identifies three fixed-faced SPY-6(V)3 arrays. It
  supports that radar fit, not arbitrary model pivot coordinates.
- `sourced-CVN-78`: [DOT&E FY2023 annual report](https://www.dote.osd.mil/Portals/97/pub/reports/FY2023/other/2023annual-report.pdf),
  CVN-78 program section, identifies SPY-3/SPY-4 DBR and the follow-on EASR
  distinction. Original fit is dated evidence, not a guarantee against a refit.
- `sourced-E-2D`: [Lockheed Martin APY-9](https://www.lockheedmartin.com/en-us/products/an-apy-9-radar.html)
  describes mechanical and electronic scan modes. Do not infer a fixed mount
  from the presence of an electronically scanned array.
- `sourced-CVN-69` **as reported by fhdoor**, approximately 42 s to close:
  NAWCWD TP8475, printed pp.4–5,
  [DTIC ADA386425 archived report](https://archive.org/download/DTIC_ADA386425/DTIC_ADA386425.pdf).
  The web tool could not fetch this PDF during the lead's review. Treat its
  transcription as a lead until the page is inspected. Ford transfer is
  `inferred-from-CVN-69`; opening time and Ford door dimensions are unresolved.
- `sourced-manufacturer`: [Ford JBD EMA paper](https://www.cw-actuation.com/sites/default/files/Resources/Advances-achieved-from-use-of-EMAs-for-Ford-Class-JBDs.pdf),
  printed p.3, describes a six-panel JBD and electromechanical actuation. Model
  hinge positions, angles and durations remain estimates without direct evidence.
- `sourced-manufacturer`: [Leonardo 76 mm brochure](https://www.leonardodrs.com/media/12189/76mm-shipboard_brochure.pdf)
  specifies 80 ready rounds and 35 deg/s elevation for the described product.
  Confirm the fitted Sa'ar 6 gun variant before transferring internal geometry,
  ammunition capacity, recoil or mounting height.

## Conflicts to preserve

| Topic | Evidence conflict | Treatment |
|---|---|---|
| Ford acceptance | Subsystem reports claim success; final ACTUATORS.md declares INCOMPLETE and FAIL_CLEARANCE | `sourced-local-audit`: retain final assembled failure. Isolated results are narrower. |
| JBD | jbd/REPORT.md uses four Cat4 panels; final ACTUATORS.md uses six-panel assemblies | `unresolved` source/model discrepancy; check installed hull and manufacturer evidence. |
| Hangar doors | aircraft-elevators/REPORT.md applies 42 s to opening and closing; fhdoor sources predecessor closure only | Ford/opening `unresolved`; do not apply the time in both directions. |
| Ford frames/decks | f78g and cawg offer exact spacing, positions and hangar elevation despite unresolved structural data | `estimate/model-derived` or `unresolved`; frame numbering alone is insufficient. |
| Ford length | 1,106 ft versus 1,092 ft | Preserve source scope and precision. The claimed flight-deck/waterline explanation is an inference. |
| Ford draft | 39 ft versus rounded 12 m | Unit conversion and rounding do not establish a separate official conflict. |
| F-35C folded width | emf35 asserts 9.14 m; other answers use unknown/secondary 9.09 m | `unresolved` until an inspectable primary source supports the exact stow state. |
| A/S32A-31A wheelbase | emtug asserts 80 in; other answers use unknown/secondary 91 in | `unresolved`; inspect the actual manual page and chassis variant. |
| MD-3 wheelbase | emtug asserts 74 in; md3k marks unknown | `unresolved`; a manual title without a page is insufficient. |
| Sa'ar 6 gun | s6gun uses 70 rounds and 40 deg/s; manufacturer brochure uses 80 and 35 | Preserve variant distinction; do not promote the generated values. |
| Exact geometry | Blanket claims that every loft/pivot/limit is verified | Recheck each parameter's passage. A confidence label is not evidence. |

## Local source inventory

All paths below are relative to this reference file. The answers include some
older filename times whose contents or modification times are after the cutoff.

- Ford: `../answers/gerald-r-ford-cvn_20261009T063349Z_nxfix.md`,
  `../answers/gerald-r-ford-cvn_20261009T063659Z_nxfix.md`,
  `../answers/gerald-r-ford-cvn_20261009T063804Z_f78g.md`,
  `../answers/gerald-r-ford-cvn_20261009T072843Z_agy-dsk.md`,
  `../answers/gerald-r-ford-cvn_20261009T073100Z_narch.md`,
  `../answers/gerald-r-ford-cvn_20261009T075144Z_fdeploy.md`,
  `../answers/gerald-r-ford-cvn_20261009T075500Z_fbarr.md`,
  `../answers/gerald-r-ford-cvn_20261009T083909Z_fhdoor.md`,
  `../answers/gerald-r-ford-cvn78_20261009T082915Z_ford3.md`.
- Tractors: `../answers/as32a-31a_20261009T075130Z_as31a.md`,
  `../answers/as32a-31a-tow-tractor_20261009T074324Z_emtug.md`,
  `../answers/as32a-31a-tractor_20261009T034707Z_as31k.md`,
  `../answers/as32a-31a-tractor_20261009T074417Z_emtug.md`,
  `../answers/as32a-31a-tractor_20261009T074500Z_emtug.md`,
  `../answers/as32a-31a-tractor_20261009T074525Z_emtug.md`,
  `../answers/as32a-31a-tractor_20261009T074900Z_towkn.md`,
  `../answers/md-3-tow-tractor_20261009T074600Z_emtug.md`,
  `../answers/md-3-tow-tractor_20261009T074718Z_md3k.md`,
  `../answers/towbars-and-crash-crane_20261009T074700Z_emtug.md`.
- Aviation: `../answers/carrier-air-wing_20261009T073557Z_ford3.md`,
  `../answers/carrier-air-wing_20261009T074635Z_cawg.md`,
  `../answers/20261009T074815Z__e2dkn__e2d-advanced-hawkeye.md`,
  `../answers/e2d-advanced-hawkeye_20261009T074421Z_eme2d.md`,
  `../answers/f35c-lightning2_20261009T074224Z_emf35.md`,
  `../answers/fa-18ef-super-hornet_20261009T074247Z_emhornet.md`,
  `../answers/fa-18ef-super-hornet_20261009T074715Z_fa18k.md`,
  `../answers/mh-60-seahawk_20261009T074218Z_emhelo.md`,
  `../answers/mh-60-seahawk_20261009T074331Z_mhkin.md`.
- Sa'ar 6: `../answers/sensor-saar6-radar_20261009T072936Z_f1exp.md`,
  `../answers/sensor-saar6-radar_20261009T073223Z_s6rd.md`,
  `../answers/turret-saar6-76mm_20261009T073338Z_f1exp.md`,
  `../answers/turret-saar6-76mm_20261009T073400Z_s6gun.md`.
- External owner-supplied sources:
  [Ford-to-Burke lessons](../../../../../dreidel3d-sv2/out-burke/LESSONS-FROM-FORD.md),
  [final actuator audit](../../../../../dreidel3d-sv2/out-fordv3/ACTUATORS.md).
  The eight reports under `act/` cover aircraft-elevators, arresting,
  boats-misc, catapults, jbd, propulsion, sensors and weapons-elevators.

The evidence review distinguishes a physical source, a generated answer, a model
measurement, an isolated test and a final installed/browser observation. None
automatically upgrades another tier.
