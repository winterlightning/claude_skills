"""Loop manual: an open infinity loop.

Symbol plan: Lucide `infinity` construction widened to HRECT_M. Two
elliptical end caps (rx8, ry14) about (12,24) and (36,24) reach x=4 / x=44;
the rising diagonal is one cubic from (12,38) to (36,10) with flat tangents
(controls 10 in from each end) crossing the centre at (24,24). The falling
diagonal is broken at the crossing like the reference: each open end is the
first 27% of the full falling cubic (de Casteljau split, end snapped to the
lattice), ending at (19,15) and, by half-turn symmetry, (29,33), both 8.5
from the rising stroke.
Revision: the rejected drawing squeezed the loops into two tall ovals (read
as "CS"); the reference is a wide infinity with an open crossing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2c06654c-8d06-5a7b-95e0-7f57b63f8bac"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__loop-manual/20260927T153253Z-thuan-mac-1/reference/loop manual_2c06654c-8d06-5a7b-95e0-7f57b63f8bac.svg"
AUTHOR = "claude-opus-5-5"


def _turn(p):
    return (48 - p[0], 48 - p[1])


class LoopManual(Solo48):
    icon_id = "loop-manual"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "arrows"
    categories = ("primitives", "interface")
    aliases = ("infinity", "loop")
    keywords = ("loop", "manual", "infinity", "repeat", "cycle", "endless")

    def build(self) -> None:
        end, c1, c2 = (19, 15), (14.7, 10), (16.939, 12.02)
        self.add_bezier("fall-left", end, (c2, c1, (12, 10)))
        self.add_arc("cap-left", (12, 10), (12, 38), radius_x=8, radius_y=14, sweep=False)
        self.add_bezier("rise", (12, 38), ((22, 38), (26, 10), (36, 10)))
        self.add_arc("cap-right", (36, 10), (36, 38), radius_x=8, radius_y=14, sweep=True)
        self.add_bezier("fall-right", (36, 38), (_turn(c1), _turn(c2), _turn(end)))
        self.add_contour("loop", "fall-left", "cap-left", "rise", "cap-right", "fall-right")
