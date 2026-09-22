# Queue offset 0 — 10 references

The original HTTP response returned 10 references from 75 eligible items. The UUID worklist stayed fixed and was processed in order; no replacement page was fetched. Current status and saved brief were read from the same local gallery immediately before each item’s intake, with effective catalog status also checked. All remained TODO, without generated models. The ninth item’s saved family is sub, with an authoritative family selection included in the fetched queue response.

## Accounting

**Outcome: 1 generated sub-family icon; 9 unresolved references; 0 prepared combinations; 0 status-change skips.** The new original was authored, validated, built and visually approved. No solo export is claimed for an unresolved draft. No combinations were identified, no status-change skips occurred, and no classification/brief POSTs were necessary. There are no saving failures or retry payloads. See `09-build.txt` and `export-verification.json` for the final export outcome.

| # | Original source UUID | Subject | Outcome and evidence |
|---|---|---|---|
| 1 | `42cdb953-b64a-446a-9e2f-0a5e1116e601` | Three Office Ring Binders | Unresolved visual identity. Revalidated existing HRECT_L draft: valid, zero warnings. Three empty rectangular spines lose the reference label holders and finger holes. Reviewed at 48 px in both themes; draft preserved. |
| 2 | `3278a9d5-891d-4c6a-acc3-7bd972888b5c` | Fresh Berry Fruit with Leaf | Unresolved visual identity. Revalidated existing VRECT_L draft: valid, zero warnings. The scalloped empty body reads as a bowl and loses the overlapping round blackberry cells. Reviewed at 48 px in both themes; draft preserved. |
| 3 | `86657946-998d-44be-80c5-35a4d1b96f55` | Fresh Raspberry Berry Fruit | Unresolved visual identity. Revalidated existing VRECT_L draft: valid, zero warnings. The draft reduces three leaves to one and loses the raspberry cells. Reviewed at 48 px in both themes; draft preserved. |
| 4 | `82c1163c-aaf6-4c80-9120-18bf38090361` | Two Interlocking Gears | Unresolved spacing. Inspected source and prior diagonal gear trial. Prior measured gear/hub clearance is 5.071 and gear/gear clearance is 2.828 centerline units, below 8. Prior trial is not a new validation result; no export claimed. |
| 5 | `b484255b-2a40-40d1-9943-7e27cfb9f399` | Double Interlocking Gears | Unresolved spacing. Inspected this source separately: same diagonal meshing-wheel construction and clear hub holes. The shared prior gear trial has the same unresolved 5.071/2.828-unit clearances. No export claimed. |
| 6 | `f4812ef0-fce6-4380-9124-384916ee103d` | Lobster Seafood Crustacean | Unresolved validation and visual quality. Existing lobster draft freshly fails parallel leg clearance (6.946–7.155 versus 8) and last-leg/tail separation (0.088 versus 8). Thin crowded claws and fused lower limbs do not reproduce the source clearly. Preserved existing draft. |
| 7 | `813ecb4a-07a5-40d2-a4dc-2d3842c2a9f0` | Lobster Seafood Crustacean | Unresolved validation and visual quality. Existing draft has the same fresh leg and tail failures. Its small closed claw shapes also lose this source’s broad open pincers. Preserved existing draft. |
| 8 | `e89d9bcb-0e93-4a07-abd4-7740608fbbd7` | Triple Curved Arcs Symbol | Unresolved reference interpretation; no drawing. Actual reference has two nested outlined crescents, each interrupted into upper and lower pieces, with tapered ends. Saved text says three broad curved bands. I could not reconcile the intended count and outline treatment confidently; no forced reclassification or generic arc substitution. |
| 9 | `566c0e57-a142-4e0c-b0fc-b66d54d9dee7` | Double Downward Chevron | New complete SUB32 model. Preserved the saved user-selected sub family. Both equal V marks, four arms, downward direction and square proportions retained. SQUARE; valid with zero warnings. Native 32 px and enlarged light/dark renders reviewed. Container-circle composition is valid. Export verification recorded separately. |
| 10 | `8d2595e2-135f-48bd-8886-08c5da475869` | Earthquake Shelter Under Table | Unresolved visual identity. The source is a natural sheltering scene, not a container combination. New HRECT_L stick-figure trial validates without warnings with exact head/torso gap, but its compact body reads as a zigzag beside a circle. SQUARE curved-body alternative remains review (table/torso clearance) and still lacks a convincing crouching pose. Trials retained under work; no model registered or export claimed. |

