"""Badge 3: a winged shield badge - a shield with a shallow peaked top and a pointed
base, flanked by two wing panels.

Symbol plan: mirror symmetry about x=24. The shield is one closed contour: a peaked
top (24,10) to shoulders at x 15/33, straight sides down to y=26, then tangent
cubics converging to the point (24,38). Each wing is an open run that leaves the
shield side at y=18 along a straight horizontal top to the outer tip, sweeps down
and in along a curved outer edge (one cubic ending horizontal), and returns along a
short flat bottom (y=26) into the shield side, so each wing panel is 8 tall.
Revision (reviewer: "Replace the rectangular side loops with wing-like panels that
have straight horizontal tops, curved outer edges, and short, flat bottoms"):
applied; the shield also takes the reference's pointed base.
Lucide construction: 'shield' - peaked top, sides converging to a point.
Keyshape HRECT_M: centerline x 4..44 (wing tips), y 10 (peak) .. 38 (point).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a8f967f3-b422-5921-9bb1-899ad88e3265"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__badge-3/20260926T061914Z-thuan-mac/reference/badge 3_a8f967f3-b422-5921-9bb1-899ad88e3265.svg"
AUTHOR = "claude-opus-5-5"


def mx(p):
    return (48 - p[0], p[1])


class Badge3(Solo48):
    icon_id = "badge-3"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "awards"
    aliases = ("winged-shield", "winged-badge")
    keywords = ("badge", "shield", "wings", "emblem", "rank", "award", "insignia")

    def build(self) -> None:
        wing_top, wing_bottom, side = 18, 26, 15
        self.add_line("peak-right", (24, 10), mx((side, 13)))
        self.add_line("side-right-upper", mx((side, 13)), mx((side, wing_top)))
        self.add_line("side-right-lower", mx((side, wing_top)), mx((side, wing_bottom)))
        self.add_bezier("base-right", mx((side, wing_bottom)), (mx((15, 31)), mx((20, 35)), (24, 38)))
        self.add_bezier("base-left", (24, 38), ((20, 35), (15, 31), (side, wing_bottom)))
        self.add_line("side-left-lower", (side, wing_bottom), (side, wing_top))
        self.add_line("side-left-upper", (side, wing_top), (side, 13))
        self.add_line("peak-left", (side, 13), (24, 10))
        self.add_contour("shield", "peak-right", "side-right-upper", "side-right-lower", "base-right",
                         "base-left", "side-left-lower", "side-left-upper", "peak-left", closed=True)
        for name, f in (("left", lambda p: p), ("right", mx)):
            self.add_line(f"{name}-wing-top", f((side, wing_top)), f((4, wing_top)))
            self.add_bezier(f"{name}-wing-edge", f((4, wing_top)),
                            (f((6, 22)), f((8, wing_bottom)), f((11, wing_bottom))))
            self.add_line(f"{name}-wing-bottom", f((11, wing_bottom)), f((side, wing_bottom)))
            self.add_contour(f"{name}-wing", f"{name}-wing-top", f"{name}-wing-edge", f"{name}-wing-bottom")
            self.relate("connect", "shield", f"{name}-wing")
