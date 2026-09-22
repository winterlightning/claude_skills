# Solo queue offset 70

Fetched 10 items from http://localhost:8000 with the default page size. The worklist remained fixed; no replacement items or next page were fetched. Each item was checked against the status and saved-brief endpoints immediately before intake. Actual reference renders were inspected.

Four new icons were exported, verified in the solo manifest, matched byte-for-byte against their current Python originals, and visually reviewed from the actual exports in both themes. The repaired berry original passes full QA with no errors or warnings and has been visually reviewed, but its canonical export remains blocked by the shared build lock after 20 retries plus a final attempt. It is not counted as generated. Summary: 4 generated, 1 export-blocked, 5 unresolved. Three source UUIDs had earlier tracked drafts that still fail validation and remain unresolved. One gear attempt failed clearance checks and its numeric-passing alternative failed visual review; one cropped abstract reference remains ambiguous. No item was skipped due to a changed gallery status. No combinations were identified or saved. No gallery classification or brief records were changed, and no save failures occurred.

Author metadata: `gpt-6`. Existing editorial briefs are preserved in `frozen-intake.json`; original reference artwork is unchanged.

## 1. Double Interlocking Gears
UUID: `b484255b-2a40-40d1-9943-7e27cfb9f399`

Source: `pictographic-primitives/_uncategorized_12/cog double_b484255b-2a40-40d1-9943-7e27cfb9f399.svg`

**Unresolved: clearance validation failed.** Standalone diagonal gear pair. Two matching toothed outlines and circular hubs were attempted in SQUARE, then tooth widths were enlarged from 6 to 8 units. The diagonal arrangement still leaves only 2.83 units between gears, approximately 6.06 between each hub and its gear, and 5 between some parallel inter-gear edges; SOLO48 requires 8 centerline units. No contact exemptions or contract changes were added. Lucide cog supplied radial repetition; the source supplied the paired meshing arrangement.
Unexported experiment: `icon_set/work/queue70/gears-first-attempt.py`
Validation findings: `gears-validation.txt`. A second layout used one shared meshing outline with hub dots; it passed numerical validation but visually resembled a linkage rather than two distinct meshing gears at 48px. That rejected alternative is retained as `gears-shared-silhouette-attempt.py` with both theme renders. No rejected candidate remains in the active model registry.

## 2. Decorating Smiley Face Cookie
UUID: `904b04ae-403a-4be5-b2d3-bed163228a74`

Source: `pictographic-primitives/_uncategorized_13/cookies decirating 1_904b04ae-403a-4be5-b2d3-bed163228a74.svg`

Standalone. **Generated: valid, zero warnings; light/dark native review passed; SVG and manifest verified.** Keyshape `SQUARE` fits the subject proportions. Round cookie with diagonal piping tip; circular eyes reduced to dots. The cookie and piping action remain legible in both themes.
Construction reference: local Lucide `cookie` original and atomic geometry; re-authored on SOLO48. Source and construction contributions are documented in the module.
Original: `icon_set/model/icons/solo/piping_a_smiling_cookie_904b04ae_403a_4be5_b2d3_bed163228a74.py`
Export: `published/solo48/piping-a-smiling-cookie.svg`

## 3. Cylindrical Wine Bottle Cork
UUID: `d2fd87af-78f7-4b97-939a-7bdc6346bac4`

Source: `pictographic-primitives/_uncategorized_13/cork_d2fd87af-78f7-4b97-939a-7bdc6346bac4.svg`

Standalone. **Generated: valid, zero warnings; light/dark native review passed; SVG and manifest verified.** Keyshape `VRECT_M` fits the subject proportions. Tall cork with elliptical top and two separated grain marks; top scratch and extra grain omitted. Rim and grain remain clear in both themes.
Construction reference: local Lucide `cylinder` original and atomic geometry; re-authored on SOLO48. Source and construction contributions are documented in the module.
Original: `icon_set/model/icons/solo/upright_cylindrical_cork_stopper_d2fd87af_78f7_4b97_939a_7bdc6346bac4.py`
Export: `published/solo48/upright-cylindrical-cork-stopper.svg`

