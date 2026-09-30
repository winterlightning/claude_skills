"""Taller landscape display; retained sensor and bezel.
Independent review variant of landscape-mobile-phone. HRECT_XL CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [39, 32]. See container-fit-repair report for measured hosting results.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (landscape-mobile-phone HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class LandscapeMobilePhone(Container64):
    icon_id = 'landscape-mobile-phone'
    keyshape = Keyshape.HRECT_L
    aliases = ('horizontal-phone',)
    keywords = ('landscape', 'mobile', 'phone')

    def build(self) -> None:
        self.add_line('frame-0', (10, 10), (54, 10))
        self.add_arc('frame-1', (54, 10), (60, 16), radius_x=6)
        self.add_line('frame-2', (60, 16), (60, 48))
        self.add_arc('frame-3', (60, 48), (54, 54), radius_x=6)
        self.add_line('frame-4', (54, 54), (10, 54))
        self.add_arc('frame-5', (10, 54), (4, 48), radius_x=6)
        self.add_line('frame-6', (4, 48), (4, 16))
        self.add_arc('frame-7', (4, 16), (10, 10), radius_x=6)
        self.add_line('bezel-divider', (18, 10), (18, 54))
        self.add_dot('sensor', (11, 32))
        self.add_contour('frame', 'frame-0', 'frame-1', 'frame-2', 'frame-3', 'frame-4', 'frame-5', 'frame-6', 'frame-7', closed=True)
        self.relate('connect', 'frame', 'bezel-divider')
