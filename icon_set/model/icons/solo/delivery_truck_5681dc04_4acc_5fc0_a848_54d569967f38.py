"""Delivery truck (delivery), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5681dc04-4acc-5fc0-a848-54d569967f38'
SOURCE_PATH = 'icons-json/delivery/delivery truck_5681dc04-4acc-5fc0-a848-54d569967f38.json'
AUTHOR = 'json_to_solo'

class DeliveryTruckDelivery(Solo48):
    icon_id = 'delivery-truck-delivery'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'delivery'
    aliases = ()
    keywords = ('delivery', 'truck')

    def build(self):
        self.add_line('e0', (44, 34), (44, 24))
        self.add_line('e1', (43, 22), (39, 16))
        self.add_line('e2', (37, 12), (29, 12))
        self.add_line('e3', (31, 35), (18, 35))
        self.add_line('e4', (9, 35), (5, 35))
        self.add_line('e5', (4, 32), (4, 10))
        self.add_line('e6', (6, 8), (28, 8))
        self.add_line('e7', (29, 10), (29, 35))
        self.add_arc('e8-top', (31, 35), (41, 35), radius_x=5)
        self.add_arc('e8-bottom', (41, 35), (31, 35), radius_x=5)
        self.add_arc('e9-top', (8, 35), (18, 35), radius_x=5)
        self.add_arc('e9-bottom', (18, 35), (8, 35), radius_x=5)
        self.add_arc('e10', (40, 35), (44, 34), radius_x=3, sweep=False)
        self.add_arc('e11', (44, 24), (43, 22), radius_x=4, sweep=False)
        self.add_arc('e12', (39, 16), (37, 12), radius_x=4, sweep=False)
        self.add_line('e13-1', (5, 35), (4, 33))
        self.add_line('e13-2', (4, 33), (4, 32))
        self.add_arc('e14', (4, 10), (6, 8), radius_x=2)
        self.add_arc('e15', (28, 8), (29, 10), radius_x=2)
        self.add_contour('c0', 'e10', 'e0', 'e11', 'e1', 'e12', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e13-1', 'e13-2', 'e5', 'e14', 'e6', 'e15', 'e7')
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'e8')
        self.relate('connect', 'c1', 'e9')
        self.relate('connect', 'c2', 'e9')
        self.relate('connect', 'c2', 'c1')
