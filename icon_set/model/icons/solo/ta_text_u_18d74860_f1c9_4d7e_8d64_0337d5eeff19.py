"""Ta (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18d74860-f1c9-4d7e-8d64-0337d5eeff19'
SOURCE_PATH = 'icons-json/symbol/ta (text u)_18d74860-f1c9-4d7e-8d64-0337d5eeff19.json'
AUTHOR = 'json_to_solo'

class TaTextU(Solo48):
    icon_id = 'ta-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ta', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (21, 4))
        self.add_line('e1', (15, 27), (15, 4))
        self.add_line('e2', (40, 27), (40, 23))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_arc('e4-1', (40, 23), (33, 26), radius_x=5)
        self.add_arc('e4-2', (33, 26), (30, 23), radius_x=5)
        self.add_arc('e4-3', (30, 23), (35, 12), radius_x=8)
        self.add_arc('e4-4', (35, 12), (40, 17), radius_x=5)
        self.add_line('e4-5', (40, 17), (40, 23))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', closed=True)
        self.relate('connect', 'c1', 'c0')
