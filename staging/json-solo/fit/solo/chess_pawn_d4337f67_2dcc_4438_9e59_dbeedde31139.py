"""Chess pawn (hobbies), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4337f67-2dcc-4438-9e59-dbeedde31139'
SOURCE_PATH = 'icons-json/hobbies/chess pawn_d4337f67-2dcc-4438-9e59-dbeedde31139.json'
AUTHOR = 'json_to_solo'

class ChessPawnHobbies(Solo48):
    icon_id = 'chess-pawn-hobbies'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    aliases = ()
    keywords = ('chess', 'pawn', 'hobbies')

    def build(self):
        self.add_arc('sym-e0', (12, 13), (36, 13), radius_x=12, radius_y=9)
        self.add_arc('sym-e1', (36, 13), (31, 20), radius_x=12, radius_y=9)
        self.add_arc('sym-e2', (31, 20), (17, 20), radius_x=12, radius_y=9)
        self.add_arc('sym-e3', (17, 20), (12, 13), radius_x=12, radius_y=9)
        self.add_line('sym-e4', (34, 35), (14, 35))
        self.add_line('sym-e5', (14, 35), (17, 22))
        self.add_line('sym-e6', (17, 22), (17, 20))
        self.add_line('sym-e7', (24, 44), (8, 44))
        self.add_line('sym-e8', (8, 44), (8, 41))
        self.add_arc('sym-e9', (8, 41), (14, 35), radius_x=7)
        self.add_line('sym-e10', (31, 20), (31, 22))
        self.add_line('sym-e11', (31, 22), (34, 35))
        self.add_arc('sym-e12', (34, 35), (40, 41), radius_x=7)
        self.add_line('sym-e13', (40, 41), (40, 44))
        self.add_line('sym-e14', (40, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c3', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
