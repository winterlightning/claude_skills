"""Attached file: a paperclip lying on the diagonal, one continuous wire bent
into three nested loops.

Symbol plan: four parallel 45-degree rails x+y = 27, 41, 55, 69 (9.9 apart)
joined by three near-semicircular loops whose end points are Pythagorean
points of their circles: radius 5 (3-4-5) and radius 15 (9-12-15), concentric
about (21,27) at the lower-left, and radius 10 (6-8-10) about (25,16) at the
upper-right. The wire starts inside the upper loop and ends on the outer rail.
Keyshape SQUARE: outer loop left x=6 / bottom y=42, upper loop top y=6,
outer rail end x=42.
Lucide construction: paperclip (one spiral wire, loop radii in ratio 1:2:3).
Revision of the rejected drawing ("Bad stroke drawn"): the old drawing's wire
wobbled through uneven cubic bends; here every bend is a true circular loop.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5473937d-c579-47bd-9ac8-1ed8c210eb47"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__diagonal-paperclip-batch-021-13/20260925T092544Z-thuan-mac/reference/attached file_5473937d-c579-47bd-9ac8-1ed8c210eb47.svg"
AUTHOR = "claude-opus-5-5"

LOW = (21, 27)          # centre of the two lower-left loops
HIGH = (25, 16)         # centre of the upper-right loop


def add(p, d):
    return (p[0] + d[0], p[1] + d[1])


class DiagonalPaperclipBatch02113(Solo48):
    icon_id = "diagonal-paperclip-batch-021-13"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("attached-file", "paperclip", "attachment")
    keywords = ("attached", "file", "paperclip", "attachment", "clip")

    def build(self) -> None:
        start = add(HIGH, (1, -1))                  # free end inside the upper loop
        inner_a, inner_b = add(LOW, (-3, -4)), add(LOW, (4, 3))
        upper_a, upper_b = add(HIGH, (6, 8)), add(HIGH, (-8, -6))
        outer_a, outer_b = add(LOW, (-9, -12)), add(LOW, (12, 9))
        end = (42, 27)
        self.add_line("rail-1", start, inner_a)
        self.add_arc("loop-inner", inner_a, inner_b, radius_x=5, large_arc=True, sweep=False)
        self.add_line("rail-2", inner_b, upper_a)
        self.add_arc("loop-upper", upper_a, upper_b, radius_x=10, large_arc=True, sweep=False)
        self.add_line("rail-3", upper_b, outer_a)
        self.add_arc("loop-outer", outer_a, outer_b, radius_x=15, large_arc=True, sweep=False)
        self.add_line("rail-4", outer_b, end)
        self.add_contour("wire", "rail-1", "loop-inner", "rail-2", "loop-upper",
                         "rail-3", "loop-outer", "rail-4")
