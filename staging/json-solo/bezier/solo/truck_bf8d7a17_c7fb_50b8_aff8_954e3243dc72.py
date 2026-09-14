"""Truck (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf8d7a17-c7fb-50b8-aff8-954e3243dc72'
SOURCE_PATH = 'icons-json/transportation/truck_bf8d7a17-c7fb-50b8-aff8-954e3243dc72.json'
AUTHOR = 'json_to_solo'

class TruckBf8d7a17(Solo48):
    icon_id = 'truck-bf8d7a17'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('truck', 'transportation')

    def build(self):
        self.add_line('e0', (41, 35), (44, 35))
        self.add_line('e1', (44, 35), (44, 25))
        self.add_line('e2', (44, 25), (41, 20))
        self.add_line('e3', (41, 20), (39, 16))
        self.add_line('e4', (37, 14), (29, 14))
        self.add_line('e5', (32, 35), (18, 35))
        self.add_line('e6', (29, 35), (29, 8))
        self.add_line('e7', (29, 8), (4, 8))
        self.add_line('e8', (4, 8), (4, 35))
        self.add_line('e9', (9, 35), (4, 35))
        self.add_arc('e10-top', (8, 35), (18, 35), radius_x=5)
        self.add_arc('e10-bottom', (18, 35), (8, 35), radius_x=5)
        self.add_arc('e11-top', (32, 35), (42, 35), radius_x=5)
        self.add_arc('e11-bottom', (42, 35), (32, 35), radius_x=5)
        self.add_bezier('e12', (39, 16), ((38.464, 14.81), (38.236, 14), (37, 14)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e12', 'e4')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e6', 'e7', 'e8')
        self.add_contour('c3', 'e9')
        self.add_contour('e11', 'e11-top', 'e11-bottom', closed=True)
        self.add_contour('e10', 'e10-top', 'e10-bottom', closed=True)
        self.relate('connect', 'c0', 'e11')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'e11')
        self.relate('connect', 'c1', 'e10')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'e10')
