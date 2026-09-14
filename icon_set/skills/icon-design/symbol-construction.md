# Symbol construction for Pictographic icons

Use this guide when constructing an icon from a brief or reference, or repairing
an existing icon. Decide what the drawing is made of before placing its points:
which shapes belong together, which dimensions repeat, which parts mirror, and
where parts actually join. Encode those decisions in the Python module so a
later spacing repair preserves the drawing's structure.

The source of a finished icon is a Python `Icon` subclass. Symbols described
here are authoring units represented by shared parameters, local helpers, named
points and contours. They do not introduce another runtime format. The supported
emission methods are documented in [geometry.md](geometry.md); the family skill
supplies the profile, output location and validation commands.

## 1. Vocabulary and what each term owns

**Stroke:** one continuous drawn run, from pen-down to pen-up. A stroke may
contain several lines and arcs. Keep it logically whole even when the Python
model represents it with multiple primitives. Use a contour when those members
must paint as one path with joins rather than separate round caps.

**Typed shape:** a recognizable geometric construction described by parameters.
A rounded rectangle is a width, height and corner radius, even though emission
requires several lines and arcs. Keep the parameters together so changing the
width does not accidentally change one corner or detach an edge.

**Pattern:** a repeated drawing idiom such as a spiral, wave, zigzag or ring of
marks. Its count, spacing and radii describe it more usefully than unrelated
endpoints. Recognize patterns from visible geometry, not the icon's filename.

**Symbol:** a logical unit that is either one shape/stroke (a leaf), or a group
of child symbols and their relationships (a composite). A composite may be
represented by a helper or a clearly separated block of parameterized code.
It need not become a new Python class.

**Node:** a named point used to construct or attach geometry. In this system a
node is a Python coordinate tuple, for example `handle_top = (body_right, y)`.
It is not a string that the geometry API resolves. An exported composition
anchor uses `add_anchor`; ordinary internal nodes can remain local variables.

**Connection:** an intentional join between actual emitted members. Both sides
reuse one integer point, and the relevant relationship is declared with
`relate("connect", ...)`. The declaration describes existing geometry; it does
not move endpoints into contact.

**Definition and instance:** a reusable shape construction and one placement of
it. The definition owns dimensions and geometry; the instance owns its origin
and unique element-ID prefix. Editing the definition changes every instance.

**Series:** instances with a count and constant step. The series owns spacing.
If three windows form a row, place them from one origin and step rather than
three unrelated x coordinates.

**Related group:** nonidentical parts that share a particular constraint. Two
wheels of different size can share a baseline and move with the vehicle while
keeping different radii. Share only the relationships that the subject needs.

**Symmetry:** a relationship that generates one part from another about an axis.
The owner stores the axis and the independent dimensions. The mirrored side is
derived from them, rather than maintained as another set of editable numbers.

## 2. Shape vocabulary and emission

These are conceptual constructions, not additional `Icon` methods. Choose the
most specific shape that preserves the subject. A square should remain square
when surrounding geometry changes; an oval must not become a circle merely
because circles are easier to author.

| Shape | Parameters to keep together | Useful internal nodes | Emit with |
|---|---|---|---|
| Line | start and end | start, end, an exact point along the run | `add_line` |
| Circular arc | endpoints, radius, sweep, major/minor choice | start, end, verified points on the arc | `add_arc` with equal radii |
| Elliptical arc | endpoints, x/y radii, sweep, major/minor choice | start, end, verified extrema | `add_arc` with separate radii |
| Dot | position; diameter is fixed by the stroke | center | `add_dot` |
| Circle | center, one radius | center and four axial extrema | Two semicircular arcs in a closed contour |
| Oval | center, x/y radii | center and four axial extrema for an unrotated oval | Elliptical arcs in a closed contour |
| Square | origin, one side, optional corner radius | corners, edge attachment points, center | Closed polyline, or lines/arcs in a closed contour |
| Rectangle | origin, width, height, optional corner radius | corners, edge attachment points, center | Closed polyline, or lines/arcs in a closed contour |
| Capsule | long dimension, short dimension, orientation | straight-edge endpoints, round-end extrema | Straight runs and semicircular ends |
| Trapezoid | top/bottom widths, height, optional corner radii | vertices and exact points on sloping edges | Polyline, or tangent lines/arcs |
| Polygon/polyline | ordered vertices, closure, optional corner radii | vertices and exact points on edges | `add_polyline`, or a mixed contour |
| Irregular stroke | ordered parts and shared junctions | start, end, junctions between parts | Lines/arcs collected into one contour |
| Spiral | outer extent, turn count, progression of radii, direction | outer end, inner end, turn junctions | A coherent arc construction |
| Wave | endpoints, amplitude, count, regular progression | endpoints, crests, troughs | Alternating tangent arc sections |
| Zigzag | amplitude, count, step | endpoints and repeated corners | Open polyline |
| Star | center, point count, alternating inner/outer vertices | tips and valleys | Closed polyline when integer geometry permits |
| Ring of members | center, radius, count, member construction | each member's origin and local attachment points | Repeated supported primitives |

