"""Rotation about the x axis: a looped arrow around a horizontal axis.

Symbol plan: full-width axis y=24 (6..42). Around it a tall elliptical
loop (rx10, ry18 about (24,24), cubic quarter-ellipse controls k=0.5523)
passes in front of the axis on the right, crossing it at the shared node
(34,24), and is broken on the left where it runs behind the axis: the upper
end stops 9 above the axis at (15,15) with an arrowhead pointing down, the
lower end resumes 9 below it at (15,33). Both left ends follow the same
ellipse and leave vertically.
Revision: the rejected drawing dropped the loop's lower-left return and
angled the arrowhead sideways; the reference shows the whole loop around the
axis with a gap on the left and a downward arrowhead.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c15ccdfd-3287-49fc-992e-2fbe01ffe897"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__looped-arrow-around-horizontal-axis/20260927T153253Z-thuan-mac-1/reference/rotation x axis_c15ccdfd-3287-49fc-992e-2fbe01ffe897.svg"
AUTHOR = "claude-opus-5-5"

K = 0.5523


class LoopedArrowAroundHorizontalAxis(Solo48):
    icon_id = "looped-arrow-around-horizontal-axis"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "arrows"
    categories = ("primitives", "arrows")
    aliases = ("rotation x axis", "rotate around x")
    keywords = ("rotation", "x axis", "rotate", "3d", "orbit", "axis")

    def build(self) -> None:
        cx, cy, rx, ry = 24, 24, 10, 18
        top, bottom, right = (cx, cy - ry), (cx, cy + ry), (cx + rx, cy)
        self.add_bezier("loop-upper-left", (15, 15), ((15, 11), (cx - rx * K, top[1]), top))
        self.add_bezier("loop-upper-right", top, ((cx + rx * K, top[1]), (right[0], cy - ry * K), right))
        self.add_bezier("loop-lower-right", right, ((right[0], cy + ry * K), (cx + rx * K, bottom[1]), bottom))
        self.add_bezier("loop-lower-left", bottom, ((cx - rx * K, bottom[1]), (15, 37), (15, 33)))
        self.add_contour("loop", "loop-upper-left", "loop-upper-right",
                         "loop-lower-right", "loop-lower-left")
        self.add_polyline("arrowhead", (11, 11), (15, 15), (19, 11))
        self.relate("connect", "arrowhead", "loop")

        self.add_line("axis-left", (6, cy), right)
        self.add_line("axis-right", right, (42, cy))
        for part in ("axis-left", "axis-right"):
            self.relate("connect", part, "loop")
        self.relate("connect", "axis-left", "axis-right")
