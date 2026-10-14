---
name: icon-fill
description: Create or revise Pictographic Fill (solid) variants of existing line-art icons - one currentColor shape where every enclosed surface is solid, openings that mean something stay open, and inner lines become knocked-out negative lines inside an unbroken silhouette. Uses icon_set/scripts/icon_variant.py (faces, fill, preview). Use for solid or filled icon versions, the Fill tab of the Experiment gallery, or fill-specific review feedback across sub, solo, container and combination icons. Hand-authored; edit this file directly.
---

# /icon-fill — solid variants

Use the user's requested icons, collection and output location. Resolve repository paths from the
directory containing `icon_set/`. Run Python with `/opt/homebrew/bin/python3` (it has svgpathtools,
shapely and cairosvg).

## What a Fill icon is

The Fill tab of Experiment (`experiment.html?type=fill`, snapshot in
`icon_set/assets/experiments/experiment-fill.json`) sets the style:

- One `<path fill-rule="evenodd">` on a root with `fill="currentColor"` and no stroke, on the source's
  native canvas (`viewBox` unchanged). It takes the text colour, so it works on light and dark.
- The silhouette is the source drawing's outer edge: the strokes outlined at their own width with
  round caps and joins, plus every enclosed surface filled solid.
- Lines drawn inside the silhouette (a flap, a seam, a screen edge, text lines, a lamp in a body) become
  **knockouts**: negative lines as wide as the stroke, stopping one stroke width short of the edge so
  the silhouette stays whole. They carry the inner detail; without them a solid blob loses its meaning.
- Openings that are part of what the object is stay open: a handle loop, the space between legs or
  wheels, a ring's hole, a window you look through. Openings only drawn because it is a line icon close.
- Some icons do not take a fill: pure line symbols (arrows, chevrons, plus, text, italic, waveforms,
  dashed diagrams) have no surface. Record them as `fill_applicable: false` and keep the line art as
  the result rather than inventing a shape. About a quarter of the 500-sample set was not applicable.

## Workflow

1. **Get the source.** Use the SVG the user names, or the icon's current artwork from production
   (`<base>/api/icon-artwork/svg?icon=<family>/<icon_id>`, base from
   `icon_set.scripts.work_queue.default_base_url()`). Never edit the source or its Python model; a fill
   is a variant, not a redraw, and does not change any review status.
2. **Look at it.** Render it at native size and 4x. Name the object, its surfaces, its real openings,
   and the inner lines that carry meaning. Decide whether a fill applies at all.
3. **Map the faces.**
   `python3 icon_set/scripts/icon_variant.py faces SRC.svg --png FACES.png` lists the paths and every
   enclosed face (F1 = largest) and draws them numbered. Read the PNG.
4. **Build.**
   `python3 icon_set/scripts/icon_variant.py fill SRC.svg OUT.svg --open F3,F5 [--keep id] [--region D]`
   - `--open` the faces that are real openings; every other face fills.
   - Inner strokes become knockouts automatically. `--keep` a path whose cut means nothing and only
     chops the shape (a construction seam, a shading hint that becomes noise when negative).
   - An open silhouette (a cup drawn as a U, a figure missing its base) has no face to fill: add the
     closing area with `--region "M.. Z"` along the natural endpoints.
   - `--gap` / `--rim` change the knockout width and the solid kept at the edge; leave them at the
     stroke width unless a knockout is crowded.
5. **Check.** `python3 icon_set/scripts/icon_variant.py preview SHEET.png SRC.svg OUT.svg` shows source
   and result at native size and 4x on light and dark. Look at it, at 48 px especially:
   - The subject still reads; inner meaning (screen vs body, lid vs jar) survives as knockouts.
   - No knockout or opening is thinner than ~3 units (the script warns) and no sliver or speck is left
     where a knockout meets another line or a cap; fix with `--keep`, `--open` or a `--region`.
   - Real openings are open, nothing that should be solid shows the background.
   - The silhouette matches the source: no dents or bumps the line icon did not have.
   Iterate on the flags; hand-edit geometry only for a closure or region, never the source strokes.
6. **Record and deliver.** Save each icon in its own folder (default
   `icon_set/work/fill-variants/<icon_id>/`): `source.svg`, `fill.svg`, `preview.png` and
   `decisions.json` with the source key, source sha256, canvas, `fill_applicable`, open faces, kept
   paths, regions and a one-line reason for each. Report what you made and what each decision was.

## Experiment gallery

Only when the user asks to show results on Experiment: append rows
`{key, number, name, canvas_size, fill_applicable, outline, result}` (SVG text inline, `key` unique) to
`icon_set/assets/experiments/experiment-fill.json`, then run
`python3 -m icon_set.scripts.experiment_gallery` from the repo root to restage `published/gallery/`. Pushing the gallery
to production is a separate step (R2 `site/gallery/`); ask before doing it.

Distinguish the visual checks you ran from production validation: a fill variant is an experiment and
carries no approval.
