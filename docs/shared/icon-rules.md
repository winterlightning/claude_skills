# Shared Icon Style Rules

These rules apply to all icon types. Rule IDs are stable so reviews can cite them
precisely. Start with the selected type's skill and rules:
[normal](../icons/SKILL.md), [sub](../sub-icons/SKILL.md), or
[container](../container-icons/SKILL.md). Type-specific composition, detail
budgets, and delivery requirements live in those folders.

Numeric canvas, stroke, center, keyshape, distance, and container-slot values come
from [`core/icon_profiles.json`](../../core/icon_profiles.json). Read the selected
type's generated `profile.md`; the [combined reference](icon-profiles.md) is
available when comparing profiles.

## 1. Baseline specification

| Property | Canonical value |
| --- | --- |
| Profile geometry | Selected `iconType` in `core/icon_profiles.json` |
| Coordinate scale | Exact design-to-ship ratio declared by the profile |
| Grid | 1u minor, 4u major |
| Keyshapes | Type-specific centered painted boundaries declared by the profile |
| Regular stroke | Profile design stroke → profile ship stroke |
| Stroke alignment | Centered |
| Caps / joins | Round / round |
| Ordinary corner radii | Prefer 4u; 2u for compact forms; other justified geometric/optical radii allowed |
| Straight-line angles | Chosen for a natural silhouette and optical balance |
| Curves | Circular/elliptical arcs and deliberate quadratic/cubic Béziers |
| Launch weights | Regular only |
| Bold | Roadmap follow-up within six months; not a launch weight |

The declared type's design canvas is the editable source of truth. The ship SVG is a geometrically equivalent half-scale export: coordinates, dimensions, radii, and stroke widths are divided by two.

## 2. System model and source document

New icons use `schemaVersion: 2` and an ordered `elements` array of exact,
editable SVG geometry. Each element has a unique `id`, optional semantic `role`,
supported `tag`, and geometry-only `attrs`. Lines, arcs, quadratic/cubic paths,
circles, ellipses, rectangles and polygons are available directly. Connected
contours can remain connected paths; a new contour needs no registry change.
See [the geometry guide](atomic-shapes.md) for the schema and reference workflow.

Editable sources also declare `name`, `iconType`, the profile's `canvas` and
`strokeWidth`, `keyfitCheck.targetToken`, and `cornerStyle`. The shared pipeline
defines accompanying `sourceAnalysis` evidence. Containers retain `containerSlot`.
Legacy `instances`/`shapeId` documents are compatibility inputs, not the new
authoring contract.

Coordinates use `(0,0)` at top-left, with `x` rightward and `y` downward. Author
actual geometry on the design canvas with no SVG transforms or per-element paint.
Prefer whole design units for ordinary construction; exact curve junctions,
deliberate diagonal geometry and documented optical corrections may use fractions.

### SVG reference preflight

Before rebuilding an SVG reference, run the project detector:

```bash
python3 core/detect_svg_shapes.py path/to/input.svg \
  --output path/to/input-shapes.json \
  --plot path/to/input-preflight.png
```

It classifies native SVG elements and path commands, normalizes source-analysis
bounds to its 48-unit reference grid, and reports geometry needing review. Legacy
`suggestedAtoms` are optional detector hints, not mandatory authoring choices.
The plot shows sampled geometry, grid, bounds and QA labels. Review the plot,
`specIssues`, and `makerPreflight.manualReview`; curves, non-default radii and
foreign-grid coordinates need interpretation rather than automatic rejection.
Detection is evidence, not a tracing instruction; R6/R7 still govern the result.

## 3. Family rules

### R1 — Canvas, live area, and scale

- Declare `iconType` before composition. Omission means `normal` only for backward compatibility.
- Author on the selected profile's design canvas and export to its ship canvas.
- Every icon uses one centered painted keyshape declared by its type profile.
  The keyshape is the padding boundary; its generated dimensions and bounds are
  listed in the selected type's `profile.md` and the
  [combined profile reference](icon-profiles.md).
