"""Dash fast up (large head): a speed arrow - two short dashes along a baseline lead
into a curve that sweeps up into a large open arrowhead.

Symbol plan: all three strokes share the baseline y=38: two 3-long dashes 8 apart,
then the shaft (9 after the second dash, since it is curved), a quarter ellipse (rx 11, ry 28 about (27,10)) that
leaves the baseline horizontally and arrives vertically at the tip (38,10). The
head is one open chevron on the tip with arms of 8.5 at +/-45 degrees, reaching
the right edge.
Revision (no reviewer text): the rejected drawing lifted the second dash off the
baseline and cramped the head; the dashes now line up with the shaft start as in
the reference and the head is symmetric about the shaft's tangent.
Lucide construction: 'move-up-right' / 'trending-up' - curved shaft with open head.
Keyshape HRECT_M: centerline x 4 (first dash) .. 44 (head arm), y 10 (tip) .. 38.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ef45cf2e-5e94-4067-a4b1-6061831c3128"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dash-fast-up-large-head/20260926T073832Z-thuan-mac/reference/dash fast up large head_ef45cf2e-5e94-4067-a4b1-6061831c3128.svg"
AUTHOR = "claude-opus-5-5"


class DashFastUpLargeHead(Solo48):
    icon_id = "dash-fast-up-large-head"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "arrows"
    aliases = ("speed-arrow-up", "fast-up")
    keywords = ("dash", "fast", "up", "arrow", "speed", "growth", "rise", "trend")

    def build(self) -> None:
        base, tip = 38, (38, 10)
        self.add_line("dash-1", (4, base), (7, base))
        self.add_line("dash-2", (15, base), (18, base))
        self.add_arc("shaft", (27, base), tip, radius_x=11, radius_y=28, sweep=False)
        self.add_polyline("head", (32, 16), tip, (44, 16))
        self.relate("connect", "shaft", "head")
