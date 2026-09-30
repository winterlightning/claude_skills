"""isometric-cube-with-three-circular-nodes (redraw of the new-pipeline traced SVG).

Plan: an isometric cube outline (three visible faces) whose upper-left,
upper-right and bottom vertices are replaced by hollow circular nodes, on
SQUARE (centerline box (6,6)-(42,42)), mirrored about x=24.
- nodes: three circles of radius 5 (the smallest radius with integer
  Pythagorean rim points (4,3)/(0,5), so every edge lands on the rim at an
  integer point). Left node (11,13) touches x=6, right node (37,13) touches
  x=42, bottom node (24,37) touches y=42; the top vertex (24,6) touches y=6.
- edges: every sloped edge runs 9 across and 4 down/up (one isometric slope
  for the top face, the inner Y and the base), vertical edges are 12 long
  (x=11, x=37 from y 18..30 and the centre stem 20..32).
- construction: each node is split into arcs at its attachment points; the
  outer silhouette (top edges, outer node arcs, sides, base) is one closed
  contour, the inner Y (upper inner node arcs + both top-face inner edges) a
  second contour, and the remaining inner arcs and the stem share endpoints
  with them and are declared `connect`. Edges therefore end exactly on the
  circle rims instead of crossing into the node holes.
Keyshape: SQUARE, as suggested (score 1.25, fill 1.0 x 1.0, matches hint).
Lucide constructions used: box (isometric hexagon with inner Y) and the
network/git-graph node circles (hollow circle, line ends on its rim).

Metric issues fixed:
- stroke-width: redrawn at stroke 4 with the gaps budgeted for it.
- stroke-count (8 > 6): now 6 paths (outline, inner Y, two inner node arcs,
  stem, bottom inner arc).
- clearance e3/e4, e3/e6, e4/e6 (bottom node, 3.6-5.7): the base edges and
  the stem end on the bottom node rim at shared points; no near-miss gaps.
- clearance e3/e5, e3/e7, e4/e5, e4/e7, e5/e7 (upper nodes, 2.8-5.3): the
  top edges and the inner Y end on the node rims at shared arc endpoints.
- holes at [8.9,12.9], [39.0,12.9], [23.9,38.8] (~2 wide slivers where the
  trace's edges overshot into the node rings): gone; the only enclosed
  holes are the three node interiors (diameter 10 on centerlines) and the
  three cube faces.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a1ebcd1c-faf5-4d0c-93f2-8b0f08933387"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1522-isometric-cube-with-three-circular-nodes/"
    "isometric-cube-with-three-circular-nodes_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
NODE_R = 5
LEFT_NODE = (11, 13)        # right node mirrored about AXIS
BOTTOM_NODE = (24, 37)
TOP = (24, 6)
CENTRE = (24, 20)
LOWER_LEFT = (11, 30)       # lower-left cube corner


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class IsometricCubeWithThreeCircularNodesRedraw(Solo48):
    icon_id = "isometric-cube-with-three-circular-nodes-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shape"
    aliases = ("cube-nodes", "3d-model-nodes", "isometric-box-vertices")
    keywords = ("cube", "isometric", "3d", "box", "nodes", "vertices", "model", "network", "blockchain")

    def build(self) -> None:
        lx, ly = LEFT_NODE
        bx, by = BOTTOM_NODE
        # Rim attachment points (integer, radius 5).
        l_top = (lx + 4, ly - 3)     # edge to the top vertex
        l_mid = (lx + 4, ly + 3)     # edge to the centre
        l_down = (lx, ly + NODE_R)   # vertical side edge
        b_left = (bx - 4, by - 3)    # base edge from the lower-left corner
        b_top = (bx, by - NODE_R)    # centre stem

        # Outer silhouette, clockwise from the top vertex.
        self.add_line("top-l", TOP, l_top)
        self.add_arc("node-l-outer", l_top, l_down, radius_x=NODE_R, large_arc=True, sweep=False)
        self.add_line("side-l", l_down, LOWER_LEFT)
        self.add_line("base-l", LOWER_LEFT, b_left)
        self.add_arc("node-b-outer", b_left, mirror(b_left), radius_x=NODE_R, large_arc=True, sweep=False)
        self.add_line("base-r", mirror(b_left), mirror(LOWER_LEFT))
        self.add_line("side-r", mirror(LOWER_LEFT), mirror(l_down))
        self.add_arc("node-r-outer", mirror(l_down), mirror(l_top), radius_x=NODE_R, large_arc=True, sweep=False)
        self.add_line("top-r", mirror(l_top), TOP)
        self.add_contour(
            "outline", "top-l", "node-l-outer", "side-l", "base-l", "node-b-outer",
            "base-r", "side-r", "node-r-outer", "top-r", closed=True,
        )

        # Inner Y: upper inner node arcs and the two top-face inner edges.
        self.add_arc("node-l-inner-a", l_top, l_mid, radius_x=NODE_R, sweep=True)
        self.add_line("mid-l", l_mid, CENTRE)
        self.add_line("mid-r", CENTRE, mirror(l_mid))
        self.add_arc("node-r-inner-a", mirror(l_mid), mirror(l_top), radius_x=NODE_R, sweep=True)
        self.add_contour("inner-y", "node-l-inner-a", "mid-l", "mid-r", "node-r-inner-a")

        # Remaining node arcs and the centre stem.
        self.add_arc("node-l-inner-b", l_mid, l_down, radius_x=NODE_R, sweep=True)
        self.add_arc("node-r-inner-b", mirror(l_down), mirror(l_mid), radius_x=NODE_R, sweep=True)
        self.add_line("stem", CENTRE, b_top)
        self.add_arc("node-b-inner-a", b_left, b_top, radius_x=NODE_R, sweep=True)
        self.add_arc("node-b-inner-b", b_top, mirror(b_left), radius_x=NODE_R, sweep=True)
        self.add_contour("node-b-inner", "node-b-inner-a", "node-b-inner-b")

        for a, b in (
            ("outline", "inner-y"), ("outline", "node-l-inner-b"), ("outline", "node-r-inner-b"),
            ("inner-y", "node-l-inner-b"), ("inner-y", "node-r-inner-b"), ("inner-y", "stem"),
            ("stem", "node-b-inner"), ("outline", "node-b-inner"),
        ):
            self.relate("connect", a, b)
