"""Circular diverging arrows: a ring holding a Y split whose two branches end in corner arrowheads.

Revision of the disapproved drawing, whose two arrowheads collided into one T blob.
Plan (CIRCLE r20 about (24,24)): everything inside stays within radius 11 so the
ring keeps 9 units of clearance. Stem (24,35)-(24,30), two mirrored cubics to the
tips (15,18) and (33,18), corner heads of 5-unit bars with an 8-unit gap between
their inner ends. Lucide `split` informs the Y construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "94ff1421-50cb-4e9c-918c-422ba8141be2"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__circular-diverging-arrows-solo/20260927T150749Z-thuan-mac-1/reference/circle split arrow_94ff1421-50cb-4e9c-918c-422ba8141be2.svg"
AUTHOR = "claude-fable-5-1"


class CircularDivergingArrows(Solo48):
    icon_id = "circular-diverging-arrows-solo"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "other"
    aliases = ("circle split arrow", "fork arrows in circle")
    keywords = ("diverge", "split", "fork", "arrows", "circle", "branch")

    def build(self) -> None:
        cx, cy, r = 24, 24, 20
        self.add_arc("ring-1", (cx - r, cy), (cx, cy - r), radius_x=r)
        self.add_arc("ring-2", (cx, cy - r), (cx + r, cy), radius_x=r)
        self.add_arc("ring-3", (cx + r, cy), (cx, cy + r), radius_x=r)
        self.add_arc("ring-4", (cx, cy + r), (cx - r, cy), radius_x=r)
        self.add_contour("ring", "ring-1", "ring-2", "ring-3", "ring-4", closed=True)
        # Y split
        self.add_line("stem", (24, 35), (24, 30))
        self.add_bezier("branch-left", (24, 30), ((24, 25), (18, 21), (15, 18)))
        self.add_bezier("branch-right", (24, 30), ((24, 25), (30, 21), (33, 18)))
        self.add_contour("arrows", "branch-left")
        self.relate("connect", "stem", "branch-left")
        self.relate("connect", "stem", "branch-right")
        self.relate("connect", "branch-left", "branch-right")
        self.add_polyline("head-left", (15, 23), (15, 18), (20, 18))
        self.add_polyline("head-right", (28, 18), (33, 18), (33, 23))
        self.relate("connect", "head-left", "branch-left")
        self.relate("connect", "head-right", "branch-right")
