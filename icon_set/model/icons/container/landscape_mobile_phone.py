"""A landscape phone enclosure with a sensor in its left bezel.

Keyshape HRECT_M: centerline extremes recorded in build below.
Lucide smartphone supplies tangent quarter-circle corners and a single sensor mark. Both supplied phone references map here; the left bezel is widened for clearance.
Hosting (compose.py): plus invalid, heart invalid, check invalid.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class LandscapeMobilePhone(Container64):
    icon_id = 'landscape-mobile-phone'
    keyshape = Keyshape.HRECT_M
    aliases = ('horizontal-phone',)
    keywords = ('landscape', 'mobile', 'phone')

    def build(self) -> None:
        # HRECT_M centerline extremes: (2,14)-(62,50).
        self.add_line("frame-0", (8, 14), (56, 14))
        self.add_arc("frame-1", (56, 14), (62, 20), radius_x=6)
        self.add_line("frame-2", (62, 20), (62, 44))
        self.add_arc("frame-3", (62, 44), (56, 50), radius_x=6)
        self.add_line("frame-4", (56, 50), (8, 50))
        self.add_arc("frame-5", (8, 50), (2, 44), radius_x=6)
        self.add_line("frame-6", (2, 44), (2, 20))
        self.add_arc("frame-7", (2, 20), (8, 14), radius_x=6)
        self.add_contour("frame", "frame-0", "frame-1", "frame-2", "frame-3", "frame-4", "frame-5", "frame-6", "frame-7", closed=True)
        self.add_line("bezel-divider", (16,14), (16,50))
        self.relate("connect", "frame", "bezel-divider")
        self.add_dot("sensor", (9,32))
