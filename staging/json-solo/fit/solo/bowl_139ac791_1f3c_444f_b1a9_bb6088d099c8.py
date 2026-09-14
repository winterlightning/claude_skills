"""Bowl (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '139ac791-1f3c-444f-b1a9-bb6088d099c8'
SOURCE_PATH = 'icons-json/symbol/bowl_139ac791-1f3c-444f-b1a9-bb6088d099c8.json'
AUTHOR = 'json_to_solo'

class BowlSymbol(Solo48):
    icon_id = 'bowl-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bowl', 'symbol')

    def build(self):
        self.add_arc('sym-e0', (33, 33), (44, 10), radius_x=30, sweep=False)
        self.add_line('sym-e1', (44, 10), (44, 9))
        self.add_arc('sym-e2', (44, 9), (44, 8), radius_x=23)
        self.add_line('sym-e3', (44, 8), (24, 8))
        self.add_line('sym-e4', (24, 8), (4, 8))
        self.add_line('sym-e5', (4, 8), (4, 9))
        self.add_line('sym-e6', (4, 9), (4, 10))
        self.add_arc('sym-e7', (4, 10), (15, 33), radius_x=31, sweep=False)
        self.add_line('sym-e8', (15, 33), (15, 39))
        self.add_arc('sym-e9', (15, 39), (15, 40), radius_x=3)
        self.add_arc('sym-e10', (15, 40), (16, 40), radius_x=1)
        self.add_line('sym-e12', (16, 40), (24, 40))
        self.add_line('sym-e13', (24, 40), (32, 40))
        self.add_line('sym-e15', (32, 40), (33, 40))
        self.add_arc('sym-e16', (33, 40), (33, 39), radius_x=3)
        self.add_line('sym-e17', (33, 39), (33, 33))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
