# Intake

Two modes; both end in an `Icon` subclass on the chosen profile. Neither licenses copying a drawing in.

**Brief only.** Use the name and description to identify subject, essential parts, arrangement. No fabricated source, detector run or reference name. Record `category`, `aliases`, `keywords`. If you made a judgment call on a thin brief, say so.

**Brief plus references.** Inspect only what is in scope; record what you took from each.
- Raster: read silhouette, part count, openings, arrangement. Do not invent element ids for pixel shapes.
- SVG: **render it and look**. Never read its coordinates and fit primitives to them; that copies exporter fragmentation and the wrong stroke ratio. One file: `cairosvg`. A folder: `python3 icon_set/scripts/prepare_references.py <folder> --out <work> [--native 48|32]`.
- Unreadable: say so. Never substitute or claim a review you did not do.

A reference is evidence about the subject. It is not a grid, a stroke weight, permission to add features, permission to change subject, or authority over the brief. Its extraction defects are defects.

**Batch order: look, measure, decide, draw, compare.**
```bash
python3 icon_set/scripts/reconstruct.py trace <svg folder>       # bounds, aspect, keyshape hint, rules, marks, corner radius per icon
python3 icon_set/scripts/reconstruct.py compare --family <fam>   # fidelity + iou vs source, worst first
```
Recompose the trace's proportions on the integer grid; do not transcribe fractional numbers, and open up gaps the source packs tighter than the profile minimum. A reconstruction at fidelity 0.55 is a different icon. Check the native-size render; it decides what to drop.

**Lucide** (`icon_set/references/lucide/`, `original/` and `atomic-debug/`) is the default construction reference in both modes, after the human reference for people. It teaches contour flow, corner turns, spacing. Not coordinates: Lucide is 2/24, this system is 4/32, so detail that separates there closes here; Lucide is fractional, this is integer.
```bash
python3 icon_set/scripts/lucide_reference.py search 'cloud' --limit 6
python3 icon_set/scripts/lucide_reference.py inspect cloud --profile SOLO48   # bounds, aspect, keyshape hint
python3 icon_set/scripts/lucide_reference.py atoms cloud                       # segment kinds and d
python3 icon_set/scripts/lucide_reference.py search 'square' --kind arc/quarter-circle
```
`atoms` is an inventory, not a part count; your contours follow how the icon should paint. Inspect only what answers a real question. Record the references used and the principle taken, or say none matched.
