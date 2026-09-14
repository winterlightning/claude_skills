"""C5 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '259c0878-528e-42fb-8d9f-56fe04a84b03'
SOURCE_PATH = 'icons-json/symbol/c5_259c0878-528e-42fb-8d9f-56fe04a84b03.json'
AUTHOR = 'json_to_solo'

class C5Symbol(Solo48):
    icon_id = 'c5-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('c5', 'symbol')

    def build(self):
        self.add_line('e0', (42, 8), (31, 8))
        self.add_line('e1', (31, 8), (29, 24))
        self.add_line('e2', (29, 24), (32, 22))
        self.add_arc('e3-1', (21, 14), (14, 8), radius_x=8, sweep=False)
        self.add_line('e3-2', (14, 8), (10, 9))
        self.add_arc('e3-3', (10, 9), (5, 16), radius_x=12, sweep=False)
        self.add_line('e3-4', (5, 16), (4, 24))
        self.add_line('e3-5', (4, 24), (6, 35))
        self.add_arc('e3-6', (6, 35), (13, 40), radius_x=8, sweep=False)
        self.add_line('e3-7', (13, 40), (19, 38))
        self.add_arc('e3-8', (19, 38), (21, 34), radius_x=11, sweep=False)
        self.add_arc('e4-1', (32, 22), (40, 21), radius_x=7)
        self.add_arc('e4-2', (40, 21), (43, 25), radius_x=7)
        self.add_line('e4-3', (43, 25), (44, 30))
        self.add_line('e4-4', (44, 30), (43, 35))
        self.add_line('e4-5', (43, 35), (41, 38))
        self.add_line('e4-6', (41, 38), (36, 40))
        self.add_line('e4-7', (36, 40), (32, 39))
        self.add_arc('e4-8', (32, 39), (29, 36), radius_x=11)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8')
        self.add_contour('c1', 'e0', 'e1', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8')