A capsule's round ends are full semicircles: their radius is half the short
centerline dimension. A rounded rectangle has an independent corner radius.
Avoid giving a capsule a second, unrelated end-radius parameter. Corner radii
must fit their adjoining edges and preserve intended straight sections.

A circle cannot be emitted as one arc whose endpoints coincide. Construct two
halves or four quarters with coherent traversal, then close the contour. For
arcs, inspect the actual center and extrema: endpoints plus radius determine
the center, and an arc can bulge outside its endpoint box.

General Bézier curves and arbitrary rotated ellipses are not exposed by the
current authoring methods. Reconstruct a smooth feature with supported tangent
arcs when that preserves its identity. If it cannot be represented faithfully,
record the limitation. Do not insert unsupported SVG or fabricate API methods.

## 3. Nesting and ownership

Build the hierarchy from visible enclosure and actual subject structure:

1. Identify each closed loop and each detached stroke run.
2. Put enclosed details under the composite owning the surrounding loop.
3. Keep an externally attached part as a sibling of that loop under their
   common owner. A mug handle does not become a piece of the body rectangle.
4. Group the parts that must move together to remain one recognizable object.
5. Repeat until the icon has one root. If one outline encloses everything,
   the root owns that outline and its contents.

For example, a building owns an outline and a row of windows. The row owns its
spacing and instances; a window definition owns its frame and panes. Widening
the building may change the row's spacing, but must not widen only one window.
Moving the building moves its contents as well as its outline.

The closest common owner controls a relationship between siblings. The mug
controls its body/handle join. The root controls the clearance between the mug
and a detached steam series. Do not fix the root's gap problem by independently
moving a handle endpoint inside the mug.

Logical composites do not replace family routing. A body and handle are one
noun. A distinct status glyph inside a separate enclosure can be two independent
icons. Apply [reference-triage.md](reference-triage.md) before construction. For a
Pending component brief, plan only the named component even if the full source
shows other subjects.

## 4. Repetition, groups and symmetry

Look for symmetry first, then identical instances, regular series, and related
but nonidentical groups. This order helps avoid storing mirror twins as two
unrelated definitions or confusing a repeated row with independent objects.

### Symmetry

Choose vertical or horizontal symmetry only where the subject supports it.
A leaning trunk, perspective view or directional feature may need asymmetry.
State which parts mirror and which deliberately do not.

For a vertical integer axis `axis_x`, derive `x_right = 2 * axis_x - x_left`.
For a horizontal axis, derive y coordinates similarly. Share paired radii,
heights and clearances. A whole circle or outline crossing the axis is stored
once; do not emit that whole shape again as its own mirror.

Mirroring points alone is insufficient for curves. A reflection reverses arc
sweep if endpoint order is preserved. If traversal order is also reversed,
account for both operations. Verify contour continuity and arc bulge rather
than changing sweep flags until an image looks approximately right.

### Definitions and series

A helper takes the values that really differ per instance: usually an origin
and an ID prefix. Shape dimensions belong in the definition or shared parent
parameters. Use an index in every emitted member name to avoid duplicate IDs.

For a straight series, compute `origin_i = origin_0 + i * step`. Recompute all
origins when step or count changes. To center an even-count series, choose a
step that yields integer origins; do not round the two halves independently.
When a series is shortened, recenter or intentionally anchor it according to
its owner rather than leaving an accidental gap at one end.

A ring is the circular counterpart. Derive placements from a common center and
angular pattern, then choose integer geometry that preserves the intended
regularity. Arbitrary equal-angle placements may not lie on the integer grid.
Do not silently jitter members or break a shared join through independent
rounding; simplify the pattern or report the unresolved fit.

### Related groups

