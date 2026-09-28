"""Airplane (side view, climbing): an airliner tilted up to the right with a broad
rounded nose, a long straight belly that curves smoothly into the rear, a large
angular wing toward the upper left and a small tail fin at the left, separated
from the wing by a deep V notch.

Symbol plan: one closed outline. The belly is a straight run of direction (-12,7)
(about 30 degrees of climb); the body top is parallel to it about 10 higher, so
the body keeps an even thickness. The nose is a radius-6 quarter arc over the top
and right, closed into the belly by one tangent cubic; the rear is two tangent
cubics through the lowest point (12,38). The wing is a 45-degree parallelogram band
8.5 wide rising from the body top to the top edge. The tail fin rises at the rear;
its back edge and the wing's trailing edge meet in the V notch on the body top.
Deliberate asymmetry: a directional side view.
Revision (reviewer feedback above): the rejected drawing was a symmetric top view.
Lucide construction: 'plane-takeoff' - climbing side view with wing and fin.
Keyshape HRECT_M: centerline x 4 (tail tip) .. 44 (nose), y 10 (nose, wing tip)
.. 38 (rear belly).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "4a625cc1-8989-433b-89db-ddf1b6a98ffe"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__airplane-other/20260926T061914Z-thuan-mac/reference/airplane_4a625cc1-8989-433b-89db-ddf1b6a98ffe.svg"
AUTHOR = "claude-opus-5-5"


class AirplaneOther(Solo48):
    icon_id = "ascending-commercial-airplane"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/air"
    aliases = ("airplane", "plane-side-view")
    keywords = ("airplane", "plane", "flight", "takeoff", "travel", "aircraft", "jet")

    def segments(self, name: str, *points: tuple[int, int]) -> list[str]:
        names = []
        for i, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f"{name}-{i}", a, b)
            names.append(f"{name}-{i}")
        return names

    def build(self) -> None:
        root = (27, 18)
        self.add_bezier("body-top", root, ((31, 15.7), (34.5, 10), (38, 10)))
        self.add_arc("nose", (38, 10), (44, 16), radius_x=6, sweep=True)
        self.add_bezier("chin", (44, 16), ((44, 19), (42, 20.8), (40, 22)))
        self.add_line("belly", (40, 22), (16, 36))
        self.add_bezier("rear", (16, 36), ((14.3, 37), (13.5, 38), (12, 38)),
                        ((10, 38), (8, 37), (7, 35)))
        tail = self.segments("tail", (7, 35), (4, 25), (8, 22), (19, 22))
        wing = self.segments("wing", (19, 22), (11, 14), (19, 10), root)
        self.add_contour("airframe", "body-top", "nose", "chin", "belly", "rear", *tail, *wing,
                         closed=True)
