# Unlimited Shapes Icon Style Rules

This is the canonical authoring and review specification for the icon grid.
Rule IDs are stable so reviews can cite them precisely. Select `normal`, `sub`,
or `container` using [icon-types.md](icon-types.md) before applying these shared
invariants. Numeric canvas, stroke, center, keyshape, distance, and container-slot
values come from [`core/icon_profiles.json`](../core/icon_profiles.json); use the
[generated profile reference](generated/icon-profiles.md) instead of copying
those tables into another document.

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
| Ordinary corner radii | 4u or 8u only |
| Straight-line angles | Multiples of 15° |
| Curves | Circular/elliptical arcs and quadratic Béziers; no freehand cubics |
| Launch weights | Regular only |
| Bold | Roadmap follow-up within six months; not a launch weight |

The declared type's design canvas is the editable source of truth. The ship SVG is a geometrically equivalent half-scale export: coordinates, dimensions, radii, and stroke widths are divided by two.

## 2. System model and source document

An icon is an ordered list of registered atomic-shape instances. The registry is
an extensible implementation library, not a fixed visual vocabulary: add a new
generic atom whenever the current catalog would weaken the icon. Atoms generate
real geometry at the requested size and are never resized with a scale transform;
rotation and flips are rigid transforms about the instance center.

Recommended editable source:

```json
{
  "name": "coffee-mug",
  "iconType": "normal",
  "canvas": 48,
  "strokeWidth": 4,
  "keyfitCheck": { "targetToken": "square-40" },
  "cornerStyle": "round",
  "instances": [
    {
      "shapeId": "square",
      "x": 6,
      "y": 6,
      "w": 36,
      "h": 36,
      "rotation": 0,
      "flipX": false,
      "flipY": false,
      "z": 0
    }
  ]
}
```

Coordinates use `(0,0)` at top-left, with `x` rightward and `y` downward. Position is the unrotated instance box's top-left. Rotation is clockwise about the box center. Use whole design units unless an exact arc junction or documented optical correction requires a fraction.

### SVG reference preflight

Before rebuilding an SVG reference, run the project detector:

```bash
python3 core/detect_svg_shapes.py path/to/input.svg \
  --output path/to/input-shapes.json \
  --plot path/to/input-preflight.png
```

It classifies native SVG elements and flattened path commands, proposes atomic candidates, normalizes bounds to the 48-unit design canvas, and reports prohibited cubics, off-grid angles, undersized outlines, non-token corner radii, transforms, and ambiguous compound paths. The Matplotlib plot shows sampled source geometry, the 48-unit grid, detection bounds, labels, and color-coded QA state. Use `--show` for an interactive window. Review the plot, `specIssues`, and `makerPreflight.manualReview` before composition. Detection is evidence, not a tracing instruction; R6/R7 simplification and optical judgment still control the final icon.

## 3. Family rules

### R1 — Canvas, live area, and scale

- Declare `iconType` before composition. Omission means `normal` only for backward compatibility.
- Author on the selected profile's design canvas and export to its ship canvas.
- Every icon uses one centered painted keyshape declared by its type profile.
  The keyshape is the padding boundary; its generated dimensions and bounds are
  listed in [generated/icon-profiles.md](generated/icon-profiles.md).
- Use the selected profile's declared center as the optical center and symmetry axes.
- Paint must reach the selected keyshape's four cardinals or rectangular edges
  and remain entirely inside it. Circle paint may not enter the corner regions
  of that token's square bounding box. Merely fitting inside fails.
- Export by the profile's exact design-to-ship ratio.
- Centered strokes must not clip the canvas or cross the selected keyshape boundary.
- Container paint must also leave the profile's full centered 32×32 clearance
  square empty. The accepted sub keyshape describes preview compatibility; it
  does not reduce that required clear area. Validate the empty container and a
  filled preview as specified in [icon-types.md](icon-types.md).

### R2 — Paint and weight

- Stroke only; no fill, gradients, shadows, or baked background.
- Use `stroke="currentColor"`.
- Regular source stroke is exactly 4u; Regular ship stroke is exactly 2px.
- Stroke alignment is centered. Caps and joins are round.
- Regular is the only launch weight. Bold is a planned family extension, not an output to synthesize ad hoc.

A dot is a zero-length or nearly zero-length line with round caps centered on one point. It is not a tiny outlined circle.

### R3 — Geometry vocabulary

- Start with the strongest natural, immediately recognizable silhouette. Reuse an
  existing atom only when it preserves that visual quality without forced
  proportions, awkward seams, excess parts, or semantic drift. Otherwise create
  and register a new generic parametric atom. Catalog reuse is an optimization,
  never a reason to accept a worse icon.
