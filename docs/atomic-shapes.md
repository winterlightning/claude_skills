# Atomic Shapes

> **Compatibility:** [icon-rules.md](icon-rules.md) is authoritative for icon
> invariants and [`core/icon_profiles.json`](../core/icon_profiles.json) owns
> profile geometry. The legacy `s-curve` uses a cubic and is not valid for new
> icons; use `s-bend`. A `rounded-square` instance is valid only when its
> resolved radius is an allowed token.

**Atomic Shapes are the reusable implementation layer, not a limit on icon
design.** Start with the strongest natural, immediately recognizable silhouette.
Reuse a current atom only when it expresses that form without visual compromise;
otherwise create and register a new generic parametric atom. A new atom is a
normal authoring outcome, even for one icon. Never accept an awkward contour,
forced proportions, excess pieces, or a less convincing icon merely to avoid a
registry change.

The final editable source is still an ordered composition of registered atoms so
geometry remains reusable, testable, and re-emittable. This quality-first rule
authorizes extending the registry; it does not authorize patching flattened output
paths or storing unregistered bespoke geometry only inside one finished SVG.

```
Level 0  ATOMIC SHAPES   the 68 primitives (this document)
Level 1  INSTANCES       an atom placed on the canvas: position, size,
                         rotation, flips
Level 2  ICONS           an ordered list of instances obeying the icon
                         rules (docs/icon-rules.md)
```

## The atomic contract

Every atom obeys the same contract, which is what makes icons consistent:

- **Parametric geometry.** An atom is a function `geometry(w, h)` returning a
  real SVG primitive drawn at actual size in a local `0..w × 0..h` box.
  `core/shape_registry.py` is authoritative; `frontend/js/shapes.js` is its
  browser mirror, guarded by registry tests.
- **Real size, never scaled.** Resizing an instance re-generates the
  geometry; atoms are never scaled with a transform. Only rigid operations
  (translate, rotate, flip) are applied as transforms.
- **Constant stroke.** Because geometry is real-size, stroke width never
  stretches or thins. The selected icon profile supplies the design and ship
  Regular strokes.
- **Edge-to-edge.** The geometry fills its `w × h` box exactly; the box IS
  the shape's footprint.
- **Paint-free.** Atoms define geometry only. Paint (stroke color, width,
  caps) is applied by the renderer according to the icon rules.

## Catalog (68 atoms)

Orientations listed are the un-rotated, un-flipped defaults; other
orientations come from `rotation` / `flipX` / `flipY` on the instance.

### Closed outlines (35)

