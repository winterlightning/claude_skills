"""Airplane with landing wheel: an airliner in side view flying right, with swept
upper and lower wings, a raised tail fin and one small wheel on a vertical strut
under the nose.

Symbol plan: one closed airframe outline. The body is a straight band y 18..26
ending in a radius-4 semicircular nose. The wings are sharp-cornered swept
quadrilaterals: the upper one rises to the top edge (roots x 24..34, tip x 20..30)
and the longer lower one drops to the bottom edge (roots x 20..29, tip x 15..25);
each is 8.6+ wide across its parallel-ish edges. At the rear a raised fin (top edge
y=13) curves down into the body top through one tangent cubic, and the underside
sweeps up from the belly to the fin corner in one smooth cubic. The strut drops
from the nose's lower junction (40,26) to a small radius-2 wheel (the approved
4-diameter circle) on the bottom edge.
Deliberate asymmetry: a directional side view.
Revision (reviewer: raised fin and smooth curved underside instead of the notched
arrow tail; smaller wheel on a vertical strut; sharp wing corners, smooth body):
all applied. The stroke stays the profile's 4 units, so the strut cannot be drawn
thinner than the outline.
Lucide construction: 'plane' - swept wings on a straight fuselage.
Keyshape HRECT_M: centerline x 4 (fin corner) .. 44 (nose), y 10 (upper wing) ..
38 (lower wing).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b7792e71-0de0-4b22-ab92-ffaf9912effd"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__airplane-with-landing-wheel/20260926T061914Z-thuan-mac/reference/plane with wheel_b7792e71-0de0-4b22-ab92-ffaf9912effd.svg"
AUTHOR = "claude-opus-5-5"


class AirplaneWithLandingWheel(Solo48):
    icon_id = "airplane-with-landing-wheel"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/air"
    aliases = ("plane-with-wheel", "landing-gear")
    keywords = ("airplane", "landing", "wheel", "landing-gear", "flight", "aircraft", "plane")

    def segments(self, name: str, *points: tuple[int, int]) -> list[str]:
        names = []
        for i, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f"{name}-{i}", a, b)
            names.append(f"{name}-{i}")
        return names

    def build(self) -> None:
        top, belly, nose_x = 18, 26, 40
        upper = self.segments("upper", (18, top), (24, top), (20, 10), (30, 10), (34, top), (nose_x, top))
        self.add_arc("nose-upper", (nose_x, top), (44, 22), radius_x=4, sweep=True)
        self.add_arc("nose-lower", (44, 22), (nose_x, belly), radius_x=4, sweep=True)
        lower = self.segments("lower", (nose_x, belly), (29, belly), (25, 38), (15, 38), (20, belly), (15, belly))
        self.add_bezier("underside", (15, belly), ((10, 26), (5, 22), (4, 13)))
        self.add_line("fin-top", (4, 13), (9, 13))
        self.add_bezier("fin-back", (9, 13), ((13, 13), (13, 18), (18, 18)))
        self.add_contour("airframe", *upper, "nose-upper", "nose-lower", *lower, "underside",
                         "fin-top", "fin-back", closed=True)
        self.add_line("strut", (nose_x, belly), (nose_x, 34))
        self.add_arc("wheel-right", (nose_x, 34), (nose_x, 38), radius_x=2, sweep=True)
        self.add_arc("wheel-left", (nose_x, 38), (nose_x, 34), radius_x=2, sweep=True)
        self.add_contour("wheel", "wheel-right", "wheel-left", closed=True)
        self.relate("connect", "airframe", "strut")
        self.relate("connect", "strut", "wheel")
