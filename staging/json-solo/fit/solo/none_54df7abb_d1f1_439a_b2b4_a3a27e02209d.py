"""None (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '54df7abb-d1f1-439a-b2b4-a3a27e02209d'
SOURCE_PATH = 'icons-json/symbol/none_54df7abb-d1f1-439a-b2b4-a3a27e02209d.json'
AUTHOR = 'json_to_solo'

class NoneSymbol(Solo48):
    icon_id = 'none-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('none', 'symbol')

    def build(self):
        self.add_line('e0', (8, 44), (8, 4))
        self.add_line('e1', (40, 4), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
