# Icon authoring techniques

This is the practical drawing guide. It intentionally does not repeat profile
numbers, validation commands, or delivery rules.

- Start with the selected [type skill](icon-types.md), then use the shared
  [icon pipeline](icon-pipeline.md).
- Treat [icon-rules.md](icon-rules.md) as the written visual specification.
- Read the generated [profile reference](icon-profiles.md) for exact
  canvas, stroke, center, keyshape, distinct-part distance, and container-slot values.
- Use [atomic-shapes.md](atomic-shapes.md) for editable geometry and reference retrieval.
- Use [scripts.md](scripts.md) to understand a command before running it.

The machine authority for profile geometry and numerical validation is
[`core/icon_profiles.json`](../../core/icon_profiles.json). Do not copy those values
into another guide; use the [profile manager](profile-configuration.md) to update
that source and its mirrors. The built-in skills are role templates; custom
profile names use this same shared workflow. Configuration changes do not migrate
existing icons or preserve their old QA verdicts.

## Reduce before composing

Describe the subject in one short sentence, then keep only:

1. its smallest recognizable silhouette;
2. the identity-bearing features allowed by the selected type's detail guidance;
3. no secondary detail that disappears at the selected profile's native size.

The selected type's rules define its detail budget.

## Choose quality first, then exact construction

Decide the clearest natural silhouette from the semantic brief and prototype.
Retrieve useful Lucide original/debug pairs and inspect exact coordinates to
understand contour flow, proportions, corners and gaps. Apply the relevant
principles on the declared profile rather than copying the whole reference.
Record reference names, reasons and principles under `sourceAnalysis`.

Build schema-version-2 editable JSON from geometry elements. A contour may use
connected line/arc/quadratic/cubic segments within one path; a simple native
shape need not be split. New contours do not require registry additions. Do not
force a form into a named template or add segments to meet a density target.

When two approaches are genuinely close, render both at native size and keep
the visually stronger result. Edit endpoints, curve controls and attachments
directly so the source remains clear and re-emittable.

Good compositions usually have:

- one dominant mass or outline;
- a clear symmetry or intentional asymmetry;
- a small number of readable internal relationships;
- negative spaces that survive true-size review.

Choose the semantic keyshape before tuning the drawing. The complete painted
artwork must meet its declared exact or reviewed optical keyfit contract and stay
inside the boundary. The agent may approve a subject- or prototype-justified
[keyshape exception](icon-pipeline.md#keyshape-exceptions), recording optical
mode and measured bounds instead of distorting the form to reach every edge.
Do not switch keyshapes merely to make a weak composition pass.

## Join and spacing technique

- Make connected parts meet cleanly and trim redundant segments.
- Keep distinct parts separated according to the Distance Rule in
  [icon-rules.md](icon-rules.md).
- When an overlap needs visual separation, cut the underlying path rather than
  stacking an opaque patch over it.
- Prefer enlarging an opening, rebalancing the composition, or removing a whole
  part over squeezing a gap until it disappears.
- Choose line directions for a natural silhouette and optical balance, and use
  deliberate arcs or quadratic/cubic curves with smooth joins where appropriate.

Inspect the actual painted result, not just centerlines. A mathematically even
layout can still need a small optical correction when one side carries more
visual weight.

## Containers

Use the [container rules](../container-icons/rules.md) for slot clearance and
empty/filled review. Compose the inserted symbol using the
[sub-icon skill](../sub-icons/SKILL.md). Judge both the outer silhouette and the
combined preview; the type guides define which artifacts ship.

## Composite badges

A badge is a semantic modifier inside a normal icon, not a standalone sub-icon
profile. Use the badge geometry defined by the [normal rules](../icons/rules.md), and
respect the corner semantics documented there. Rework the main symbol before
moving a badge to a semantically incorrect corner.

## Runtime axes

The renderer may expose color, ship stroke, keyshape, and corner style. Treat
these as controlled parameters of one composition, not permission to improvise
separate drawings. Every variant must preserve recognition, spacing semantics,
and optical centering.

## Review at native size

Inspect the editable composition and canonical SVG at the same native profile
size. Check geometry, grid, joins, protected regions, keyfit, negative space,
balance and recognition there. Native-size acceptance is mandatory; do not
produce a second reduced or enlarged review export. Optional manual zoom can
help diagnose a coordinate or join, but it is not another deliverable size and
cannot replace the native-size verdict.

The pipeline's automated gates establish structural compliance. Native-size visual
review still decides whether the icon is legible and visually convincing.

## Migration note

Legacy canvases, old keyfit ladders, common-fit exports, and `-fit.svg`
artifacts are historical inputs, not current authority. Migrate their meaning
into schema-version-2 editable JSON, select an explicit profile, and regenerate outputs
through the shared pipeline.
