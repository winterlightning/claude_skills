"""brain-circuit (redraw of the new-pipeline traced SVG).

Plan: a frontal two-lobed brain on CIRCLE (centerline radius 20 about
(24,24)), mirrored about x=24, with one angular circuit trace per hemisphere.
- outline: one closed contour.  Each half has three lobes (top, side, bottom)
  separated by small notches; the top lobes meet in a shallow cleft at
  (24,10) and the bottom lobes meet at (24,40).  The side lobe's extreme
  (4,24) / (44,24) touches the keyshape radius.
- fissure: a short divider from the top cleft (24,10) down to (24,14), so
  the lower middle stays open for the traces.
- traces: in each hemisphere a node at (15,22) / (33,22), a drop to y=28, a
  step in to x=19 / x=29 and a drop to y=32 (the generated image's Z trace).
  Nodes are r2 rings, which paint as solid pads of ink diameter 8.
Validation: validate_icon() valid, zero warnings.
Construction reference: lucide/brain-circuit (lobed half outline, straight
circuit runs ending in round nodes); coordinates rebuilt on the 48 grid, the
trace only supplied the subject and layout.

Metrics issues:
- clearance (14 errors: outline vs traces, outline vs nodes, trace vs node,
  node vs trace step): fixed.  The fissure is shortened, traces sit 8+ from the
  outline, the fissure and each other (the two lower runs 10 apart), and
  the node rings 8+ from everything they do not touch.
- stroke-count (9 strokes, budget 6): fixed, 6 strokes (outline, fissure, two
  traces, two nodes).
- stroke-width (trace 2.79 after fit): fixed by redrawing at stroke 4 with
  8-unit centerline gaps.
Not kept: the open-circle terminals.  An open ring needs r>=5 for a 6-unit
hole and so a 26-unit band between walls; each hemisphere is only ~20 wide,
so the terminals are drawn as solid r2 nodes (Lucide's dot terminals), and
the full-height divider of the image became a short top fissure.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "994c360d-a3ef-411d-83b6-1227713cc09e"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1657-brain-circuit/brain-circuit_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
CLEFT_Y = 10
BOTTOM_Y = 40         # bottom lobes meet here
FISSURE_BOTTOM = 14
NODE_R = 2
NODE = (15, 22)        # left node centre
STEP_Y = 28            # trace steps in towards the axis here
INNER_X = 19           # lower run of the trace
TRACE_END_Y = 32

# Left half of the outline, cleft -> bottom centre: (c1, c2, knot) cubics.
LEFT_OUTLINE = (
    ((23, 7), (20.5, 6), (17, 6)),         # top lobe up to its crown
    ((13, 6), (10, 9.5), (10, 13)),        # down into the upper notch
    ((7, 13.5), (4, 18), (4, 24)),         # side lobe out to the keyshape edge
    ((4, 28), (5.5, 32), (9, 34)),         # into the lower notch
    ((8.5, 38), (12, 41), (16, 41)),       # bottom lobe
    ((20, 41), (23, 41), (AXIS, BOTTOM_Y)),  # up to the bottom meeting point
)


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class BrainCircuitRedraw(Solo48):
    icon_id = "brain-circuit-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ("ai-brain", "neural-circuit")
    keywords = ("brain", "circuit", "ai", "artificial intelligence", "neural",
                "machine learning", "mind", "technology")

    def build(self) -> None:
        top = (AXIS, CLEFT_Y)
        left_ids, right_ids = [], []
        start = top
        for i, (c1, c2, knot) in enumerate(LEFT_OUTLINE):
            self.add_bezier(f"left-{i}", start, (c1, c2, knot))
            left_ids.append(f"left-{i}")
            start = knot
        # Right half walked back from the bottom meeting point to the cleft.
        knots = [top] + [k for _, _, k in LEFT_OUTLINE]
        for i in reversed(range(len(LEFT_OUTLINE))):
            c1, c2, knot = LEFT_OUTLINE[i]
            self.add_bezier(f"right-{i}", mirror(knot),
                            (mirror(c2), mirror(c1), mirror(knots[i])))
            right_ids.append(f"right-{i}")
        self.add_contour("outline", *left_ids, *right_ids, closed=True)

        self.add_line("fissure", top, (AXIS, FISSURE_BOTTOM))
        self.relate("connect", "fissure", "outline")

        for side, flip in (("left", lambda p: p), ("right", mirror)):
            cx, cy = NODE
            a, b = flip((cx - NODE_R, cy)), flip((cx + NODE_R, cy))
            self.add_arc(f"node-{side}-a", a, b, radius_x=NODE_R)
            self.add_arc(f"node-{side}-b", b, a, radius_x=NODE_R)
            self.add_contour(f"node-{side}", f"node-{side}-a", f"node-{side}-b",
                             closed=True)
            self.add_polyline(
                f"trace-{side}",
                flip((cx, cy + NODE_R)), flip((cx, STEP_Y)),
                flip((INNER_X, STEP_Y)), flip((INNER_X, TRACE_END_Y)),
            )
            self.relate("connect", f"trace-{side}", f"node-{side}")