## New chevron

Two equal downward chevrons retain all four arms and both points. SQUARE gives centerline bounds (2,2)–(30,30); a shared 14-unit arm span and 14-unit vertical step preserve symmetry and repeat spacing. No parts were omitted. The source supplies the square aspect and wide arms. Lucide `chevrons-down` and its atomic geometry supply the continuous V contour and equal-repeat construction principle. Both native and enlarged light/dark views show clean round joints, equal arms, an open gap, and the correct direction. Source coverage and numeric validation both pass. The composition with `container-circle` validates as well.

- Python: `icon_set/model/icons/sub/chevron_double_down_with_wide_arms_566c0e57_a142_4e0c_b0fc_b66d54d9dee7.py`
- Export: `published/sub32/chevron-double-down-with-wide-arms.svg`
- Author: `gpt-6-astra`
- Preview: `09-model-light-32.png`, `09-model-dark-32.png`, enlarged 192 px companions, and `sub-light.png` / `sub-dark.png` contact sheets.
- Composition: `composition/container-circle-chevron-double-down-with-wide-arms.svg` and its report.

The default composition command encountered an existing path-reporting bug after writing its SVG. Re-running with an absolute work-directory destination succeeded. No tool code was changed.

## Unresolved construction evidence

The prior binder layout fills a 40-unit span with three 8-unit spines and two 8-unit gaps. A diameter-4 hole with 8-unit clearance to both spine walls needs a 20-unit spine, exceeding the available span when repeated three times. This explains the existing draft’s loss of its distinguishing details; it does not prove every possible reconstruction impossible.

Both berry references are physical clusters with their own leaves, not combinations. The inspected Lucide `grape` construction uses separate round cells; keeping those cells readable remains the unresolved part of these drafts. The current valid but empty scalloped outlines are not accepted substitutes. Lucide `library` supplied the repeated upright construction comparison for the binders; `shrimp` was inspected for crustacean curves and segmented anatomy but is not a direct match for the raised-claw frontal lobsters. Their atomic geometry was inspected. The gear trial was retained from the prior run and visually checked again; no unsupported claim of fresh gear validation is made.

For the shelter scene, `icon_set/references/human_ref/full_body_ref.png` supplies the circular head and minimal round-ended crouching figure. Lucide `table` was inspected but is a data grid and is not a useful furniture match. The source’s table and shaking marks inform both trials. The first uses HRECT_L, head center (32,32), radius 4, torso junction (20,32): 12−4=8 centerline units, exactly 4 visible ink units. It omits the tabletop thickness, outlined limbs and fingers; the resulting pose is insufficiently clear. The second uses SQUARE and a curved leg, but remains visually unresolved and has one MIC warning. Neither is a completed icon.

## Preservation

Exact UUIDs, paths and the saved editorial briefs remain in the per-item current records. `fixed-worklist.json` indexes them. All actual source SVGs were rendered and visually inspected. Existing artwork, draft originals, metadata, statuses and briefs were left unchanged. Only the new chevron was selected for a targeted build; no full-library build, metadata seeding, publish, commit or deployment was requested. The shared output lock was respected while other builds ran.

## Final checks

The targeted build completed successfully: 1 of 1,562 sub originals was checked, with the other 1,561 reused. The chevron is present in `published/sub32/manifest.json`; its SVG matches the current validated Python geometry byte for byte. Validation has zero errors and zero warnings. The actual exported SVG was rendered for native 32 px light/dark review.

Existing workflow-isolation, generation and metadata tests: **37 passed**. The first sandboxed attempt could not bind temporary test servers; the permitted rerun passed. The tests emitted existing unclosed-database ResourceWarnings; these are separate from the icon’s zero-warning geometry validation.
