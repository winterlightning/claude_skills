---
name: icon-twotone
description: Create or revise Pictographic Twotone variants of existing line-art icons - the original strokes, unchanged in geometry and width and with nothing filled, sorted into two tones the way hugeicons Twotone does: the outline of the object stays in the full line colour and its sub elements (markings, attachments, a second object on it) take the same colour at 40 % opacity. A path shared by the outline and a sub element is cut at the joint so each piece gets its tone. Uses icon_set/scripts/icon_variant.py (strokes, twotone, preview). Use for twotone icon versions, the Twotone tab of the Experiment gallery, or twotone-specific review feedback across sub, solo, container and combination icons. Not Duotone (that fills surfaces under black strokes) and not Color (full palette); for those use /icon-duotone or /icon-color. Hand-authored; edit this file directly.
---

# /icon-twotone — one drawing, two stroke tones

Use the user's requested icons, collection, accent and output location. Resolve repository paths
from the directory containing `icon_set/`. Run Python with `/opt/homebrew/bin/python3`.

## What a Twotone icon is

The Twotone tab of Experiment (`experiment.html?type=twotone`, snapshot in
`icon_set/assets/experiments/experiment-twotone.json`) sets the style:

- **The original, recoloured.** Every stroke of the source stays: geometry, stroke width, caps, joins
  and canvas (`viewBox`) are untouched and nothing is filled. The only change is the stroke colour of
  some paths. A twotone is the line icon with its strokes sorted into two tones.
- **Two tones of one colour (the hugeicons pattern).** Primary strokes keep `currentColor` at full
  strength (black on light, white on dark). Secondary strokes are the same `currentColor` at 40 %
  opacity, applied to the secondary group as a whole so crossings inside it do not double up. No second
  hue unless the user asks for one (`--color HEX`, e.g. `SKY_BLUE #7EC8E3`).
- **Outline primary, sub elements secondary.** The strokes that draw the object's outline, its body
  and the structural lines that belong to it, stay primary, always. Secondary is one nameable sub
  element that sits on or beside the object:
  - *markings on it* - eyes and a nose on a face, text lines on a page, calendar dots, a keyhole, the
    bars inside a cart, a wing fold drawn inside a bird;
  - *attachments and accessories* - sun rays, a motion trail, flash dots, a bell's knob, a magnifier's
    handle, a lock's shackle, a gift's ribbon, steam over a cup;
  - *a second object on or in it* - the rider on a scooter, a shoe on a rack, the plant in a pot, a
    bolt inside a frame, the lever and keyhole on a door plate, a picture inside a frame.
  The outline is never the secondary group, even when the sub element carries the meaning (a check in a
  shield: shield primary, check secondary). Both groups are whole things.
- **One body, one tone.** A living figure or a single object is never split between tones: limbs,
  legs, wings, a lid, a handle drawn as part of the body stay with the body. A rider's torso in the
  second tone with its legs in the line colour is wrong, and so is a bird whose leg changes colour.
