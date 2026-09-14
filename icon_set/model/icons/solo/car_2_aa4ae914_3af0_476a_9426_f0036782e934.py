"""Car 2 (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa4ae914-3af0-476a-9426-f0036782e934'
SOURCE_PATH = 'icons-json/transportation/car 2_aa4ae914-3af0-476a-9426-f0036782e934.json'
AUTHOR = 'json_to_solo'

class Car2(Solo48):
    icon_id = 'car-2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'transportation')

    def build(self):
        self.add_line('e0', (39, 34), (42, 34))
        self.add_line('e1', (9, 34), (6, 34))
        self.add_line('e2', (4, 31), (4, 23))
        self.add_line('e3', (6, 19), (20, 19))
        self.add_line('e4', (6, 19), (12, 9))
        self.add_line('e5', (30, 34), (18, 34))
        self.add_line('e6', (20, 19), (36, 19))
        self.add_line('e7', (36, 19), (29, 9))
        self.add_line('e8', (26, 8), (20, 8))
        self.add_line('e9', (20, 19), (20, 8))
        self.add_arc('e10-top', (30, 34), (40, 34), radius_x=5, radius_y=6)
        self.add_arc('e10-bottom', (40, 34), (30, 34), radius_x=5, radius_y=6)
        self.add_arc('e11-top', (8, 34), (18, 34), radius_x=5, radius_y=6)
        self.add_arc('e11-bottom', (18, 34), (8, 34), radius_x=5, radius_y=6)
        self.add_arc('e12-1', (42, 34), (44, 31), radius_x=4, sweep=False)
        self.add_line('e12-2', (44, 31), (44, 27))
        self.add_line('e12-3', (44, 27), (42, 21))
        self.add_arc('e12-4', (42, 21), (36, 19), radius_x=8, sweep=False)
        self.add_line('e13', (6, 34), (4, 31))
        self.add_arc('e14', (4, 23), (6, 19), radius_x=5)
        self.add_line('e15', (12, 9), (20, 8))
        self.add_line('e16', (29, 9), (26, 8))
        self.add_contour('c0', 'e0', 'e12-1', 'e12-2', 'e12-3', 'e12-4')
        self.add_contour('c1', 'e1', 'e13', 'e2', 'e14')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e15')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6', 'e7', 'e16', 'e8')
        self.add_contour('c6', 'e9')
        self.add_contour('e10', 'e10-top', 'e10-bottom', closed=True)
        self.add_contour('e11', 'e11-top', 'e11-bottom', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c0', 'e10')
        self.relate('connect', 'c1', 'e11')
        self.relate('connect', 'c4', 'e10')
        self.relate('connect', 'c4', 'e11')