Use a group when members share alignment, movement or proportions without
being identical. A chart's bars may share width and baseline but have different
heights. Keep those heights independent; forcing all bars into one identical
instance definition would change the meaning.

Record exactly what is shared. “Move together” does not mean “all sizes equal,”
and “same radius” does not mean “same position.” During a repair, update the
owning parameter and derive the affected coordinates again.

## 5. Nodes, joins and crossings

Choose internal node names that express their role: `body_handle_top`,
`roof_apex`, `shaft_end`, or `window_center`. Compute them from the owner's
parameters. Avoid storing a second copy of a coordinate that must stay equal.

For a straight edge, a conceptual percentage attachment is useful during
planning, but emitted coordinates must be integers. If the midpoint of a span
is fractional, revise the span or choose a different legal attachment. Do not
pass percentages or node-name strings to the Python drawing methods.

For a curved receiver, an attachment must lie on the actual arc. A point near
the circle, or a projection rounded to the nearest integer, is not enough.
Choose a construction with an exact shared point and verify the resulting arc.

When another stroke joins the middle of a receiving run, split that run at the
join so the receiving members expose the same endpoint. Preserve the original
run's logical identity and contour traversal. Declare only the actual contact
pairs; do not relate every member of a large composite just to suppress gaps.

A crossing is not automatically a join. Determine whether the subject needs a
junction, an over/under crossing, or separate parts with clearance. Use the
existing relationship and validation rules in [geometry.md](geometry.md) and
[validation.md](validation.md). Never convert an unresolved collision into an
intentional join merely to obtain a passing report.

Two closed shapes touching must not be excused by a connection declaration.
Give distinct loops their required clearance, or redesign the actual topology
when the subject genuinely requires one joined outline. A zero-width gap is
not a substitute for an opening.

## 6. Coordinates, keyshape and spacing

The family determines the canvas: SUB32, SOLO48 or CONTAINER64. All emitted
coordinates use that family's final canvas space. A local helper can express
points relative to its own origin, but it must resolve them to integer tuples
before emission. Author each family separately; do not scale another family's
finished geometry or use scale transforms.

Choose the keyshape before solving individual points. Its dimensions describe
visible ink, while authoring coordinates describe stroke centerlines. With a
4-unit round stroke, a rectangular centerline box is inset 2 from each visible
edge. For a circle, the centerline radius is the visible radius minus 2.

### SOLO48 dimensions

The canvas is 48×48, centered at `(24, 24)`:

| Keyshape | Visible ink size | Visible bounds | Centerline bounds |
|---|---|---|---|
| `CIRCLE` | 44×44 | (2,2)–(46,46), tested radially | Radius 20 about (24,24) |
| `SQUARE` | 40×40 | (4,4)–(44,44) | (6,6)–(42,42) |
| `HRECT_L` | 44×36 | (2,6)–(46,42) | (4,8)–(44,40) |
| `VRECT_L` | 36×44 | (6,2)–(42,46) | (8,4)–(40,44) |

Other rectangle size suffixes remain compatibility names for the same
orientation envelope on SOLO48. Use the four choices above for new SOLO48
construction. Other families retain their own tables in
[keyshape-fitting.md](keyshape-fitting.md).

SOLO48 requires **4 units between ink edges**, equivalent to **8 units between
centerlines** for distinct 4-unit strokes. This is spacing between parts, not
an additional 4-unit canvas inset. A circle's radius and an opening's diameter
also need to be reasoned about as different measurements.

Parallel straight runs can be certified at the exact minimum. Curved pairs
need enough margin for the distance engine to certify them; a `review` finding
is not a pass. A connected pair is not a license to ignore nearby unrelated
parts or tight gaps elsewhere inside the same contour.

### Diagonal layout and exceptions

If the upright subject cannot fit recognizably, consider a diagonal layout.
Rotate the logical subject together, preserving its shared dimensions, joins
and internal relationships. Construct legal integer geometry; independently
rounding a transformed point cloud can break all three.

Diagonal placement still must satisfy the selected keyshape, canvas, stroke
and spacing checks. Do not rotate directional symbols when orientation carries
their meaning. Judge the new silhouette at native size before choosing it.

If no acceptable layout fits, retain the candidate and its validation findings
where the current workflow permits, describe the attempted layouts and the
remaining conflict, and use **Exception — manual review** (`exception`) in the
gallery's Flag selector for an available gallery icon. Record the reason in
feedback. The flag does not approve the icon, change review status, waive a
failed rule, or allow paint outside the canvas. If generation stops before a
candidate reaches the gallery, report that blocker rather than claim a flag
was saved. Custom envelopes follow the existing FREE proposal/approval process
in [keyshape-fitting.md](keyshape-fitting.md).

