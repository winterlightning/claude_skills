# Solo queue — offset 20

Returned count: 10. Fixed worklist saved in queue.json.

Seven new SOLO48 originals were authored; a second frame reference reuses the first design under its saved editorial instruction. Two lettering references remain unresolved. No component-generation jobs were started.

The current user-restored TODO decisions were retained. Old container and component briefs are preserved as editorial history beneath verified current solo instructions.

| Source UUID | Subject | Outcome |
|---|---|---|
| `f52d2ec1-9555-4994-817d-73a093488f5a` | Email Bomb Attack | Unresolved glyph reuse; remains TODO |
| `1837ed86-65ba-5a7c-9d4a-bcb9c0b8972e` | Ancient Runic Symbols | Unresolved glyph reuse; remains TODO |
| `18f0d710-f228-47b5-b530-9b1557c6d936` | Two Overlapping Square Shapes | Generated; valid, zero warnings; actual exports visually reviewed in both themes |
| `237056af-13be-4d06-9e11-1ea0aaf3cfc3` | Overlapping Rectangular Windows | Declared reuse of two-overlapping-square-shapes; export verified |
| `d2ad2f5a-c96d-41a2-ba22-217f6b8a8dfa` | Move List Item Upward | Generated; valid, zero warnings; actual exports visually reviewed in both themes |
| `cd6cedc7-561f-411a-b476-374ac6017d69` | Square Vector Selection Tool | Generated; valid, zero warnings; actual exports visually reviewed in both themes |
| `5996b5b2-ef03-4d19-80f8-43138f7728aa` | Full Battery Level | Generated; valid, zero warnings; actual exports visually reviewed in both themes |
| `e4492a9c-8c97-4b9a-9c29-d08262d7e796` | Battery with Medium Charge | Generated; valid, zero warnings; actual exports visually reviewed in both themes |
| `058db2e8-12db-48c2-b344-337f39e8f77d` | Low Battery Level | Generated; valid, zero warnings; actual exports visually reviewed in both themes |
| `d6b813e9-7593-44ac-8b7e-dc8a1b2e1275` | Low Battery Level | Generated; valid, zero warnings; actual exports visually reviewed in both themes |

## Drawings and review

All seven drawings were inspected at native 48px on light and dark backgrounds. The shared frame has an open rear contour and clear foreground overlap. The upward movement arrow and stacked cells remain separate and legible. Four equal selection handles surround a clear central opening. The batteries retain distinct full, medium-block, low-bar, and low-block states.

Keyshapes: SQUARE for frames, list movement and selection; HRECT_M for the batteries. The rectangles match all four prescribed extremes. The full battery uses three charge bars instead of five; small battery corner curves were omitted to keep openings and terminal geometry clear. Selection handles use square corners with rounded stroke joins.

Lucide references inspected: copy (continuous rounded frame contour), list-start (open arrowhead and aligned list structure), scan (four-corner symmetry and open center), battery-full (simple case and repeated charge bars). Source renders supplied the subject and distinguishing details.

Authorship: AUTHOR = gpt-6 on the seven originals. No commits or full-library builds were requested.

## Files

[Light native-size review](light.png) · [Dark native-size review](dark.png) · [Validation](validation.json) · [Saved family readbacks](brief-save-results.json) · [Exact source/output inventory](results.json) · [Glyph handoffs](glyph-handoffs.md)

## Unresolved lettering

Email Bomb Attack: symbol-at exists, but three unchanged-glyph layout probes (12, 20 and 28 units high in a generous circular enclosure) all failed validation. See [fit diagnostics](at-glyph-fit-probes.json). No replacement letterform was drawn. Ancient Runic Symbols: exact characters remain uncertain and no Runic glyphs are available in the reusable catalog. Neither source was marked generated or reclassified.

The invoked [icon-solo-distilled skill](../../../.agents/skills/icon-solo-distilled/SKILL.md) requires glyph reuse: “reuse existing glyphs. Never draw, trace or redraw letterforms.” It also says, “Missing character: report it and leave that part unresolved.” These requirements leave the two lettering references unfinished.

## Export status

Completed: all seven distinct icons are present in published/solo48/manifest.json with valid status and zero warnings. All eight source UUID links are verified in the primitive catalog, including the declared frame reuse. Actual exported SVGs were inspected at 48 pixels in both themes. Initial lock contention was resolved by waiting; no lock was removed and no unrelated process was stopped. Eight saved family/brief updates passed exact readback verification; there were no saving failures. No new combination splits were prepared, and no items were skipped due to a status change.

## Exported previews

[Light exported SVG render](exports-light.png) · [Dark exported SVG render](exports-dark.png) · [Manifest verification](manifest-verification.json)

- Two Overlapping Square Shapes: `icon_set/model/icons/solo/two_overlapping_square_shapes_18f0d710_f228_47b5_b530_9b1557c6d936.py` → `published/solo48/two-overlapping-square-shapes.svg`
- Move List Item Upward: `icon_set/model/icons/solo/move_list_item_upward_d2ad2f5a_c96d_41a2_ba22_217f6b8a8dfa.py` → `published/solo48/move-list-item-upward.svg`
- Square Vector Selection Tool: `icon_set/model/icons/solo/square_vector_selection_tool_cd6cedc7_561f_411a_b476_374ac6017d69.py` → `published/solo48/square-vector-selection-tool.svg`
- Full Battery Level: `icon_set/model/icons/solo/full_battery_level_5996b5b2_ef03_4d19_80f8_43138f7728aa.py` → `published/solo48/full-battery-level.svg`
- Battery with Medium Charge: `icon_set/model/icons/solo/battery_with_medium_charge_e4492a9c_8c97_4b9a_9c29_d08262d7e796.py` → `published/solo48/battery-with-medium-charge.svg`
- Low Battery Level: `icon_set/model/icons/solo/low_battery_level_058db2e8_12db_48c2_b344_337f39e8f77d.py` → `published/solo48/low-battery-level.svg`
- Low Battery Level: `icon_set/model/icons/solo/low_battery_level_block_d6b813e9_7593_44ac_8b7e_dc8a1b2e1275.py` → `published/solo48/low-battery-level-block.svg`
