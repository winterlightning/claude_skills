"""Car engine (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3a63ee0-3071-45c6-999f-7f964c495da1'
SOURCE_PATH = 'icons-json/transportation/car engine_e3a63ee0-3071-45c6-999f-7f964c495da1.json'
AUTHOR = 'json_to_solo'

class CarEngine(Solo48):
    icon_id = 'car-engine'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'engine', 'transportation')

    def build(self):
        self.add_line('e0', (16, 8), (22, 8))
        self.add_line('e1', (4, 18), (4, 24))
        self.add_line('e2', (4, 35), (4, 31))
        self.add_line('e3', (29, 8), (22, 8))
        self.add_line('e4', (4, 31), (10, 31))
        self.add_line('e5', (11, 32), (19, 39))
        self.add_line('e6', (21, 40), (40, 40))
        self.add_line('e7', (44, 36), (44, 21))
        self.add_line('e8', (42, 20), (37, 20))
        self.add_line('e9', (36, 19), (31, 15))
        self.add_line('e10', (30, 14), (22, 14))
        self.add_line('e11', (4, 31), (4, 24))
        self.add_line('e12', (22, 14), (14, 14))
        self.add_line('e13', (12, 16), (12, 24))
        self.add_line('e14', (12, 24), (4, 24))
        self.add_line('e15', (22, 14), (22, 8))
        self.add_arc('e16', (10, 31), (11, 32), radius_x=16)
        self.add_line('e17', (19, 39), (21, 40))
        self.add_arc('e18', (40, 40), (44, 36), radius_x=4, sweep=False)
        self.add_line('e19', (44, 21), (42, 20))
        self.add_line('e20', (37, 20), (36, 19))
        self.add_arc('e21', (31, 15), (30, 14), radius_x=21, sweep=False)
        self.add_line('e22', (14, 14), (12, 16))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e16', 'e5', 'e17', 'e6', 'e18', 'e7', 'e19', 'e8', 'e20', 'e9', 'e21', 'e10')
        self.add_contour('c5', 'e11')
        self.add_contour('c6', 'e12', 'e22', 'e13', 'e14')
        self.add_contour('c7', 'e15')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c6', 'c7')
