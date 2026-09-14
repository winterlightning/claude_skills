# Symbol language (draft spec)

A readable, hierarchical description of an icon that decides everything decidable from the
source geometry at construction time: what the shapes are, how they group, what repeats, what is
symmetric, and where things connect. Later stages only place symbols and enforce grid rules on a
structure that already knows what must stay equal, aligned, or mirrored.

Status: implemented and switched on (2026-09-12); the pipeline's language step writes this tree by
default. Section 10 records what the implementation changed in the draft and the measured results.

## 1. Vocabulary

**Stroke.** One continuous drawn run. It may have several parts (line, curve, line) but it is one
stroke: one pen-down, one pen-up. Never split for the reader's convenience.

**Typed shape.** A stroke, or a closed loop, recognised as a parametric shape and stored by its
parameters instead of its parts: line, arc, curve, dot, circle, oval, square, rect,
rounded-end rect (stadium), trapezoid, polygon, each straight-sided one with a corner radius,
plus the patterns below. A closed chain of four lines and four arcs is stored as
`rect w h r`, not as eight parts. The full list with parameters and nodes is the table under
**Node**.

**Pattern.** A typed shape for a recurring drawing idiom that would otherwise be a long chain:
spiral (centre, turns, start radius, end radius, direction), wave (count, amplitude, wavelength),
zigzag, star (points, inner and outer radius), ring of N (a dot or shape repeated around a
circle). Patterns are recognised by generic geometric tests, never by icon name. A pattern keeps
its meaning through scaling: a spiral drawn smaller stays a spiral with fewer visible turns
rather than a heap of arcs that no longer fit the grid.

**Symbol.** The unit of the drawing. A symbol is one of:

- a **leaf**: one typed shape;
- a **composite**: child symbols plus the connections between them.

A leaf is created for every enclosed loop and for every detached run of strokes (touching nothing
else). Anything that touches a loop from outside is its own symbol, joined to the loop by a
connection, not absorbed into it. Anything inside a loop (touching it or not) is a child of that
loop's composite.

**Node.** A named point on a symbol that other symbols can attach to. Every typed shape exposes a
fixed vocabulary; composites expose their bounding box nodes plus any node they re-export from a
child by name.

| shape | parameters | nodes |
|---|---|---|
| line | from, to | `start`, `end`, `at(p)` for p in 0..100 percent of length |
| arc | radius, sweep, from, to | `start`, `end`, `at(p)`, `mid` |
| curve | from, to, bulge or handles | `start`, `end`, `at(p)` |
| dot | position | `center` |
| circle | radius | `at(angle)`, `center` |
| oval (ellipse) | rx, ry, angle | `at(angle)`, `center`, `top`, `bottom`, `left`, `right` (the four extremes) |
| square | side, corner radius r (0 = sharp) | `top(p)`, `bottom(p)`, `left(p)`, `right(p)` at p percent along that edge; `corner(tl\|tr\|br\|bl)`; `center` |
| rect | w, h, corner radius r (0 = sharp) | same as square |
| rounded-end rect (stadium / capsule) | w, h; the short sides are full semicircles | `top(p)`, `bottom(p)` on the straight edges; `left(angle)`, `right(angle)` on the round ends; `center` |
| trapezoid | top width, bottom width, height, corner radius r (0 = sharp) | `top(p)`, `bottom(p)`, `left(p)`, `right(p)` (p along the slanted side); `corner(tl\|tr\|br\|bl)`; `center` |
| polygon (triangle, hexagon, ...) | vertices, per-corner radius | `edge(i, p)`, `corner(i)`, `center` |
| spiral | center, turns, r_outer, r_inner, direction | `outer` (start of the outermost turn), `inner`, `center` |
| wave | count, amplitude, wavelength, from | `start`, `end`, `crest(i)`, `trough(i)` |
| ring of N | radius, count, member definition | `member(i)`, `center` |
| any composite | children, connections, attributes | `box.top(p)` etc. on its bounding box; re-exported child nodes as `child.node` |

