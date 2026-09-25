"""Fender: the front section of a car in side view - rounded cabin with a
sloping windshield on the belt line, hood curving down into the nose, and
the front wheel with its hub breaking the body's bottom line.

Symbol plan: the body is one open run from the wheel's right node round the
nose, hood, belt line, left edge and bottom to the wheel's left node; the
wheel is a radius-8 circle split at those two nodes kept plain (a hub
would sit inside the 8-unit clearance). The cabin is an open run (radius-8 corner, roof, windshield curve)
standing on two belt-line nodes. Keyshape HRECT_L, centerline box
(4,8)-(44,40).
Lucide construction: car-front / car (rounded cabin over a body line,
wheel circles interrupting the sill).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3db3961f-b690-449d-b4da-3a42295c5b5d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__front-car-section-with-wheel/20260925T092530Z-thuan-mac/reference/fender_3db3961f-b690-449d-b4da-3a42295c5b5d.svg"
AUTHOR = "claude-opus-5-5"


class FrontCarSectionWithWheel(Solo48):
    icon_id = "front-car-section-with-wheel"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport"
    aliases = ("fender", "car side", "car front")
    keywords = ("car", "fender", "wheel", "vehicle", "auto", "body")

    def build(self) -> None:
        wx, wy, r = 28, 32, 8
        belt = 16
        cabin_left, windshield_foot = (8, belt), (32, belt)
        # Body: wheel right -> nose -> hood -> belt -> left edge -> wheel left.
        self.add_line("body-1", (wx + r, wy), (40, wy))
        self.add_arc("body-2", (40, wy), (44, 28), radius_x=4, sweep=False)
        self.add_line("body-3", (44, 28), (44, 24))
        self.add_bezier("body-4", (44, 24), ((44, 18), (38, belt), windshield_foot))
        self.add_line("body-5", windshield_foot, cabin_left)
        self.add_line("body-6", cabin_left, (4, belt))
        self.add_line("body-7", (4, belt), (4, 28))
        self.add_arc("body-8", (4, 28), (8, wy), radius_x=4, sweep=False)
        self.add_line("body-9", (8, wy), (wx - r, wy))
        self.add_contour("body", *[f"body-{i}" for i in range(1, 10)])
        # Wheel, split at the nodes where the sill meets it.
        self.add_arc("wheel-1", (wx - r, wy), (wx + r, wy), radius_x=r)
        self.add_arc("wheel-2", (wx + r, wy), (wx - r, wy), radius_x=r)
        self.add_contour("wheel", "wheel-1", "wheel-2", closed=True)
        # Cabin standing on the belt line.
        self.add_arc("cabin-1", cabin_left, (16, 8), radius_x=8)
        self.add_line("cabin-2", (16, 8), (22, 8))
        self.add_bezier("cabin-3", (22, 8), ((26, 8), (29, 11), windshield_foot))
        self.add_contour("cabin", "cabin-1", "cabin-2", "cabin-3")
        self.relate("connect", "body", "wheel")
        self.relate("connect", "body", "cabin")
