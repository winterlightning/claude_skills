"""Arrows move (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ebb706f-5a30-4d8c-b8f1-4519aeaf46ea'
SOURCE_PATH = 'icons-json/symbol/arrows move_5ebb706f-5a30-4d8c-b8f1-4519aeaf46ea.json'
AUTHOR = 'json_to_solo'

class ArrowsMoveSymbol(Solo48):
    icon_id = 'arrows-move-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrows', 'move', 'symbol')

    def build(self):
        self.add_line('sym-e0', (42, 24), (31, 24))
        self.add_line('sym-e1', (6, 24), (17, 24))
        self.add_line('sym-e2', (11, 29), (6, 24))
        self.add_line('sym-e3', (6, 24), (11, 19))
        self.add_line('sym-e4', (42, 24), (37, 29))
        self.add_line('sym-e5', (24, 30), (24, 42))
        self.add_line('sym-e6', (24, 42), (19, 37))
        self.add_line('sym-e7', (29, 37), (24, 42))
        self.add_line('sym-e8', (42, 24), (37, 19))
        self.add_line('sym-e9', (24, 18), (24, 6))
        self.add_line('sym-e10', (24, 6), (19, 11))
        self.add_line('sym-e11', (29, 11), (24, 6))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c3', 'sym-e4')
        self.add_contour('sym-c4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c5', 'sym-e7')
        self.add_contour('sym-c6', 'sym-e8')
        self.add_contour('sym-c7', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c8', 'sym-e11')
        self.relate('connect', 'sym-c0', 'sym-c3', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c7', 'sym-c8')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c7', 'sym-c8')
        self.relate('connect', 'sym-c4', 'sym-c5')