Square is its own type, not a rect that happens to be square: a square must stay square when
the icon is stretched, and the type is what tells the rule so. The same goes for circle versus
oval, and for rounded-end rect versus rounded rect: a stadium's ends are always full semicircles,
so it has one fewer parameter and its round ends expose angle nodes like a circle. A trapezoid
with rounded corners is a trapezoid with r > 0, exactly as a rounded rect is a rect with r > 0;
the corner radius is a parameter on every straight-sided shape, not a separate type.

**Connection.** An explicit statement that two nodes are the same grid point:
`stick.start = swirl.outer`. Connections are listed by the composite that owns both sides. The
interpreter resolves a connection to one integer point shared exactly by both symbols. A
connection is never implied by proximity after this stage; if it is not written, the strokes are
not joined and the gap rule applies between them.

**Instance.** A symbol defined once and placed several times. The definition holds the shape; each
instance holds only what differs: `at` (position of its centre or anchor), and optionally `scale`
and `mirror`. Editing the definition changes every instance.

**Series.** Instances placed at regular spacing: `count`, `step` (dx, dy). A series is one thing
to a stretch rule: it can be respaced or shortened, never made uneven.

**Group sign.** A tag shared by symbols that must be treated together even when they are not
instances of one definition (two wheels of different size, three bars of different height):
`group: "wheels"`. Rules that resize or move one member must move all members the same way.

**Symmetry.** A per-symbol attribute, detected when the language is built:
`symmetry: {axis: "vertical"|"horizontal", position: <relative to the symbol box>}`. Only the
strokes on one side of the axis are stored; the other side is generated at construction. A shape
that straddles the axis is stored once with the axis passing through it. The root (the icon) is a
composite like any other and may carry its own symmetry. Because the mirror half is generated,
no later stage can make a symmetric symbol asymmetric, and no separate guard is needed.

## 2. Levels and ownership

The tree has as many levels as the drawing has: a building contains a row of windows (a series)
whose window (a definition) contains two panes (children). Each level stores only what it owns:

- the window's panes are stored once, in the window;
- the row's spacing is stored in the series, not in each window;
- the building's symmetry is stored in the building.

Rules act at the level that owns the fact. Gap between two mugs is the root's business; gap
between a handle and its body is the mug's. Stretching the icon moves mugs; it never moves a
handle on its own.

## 3. Sizes and positions

Sizes are written in grid cells of the 48 grid (radius 8, width 20). Positions inside a
composite are relative to the composite's box, in cells. The root's box is the keyshape box.
Percentages appear only in node names (`right(30)`), never as coordinates. Fitting the drawing
into the keyshape scales the root; children scale with their parent unless the parent says
`rigid: true` (a circle radius that must stay round, a fixed corner radius).

## 4. Construction procedure (deterministic, generic)

1. **Identify** strokes as today.
2. **Type** each stroke or loop: try typed shapes and patterns by generic geometric tests, keep
   the most specific that reproduces the source within one cell.
3. **Nest**: loops and detached runs become leaves; enclosed things become children; touching
   outside things become siblings with a connection. Repeat upward until one root.
4. **Sign** at every level, bottom up: identical children (within tolerance) become instances
   of one definition; evenly spaced instances become a series; similar-but-scaled children get
   a group sign; a mirror-symmetric composite stores one half and its axis.
5. **Write** the tree. This is the file the page links as "Primitive language".
6. **Construct** on the grid: place the root in the keyshape box, resolve sizes to integers,
   generate mirrored halves and instances, resolve connections to shared integer points.
7. **Place and space**: rules that move whole symbols to satisfy gap and box, respace series,
   and never touch what a sign says must stay equal. This replaces the current search.

## 5. File format

