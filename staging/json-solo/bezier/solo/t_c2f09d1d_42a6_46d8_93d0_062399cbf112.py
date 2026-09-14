"""T (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2f09d1d-42a6-46d8-93d0-062399cbf112'
SOURCE_PATH = 'icons-json/symbol/T_c2f09d1d-42a6-46d8-93d0-062399cbf112.json'
AUTHOR = 'json_to_solo'

class TSymbol(Solo48):
    icon_id = 't-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('t', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (40, 4))
        self.add_line('e1', (25, 44), (25, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.relate('connect', 'c1', 'c0')
