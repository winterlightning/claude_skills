"""Round: a clockwise circular arrow, open at the left, with a V arrowhead at its
lower-left end pointing up into the gap.

Symbol plan: a true circle (radius 18 about the canvas centre) drawn clockwise
from its left point (6,24) over the top and right to the bottom (24,42), then one
cubic that leaves the bottom horizontally and arrives at the head corner (6,34)
at 45 degrees, so the whole run is tangent-continuous. The head is one open
chevron with its tip on that corner: arms of 8 along the box edges (down and
right), i.e. +/-45 degrees about the backward tangent (1,1). The gap (6,24)-(6,34)
is 10.
Revision: the rejected drawing closed the circle with an elliptical 14x10 segment,
kinking the curve, and squashed the arrowhead into a blob.
Lucide construction: 'rotate-cw', rotated 180 degrees - circle, tangent run into
a corner, L head on the box edges.
Keyshape SQUARE: centerline 6..42 from the circle's left/top/right/bottom points
and the head arms.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "09113b60-330a-48f7-bd5a-2a66b63402bc"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__round/20260926T055144Z-thuan-mac/reference/round_09113b60-330a-48f7-bd5a-2a66b63402bc.svg"
AUTHOR = "claude-opus-5-5"


class Round(Solo48):
    icon_id = "round"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "arrows"
    aliases = ("rotate-clockwise", "redo", "refresh")
    keywords = ("round", "rotate", "clockwise", "circular-arrow", "repeat", "cycle", "arrow")

    def build(self) -> None:
        r = 18
        corner = (6, 34)
        self.add_arc("ring-top", (6, 24), (42, 24), radius_x=r, sweep=True)
        self.add_arc("ring-right", (42, 24), (24, 42), radius_x=r, sweep=True)
        self.add_bezier("ring-tail", (24, 42), ((17, 42), (11, 39), corner))
        self.add_contour("ring", "ring-top", "ring-right", "ring-tail")
        self.add_polyline("head", (6, 42), corner, (14, 34))
        self.relate("connect", "ring", "head")
