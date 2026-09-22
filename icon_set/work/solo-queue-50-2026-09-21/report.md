# Solo queue offset 50 — 2026-09-21

Fixed batch: 10 references, in returned order. No replacement items fetched.

Nine standalone originals validate as `valid`, with zero errors and zero warnings. Light and dark contact sheets were visually inspected at native 48 pixels. Export verification is recorded separately in `verification.json`.

The one container combination was saved and read back from both gallery endpoints. No component drawing or generation jobs were started. No current-state changes caused skips. No unresolved classification or saving failures remain.

| Source UUID | Subject | Result | Source and output |
|---|---|---|---|
| 98aa08f5-1496-43e2-8294-a02bf0a05cd3 | spreadsheet-grid-with-blank-header | Valid; light/dark visual pass | [Python](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/spreadsheet_grid_with_blank_header_98aa08f5_1496_43e2_8294_a02bf0a05cd3.py) · [SVG](/Applications/Workspaces/pictographic/claude_skills/published/solo48/spreadsheet-grid-with-blank-header.svg) |
| 40a3bd08-4dc9-4334-86a0-fec93b588fee | tall-inner-rectangle-in-rounded-frame | Valid; light/dark visual pass | [Python](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/tall_inner_rectangle_in_rounded_frame_40a3bd08_4dc9_4334_86a0_fec93b588fee.py) · [SVG](/Applications/Workspaces/pictographic/claude_skills/published/solo48/tall-inner-rectangle-in-rounded-frame.svg) |
| 4efd1e1c-ec61-4fe5-b815-ddae28bc698c | blank-soft-cornered-square-border | Valid; light/dark visual pass | [Python](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/blank_soft_cornered_square_border_4efd1e1c_ec61_4fe5_b815_ddae28bc698c.py) · [SVG](/Applications/Workspaces/pictographic/claude_skills/published/solo48/blank-soft-cornered-square-border.svg) |
| b6f3e399-8c54-4b3a-be2f-789e48c4c08a | blank-rounded-square-with-straight-lower-edge | Valid; light/dark visual pass | [Python](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/blank_rounded_square_with_straight_lower_edge_b6f3e399_8c54_4b3a_be2f_789e48c4c08a.py) · [SVG](/Applications/Workspaces/pictographic/claude_skills/published/solo48/blank-rounded-square-with-straight-lower-edge.svg) |
| d70ff34b-b46b-47ce-84af-a9faa347f1ba | Three Equal Rows inside Rounded Panel | Verified container combination: Rounded square menu panel (container) + Three equal horizontal menu lines (sub) | See `4-verified.json` and `4-payloads.json` |
| 8dd962cb-3ffc-41f0-a564-b71b21cd01db | soft-cornered-nested-square-outlines | Valid; light/dark visual pass | [Python](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/soft_cornered_nested_square_outlines_8dd962cb_3ffc_41f0_a564_b71b21cd01db.py) · [SVG](/Applications/Workspaces/pictographic/claude_skills/published/solo48/soft-cornered-nested-square-outlines.svg) |
| eb1cc848-e5d7-46a2-8b20-8415af722c56 | lower-inset-square-within-rounded-border | Valid; light/dark visual pass | [Python](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/lower_inset_square_within_rounded_border_eb1cc848_e5d7_46a2_8b20_8415af722c56.py) · [SVG](/Applications/Workspaces/pictographic/claude_skills/published/solo48/lower-inset-square-within-rounded-border.svg) |
| 1924e02e-db4a-4b33-be67-bcd8d28b867c | long-drinking-straw-with-angled-bend | Valid; light/dark visual pass | [Python](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/long_drinking_straw_with_angled_bend_1924e02e_db4a_4b33_be67_bcd8d28b867c.py) · [SVG](/Applications/Workspaces/pictographic/claude_skills/published/solo48/long-drinking-straw-with-angled-bend.svg) |
| 537ef89a-3255-4de5-963f-3e20a738be5d | rounded-horizontal-strip-with-diagonal-bands | Valid; light/dark visual pass | [Python](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/rounded_horizontal_strip_with_diagonal_bands_537ef89a_3255_4de5_963f_3e20a738be5d.py) · [SVG](/Applications/Workspaces/pictographic/claude_skills/published/solo48/rounded-horizontal-strip-with-diagonal-bands.svg) |
| e5926cfa-0169-4bd6-8349-2cc298507e67 | nested-rounded-square-frame | Valid; light/dark visual pass | [Python](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/nested_rounded_square_frame_e5926cfa_0169_4bd6_8349_2cc298507e67.py) · [SVG](/Applications/Workspaces/pictographic/claude_skills/published/solo48/nested-rounded-square-frame.svg) |

## Construction and review

- Spreadsheet: VRECT_L preserves its upright table proportions; all three columns, four body rows, and blank header retained. Grid cells remain open at native size. Lucide table informed the rounded boundary and connected rules.
- Plain and nested squares: SQUARE maintains square silhouettes and balanced borders. Nested boundaries are intrinsic frame geometry, not independent content glyphs. Lucide square informed tangent quarter-circle turns. The lower inset retains its slight vertical offset; the tall inset remains taller than wide. No defining parts omitted.
- Bent straw: VRECT_M supports the long diagonal stem and shorter angled mouth end. A continuous stroke and curved elbow read cleanly in both themes. No useful Lucide straw match was found; the inspected source supplied its construction. No parts omitted.
- Striped bar: HRECT_M provides a horizontal silhouette with a thicker body than the source to accommodate stroke and spacing. Two repeated diagonal seams replace three, preserving the stripe reading. Lucide rectangle-horizontal informed the rounded contour. Both themes show open divisions with no merged gaps.

All originals preserve the full source UUID and source path. Authorship is `gpt-6-astra`. Editorial gallery briefs were preserved for standalone subjects. The menu reference brief retains its source and description, replaces obsolete solo instructions with deferred component instructions, and is stored as family `container`.

Initial build attempts encountered the shared output lock and were retried. A preliminary menu verification detected only server trimming of a trailing newline; the normalized saved text and both component records were subsequently verified.

![Light native-size review](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/solo-queue-50-2026-09-21/light.png)

![Dark native-size review](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/solo-queue-50-2026-09-21/dark.png)