## 4. Berries with Stem and Leaf
UUID: `caa9f497-47bb-4168-ab8e-e78de139cf75`

Source: `pictographic-primitives/_uncategorized_13/cranberry_caa9f497-47bb-4168-ab8e-e78de139cf75.svg`

Standalone. **Export blocked: current original passes full QA with zero errors/warnings and light/dark native review. Not counted as generated.** Keyshape `SQUARE` fits the subject proportions. Three berries with a shared front rim, stem and leaf; texture omitted. The final repair widens the leaf, enlarges its clearance above the fruit, and reduces the front berry radius to retain rounded rear lobes. Full build QA preflight passes with no errors or warnings, including holes and internal spacing. Three fruit lobes and the leaf remain readable in both themes.
Construction reference: local Lucide `cherry` original and atomic geometry; re-authored on SOLO48. Source and construction contributions are documented in the module.
Original: `icon_set/model/icons/solo/three_round_berries_on_stem_caa9f497_47bb_4168_ab8e_e78de139cf75.py`
Pending export: `published/solo48/three-round-berries-on-stem.svg`

The first published build rejected the earlier narrow leaf. That earlier failure may remain visible in the Failed build gallery until the repaired original can be exported. The repair passes `inspect_icon` including holes and internal spacing; see `berries-full-qa.json`. The canonical build was blocked by another process holding `published/`. No lock was removed or other process interrupted.

Retry when the output lock is free:

```sh
rtk proxy python3 -m icon_set build --icon icon_set/model/icons/solo/three_round_berries_on_stem_caa9f497_47bb_4168_ab8e_e78de139cf75.py --no-png --no-report
```

## 5. Lobster Seafood Crustacean
UUID: `f4812ef0-fce6-4380-9124-384916ee103d`

Source: `pictographic-primitives/_uncategorized_13/crawdad_f4812ef0-fce6-4380-9124-384916ee103d.svg`

**Unresolved: earlier draft still fails validation.** Gallery reported TODO with no exported model; the UUID search found a tracked draft. Revalidated and visually inspected the existing draft, saved its failure evidence, and preserved it without creating a duplicate or claiming completion.
Existing draft: `icon_set/model/icons/solo/_draft_lobster_with_pointed_closed_claws_f4812ef0_fce6_4380_9124_384916ee103d.py`
The inspected source is a standalone physical subject/scene, not a modifier combination. The two lobster drafts have leg runs separated by only 6.95–7.16 centerline units and nearly coincident lower-leg/tail geometry. Their native renders are crowded and do not convincingly preserve the specified claw shapes. The padlock draft has only 3.90 units between lock and pick and 4.86 between lock and handle. SOLO48 requires 8 centerline units. Per-UUID draft validation logs and renders are saved beside this report.

## 6. Lobster Seafood Crustacean
UUID: `813ecb4a-07a5-40d2-a4dc-2d3842c2a9f0`

Source: `pictographic-primitives/_uncategorized_13/crayfish_813ecb4a-07a5-40d2-a4dc-2d3842c2a9f0.svg`

**Unresolved: earlier draft still fails validation.** Gallery reported TODO with no exported model; the UUID search found a tracked draft. Revalidated and visually inspected the existing draft, saved its failure evidence, and preserved it without creating a duplicate or claiming completion.
Existing draft: `icon_set/model/icons/solo/_draft_lobster_with_broad_open_pincers_813ecb4a_07a5_40d2_a4dc_2d3842c2a9f0.py`
The inspected source is a standalone physical subject/scene, not a modifier combination. The two lobster drafts have leg runs separated by only 6.95–7.16 centerline units and nearly coincident lower-leg/tail geometry. Their native renders are crowded and do not convincingly preserve the specified claw shapes. The padlock draft has only 3.90 units between lock and pick and 4.86 between lock and handle. SOLO48 requires 8 centerline units. Per-UUID draft validation logs and renders are saved beside this report.

## 7. Diagonal Wax Crayon
UUID: `93905fae-078a-429e-9b1f-d3c33e7f679e`

