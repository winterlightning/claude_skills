# Editable geometry and Lucide references

New icons are authored as exact, inspectable geometry in schema-version-2 JSON.
They do not need a registered shape ID or a new registry entry. This page keeps
its historical filename so existing skill links still resolve; it is no longer
a catalog of mandatory building blocks.

The [shared rules](icon-rules.md) define style and QA. The selected type's
resolved JSON profile supplies canvas, stroke, keyshape, grid and validation
values; see [profile configuration](profile-configuration.md). Reference
geometry informs construction; it does not override either source.

## Work at the useful level

Reason about the subject, its contours and relationships, then the exact geometry
needed to draw them. A circle can remain a `circle`; a connected outline can
remain one compound `path`. Use separate elements where separate editing or
semantic roles help. Do not split a contour merely to raise a part count, and do
not hide a whole subject behind an opaque named-shape implementation.

The low-level vocabulary is line endpoints, arc radii/flags, Bézier control
points, and native SVG shapes. The reusable knowledge is how those coordinates
form smooth corners, balanced enclosures, open contours, attachments and gaps.
Neither primitive reuse frequency nor elements per icon is a quality gate.

## Schema-version-2 geometry

An editable source retains its existing profile and evidence fields and adds
`schemaVersion: 2` with an ordered `elements` array:

```json
{
  "schemaVersion": 2,
  "name": "example-search",
  "iconType": "normal",
  "canvas": 48,
  "strokeWidth": 4,
  "cornerStyle": "round",
  "keyfitCheck": {
    "targetToken": "square-40",
    "reason": "Illustrative declaration; choose and verify the finished silhouette."
  },
  "elements": [
    {"id": "lens", "role": "main outline", "tag": "circle", "attrs": {"cx": 22, "cy": 22, "r": 16}},
    {"id": "handle", "role": "attachment", "tag": "line", "attrs": {"x1": 34, "y1": 34, "x2": 42, "y2": 42}}
  ],
  "sourceAnalysis": {"incomplete": true}
}
```

This uses built-in normal defaults as a schema illustration, not a validated
deliverable or a fixed canvas/stroke requirement. Complete the source
analysis, choose the appropriate keyshape, and run the pipeline before shipping.
Containers also retain their required `containerSlot` metadata.

Keyfit defaults to `exact`. Intrinsically thin/sparse forms may use
`keyfitCheck.mode: "optical"` with a meaningful `rationale` and design-unit
`paintedBounds: [left, top, right, bottom]`. These are measured targets, not
permission to overflow a token. See shared R1 for the complete review contract.

Each element has a stable unique `id`, an optional readable `role`, a supported
`tag`, and geometry-only `attrs`. Array order is drawing order.
IDs start with a letter and then use letters, digits, `_`, `.`, `:` or `-`.
Coordinates are finite unitless numbers; dimensions and circle/ellipse radii
must be positive. Rectangle corner radii may be zero.

| Tag | Geometry attributes |
| --- | --- |
| `path` | `d`: SVG path data, including connected subpaths and `M/L/H/V/A/Q/T/C/S/Z` commands |
| `line` | `x1`, `y1`, `x2`, `y2`; endpoints may use any deliberate direction |
| `circle` | `cx`, `cy`, `r` |
| `ellipse` | `cx`, `cy`, `rx`, `ry` |
| `rect` | `x`, `y`, `width`, `height`, optional `rx` and `ry` |
| `polyline`, `polygon` | `points`: SVG coordinate-pair string |

Author coordinates on the declared design canvas. Geometry attributes cannot
contain paint, CSS, transforms, event handlers, external references, or arbitrary
SVG markup. The emitter supplies no fill, `currentColor`, profile stroke width,
and round caps/joins centrally. Bake deliberate rotations/reflections into the
coordinates rather than adding SVG transforms. Repair this JSON and re-emit the
native SVG and any same-size compatibility alias; never patch only the final SVG.

## Curve and corner construction

- For the built-in 4u stroke, prefer a 4u ordinary corner radius; 2u can serve compact
  forms. Other radii are valid when they produce a smooth geometric join or a
  justified optical result. There is no 4u/8u-only token gate.
- Use circular/elliptical arcs when the contour is genuinely circular/elliptical.
  Set endpoints, radii and sweep intentionally; do not infer them from a colored
  preview when exact source values are available.
- Use quadratic or cubic Béziers for contours that need them. Align tangent
  directions at smooth joins and keep control points economical. Cubics are not
  prohibited merely because they are cubics.
- Prefer the configured ordinary grid where useful, while retaining exact arc
  junctions, diagonal geometry and documented optical corrections. There is no
  prescribed 45-degree angle restriction.
- Keep a connected contour connected when that preserves its stroke joins and
  makes the intended shape easier to edit.

## Retrieve references instead of loading the whole corpus

Use the local Lucide bundle at `references/lucide/`. Its original 24px canvases
remain unchanged reference evidence. They do not set the output/review size:
use the selected profile's configured native dimensions.

The bundle contains:

- `original/<name>.svg`: authoritative reference appearance and SVG structure.
- `atomic-debug/<name>.svg`: generated colored segments for inspecting geometry.
- `index.json`: searchable corpus metadata.
- `PROVENANCE.md` and `LICENSE`: origin, generation notes and attribution.

From the repository root:

```bash
python3 core/lucide_reference.py search 'cloud' --limit 6
python3 core/lucide_reference.py inspect cloud
python3 core/lucide_reference.py inspect cloud --json
```

Search the subject and, when helpful, a construction family such as an enclosure,
handle or attachment. Inspect the relevant original and debug pair and use the
inspector for exact geometry. Choose only references that answer a real design
question; there is no required reference count and no need to ingest the corpus.

The supplied brief/prototype establishes meaning. Lucide references establish
useful construction examples, not permission to substitute a different subject
or introduce unrequested features. Recompose for this repository's declared
profile rather than copying an entire foreign-grid drawing into the output.

Record choices in `sourceAnalysis.lucideReferences`, with each reference's name,
selection reason, and the construction principles applied. Record a missing
useful match honestly rather than inventing one.

Debug segmentation is a generated analysis, not proof of the original designer's
thought process: a native circle is split into four arcs, while a large source
arc may stay whole. Colors identify local segments, not universal categories.
Keep original grouping and closure information when it matters. Aggregate
frequency summaries are advisory defaults, never angle/radius restrictions,
reuse requirements or a target number of elements.

## Legacy compatibility

Older documents with `instances` and `shapeId` remain compatibility inputs.
`core/shape_registry.py` and its retained compatibility fixtures belong to the
legacy path, not the new authoring workflow. Do not add named
subject outlines or regenerate shape assets to make a new icon. Migrate a legacy
document by resolving its actual geometry into editable elements, retaining
meaningful grouping and evidence, then verifying visual parity before redesign.
Do not mix a legacy instance list and canonical elements as competing sources of
truth in one new document.
