---
name: icon-duotone
description: Create or revise Pictographic Duotone variants of existing line-art icons - the unchanged black strokes over one accent colour (SKY_BLUE by default) that fills the object's main surfaces, with openings and small details left clear. Uses icon_set/scripts/icon_variant.py (faces, duotone, preview). Use for two-tone icon versions, the Duotone tab of the Experiment gallery, or duotone-specific review feedback across sub, solo, container and combination icons. For full multi-colour icons use $icon-color. Generated from .claude/skills/icon-duotone/SKILL.md by icon_set/scripts/generate_skills.py; edit the source, not this copy.
---

# $icon-duotone — black line plus one accent

Use the user's requested icons, collection, accent and output location. Resolve repository paths
from the directory containing `icon_set/`. Run Python with `/opt/homebrew/bin/python3`.

## What a Duotone icon is

The Duotone tab of Experiment (`experiment.html?type=duotone`, snapshot in
`icon_set/assets/experiments/experiment-duotone.json`) sets the style:

- Two colours only: the source strokes in black `#000000`, unchanged in geometry, width, caps and
  joins, and one accent fill, `SKY_BLUE #7EC8E3` from `icon_set/skills/icon-design/color-theme.json`
  unless the user names another. No gradients, no opacity steps, no third colour.
- The accent fills sit **behind** the strokes (fills first, strokes last), so the black line is never
  covered and the fill's edge hides under it.
- The accent goes on the object's main surfaces - the body, the screen, the shade, the liquid - the
  part that makes the shape read as a thing. Openings stay clear (handle loops, gaps between legs,
  holes), and so do faces too small to read at native size (under ~3 units across). When every face
  is filled the icon turns into a colouring-book; pick what carries the subject.
- Line-only symbols with no surface (arrows, text, waves) may stay plain black. A minimal accent region
  inside the subject (water in a glass, a flame core) is allowed when it clarifies the meaning.

## Workflow

1. **Get the source.** Use the SVG the user names, or the icon's current artwork from production
   (`<base>/api/icon-artwork/svg?icon=<family>/<icon_id>`, base from
   `icon_set.scripts.work_queue.default_base_url()`). Never edit the source or its model; a duotone is
   a variant and changes no review status.
2. **Look at it** at native size and 4x. Name the object and decide which surfaces carry it.
3. **Map the faces.**
   `python3 icon_set/scripts/icon_variant.py faces SRC.svg --png FACES.png` lists every enclosed face
   (F1 = largest) and draws them numbered. Read the PNG.
4. **Build.**
   `python3 icon_set/scripts/icon_variant.py duotone SRC.svg OUT.svg --face F1,F3 [--region D] [--closure D] [--color HEX]`
   - `--face` the surfaces to paint.
   - An open silhouette with nothing to fill: add the accent area with `--region "M.. Z"`, and if the
     shape then needs a black edge, a `--closure "M.. L.."` stroke between the natural endpoints.
5. **Check.** `python3 icon_set/scripts/icon_variant.py preview SHEET.png SRC.svg OUT.svg` shows source
   and result at native size and 4x, on light and dark. At 48 px the accent must read as one surface,
   not confetti; openings stay clear; no accent pokes outside the black edge; the black line is intact.
6. **Record and deliver.** Save each icon in its own folder (default
   `icon_set/work/duotone-variants/<icon_id>/`): `source.svg`, `duotone.svg`, `preview.png` and
   `decisions.json` with the source key, source sha256, canvas, accent, painted faces, regions,
   closures and a one-line reason each. Report what you made.

## Experiment gallery

Only when the user asks to show results on Experiment: append rows
`{key, number, name, canvas_size, outline, result}` (SVG text inline, `key` unique) to
`icon_set/assets/experiments/experiment-duotone.json`, then run
`python3 -m icon_set.scripts.experiment_gallery` from the repo root to restage `published/gallery/`. Pushing the gallery
to production is a separate step (R2 `site/gallery/`); ask before doing it.

A duotone variant is an experiment and carries no approval.