- Use the selected profile's declared center as the optical center and symmetry axes.
- In the default `exact` keyfit mode, paint must reach the selected keyshape's four cardinals or rectangular edges
  and remain entirely inside it. Circle paint may not enter the corner regions
  of that token's square bounding box. Merely fitting inside fails in exact mode.
- Intrinsically thin or sparse subjects, such as a divider, ellipsis or glyph,
  may use `keyfitCheck.mode: "optical"` rather than being stretched to four edges.
  This requires a meaningful `rationale` and explicit design-unit
  `paintedBounds: [left, top, right, bottom]`. Measured paint must match those
  declared bounds and stay inside the selected token, including radial circle
  containment. True-size visual review is mandatory; optical mode is not an
  overflow waiver or a substitute for repairing unintended undersizing.
- Export by the profile's exact design-to-ship ratio.
- Centered strokes must not clip the canvas or cross the selected keyshape boundary.
- Apply the selected type's additional constraints, including the
  [container clearance and preview contract](../container-icons/rules.md).

### R2 — Paint and weight

- Stroke only; no fill, gradients, shadows, or baked background.
- Use `stroke="currentColor"`.
- Use the exact Regular design and ship strokes declared in the selected profile.
- Stroke alignment is centered. Caps and joins are round.
- Regular is the only launch weight. Bold is a planned family extension, not an output to synthesize ad hoc.

A dot is a zero-length or nearly zero-length line with round caps centered on one point. It is not a tiny outlined circle.

### R3 — Geometry vocabulary

- Start with the strongest natural, immediately recognizable silhouette. Use
  exact editable geometry and relevant original/debug references to understand
  construction. Reuse a motif only when it fits; neither registry growth nor a
  prescribed element count is part of the authoring workflow.
- Choose straight-line directions for a clear, natural silhouette and optical balance. There is no prescribed angle increment.
- Prefer whole-unit ordinary construction. Exact arc junctions, arbitrary
  line directions, curve controls and documented optical corrections may use
  fractions. Do not introduce bulk decimals by scaling a finished foreign-grid icon.
- Use circular/elliptical arcs or intentional quadratic/cubic Béziers. Choose
  controls for smooth tangency and the intended silhouette, not incidental texture.
- Prefer radius 4u for ordinary rounded corners and 2u for compact forms. Other
  smooth geometric or optical radii are allowed with a reason. Circles, ellipses
  and capsules retain their geometric radii.
- Outlined circles/ellipses and square-like outlines must be at least 4×4u. A true outlined circle therefore has radius at least 2u. Smaller details become point-line dots or are removed.

Judge curves by their finished contour, continuity and true-size clarity, not by
whether they match a legacy registered shape or a fixed radius list.

### R4 — Distance Rule

Distinct, non-connected geometry must keep the profile's minimum distance between
the shortest points on their stroke centerlines. This applies to every orientation
and pair type, not only parallel lines.

Read the minimum centerline distance from the selected type's `profile.md`.
Measure actual paths, not bounding boxes or object centers. A centerline floor
does not guarantee visible white space between painted strokes; when two parts
must show an opening, use R5's painted-clearance requirement. The
[sub-icon rules](../sub-icons/rules.md) explain that profile's compact spacing.
Intentional connections and meaningful crossings also follow R5.

### R5 — Connections, intersections, and cutouts

- Connected parts must visibly meet at a shared endpoint, coincident edge, tangent, or intentional crossing.
- At a simple joint, trim paths to the junction. Do not leave redundant geometry invisibly underneath or visibly beyond it.
- A declared visual opening must preserve at least 3u of painted clearance. With
  the Regular 4u stroke, that is at least 7u between stroke centerlines.
- When one element visually overlaps another but needs separation, cut the underlying path and leave a 3u cutout around the overlap boundary.
- Preserve a full crossing only when the crossing communicates the subject.
- Prefer rearrangement and path trimming to masks, erasers, or decorative fills.

### R6 — Scale, centering, and symmetry

