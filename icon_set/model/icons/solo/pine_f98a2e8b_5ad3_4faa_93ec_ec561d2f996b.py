"""Pine (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f98a2e8b-5ad3-4faa-93ec-ec561d2f996b'
SOURCE_PATH = 'icons-json/symbol/pine_f98a2e8b-5ad3-4faa-93ec-ec561d2f996b.json'
AUTHOR = 'json_to_solo'

class PineF98a2e8b(Solo48):
    icon_id = 'pine-f98a2e8b'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pine', 'symbol')

    def build(self):
        self.add_line('e0', (24, 44), (24, 39))
        self.add_line('e1', (13, 16), (19, 16))
        self.add_line('e2', (19, 16), (8, 29))
        self.add_line('e3', (8, 29), (17, 29))
        self.add_line('e4', (17, 29), (8, 39))
        self.add_line('e5', (8, 39), (40, 39))
        self.add_line('e6', (40, 39), (30, 29))
        self.add_line('e7', (30, 29), (40, 29))
        self.add_line('e8', (40, 29), (29, 16))
        self.add_line('e9', (29, 16), (34, 16))
        self.add_line('e10', (34, 16), (24, 4))
        self.add_line('e11', (24, 4), (13, 16))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', closed=True)
        self.relate('connect', 'c0', 'c1')
