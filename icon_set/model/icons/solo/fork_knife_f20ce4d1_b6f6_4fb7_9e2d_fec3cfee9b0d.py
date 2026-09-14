"""Fork knife (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f20ce4d1-b6f6-4fb7-9e2d-fec3cfee9b0d'
SOURCE_PATH = 'icons-json/symbol/fork knife_f20ce4d1-b6f6-4fb7-9e2d-fec3cfee9b0d.json'
AUTHOR = 'json_to_solo'

class ForkKnife(Solo48):
    icon_id = 'fork-knife'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('fork', 'knife', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (8, 15))
        self.add_line('e1', (17, 22), (17, 4))
        self.add_line('e2', (17, 44), (17, 22))
        self.add_line('e3', (24, 15), (24, 4))
        self.add_line('e4', (33, 44), (33, 4))
        self.add_line('e5', (33, 4), (40, 24))
        self.add_line('e6', (37, 28), (33, 28))
        self.add_arc('e7', (8, 15), (17, 22), radius_x=8, sweep=False)
        self.add_arc('e8', (17, 22), (24, 15), radius_x=8, sweep=False)
        self.add_line('e9-1', (40, 24), (40, 25))
        self.add_arc('e9-2', (40, 25), (37, 28), radius_x=3)
        self.add_contour('c0', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e2', 'e8', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5', 'e9-1', 'e9-2', 'e6')
        self.relate('connect', 'c3', 'c2')
