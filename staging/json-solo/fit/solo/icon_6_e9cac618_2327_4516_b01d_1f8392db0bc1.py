"""6 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e9cac618-2327-4516-b01d-1f8392db0bc1'
SOURCE_PATH = 'icons-json/symbol/6_e9cac618-2327-4516-b01d-1f8392db0bc1.json'
AUTHOR = 'json_to_solo'

class Icon6Symbol(Solo48):
    icon_id = 'icon-6-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('symbol',)

    def build(self):
        self.add_arc('e0-1', (39, 9), (32, 5), radius_x=19, sweep=False)
        self.add_line('e0-2', (32, 5), (26, 4))
        self.add_arc('e0-3', (26, 4), (12, 10), radius_x=20, sweep=False)
        self.add_arc('e0-4', (12, 10), (9, 15), radius_x=15, sweep=False)
        self.add_line('e0-5', (9, 15), (8, 25))
        self.add_line('e0-6', (8, 25), (8, 30))
        self.add_arc('e1-1', (8, 30), (13, 41), radius_x=15, sweep=False)
        self.add_arc('e1-2', (13, 41), (18, 43), radius_x=14, sweep=False)
        self.add_line('e1-3', (18, 43), (25, 44))
        self.add_line('e1-4', (25, 44), (31, 43))
        self.add_arc('e1-5', (31, 43), (35, 41), radius_x=13, sweep=False)
        self.add_arc('e1-6', (35, 41), (40, 32), radius_x=12, sweep=False)
        self.add_line('e1-7', (40, 32), (38, 25))
        self.add_arc('e1-8', (38, 25), (25, 19), radius_x=15, sweep=False)
        self.add_arc('e1-9', (25, 19), (8, 30), radius_x=16, sweep=False)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', closed=True)
        self.relate('connect', 'c0', 'c1')
