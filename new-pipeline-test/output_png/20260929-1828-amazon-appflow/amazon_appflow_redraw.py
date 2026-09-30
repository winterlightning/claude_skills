"""amazon-appflow (redraw of the new-pipeline traced SVG).

Plan: two hollow rounded-square app nodes (upper left, lower right) joined by
two bent flow arrows (right-then-down in the upper right, left-then-up in the
lower left), on SQUARE (centerline box (6,6)-(42,42)). The whole drawing has
half-turn symmetry about (24,24): the lower-right node and the lower-left
arrow are the upper-left node and upper-right arrow rotated 180 degrees.
- node: closed contour, 12 x 12 on centerlines with r3 corners (inner hole
  8 x 8). Upper-left node (6,6)-(18,18) sets the left and top extremes; its
  rotation (30,30)-(42,42) sets the right and bottom.
- arrow: a straight run along y=6 from (26,6), a tangent r4 quarter arc
  about (34,10) turning down, a shaft at x=38 to the tip (38,22) and a
  90-degree chevron head with half-width 4 ending at (34,18) / (42,18).
  The tail sits 8 right of the node, the tip 8 above the other node; the
  inner wing end stays ~8.9 from the arc so the head does not crowd the bend.
  The shaft lands right of the target node's centre, as in the image.
Traced shape: 20260929-1828-amazon-appflow/amazon-appflow_raw.svg (read for
the subject only; nothing copied from its coordinates).
Lucide: square + corner-down-right / corner-up-left informed the construction
(rounded square nodes; a straight run turned by a quarter arc into a shaft
ending in a chevron head).

Metric issues:
- clearance e0/e3 (arrow tail 4.2 from the upper node): fixed, 8.
- clearance e0/e4, e0/e5, e0/e6 (lower arrow head 4 below the upper node):
  fixed, tip 8 below it.
- clearance e1/e7, e2/e7, e3/e7 (upper arrow head 4 above the lower node):
  fixed, tip 8 above it.
- clearance e4/e7 (lower arrow tail 4.6 from the lower node): fixed, 8.
- stroke-count (8 strokes, budget 6): fixed, 6 parts (2 nodes, 2 arrow
  bodies, 2 heads, each head joined to its shaft).
- stroke-width (info): drawn at stroke 4; every gap budgeted for 4.
Nodes shrink from the image's ~16 to 12 so both arrows and all 8-unit gaps
fit in the 36-unit box.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a73e4821-31f4-57d4-a0bb-b281fc0c8840"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1828-amazon-appflow/"
    "amazon-appflow_raw.svg"
)
AUTHOR = "claude-opus-5-5"

LO, HI = 6, 42              # centerline box
NODE = 12                   # node side on centerlines
NODE_R = 3                  # node corner radius
GAP = 8                     # centerline clearance
RUN_Y = LO                  # arrow run
SHAFT_X = 38
BEND_R = 4
HEAD = 4                    # chevron half-width / depth


def _rot(p):
    """Half turn about (24,24)."""
    return (48 - p[0], 48 - p[1])


class AmazonAppflowRedraw(Solo48):
    icon_id = "amazon-appflow-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "apps"
    aliases = ("amazon-appflow", "appflow")
    keywords = ("amazon", "appflow", "aws", "data flow", "integration", "sync", "transfer")

    def _node(self, name, x0, y0, x1, y1):
        r = NODE_R
        self.add_line(f"{name}-top", (x0 + r, y0), (x1 - r, y0))
        self.add_arc(f"{name}-tr", (x1 - r, y0), (x1, y0 + r), radius_x=r)
        self.add_line(f"{name}-right", (x1, y0 + r), (x1, y1 - r))
        self.add_arc(f"{name}-br", (x1, y1 - r), (x1 - r, y1), radius_x=r)
        self.add_line(f"{name}-bottom", (x1 - r, y1), (x0 + r, y1))
        self.add_arc(f"{name}-bl", (x0 + r, y1), (x0, y1 - r), radius_x=r)
        self.add_line(f"{name}-left", (x0, y1 - r), (x0, y0 + r))
        self.add_arc(f"{name}-tl", (x0, y0 + r), (x0 + r, y0), radius_x=r)
        self.add_contour(name, *(f"{name}-{k}" for k in
                                 ("top", "tr", "right", "br", "bottom", "bl", "left", "tl")),
                         closed=True)

    def _arrow(self, name, t):
        tail = t((LO + NODE + GAP, RUN_Y))
        bend_a = t((SHAFT_X - BEND_R, RUN_Y))
        bend_b = t((SHAFT_X, RUN_Y + BEND_R))
        tip = t((SHAFT_X, HI - NODE - GAP))
        wing_in = t((SHAFT_X - HEAD, HI - NODE - GAP - HEAD))
        wing_out = t((SHAFT_X + HEAD, HI - NODE - GAP - HEAD))
        self.add_line(f"{name}-run", tail, bend_a)
        self.add_arc(f"{name}-bend", bend_a, bend_b, radius_x=BEND_R)
        self.add_line(f"{name}-shaft", bend_b, tip)
        self.add_contour(name, f"{name}-run", f"{name}-bend", f"{name}-shaft")
        self.add_polyline(f"{name}-head", wing_in, tip, wing_out)
        self.relate("connect", name, f"{name}-head")

    def build(self) -> None:
        self._node("node-a", LO, LO, LO + NODE, LO + NODE)
        self._node("node-b", HI - NODE, HI - NODE, HI, HI)
        self._arrow("flow-a", lambda p: p)
        self._arrow("flow-b", _rot)
