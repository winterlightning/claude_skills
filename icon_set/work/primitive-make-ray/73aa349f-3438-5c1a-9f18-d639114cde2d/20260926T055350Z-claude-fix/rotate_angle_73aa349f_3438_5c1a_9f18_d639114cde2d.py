"""A clockwise rotate arrow: a nearly full circle sweeping from the bottom round the left and
over the top, ending in an arrowhead at the upper right.

Symbol plan: the path is an r18 circle about (24, 24): a large arc from the bottom
(24, 42) clockwise through the left (6, 24) to the top (24, 6), then a cubic that
leaves the top horizontally and turns to 45 degrees at (38, 12), and a straight run to
the arrow tip (42, 16). The arrowhead is Lucide's square corner: arms straight up to
(42, 6) and straight left to (36, 16). The gap between the arrowhead and the start at the
bottom leaves the lower-right quadrant open, as in the reference.
Lucide construction: 'rotate-cw' - circle arc easing into a 45-degree run with an
axis-aligned corner arrowhead.
Keyshape SQUARE: centerline x 6..42 (arc left, tip and up arm), y 6..42 (arc top and up arm,
arc start).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "73aa349f-3438-5c1a-9f18-d639114cde2d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__rotate-angle/20260926T055140Z-thuan-mac/reference/rotate angle_73aa349f-3438-5c1a-9f18-d639114cde2d.svg"
AUTHOR = "claude-opus-5-5"


class RotateAngle(Solo48):
    icon_id = "rotate-angle"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/arrow"
    aliases = ("rotate angle", "rotate clockwise", "rotate-cw")
    keywords = ("rotate", "clockwise", "turn", "angle", "refresh", "redo", "spin", "orientation")

    def build(self) -> None:
        self.add_arc("sweep-lower", (24, 42), (6, 24), radius_x=18)
        self.add_arc("sweep-upper", (6, 24), (24, 6), radius_x=18)
        self.add_bezier("ease", (24, 6), ((29, 6), (34, 8), (38, 12)))
        self.add_line("run", (38, 12), (42, 16))
        self.add_contour("rotation", "sweep-lower", "sweep-upper", "ease", "run")
        self.add_polyline("arrowhead", (42, 6), (42, 16), (36, 16))
        self.relate("connect", "rotation", "arrowhead")
