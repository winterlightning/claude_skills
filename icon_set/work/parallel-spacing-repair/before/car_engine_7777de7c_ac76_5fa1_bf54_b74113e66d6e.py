"""Car engine (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7777de7c-ac76-5fa1-bf54-b74113e66d6e'
SOURCE_PATH = 'icons-json/transportation/car engine_7777de7c-ac76-5fa1-bf54-b74113e66d6e.json'
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
        self.add_line('e0', (4, 18), (4, 35))
        self.add_line('e1', (4, 24), (12, 24))
        self.add_line('e2', (12, 24), (12, 17))
        self.add_line('e3', (15, 14), (29, 14))
        self.add_line('e4', (33, 16), (36, 19))
        self.add_line('e5', (37, 20), (42, 20))
        self.add_line('e6', (44, 22), (44, 35))
        self.add_line('e7', (39, 40), (22, 40))
        self.add_line('e8', (19, 39), (14, 34))
        self.add_line('e9', (10, 31), (4, 31))
        self.add_line('e10', (16, 8), (29, 8))
        self.add_line('e11', (22, 14), (22, 8))
        self.add_arc('e12', (12, 17), (15, 14), radius_x=3)
        self.add_arc('e13', (29, 14), (33, 16), radius_x=8)
        self.add_arc('e14', (36, 19), (37, 20), radius_x=33, sweep=False)
        self.add_arc('e15', (42, 20), (44, 22), radius_x=2)
        self.add_arc('e16', (44, 35), (39, 40), radius_x=5)
        self.add_arc('e17', (22, 40), (19, 39), radius_x=5)
        self.add_arc('e18', (14, 34), (10, 31), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e12', 'e3', 'e13', 'e4', 'e14', 'e5', 'e15', 'e6', 'e16', 'e7', 'e17', 'e8', 'e18', 'e9')
        self.add_contour('c2', 'e10')
        self.add_contour('c3', 'e11')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c1')
        self.relate('connect', 'c3', 'c2')