```json
{
  "version": "symbol-language/1",
  "keyshape": "portrait",
  "definitions": {
    "window": {
      "type": "composite",
      "box": [8, 10],
      "symmetry": {"axis": "vertical"},
      "children": {
        "frame": {"type": "rect", "w": 8, "h": 10},
        "bar":   {"type": "line", "from": "frame.left(50)", "to": "frame.center", "direction": "horizontal"}
      }
    }
  },
  "root": {
    "type": "composite",
    "symmetry": {"axis": "vertical"},
    "children": {
      "house": {"type": "rect", "w": 36, "h": 28, "r": 4, "at": [24, 30]},
      "windows": {"instance": "window", "series": {"count": 3, "step": [12, 0]}, "at": [8, 26], "parent": "house"}
    },
    "connections": [
      ["windows[*].frame.bottom(50)", "house.top(*)"]
    ]
  }
}
```

Every key is a plain word; every number is cells or a percent along a node. A person can change
`"count": 3` to `2`, or `"r": 4` to `8`, and know exactly what will happen.

## 6. Worked examples

### Lollipop (source: swirl-lollipop-candy, survey icon 1)

Identification finds three strokes: an arc, a chain of line + curve + line, and a chain of four
arcs. Typing recognises the four arcs as one spiral, the line+curve+line as one stick with a
rounded end, and the lone arc as the part of the outer turn that continues past the stick.

```json
{
  "version": "symbol-language/1",
  "keyshape": "portrait",
  "root": {
    "type": "composite",
    "children": {
      "swirl": {"type": "spiral", "center": [26, 16], "turns": 1.5, "r_outer": 12, "r_inner": 3, "direction": "cw"},
      "stick": {"type": "line", "from": [20, 26], "to": [6, 44], "cap": "round"}
    },
    "connections": [["stick.start", "swirl.outer"]]
  }
}
```

Two symbols, one connection, no coordinates that depend on each other. Scaling the icon scales the
spiral as a spiral; the stick's start stays on the spiral's outer turn because the connection says
so. Compare the current language for the same icon: fourteen primitives, each endpoint a nested
percent expression, the join hidden inside `start: {on: "s3.0", at: "start"}`.

### Mug with a handle

```json
{
  "root": {
    "type": "composite",
    "children": {
      "mug": {
        "type": "composite",
        "children": {
          "body":   {"type": "rect", "w": 24, "h": 28, "r": 4, "at": [18, 26]},
          "handle": {"type": "arc", "r": 8, "sweep": "cw", "from": "body.right(25)", "to": "body.right(75)"},
          "steam":  {"type": "curve", "instance": "wisp", "series": {"count": 2, "step": [8, 0]}, "at": [12, 4]}
        },
        "connections": [["handle.start", "body.right(25)"], ["handle.end", "body.right(75)"]]
      }
    }
  },
  "definitions": {"wisp": {"type": "curve", "from": [0, 8], "to": [0, 0], "bulge": 2}}
}
```

The handle is its own symbol because it touches the loop from outside. The steam wisps are inside
the icon's box but touch nothing, so they are detached symbols; because they are identical and
evenly spaced they are a series of one definition. Moving the mug moves the handle; respacing the
steam respaces both wisps together; making the body wider does not change the handle radius.

### Building with a row of windows

See the format example in section 5: one `window` definition with its own vertical symmetry, a
series of three placed on the house, and one connection rule written once for the whole series.
Stretching the house wider can widen the series step; it cannot make one window wider than another.

## 7. What this replaces and what it keeps

Keeps: identification, the gridicon rules and validator, the review page, the survey.

Replaces: `language_extract.py` (writes the tree instead of the flat list), `language.py`
(interprets the tree), and the stretch/refine search (rules on symbols). The first implementation
can be a reader that converts the tree into the current flat language, so construct, validate and
select run unchanged while the new format proves itself on the survey.

## 8. Open decisions

1. Diagonal and rotational symmetry: not in version 1.
2. Pattern catalogue for version 1: spiral, wave, ring of N. Zigzag and star added when the survey
   shows them often enough to matter.
3. Whether a stroke that touches a loop at both ends and encloses nothing (the handle) can ever
   be merged into the loop's type: no, it stays a sibling.

## 9. Plan

Ground truth first, engine second. The twenty icons of `benchmarks/primitive-language/all-60`
(indices 1 to 20) are written by hand in the symbol language before any extractor exists; the
extractor is then measured by how many of the twenty it reproduces.

