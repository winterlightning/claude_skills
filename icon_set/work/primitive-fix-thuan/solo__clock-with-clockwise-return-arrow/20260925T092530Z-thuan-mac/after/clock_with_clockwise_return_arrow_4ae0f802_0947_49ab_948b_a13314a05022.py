"""Clock face whose rim is a clockwise return arrow: the rim starts at six
o'clock, runs clockwise round the dial and ends at about half past four in an
arrowhead pointing back toward its start; two hands read three o'clock.

Symbol plan: rim = three quarter arcs about (24,24), radius 18, plus a last
radius-18 arc to the arrow tip; the arrowhead is one right-angle chevron whose
corner is the rim's end and whose arms run back at 45 degrees to the rim's
direction (up and right), so the head points along the travel. Hands share
the centre node. Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: rotate-cw / history (arc with a corner-bracket head at
its end, hands from the centre).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4ae0f802-0947-49ab-948b-a13314a05022"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__clock-with-clockwise-return-arrow/20260925T092530Z-thuan-mac/reference/snooze return repeat_4ae0f802-0947-49ab-948b-a13314a05022.svg"
AUTHOR = "claude-opus-5-5"


class ClockWithClockwiseReturnArrow(Solo48):
    icon_id = "clock-with-clockwise-return-arrow"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "time"
    aliases = ("snooze", "repeat", "clock return")
    keywords = ("clock", "clockwise", "return", "repeat", "snooze", "arrow")

    def build(self) -> None:
        cx, cy, r = 24, 24, 18
        tip = (36, 36)
        arm = 6
        self.add_arc("rim-1", (cx, cy + r), (cx - r, cy), radius_x=r)
        self.add_arc("rim-2", (cx - r, cy), (cx, cy - r), radius_x=r)
        self.add_arc("rim-3", (cx, cy - r), (cx + r, cy), radius_x=r)
        self.add_arc("rim-4", (cx + r, cy), tip, radius_x=r)
        self.add_contour("rim", "rim-1", "rim-2", "rim-3", "rim-4")
        self.add_polyline("head", (tip[0], tip[1] - arm), tip, (tip[0] + arm, tip[1]))
        self.relate("connect", "rim", "head")
        self.add_polyline("hands", (cx, cy - 9), (cx, cy), (cx + 6, cy))
