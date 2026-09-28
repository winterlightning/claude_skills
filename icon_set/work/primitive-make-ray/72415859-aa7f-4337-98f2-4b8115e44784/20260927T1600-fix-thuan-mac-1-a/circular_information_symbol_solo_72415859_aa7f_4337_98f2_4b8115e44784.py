"""Circular information symbol: a ring around a serif lowercase i.

Revision of the disapproved drawing, whose stubby i sat too low and small in the ring.
Plan (CIRCLE r20 about (24,24)): dot at (24,13), stem (24,22)-(24,33) with a short
top serif to the left and a base serif; everything within radius 11 keeps 9 units
of ring clearance. Lucide `info` informs the ring and the dot/stem split.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "72415859-aa7f-4337-98f2-4b8115e44784"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__circular-information-symbol-solo/20260927T150749Z-thuan-mac-1/reference/circle information_72415859-aa7f-4337-98f2-4b8115e44784.svg"
AUTHOR = "claude-fable-5-1"


class CircularInformationSymbol(Solo48):
    icon_id = "circular-information-symbol-solo"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "other"
    aliases = ("info circle", "information")
    keywords = ("info", "information", "help", "circle", "i")

    def build(self) -> None:
        cx, cy, r = 24, 24, 20
        self.add_arc("ring-1", (cx - r, cy), (cx, cy - r), radius_x=r)
        self.add_arc("ring-2", (cx, cy - r), (cx + r, cy), radius_x=r)
        self.add_arc("ring-3", (cx + r, cy), (cx, cy + r), radius_x=r)
        self.add_arc("ring-4", (cx, cy + r), (cx - r, cy), radius_x=r)
        self.add_contour("ring", "ring-1", "ring-2", "ring-3", "ring-4", closed=True)
        self.add_dot("dot", (24, 13))
        self.add_polyline("stem", (20, 22), (24, 22), (24, 33))
        self.add_polyline("base", (20, 33), (24, 33), (28, 33))
        self.relate("connect", "stem", "base")
