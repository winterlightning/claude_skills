# Complete-original policy for the whole sub library

Latest user correction, 2026-09-23: every newly authored sub output uses a
32×32 canvas, `viewBox="0 0 32 32"`, and 4px strokes on every element. This
supersedes the former larger-canvas permission and the compact 2px inner-stroke
approach for new work. Existing exceptions are historical artwork, not a
pattern to copy. Use the strict gate in `icon_set/scripts/fix_icon_sub.py check`
for repairs. A passing geometry check does not replace visual source review.

User direction, 2026-09-19: apply this to every existing sub concept and all
selected side/container variants, not just the latest eight repairs.

Preserve the original drawing and meaning. Do not add or remove parts. Retain
outline frames, badges, internal symbols, text, repeated marks, their counts,
direction, relative placement and characteristic proportions. Do not replace a
complete composition with a generic symbol that merely shares its name.

Fit the defining parts and relationships at 32×32 with 4px strokes. Simplify
only details that do not carry the source's identity. Do not squeeze strokes or
openings below clearance, distort a source's aspect ratio, enlarge the canvas,
or thin strokes to force completion. If the complete composition cannot pass,
record the specific blocker and keep the original as review evidence. Do not
count that source as a generated SUB32 icon.

Reopen the actual original SVG, not the last generated variant. Inventory its
parts, compare the complete original and proposed drawing at enlarged and native
sizes, and inspect centerlines and both light/dark previews. Shared glyph reuse
must preserve the source character, case and arrangement. Preserve earlier
variants and record their source UUIDs and replacement links.

Track geometry validation and visual source fidelity separately. A geometry pass
is not evidence of source fidelity. Missing references remain explicitly
unverified. Existing geometry-pass totals must never be described as a completed
library-wide source audit. Preserve human feedback and editorial metadata.

Historical expanded models are not plain SUB32 output and must not be selected
as fixes for strict 32×32 requests. Validate the actual placement and containing
canvas separately when reviewing older combinations.