- **Structure stays primary.** A line that runs through the outline from edge to edge and divides it
  (a brow band on a skull, a shelf, a screen edge, a bell's rim) is part of how the object is drawn.
  Colouring it leaves a stray line floating across the subject. Secondary parts sit inside the
  outline or stick out of it.
- **One named part, not the leftovers.** The secondary group is the features, the rays, the trail,
  the box: one thing you can name in the reason. Never "every stroke that is not the outline". It
  may be small as long as it reads at native size (a knob 8 units long is fine); a single 2 unit dot
  on its own is not.
- **Two checks before building.** Cover the secondary strokes: the primary strokes alone must still
  look like the complete object. Cover the primary strokes: the secondary strokes alone must look
  like the named part. If either fails, change the split.
- **When two parts share a path, cut it at the joint.** A path that draws strokes from both groups
  (a scooter frame line that continues into the rider's leg, a box edge that runs on into a chassis)
  is cut at the vertex where one part ends and the other begins (`--split ID@X,Y`), and each piece
  takes its own tone. Watch for a closed sub element that sits on the outline: one of its edges is
  often the outline itself (a helmet crest whose underside is the helmet's crown, a lid whose bottom
  is the box's top). Cut it at both ends of that edge and keep the edge primary; the outline must stay
  complete in the line colour. Round caps make the cut invisible: the geometry on screen is unchanged. Read the
  `points` line of the stroke map to find the vertex; never cut mid-stroke unless the joint really is
  there, and never move, add or redraw a stroke.
- **Whole strokes otherwise.** Pictographic paths are named by part (`head`, `body-left`, `pump`), so
  the split follows the ids, but the id is a hint, not proof: read the stroke map to see what each
  stroke really draws. Production artwork may instead group shapes under `<g id>` with
  circles and filled dots inside; the helper names those `group.1`, `group.2` ... and a group id
  selects all of them, so a part can still be picked stroke by stroke (`scooter.4`). A filled dot
  dims with its group (or takes the second colour as its fill).
- **Primary draws last.** The result holds two groups, `data-tone="secondary"` first and
  `data-tone="primary"` after, so every junction between the tones is owned by the line colour and the
  light stroke tucks under it. Each stroke keeps its id; a cut piece is `IDa`, `IDb` with `data-part`.
- **Not every icon takes a twotone.** One stroke with no part to separate (a ring, a plain arrow, a
  chevron, a letter, a single wave) has no second group. Record it as `twotone_applicable: false` and
  keep the line art as the result rather than dimming the whole icon.
- **Combinations.** A container pair splits container (primary) versus content (secondary); a side
  pair splits main (primary) versus sub (secondary). The same rule as everywhere: the outline that
  hosts stays in the line colour, what sits on it is the second tone.

## Workflow

1. **Get the source.** Use the SVG the user names, or the icon's current artwork from production
   (`<base>/api/icon-artwork/svg?icon=<family>/<icon_id>`, base from
   `icon_set.scripts.work_queue.default_base_url()`). Never edit the source or its model; a twotone is
   a variant and changes no review status.
2. **Look at it** at native size and 4x. Name the subject, then name the one sub element (markings,
   attachment, second object) and check that the outline keeps every limb and every structural line.
   Find any stroke that is shared by both and the vertex where it should be cut. Write the one-line
   reason before building.
3. **Map the strokes.**
   `python3 icon_set/scripts/icon_variant.py strokes SRC.svg --png STROKES.png [--split ID@X,Y]` lists
   every stroke (id, open, closed or filled, bounding box, length, the faces it bounds and its corner
   `points`) and draws the icon with each stroke in its own colour, labelled by id. Read the PNG; this
   is where a path that mixes both groups shows up. Re-run with `--split` to see the pieces.
4. **Build.**
   `python3 icon_set/scripts/icon_variant.py twotone SRC.svg OUT.svg --secondary shackle,keyhole [--split frame@20,26] [--color HEX]`
   - `--secondary` the stroke or group ids in the second tone; every other stroke stays primary.
   - `--split ID@X,Y` cuts a shared stroke at that vertex first; the pieces are `IDa`, `IDb` ...
   - `--dim` (default 0.4) sets the second tone's opacity; `--color` a second hue instead, only when asked.
   The result keeps the source root (`stroke="currentColor"`, width, caps, joins, title) and holds the
   two tone groups.
5. **Check.** `python3 icon_set/scripts/icon_variant.py preview SHEET.png SRC.svg OUT.svg` shows source
   and result at native size and 4x, on light and dark. At 48 px (32 for subs) the two tones must read
   as an object and one named sub element: the outline is complete in the primary strokes, no body or
   limb changes tone, no structural line floats in the light tone, junctions are owned by the line
   colour, and the light tone is still visible on both backgrounds. If the split does not read, change
   the groups or the cut; never the drawing.
6. **Record and deliver.** Save each icon in its own folder (default
   `icon_set/work/twotone-variants/<icon_id>/`): `source.svg`, `twotone.svg`, `preview.png` and
   `decisions.json` with the source key, source sha256, canvas, the tone (`dim` opacity or a colour),
   `twotone_applicable`, the primary ids, the secondary ids, any cuts, and the one-line reason. Report what you made and the reason for each split.

## Experiment gallery

Only when the user asks to show results on Experiment: append rows
`{key, number, name, canvas_size, twotone_applicable, outline, result}` (SVG text inline, `key` unique)
to `icon_set/assets/experiments/experiment-twotone.json`, then run
`python3 -m icon_set.scripts.experiment_gallery` from the repo root to restage `published/gallery/`.
Pushing the gallery to production is a separate step (R2 `site/gallery/`); ask before doing it.

A twotone variant is an experiment and carries no approval.
