"""Taller landscape display; retained left bezel divider.
Independent review variant of horizontal-mobile-phone. HRECT_XL CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [37, 32]. See container-fit-repair report for measured hosting results."""
SOURCE_PATH = None
SOURCE_ICON_ID = None
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class HorizontalMobilePhone(Container64):
    icon_id = 'horizontal-mobile-phone'
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ('horizontal', 'mobile', 'phone')

    def build(self) -> None:
        self.add_line('outline-0', (8, 6), (56, 6))
        self.add_arc('outline-1', (56, 6), (62, 12), radius_x=6, radius_y=6, sweep=True)
        self.add_line('outline-2', (62, 12), (62, 52))
        self.add_arc('outline-3', (62, 52), (56, 58), radius_x=6, radius_y=6, sweep=True)
        self.add_line('outline-4', (56, 58), (8, 58))
        self.add_arc('outline-5', (8, 58), (2, 52), radius_x=6, radius_y=6, sweep=True)
        self.add_line('outline-6', (2, 52), (2, 12))
        self.add_arc('outline-7', (2, 12), (8, 6), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.add_line('bezel', (12, 6), (12, 58))
        self.relate('connect', 'outline', 'bezel')
