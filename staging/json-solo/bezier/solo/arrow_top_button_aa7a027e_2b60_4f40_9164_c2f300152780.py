"""Arrow top button (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa7a027e-2b60-4f40-9164-c2f300152780'
SOURCE_PATH = 'icons-json/symbol/arrow top button_aa7a027e-2b60-4f40-9164-c2f300152780.json'
AUTHOR = 'json_to_solo'

class ArrowTopButtonSymbol(Solo48):
    icon_id = 'arrow-top-button-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'top', 'button', 'symbol')

    def build(self):
        self.add_line('e0', (8, 44), (25, 27))
        self.add_line('e1', (25, 27), (40, 43))
        self.add_line('e2', (40, 43), (40, 21))
        self.add_line('e3', (40, 21), (24, 4))
        self.add_line('e4', (24, 4), (8, 21))
        self.add_line('e5', (8, 21), (8, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', closed=True)
