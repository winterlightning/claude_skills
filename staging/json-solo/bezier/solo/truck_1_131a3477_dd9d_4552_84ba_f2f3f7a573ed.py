"""Truck 1 (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '131a3477-dd9d-4552-84ba-f2f3f7a573ed'
SOURCE_PATH = 'icons-json/transportation/truck 1_131a3477-dd9d-4552-84ba-f2f3f7a573ed.json'
AUTHOR = 'json_to_solo'

class Truck1Transportation(Solo48):
    icon_id = 'truck-1-transportation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('truck', 'transportation')

    def build(self):
        self.add_line('e0', (44, 32), (44, 27))
        self.add_line('e1', (44, 23), (34, 23))
        self.add_line('e2', (31, 34), (19, 34))
        self.add_line('e3', (9, 34), (6, 34))
        self.add_line('e4', (4, 32), (4, 10))
        self.add_line('e5', (6, 8), (28, 8))
        self.add_line('e6', (28, 8), (28, 34))
        self.add_line('e7', (44, 23), (39, 15))
        self.add_line('e8', (36, 12), (28, 12))
        self.add_arc('e9-top', (9, 35), (19, 35), radius_x=5)
        self.add_arc('e9-bottom', (19, 35), (9, 35), radius_x=5)
        self.add_arc('e10-top', (31, 35), (41, 35), radius_x=5)
        self.add_arc('e10-bottom', (41, 35), (31, 35), radius_x=5)
        self.add_bezier('e11', (40, 35), ((41.727, 34.91), (44, 34.4), (44, 32)))
        self.add_bezier('e12', (44, 27), ((44, 25.67), (44, 24.33), (44, 23)))
        self.add_bezier('e13', (6, 34), ((4.7, 33.43), (4.509, 33.41), (4, 32)))
        self.add_bezier('e14', (4, 10), ((4.3, 9.32), (4.564, 8.51), (5.255, 8.14)), ((5.345, 8.11), (5.436, 8.09), (5.527, 8.06)), ((5.618, 8.04), (5.9, 8.02), (6, 8)))
        self.add_bezier('e15', (39, 15), ((38.173, 13.54), (37.7, 12), (36, 12)))
        self.add_contour('c0', 'e11', 'e0', 'e12', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e13', 'e4', 'e14', 'e5', 'e6')
        self.add_contour('c3', 'e7', 'e15', 'e8')
        self.add_contour('e10', 'e10-top', 'e10-bottom', closed=True)
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'e10')
        self.relate('connect', 'c1', 'e10')
        self.relate('connect', 'c1', 'e9')
        self.relate('connect', 'c2', 'e9')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c2')
