"""blackberry-cluster-with-a-single-leaf (redraw of the new-pipeline traced SVG).

Plan: a scalloped blackberry whose bottom drupelet continues upward as the
two column seams of the trace, plus one detached pointed leaf in the upper
right, on VRECT_L (centerline box (8,4)-(40,44)).
- berry: one closed contour of six lobes mirrored about x=22 -- a round
  top-centre lobe (arc r6 between the top cusps (17,21)/(27,21)), two small
  top-left/right lobes, two long side lobes whose extremes (8,32)/(36,32)
  are reached with vertical tangents, and the bottom drupelet (semicircle
  r5 on (17,39)-(27,39), base (22,44)).
- seams: two straight lines rising from the bottom cusps to (17,30)/(27,30);
  they continue the drupelet's vertical tangents, sit directly under the top
  cusps so the eye reads a central drupelet column, and end with free tips.
- leaf: a closed lens between (26,10) and its tip (40,4); the upper side
  reaches the tip horizontally, so the tip is both the top and right extreme.
Deliberate asymmetry: only the leaf (the berry is mirrored).

Keyshape: the metrics suggest SQUARE (score 0.98, from the "square" shape
hint) but it needs a 1.37 x-stretch. VRECT_L (x-stretch 1.09) is used over
VRECT_M (1.05) because the detached leaf needs x 36..40 beside the berry to
keep its 8-unit gap; the berry alone spans x 8..36.

Metric issues fixed:
- stroke-width (info): drawn at stroke 4; every gap is sized for it.
- keyshape-short-axis (warn): moot on VRECT_L; berry side at x=8, leaf tip
  at x=40 and y=4, drupelet base at y=44.
- clearance e0/e3 (error, leaf vs berry 2.36): now 8.05 on centerlines.
- clearance e1/e3 and e2/e3 (error, seams vs outline 4.37): the seams now
  start at the bottom cusps and stop 9 below the top cusps; 8.6 from the
  outline beyond the shared joints, 10 from each other.
Not fixed:
- hole (error, leaf interior 3.11 wide, need 6): the leaf interior is about
  2.8 ink wide (build gate passes). A 6-wide interior needs a lens 10 thick;
  with the 8-unit gap that pushes the berry top below y=23, which removes
  the seams and the top lobes that make it read as a blackberry. The flatter
  D-shaped lens that reaches 3.3 stopped reading as a leaf.

Lucide: no useful blackberry match; the construction follows the trace.
Traced shape: 20260929-1831-blackberry-cluster-with-a-single-leaf/
blackberry-cluster-with-a-single-leaf_raw.svg
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3278a9d5-891d-4c6a-acc3-7bd972888b5c"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1831-blackberry-cluster-with-a-single-leaf/"
    "blackberry-cluster-with-a-single-leaf_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 22
TOP_CUSP = (17, 21)        # between the top-left and top-centre lobes
SIDE_CUSP = (10, 25)       # between the top-left lobe and the side lobe
SIDE_EXTREME = (8, 32)     # left extreme of the side lobe (x = 8)
BOTTOM_CUSP = (17, 39)     # between the side lobe and the bottom drupelet
TOP_R, BOTTOM_R = 6, 5     # top-centre lobe apex (22,18.3); bottom (22,44)
SEAM_TIP = (17, 30)        # column seam rises from the bottom cusp to here
LEAF_A, LEAF_B = (26, 10), (40, 4)
LEAF_UPPER = ((26, 5), (32, 4))
LEAF_LOWER = ((40, 12), (35, 12))


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class BlackberryClusterWithASingleLeafRedraw(Solo48):
    icon_id = "blackberry-cluster-with-a-single-leaf-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/fruit"
    aliases = ("blackberry", "bramble-berry")
    keywords = ("blackberry", "berry", "fruit", "leaf", "bramble", "food")

    def build(self) -> None:
        m = mirror
        # Outline, clockwise from the upper-left cusp.
        self.add_arc("lobe-top", TOP_CUSP, m(TOP_CUSP), radius_x=TOP_R)
        self.add_bezier("lobe-top-right", m(TOP_CUSP),
                        (m((15, 17)), m((10, 19)), m(SIDE_CUSP)))
        self.add_bezier("lobe-right", m(SIDE_CUSP),
                        (m((8, 26)), m((8, 29)), m(SIDE_EXTREME)),
                        (m((8, 37)), m((12, 40)), m(BOTTOM_CUSP)))
        self.add_arc("lobe-bottom", m(BOTTOM_CUSP), BOTTOM_CUSP,
                     radius_x=BOTTOM_R)
        self.add_bezier("lobe-left", BOTTOM_CUSP,
                        ((12, 40), (8, 37), SIDE_EXTREME),
                        ((8, 29), (8, 26), SIDE_CUSP))
        self.add_bezier("lobe-top-left", SIDE_CUSP,
                        ((10, 19), (15, 17), TOP_CUSP))
        self.add_contour("berry", "lobe-top", "lobe-top-right", "lobe-right",
                         "lobe-bottom", "lobe-left", "lobe-top-left",
                         closed=True)

        # Column seams: the bottom drupelet's sides carried straight up.
        self.add_line("seam-left", BOTTOM_CUSP, SEAM_TIP)
        self.add_line("seam-right", m(BOTTOM_CUSP), m(SEAM_TIP))
        self.relate("connect", "seam-left", "berry")
        self.relate("connect", "seam-right", "berry")

        # Detached leaf: lens between LEAF_A (stem end) and LEAF_B (tip).
        self.add_bezier("leaf-upper", LEAF_A, (*LEAF_UPPER, LEAF_B))
        self.add_bezier("leaf-lower", LEAF_B, (*LEAF_LOWER, LEAF_A))
        self.add_contour("leaf", "leaf-upper", "leaf-lower", closed=True)
