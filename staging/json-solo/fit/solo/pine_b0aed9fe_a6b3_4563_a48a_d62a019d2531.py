"""Pine (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0aed9fe-a6b3-4563-a48a-d62a019d2531'
SOURCE_PATH = 'icons-json/symbol/pine_b0aed9fe-a6b3-4563-a48a-d62a019d2531.json'
AUTHOR = 'json_to_solo'

class PineB0aed9fe(Solo48):
    icon_id = 'pine-b0aed9fe'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pine', 'symbol')

    def build(self):
        self.add_line('e0', (24, 37), (24, 44))
        self.add_line('e1', (35, 20), (24, 4))
        self.add_line('e2', (24, 4), (12, 20))
        self.add_line('e3', (12, 20), (18, 20))
        self.add_line('e4', (18, 20), (8, 37))
        self.add_line('e5', (8, 37), (40, 37))
        self.add_line('e6', (40, 37), (30, 20))
        self.add_line('e7', (30, 20), (35, 20))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', closed=True)
        self.relate('connect', 'c0', 'c1')
