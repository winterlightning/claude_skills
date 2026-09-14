"""Ghost (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a257f108-5e8d-40d4-97ad-643846319b7b'
SOURCE_PATH = 'icons-json/symbol/ghost_a257f108-5e8d-40d4-97ad-643846319b7b.json'
AUTHOR = 'json_to_solo'

class GhostSymbol(Solo48):
    icon_id = 'ghost-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ghost', 'symbol')

    def build(self):
        self.add_line('e0', (10, 36), (8, 40))
        self.add_line('e1', (8, 42), (10, 44))
        self.add_line('e2', (20, 44), (22, 42))
        self.add_line('e3', (35, 41), (37, 43))
        self.add_line('e4', (8, 40), (8, 42))
        self.add_arc('e5-1', (10, 44), (17, 44), radius_x=4)
        self.add_arc('e5-2', (17, 44), (20, 44), radius_x=25)
        self.add_line('e6-1', (22, 42), (25, 42))
        self.add_arc('e6-2', (25, 42), (29, 44), radius_x=6, sweep=False)
        self.add_line('e6-3', (29, 44), (35, 41))
        self.add_arc('e7-1', (37, 43), (39, 43), radius_x=2, sweep=False)
        self.add_line('e7-2', (39, 43), (40, 41))
        self.add_line('e7-3', (40, 41), (38, 31))
        self.add_line('e7-4', (38, 31), (38, 16))
        self.add_arc('e7-5', (38, 16), (25, 4), radius_x=14, sweep=False)
        self.add_line('e7-6', (25, 4), (17, 6))
        self.add_arc('e7-7', (17, 6), (12, 11), radius_x=16, sweep=False)
        self.add_arc('e7-8', (12, 11), (10, 16), radius_x=18, sweep=False)
        self.add_line('e7-9', (10, 16), (10, 36))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5-1', 'e5-2', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e3', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e7-6', 'e7-7', 'e7-8', 'e7-9', closed=True)
