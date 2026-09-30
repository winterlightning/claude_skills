"""cloudberry-with-paired-top-leaves (redraw of the new-pipeline traced SVG).

Plan: a squat scalloped cloudberry mirrored about x=24, two segment dividers
rising from its bottom cusps, and two detached pointed leaves above it, on
VRECT_L (centerline box (8,4)-(40,44)).
- berry: one closed contour of five lobes -- two round top lobes meeting at
  the centre notch (24,26), two large side lobes whose extremes (8,34)/(40,34)
  are reached with vertical tangents, and the centre drupelet whose base
  (24,44) is the bottom extreme. The trace's nine small lobes were reduced
  to five; smaller lobes filled in at 48 px (a SQUARE draft with seven lobes
  read as a brain).
- dividers: the trace's two free-floating arcs cannot sit 8 from every cusp
  inside the berry, so each divider rises from a bottom cusp (18,40)/(30,40)
  to (18,33)/(30,33), slightly bowed outwards like the trace, and connects
  to the outline. They stop 8.5 from the side cusps and 9.2 from the notch.
- leaves: closed lenses from the base (19,13)/(29,13) to the tip (9,4)/(39,4);
  each upper side meets the tip level, so the tips are the top extreme.

Keyshape: the metrics suggest SQUARE (score 1.12, helped by the "square"
shape hint) with a 1.15 x-stretch; VRECT_L needs only 1.08 on y and its 40
units of height leave room for the 8-unit leaf gap plus a berry tall enough
for the dividers.

Metric issues fixed:
- stroke-width (info): drawn at stroke 4; every gap is sized for it.
- keyshape-short-axis (warn): moot on VRECT_L; berry sides at x=8/40, leaf
  tips at y=4, drupelet base at y=44.
- clearance e0/e1 (leaf vs leaf, 4.32): leaf bases now 10 apart.
- clearance e0/e2 and e1/e2 (leaves vs berry, 2.1): now 8.01 on centerlines.
- clearance e2/e3 and e2/e4 (dividers vs outline, 4.4): dividers now join the
  outline at the bottom cusps and keep >= 8 from every other part of it.
Not fixed:
- hole x2 (leaf interiors 2.55 wide, need 6): now 3.31. A 6-wide interior
  needs a leaf about 10 units thick; the leaves have 9 units of height above
  the 8-unit gap to the berry, and a thicker lens crosses y=4 or the gap.
  Taking the space from the berry would drop the dividers. build_gate passes.

Lucide: no useful cloudberry match; the construction follows the trace.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "eafdf9a0-9c6d-4a1c-8cdd-84a2ec5341c9"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1912-cloudberry-with-paired-top-leaves/"
    "cloudberry-with-paired-top-leaves_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
# Right half of the berry (the left half mirrors it about x = 24).
NOTCH = (24, 26)            # top centre cusp between the two top lobes
TOP_APEX = (30, 21)         # apex of the top-right lobe
SIDE_CUSP = (37, 28)        # between the top lobe and the side lobe
SIDE_EXTREME = (40, 34)     # right extreme (x = 40)
SIDE_BOTTOM = (33, 42)      # lowest point of the side lobe
BOTTOM_CUSP = (30, 40)      # between the side lobe and the centre drupelet
BOTTOM_APEX = (24, 44)      # bottom of the centre drupelet (y = 44)
DIVIDER_TIP = (30, 33)      # divider rises from BOTTOM_CUSP to here
DIVIDER_BOW = ((31, 37), (31, 35))
# Right leaf: lens from its base beside the notch to its tip (y = 4).
LEAF_BASE, LEAF_TIP = (29, 13), (39, 4)
LEAF_UPPER = ((28, 6), (32, 4))
LEAF_LOWER = ((39, 11), (35, 13))

TOP_LOBE = (((25, 22), (27, 21), TOP_APEX), ((34, 21), (37, 24), SIDE_CUSP))
SIDE_LOBE = (((39, 28), (40, 31), SIDE_EXTREME),
             ((40, 38), (37, 42), SIDE_BOTTOM),
             ((31, 42), (30, 42), BOTTOM_CUSP))
CENTRE_HALF = ((30, 43), (27, 44), BOTTOM_APEX)


def mirror(p):
    return (2 * AXIS - p[0], p[1])


def mirrored_reverse(start, segments):
    """The mirror image of a cubic run, traversed in the opposite direction."""
    points = [start] + [p for segment in segments for p in segment]
    points = [mirror(p) for p in reversed(points)]
    return points[0], [tuple(points[i:i + 3]) for i in range(1, len(points), 3)]


class CloudberryWithPairedTopLeavesRedraw(Solo48):
    icon_id = "cloudberry-with-paired-top-leaves-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/fruit"
    aliases = ("cloudberry", "bakeapple")
    keywords = ("cloudberry", "berry", "fruit", "leaves", "food", "nordic")

    def build(self) -> None:
        m = mirror
        # Berry outline, clockwise from the notch.
        self.add_bezier("top-right", NOTCH, *TOP_LOBE)
        self.add_bezier("side-right", SIDE_CUSP, *SIDE_LOBE)
        _, tail = mirrored_reverse(BOTTOM_CUSP, (CENTRE_HALF,))
        self.add_bezier("centre", BOTTOM_CUSP, CENTRE_HALF, *tail)
        start, segments = mirrored_reverse(SIDE_CUSP, SIDE_LOBE)
        self.add_bezier("side-left", start, *segments)
        start, segments = mirrored_reverse(NOTCH, TOP_LOBE)
        self.add_bezier("top-left", start, *segments)
        self.add_contour("berry", "top-right", "side-right", "centre",
                         "side-left", "top-left", closed=True)

        # Segment dividers rising from the bottom cusps, bowed outwards.
        self.add_bezier("divider-right", BOTTOM_CUSP, (*DIVIDER_BOW, DIVIDER_TIP))
        self.add_bezier("divider-left", m(BOTTOM_CUSP),
                        (*map(m, DIVIDER_BOW), m(DIVIDER_TIP)))
        self.relate("connect", "divider-right", "berry")
        self.relate("connect", "divider-left", "berry")

        # Leaves: pointed lenses, the sides meeting at right angles.
        for side, f in (("right", lambda p: p), ("left", m)):
            self.add_bezier(f"leaf-{side}-upper", f(LEAF_BASE),
                            (*map(f, LEAF_UPPER), f(LEAF_TIP)))
            self.add_bezier(f"leaf-{side}-lower", f(LEAF_TIP),
                            (*map(f, LEAF_LOWER), f(LEAF_BASE)))
            self.add_contour(f"leaf-{side}", f"leaf-{side}-upper",
                             f"leaf-{side}-lower", closed=True)
