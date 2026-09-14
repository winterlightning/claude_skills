"""Lv (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39ccb5c4-ba10-4742-8cf1-04e617232ae7'
SOURCE_PATH = 'icons-json/symbol/lv (text u)_39ccb5c4-ba10-4742-8cf1-04e617232ae7.json'
AUTHOR = 'json_to_solo'

class LvTextUSymbol(Solo48):
    icon_id = 'lv-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('lv', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (8, 27))
        self.add_line('e1', (8, 27), (20, 27))
        self.add_line('e2', (28, 12), (34, 27))
        self.add_line('e3', (34, 27), (40, 12))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
