---
name: icon-animate
description: Create or revise animated Pictographic icons - a self-contained SVG where the existing line drawing acts out what it means in one short looping motion (a bell rings, a heart beats, an arrow drops into a tray), with CSS keyframes or SMIL, a reduced-motion fallback, and every frame inside the canvas. Uses icon_set/scripts/animation_frames.py to check the motion frame by frame. Use for animated icons, motion studies, the Animation tab of the Experiment gallery, or animation review feedback across solo, sub, container and combination icons. Hand-authored; edit this file directly.
---

# /icon-animate — meaning in motion

Use the user's requested icons, motion ideas and output location. Resolve repository paths from the
directory containing `icon_set/`. Run Python with `/opt/homebrew/bin/python3`.

## What an animated icon is

The Animation tab of Experiment (`experiment.html?type=animation`, snapshot in
`icon_set/assets/experiments/experiment-animation.json`, 23 samples) sets the style. Read two or three
of its `result` SVGs before starting; each row also has a one-sentence `motion`.

- **One idea that is the meaning.** The motion acts out what the icon says: the bell rings from its
  knob, the trash lid tips open and snaps shut, the download arrow drops into the tray, the sync arrows
  spin one turn, wifi arcs light up from the source. Motion that is only decoration (wobbling, pulsing
  everything) is wrong. In a combination the sub usually carries the action and the main answers.
- **Same drawing.** The source paths stay as they are; group them (`<g>`) by moving part and animate the
  groups. The rest pose (time 0 and the end of the loop) is exactly the static icon.
- **Short loop with a rest.** 1.8 to 3 s, `infinite`. Act, then hold still for a beat so it reads as
  an event, not a vibration. Physical timing: ease-in on the wind-up, overshoot and decay on a swing,
  a small squash on impact, the follower lagging the leader (clapper after the bell).
- **Inside the canvas, always.** Rotations pivot on the real hinge (`transform-origin` in canvas
  units, or `transform-box: fill-box` with `transform-origin: center` for a spin); scale down slightly
  while spinning if the corners would leave the canvas. Something that exits must re-enter from the
  other side or reappear inside the frame.
- **Self-contained SVG.** One `<style>` with class names prefixed per icon (`a07-lid`, `@keyframes
  a07-tip`) so several icons on one page never clash; CSS transforms, opacity and
  `stroke-dasharray`/`stroke-dashoffset` (redraw a stroke with `pathLength="1"`); SMIL `<animate
  attributeName="d">` only for a path morph (a flag rippling) with the same command structure in every
  value. No script, no external file.
- **Reduced motion.** End the style with
  `@media (prefers-reduced-motion: reduce) { .aNN { animation: none !important; } }` and give every
  animated element the `aNN` class, so the static icon shows. For SMIL, keep the rest pose as the
  path's own `d`.
- Stroke colour stays as the source (`currentColor` or black); colour flashes only where they mean
  something (a spark, a status).

## Workflow

1. **Get the source** the user names, or the icon's current artwork from production
   (`<base>/api/icon-artwork/svg?icon=<family>/<icon_id>`; for a side or container combination the
   built combined SVG). Never edit the source or its model; the animation is a variant.
2. **Look and write the motion.** Name the object and what it does, then write the motion in one
   sentence before coding, like the samples' `motion` field. Identify the moving parts, their pivots
   and what stays still.
3. **Build** `<icon_id>-animated.svg`: regroup the source paths by moving part (geometry untouched),
   add the style and keyframes.
4. **Check frames.** `python3 icon_set/scripts/animation_frames.py OUT.svg FRAMES.png --frames 12`
   freezes the loop at even times and shows it at 96 px and at native size, each frame bordered by the
   canvas edge. Read the strip:
   - frame 0 equals the static icon; the loop ends where it starts (no jump);
   - nothing crosses the red border unless it is meant to exit and come back;
   - pivots look physical (a lid hinges on its hinge, a hand turns on the clock centre);
   - at native size the action still reads;
   - the script warns if `prefers-reduced-motion` is missing.
   Frames show poses, not timing: when the user can watch, also open the SVG in the browser to judge
   speed and easing.
5. **Record and deliver.** Save each icon in its own folder (default
   `icon_set/work/animation-variants/<icon_id>/`): `source.svg`, `<icon_id>-animated.svg`,
   `frames.png` and `notes.json` with the source key, source sha256, canvas, the motion sentence,
   duration and moving parts. Report the motion and anything you could not make read.

## Experiment gallery

Only when the user asks to show results on Experiment: append rows
`{key, number, name, icon_id, source, canvas_size, motion, outline, result}` (SVG text inline, `key`
unique) to `icon_set/assets/experiments/experiment-animation.json`, then run
`python3 -m icon_set.scripts.experiment_gallery` from the repo root to restage `published/gallery/`. Pushing the gallery
to production is a separate step (R2 `site/gallery/`); ask before doing it.

An animated icon is an experiment and carries no approval.
