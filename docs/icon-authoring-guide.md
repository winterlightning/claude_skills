# Icon authoring techniques

This is the practical drawing guide. It intentionally does not repeat profile
numbers, validation commands, or delivery rules.

- Start with the shared [icon pipeline](icon-pipeline.md).
- Treat [icon-rules.md](icon-rules.md) as the written visual specification.
- Read the generated [profile reference](generated/icon-profiles.md) for exact
  canvas, stroke, center, keyshape, distinct-part distance, and container-slot values.
- Use [atomic-shapes.md](atomic-shapes.md) to choose registered building blocks.
- Use [scripts.md](scripts.md) to understand a command before running it.

The machine authority for profile geometry is
[`core/icon_profiles.json`](../core/icon_profiles.json). Do not copy those values
into another guide; update that source and regenerate its mirrors instead.

## Reduce before composing

Describe the subject in one short sentence, then keep only:

1. its smallest recognizable silhouette;
2. one to three identity-bearing features;
3. no secondary detail that disappears at the selected profile's ship size.

Sub icons need an especially strict edit: prefer one silhouette and no more
than two internal identity features.

## Choose quality first, then reuse or extend

Decide the clearest, most natural silhouette before treating the current catalog
as a menu. Build the editable JSON from registered atoms, not flattened output
paths, but reuse a current atom only when it produces that intended form without
compromise. If reuse makes the icon stiff, generic, distorted, fragmented, or
less recognizable, create and register a new generic parametric atom immediately.
One initial icon is sufficient; do not make a worse icon to avoid registry work.

When two approaches are genuinely close, render both at true ship size and keep
the visually stronger result. Existing-atom reuse is only a tie-breaker. Place,
resize, rotate, or reflect complete instances after making that decision.

Good compositions usually have:

- one dominant mass or outline;
- a clear symmetry or intentional asymmetry;
- a small number of readable internal relationships;
- negative spaces that survive true-size review.

Choose the semantic keyshape before tuning the drawing. The complete painted
artwork must reach the selected keyshape's cardinals or edges without crossing
its boundary. Do not switch keyshapes merely to make a weak composition pass.

## Join and spacing technique

- Make connected parts meet cleanly and trim redundant segments.
- Keep distinct parts separated according to the Distance Rule in
  [icon-rules.md](icon-rules.md).
- When an overlap needs visual separation, cut the underlying path rather than
  stacking an opaque patch over it.
- Prefer enlarging an opening, rebalancing the composition, or removing a whole
  part over squeezing a gap until it disappears.
- Keep line directions on the allowed angular grid and use registered arcs or
  quadratic curves instead of freehand cubic paths.

Inspect the actual painted result, not just centerlines. A mathematically even
layout can still need a small optical correction when one side carries more
visual weight.

## Containers

A container is authored on its own profile and declares an accepted sub-icon
keyshape for preview compatibility. Keep the full centered 32×32 slot free of
container paint; the accepted keyshape does not reduce this clearance.
Review both states:

- the empty container, which is the shipping artwork;
- a filled preview with an accepted sub icon, which is review evidence only.

Do not scale a flattened normal icon into the slot. Compose the sub icon on the
sub profile and place its design source into the declared container slot.

## Composite badges

A badge is a semantic modifier inside a normal icon, not a standalone sub-icon
profile. Use the badge geometry defined by [icon-rules.md](icon-rules.md), and
respect the corner semantics documented there. Rework the main symbol before
moving a badge to a semantically incorrect corner.

## Runtime axes

The renderer may expose color, ship stroke, keyshape, and corner style. Treat
these as controlled parameters of one composition, not permission to improvise
separate drawings. Every variant must preserve recognition, spacing semantics,
and optical centering.

## Review at two scales

Always inspect both the editable design canvas and the profile's true ship
size. At design scale, look for geometry, grid, joins, protected regions, and
keyfit. At ship size, look for clipping, crowded negative space, imbalance,
and lost recognition.

The pipeline's automated gates establish structural compliance. Human review
still decides whether the icon is legible and visually convincing.

## Migration note

Legacy canvases, old keyfit ladders, common-fit exports, and `-fit.svg`
artifacts are historical inputs, not current authority. Migrate their meaning
into editable atomic JSON, select an explicit profile, and regenerate outputs
through the shared pipeline.
