"""Jeep: a boxy off-road vehicle in side view - a long flat body with rounded
top corners, a small cabin with a sloping windshield at the front (left),
and two large wheels.

Symbol plan: the body is one open run from the rear wheel's right node up
the rear side, over the top (radius-4 corners) and down the front side to
the front wheel's left node, plus the sill between the wheels. Each wheel is
a radius-8 circle split at its left and right nodes so the body sides and
sill end on it tangentially. The cabin is an open trapezoid standing on two
split nodes of the body top. Wheels mirror about x = 24.
Keyshape HRECT_L, centerline box (4,8)-(44,40).
Lucide construction: truck / car (body outline broken by wheel circles,
cabin on top).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "87fdb6c4-b392-445f-b29f-1ee390cf87cd"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__simple-off-road-vehicle/20260925T092530Z-thuan-mac/reference/jeep_87fdb6c4-b392-445f-b29f-1ee390cf87cd.svg"
AUTHOR = "claude-opus-5-5"


class SimpleOffRoadVehicle(Solo48):
    icon_id = "simple-off-road-vehicle"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport"
    aliases = ("jeep", "off-road vehicle", "4x4")
    keywords = ("jeep", "car", "vehicle", "off-road", "4x4", "suv")

    def build(self) -> None:
        top, axle, r = 16, 32, 8
        front, rear = 12, 36                     # wheel centres
        cab_front, cab_rear = (12, top), (26, top)
        self.add_line("body-1", (rear + r, axle), (44, 20))
        self.add_arc("body-2", (44, 20), (40, top), radius_x=4, sweep=False)
        self.add_line("body-3", (40, top), cab_rear)
        self.add_line("body-4", cab_rear, cab_front)
        self.add_line("body-5", cab_front, (8, top))
        self.add_arc("body-6", (8, top), (4, 20), radius_x=4, sweep=False)
        self.add_line("body-7", (4, 20), (front - r, axle))
        self.add_contour("body", *[f"body-{i}" for i in range(1, 8)])
        self.add_line("sill", (front + r, axle), (rear - r, axle))
        for name, cx in (("wheel-front", front), ("wheel-rear", rear)):
            self.add_arc(f"{name}-1", (cx - r, axle), (cx + r, axle), radius_x=r)
            self.add_arc(f"{name}-2", (cx + r, axle), (cx - r, axle), radius_x=r)
            self.add_contour(name, f"{name}-1", f"{name}-2", closed=True)
            self.relate("connect", "body", name)
            self.relate("connect", "sill", name)
        self.add_polyline("cabin", cab_front, (16, 8), (26, 8), cab_rear)
        self.relate("connect", "body", "cabin")
