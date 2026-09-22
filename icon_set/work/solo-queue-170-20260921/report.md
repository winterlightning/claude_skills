# Solo queue — offset 170

10 returned references: **8 generated**, **2 unresolved drafts**, 0 prepared combinations, 0 changed-status skips, 0 saving failures.

All eight exports match their current Python originals and the solo manifest, with valid status and zero warnings. All were inspected in light and dark at 48px. The eight-item build initially identified extra spacing/hole failures in the house, narwhal and globe; repaired originals then passed the complete SVG checks and targeted export.

[Actual exported SVGs, light](exports-light.png) · [Actual exported SVGs, dark](exports-dark.png)

Each source was checked against `/api/primitives/status` and `/api/primitives/briefs` immediately before intake using http://localhost:8000. All remained eligible. No container or side combinations were found: these are standalone objects, groups, directional symbols or intrinsic anatomy. No component saves or generation jobs were needed. Source reference artwork and unrelated work were preserved.

## 1. Dual Computer Monitors — two-overlapping-desktop-monitors

- UUID: `51794538-e0cd-4fd6-bb22-9d08f32d43d4`
- Source reference: `pictographic-primitives/_uncategorized_27/monitor transfer_51794538-e0cd-4fd6-bb22-9d08f32d43d4.svg`
- Python original: `icon_set/model/icons/solo/two_overlapping_desktop_monitors_51794538_e0cd_4fd6_bb22_9d08f32d43d4.py`
- Keyshape: `HRECT_L`
- Outcome: **generated**.
- Export: `published/solo48/two-overlapping-desktop-monitors.svg`
- Validation: model and full SVG/build checks passed, zero warnings; manifest and SVG hash verified.
- Visual review: recognizable at native 48px in both themes.

Two diagonally overlapping desktop monitors. HRECT_L (4,8)-(44,40).
Rear screen is an open occluded contour; foreground screen owns its stand.
Lucide monitor contributes simple screen/stand construction. Omit bezel and
rear stand to preserve clearance; reference contributes diagonal pair layout.

## 2. Manual Wheelchair Accessibility Icon — wheelchair-with-large-rear-wheel

- UUID: `5e279196-338d-47df-9c7e-639098b008bb`
- Source reference: `pictographic-primitives/_uncategorized_27/motorized wheelchair_5e279196-338d-47df-9c7e-639098b008bb.svg`
- Python original: `icon_set/model/icons/solo/wheelchair_with_large_rear_wheel_5e279196_338d_47df_9c7e_639098b008bb.py`
- Keyshape: `SQUARE`
- Outcome: **generated**.
- Export: `published/solo48/wheelchair-with-large-rear-wheel.svg`
- Validation: model and full SVG/build checks passed, zero warnings; manifest and SVG hash verified.
- Visual review: recognizable at native 48px in both themes.

Empty right-facing manual wheelchair with large rear wheel, small caster, push handle and projecting front frame. Omit tiny axle, redundant seat rail and footrest bend.
Plan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. Lucide wheelchair search found no match. Reference supplies large wheel and projecting front frame; omit axle and redundant seat rail.

## 3. Downward Arrow with Bottom Bar — arrow-down-toward-long-baseline

- UUID: `65a091c4-02d6-4e29-be08-c4eca75b2def`
- Source reference: `pictographic-primitives/_uncategorized_27/move down 1_65a091c4-02d6-4e29-be08-c4eca75b2def.svg`
- Python original: `icon_set/model/icons/solo/arrow_down_toward_long_baseline_65a091c4_02d6_4e29_be08_c4eca75b2def.py`
- Keyshape: `SQUARE`
- Outcome: **generated**.
- Export: `published/solo48/arrow-down-toward-long-baseline.svg`
- Validation: model and full SVG/build checks passed, zero warnings; manifest and SVG hash verified.
- Visual review: recognizable at native 48px in both themes.

A downward arrow approaches a separate horizontal baseline. Square envelope; vertical axis x24 owns mirrored head. Lucide arrow-down-to-line supplies the detached baseline and joined arrow principle. Reference supplies long baseline; no meaningful details omitted.

## 4. Global User Community — three-people-beneath-gridded-globe

