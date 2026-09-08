# Authoring technique

The practical drawing guide. It deliberately does not repeat profile numbers or
validation commands — those are in the contracts and in
[validation.md](validation.md).

## Default aesthetic: Lucide geometry, smoothness, appropriate balance

Use the local Lucide bundle as the first construction reference when designing
or repairing an icon. Inspect the original silhouette and the relevant
atomic-debug geometry: identify its main primitives, repeated radii, symmetry
axes and curve junctions. An exact subject match is useful but not required;
a related handle, enclosure, garment or tool may teach the needed construction.
If no useful match exists, say so and apply the same geometric principles.
Re-author the drawing for the selected profile; do not copy Lucide's coordinates
or stroke weight, and do not replace a user-supplied subject with another one.

Prefer mirrored geometry and visual balance only where they preserve the icon's
meaning, recognizability, and natural shape. These are optional design choices,
not requirements: skip mirroring or forced balance when they would distort the
subject. A palm tree, for example, may retain uneven fronds and a leaning trunk;
mirror only the parts where it helps the drawing read clearly.

Before placing individual points:

- Choose the symmetry axis when the subject supports one. Derive one side from
  the other, e.g. `x_right = 2 * axis_x - x_left`; use shared parameters for
  paired radii, heights and spacing. Check symmetry of negative space too.
- For rotated symmetric parts, reason about their local axis while keeping the
  final authored points on the integer grid. Perspective, motion and naturally
  asymmetric subjects may need deliberate asymmetry; explain that choice.
- Prefer a small number of coherent straight runs and arcs. Use consistent
  radii for equivalent features and matching tangents where curves flow into
  each other or into straight runs. Retain purposeful corners; do not round
  every feature indiscriminately or approximate a smooth curve with many kinks.
- Repair clearance by moving paired features together when appropriate, keeping
  the intended symmetry and smooth flow. Review internal-spacing advisories
  instead of accepting pinched shoulders or jaws solely because release gates
  pass. Existing hole exceptions and validation thresholds still apply.

At native size in light and dark themes, inspect the contour flow, paired
proportions, visual centre, and clear space around curves. A drawing that passes
numerically but looks lopsided or kinked needs another geometry pass. In the
handoff, name the useful Lucide reference and construction principle, and note
any intentional asymmetry; do not claim a reference you did not inspect.

## Reduce before composing

Write the subject as one short sentence. Then keep only:

1. the smallest recognizable silhouette;
2. the features that carry its identity;
3. nothing that disappears at native size.

"Native size" is the family's canvas with a 4-pixel stroke: 32 pixels for
`sub`, 48 for `solo`, 64 for `container`. At 32 that is eight stroke widths
across the whole icon and a third level of detail does not survive; at 48 it is
twelve, which buys one more feature and no more; at 64 it is sixteen, and all
sixteen are yours — a container reserves nothing, so interior furniture is not
only allowed but usually what makes the subject read.

## Choose the keyshape first, then design backwards

This is the one habit that makes the difference. Do not draw and then hope it
fits a keyshape.

1. Choose the keyshape from the subject's natural proportions.
2. Write down its four extreme coordinates.
3. Place geometry so it reaches exactly those numbers.

Worked example — `heart`, `sub` family (`SUB32`), `HRECT_XL`:

```
visible bounds     (0, 2) - (32, 30)
centerline bounds  (2, 4) - (30, 28)     <- the numbers you author to
```

So the heart's leftmost point is `x = 2`, its rightmost `x = 30`, its crests
`y = 4`, its tip `y = 28`. Everything else is designed between those. See
[keyshape-fitting.md](keyshape-fitting.md) for how to hit them.

## Make joins tangent-continuous

Where two curves meet, match their tangents. Where a curve meets a line, aim the
line along the curve's tangent. A kink in the middle of a smooth contour is the
single most common reason an otherwise-correct icon looks wrong.

The heart is the worked example again. Its lobe and its shoulder are both
circles centred on `y = 12`, so both are vertical where they meet at the widest
point and there is no corner at all. Its shoulder leaves at 36.9 degrees and its
side runs at 38.7, which is close enough to read as continuous. Taking the side
as a straight line straight off the widest point instead puts a 41-degree kink
exactly where the eye reads the shoulder, and the icon flattens into a V with
two horns. Same bounds, same keyshape, same validator verdict — and visibly
worse.

Two tools for this:

- Put a shared axis extreme at the junction. Two shapes that both reach a
  horizontal extreme there are both horizontal there.
- Give a straight run the same angle as the tangent it leaves.

## Spacing

Distinct parts need the profile's minimum ink clearance: 2 / 2 / 2 units for
SUB32 / SOLO48 / CONTAINER64, which is 6 / 6 / 6 between equal-stroke
centerlines.

- **Straight parts may sit exactly on the minimum.** The measurement is exact.
- **Curved parts need real margin.** The spacing engine bounds a curve's
  flattening error, so a curve exactly on the threshold cannot be certified and
  comes back `review`, which is not a pass. `target` was first drawn with radii
  14 and 7 — exactly 7 apart — and measured 6.99987. Radius 6 is correct. The
  same rule caught `film-frame` at 48: its perforations sat exactly 8 from the
  frame's rails, but the rails belong to one contour with curved corners, so
  the pair is curved and 8 could not be certified. They sit at 9 now.
- **An intentional contact is declared, not ignored:**
  `icon.relate("connect", "shaft", "head")`. That excuses **that pair only**.

## When a gap is too small, give it room

Work down this ladder and stop at the first rung that keeps the icon
recognizable:

1. **Enlarge the opening.** Grow the enclosing shape, lengthen or reangle the
   parts that bound it, or move them apart.
2. **Rebalance.** Scale the dominant part down and the crowded detail up, then
   recentre. Redistribute space; never steal it.
3. **Remove the part.** Delete the whole non-essential element and record the
   omission. Two clean parts beat four crowded ones.

Never squeeze parts together until the gap disappears — making an undersized
opening vanish changes the topology, it does not fix the diameter. Never shrink
a detail until its own interior stops being measurable, and never nudge a
crossing so an acute wedge inks over.

**Every rung moves paint, so re-check the keyshape after every repair.** Rung 1
pushes outward and can overflow; rungs 2 and 3 remove paint and can leave the
icon undersized. Record the declared bounds before repairing, and re-measure
after.

## Optical judgment

Inspect the painted result, not the centerlines. A mathematically even layout
can still need a correction when one side carries more visual weight.

When two approaches are genuinely close, render both at native size and keep the
stronger one. That is a real step, not a formality — the heart went through four
candidates and the sparkle through two.

Good compositions usually have one dominant mass, a clear symmetry or a
deliberate asymmetry, few internal relationships, and negative spaces that
survive at native size.

## Review at native size

The validators establish that the rules were followed. They cannot tell you the
icon is legible or convincing. Only looking at it at 32, 48 or 64 pixels does
that, and that review is mandatory.

```bash
python3 icon_set/scripts/contact_sheet.py --family solo --theme dark --png /tmp/solo.png
```

Review one family at a time. The sheet renders each icon at its own native
canvas, so a 32 sub and a 64 container do not compare meaningfully side by side.