| id | geometry in its box |
| --- | --- |
| `circle` | ellipse touching all four box edges (a circle when w = h) |
| `ellipse` | identical geometry to circle (palette convenience) |
| `square` | the full box |
| `rectangle` | identical to square (palette convenience) |
| `water-drop` | symmetric pointed teardrop made from four quadratic curves, with a sharp top cusp and rounded lower bowl. The default orientation points upward; rotation supports falling, sideways, and inverted drops without changing topology |
| `tapered-spire` | symmetric pointed shell made from two quadratic sides joined by one flat base. It reaches all four box edges, preserves a narrow central cusp without straight-angle constraints, and provides a reusable shoulder-free contour for spires, tapered towers, organic monuments, and pointed leaves |
| `rounded-square` | legacy: box with corner radius = 20% of the shorter side; new-grid output must resolve to radius 4u or 8u |
| `rounded-rectangle` | new-grid rectangle with the ordinary 4u corner token at every normal size. The radius clamps only when width or height is below 8u, keeping the atom bounded without changing its closed rounded-box topology. Use this for tall or wide rounded frames whose aspect ratio would make the legacy percentage-based `rounded-square` produce a non-token radius |
| `pill` | capsule: corner radius = half the shorter side. A wide box gives a horizontal capsule, a tall box a vertical one — no rotation needed |
| `triangle` | isoceles: apex top-center, base along the bottom edge |
| `right-triangle` | right angle at the bottom-left corner; hypotenuse top-left → bottom-right |
| `diamond` | rhombus with points at the middle of all four edges |
| `gable` | pentagon: a rectangular body under a peaked head. The head rise is w/2, so both roof edges sit at exactly 45° at every size, and the body runs from the springing line to the bottom edge. The pointed-head counterpart of the round-headed `arch`; when h ≤ w/2 the body vanishes and the outline is the triangle spanning the box |
| `twin-gable` | symmetric seven-sided closed shell for two adjoining equal gables with one shared central valley. Each half-span roof rises by `min(w/4, h)`, giving four 45° roof runs whenever the box is at least one quarter as tall as it is wide. The contour encodes only the reusable exterior; add a separate `line` when a central wall or seam is needed, avoiding the doubled shared wall produced by overlapping two `gable` atoms |
| `sloped-box` | asymmetric quadrilateral building shell with parallel walls, a horizontal base, and one roof edge fixed at exactly 15°; useful instances keep enough height for the short wall to remain |
| `trapezoid` | closed symmetric quadrilateral: a full-width base under a narrower flat top, both sides fixed at exactly 60° from horizontal at every size — the same on-grid guarantee `gable` gives its 45° roof and `sloped-box` its 15° one. The inset is `h / tan(60°)`, clamped to `w * 0.4` so the top edge can never collapse to a point and the whole size range stays valid. The flat-topped, two-sided counterpart of the one-sided `sloped-box` and the peaked `gable` — a flared roof, a lampshade, a hopper, a keystone, a slab in perspective. Default orientation is the wide base; `flipY` gives the hopper and `rotation` lays it on its side |
| `flared-horn` | closed flared tube with a narrow rear opening and a full-height bell, joined by gently curved quadratic sides. The default 24×16 orientation opens to the right; rotations and flips support other directions. A reusable silhouette for horns, speaker bells, funnels, and nozzles |
| `cut-corner-box` | pentagon: a rectangle with its top-left corner replaced by one straight run. The cut is `min(w, h) / 2` on both axes, so it sits at exactly 45° at every size and always fits inside the box. Unlike `sloped-box`, where the whole top edge slopes, the roof stays flat over the rest of the span — a box seen in profile with one corner chamfered, such as a vehicle cab, a cut-corner label, or a dog-eared document. The cut faces top-left; `flipX`, `flipY` and rotation reach the other three corners |
| `hexagon` | closed flat-top hexagon: a rectangle whose two ends are mitred to a point. The mitre inset is `min(h, w) / 2`, so all four slanted edges sit at exactly 45° whenever `w ≥ h` — the same on-grid guarantee `gable` gives its roof and `cut-corner-box` its corner — and the outline stays edge-to-edge in the box. The polygon-family companion to `triangle`, `square` and `diamond`: chips, badges, honeycomb cells, nuts, angular geometric bodies. At `w = h` the flats vanish and the outline is the diamond spanning the box, so the whole size range stays valid; useful instances keep `w ≥ h`, and `rotation: 90` gives the pointy-top form with vertical sides |
| `star` | closed five-point star: the classic rating or favourite outline. Outer vertices sit every 72° from the apex and the inner radius is `cos72° / cos36°`, so each pair of edges is collinear with one pentagram line and the notches stay at the canonical depth. The unit star is mapped onto the box, so the apex touches the top edge, the two upper arms the sides, and the two lower arms the bottom edge at every size; a non-square box gives the wide or tall variant and `rotation` tips the star. Unlike every other straight-edged atom its edges run at 18° and 54°, off the 15° direction grid, so an icon using it must carry a documented `off-angle` grid exception |
| `dome` | half-ellipse: flat side on the bottom, arch on top |
| `cloud` | symmetric multi-lobed cloud with a straight lower chord, parameterized across ordinary cloud aspect ratios using quadratic curves only |
| `scalloped-oval` | closed radially lobed oval: eight equal outward quadratic bulges around one continuous contour. Valleys sit on the 0.82 ellipse and each crest control radius is solved from the valley radius so the crest lands exactly on the ellipse; the crests fall on the four cardinals, so the contour touches all four box edges at every aspect ratio. The radially symmetric counterpart of `cloud`, which lobes only its upper half over a straight lower chord — brain hemispheres, blossoms, soft cogs, organic blobs. A non-square box gives the wide or tall variant and `rotation` offsets the lobe rhythm |
| `lens` | pointed oval: two equal circular arcs meeting at cusps on the ends of the horizontal axis, tips at the middle of the left and right edges and the arcs touching the top and bottom edges. One radius, `R = (w² + h²) / 4h`, serves both, so `h/w` alone sets the tip angle; at `h = w` the arcs are semicircles and the outline is exactly the circle in the same box, and past `h = w` they run more than half a turn and give a fat vertical oval with cusps on its sides. Doubly symmetric, so `flipX`/`flipY` are no-ops and `rotation` places it on any allowed direction |
| `lobed-drop` | closed asymmetric drop with a folded side lobe and inward notch, built only from quadratic curves and touching all four box edges. Its default orientation points upward; flips and rotation support flames, leaves, petals, and flowing-drop contours across useful portrait proportions |
| `stepped-cog` | sparse closed orthogonal cog with four broad cardinal teeth and four open corner cutaways. Every edge is horizontal or vertical; the reduced perimeter rhythm stays mechanical without becoming blocky or dense |
| `twin-lobed-drop` | closed symmetric double-lobed drop with a central cleft, built as one continuous quadratic contour. Useful for natural hearts, paired leaves, and crest-like silhouettes without doubled joints |
| `lightning-bolt` | closed upright six-vertex lightning silhouette. Its canonical 20×24 form uses exact 14u-by-14u and 12u-by-12u diagonal runs with axis-aligned steps between them, producing a compact energetic bolt without overlapping line fragments; useful instances retain the portrait aspect ratio |
| `puzzle-piece` | closed jigsaw-piece silhouette with one outward tab on the top and right sides and one inward socket on the bottom and left sides. Its canonical 20×20 form keeps every straight endpoint on whole units; eight quadratic quarter-lobes keep the contour smooth, cubic-free, and edge-to-edge |
| `phone-handset-outline` | closed diagonal telephone handset with two flared earpieces connected by a curved receiver body. The canonical 36×36 form keeps every straight endpoint on whole units and every exposed straight run horizontal, vertical, or at 45°, while quadratic shoulders preserve the recognizable handset topology without secondary phone detail |
| `quarter-circle` | corner wedge: right angle bottom-left, arc from top-left to bottom-right |
| `ring` | donut: outer ellipse + inner ellipse at 60% size (two concentric rims) |
| `pig-outline` | closed side-view pig silhouette with raised ear, blunt snout, belly, and two feet. It carries no bank slot, coin, or damage cue, leaving those semantic details composable |
| `broken-pig-outline` | two independently closed side-view pig halves separated by matching zigzag crack edges. The canonical 40×22 form uses parallel 45° crack runs with a 10u horizontal offset (7.07u perpendicular clearance) and scales proportionally into its instance box; use it when a genuinely split pig silhouette is required rather than drawing a crack over an intact `pig-outline` |
| `bottle-outline` | closed shouldered bottle for compact production and packaging scenes. Its canonical 14×20 form has an 8u neck, exact 45° shoulders, and 4u circular lower corners; preserve that aspect ratio when the shoulders carry the bottle identity |

