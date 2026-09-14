"""Plus (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0d26164b-e2b7-4c96-bb61-775619425cd0'
SOURCE_PATH = 'icons-json/symbol/PLUS_0d26164b-e2b7-4c96-bb61-775619425cd0.json'
AUTHOR = 'json_to_solo'

class Plus(Solo48):
    icon_id = 'plus'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('plus', 'symbol')

    def build(self):
        self.add_line('e0', (37, 14), (44, 8))
        self.add_line('e1', (44, 8), (44, 40))
        self.add_line('e2', (13, 15), (13, 36))
        self.add_line('e3', (4, 26), (22, 26))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
