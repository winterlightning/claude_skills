"""Taller landscape display; retained sensor and bezel.
Independent review variant of landscape-mobile-phone. HRECT_XL CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [39, 32]. See container-fit-repair report for measured hosting results."""
SOURCE_PATH = None
SOURCE_ICON_ID = None
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class LandscapeMobilePhone(Container64):
    icon_id = 'landscape-mobile-phone'
    keyshape = Keyshape.HRECT_XL
    aliases = ('horizontal-phone',)
    keywords = ('landscape', 'mobile', 'phone')

    def build(self) -> None:
        self.add_line('frame-0', (8, 6), (56, 6))
        self.add_arc('frame-1', (56, 6), (62, 12), radius_x=6)
        self.add_line('frame-2', (62, 12), (62, 52))
        self.add_arc('frame-3', (62, 52), (56, 58), radius_x=6)
        self.add_line('frame-4', (56, 58), (8, 58))
        self.add_arc('frame-5', (8, 58), (2, 52), radius_x=6)
        self.add_line('frame-6', (2, 52), (2, 12))
        self.add_arc('frame-7', (2, 12), (8, 6), radius_x=6)
        self.add_contour('frame', 'frame-0', 'frame-1', 'frame-2', 'frame-3', 'frame-4', 'frame-5', 'frame-6', 'frame-7', closed=True)
        self.add_line('bezel-divider', (16, 6), (16, 58))
        self.relate('connect', 'frame', 'bezel-divider')
        self.add_dot('sensor', (9, 32))