- Size the icon to its selected semantic keyshape and declared keyfit mode while preserving identity and internal spacing. Recompose coordinates in the editable source; never scale flattened final paths.
- Center visual mass around the selected profile's declared center.
- Prioritize bilateral symmetry for naturally symmetrical subjects. Mirror paired geometry around a deliberate axis.
- Keep asymmetry only when needed for recognition, action, perspective, status, or optical balance.
- Judge negative space and recognizability at the selected profile's true ship size.

### R7 — Minimal recognizable detail

- Use a few large, legible shapes within the selected type's detail guidance.
- Preserve the silhouette and its identity-bearing features; remove texture and incidental repetition.
- A reference is not a tracing template. Change primitives, proportions, connections, or feature placement when needed for clarity and compliance.

Priority: visual quality and a natural, immediately recognizable silhouette;
then rule compliance, family consistency, implementation simplicity, and literal
reference fidelity. A compliant but awkward icon still fails.

### R8 — Stable naming and ordering

- Use kebab-case names.
- Keep elements in conceptual build order: main form first, attachments and details afterward.
- Use explicit stacking only when it materially affects an overlap.

### R9 — Enclosed negative space

Every enclosed negative-space region in the final ship SVG must have a largest inscribed radius of at least 1u on its design canvas (2u design diameter; equality passes). This is the floor, not the target: an identity-bearing opening still needs the profile-specific R4 centerline distance or R5's 3u painted clearance, as applicable.

A junction that is solid must be solid *on purpose*. Paint must fill it at least 1u deep, so that retreating every painted edge by 1u leaves it closed. A junction that survives on less than that is a **pinch**: two parts squeezed until their paint happens to merge. A pinch fails review exactly like an undersized hole — it reads as a mud spot at ship size, and it hides the collision instead of resolving it.

Geometric shapes keep their spacing. Both defects mean the artwork is short of room in that zone, so every legal repair *gives* room:

**Repair ladder — work down it in order, and stop at the first option that keeps the icon recognizable.**

1. **Enlarge the opening.** Grow the enclosing shape, lengthen or reangle the parts that bound it, or move the parts apart until the region clears 1u inscribed radius with margin.
2. **Rebalance the composition.** Scale the dominant part down and the crowded detail up, so the detail is large enough to carry a legal opening. Recenter on the selected profile afterwards; redistribute space, never steal it.
3. **Remove the part.** Delete the complete non-essential element or semantic group that creates the sub-minimum region. Record the omission. Two clean parts beat four crowded ones.

**A repair may not change the icon's declared keyshape.** Every rung moves paint, so a repair that clears R9 can silently break R1:

- Record the declared keyshape with `check_keyfit.py` *before* repairing.
- After repairing, the paint must still satisfy the **same declared keyshape and keyfit mode** and stay optically centered. Exact mode retains its edge/cardinal contacts; optical mode retains its justified measured-bound declaration.
- Rung 1 pushes paint outward — verify nothing crossed the selected circle or rectangle boundary. If clearing the opening needs more room, use rung 2 instead of overflowing.
- Rungs 2 and 3 remove paint — verify the artwork still meets its declared extents and did not become unintentionally undersized.
- If the declared keyshape fails, restore the required extent and containment, then re-measure both negative-space gates.

**Never** do any of the following to obtain a pass:

- Squeeze the surrounding parts together until the region collapses to zero area. Making an undersized hole disappear changes the topology; it is not a diameter fix.
- Shrink a detail until its own interior stops being measurable.
- Nudge a crossing so an acute wedge inks over.
- Clip or delete an arbitrary path fragment, or leave a part visibly truncated.
- Let the silhouette cross its keyshape boundary or become undersized in order to open a zone.

Regenerate both SVG sizes and rerun structural, overlap, keyshape, hole-diameter, pinch, and true-size checks after every correction — keyshape containment included even when the repair looks local, because painted bounds are what the token is measured from. `core/qa_overlays.py` measures both gates; see [qa-overlays-guide.md](qa-overlays-guide.md).

