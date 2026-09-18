"""Wider phone display; retained bottom navigation band and equal corner radii.
Independent review variant of mobile-phone-device. VRECT_XL CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [32, 25]. See container-fit-repair report for measured hosting results."""
SOURCE_PATH = None
SOURCE_ICON_ID = None
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class MobilePhoneDeviceVariant2(Container64):
    icon_id = 'mobile-phone-device-v2'
    variant_of = 'mobile-phone-device'
    variant_label = 'Native SUB32 clearance'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('mobile', 'phone', 'device')

    def build(self) -> None:
        self.add_line('top', (12, 2), (52, 2))
        self.add_arc('ne', (52, 2), (58, 8), radius_x=6)
        self.add_line('right', (58, 8), (58, 56))
        self.add_arc('se', (58, 56), (52, 62), radius_x=6)
        self.add_line('bottom', (52, 62), (12, 62))
        self.add_arc('sw', (12, 62), (6, 56), radius_x=6)
        self.add_line('left', (6, 56), (6, 8))
        self.add_arc('nw', (6, 8), (12, 2), radius_x=6)
        self.add_contour('outline', 'top', 'ne', 'right', 'se', 'bottom', 'sw', 'left', 'nw', closed=True)
        self.add_line('bezel', (6, 48), (58, 48))
        self.relate('connect', 'outline', 'bezel')
