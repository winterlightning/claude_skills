"""Wider phone display; retained bottom navigation band and equal corner radii.
Independent review variant of mobile-phone-device. VRECT_XL CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [32, 25]. See container-fit-repair report for measured hosting results.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (mobile-phone-device VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class MobilePhoneDevice(Container64):
    icon_id = 'mobile-phone-device'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('mobile', 'phone', 'device')

    def build(self) -> None:
        self.add_line('top', (16, 4), (48, 4))
        self.add_arc('ne', (48, 4), (54, 10), radius_x=6)
        self.add_line('right', (54, 10), (54, 54))
        self.add_arc('se', (54, 54), (48, 60), radius_x=6)
        self.add_line('bottom', (48, 60), (16, 60))
        self.add_arc('sw', (16, 60), (10, 54), radius_x=6)
        self.add_line('left', (10, 54), (10, 10))
        self.add_arc('nw', (10, 10), (16, 4), radius_x=6)
        self.add_line('bezel', (10, 46), (54, 46))
        self.add_contour('outline', 'top', 'ne', 'right', 'se', 'bottom', 'sw', 'left', 'nw', closed=True)
        self.relate('connect', 'outline', 'bezel')
