# Text and number icons

Use the existing **typeface** glyphs for icons representing letters, words,
abbreviations, digits, or numbers, including text within or beside another icon.
Do not invent, trace, or redraw replacement letter/number geometry as a new
solo or sub icon.

Look up the exact characters in `icon_set/typeface/glyphs.json` and reuse their
existing `icon_id` and paths. Use the `preferred` glyph unless a specific variant
is requested. Preserve case, readable content, and meaningful arrangement.
Use the stored grid-fitted base: every glyph's visible stroke envelope is 24
units high and its width is a whole grid unit. Read `stroke_width`, `ink_width`,
and `ink_height` from the glyph; flat marks use a 24-unit stroke to reach the
required height. Preserve the stored baseline/body metrics for text layout.
Do not replace these paths with the older free-proportion source geometry.

For standalone glyphs at heights 12 through 32, reuse the generated size-specific
SVGs under `gallery/typeface/sizes/<height>/<icon_id>.svg`. Every integer height
is supported. Generate these with `python3 -m icon_set typeface-sizes`; normal
gallery builds also export them. Width is the base width times height / 24,
rounded to the nearest whole unit (half upward). Stroke width stays exactly 4 in final coordinates at every size. Geometry
is fitted before export; no transform scales the stroke. Zero-width centerlines
(such as i) stay 4 units wide. Flat marks and point-only glyphs remain 4 units
tall, centered in the requested height. Read `ink_height` and `ink_top` separately
from the canvas height for these cases. These size-specific exports supersede
the base catalog's enlarged flat-mark stroke treatment.


For a combined reference, prepare the non-text component normally and record
the text component as typeface reuse, with the exact string and matching glyph
IDs. A text component brief is a reuse/layout brief, not permission to generate
new letter or number primitives. This also applies to existing Pending briefs.
If a required character is missing, report the missing glyph and leave that
part unresolved rather than inventing a substitute.

This rule concerns actual characters, not abstract text-line marks or objects
associated with writing or numbers (such as a pen or calculator).
