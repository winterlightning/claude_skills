"""Truck style (delivery), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76d08941-ee75-5b6a-94d2-97d9d4c45931'
SOURCE_PATH = 'icons-json/delivery/truck style_76d08941-ee75-5b6a-94d2-97d9d4c45931.json'
AUTHOR = 'json_to_solo'

class TruckStyleDelivery(Solo48):
    icon_id = 'truck-style-delivery'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'delivery'
    aliases = ()
    keywords = ('truck', 'style', 'delivery')

    def build(self):
        self.add_line('e0', (27, 8), (6, 8))
        self.add_line('e1', (4, 10), (4, 33))
        self.add_line('e2', (29, 13), (36, 13))
        self.add_line('e3', (39, 15), (42, 21))
        self.add_line('e4', (44, 25), (44, 33))
        self.add_line('e5', (29, 13), (29, 35))
        self.add_line('e6', (19, 35), (30, 35))
        self.add_line('e7', (44, 23), (29, 23))
        self.add_arc('e8-top', (9, 35), (19, 35), radius_x=5)
        self.add_arc('e8-bottom', (19, 35), (9, 35), radius_x=5)
        self.add_arc('e9-top', (30, 35), (40, 35), radius_x=5)
        self.add_arc('e9-bottom', (40, 35), (30, 35), radius_x=5)
        self.add_bezier('e10', (29, 13), ((29, 11.33), (28.7, 9.84), (27.755, 8.49)), ((27.664, 8.37), (27.455, 8), (27.282, 8)), ((27.1, 8), (27.182, 8), (27, 8)))
        self.add_bezier('e11', (6, 8), ((5.327, 8), (4.291, 8.79), (4.091, 9.49)), ((4, 9.93), (4.173, 9.54), (4, 10)))
        self.add_bezier('e12', (4, 33), ((4.109, 33.35), (4.055, 33.7), (4.318, 34)), ((5.445, 35.28), (7.573, 34.97), (9, 35)))
        self.add_bezier('e13', (36, 13), ((37.673, 13), (38.191, 13.22), (39, 15)))
        self.add_bezier('e14', (42, 21), ((42.255, 21.56), (44, 22.55), (44, 23)), ((44, 23.41), (43.991, 23.82), (43.991, 24.24)), ((43.991, 24.49), (44, 24.75), (44, 25)))
        self.add_bezier('e15', (44, 33), ((44, 33.1), (43.991, 33.19), (43.991, 33.29)), ((43.991, 35.67), (40.282, 35.02), (39, 35)))
        self.add_contour('c0', 'e10', 'e0', 'e11', 'e1', 'e12')
        self.add_contour('c1', 'e2', 'e13', 'e3', 'e14', 'e4', 'e15')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c1', 'e9')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'e8')
        self.relate('connect', 'c3', 'e9')
        self.relate('connect', 'c4', 'c1')
        self.relate('connect', 'c4', 'c2')
