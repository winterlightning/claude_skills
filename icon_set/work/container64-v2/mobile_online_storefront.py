"""A mobile shop with a scalloped awning and a bottom phone bezel.

VRECT_L: exact centerline extremes recorded in build.
Construction: Lucide store and smartphone, repeated canopy lobes and equal body corners. Source identity retained without extra decoration.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (mobile-online-storefront VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class MobileOnlineStorefront(Container64):
    icon_id = 'mobile-online-storefront'
    keyshape = Keyshape.VRECT_M
    aliases = ('smartphone-with-shop-awning',)
    keywords = ('mobile', 'online', 'storefront')

    def build(self) -> None:
        self.add_line('awning-top', (22, 4), (42, 4))
        self.add_arc('awning-ne', (42, 4), (48, 10), radius_x=6)
        self.add_line('awning-slope-right', (48, 10), (52, 18))
        self.add_arc('scallop-right-a', (52, 18), (46, 22), radius_x=6, radius_y=4)
        self.add_arc('scallop-right-b', (46, 22), (40, 18), radius_x=6, radius_y=4)
        self.add_arc('scallop-mid-right', (40, 18), (32, 18), radius_x=4)
        self.add_arc('scallop-mid-left', (32, 18), (24, 18), radius_x=4)
        self.add_arc('scallop-left-a', (24, 18), (18, 22), radius_x=6, radius_y=4)
        self.add_arc('scallop-left-b', (18, 22), (12, 18), radius_x=6, radius_y=4)
        self.add_line('awning-slope-left', (12, 18), (16, 10))
        self.add_arc('awning-nw', (16, 10), (22, 4), radius_x=6)
        self.add_line('body-right', (46, 22), (46, 54))
        self.add_arc('body-se', (46, 54), (40, 60), radius_x=6)
        self.add_line('body-bottom', (40, 60), (24, 60))
        self.add_arc('body-sw', (24, 60), (18, 54), radius_x=6)
        self.add_line('body-left', (18, 54), (18, 22))
        self.add_line('bezel', (18, 48), (46, 48))
        self.add_line('rib-left', (24, 18), (26, 11))
        self.add_line('rib-center', (32, 18), (32, 11))
        self.add_line('rib-right', (40, 18), (38, 11))
        self.add_contour('awning', 'awning-top', 'awning-ne', 'awning-slope-right', 'scallop-right-a', 'scallop-right-b', 'scallop-mid-right', 'scallop-mid-left', 'scallop-left-a', 'scallop-left-b', 'awning-slope-left', 'awning-nw', closed=True)
        self.add_contour('body', 'body-right', 'body-se', 'body-bottom', 'body-sw', 'body-left')
        self.relate('connect', 'bezel', 'body')
        self.relate('connect', 'awning', 'body')
        self.relate('connect', 'awning', 'rib-left')
        self.relate('connect', 'awning', 'rib-center')
        self.relate('connect', 'awning', 'rib-right')
