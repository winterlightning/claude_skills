"""Thumbs up (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '159051f0-87aa-4c05-9b9f-53abd2ca05ef'
SOURCE_PATH = 'icons-json/symbol/thumbs up_159051f0-87aa-4c05-9b9f-53abd2ca05ef.json'
AUTHOR = 'json_to_solo'

class ThumbsUpSymbol(Solo48):
    icon_id = 'thumbs-up-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('thumbs', 'up', 'symbol')

    def build(self):
        self.add_line('e0', (31, 13), (29, 19))
        self.add_line('e1', (29, 19), (39, 19))
        self.add_line('e2', (33, 42), (20, 42))
        self.add_line('e3', (13, 24), (6, 24))
        self.add_line('e4', (13, 40), (13, 25))
        self.add_line('e5', (13, 40), (6, 40))
        self.add_line('e6', (6, 40), (6, 24))
        self.add_arc('e7-1', (13, 24), (22, 16), radius_x=31, sweep=False)
        self.add_arc('e7-2', (22, 16), (25, 7), radius_x=18, sweep=False)
        self.add_line('e7-3', (25, 7), (27, 6))
        self.add_arc('e7-4', (27, 6), (31, 13), radius_x=5)
        self.add_arc('e8-1', (39, 19), (42, 22), radius_x=4)
        self.add_arc('e8-2', (42, 22), (40, 26), radius_x=5)
        self.add_arc('e8-3', (40, 26), (40, 32), radius_x=4)
        self.add_line('e8-4', (40, 32), (40, 36))
        self.add_arc('e8-5', (40, 36), (33, 42), radius_x=8)
        self.add_arc('e9', (20, 42), (13, 40), radius_x=15)
        self.add_contour('c0', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e0', 'e1', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5', 'e2', 'e9')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5', 'e6')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
