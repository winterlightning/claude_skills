"""Sum symbol (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd04a175f-06bf-4489-ae4e-d1537b8f000b'
SOURCE_PATH = 'icons-json/symbol/sum symbol_d04a175f-06bf-4489-ae4e-d1537b8f000b.json'
AUTHOR = 'json_to_solo'

class SumSymbolD04a175f(Solo48):
    icon_id = 'sum-symbol-d04a175f'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('sum', 'symbol')

    def build(self):
        self.add_line('e0', (40, 4), (8, 4))
        self.add_line('e1', (8, 4), (25, 24))
        self.add_line('e2', (25, 24), (8, 44))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
