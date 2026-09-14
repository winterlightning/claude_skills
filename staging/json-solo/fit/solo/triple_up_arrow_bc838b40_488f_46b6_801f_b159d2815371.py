"""Triple up arrow (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc838b40-488f-46b6-801f-b159d2815371'
SOURCE_PATH = 'icons-json/symbol/triple up arrow_bc838b40-488f-46b6-801f-b159d2815371.json'
AUTHOR = 'json_to_solo'

class TripleUpArrowSymbol(Solo48):
    icon_id = 'triple-up-arrow-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('triple', 'up', 'arrow', 'symbol')

    def build(self):
        self.add_line('e0', (24, 26), (24, 8))
        self.add_line('e1', (24, 8), (29, 13))
        self.add_line('e2', (24, 8), (19, 13))
        self.add_line('e3', (4, 31), (9, 26))
        self.add_line('e4', (9, 26), (9, 40))
        self.add_line('e5', (9, 26), (14, 31))
        self.add_line('e6', (39, 25), (34, 30))
        self.add_line('e7', (39, 40), (39, 25))
        self.add_line('e8', (39, 25), (44, 30))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7', 'e8')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
