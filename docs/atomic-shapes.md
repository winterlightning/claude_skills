# Atomic Shapes

> **New-grid compatibility:** [icon-rules.md](icon-rules.md) is authoritative
> for the 48-unit design / 24px ship system. The registry described here is
> still the legacy implementation. In particular, `s-curve` uses a cubic and
> is not valid for new-grid icons, while `rounded-square` must migrate from a
> percentage radius to an explicit 4u or 8u radius. Do not use legacy generated
> atoms as proof of new-grid compliance until the renderer is migrated.

**Atomic Shapes are the lowest level of the system.** Every icon, no matter
how complex, is built exclusively by placing atoms — nothing is ever drawn
freehand, and no SVG path is ever written by hand. If a form cannot be built
from atoms, either the design is rethought or a new atom is added to the
registry (a deliberate, rare event — see "Adding an atom").

```
Level 0  ATOMIC SHAPES   the 47 primitives (this document)
Level 1  INSTANCES       an atom placed on the canvas: position, size,
                         rotation, flips
Level 2  ICONS           an ordered list of instances obeying the icon
                         rules (docs/icon-rules.md)
```

## The atomic contract

Every atom obeys the same contract, which is what makes icons consistent:

- **Parametric geometry.** An atom is a function `geometry(w, h)` returning a
  real SVG primitive drawn at actual size in a local `0..w × 0..h` box. It is
  kept in aligned browser and Python registries: `frontend/js/shapes.js` and `core/shape_registry.py` — the runtime sources of truth for
  the editor, the asset generator, and the compose script alike.
- **Real size, never scaled.** Resizing an instance re-generates the
  geometry; atoms are never scaled with a transform. Only rigid operations
  (translate, rotate, flip) are applied as transforms.
- **Constant stroke.** Because geometry is real-size, stroke width never
  stretches or thins. The new-grid Regular stroke is 4u in the 48-unit design
  source and 2px in the 24px ship export.
- **Edge-to-edge.** The geometry fills its `w × h` box exactly; the box IS
  the shape's footprint.
- **Paint-free.** Atoms define geometry only. Paint (stroke color, width,
  caps) is applied by the renderer according to the icon rules.

## Catalog (47 atoms)

Orientations listed are the un-rotated, un-flipped defaults; other
orientations come from `rotation` / `flipX` / `flipY` on the instance.

### Closed outlines (27)

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
| `cut-corner-box` | pentagon: a rectangle with its top-left corner replaced by one straight run. The cut is `min(w, h) / 2` on both axes, so it sits at exactly 45° at every size and always fits inside the box. Unlike `sloped-box`, where the whole top edge slopes, the roof stays flat over the rest of the span — a box seen in profile with one corner chamfered, such as a vehicle cab, a cut-corner label, or a dog-eared document. The cut faces top-left; `flipX`, `flipY` and rotation reach the other three corners |
| `hexagon` | closed flat-top hexagon: a rectangle whose two ends are mitred to a point. The mitre inset is `min(h, w) / 2`, so all four slanted edges sit at exactly 45° whenever `w ≥ h` — the same on-grid guarantee `gable` gives its roof and `cut-corner-box` its corner — and the outline stays edge-to-edge in the box. The polygon-family companion to `triangle`, `square` and `diamond`: chips, badges, honeycomb cells, nuts, angular geometric bodies. At `w = h` the flats vanish and the outline is the diamond spanning the box, so the whole size range stays valid; useful instances keep `w ≥ h`, and `rotation: 90` gives the pointy-top form with vertical sides |
| `dome` | half-ellipse: flat side on the bottom, arch on top |
| `cloud` | symmetric multi-lobed cloud with a straight lower chord, parameterized across ordinary cloud aspect ratios using quadratic curves only |
| `scalloped-oval` | closed radially lobed oval: eight equal outward quadratic bulges around one continuous contour. Valleys sit on the 0.82 ellipse and each crest control radius is solved from the valley radius so the crest lands exactly on the ellipse; the crests fall on the four cardinals, so the contour touches all four box edges at every aspect ratio. The radially symmetric counterpart of `cloud`, which lobes only its upper half over a straight lower chord — brain hemispheres, blossoms, soft cogs, organic blobs. A non-square box gives the wide or tall variant and `rotation` offsets the lobe rhythm |
| `lens` | pointed oval: two equal circular arcs meeting at cusps on the ends of the horizontal axis, tips at the middle of the left and right edges and the arcs touching the top and bottom edges. One radius, `R = (w² + h²) / 4h`, serves both, so `h/w` alone sets the tip angle; at `h = w` the arcs are semicircles and the outline is exactly the circle in the same box, and past `h = w` they run more than half a turn and give a fat vertical oval with cusps on its sides. Doubly symmetric, so `flipX`/`flipY` are no-ops and `rotation` places it on any allowed direction |
| `lobed-drop` | closed asymmetric drop with a folded side lobe and inward notch, built only from quadratic curves and touching all four box edges. Its default orientation points upward; flips and rotation support flames, leaves, petals, and flowing-drop contours across useful portrait proportions |
| `stepped-cog` | sparse closed orthogonal cog with four broad cardinal teeth and four open corner cutaways. Every edge is horizontal or vertical; the reduced perimeter rhythm stays mechanical without becoming blocky or dense |
| `twin-lobed-drop` | closed symmetric double-lobed drop with a central cleft, built as one continuous quadratic contour. Useful for natural hearts, paired leaves, and crest-like silhouettes without doubled joints |
| `quarter-circle` | corner wedge: right angle bottom-left, arc from top-left to bottom-right |
| `ring` | donut: outer ellipse + inner ellipse at 60% size (two concentric rims) |

