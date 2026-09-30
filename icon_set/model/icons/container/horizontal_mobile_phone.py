"""Taller landscape display; retained left bezel divider.
Independent review variant of horizontal-mobile-phone. HRECT_XL CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [37, 32]. See container-fit-repair report for measured hosting results.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (horizontal-mobile-phone HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class HorizontalMobilePhone(Container64):
    icon_id = 'horizontal-mobile-phone'
    keyshape = Keyshape.HRECT_L
    aliases = ()
    keywords = ('horizontal', 'mobile', 'phone')

    def build(self) -> None:
        self.add_line('outline-0', (10, 10), (54, 10))
        self.add_arc('outline-1', (54, 10), (60, 16), radius_x=6)
        self.add_line('outline-2', (60, 16), (60, 48))
        self.add_arc('outline-3', (60, 48), (54, 54), radius_x=6)
        self.add_line('outline-4', (54, 54), (10, 54))
        self.add_arc('outline-5', (10, 54), (4, 48), radius_x=6)
        self.add_line('outline-6', (4, 48), (4, 16))
        self.add_arc('outline-7', (4, 16), (10, 10), radius_x=6)
        self.add_line('bezel', (14, 10), (14, 54))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.relate('connect', 'outline', 'bezel')
