"""Delivery truck (delivery), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5681dc04-4acc-5fc0-a848-54d569967f38'
SOURCE_PATH = 'icons-json/delivery/delivery truck_5681dc04-4acc-5fc0-a848-54d569967f38.json'
AUTHOR = 'json_to_solo'

class DeliveryTruck5681dc04(Solo48):
    icon_id = 'delivery-truck-5681dc04'
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
        self.add_bezier('e10', (40, 35), ((40.5, 35.03), (41.355, 35.05), (41.855, 35.12)), ((42.664, 35.25), (43.2, 35.46), (43.755, 34.69)), ((43.918, 34.46), (43.882, 34.23), (44, 34)))
        self.add_bezier('e11', (44, 24), ((44, 23.25), (43.355, 22.59), (43, 22)))
        self.add_bezier('e12', (39, 16), ((38.5, 15.17), (38.209, 12.99), (37.555, 12.4)), ((37.291, 12.18), (37.282, 12.15), (37, 12)))
        self.add_bezier('e13', (5, 35), ((4.491, 35), (4.018, 34.64), (4.018, 34.08)), ((4.018, 33.68), (4, 33.28), (4, 32.87)), ((4, 32.58), (4, 32.29), (4, 32)))
        self.add_bezier('e14', (4, 10), ((4.009, 9.92), (4.009, 9.83), (4.018, 9.75)), ((4.018, 8.91), (4.827, 8.02), (5.573, 8.02)), ((5.655, 8.01), (5.918, 8.01), (6, 8)))
        self.add_bezier('e15', (28, 8), ((28.091, 8.01), (27.818, 8.03), (27.909, 8.04)), ((28, 8.07), (28.091, 8.09), (28.182, 8.12)), ((28.982, 8.51), (28.718, 9.19), (29, 10)))
        self.add_contour('c0', 'e10', 'e0', 'e11', 'e1', 'e12', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e13', 'e5', 'e14', 'e6', 'e15', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'e8')
        self.relate('connect', 'c1', 'e9')
        self.relate('connect', 'c2', 'e9')
        self.relate('connect', 'c2', 'c1')