### Open paths (33)

| id | geometry in its box |
| --- | --- |
| `dashed-rectangle` | broken rectangular perimeter with a fixed 4u dash / 4u gap rhythm carried as geometry rather than paint. The outline remains open as multiple subpaths, touches all four box edges, and can represent planned bounds, selection frames, or incomplete structures without changing stroke settings |
| `dot` | zero-length point-line centered in its box. The required round line cap supplies the visible disc, whose diameter equals the stroke width; this is the canonical small mark and is not a tiny outlined circle |
| `line` | horizontal line at mid-height |
| `diagonal-line` | bottom-left → top-right |
| `curve` | quadratic arch ∩: endpoints at the bottom corners, peak touching the top edge |
| `s-curve` | legacy-only cubic S-bend; prohibited in new-grid icons |
| `s-bend` | open continuous S contour made from two opposite-sweep quarter ellipses meeting tangentially at the box center. It runs from the top-left to bottom-right corners in the default orientation, remains edge-to-edge for any positive width and height, and uses arcs only; flips and rotation provide the other orientations. This is the new-grid replacement for the prohibited cubic `s-curve` |
| `arc` | half-ellipse arch ∩ (open — no closing chord): endpoints at the bottom corners, peak at the top edge |
| `quarter-arc` | open quarter-ellipse corner contour: leaves the top-left corner tangent to the top edge and arrives at the bottom-right corner tangent to the right edge, curving around a centre at the bottom-left. The open counterpart of `quarter-circle`; `flipX` / `flipY` / `rotation` reach the other three corners |
| `bulb-outline` | open symmetric globe contour that reaches the top and both side extrema before tapering to two neck endpoints at one-third and two-thirds of the bottom edge. Quadratic-only and designed to accept a separate socket without hidden or doubled geometry; useful for bulbs, lamps, and idea-light silhouettes across ordinary portrait proportions |
| `open-rectangle` | three sides of a rectangle drawn as one open contour, the fourth absent: up the left side, across the flat head, down the right side. The flat-headed counterpart of the round-headed `arch` and the open counterpart of `rectangle`; the opening faces down, `flipY` turns it over and `rotation` gives a side-opening channel |
| `arch` | open arch ∩ with straight sides: an elliptical head (rx = w/2, ry = min(w/2, h)) on two vertical jambs running from the springing line to the bottom edge. Opening faces down; `flipY` turns it over and `rotation` gives a side-opening arch. When h ≤ w/2 the jambs vanish and only the head remains |
| `hook` | open J-hook made from one long vertical attachment stem, one semicircular bowl of radius `w/2`, and one short opposing return tip. The default stem is on the left; `flipX` moves it to the right for a cable-hung lifting hook. Portrait instances with `h ≥ w` preserve the full edge-to-edge contour, while rotation provides horizontal hook orientations |
| `faucet` | minimal wall faucet combining a horizontal inlet, one quarter-ellipse elbow, a downward outlet, and a T-handle as open subpaths. Default flow direction is downward at the right edge; flips and rotation provide opposite wall and outlet orientations |
| `open-end-wrench` | horizontal ring-handle wrench with a straight shaft and two exact 45-degree jaw arms opening to the right. Useful instances keep `w ≥ 1.5h`; rotation aims the jaw toward a repair target while preserving constant stroke |
| `open-gable` | open gable ∧ with straight sides: a peaked head (rise = min(w/2, h), so both roof edges sit at exactly 45° whenever the box is at least half as tall as it is wide) on two vertical walls running from the springing line to the bottom edge. `gable` with its base absent — the pointed-head counterpart of the round-headed `arch` and the flat-headed `open-rectangle`, and the open counterpart of `gable`. Use it wherever the bottom edge is drawn separately or interrupted, such as a shell whose ground line is broken by a doorway. Opening faces down; `flipY` turns it over and `rotation` gives a side-opening channel. When h ≤ w/2 the walls vanish and only the peak remains |
| `head-profile` | open human head seen in profile, facing right, drawn as one continuous contour: the back of the neck, up the back of the skull, over the crown, down the forehead, out to the nose, in at the lip, out at the chin, then down the front of the neck. It touches all four box edges — skull left, crown top, nose tip right, both neck ends bottom — and the bottom stays open between them so a shoulder, collar, or frame is drawn separately. Built from quadratics only, so it never emits a straight segment and can never leave the 15° angle grid at any size. `flipX` faces it left |
| `worker-profile` | open side-view worker made from a separate circular head and one walking body contour with torso, extended arm, and two legs. Quadratic-only body geometry keeps the reusable pose cubic-free across tall portrait proportions |
| `worker-profile-solid` | compact 12×24 sibling of `worker-profile` for small repeated workers. It keeps the same proportional quadratic torso, arm, and leg contours, but replaces the outlined head with one zero-length point at the same centre; the required round cap turns the normal 4u stroke into a solid 4u head without an enclosed hole |
| `holding-hand` | open side-view hand contour with two broad gripping finger lobes, a palm return, and a deliberate wrist gap. It uses only lines, arcs, and one quadratic sweep, touches all four box edges, and is intended for hands holding cards, tools, or compact objects without encoding the held object itself |
| `transfer-hand` | compact open 20×12 transfer palm with a wrist gap, one thumb rise, and a broad fingertip block. It is the small-size hand alternative for giving, receiving, and dropping gestures where the larger finger-lobed hand atoms become dense at 24px |
| `radial-ticks` | twelve evenly spaced radial ticks drawn as open subpaths, each running from the 0.8 inner ellipse out to the box edge. Every tick sits on a 30° ray, so the ring stays on the 15° grid at any size, and the inner endpoints land exactly on the 0.8 ellipse — a `circle` rim drawn in the same 0.8 box meets them at their endpoints without doubled paint. The repeated-radial-mark counterpart of the single `line`: cog and gear teeth, dial and gauge ticks, compass rose, sun rays, spinner segments. A non-square box gives the elliptical variant and `rotation` offsets the whole ring |
| `open-twin-gable` | `twin-gable` with its base removed: one open two-peak zigzag. The rise is min(w/4, h), so all four flanks sit at exactly 45° and the contour stays on the 15° grid at any size; when the box is taller than that rise the two end stems drop to the bottom edge, so the box is still filled. The two-peak counterpart of `open-gable` and the open counterpart of `twin-gable`. Use it wherever a repeated peaked edge is a contour rather than a silhouette — a cracked shell or broken edge, a comb or crest, a frill, a sawtooth or signal trace. `flipY` turns the peaks into notches and `rotation` gives a vertical serration |
| `spiral` | one open contour that winds inward: five 90° arcs, each radius 0.86 of the one before, with every centre placed on the shared normal at the junction so the contour is tangent-continuous rather than a chain of separate arcs. Every junction lands on a multiple of 90°, so each arc's extremes are its own endpoints and the contour fills its box exactly. The winding counterpart of the constant-radius `arc` and `quarter-arc`, and the open, single-contour counterpart of `ring`: shells, snails, ferns, volutes, whirls, spinners. A non-square box gives the elliptical variant; rotation and the flips choose where the mouth opens |
| `gapped-rounded-rectangle` | the closed `rounded-rectangle` broken in the middle of its head: one open contour running clockwise from the gap's right lip, around all four ordinary 4u corners, and back to the gap's left lip. The gap is exactly half the box width, so the two head runs stay equal and the opening stays centred at every size — the same fixed-ratio guarantee `ring` gives its 60% inner rim and `radial-ticks` its 0.8 inner ellipse — and the corner radius clamps to the head run and half-height so those runs can never invert on a short or narrow box. Every corner and side it keeps lands on the closed `rounded-rectangle` of the same box, so the two read as one family. Use it wherever a frame is interrupted by a part that seats in the break rather than crossing it — a clipboard clip, a tab or handle, a labelled panel, a gated enclosure — instead of drawing the whole frame and then hiding the crossing under another atom. `flipY` moves the gap to the foot and `rotation` puts it on either side |
| `corner-gapped-rounded-rectangle` | an open rounded frame with its lower-left corner and adjacent side runs removed. The cutout lets a foreground object cross a card, panel, or enclosure without doubled hidden strokes; flips and rigid rotations move the cutout to another corner |
| `open-shell` | two asymmetric quadratic shell lips sharing a left hinge and opening on the right; add a separate circle for a pearl or a line for a hinge detail |
| `oyster-shell` | one continuous asymmetric oyster rim whose two endpoints form a compact right-facing mouth. Its broad outer bowl and folded upper lip avoid the eye silhouette produced by paired open arcs; add a separate circle in the mouth for a pearl and a short line near the hinge when needed |
| `side-gapped-rounded-rectangle` | rounded frame with a centred opening in its left wall, intended for an arm, connector, cable, or other foreground element entering a panel without a doubled crossing. The opening occupies the middle quarter of the height; flips and rotation move it to any side |
| `shark-fin` | open asymmetric fin contour with a long convex leading face, right-leaning apex, and short trailing edge; intended to terminate into a separate waterline |
| `wave-line` | two-cycle horizontal wave built from four tangent quadratic lobes; it fills its box without cubic geometry and provides a reusable water or signal rhythm |
| `gripping-hand` | open side-view palm contour with a separate broad finger wrap, leaving a clear tool-grip zone instead of encoding a held object |
| `gapped-eye` | quadratic eye outline with a broad lower-right contour cutout for a connected search handle or foreground tool; the remaining upper and lower contours keep the eye silhouette without a doubled crossing |