## 7. Construction procedure

1. **Inspect and reduce.** Render a supplied reference and establish the subject.
   Preserve its identity and source information. Keep the silhouette and the
   features that survive native size. For a text brief, design those features
   without claiming extraction from an image.
2. **Identify runs and loops.** Distinguish continuous strokes, detached runs,
   enclosed details, real junctions and crossings. Do not split a logical stroke
   merely because several API calls will be needed.
3. **Assign shapes and patterns.** Choose the most specific useful construction.
   Keep an irregular coherent stroke where a regular shape would distort it.
4. **Build ownership.** Establish the root, child groups and the owner of each
   attachment and gap. Complete semantic combination triage before authoring.
5. **Record constraints.** Note axes, shared dimensions, definitions, series,
   related groups and exact attachments in the module's plan.
6. **Solve the family layout.** Choose the keyshape, derive the centerline
   extremes, allocate room for internal details and gaps, then solve points.
7. **Emit geometry.** Expand helpers and repeats with unique IDs, reuse shared
   points, collect continuous members into contours, and declare true contacts.
8. **Validate and repair.** Use the family validation chain. Repair at the owner
   of the violated relationship and regenerate all affected coordinates.
9. **Inspect and hand off.** Inspect native-size output in both themes. Report
   validation, identity-preserving simplifications, intentional asymmetry and
   any unresolved exception. Preserve the parent when creating a fix variant.

The plan should be proportional to the drawing. One line is enough for a slash;
a building with repeated details needs explicit ownership and a repeat rule.
Do not create a separate formal schema or a verbose description of every point.

## 8. Worked constructions

The code fragments below demonstrate supported emission inside a `build()`
method. They are component examples, not complete approved icons: the family
module still needs its metadata, enclosing layout, validation and visual review.

### A circle stored as one shape

Plan: one circle; center and radius are the only independent dimensions. The
left/right extrema and the two arc halves derive from those values.

```python
cx, cy, radius = 24, 24, 20
left = (cx - radius, cy)
right = (cx + radius, cy)
self.add_arc("outline-top", left, right, radius_x=radius)
self.add_arc("outline-bottom", right, left, radius_x=radius)
self.add_contour("outline", "outline-top", "outline-bottom", closed=True)
```

This produces the SOLO48 circle centerline radius of 20 and visible radius of
22. The halves share their endpoints exactly. Changing the radius changes both
halves together. No mirrored duplicate of the whole circle is needed.

### A repeated row with one definition

Plan: three identical short marks, centered on the icon's vertical axis. The
mark owns its length; the series owns count, horizontal step and y position.

```python
count, step, axis_x = 3, 12, 24
half_length, center_y = 2, 24
span = (count - 1) * step
assert span % 2 == 0
first_x = axis_x - span // 2

for index in range(count):
    x = first_x + index * step
    self.add_line(
        f"mark-{index}",
        (x, center_y - half_length),
        (x, center_y + half_length),
    )
```

Changing count recomputes the centered series. Changing `half_length` changes
every mark. Changing step changes each inter-mark gap equally. These marks
alone do not fill a standard SOLO48 envelope; their owner must provide the
remaining subject geometry or follow the appropriate custom-envelope process.

### Mug body and attached handle

Plan the subject before solving its envelope:

```text
root
  mug
    body: rounded rectangle, owns width/height/corner radius
    handle: external arc, owns its radius
    joins: handle.start = body.handle_top
           handle.end   = body.handle_bottom
  steam: detached series, owns count/step and a shared wisp definition
```

The body and handle share an owner; steam is separate from the mug's physical
structure. Moving the mug moves its body and handle together. Moving the steam
series changes the mug/steam gap without detaching the handle.

This attachment fragment splits the body's right wall at two shared nodes:

```python
body_right = 28
handle_top = (body_right, 16)
handle_bottom = (body_right, 32)
self.add_line("wall-upper", (body_right, 8), handle_top)
self.add_line("wall-middle", handle_top, handle_bottom)
self.add_line("wall-lower", handle_bottom, (body_right, 40))
self.add_arc(
    "handle", handle_top, handle_bottom, radius_x=8, sweep=True,
)
for wall in ("wall-upper", "wall-middle", "wall-lower"):
    self.relate("connect", wall, "handle")
```

