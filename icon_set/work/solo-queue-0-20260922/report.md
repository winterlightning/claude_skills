# Solo queue offset 0 — 2026-09-22

Fixed returned batch: **10 references**. Every source was rechecked against the same gallery status and brief endpoints immediately before intake, then rendered and visually inspected. All remained eligible; no combinations, status-change skips, or persistence failures. No component jobs were started.

**Generated: 2. Unresolved: 8. Prepared combinations: 0. Status-change skips: 0. Saving failures: 0.** Both berry originals pass registry validation with zero warnings, were built individually, and are verified in published/solo48/manifest.json. Their exported SVGs match their Python originals byte-for-byte. The eight unresolved references are not claimed as completed.

Authorship for new/revised originals: `gpt-6-astra` (an existing author value). Unrelated workspace changes were preserved.

Review evidence: [References](references.png) · [Light](light-review.png) · [Dark](dark-review.png) · [Rejected alternatives, light](light-rejected-alternatives.png) · [Rejected alternatives, dark](dark-rejected-alternatives.png). Each cell includes an actual 48-pixel render alongside an enlarged render.

## 1. Three Office Ring Binders

- UUID: `42cdb953-b64a-446a-9e2f-0a5e1116e601`
- Source: `pictographic-primitives/_uncategorized_04/archive books_42cdb953-b64a-446a-9e2f-0a5e1116e601.svg`
- Outcome: **unresolved**; validation: **valid**; keyshape: `HRECT_L`.
- Three equal 8-wide spine rectangles fit with 8-unit gaps, but labels and finger holes cannot fit inside. A single internal dot requires a 16-wide spine; three with gaps need 64 centerline units, beyond the 40-wide envelope and its diagonal. Native review: three bare rectangles lose ring-binder identity. Original draft preserved.
- References: Lucide library: repeated upright strokes.
- Original(s): `icon_set/model/icons/solo/_draft_three_labeled_ring_binders_42cdb953_b64a_446a_9e2f_0a5e1116e601.py`

## 2. Fresh Berry Fruit with Leaf

- UUID: `3278a9d5-891d-4c6a-acc3-7bd972888b5c`
- Source: `pictographic-primitives/_uncategorized_06/blackberry_3278a9d5-891d-4c6a-acc3-7bd972888b5c.svg`
- Outcome: **generated**; validation: **valid**; keyshape: `VRECT_L`.
- Rebuilt three broad drupelet regions, tapered fruit body, and upper-right leaf as a shared outline with genuine attachment seams. Omitted fine fruit lobes and stem curl. Native light/dark review: readable berry cluster and single leaf, clean openings, smooth curves.
- References: Source supplies leaf placement and fruit taper; Lucide grape supplies round-cell construction.
- Original(s): `icon_set/model/icons/solo/blackberry_cluster_with_a_single_leaf_3278a9d5_891d_4c6a_acc3_7bd972888b5c.py`

## 3. Fresh Raspberry Berry Fruit

- UUID: `86657946-998d-44be-80c5-35a4d1b96f55`
- Source: `pictographic-primitives/_uncategorized_07/boysenberry_86657946-998d-44be-80c5-35a4d1b96f55.svg`
- Outcome: **generated**; validation: **valid**; keyshape: `VRECT_L`.
- Rebuilt the three-leaf crown and tapered cluster with three broad fruit cells. Mirrored outer leaves share parameters. Omitted four smaller fruit cells. Native light/dark review: distinct three-leaf crown, readable berry body, balanced outline.
- References: Source supplies three-leaf crown and fruit taper; Lucide grape supplies round-cell construction.
- Original(s): `icon_set/model/icons/solo/raspberry_with_three_leaves_86657946_998d_44be_80c5_35a4d1b96f55.py`

## 4. Two Interlocking Gears

- UUID: `82c1163c-aaf6-4c80-9120-18bf38090361`
- Source: `pictographic-primitives/_uncategorized_12/cog double 1_82c1163c-aaf6-4c80-9120-18bf38090361.svg`
- Outcome: **unresolved**; validation: **invalid**; keyshape: `SQUARE`.
- Diagonal gear trial: gear-to-gear centerline clearance 2; axle-to-outline 5.2111; inter-gear parallel edges 4. Required clearance is 8. Four broad teeth already simplify the source eight; further removal loses gear identity. Enlarging wheel roots worsens inter-gear room.
- References: Source diagonal arrangement; Lucide cog radial repeat principle.
- Original(s): `icon_set/model/icons/solo/_draft_two_interlocking_toothed_wheels_82c1163c_aaf6_4c80_9120_18bf38090361.py`

## 5. Double Interlocking Gears

- UUID: `b484255b-2a40-40d1-9943-7e27cfb9f399`
- Source: `pictographic-primitives/_uncategorized_12/cog double_b484255b-2a40-40d1-9943-7e27cfb9f399.svg`
- Outcome: **unresolved**; validation: **invalid**; keyshape: `HRECT_L`.
- Wider diagonal layout (centers 14,30 and 34,18) still has 6-unit inter-gear parallel separation and 5.2111 axle-to-outline clearance. Native holes close visually. Upright/horizontal pairing offers less room; omitted-hole alternative would lose the characteristic axle openings.
- References: Source matching meshing wheels; Lucide cog radial repeat principle.
- Original(s): `icon_set/model/icons/solo/_draft_diagonal_pair_of_meshing_gears_b484255b_2a40_40d1_9943_7e27cfb9f399.py`