- Straight-line directions snap to 15° increments: 0°, 15°, 30°, 45°, 60°, 75°, and 90°, plus rotations/reflections equivalent to those directions.
- Ordinary instance boxes and axis-aligned/45° endpoints stay on whole design units. Exact 15°/30°/60°/75° rotations and arc junctions may emit fractions only when derived from valid atomic geometry or documented as an optical correction. Bulk decimal coordinates from post-composition scaling are prohibited.
- Curves must be circular/elliptical arcs or quadratic Béziers. Freehand cubic Béziers are prohibited.
- Ordinary rounded corners use radius 4u or 8u only. Circles, ellipses, and capsule ends use their geometric radii as exceptions. The `sharp` runtime style uses radius 0.
- Outlined circles/ellipses and square-like outlines must be at least 4×4u. A true outlined circle therefore has radius at least 2u. Smaller details become point-line dots or are removed.

The legacy `s-curve` atom uses a cubic and is not valid for new-grid icons; use the arc-only `s-bend` atom for a continuous S contour. The legacy percentage-based `rounded-square` must resolve to an explicit 4u or 8u radius before it is valid.

### R4 — Distance Rule

Distinct, non-connected geometry must keep the profile's minimum distance between
the shortest points on their stroke centerlines. This applies to every orientation
and pair type, not only parallel lines.

| Type | Minimum centerline distance |
| --- | ---: |
| `normal` | 4u |
| `sub` | 3u |
| `container` | 4u |

Measure actual paths, not bounding boxes or object centers. At the Regular 4u
design stroke, normal and container parts exactly 4u apart touch at their painted
edges. The compact sub profile deliberately permits its 4u paint envelopes to
overlap by up to 1u at the 3u centerline floor. When two parts must show a visible
opening, use R5's painted-clearance requirement instead. Intentional connections
and meaningful crossings also follow R5.

### R5 — Connections, intersections, and cutouts

- Connected parts must visibly meet at a shared endpoint, coincident edge, tangent, or intentional crossing.
- At a simple joint, trim paths to the junction. Do not leave redundant geometry invisibly underneath or visibly beyond it.
- A declared visual opening must preserve at least 3u of painted clearance. With
  the Regular 4u stroke, that is at least 7u between stroke centerlines.
- When one element visually overlaps another but needs separation, cut the underlying path and leave a 3u cutout around the overlap boundary.
- Preserve a full crossing only when the crossing communicates the subject.
- Prefer rearrangement and path trimming to masks, erasers, or decorative fills.

### R6 — Scale, centering, and symmetry

- Size the icon to its selected semantic keyshape while preserving identity and internal spacing. Resize and resnap atoms in the editable source; never scale flattened final paths.
- Center visual mass around the selected profile's declared center.
- Prioritize bilateral symmetry for naturally symmetrical subjects. Mirror paired geometry around a deliberate axis.
- Keep asymmetry only when needed for recognition, action, perspective, status, or optical balance.
- Judge negative space and recognizability at the true ship size: 24px for
  normal, 16px for sub, and 32px for container.

### R7 — Minimal recognizable detail

- Prefer 3–10 instances and a few large, legible shapes.
- For sub icons, prefer 1–5 instances and no more than two identity-bearing internal features.
- Preserve the silhouette and one to three identity-bearing features; remove texture and incidental repetition.
- A reference is not a tracing template. Change primitives, proportions, connections, or feature placement when needed for clarity and compliance.

Priority: visual quality and a natural, immediately recognizable silhouette;
then rule compliance, family consistency, implementation simplicity, catalog
reuse, and literal reference fidelity. A compliant but awkward icon still fails.

### R8 — Stable naming and ordering

- Use kebab-case names.
- Keep instances in conceptual build order: main form first, attachments and details afterward.
- Use explicit stacking only when it materially affects an overlap.

### R9 — Enclosed negative space

Every enclosed negative-space region in the final ship SVG must have a largest inscribed radius of at least 1u on its design canvas (2u design diameter; equality passes). This is the floor, not the target: an identity-bearing opening still needs the profile-specific R4 centerline distance or R5's 3u painted clearance, as applicable.

A junction that is solid must be solid *on purpose*. Paint must fill it at least 1u deep, so that retreating every painted edge by 1u leaves it closed. A junction that survives on less than that is a **pinch**: two parts squeezed until their paint happens to merge. A pinch fails review exactly like an undersized hole — it reads as a mud spot at ship size, and it hides the collision instead of resolving it.

Geometric shapes keep their spacing. Both defects mean the artwork is short of room in that zone, so every legal repair *gives* room:

**Repair ladder — work down it in order, and stop at the first option that keeps the icon recognizable.**

1. **Enlarge the opening.** Grow the enclosing shape, lengthen or reangle the parts that bound it, or move the parts apart until the region clears 1u inscribed radius with margin.
2. **Rebalance the composition.** Scale the dominant part down and the crowded detail up, so the detail is large enough to carry a legal opening. Recenter on the selected profile afterwards; redistribute space, never steal it.
3. **Remove the part.** Delete the whole SVG element, semantic group, or atom instance that creates the sub-minimum region, when it is not identity-bearing. Record the omission. Two clean parts beat four crowded ones.

