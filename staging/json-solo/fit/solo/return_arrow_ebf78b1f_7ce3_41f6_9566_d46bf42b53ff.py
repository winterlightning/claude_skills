"""Return arrow (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ebf78b1f-7ce3-41f6-9566-d46bf42b53ff'
SOURCE_PATH = 'icons-json/symbol/return arrow_ebf78b1f-7ce3-41f6-9566-d46bf42b53ff.json'
AUTHOR = 'json_to_solo'

class ReturnArrowSymbol(Solo48):
    icon_id = 'return-arrow-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('return', 'arrow', 'symbol')

    def build(self):
        self.add_line('e0', (18, 8), (4, 24))
        self.add_line('e1', (18, 40), (4, 24))
        self.add_line('e2', (4, 24), (40, 24))
        self.add_line('e3', (44, 19), (44, 11))
        self.add_line('e4-1', (40, 24), (43, 23))
        self.add_line('e4-2', (43, 23), (44, 19))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e4-1', 'e4-2', 'e3')
