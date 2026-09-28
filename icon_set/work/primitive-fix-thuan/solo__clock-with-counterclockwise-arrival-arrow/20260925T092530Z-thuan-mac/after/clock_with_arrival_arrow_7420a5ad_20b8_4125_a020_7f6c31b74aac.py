"""Estimated-arrival clock: a clock face whose rim is an arrow. The rim starts
near half past ten, runs clockwise round the dial and ends at nine o'clock in
an upward arrowhead; two hands read three o'clock.

Symbol plan: rim = one short elliptical arc into twelve o'clock and three
quarter arcs about (26,24) with radii 16 x 18; the arrowhead is a symmetric
chevron whose apex is the rim's end, arms at 45 degrees either side of the
vertical travel direction. The rim is 2 units narrower than it is tall so the
arrowhead's outer arm fits inside the square without shrinking the dial.
Hands share the centre node. Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: rotate-ccw / history (open rim, chevron at its end,
hands from the centre).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7420a5ad-20b8-4125-a020-7f6c31b74aac"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__clock-with-counterclockwise-arrival-arrow/20260925T092530Z-thuan-mac/reference/shipping logistic estimate time arrival 1_7420a5ad-20b8-4125-a020-7f6c31b74aac.svg"
AUTHOR = "claude-opus-5-5"


class ClockWithArrivalArrow(Solo48):
    icon_id = "clock-with-counterclockwise-arrival-arrow"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "time"
    aliases = ("estimated time of arrival", "eta")
    keywords = ("clock", "arrival", "estimate", "time", "shipping", "arrow")

    def build(self) -> None:
        cx, cy, rx, ry = 26, 24, 16, 18
        tip = (cx - rx, cy)
        arm = 4
        self.add_arc("rim-1", (15, 11), (cx, cy - ry), radius_x=rx, radius_y=ry)
        self.add_arc("rim-2", (cx, cy - ry), (cx + rx, cy), radius_x=rx, radius_y=ry)
        self.add_arc("rim-3", (cx + rx, cy), (cx, cy + ry), radius_x=rx, radius_y=ry)
        self.add_arc("rim-4", (cx, cy + ry), tip, radius_x=rx, radius_y=ry)
        self.add_contour("rim", "rim-1", "rim-2", "rim-3", "rim-4")
        self.add_polyline("head", (tip[0] - arm, tip[1] + arm), tip, (tip[0] + arm, tip[1] + arm))
        self.relate("connect", "rim", "head")
        self.add_polyline("hands", (cx, cy - 9), (cx, cy), (cx + 6, cy))
