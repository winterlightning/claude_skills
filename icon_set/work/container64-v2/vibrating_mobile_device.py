"""A mobile device flanked by two vibration strokes.

Keyshape SQUARE, bounds (0, 0, 64, 64): chosen for the reference proportions.
Lucide construction: smartphone: equal corner radii and parallel sides. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (vibrating-mobile-device SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class VibratingMobileDevice(Container64):
    icon_id = 'vibrating-mobile-device'
    keyshape = Keyshape.SQUARE
    aliases = ('vibration-mode', 'silent-mode')
    keywords = ('vibrating', 'mobile', 'device')

    def build(self) -> None:
        self.add_line('device-0', (18, 6), (46, 6))
        self.add_arc('device-1', (46, 6), (50, 10), radius_x=4)
        self.add_line('device-2', (50, 10), (50, 54))
        self.add_arc('device-3', (50, 54), (46, 58), radius_x=4)
        self.add_line('device-4', (46, 58), (18, 58))
        self.add_arc('device-5', (18, 58), (14, 54), radius_x=4)
        self.add_line('device-6', (14, 54), (14, 10))
        self.add_arc('device-7', (14, 10), (18, 6), radius_x=4)
        self.add_line('vibration-left', (6, 16), (6, 48))
        self.add_line('vibration-right', (58, 16), (58, 48))
        self.add_contour('device', 'device-0', 'device-1', 'device-2', 'device-3', 'device-4', 'device-5', 'device-6', 'device-7', closed=True)