- UUID: `e7e9d324-0221-4314-a633-0dbbed7197d6`
- Source reference: `pictographic-primitives/_uncategorized_27/multiple users network_e7e9d324-0221-4314-a633-0dbbed7197d6.svg`
- Python original: `icon_set/model/icons/solo/three_people_beneath_gridded_globe_e7e9d324_0221_4314_a633_0dbbed7197d6.py`
- Keyshape: `VRECT_L`
- Outcome: **generated**.
- Export: `published/solo48/three-people-beneath-gridded-globe.svg`
- Validation: model and full SVG/build checks passed, zero warnings; manifest and SVG hash verified.
- Visual review: recognizable at native 48px in both themes.

Global User Community.

Plan: VRECT_L, centerline extremes (8, 4, 40, 44); 48 x 48, stroke 4.
Curved meridian and equator preserve globe identity. Three equal small busts follow human_ref/user.svg: heads r2, shoulder arcs r2, with exactly4 units of visible head/shoulder clearance (8 centerline). Omit extra latitude bands. Source supplies globe-over-three-people arrangement. Wider shoulder experiment violated spacing. Widen globe to radii13/9, reduce meridian width, and retain equal compact shoulders after SVG hole review.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction references: human_ref/user.svg bust vocabulary; Lucide globe and its atoms supply the curved meridian joined at poles and split equator.

## 5. Cute Narwhal with Long Tusk — upturned-narwhal

- UUID: `92c799ca-6aa2-4c2b-b0a0-aee64eb0d86c`
- Source reference: `pictographic-primitives/_uncategorized_28/narwhal_92c799ca-6aa2-4c2b-b0a0-aee64eb0d86c.svg`
- Python original: `icon_set/model/icons/solo/upturned_narwhal_92c799ca_6aa2_4c2b_b0a0_aee64eb0d86c.py`
- Keyshape: `SQUARE`
- Outcome: **generated**.
- Export: `published/solo48/upturned-narwhal.svg`
- Validation: model and full SVG/build checks passed, zero warnings; manifest and SVG hash verified.
- Visual review: recognizable at native 48px in both themes.

Narwhal swimming upward-right, with an integral tail and long tusk. SQUARE envelope supplied by tusk and tail. Source supplies silhouette and upward pose. No Lucide whale match. Omit the narrow tail notch and flipper crease to preserve openings; retain a single eye; body owns contiguous curves.

## 6. Damaged House Icon — house-roof-crack

- UUID: `0e26ccf9-f038-4d05-aee6-75c22820f856`
- Source reference: `pictographic-primitives/_uncategorized_28/natural disaster hurricane house damaged_0e26ccf9-f038-4d05-aee6-75c22820f856.svg`
- Python original: `icon_set/model/icons/solo/house_roof_crack_0e26ccf9_f038_4d05_aee6_75c22820f856.py`
- Keyshape: `SQUARE`
- Outcome: **generated**.
- Export: `published/solo48/house-roof-crack.svg`
- Validation: model and full SVG/build checks passed, zero warnings; manifest and SVG hash verified.
- Visual review: recognizable at native 48px in both themes.

A pitched-roof house with a crack descending from its right roof slope. Square envelope. Roof owns exact crack attachment (32,14); left-shifted doorway reserves room for the asymmetric damage. Lucide house informs coherent outline and open doorway. Reference supplies crack placement; simplify rounded doorway to three sides and omit the final small crack bend.

## 7. Double Downward Arrows — arrowhead-stacked-down

- UUID: `07cb98df-804a-4cc9-b536-6c3397ada2af`
- Source reference: `pictographic-primitives/_uncategorized_28/navigation arrows down 1_07cb98df-804a-4cc9-b536-6c3397ada2af.svg`
- Python original: `icon_set/model/icons/solo/arrowhead_stacked_down_07cb98df_804a_4cc9_b536_6c3397ada2af.py`
- Keyshape: `SQUARE`
- Outcome: **generated**.
- Export: `published/solo48/arrowhead-stacked-down.svg`
- Validation: model and full SVG/build checks passed, zero warnings; manifest and SVG hash verified.
- Visual review: recognizable at native 48px in both themes.

Two downward arrowheads on a shared x24 axis; upper triangle covers the lower shoulder. Square envelope. Shared width and 16-unit vertical offset keep parallel slopes clear. Lucide chevrons-down informs equal repeated slopes; source supplies closed upper shoulder. Omit short lower shoulder stubs.

