"""Car (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ecb7b0f-c4d1-5669-81fe-5c2d48418656'
SOURCE_PATH = 'icons-json/transportation/car_4ecb7b0f-c4d1-5669-81fe-5c2d48418656.json'
AUTHOR = 'json_to_solo'

class Car4ecb7b0f(Solo48):
    icon_id = 'car-4ecb7b0f'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'transportation')

    def build(self):
        self.add_line('e0', (30, 34), (18, 34))
        self.add_line('e1', (20, 8), (20, 19))
        self.add_line('e2', (36, 19), (6, 19))
        self.add_line('e3', (6, 19), (11, 10))
        self.add_line('e4', (16, 8), (24, 8))
        self.add_line('e5', (29, 10), (36, 19))
        self.add_arc('e6-top', (30, 34), (40, 34), radius_x=5, radius_y=6)
        self.add_arc('e6-bottom', (40, 34), (30, 34), radius_x=5, radius_y=6)
        self.add_arc('e7-top', (8, 34), (18, 34), radius_x=5, radius_y=6)
        self.add_arc('e7-bottom', (18, 34), (8, 34), radius_x=5, radius_y=6)
        self.add_line('e8-1', (39, 34), (43, 33))
        self.add_line('e8-2', (43, 33), (44, 29))
        self.add_arc('e8-3', (44, 29), (44, 26), radius_x=58)
        self.add_arc('e8-4', (44, 26), (42, 21), radius_x=9, sweep=False)
        self.add_arc('e8-5', (42, 21), (36, 19), radius_x=8, sweep=False)
        self.add_line('e9-1', (9, 34), (5, 33))
        self.add_line('e9-2', (5, 33), (4, 26))
        self.add_line('e9-3', (4, 26), (5, 19))
        self.add_line('e10', (11, 10), (16, 8))
        self.add_line('e11', (24, 8), (29, 10))
        self.add_contour('c0', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e9-1', 'e9-2', 'e9-3')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e2', 'e3', 'e10', 'e4', 'e11', 'e5', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c1', 'e7')
        self.relate('connect', 'c2', 'e7')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c4')
