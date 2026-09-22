# Text and number icons

Typeface means alphabet letters, digits, and keyboard punctuation (including
curly quote and degree variants). Currency symbols are **icons, not typeface**,
even `$` on a keyboard. This includes dollar, euro, pound, yen/yuan, bitcoin,
rupee, won, hryvnia, kip and lira. Specialist symbols such as prescription and
subset-or-equal are also icons. Route them by use: solo when standalone, sub
as a modifier, or symbol as container content. Currency inside a combination
remains an icon component, not a typeface reuse brief. Existing reusable symbol
paths are preserved separately in `icon_set/typeface/symbol-glyphs.json`; their
presence does not classify them as text.

Use the existing **typeface** glyphs for icons representing letters, words,
abbreviations, digits, or numbers, including text within or beside another icon.
Do not invent, trace, or redraw replacement letter/number geometry as a new
solo or sub icon.

Look up the exact characters in `icon_set/typeface/glyphs.json` and reuse their
existing `icon_id` and paths. Use the `preferred` glyph unless a specific variant
is requested. Preserve case, readable content, and meaningful arrangement.
Use only the fixed-size typeface: a 6 × 20 centerline box with stroke 4,
within a 10 × 24 canvas. Width and height describe centerlines separately
from ink. Do not generate the retired 12–32 size range or scale strokes.
Read the stored actual `centerline_width`, `centerline_height`, `ink_width`,
`ink_height`, `ink_left` and `ink_top`; regular glyphs use a 10 × 24 preview box.
Special cases i, l, !, apostrophe, colon and vertical bar keep their straight
centerlines and fit height 20. Period and horizontal marks stay flat within
that 20-unit band, with stroke 4; their actual ink height is 4. Hyphen retains
its original 16-unit centerline width and underscore retains 28, giving
20 × 24 and 32 × 24 canvases respectively. Do not enlarge a dot or thicken
flat strokes to make them fill the vertical band.

Generate the single-size exports with `python3 -m icon_set typeface-sizes`.
They are under `gallery/typeface/sizes/24/<icon_id>.svg`; the bundle is
`typeface-6x20.zip`. Normal gallery builds export the same size.

For a combined reference, prepare the non-text component normally and record
the text component as typeface reuse, with the exact string and matching glyph
IDs. A text component brief is a reuse/layout brief, not permission to generate
new letter or number primitives. This also applies to existing Pending briefs.
If a required character is missing, report the missing glyph and leave that
part unresolved rather than inventing a substitute.

This rule concerns actual characters, not abstract text-line marks or objects
associated with writing or numbers (such as a pen or calculator).