## 6. Lobster Seafood Crustacean

- UUID: `f4812ef0-fce6-4380-9124-384916ee103d`
- Source: `pictographic-primitives/_uncategorized_13/crawdad_f4812ef0-fce6-4380-9124-384916ee103d.svg`
- Outcome: **unresolved**; validation: **invalid**; keyshape: `VRECT_L`.
- Existing draft: repeated leg separations 6.94595–7.15542 and leg/tail separation 0.0879945. A reduced HRECT_L layout passed validation but lost antennae, multiple legs and fan-tail identity. Reduced trial saved; original draft restored unchanged.
- References: Inspected actual crawdad source. No useful local Lucide lobster match.
- Original(s): `icon_set/model/icons/solo/_draft_lobster_with_pointed_closed_claws_f4812ef0_fce6_4380_9124_384916ee103d.py`

## 7. Lobster Seafood Crustacean

- UUID: `813ecb4a-07a5-40d2-a4dc-2d3842c2a9f0`
- Source: `pictographic-primitives/_uncategorized_13/crayfish_813ecb4a-07a5-40d2-a4dc-2d3842c2a9f0.svg`
- Outcome: **unresolved**; validation: **invalid**; keyshape: `VRECT_L`.
- Existing draft has the same leg-spacing and tail-contact failures and does not retain open pincer notches. Reduced HRECT_L trial with broad forked pincers and fan tail passed validation, but omission of antennae and most legs weakened lobster identity. Original draft restored unchanged.
- References: Inspected actual crayfish source. No useful local Lucide lobster match.
- Original(s): `icon_set/model/icons/solo/_draft_lobster_with_broad_open_pincers_813ecb4a_07a5_40d2_a4dc_2d3842c2a9f0.py`

## 8. Triple Curved Arcs Symbol

- UUID: `e89d9bcb-0e93-4a07-abd4-7740608fbbd7`
- Source: `pictographic-primitives/_uncategorized_13/crowdin logo_e89d9bcb-0e93-4a07-abd4-7740608fbbd7.svg`
- Outcome: **unresolved**; validation: **valid**; keyshape: `HRECT_L`.
- Rebalanced the inner lower arc and increased upper-arc spacing to pass with zero warnings. Native review still loses the source broad tapered ribbons and slanted shared interruption; reads as generic curved strokes. Kept as draft, not exported.
- References: Source asymmetric interrupted bands; Lucide rss demonstrates separated nested arcs, inspected as comparison.
- Original(s): `icon_set/model/icons/solo/_draft_nested_interrupted_curved_bands_e89d9bcb_0e93_4a07_abd4_7740608fbbd7.py`

## 9. Earthquake Shelter Under Table

- UUID: `8d2595e2-135f-48bd-8886-08c5da475869`
- Source: `pictographic-primitives/_uncategorized_16/earthquake hiding proof table_8d2595e2-135f-48bd-8886-08c5da475869.svg`
- Outcome: **unresolved**; validation: **valid**; keyshape: `HRECT_L`.
- Human head radius 2 at (32,28), torso starts (22,28): exact 8-unit centerline/4-unit ink gap and correct horizontal axis. Table and vibration marks fit, but omitted arms and flattened crouching torso make the native figure read like disconnected marks. Draft retained, not exported.
- References: Source scene and human_ref/full_body_ref.png kneeling construction. No exact Lucide shelter-scene match used.
- Original(s): `icon_set/model/icons/solo/_draft_person_sheltering_beneath_shaking_table_8d2595e2_135f_48bd_8886_08c5da475869.py`

## 10. Four Stud Toy Building Brick

- UUID: `8c0da42a-e577-481a-a50e-84f0e8648aae`
- Source: `pictographic-primitives/_uncategorized_27/module four_8c0da42a-e577-481a-a50e-84f0e8648aae.svg`
- Outcome: **unresolved**; validation: **invalid / valid**; keyshape: `HRECT_L / VRECT_L`.
- Two pre-existing drafts share this source. Perspective draft has stud/body collisions and 6.05032–7 clearance failures; top-view draft is valid but resembles a button or die and loses protruding studs and two side faces. Both preserved without edits; neither exported.
- References: Source four studs and two side faces; Lucide toy-brick shows protruding-stud/body hierarchy.
- Original(s): `icon_set/model/icons/solo/_draft_four_stud_perspective_toy_brick_8c0da42a_e577_481a_a50e_84f0e8648aae.py`, `icon_set/model/icons/solo/_draft_toy_brick_with_four_top_studs_8c0da42a_e577_481a_a50e_84f0e8648aae.py`

## Verified outputs

- [Blackberry SVG](../../../published/solo48/blackberry-cluster-with-a-single-leaf.svg)
- [Raspberry SVG](../../../published/solo48/raspberry-with-three-leaves.svg)
- [Export preview, light](exports-light.png) · [Export preview, dark](exports-dark.png)

Each build checked only its requested original and reused the existing catalog. Shared build-lock conflicts were resolved by waiting and retrying; no process was interrupted and no lock was removed. No commits or full-library publish were performed.
