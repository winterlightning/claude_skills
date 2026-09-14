"""Network and content delivery (websites), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f8a80ae-63cc-53f7-8f79-a6416f714365'
SOURCE_PATH = 'icons-json/websites/network and content delivery_6f8a80ae-63cc-53f7-8f79-a6416f714365.json'
AUTHOR = 'json_to_solo'

class NetworkAndContentDeliveryWebsites(Solo48):
    icon_id = 'network-and-content-delivery-websites'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    aliases = ()
    keywords = ('network', 'and', 'content', 'delivery', 'websites')

    def build(self):
        self.add_line('e0', (13, 39), (24, 29))
        self.add_line('e1', (24, 28), (24, 40))
        self.add_line('e2', (24, 29), (36, 39))
        self.add_line('e3', (16, 28), (26, 28))
        self.add_line('e4', (26, 28), (35, 28))
        self.add_arc('e5-top', (22, 42), (26, 42), radius_x=2)
        self.add_arc('e5-bottom', (26, 42), (22, 42), radius_x=2)
        self.add_arc('e6-1', (35, 28), (39, 24), radius_x=7, sweep=False)
        self.add_arc('e6-2', (39, 24), (40, 20), radius_x=9, sweep=False)
        self.add_arc('e6-3', (40, 20), (35, 12), radius_x=9, sweep=False)
        self.add_arc('e6-4', (35, 12), (30, 12), radius_x=8, sweep=False)
        self.add_arc('e6-5', (30, 12), (29, 12), radius_x=1)
        self.add_arc('e6-6', (29, 12), (26, 7), radius_x=13, sweep=False)
        self.add_arc('e6-7', (26, 7), (23, 5), radius_x=10, sweep=False)
        self.add_line('e6-8', (23, 5), (18, 4))
        self.add_arc('e6-9', (18, 4), (10, 9), radius_x=9, sweep=False)
        self.add_line('e6-10', (10, 9), (8, 16))
        self.add_line('e6-11', (8, 16), (10, 23))
        self.add_line('e6-12', (10, 23), (16, 28))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7', 'e6-8', 'e6-9', 'e6-10', 'e6-11', 'e6-12', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'e5')
