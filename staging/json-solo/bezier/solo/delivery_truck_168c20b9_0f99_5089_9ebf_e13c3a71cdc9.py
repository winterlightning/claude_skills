"""Delivery truck (delivery), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '168c20b9-0f99-5089-9ebf-e13c3a71cdc9'
SOURCE_PATH = 'icons-json/delivery/delivery truck_168c20b9-0f99-5089-9ebf-e13c3a71cdc9.json'
AUTHOR = 'json_to_solo'

class DeliveryTruck168c20b9(Solo48):
    icon_id = 'delivery-truck-168c20b9'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'delivery'
    aliases = ()
    keywords = ('delivery', 'truck')

    def build(self):
        self.add_line('e0', (44, 33), (44, 24))
        self.add_line('e1', (43, 21), (40, 16))
        self.add_line('e2', (38, 14), (30, 14))
        self.add_line('e3', (4, 33), (4, 9))
        self.add_line('e4', (6, 8), (28, 8))
        self.add_line('e5', (30, 12), (30, 35))
        self.add_line('e6', (32, 35), (19, 35))
        self.add_line('e7', (44, 23), (30, 23))
        self.add_arc('e8-top', (32, 35), (42, 35), radius_x=5)
        self.add_arc('e8-bottom', (42, 35), (32, 35), radius_x=5)
        self.add_arc('e9-top', (9, 35), (19, 35), radius_x=5)
        self.add_arc('e9-bottom', (19, 35), (9, 35), radius_x=5)
        self.add_bezier('e10', (41, 35), ((41.873, 34.77), (44, 34.47), (44, 33)))
        self.add_bezier('e11', (44, 24), ((44, 23.67), (44, 23.33), (44, 23)), ((44, 22.63), (43.2, 21.36), (43, 21)))
        self.add_bezier('e12', (40, 16), ((39.473, 15.04), (39.091, 14), (38, 14)))
        self.add_bezier('e13', (9, 35), ((7.6, 34.99), (4, 35.69), (4, 33)))
        self.add_bezier('e14', (4, 9), ((4.055, 8.88), (4.109, 8.76), (4.164, 8.64)), ((4.373, 8.24), (5.045, 8.01), (5.455, 8.01)), ((5.518, 8.01), (5.573, 8), (5.636, 8)), ((5.7, 8), (5.936, 8), (6, 8)))
        self.add_bezier('e15', (28, 8), ((28.2, 8), (28.036, 8.02), (28.236, 8.02)), ((30.564, 8.02), (30, 10.1), (30, 12)))
        self.add_contour('c0', 'e10', 'e0', 'e11', 'e1', 'e12', 'e2')
        self.add_contour('c1', 'e13', 'e3', 'e14', 'e4', 'e15', 'e5')
        self.add_contour('c2', 'e6')
        self.add_contour('c3', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'e9')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'e8')
        self.relate('connect', 'c2', 'e9')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c3', 'c1')
