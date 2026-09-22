# Solo queue offset 0 — 10 references

Processed the fixed ten-item page returned at offset 0 (124 total at fetch). Seven icons generated and verified; three pre-existing drafts remain unresolved. No replacement items fetched.

All ten live status and saved-brief checks succeeded immediately before their item was processed. All references are standalone objects, scenes or anatomical depictions; no combination split or status changes were needed. No save failures and no items skipped due to changed state.

The seven generated icons pass validation with zero warnings, including the build-level hole and internal-spacing checks. Actual exported SVGs match their Python originals byte-for-byte and are present in the SOLO48 manifest. Light and dark renders were visually reviewed at 48 pixels. Only the selected originals were built; no full-library generation, metadata seeding, manual artwork import or commit was performed.

Authorship on created/revised originals: `gpt-6-astra`. The unrelated working changes and three existing unresolved drafts were preserved.

Preview: `export-preview.png`. Evidence: `results.json`, `manifest-verification.json`, original `build.log`, repaired `helmet-build.log`, and `helmet-qa.json`. Initial candidate renders are retained separately.

## Three Office Ring Binders

- UUID: `42cdb953-b64a-446a-9e2f-0a5e1116e601`
- Source: `pictographic-primitives/_uncategorized_04/archive books_42cdb953-b64a-446a-9e2f-0a5e1116e601.svg`
- Original: `icon_set/model/icons/solo/_draft_three_labeled_ring_binders_42cdb953_b64a_446a_9e2f_0a5e1116e601.py`
- Outcome: unresolved
- Validation: status: valid

Unresolved. The existing HRECT_L draft passes numeric validation but renders as three empty bars. Three 8-unit spines plus two 8-unit gaps consume all 40 horizontal units; labels or finger holes need substantially wider spines. Upright or diagonal fitting cannot preserve all three labeled binders within SOLO48. Existing draft retained without alteration; not exported.

## Bicycle Parked in Rack

- UUID: `f7ac223a-3452-4084-8389-29ffab6bfcef`
- Source: `pictographic-primitives/_uncategorized_06/bike parking 1_f7ac223a-3452-4084-8389-29ffab6bfcef.svg`
- Original: `icon_set/model/icons/solo/bicycle_parked_in_rack_f7ac223a_3452_4084_8389_29ffab6bfcef.py`
- Outcome: generated and verified
- Validation: status: valid; zero errors and zero warnings; build-level hole and internal-spacing checks passed
- Export: `published/solo48/bicycle-parked-in-rack.svg`
- Manifest: `published/solo48/manifest.json`

Final export reviewed in light and dark at 48px. HRECT_M preserves two wheels and the physical parking stand. Replaced the crowded full right wheel with its visible semicircle, meeting split stand endpoints. Omitted pedals and the inner frame triangle. Lucide bike supplied equal wheel construction.

## Cycling Safety Helmet

- UUID: `08152344-8f0e-4721-af0a-ec9f68eb4218`
- Source: `pictographic-primitives/_uncategorized_06/biking helmet_08152344-8f0e-4721-af0a-ec9f68eb4218.svg`
- Original: `icon_set/model/icons/solo/domed_cycling_helmet_with_chin_strap_08152344_8f0e_4721_af0a_ec9f68eb4218.py`
- Outcome: generated and verified
- Validation: status: valid; zero errors and zero warnings; build-level hole and internal-spacing checks passed
- Export: `published/solo48/domed-cycling-helmet-with-chin-strap.svg`
- Manifest: `published/solo48/manifest.json`

Final export reviewed in light and dark at 48px. HRECT_L keeps a broad low dome and recognizable buckle with hanging strap. Reduced the buckle to a diameter-6 circle and flattened the dome to extend the tail. Omitted strap thickness. Lucide hard-hat supplied dome/rim construction. The first build caught rim/buckle clearance below four ink units; moving the buckle center to (28,31) repaired the gap. The second targeted build passed.

## Deciduous Birch Tree

- UUID: `0dbbf821-c347-4e4b-b992-d0bdebc25338`
- Source: `pictographic-primitives/_uncategorized_06/birch_0dbbf821-c347-4e4b-b992-d0bdebc25338.svg`
- Original: `icon_set/model/icons/solo/rounded_tree_with_one_branch_0dbbf821_c347_4e4b_b992_d0bdebc25338.py`
- Outcome: generated and verified
- Validation: status: valid; zero errors and zero warnings; build-level hole and internal-spacing checks passed
- Export: `published/solo48/rounded-tree-with-one-branch.svg`
- Manifest: `published/solo48/manifest.json`

Final export reviewed in light and dark at 48px. VRECT_L retains the tall rounded crown, smaller upper lobe, centered trunk and single right branch. Crown mirrors about x=24; branch is intentionally asymmetric. Lucide tree-deciduous supplied canopy/trunk construction. No unsupported bark marks added.

## Domed Bird Cage with Perch

