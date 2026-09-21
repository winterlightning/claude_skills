# Text and numbers

Any actual letters, words, digits or numbers, alone or inside another icon, reuse existing glyphs. Never draw, trace or redraw letterforms.

- Look up each character in `icon_set/typeface/glyphs.json`; reuse its `icon_id` and paths. Use `preferred` unless a variant is requested. Preserve case, content and arrangement.
- Base glyphs: stroke envelope 24 high, width a whole unit; read `stroke_width`, `ink_width`, `ink_height`, baseline and body metrics from the glyph. Do not use the older free-proportion source geometry.
- Standalone glyphs at heights 12 to 32: use `gallery/typeface/sizes/<height>/<icon_id>.svg` (generate with `python3 -m icon_set typeface-sizes`). Width = base width x height / 24 rounded to the nearest even integer, odd ties up. Stroke stays 4; flat marks and dots stay 4 tall, centred.
- Combined reference: author the non-text part normally; record the text as a reuse/layout brief with the exact string and glyph ids. Same for Pending briefs.
- Missing character: report it and leave that part unresolved.

Objects about writing (pen, calculator) are not text.
