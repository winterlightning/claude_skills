"""Moon and cancel (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '487fd90e-ac2a-4467-9057-edc666b22495'
SOURCE_PATH = 'icons-json/symbol/moon and cancel_487fd90e-ac2a-4467-9057-edc666b22495.json'
AUTHOR = 'json_to_solo'

class MoonAndCancelSymbol(Solo48):
    icon_id = 'moon-and-cancel-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('moon', 'and', 'cancel', 'symbol')

    def build(self):
        self.add_line('e0', (42, 18), (35, 26))
        self.add_line('e1', (35, 18), (42, 26))
        self.add_line('e2', (32, 40), (26, 37))
        self.add_arc('e3-1', (26, 37), (31, 8), radius_x=17)
        self.add_arc('e3-2', (31, 8), (23, 6), radius_x=20, sweep=False)
        self.add_line('e3-3', (23, 6), (15, 8))
        self.add_arc('e3-4', (15, 8), (6, 24), radius_x=19, sweep=False)
        self.add_line('e3-5', (6, 24), (7, 30))
        self.add_arc('e3-6', (7, 30), (23, 42), radius_x=17, sweep=False)
        self.add_line('e3-7', (23, 42), (32, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', closed=True)
