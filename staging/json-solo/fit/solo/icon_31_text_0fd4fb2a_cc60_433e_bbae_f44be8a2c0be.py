"""31 (text) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fd4fb2a-cc60-433e-bbae-f44be8a2c0be'
SOURCE_PATH = 'icons-json/symbol/31 (text)_0fd4fb2a-cc60-433e-bbae-f44be8a2c0be.json'
AUTHOR = 'json_to_solo'

class Icon31TextSymbol(Solo48):
    icon_id = 'icon-31-text-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('text', 'symbol')

    def build(self):
        self.add_line('e0', (44, 8), (44, 40))
        self.add_arc('e1-1', (5, 13), (13, 8), radius_x=9)
        self.add_line('e1-2', (13, 8), (19, 10))
        self.add_arc('e1-3', (19, 10), (21, 19), radius_x=8)
        self.add_arc('e1-4', (21, 19), (17, 23), radius_x=8)
        self.add_line('e1-5', (17, 23), (12, 24))
        self.add_line('e1-6', (12, 24), (13, 24))
        self.add_line('e1-7', (13, 24), (14, 24))
        self.add_arc('e1-8', (14, 24), (22, 30), radius_x=9)
        self.add_arc('e1-9', (22, 30), (20, 37), radius_x=7)
        self.add_arc('e1-10', (20, 37), (13, 40), radius_x=10)
        self.add_arc('e1-11', (13, 40), (4, 34), radius_x=10)
        self.add_arc('e2', (36, 14), (44, 8), radius_x=19, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11')
        self.add_contour('c1', 'e2', 'e0')