The 1u minimum above is the rule. The checker does not rasterize it through the authored 4u stroke, because in a tight zone that leaves a sliver one raster sample wide, which is indistinguishable from the seam a renderer leaves where two strokes graze tangentially — a phantom failure. It rasterizes at a **1u** stroke instead and raises its threshold to **2.5u radius / 5u diameter**. Narrowing the paint by `d` per edge grows every enclosed region's largest inscribed circle by exactly `d`, so moving the threshold by the same `d` is not a relaxation: the verdict is this 1u rule, measured where the measurement is trustworthy. Reports restate every radius on the 1u scale as `equivalent_radius_at_authored_stroke_design_u`. Authors size openings against the 1u rule and never against the 2.5u internal gate. For worked examples of each rung, the sizing math, and what a squeeze looks like when it is measured, see [negative-space-repair-examples.md](negative-space-repair-examples.md).

## 4. Composite badge rules

Composite badges belong to normal icons. Their dimensions, placement, and corner
semantics live in the [normal-icon rules](../icons/rules.md). A standalone sub
icon follows its own type contract.

## 5. Runtime parameters

These renderer axes are part of the product contract:

| Parameter | Values | Default / meaning |
| --- | --- | --- |
| Color | CSS color via `currentColor` | Inherits from context |
| Ship stroke width | 1–3px | 2px Regular; equivalent design value is 2–6u |
| Keyshape | Type-specific tokens in [icon-types.md](icon-types.md) | Select the intended semantic target and satisfy the declared exact/optical keyfit contract |
| Corner style | `round`, `sharp` | Geometry remains explicitly authored; review deliberate variants rather than assuming an arbitrary path can be sharpened automatically |

Runtime stroke changes must preserve keyshape containment and legibility; they do not create separately authored launch weights.

## 6. Exact SVG output

Generate both canonical outputs from editable JSON:

```bash
python3 core/emit_icon.py <icon.json> --out-dir <output-folder>
```

The emitter resolves the selected profile and writes a design SVG using its
design canvas/stroke plus a geometrically equivalent ship SVG using its exact
scale. Both roots use `fill="none"`, `stroke="currentColor"`, and round caps and
joins. Follow the selected type's rules for additional review artifacts.

Keep the production output transparent. Construction keyshapes, grids, collision overlays, and QA annotations never ship.

## 7. Review checklist

- [ ] The icon has a natural, convincing silhouette and is immediately
  recognizable; no reference motif was reused at the expense of visual quality.
- [ ] `iconType` is declared and design/ship canvases match that profile.
- [ ] Paint satisfies the declared exact or documented optical keyfit mode and remains inside the selected centered keyshape.
- [ ] The type-appropriate grid audit passes: expected canvas/stroke and whole-unit ordinary construction.
- [ ] Paint is `currentColor`, no fill, centered profile Regular stroke, round caps/joins.
- [ ] Corner radii follow useful defaults or have a geometric/optical reason.
- [ ] Arc, quadratic and cubic contours have deliberate endpoints and smooth joins where intended.
- [ ] Minimum outlined circle/square-like size is 4×4u; smaller marks are dots or removed.
- [ ] Every distinct pair satisfies its profile's centerline Distance Rule.
- [ ] Connected parts meet; redundant intersection paths are trimmed; overlap cutouts are 3u.
- [ ] Every enclosed region clears the 1u inscribed radius; no junction is held closed by less than 1u of paint.
- [ ] Any hole repair enlarged, rebalanced, or removed a part; nothing was squeezed shut or clipped.
- [ ] The repaired icon keeps its declared keyshape token, stays centered, and remains contained by that keyshape.
- [ ] The selected type's rules and delivery checklist also pass.
- [ ] Naturally symmetrical subjects are deliberately mirrored.
- [ ] New contours live directly in schema-version-2 editable elements, with no
  registry extension or part-count quota required.
- [ ] Subject remains recognizable and balanced at the profile's true ship size.
- [ ] Runtime parameters preserve geometry and semantics.
- [ ] Reference material was simplified rather than traced literally.

## 8. Migration status

This specification supersedes the legacy 40×40 canvas, former 40u/44u/48u keyfit ladders, 2u design stroke, common-fit presets, and stroke-4 diagnostic workflow. Legacy `-fit.svg` files do not define the current keyshape system.