| phase | deliverable | files | done when |
|---|---|---|---|
| 0 | Hand-authored trees for icons 1 to 20, simplest first (slash, concentric circles, dice, clock, power, building, heart, nested squares, pin, gear, lollipop, paperclip, U arrow, links, profile, thumbs up, glove, table, disco ball, leaf) | `benchmarks/primitive-language/symbols/NN.symbols.json` | every icon expressible without escaping the spec; spec amended where it is not |
| 1 | Reader: symbol tree to the current flat language (`primitive-language/1`): schema check, expand instances, series and mirrored halves, resolve connections into attachments | `pictoshape/symbols.py`, `tests/test_symbols_reader.py` | all twenty build through `run_icon(frozen_language=reader(tree))` and a review page shows source next to construct output |
| 2 | Typing and patterns from identified geometry: square, rect, stadium, trapezoid, polygon, oval, spiral, wave, ring of N, by generic tests | `pictoshape/symbol_types.py`, tests per shape | each typed shape reproduces its source within one cell on the twenty and on the frozen 60 |
| 3 | Extractor v2: nest (loops, enclosure, touching siblings), sign (instances, series, groups, symmetry), write the tree | `pictoshape/symbols_extract.py` | structural match against the twenty hand trees, reported per icon; the language step of `run_icon` can emit the tree |
| 4 | Placement rules on symbols replacing the stretch and refine search: scale root to keyshape, move whole symbols for gap, respace series, generated symmetry | `pictoshape/place.py` | frozen-60 and 1000-icon survey pass counts equal or better, no regression on the twenty, no icon over 5 s |
| 5 | Switch: language step emits the tree, page links show it, old extractor and search retired | `pictoshape/pipeline.py`, docs | AGENTS.md and README describe the tree as the language |

Phases 1 and 4 keep the validator, selector and review page unchanged. Phase 2 and 3 can run
in parallel with phase 1 once the twenty trees exist.

## 10. Implementation status and amendments (2026-09-12)

All five phases are implemented. Files: `pictoshape/symbols.py` (schema check, resolver, reader to
`primitive-language/1`), `pictoshape/symbol_types.py` (typing), `pictoshape/symbols_extract.py`
(extractor v2), `pictoshape/place.py` (placement rules), `pictoshape/pipeline.py` (switch). Review pages:
`benchmarks/primitive-language/symbols/index.html` (hand trees), `build.html` (hand trees through the
pipeline), `match.html` and `extracted/index.html` (extractor v2 against the hand trees), `compare60.html`
(the frozen sixty through the new pipeline), `api-1000/index.html` (the survey).

### Amendments to the draft, forced by the twenty