**A repair may not change the icon's declared keyshape.** Every rung moves paint, so a repair that clears R9 can silently break R1:

- Record the declared keyshape with `check_keyfit.py` *before* repairing.
- After repairing, the paint must still reach and remain inside the **same declared keyshape** and stay optically centered.
- Rung 1 pushes paint outward — verify nothing crossed the selected circle or rectangle boundary. If clearing the opening needs more room, use rung 2 instead of overflowing.
- Rungs 2 and 3 remove paint — verify the artwork still reaches all required cardinals or edges and did not become undersized.
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

| Property | Value |
| --- | --- |
| Canvas edge padding | 4u |
| Distinct element centerline spacing | Minimum 4u (= one Regular stroke width) |
| Overlap cutout | 3u |
| Main icon with badge | Fit main symbol to a 32×32u box |
| Badge | 16u diameter / nominal box, about 50% of main |
| Standard bottom-right center | `(32,32)` |

A 16u circular bottom-right badge centered at `(32,32)` occupies `x=24…40`, `y=24…40`. Reposition the 32×32u main symbol optically within the live area so the two symbols remain legible and obey R4/R5. This badge is not the standalone 32×32 `sub` icon type.

Corner semantics:

| Corner | Meaning |
| --- | --- |
| Bottom-right | Additive action |
| Top-right | Status |
| Bottom-left | Modifier |
| Top-left | Security |

Do not place a badge in a different corner merely to solve crowding if that changes its meaning; simplify or reposition the main symbol first.

## 5. Runtime parameters

These renderer axes are part of the product contract:

| Parameter | Values | Default / meaning |
| --- | --- | --- |
| Color | CSS color via `currentColor` | Inherits from context |
| Ship stroke width | 1–3px | 2px Regular; equivalent design value is 2–6u |
| Keyshape | Type-specific tokens in [icon-types.md](icon-types.md) | Select the intended semantic target; reach its cardinals/edges and remain inside it |
| Corner style | `round`, `sharp` | `round` uses authored 4u/8u tokens; `sharp` resolves ordinary corners to 0 |

Runtime stroke changes must preserve keyshape containment and legibility; they do not create separately authored launch weights.

## 6. Exact SVG output

Generate both canonical outputs from editable JSON:

```bash
python3 core/emit_icon.py <icon.json> --out-dir <output-folder>
```

The emitter resolves the selected profile and writes a design SVG using its
design canvas/stroke plus a geometrically equivalent ship SVG using its exact
scale. Both roots use `fill="none"`, `stroke="currentColor"`, and round caps and
joins. A container's slot metadata and filled preview are review artifacts, not
extra paint in the production SVG.

Keep the production output transparent. Construction keyshapes, grids, collision overlays, and QA annotations never ship.

## 7. Review checklist

- [ ] The icon has a natural, convincing silhouette and is immediately
  recognizable; no existing atom was reused at the expense of visual quality.
- [ ] `iconType` is declared and design/ship canvases match that profile.
- [ ] Complete painted artwork reaches the selected centered keyshape at all four cardinals/edges and remains inside it.
- [ ] The type-appropriate grid audit passes: expected canvas/stroke, 15° directions, and whole-unit ordinary construction.
- [ ] Paint is `currentColor`, no fill, centered profile Regular stroke, round caps/joins.
- [ ] Ordinary radii are 4u or 8u; straight-line angles are multiples of 15°.
- [ ] Curves are arcs or quadratics; no freehand cubics or legacy `s-curve`.
- [ ] Minimum outlined circle/square-like size is 4×4u; smaller marks are dots or removed.
- [ ] Every distinct pair satisfies its profile's centerline Distance Rule: 4u
  for normal/container and 3u for sub.
- [ ] Connected parts meet; redundant intersection paths are trimmed; overlap cutouts are 3u.
- [ ] Every enclosed region clears the 1u inscribed radius; no junction is held closed by less than 1u of paint.
- [ ] Any hole repair enlarged, rebalanced, or removed a part; nothing was squeezed shut or clipped.
- [ ] The repaired icon keeps its declared keyshape token, stays centered, and remains contained by that keyshape.
- [ ] A container declares its accepted sub keyshape, keeps the full centered
  32×32 clearance square empty, and passes a filled-preview review.
- [ ] Composite badge layout uses the 32u main / 16u badge system and correct corner semantics.
- [ ] Naturally symmetrical subjects are deliberately mirrored.
- [ ] Any contour missing from the catalog was added as a reusable atom instead
  of being approximated poorly.
- [ ] Subject remains recognizable and balanced at the profile's true ship size.
- [ ] Runtime parameters preserve geometry and semantics.
- [ ] Reference material was simplified rather than traced literally.

## 8. Migration status

This specification supersedes the legacy 40×40 canvas, former 40u/44u/48u keyfit ladders, 2u design stroke, common-fit presets, and stroke-4 diagnostic workflow. Legacy `-fit.svg` files do not define the current keyshape system.
