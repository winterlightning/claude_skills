# Text and number icons

Use the existing **typeface** glyphs for icons representing letters, words,
abbreviations, digits, or numbers, including text within or beside another icon.
Do not invent, trace, or redraw replacement letter/number geometry as a new
solo or sub icon.

Look up the exact characters in `icon_set/typeface/glyphs.json` and reuse their
existing `icon_id` and paths. Use the `preferred` glyph unless a specific variant
is requested. Preserve case, readable content, and meaningful arrangement.
Keep the typeface's natural proportions and baseline/body metrics; do not force
glyphs into an icon keyshape or stretch their width independently.

For a combined reference, prepare the non-text component normally and record
the text component as typeface reuse, with the exact string and matching glyph
IDs. A text component brief is a reuse/layout brief, not permission to generate
new letter or number primitives. This also applies to existing Pending briefs.
If a required character is missing, report the missing glyph and leave that
part unresolved rather than inventing a substitute.

This rule concerns actual characters, not abstract text-line marks or objects
associated with writing or numbers (such as a pen or calculator).
