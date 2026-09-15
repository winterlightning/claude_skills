"""A mobile shop with a scalloped awning and a bottom phone bezel.

VRECT_L: exact centerline extremes recorded in build.
Construction: Lucide store and smartphone, repeated canopy lobes and equal body corners. Source identity retained without extra decoration.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class MobileOnlineStorefront(Container64):
    icon_id = 'mobile-online-storefront'
    keyshape = Keyshape.VRECT_L
    aliases = ('smartphone-with-shop-awning',)
    keywords = ('mobile', 'online', 'storefront')

    def build(self) -> None:
        # Centerline (10,2)-(54,62).
        self.add_line('awning-top',(20,2),(44,2))
        self.add_arc('awning-ne',(44,2),(50,8),radius_x=6)
        self.add_line('awning-slope-right',(50,8),(54,16))
        self.add_arc('scallop-right-a',(54,16),(48,20),radius_x=6,radius_y=4)
        self.add_arc('scallop-right-b',(48,20),(42,16),radius_x=6,radius_y=4)
        self.add_arc('scallop-mid-right',(42,16),(32,16),radius_x=5,radius_y=4)
        self.add_arc('scallop-mid-left',(32,16),(22,16),radius_x=5,radius_y=4)
        self.add_arc('scallop-left-a',(22,16),(16,20),radius_x=6,radius_y=4)
        self.add_arc('scallop-left-b',(16,20),(10,16),radius_x=6,radius_y=4)
        self.add_line('awning-slope-left',(10,16),(14,8))
        self.add_arc('awning-nw',(14,8),(20,2),radius_x=6)
        self.add_contour('awning','awning-top','awning-ne','awning-slope-right','scallop-right-a','scallop-right-b','scallop-mid-right','scallop-mid-left','scallop-left-a','scallop-left-b','awning-slope-left','awning-nw',closed=True)
        self.add_line('body-right',(48,20),(48,56))
        self.add_arc('body-se',(48,56),(42,62),radius_x=6)
        self.add_line('body-bottom',(42,62),(22,62))
        self.add_arc('body-sw',(22,62),(16,56),radius_x=6)
        self.add_line('body-left',(16,56),(16,20))
        self.add_contour('body','body-right','body-se','body-bottom','body-sw','body-left')
        self.add_line('bezel',(16,50),(48,50))
        self.relate('connect','bezel','body')

        self.relate('connect','awning','body')
        for name, a, b in [('rib-left',(22,16),(24,9)),('rib-center',(32,16),(32,9)),('rib-right',(42,16),(40,9))]:
            self.add_line(name,a,b)
            self.relate('connect','awning',name)