Open paths are pure strokes and can never be closed or filled. Closed
outlines are also rendered as strokes under the icon rules; "closed" only
describes their geometry.

## Where atoms live

| artifact | role |
| --- | --- |
| `frontend/js/shapes.js` | browser-side registry — `id`, `name`, `closed`, `natural` (thumbnail size), `defaultW/H` (drop size), `geometry(w, h)` |
| `core/shape_registry.py` | Python-side registry used by emission, validation, audits, asset generation, and tests |
| `assets/shapes/<id>.svg` | one standalone SVG per atom, generated by `python3 core/generate_assets.py`. Never edit these by hand |
| editor palette | built at runtime from the registry |

## Adding an atom

Adding to the atomic set is a normal API extension. Add an atom whenever it
materially improves the natural silhouette, recognition, or clean construction
over the available catalog. Recurrence is not required: one icon is enough when
the new geometry has a generic parametric contract rather than being a frozen
trace or whole icon. Do not force distortion, awkward seams, redundant overlaps,
or extra instances merely to reuse the current catalog.

1. Add the same entry to `SHAPES` in `frontend/js/shapes.js` and `core/shape_registry.py`: a `geometry(w, h)`
   function emitting real-size geometry, edge-to-edge in the box, geometry
   attributes only (no paint).
2. Follow the catalog conventions: pick the most useful default orientation
   (flat side down, right angle bottom-left, etc.) and document it here.
3. Confirm every renderer and validator resolves the updated registry. The Python
   path reads `core/shape_registry.py` directly; do not create a separate
   scarcity-oriented allowlist that would block newly registered atoms.
4. Teach `core/detect_svg_shapes.py` to classify the family when it can be
   recognized reliably, and cover it in `core/test_detect_svg_shapes.py`.
5. Run `python3 core/generate_assets.py` to regenerate the asset files, and
   `python3 -m unittest discover -s core -p 'test_*.py'` to check the new geometry.
6. Update this catalog and its counts.
7. Reload the editor — the palette picks it up automatically.