Every listed wall actually meets one or both handle endpoints. Complete the
body's remaining edges and corners in traversal order, then form its contour.
The fragment does not establish the final mug keyshape or steam clearance.
Widening the body moves `body_right` and both attachments together; preserving
the handle radius constrains how far apart its endpoints may be.

### Building and windows with nested ownership

```text
building root
  outline
  window row: origin, count, constant step
    window definition
      frame: shared width/height/corner radius
      panes: geometry relative to that frame
```

A row of three windows uses one definition three times. If each window has a
symmetric divider, derive its halves inside the window definition; the building
must not own six unrelated divider endpoints. A wider building can respace the
row while preserving each window. A narrower drawing may require fewer windows
or fewer panes, consistently across every instance.

At SOLO48, calculate whether frames, panes and all required gaps can coexist
before drawing them. If they cannot, remove a nonessential detail level or
shorten the row. Do not reduce the mandated spacing simply to keep the original
count. Name the simplification in the handoff.

### Lollipop with a spiral

Plan the head as one spiral pattern and the stick as one attached symbol under
their common owner. Store the outer extent, turn count, direction and progression
of arc radii together. Identify which visible point actually meets the stick;
reuse that exact point as the stick's endpoint.

An arbitrary chain of smaller arcs is not automatically a spiral. Check that
its turns progress inward consistently, join smoothly where required and leave
readable gaps between neighboring turns. When a small canvas cannot support the
source's turn count, reduce the pattern coherently while preserving its swirl
identity. Do not move one inner arc independently to conceal crowding.

A diagonal stick may improve the fit. It still shares its head attachment and
must remain inside the chosen envelope. If the source has a deliberate break,
retain that break with legal clearance rather than inventing a connection.

## 9. Placement and repair rules

Repair the smallest owner that controls the failed relationship. Keep the
existing ladder: enlarge the opening, rebalance, then remove a nonessential
part. Every change to paint requires rechecking the envelope.

| Problem | Owner to change | Preserve while repairing |
|---|---|---|
| Two separate objects crowd each other | Their common parent | Each object's internal joins and proportions |
| Detail crowds its enclosure | Enclosure composite | Detail identity, any true attachments, sufficient internal space |
| A repeated row is too dense | Series origin/step/count | Equal spacing and identical member geometry |
| Every repeated window is too dense internally | Window definition | All instances receive the same revision |
| A symmetric pair is unbalanced | Pair's axis/shared dimensions | Derived reflection and meaningful intentional asymmetry |
| Handle detaches after widening a body | Body/handle owner and shared nodes | Exact contacts and feasible handle geometry |
| Spiral turns collide | Pattern parameters | Consistent inward progression and smooth junctions |
| Gap inside one continuous stroke is too small | That stroke's construction | Recognizable topology and intended curve flow |
| No recognizable layout fits | Whole subject and review workflow | Honest validation findings and reason for exception |

Do not assume hierarchy fixes every gap. Two portions of the same contour can
crowd each other even when all sibling spacing is valid. Inspect interior holes,
turns, acute wedges and narrow necks as well as distances between objects.

Do not make a failed opening disappear by squeezing its boundary together.
Do not break repeat equality, drift a symmetry axis, or slide a join off its
receiver to make a local measurement pass. If a necessary change alters the
subject's meaning, retain the failure for review instead.

## 10. Validation and review evidence

The symbol plan explains intent; the emitted geometry is what validation and
rendering measure. Before reporting completion, check:

- Every authored coordinate and radius follows the selected profile's rules.
- The actual painted envelope satisfies the keyshape and canvas checks.
- Continuous contours are contiguous, correctly ordered and correctly closed.
- Shared nodes remain shared after edits; relationship declarations match real
  contacts and do not hide unrelated close pairs.
- Repeated definitions, series spacing and intended symmetry survived repairs.
- Clearances, internal openings and pattern detail remain readable at native
  size in both light and dark themes.
- Reported omissions, asymmetry, limitations and manual-review flags match the
  actual candidate; an unresolved finding is not described as a valid result.

Use [validation.md](validation.md) for the executable checks and
[authoring.md](authoring.md) for smoothness, reduction and optical judgment.
For feedback, follow the family skill's variant workflow and preserve the
existing icon. Edit the Python model and re-emit artifacts; never repair a final
SVG independently of its source.