Source: `pictographic-primitives/_uncategorized_13/crayon_93905fae-078a-429e-9b1f-d3c33e7f679e.svg`

Standalone. **Generated: valid, zero warnings; light/dark native review passed; SVG and manifest verified.** Keyshape `SQUARE` fits the subject proportions. Diagonal wax crayon with two wrapper boundaries; duplicate narrow tip band omitted. The broad wrapper and tapered end remain legible in both themes.
Construction reference: local Lucide `pencil` original and atomic geometry; re-authored on SOLO48. Source and construction contributions are documented in the module.
Original: `icon_set/model/icons/solo/diagonal_crayon_with_wrapper_bands_93905fae_078a_429e_9b1f_d3c33e7f679e.py`
Export: `published/solo48/diagonal-crayon-with-wrapper-bands.svg`

## 8. Lockpicking a Padlock
UUID: `7f4d0d07-e981-4efd-ae8c-b673077a9b75`

Source: `pictographic-primitives/_uncategorized_13/crime tools loackpick unlock_7f4d0d07-e981-4efd-ae8c-b673077a9b75.svg`

**Unresolved: earlier draft still fails validation.** Gallery reported TODO with no exported model; the UUID search found a tracked draft. Revalidated and visually inspected the existing draft, saved its failure evidence, and preserved it without creating a duplicate or claiming completion.
Existing draft: `icon_set/model/icons/solo/_draft_pick_entering_open_padlock_7f4d0d07_e981_4efd_ae8c_b673077a9b75.py`
The inspected source is a standalone physical subject/scene, not a modifier combination. The two lobster drafts have leg runs separated by only 6.95–7.16 centerline units and nearly coincident lower-leg/tail geometry. Their native renders are crowded and do not convincingly preserve the specified claw shapes. The padlock draft has only 3.90 units between lock and pick and 4.86 between lock and handle. SOLO48 requires 8 centerline units. Per-UUID draft validation logs and renders are saved beside this report.

## 9. Elegant Ball Gown Dress
UUID: `ff85b0ce-bebc-440e-aed8-c28fc6532c33`

Source: `pictographic-primitives/_uncategorized_13/crinoline_ff85b0ce-bebc-440e-aed8-c28fc6532c33.svg`

Standalone. **Generated: valid, zero warnings; light/dark native review passed; SVG and manifest verified.** Keyshape `SQUARE` fits the subject proportions. Symmetric sweetheart bodice and broad bell skirt; no added folds. Neckline, waist and hem remain distinct in both themes.
Construction reference: local Lucide `shirt` original and atomic geometry; re-authored on SOLO48. Source and construction contributions are documented in the module.
Original: `icon_set/model/icons/solo/sweetheart_bodice_ball_gown_ff85b0ce_bebc_440e_aed8_c28fc6532c33.py`
Export: `published/solo48/sweetheart-bodice-ball-gown.svg`

## 10. Triple Curved Arcs Symbol
UUID: `e89d9bcb-0e93-4a07-abd4-7740608fbbd7`

Source: `pictographic-primitives/_uncategorized_13/crowdin logo_e89d9bcb-0e93-4a07-abd4-7740608fbbd7.svg`

**Unresolved: reference interpretation.** The actual SVG is cropped at the right edge and visually presents two nested outlined curved bands split by an oblique gap; the saved brief describes three broad bands. The intended third band and missing right endpoints cannot be resolved confidently from this reference. No original was drawn, no classification was forced, and the saved editorial brief remains unchanged.

## Evidence

- `frozen-intake.json`: ordered UUIDs, exact source paths, current status and saved editorial briefs.
- `reference-0.png` through `reference-9.png`: inspected reference renders.
- `preview-light.png` and `preview-dark.png`: final five candidates, each enlarged and at native 48px.
- Per-icon validation files: all five are `status: valid`.

- `export-verification.json`: four completed exports, manifest hashes, and exact current-original matches.
- `export-light.png` and `export-dark.png`: actual exported SVGs at enlarged and native size.
- `berries-full-qa.json`: full passing QA for the unexported repair.