### Open paths (20)

| id | geometry in its box |
| --- | --- |
| `dashed-rectangle` | broken rectangular perimeter with a fixed 4u dash / 4u gap rhythm carried as geometry rather than paint. The outline remains open as multiple subpaths, touches all four box edges, and can represent planned bounds, selection frames, or incomplete structures without changing stroke settings |
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
| `radial-ticks` | twelve evenly spaced radial ticks drawn as open subpaths, each running from the 0.8 inner ellipse out to the box edge. Every tick sits on a 30° ray, so the ring stays on the 15° grid at any size, and the inner endpoints land exactly on the 0.8 ellipse — a `circle` rim drawn in the same 0.8 box meets them at their endpoints without doubled paint. The repeated-radial-mark counterpart of the single `line`: cog and gear teeth, dial and gauge ticks, compass rose, sun rays, spinner segments. A non-square box gives the elliptical variant and `rotation` offsets the whole ring |
| `open-twin-gable` | `twin-gable` with its base removed: one open two-peak zigzag. The rise is min(w/4, h), so all four flanks sit at exactly 45° and the contour stays on the 15° grid at any size; when the box is taller than that rise the two end stems drop to the bottom edge, so the box is still filled. The two-peak counterpart of `open-gable` and the open counterpart of `twin-gable`. Use it wherever a repeated peaked edge is a contour rather than a silhouette — a cracked shell or broken edge, a comb or crest, a frill, a sawtooth or signal trace. `flipY` turns the peaks into notches and `rotation` gives a vertical serration |
| `spiral` | one open contour that winds inward: five 90° arcs, each radius 0.86 of the one before, with every centre placed on the shared normal at the junction so the contour is tangent-continuous rather than a chain of separate arcs. Every junction lands on a multiple of 90°, so each arc's extremes are its own endpoints and the contour fills its box exactly. The winding counterpart of the constant-radius `arc` and `quarter-arc`, and the open, single-contour counterpart of `ring`: shells, snails, ferns, volutes, whirls, spinners. A non-square box gives the elliptical variant; rotation and the flips choose where the mouth opens |
| `gapped-rounded-rectangle` | the closed `rounded-rectangle` broken in the middle of its head: one open contour running clockwise from the gap's right lip, around all four ordinary 4u corners, and back to the gap's left lip. The gap is exactly half the box width, so the two head runs stay equal and the opening stays centred at every size — the same fixed-ratio guarantee `ring` gives its 60% inner rim and `radial-ticks` its 0.8 inner ellipse — and the corner radius clamps to the head run and half-height so those runs can never invert on a short or narrow box. Every corner and side it keeps lands on the closed `rounded-rectangle` of the same box, so the two read as one family. Use it wherever a frame is interrupted by a part that seats in the break rather than crossing it — a clipboard clip, a tab or handle, a labelled panel, a gated enclosure — instead of drawing the whole frame and then hiding the crossing under another atom. `flipY` moves the gap to the foot and `rotation` puts it on either side |

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

Adding to the atomic set is an API change — do it only when an essential form
cannot be composed honestly from existing atoms. Recurrence is not required: a
single icon justifies an atom when every existing option would need extreme
distortion, several overlapping atoms to imitate one continuous contour, or a
change of topology. What makes it an atom is its generic parametric contract,
not how many icons already need it.

1. Add the same entry to `SHAPES` in `frontend/js/shapes.js` and `core/shape_registry.py`: a `geometry(w, h)`
   function emitting real-size geometry, edge-to-edge in the box, geometry
   attributes only (no paint).
2. Follow the catalog conventions: pick the most useful default orientation
   (flat side down, right angle bottom-left, etc.) and document it here.
3. Add the id to the renderer's allowed-id set and `geometry()` in
   `core/shape_registry.py` so every Python validation layer agrees on the catalog.
4. Teach `core/detect_svg_shapes.py` to classify the family when it can be
   recognized reliably, and cover it in `core/test_detect_svg_shapes.py`.
5. Run `python3 core/generate_assets.py` to regenerate the asset files, and
   `python3 -m unittest discover -s core -p 'test_*.py'` to check the new geometry.
6. Update this catalog and its counts.
7. Reload the editor — the palette picks it up automatically.
