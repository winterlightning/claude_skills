"""A mobile device flanked by two vibration strokes.

Keyshape SQUARE, bounds (0, 0, 64, 64): chosen for the reference proportions.
Lucide construction: smartphone: equal corner radii and parallel sides. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class VibratingMobileDevice(Container64):
    icon_id = 'vibrating-mobile-device'
    keyshape = Keyshape.SQUARE
    aliases = ('vibration-mode', 'silent-mode')
    keywords = ('vibrating', 'mobile', 'device')

    def build(self) -> None:
        self.add_line('device-0', (14, 2), (50, 2))
        self.add_arc('device-1', (50, 2), (54, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_line('device-2', (54, 6), (54, 58))
        self.add_arc('device-3', (54, 58), (50, 62), radius_x=4, radius_y=4, sweep=True)
        self.add_line('device-4', (50, 62), (14, 62))
        self.add_arc('device-5', (14, 62), (10, 58), radius_x=4, radius_y=4, sweep=True)
        self.add_line('device-6', (10, 58), (10, 6))
        self.add_arc('device-7', (10, 6), (14, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('device', 'device-0', 'device-1', 'device-2', 'device-3', 'device-4', 'device-5', 'device-6', 'device-7', closed=True)
        self.add_line('vibration-left', (2, 12), (2, 52))
        self.add_line('vibration-right', (62, 12), (62, 52))
