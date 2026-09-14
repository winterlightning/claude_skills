"""Cup (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db8ea339-df43-4389-a7c4-43da211daa67'
SOURCE_PATH = 'icons-json/symbol/cup_db8ea339-df43-4389-a7c4-43da211daa67.json'
AUTHOR = 'json_to_solo'

class CupSymbol(Solo48):
    icon_id = 'cup-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cup', 'symbol')

    def build(self):
        self.add_line('e0', (4, 28), (4, 8))
        self.add_line('e1', (4, 8), (33, 8))
        self.add_line('e2', (33, 8), (33, 27))
        self.add_arc('e3-1', (33, 12), (44, 19), radius_x=8)
        self.add_arc('e3-2', (44, 19), (33, 27), radius_x=9)
        self.add_arc('e3-3', (33, 27), (27, 38), radius_x=15)
        self.add_line('e3-4', (27, 38), (18, 40))
        self.add_line('e3-5', (18, 40), (12, 39))
        self.add_arc('e3-6', (12, 39), (9, 37), radius_x=14)
        self.add_arc('e3-7', (9, 37), (4, 28), radius_x=14)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e0', 'e1', 'e2')
