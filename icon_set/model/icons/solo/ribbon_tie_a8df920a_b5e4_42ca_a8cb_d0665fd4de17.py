"""Ribbon tie: a bow tie - two flared bow loops either side of a central knot, each
loop with a horizontal crease line running out from the knot.

Symbol plan: mirror symmetry about x=24. The knot is a square-cornered box x 18..30,
y 15..33 (round joins soften it). Each loop is an open run from the knot's top
corner to its bottom corner: a flaring top edge (a cubic that leaves the knot at
slope 1:2 and levels off at the top edge), a radius-4 rounded outer corner, the
straight outer side, the mirrored lower corner and bottom edge. The crease lines
run horizontally from the knot's side mid-point (y=24) outward, stopping 9 short
of the outer sides and 9 from the loop edges at the knot.
Revision (reviewer: "Add two inner horizontal lines and round the outer corners of
both bow loops"): both applied.
Lucide construction: no bow tie; rounded-corner run as in 'square' corners.
Keyshape HRECT_M: centerline x 4..44 (outer sides), y 10..38 (rounded corners).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "a8df920a-b5e4-42ca-a8cb-d0665fd4de17"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__batch-05-ribbon-tie/20260926T061914Z-thuan-mac/reference/ribbon tie_a8df920a-b5e4-42ca-a8cb-d0665fd4de17.svg"
AUTHOR = "claude-opus-5-5"


def mx(p):
    return (48 - p[0], p[1])


class BatchRibbonTie(Solo48):
    icon_id = "batch-05-ribbon-tie-solo"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "fashion"
    aliases = ("ribbon-tie", "bow-tie")
    keywords = ("bow-tie", "ribbon", "tie", "formal", "fashion", "suit", "gentleman")

    def loop(self, side: str, flip) -> None:
        f = flip
        self.add_bezier(f"{side}-top", f((18, 15)), (f((15, 13.5)), f((11, 10)), f((8, 10))))
        self.add_arc(f"{side}-corner-top", f((8, 10)), f((4, 14)), radius_x=4, sweep=(side == "right"))
        self.add_line(f"{side}-outer", f((4, 14)), f((4, 34)))
        self.add_arc(f"{side}-corner-bottom", f((4, 34)), f((8, 38)), radius_x=4, sweep=(side == "right"))
        self.add_bezier(f"{side}-bottom", f((8, 38)), (f((11, 38)), f((15, 34.5)), f((18, 33))))
        self.add_contour(f"{side}-loop", f"{side}-top", f"{side}-corner-top", f"{side}-outer",
                         f"{side}-corner-bottom", f"{side}-bottom")
        self.add_line(f"{side}-crease", f((18, 24)), f((13, 24)))
        self.relate("connect", "knot", f"{side}-loop")
        self.relate("connect", "knot", f"{side}-crease")

    def build(self) -> None:
        self.add_line("knot-top", (18, 15), (30, 15))
        self.add_line("knot-right-upper", (30, 15), (30, 24))
        self.add_line("knot-right-lower", (30, 24), (30, 33))
        self.add_line("knot-bottom", (30, 33), (18, 33))
        self.add_line("knot-left-lower", (18, 33), (18, 24))
        self.add_line("knot-left-upper", (18, 24), (18, 15))
        self.add_contour("knot", "knot-top", "knot-right-upper", "knot-right-lower", "knot-bottom",
                         "knot-left-lower", "knot-left-upper", closed=True)
        self.loop("left", lambda p: p)
        self.loop("right", mx)
