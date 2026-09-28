"""An end-point arrow: a long horizontal line ending in a right-triangle arrowhead on the right.

Symbol plan: the line runs across the full diameter, (4, 24) to (44, 24). The arrowhead
is a right triangle standing on the line's last 14 units: an upright edge x 30 from the
line up to (30, 14) and a hypotenuse falling back to the line's end (44, 24), the
reference's 77:55 proportion (14 wide, 10 tall). The triangle is one closed contour that
shares the line's end points; the line is split at (30, 24).
Lucide construction: 'move-right'-style long shaft; the head is a closed right triangle.
Keyshape CIRCLE: the shaft ends lie exactly on radius 20 about (24, 24), every other point
inside, so the thin reference keeps its proportions (a rectangle keyshape would force a
28-tall head).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9c1f6ea2-97f0-41eb-96d5-43b4feacf58b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__end-point-triangle-arrow-1/20260926T055140Z-thuan-mac/reference/end point triangle arrow 1_9c1f6ea2-97f0-41eb-96d5-43b4feacf58b.svg"
AUTHOR = "claude-opus-5-5"


class EndPointTriangleArrow1(Solo48):
    icon_id = "end-point-triangle-arrow-1"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/arrow"
    aliases = ("end point triangle arrow 1", "line end arrow", "triangle line end")
    keywords = ("arrow", "line", "end", "endpoint", "triangle", "connector", "diagram", "direction")

    def build(self) -> None:
        self.add_line("shaft", (4, 24), (30, 24))
        self.add_polyline("head", (30, 24), (44, 24), (30, 14), closed=True)
        self.relate("connect", "shaft", "head")