- UUID: `68164997-d185-4b80-87f8-d9463fb372a8`
- Source: `pictographic-primitives/_uncategorized_06/bird cage empty_68164997-d185-4b80-87f8-d9463fb372a8.svg`
- Original: `icon_set/model/icons/solo/domed_birdcage_with_a_central_perch_68164997_d185_4b80_87f8_d9463fb372a8.py`
- Outcome: generated and verified
- Validation: status: valid; zero errors and zero warnings; build-level hole and internal-spacing checks passed
- Export: `published/solo48/domed-birdcage-with-a-central-perch.svg`
- Manifest: `published/solo48/manifest.json`

Final export reviewed in light and dark at 48px. VRECT_L retains dome, knob, rectangular base and centered bar/perch. Physical perch is intrinsic, so no component split. Lucide bell supplied arched shoulder construction. Knob simplified to a small loop.

## Fresh Berry Fruit with Leaf

- UUID: `3278a9d5-891d-4c6a-acc3-7bd972888b5c`
- Source: `pictographic-primitives/_uncategorized_06/blackberry_3278a9d5-891d-4c6a-acc3-7bd972888b5c.svg`
- Original: `icon_set/model/icons/solo/_draft_blackberry_cluster_with_a_single_leaf_3278a9d5_891d_4c6a_acc3_7bd972888b5c.py`
- Outcome: unresolved
- Validation: status: valid

Unresolved. The existing VRECT_L draft passes numeric validation but its single scalloped silhouette lacks separate drupelets and reads as generic fruit. The actual source has eight overlapping drupelets with one leaf. Existing draft retained without alteration; not exported.

## Whale Spouting Water

- UUID: `231dc062-282f-4d6f-ad1c-b148bd0de9d8`
- Source: `pictographic-primitives/_uncategorized_07/blowhole_231dc062-282f-4d6f-ad1c-b148bd0de9d8.svg`
- Original: `icon_set/model/icons/solo/whale_with_two_arcing_spouts_231dc062_282f_4d6f_ad1c_b148bd0de9d8.py`
- Outcome: generated and verified
- Validation: status: valid; zero errors and zero warnings; build-level hole and internal-spacing checks passed
- Export: `published/solo48/whale-with-two-arcing-spouts.svg`
- Manifest: `published/solo48/manifest.json`

Final export reviewed in light and dark at 48px. HRECT_L retains left-facing whale, eye, lower flipper, lobed tail and two water arcs. Enlarged useful eye space by moving the eye toward the center of the head/body; final clearance passes. Omitted mouth seam. No useful local Lucide whale match.

## Baby Bonnet Hat

- UUID: `83e67aec-5937-46a8-b003-935e44c13b02`
- Source: `pictographic-primitives/_uncategorized_07/bonnet_83e67aec-5937-46a8-b003-935e44c13b02.svg`
- Original: `icon_set/model/icons/solo/tied_infant_bonnet_83e67aec_5937_46a8_b003_935e44c13b02.py`
- Outcome: generated and verified
- Validation: status: valid; zero errors and zero warnings; build-level hole and internal-spacing checks passed
- Export: `published/solo48/tied-infant-bonnet.svg`
- Manifest: `published/solo48/manifest.json`

Final export reviewed in light and dark at 48px. VRECT_L preserves domed bonnet, sweeping opening band and two hanging ties. Fine bow loops were omitted to keep the lower opening legible. Lucide hard-hat contributed coherent crown curves; source supplies bonnet-specific opening and ribbons.

## Fresh Raspberry Berry Fruit

- UUID: `86657946-998d-44be-80c5-35a4d1b96f55`
- Source: `pictographic-primitives/_uncategorized_07/boysenberry_86657946-998d-44be-80c5-35a4d1b96f55.svg`
- Original: `icon_set/model/icons/solo/_draft_raspberry_with_three_leaves_86657946_998d_44be_80c5_35a4d1b96f55.py`
- Outcome: unresolved
- Validation: status: valid

Unresolved. The existing VRECT_L draft passes numeric validation but has only one leaf and no visible separate drupelets, contrary to the three-leaf source. Existing draft retained without alteration; not exported.

## Human Brain in Open Head

- UUID: `057618af-fa4d-4d15-af45-d4d6842883c1`
- Source: `pictographic-primitives/_uncategorized_07/brain open skill_057618af-fa4d-4d15-af45-d4d6842883c1.svg`
- Original: `icon_set/model/icons/solo/exposed_brain_above_open_head_057618af_fa4d_4d15_af45_d4d6842883c1.py`
- Outcome: generated and verified
- Validation: status: valid; zero errors and zero warnings; build-level hole and internal-spacing checks passed
- Export: `published/solo48/exposed-brain-above-open-head.svg`
- Manifest: `published/solo48/manifest.json`

Final export reviewed in light and dark at 48px. VRECT_L retains exposed lobed brain above horizontal skull opening and tapered rear neck. Repaired the fold clearance by attaching its start to an actual crown node. Lucide brain supplied scalloped lobes and attached crease; human_ref/user.svg reviewed, but anatomical head section does not use detached head/torso construction. Preserved existing draft geometry outside that repair and updated source/editorial metadata.
