"""Car (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38792ded-1850-5f89-8b9a-dc4c3354c564'
SOURCE_PATH = 'icons-json/transportation/car_38792ded-1850-5f89-8b9a-dc4c3354c564.json'
AUTHOR = 'json_to_solo'

class Car38792ded(Solo48):
    icon_id = 'car-38792ded'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'transportation')

    def build(self):
        self.add_line('e0', (44, 30), (44, 26))
        self.add_line('e1', (43, 23), (36, 19))
        self.add_line('e2', (36, 19), (29, 10))
        self.add_line('e3', (24, 8), (16, 8))
        self.add_line('e4', (8, 12), (5, 15))
        self.add_line('e5', (4, 18), (4, 30))
        self.add_line('e6', (31, 34), (18, 34))
        self.add_line('e7', (19, 19), (23, 19))
        self.add_arc('e8-top', (31, 34), (41, 34), radius_x=5, radius_y=6)
        self.add_arc('e8-bottom', (41, 34), (31, 34), radius_x=5, radius_y=6)
        self.add_arc('e9-top', (8, 34), (18, 34), radius_x=5, radius_y=6)
        self.add_arc('e9-bottom', (18, 34), (8, 34), radius_x=5, radius_y=6)
        self.add_arc('e10-1', (40, 34), (44, 31), radius_x=4, sweep=False)
        self.add_arc('e10-2', (44, 31), (44, 30), radius_x=32)
        self.add_line('e11', (44, 26), (43, 23))
        self.add_line('e12-1', (29, 10), (25, 8))
        self.add_line('e12-2', (25, 8), (24, 8))
        self.add_line('e13-1', (16, 8), (10, 9))
        self.add_arc('e13-2', (10, 9), (8, 12), radius_x=13, sweep=False)
        self.add_arc('e14', (5, 15), (4, 18), radius_x=8, sweep=False)
        self.add_line('e15-1', (4, 30), (5, 33))
        self.add_line('e15-2', (5, 33), (9, 34))
        self.add_contour('c0', 'e10-1', 'e10-2', 'e0', 'e11', 'e1', 'e2', 'e12-1', 'e12-2', 'e3', 'e13-1', 'e13-2', 'e4', 'e14', 'e5', 'e15-1', 'e15-2')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c0', 'e9')
        self.relate('connect', 'c1', 'e8')
        self.relate('connect', 'c1', 'e9')
