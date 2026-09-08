"""A phone frame with a bottom navigation band.

VRECT_M: exact centerline extremes recorded in build.
Construction: Lucide smartphone, equal quarter-circle corner radii. Source identity retained without extra decoration.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class MobilePhoneDevice(Container64):
    icon_id = 'mobile-phone-device'
    keyshape = Keyshape.VRECT_M
    aliases = ()
    keywords = ('mobile', 'phone', 'device')

    def build(self) -> None:
        # Centerline (14,2)-(50,62).
        self.add_line('top', (20,2), (44,2))
        self.add_arc('ne', (44,2), (50,8), radius_x=6)
        self.add_line('right', (50,8), (50,56))
        self.add_arc('se', (50,56), (44,62), radius_x=6)
        self.add_line('bottom', (44,62), (20,62))
        self.add_arc('sw', (20,62), (14,56), radius_x=6)
        self.add_line('left', (14,56), (14,8))
        self.add_arc('nw', (14,8), (20,2), radius_x=6)
        self.add_contour('outline','top','ne','right','se','bottom','sw','left','nw',closed=True)
        self.add_line('bezel',(14,48),(50,48))
        self.relate('connect','outline','bezel')
