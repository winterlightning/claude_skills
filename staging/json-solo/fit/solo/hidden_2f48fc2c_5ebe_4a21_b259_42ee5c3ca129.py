"""Hidden (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f48fc2c-5ebe-4a21-b259-42ee5c3ca129'
SOURCE_PATH = 'icons-json/symbol/hidden_2f48fc2c-5ebe-4a21-b259-42ee5c3ca129.json'
AUTHOR = 'json_to_solo'

class HiddenSymbol(Solo48):
    icon_id = 'hidden-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('hidden', 'symbol')

    def build(self):
        self.add_line('e0', (13, 12), (33, 38))
        self.add_arc('e1-1', (13, 12), (4, 24), radius_x=29, sweep=False)
        self.add_arc('e1-2', (4, 24), (24, 40), radius_x=23, sweep=False)
        self.add_line('e1-3', (24, 40), (33, 38))
        self.add_arc('e2-1', (13, 12), (24, 8), radius_x=18)
        self.add_arc('e2-2', (24, 8), (44, 24), radius_x=23)
        self.add_arc('e2-3', (44, 24), (33, 38), radius_x=29)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3')
        self.add_contour('c2', 'e2-1', 'e2-2', 'e2-3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