## 8. Egg in a Nest — single-egg-in-nest

- UUID: `652776b6-7bd1-4ba4-8e3b-b8fff4fdaedc`
- Source reference: `pictographic-primitives/_uncategorized_28/nestmate_652776b6-7bd1-4ba4-8e3b-b8fff4fdaedc.svg`
- Python original: `icon_set/model/icons/solo/single_egg_in_nest_652776b6_7bd1_4ba4_8e3b_b8fff4fdaedc.py`
- Keyshape: `HRECT_L`
- Outcome: **generated**.
- Export: `published/solo48/single-egg-in-nest.svg`
- Validation: model and full SVG/build checks passed, zero warnings; manifest and SVG hash verified.
- Visual review: recognizable at native 48px in both themes.

One egg rising from a deep rounded nest. HRECT_L envelope: egg top8, nest sides4/44 and bottom40. Shared symmetry x24 owns egg and bowl. Lucide egg supplies broad lower egg with narrowing smooth crown; source supplies the natural egg-in-nest arrangement. Omit redundant rim band and opening ellipse.

## 9. Human Head with Brain — left-profile-brain

- UUID: `6e501462-4458-4ee8-918b-3b9b1c8dded4`
- Source reference: `pictographic-primitives/_uncategorized_28/neurobiologist_6e501462-4458-4ee8-918b-3b9b1c8dded4.svg`
- Python original: `icon_set/model/icons/solo/_draft_left_profile_brain_6e501462_4458_4ee8_918b_3b9b1c8dded4.py`
- Keyshape: `VRECT_L`
- Outcome: **unresolved-visual**.
- Model validation: valid, zero warnings. Visual review remains unresolved, so no export is claimed.
- The head direction is clear, but the brain becomes a generic blob; lobes, folds and stem lose their anatomical identity. Kept as an underscore-prefixed draft.
- Attempts: original narrow layout failed clearance; moving and narrowing the whole brain resolved spacing but not recognition. The wider square reconstruction still lost brain identity and returned a 7.99986-centerline spacing warning. The square experiment is saved for review. Rotating the profile would change the meaningful upright anatomical pose.

Anatomical head and brain, preserving independent internal lobes. Must retain source direction and folds in final review.
Plan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. Lucide brain contributes lobed contour principle; human_ref/user inspected for head vocabulary. Anatomical brain is an intrinsic organ. Whole brain offset owns clearance repair; no internal folds can fit. Unresolved visual review: reduced brain loses recognizable lobes and stem, so retain draft without export.

## 10. Human Head with Brain — right-profile-folded-brain

- UUID: `0231a044-ecb1-470e-bcc3-8a45ccdc5d4a`
- Source reference: `pictographic-primitives/_uncategorized_28/neuropathologist_0231a044-ecb1-470e-bcc3-8a45ccdc5d4a.svg`
- Python original: `icon_set/model/icons/solo/_draft_right_profile_folded_brain_0231a044_ecb1_470e_bcc3_8a45ccdc5d4a.py`
- Keyshape: `VRECT_L`
- Outcome: **unresolved-visual**.
- Model validation: valid, zero warnings. Visual review remains unresolved, so no export is claimed.
- The head direction is clear, but the brain becomes a generic blob; lobes, folds and stem lose their anatomical identity. Kept as an underscore-prefixed draft.
- Attempts: original narrow layout failed clearance; moving and narrowing the whole brain resolved spacing but not recognition. The wider square reconstruction still lost brain identity and returned a 7.99986-centerline spacing warning. The square experiment is saved for review. Rotating the profile would change the meaningful upright anatomical pose.

Anatomical head and brain, preserving independent internal lobes. Must retain source direction and folds in final review.
Plan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. Lucide brain contributes lobed contour principle; human_ref/user inspected for head vocabulary. Anatomical brain is an intrinsic organ. Whole brain offset owns clearance repair; internal folds cannot fit. Unresolved visual review: reduced brain loses fold and stem identity, so retain draft without export.

## Evidence

`batch.json` preserves the ordered UUIDs, source paths, saved reference briefs, status snapshots, final outcomes and export hashes. Numbered validation files and both candidate/native export sheets are alongside this report. The wider brain experiment is saved as `09-square-experiment-*`. No full-library metadata seeding, commit, publish or deployment was performed.
