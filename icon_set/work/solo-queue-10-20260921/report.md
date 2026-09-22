# Solo queue offset 10 — 2026-09-21

Requested offset **10**, returned **10** items, processed in original order without replacement fetches. Gallery: `http://localhost:8000`. All current status records were absent (default TODO), with saved family solo. Per-item status and saved-brief snapshots, exact UUIDs and source paths are retained in `frozen-intake.json`. Every actual reference was rendered and visually inspected before its processing decision.

**Final outcome: 2 generated and verified exports; 7 unresolved candidates; 1 ambiguous reference not drawn.** No container or side combinations were identified; no classification/brief writes or save failures occurred. No status-change skips. Prior unrelated edits and drafts were preserved. New author value: `gpt-6-astra`.

| UUID | Subject | Outcome and evidence |
|---|---|---|
| b014012a-ab85-4245-8dbd-a66dc5a899be | Curved sausage with tied ends | New original, valid with zero warnings. HRECT_M preserves the shallow crescent and mirrored forked ties. Reference supplies silhouette; no Lucide sausage match. Tiny end rounding omitted. Clear sausage casing and ties in light/dark native review. |
| e6e7ff28-6ade-4296-95f7-4a6c7bd1ce2a | Litter tray with slotted scoop | Unresolved visual draft. Existing SQUARE candidate validates, but upright scoop reads as a cup/straw. Prior diagonal attempt failed envelope and slot clearance; inspected source requires a broad slotted scoop leaning from a shallow tray. Existing modified draft preserved. |
| a31f3f41-e636-492d-ad83-a82ed5593583 | Open-front hooded cloak | Unresolved visual draft. Existing VRECT_L candidate validates but reads as a badge/medal, with hood disproportionately dominant. Prior smaller-hood trial had curved-clearance review. No export claimed. |
| e886dcde-7af5-41c6-a333-6a6ddf119555 | Right arrow between data rows | New original, valid with zero warnings. HRECT_L; paired rows derive from one mirrored definition. Five ticks reduced to three. Source supplies rows/U interruptions, inspected Lucide arrow-right original and atoms supply shaft/head shared-node construction. Clear arrow and separated rows in both themes at 48px. This is an integrated flow diagram, without a meaningful wrapper or separate side badge. |
| 82c1163c-aaf6-4c80-9120-18bf38090361 | Two interlocking toothed wheels | Unresolved spacing. Adapted the earlier paired-gear construction to HRECT_L with wider horizontal spacing. Gear/hub gaps 6.0628, gear/gear gap 3.16228, and parallel tooth edges 6 units all fail the 8-unit centerline minimum. See `gears-separated.py` and per-UUID validation. Lucide cog original and atoms inspected for radial repetition. Circular hubs and meshing teeth cannot both be retained by this attempted layout. |
| b484255b-2a40-40d1-9943-7e27cfb9f399 | Diagonal pair of meshing gears | Unresolved visual review. Revalidated the earlier SQUARE shared-silhouette experiment: valid, zero warnings, but reads as a single toothed link rather than two meshing wheels in both themes. Separate-gear and shared-silhouette approaches are documented in the prior queue70 evidence. No export claimed. |
| f4812ef0-fce6-4380-9124-384916ee103d | Lobster with pointed closed claws | Unresolved existing VRECT_L draft. Revalidation fails parallel leg spacing (6.94595–7.15542 versus required 8) and lower leg/tail clearance (0.08799). Native render crowds the anatomy and weakens pointed claw identity. Preserved without exporting. |
| 813ecb4a-07a5-40d2-a4dc-2d3842c2a9f0 | Lobster with broad open pincers | Unresolved existing VRECT_L draft. Same leg/tail spacing failures; native render also lacks the source’s distinctive open pincer notches. Preserved without exporting. |
| 7f4d0d07-e981-4efd-ae8c-b673077a9b75 | Pick entering open padlock | Unresolved existing VRECT_L draft. Lock/pick clearance 3.90434 and lock/handle 4.85549 versus required 8. Native render merges handle and bent pick into the lock. Physical tool interaction is standalone, not a side modifier. Preserved without exporting. |
| e89d9bcb-0e93-4a07-abd4-7740608fbbd7 | Nested interrupted curved bands | Unresolved reference ambiguity. Actual reference is clipped at right and shows two nested outlined curved bands, while saved description specifies three broad bands. No confident third band or complete right endpoints can be established; no drawing or forced classification. |

## Build verification

Initial sausage export attempts encountered the shared output lock; no lock was removed and no other build was interrupted. The data-flow targeted build succeeded and its solo manifest entry has zero errors and warnings. The sausage passes full `inspect_icon` QA, including internal spacing and holes. Both targeted builds succeeded. Both exports are present in the solo manifest with valid status, zero errors and zero warnings; hashes and QA are recorded in `export-verification.json`. Actual exported SVGs were visually inspected in light and dark at native 48px plus enlargement (`exports-light.png`, `exports-dark.png`); both retain recognition, open negative space and the intended mirrored construction.

## Source and export paths

- Sausage original: `icon_set/model/icons/solo/curved_sausage_with_tied_ends_b014012a_ab85_4245_8dbd_a66dc5a899be.py`
- Sausage export: `published/solo48/curved-sausage-with-tied-ends.svg`
- Data-flow original: `icon_set/model/icons/solo/arrow_right_data_flow_e886dcde_7af5_41c6_a333_6a6ddf119555.py`
- Data-flow export: `published/solo48/arrow-right-data-flow.svg`

Per-UUID `*-validation.txt`, `*-reference.png`, `*-light.png`, and `*-dark.png` preserve the inspected candidates and references. Native renders use the repository contact-sheet rendering function. No full-library build, metadata seeding, commit, component job, or original reference modification was performed.
