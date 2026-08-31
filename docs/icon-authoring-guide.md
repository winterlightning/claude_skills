# Unlimited Shapes Icon Authoring Guide

Use [icon-rules.md](icon-rules.md) as the canonical specification. This guide summarizes day-to-day work on the new 48-unit design grid and 24px ship grid.

For the required operational order—including detection, skill loading, evidence handoff, mapping, registry extension, validation, and delivery—follow [icon-execution-steps.md](icon-execution-steps.md).

## Deliverables

For each new-grid icon, keep:

- `<name>.json` (or equivalent): editable atomic composition source on the 48×48 design canvas.
- `<name>-design.svg`: editable 48×48 design SVG with a 4u Regular stroke.
- `<name>.svg`: clean 24×24 ship SVG with the same geometry at half scale and a 2px Regular stroke.

Grid overlays, keyshape guides, collision views, and QA annotations are temporary review material and never ship.

## Baseline at a glance

| Design source | Ship output |
| --- | --- |
| 48×48 canvas | 24×24 canvas |
| 1u minor / 4u major grid | Exact half-scale geometry |
| Circle Ø44u; square 40×40u; portrait 36×44u; landscape 44×36u | Circle Ø22px; square 20×20px; portrait 18×22px; landscape 22×18px |
| 4u Regular stroke | 2px Regular stroke |
| Corner radii 4u / 8u | Corner radii 2px / 4px |
| Center `(24,24)` | Center `(12,12)` |

Use `currentColor`, centered strokes, and round caps/joins. Regular is the only launch weight.

## Workflow

1. Run shape detection on SVG references before interpreting or rebuilding them:

   ```bash
   python3 core/detect_svg_shapes.py path/to/input.svg \
     --output path/to/input-shapes.json \
     --plot path/to/input-preflight.png
   ```

   Add `--show` to open the Matplotlib view interactively. Add `--strict` in automated pipelines; it exits with status 3 when unsupported or ambiguous geometry needs review. The plot overlays sampled geometry, detection bounds, labels, the 48-unit grid, the live area, and color-coded QA. The report identifies native and path-based lines, arcs, quadratic/cubic curves, circles, ellipses, rectangles, pills, rounded rectangles, triangles, diamonds, and compound paths. Its `makerPreflight.suggestedAtoms` are starting suggestions, not final artwork.
2. Review every `specIssues` and `makerPreflight.manualReview` entry. Replace detected cubics with arcs or quadratics, flatten transforms before coordinate conversion, and resolve ambiguous compound paths semantically.
3. Reduce the subject or reference to its smallest recognizable silhouette and one to three identity-bearing features. Do not trace secondary detail literally.
4. Establish `x=24` or `y=24` as the symmetry axis when the subject is naturally bilateral.
5. Compose only from approved atoms on the 1u minor / 4u major grid to exactly match one centered painted keyshape. The keyshape is the padding boundary: circle Ø44u, square 40×40u, portrait 36×44u, or landscape 44×36u. Paint must reach its cardinals/edges and remain inside it; circle paint may not enter the corner regions. Resize/recompose atomic instances, never flattened path data.
6. Snap straight lines to 15° increments. Use arcs and quadratic curves only; do not add freehand cubic paths.
7. Use 4u or 8u for ordinary rounded corners. Circles and capsule ends are geometric exceptions.
8. Check every nearby pair. Distinct centerline paths stay at least 4u apart; with a 4u stroke, their painted edges may touch but must not overlap.
9. Make connected components meet cleanly. Trim redundant segments at joints. Where an overlap needs separation, cut the underlying path with a 3u cutout.
10. Inspect on the 48-unit design canvas and at 24px. Check clipping, symmetry, visual centering, negative space, and recognition.
11. Export the 24×24 SVG by dividing design coordinates, dimensions, radii, and stroke width by two. Do not scale only the outer SVG size while leaving undocumented geometry transforms.
12. Run `python3 core/check_svg_grid.py <final-svg-or-folder> --expected ship --output-dir <grid-qa>`. Fix mixed canvases, off-15° segments, and avoidable fractional axis/45° coordinates in the editable atomic source, then regenerate both sizes.

## Composite icons

- Reduce the main symbol to a 32×32u box.
- Use a 16u-diameter or nominal 16×16u subicon.
- For the standard bottom-right placement, center the subicon at `(32,32)`.
- Bottom-right means additive; top-right means status; bottom-left means modifier; top-left means security.
- Rework the main icon before moving a subicon to a semantically incorrect corner.

## Runtime axes

Expose these renderer parameters:

- Color: `currentColor`.
- Ship stroke: 1–3px; 2px is Regular.
- Keyshape: `circle-44`, `square-40`, `portrait-36x44`, or `landscape-44x36`. Choose and record the intended semantic target; paint must reach and remain inside it.
- Corner style: `round` uses the 4u/8u design tokens; `sharp` resolves ordinary corners to zero radius.

Runtime variants must preserve recognition, spacing semantics, and optical centering. They are parameters, not separately improvised icon drawings.

## Final checks

- Design SVG uses `viewBox="0 0 48 48"`; ship SVG uses `viewBox="0 0 24 24"`.
- Production paint is `fill="none"`, `stroke="currentColor"`, with round caps and joins.
- Default stroke is 4u design / 2px ship and is centered.
- Complete painted artwork reaches the selected keyshape's four cardinals/edges and remains inside it.
- Keyfit fitting did not scale flattened path data or create bulk fractional coordinates; the final SVG grid audit passes.
- Ordinary radii are 4u or 8u; line angles are multiples of 15°.
- Curves are arcs or quadratics; there are no freehand cubics.
- Outlined circles and square-like shapes are at least 4×4u. Smaller marks are point-line dots or removed.
- Distinct parts satisfy the 4u centerline Distance Rule.
- Connected parts meet; redundant paths are trimmed; overlap cutouts are 3u.
- Every enclosed region clears a 1u inscribed radius; every solid junction is filled at least 1u deep. A crowded zone is repaired by enlarging the opening, rebalancing the composition, or removing a whole part — never by squeezing parts together until the gap closes (R9).
- Any such repair keeps the same declared keyshape, remains centered, and does not cross its boundary.
- Symmetrical subjects are deliberately mirrored.
- Composite icons follow the 32u main / 16u subicon system and corner semantics.
- The subject remains clean and recognizable at 24px.

## Migration note

Legacy 40×40 canvases, former 40u/44u/48u keyfit ladders, common-fit exports, and `-fit.svg` artifacts do not define the four current centered keyshapes.