| where | amendment |
|---|---|
| §1 stroke | A stroke that is no typed shape is written as `{"type": "stroke", "from", "parts": [...], "closed"}`; parts are `line`, `arc` (`to`, `r`, `sweep`, `large`), `semicircle` (`to`, `sweep`) and `curve` (`to`, `c1`, `c2` or `bulge`). Each part's `to` may be a node reference. |
| §1 arc | `sweep` is "cw" when the arc bulges to the left of its travel direction on screen (SVG sweep flag 1); `large` marks a major arc. Arcs may also be written by `center`, `r`, `start`, `sweep_deg`. |
| §1 polygon | `closed: false` makes a polyline (the clock hands, the arrow head). A stroke made only of lines is typed as a polygon. |
| §1 spiral | Adds `start_at` (the outer point, so a connection lands on an integer) and `axis` (the angle where half turns change centre). Construction: the outer arc runs from the start to the axis, then semicircles alternate between two centres `d` apart with radii shrinking by `d`. |
| §1 wave | `from`, `to`, `count` (wavelengths, halves allowed), `amplitude`, `sweep` of the first bow. |
| §1 ring | `center`, `radius`, `count`, `start`, `member`; a member is written in a local frame (origin on the ring, +x outward, +y clockwise); a member stroke may end with `"to": "next"` to close the ring through its neighbour. |
| §1 rotation | Straight-sided shapes, stadiums and ovals take an `angle`; instances and composites take `rotate`. Needed by the paperclip and the leaf. |
| §1 nodes | Added `x(v)`, `y(v)` on lines (the point at that coordinate), `on(x, y)` on any shape (nearest outline point), `part(i).start/end/at(p)` on strokes, `outer`/`inner` on spirals, `member(i)` on rings, `name[i]` on series members. Circle nodes resolve to an exact lattice point of the circle when one lies within ten degrees; only such points make a legal meet. |
| §1 connection | A connection is verified, and its gap recorded, never fatal: an end that touches another symbol is written *as* that symbol's node (`"from": "swirl.outer"`), which is what makes the two resolve to one integer point. Two closed shapes touching is not a connection (the gap rule forbids it). |
| §1 symmetry | A shape that straddles the axis is stored once, whole; only its mirror twins on the other side are generated. The axis position is an integer. |
| §2 root | When one loop encloses everything else, that loop's composite is the root: `children.outline` is the loop, the rest are its contents. |
| §3 positions | Root children are written in 48-canvas centerline cells (as the worked lollipop does). A composite without `at`/`box` keeps its children in its parent's cells. |
| §4 typing | Plain shapes must reproduce their source within one cell; patterns (ring, spiral, wave) within 2.5 cells, because a pattern regularises a hand-drawn repeat that jitters. The ring order is the N with the smallest deviation, not the largest that passes. |
| §4 signing | Symmetry is detected first, then instances (same type, same shape, same run direction), then series (longest arithmetic progressions among the instances), then groups (same type and proportions, or the same width or height). |
| §4 extraction | Before typing: open runs that meet at a vertex where nothing else ends are joined into one stroke (one pen-down, one pen-up); curves are cut where another stroke meets or crosses them, so the crossing becomes a vertex that the resolver places on both symbols. |
| §4 placement | Fill scales the root into its keyshape (uniform first, then a bounded stretch of at most 1.35 of the residual; rigid types scale uniformly and only move) and nudges the last cell with a candidate search judged on the interpreter's construction; when rigid shapes cannot fill the natural keyshape the circle keyshape is used, as the old fit did. Separate moves unconnected siblings apart, or trims the smaller about its far point, or shrinks a child inside its loop (instances shrink through their definition). Reduce lowers a spiral's turns, respaces or shortens a series, and respaces a group of similarly sized members (R9). |
| §8 | Rotational symmetry of a closed run is covered by the ring pattern (the gear); diagonal symmetry stays out. |

### Measured (2026-09-12)

| check | result |
|---|---|
| hand trees (phase 0) | 20 of 20 written; every icon expressible with the amendments above |
| reader (phase 1) | all 20 build through `run_icon`; through the placement rules 17 of 20 pass selection (the building, the table and the disco ball keep gap violations that the source itself has) |
| typing (phase 2) | the frozen twenty and the additional forty type without failure; `tests/test_symbol_types.py` covers each shape and pattern |
| extractor (phase 3) | structural match 0.82 mean over the twenty, 13 exact; the rest differ where identification splits one run into several |
| placement (phase 4) | frozen sixty: **29 pass** (baseline 23 with hand corrections, 13 fully automatic); no regression among icons 1 to 20; four regressions among 21 to 60 (22, 27, 33, 40: gaps inside one stroke that no rule moves whole symbols to fix); slowest icon 4.1 s |
| survey (phase 4) | 1000-icon survey at a 5 s limit on an idle machine: **322 pass** (baseline 228 at 5 s, 326 without any limit); 512 needs-work, 84 timeouts, 53 unidentified, 29 errors (`benchmarks/primitive-language/symbols/api-1000/`). A first run that shared the machine with the test suite gave 295 passes with 265 timeouts (`api-1000-run1/`) |
| switch (phase 5) | `run_icon` writes the tree by default (`language.symbols`), reviews link `symbols.json`; `Overrides(symbol_language=False)` still runs the legacy flat extractor and the fit/stretch/refine search, which are kept for comparison rather than deleted |
