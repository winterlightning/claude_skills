"""Car (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1ae9ac1-dad6-526e-975f-e2ee61a2940d'
SOURCE_PATH = 'icons-json/transportation/car_e1ae9ac1-dad6-526e-975f-e2ee61a2940d.json'
AUTHOR = 'json_to_solo'

class CarE1ae9ac1(Solo48):
    icon_id = 'car-e1ae9ac1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'transportation')

    def build(self):
        self.add_line('e0', (9, 19), (15, 19))
        self.add_line('e1', (15, 19), (38, 19))
        self.add_line('e2', (44, 28), (44, 31))
        self.add_line('e3', (44, 33), (39, 33))
        self.add_line('e4', (30, 8), (23, 8))
        self.add_line('e5', (17, 34), (30, 34))
        self.add_line('e6', (28, 8), (28, 19))
        self.add_arc('e7-top', (7, 34), (17, 34), radius_x=5, radius_y=6)
        self.add_arc('e7-bottom', (17, 34), (7, 34), radius_x=5, radius_y=6)
        self.add_arc('e8-top', (30, 34), (40, 34), radius_x=5, radius_y=6)
        self.add_arc('e8-bottom', (40, 34), (30, 34), radius_x=5, radius_y=6)
        self.add_arc('e9-1', (8, 34), (4, 32), radius_x=3)
        self.add_arc('e9-2', (4, 32), (4, 28), radius_x=53, sweep=False)
        self.add_line('e9-3', (4, 28), (5, 23))
        self.add_arc('e9-4', (5, 23), (9, 19), radius_x=9)
        self.add_arc('e10-1', (38, 19), (42, 21), radius_x=3)
        self.add_line('e10-2', (42, 21), (44, 28))
        self.add_arc('e11-1', (44, 31), (44, 32), radius_x=34, sweep=False)
        self.add_arc('e11-2', (44, 32), (44, 33), radius_x=34, sweep=False)
        self.add_arc('e12-1', (39, 19), (32, 8), radius_x=12, sweep=False)
        self.add_line('e12-2', (32, 8), (30, 8))
        self.add_arc('e13', (23, 8), (14, 19), radius_x=12, sweep=False)
        self.add_line('e15', (30, 34), (31, 30))
        self.add_contour('c0', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e0', 'e1', 'e10-1', 'e10-2', 'e2', 'e11-1', 'e11-2', 'e3')
        self.add_contour('c1', 'e12-1', 'e12-2', 'e4', 'e13')
        self.add_contour('c3', 'e5', 'e15')
        self.add_contour('c4', 'e6')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'e7')
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'e7')
        self.relate('connect', 'c3', 'e8')
        self.relate('connect', 'c3', 'e8')
        self.relate('connect', 'c4', 'c1')
        self.relate('connect', 'c4', 'c0')
