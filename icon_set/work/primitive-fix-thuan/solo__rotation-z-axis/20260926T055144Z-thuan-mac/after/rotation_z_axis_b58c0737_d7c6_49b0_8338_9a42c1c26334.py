"""Rotation z axis: a counterclockwise circular arrow around a small axis ring, open
at the top-left with a V arrowhead pointing down into the gap.

Symbol plan: a true circle (radius 18 about the canvas centre) drawn
counterclockwise from its left point (6,24) down through the bottom and right to
the top (24,6), then one cubic that leaves the top horizontally and arrives at the
head corner (6,14) at 45 degrees, so the whole run is tangent-continuous. The head
is one open chevron with its tip on that corner: arms of 8 along the box edges (up
and right), +/-45 degrees about the backward tangent. The gap (6,14)-(6,24) is 10.
The z axis is a ring of radius 5 at the centre, 13 inside the circle and 9+ from
the head.
Revision: the rejected drawing closed the circle with an elliptical 16x8 segment,
kinking the curve, and its r4 axis ring read as a dot.
Lucide construction: 'rotate-ccw' - circle, tangent run into a corner, L head on
the box edges; centre ring as in 'disc'.
Keyshape SQUARE: centerline 6..42 from the circle's left/top/right/bottom points
and the head arm.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b58c0737-d7c6-49b0-8338-9a42c1c26334"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__rotation-z-axis/20260926T055144Z-thuan-mac/reference/rotation z axis_b58c0737-d7c6-49b0-8338-9a42c1c26334.svg"
AUTHOR = "claude-opus-5-5"


class RotationZAxis(Solo48):
    icon_id = "rotation-z-axis"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "arrows"
    aliases = ("rotate-z", "z-rotation", "rotate-counterclockwise")
    keywords = ("rotation", "z-axis", "rotate", "counterclockwise", "axis", "3d", "spin", "arrow")

    def build(self) -> None:
        r = 18
        corner = (6, 14)
        self.add_arc("ring-bottom", (6, 24), (42, 24), radius_x=r, sweep=False)
        self.add_arc("ring-right", (42, 24), (24, 6), radius_x=r, sweep=False)
        self.add_bezier("ring-tail", (24, 6), ((17, 6), (11, 9), corner))
        self.add_contour("ring", "ring-bottom", "ring-right", "ring-tail")
        self.add_polyline("head", (6, 6), corner, (14, 14))
        self.relate("connect", "ring", "head")
        a = 5
        self.add_arc("axis-top", (24 - a, 24), (24 + a, 24), radius_x=a, sweep=True)
        self.add_arc("axis-bottom", (24 + a, 24), (24 - a, 24), radius_x=a, sweep=True)
        self.add_contour("axis", "axis-top", "axis-bottom", closed=True)
