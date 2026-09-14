"""Head (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97903c22-da46-4913-b7f3-4e20608ab202'
SOURCE_PATH = 'icons-json/symbol/head_97903c22-da46-4913-b7f3-4e20608ab202.json'
AUTHOR = 'json_to_solo'

class HeadSymbol(Solo48):
    icon_id = 'head-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('head', 'symbol')

    def build(self):
        self.add_line('e0', (12, 44), (12, 32))
        self.add_line('e1', (36, 14), (40, 27))
        self.add_line('e2', (37, 28), (37, 33))
        self.add_line('e3', (32, 38), (29, 38))
        self.add_line('e4', (29, 38), (29, 44))
        self.add_line('e5-1', (12, 32), (9, 26))
        self.add_arc('e5-2', (9, 26), (8, 20), radius_x=19)
        self.add_line('e5-3', (8, 20), (9, 14))
        self.add_arc('e5-4', (9, 14), (14, 7), radius_x=15)
        self.add_arc('e5-5', (14, 7), (21, 4), radius_x=14)
        self.add_line('e5-6', (21, 4), (23, 4))
        self.add_arc('e5-7', (23, 4), (36, 14), radius_x=14)
        self.add_line('e6', (40, 27), (37, 28))
        self.add_arc('e7', (37, 33), (32, 38), radius_x=5)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e1', 'e6', 'e2', 'e7', 'e3', 'e4')
