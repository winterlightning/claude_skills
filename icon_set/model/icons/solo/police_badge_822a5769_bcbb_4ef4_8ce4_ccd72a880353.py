"""Police badge (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '822a5769-bcbb-4ef4-8ce4-ccd72a880353'
SOURCE_PATH = 'icons-json/symbol/police badge_822a5769-bcbb-4ef4-8ce4-ccd72a880353.json'
AUTHOR = 'json_to_solo'

class PoliceBadge(Solo48):
    icon_id = 'police-badge'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('police', 'badge', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 20), (24, 26))
        self.add_line('sym-e1', (37, 5), (40, 9))
        self.add_arc('sym-e2', (40, 9), (37, 19), radius_x=14, sweep=False)
        self.add_line('sym-e3', (37, 19), (39, 25))
        self.add_line('sym-e4', (39, 25), (40, 28))
        self.add_arc('sym-e5', (40, 28), (40, 29), radius_x=30, sweep=False)
        self.add_line('sym-e6', (40, 29), (39, 31))
        self.add_line('sym-e7', (39, 31), (38, 34))
        self.add_line('sym-e8', (38, 34), (32, 39))
        self.add_line('sym-e9', (32, 39), (26, 43))
        self.add_line('sym-e10', (26, 43), (24, 44))
        self.add_line('sym-e15', (24, 44), (22, 43))
        self.add_line('sym-e16', (22, 43), (16, 39))
        self.add_line('sym-e17', (16, 39), (10, 34))
        self.add_arc('sym-e18', (10, 34), (9, 31), radius_x=14, sweep=False)
        self.add_line('sym-e19', (9, 31), (8, 29))
        self.add_line('sym-e20', (8, 29), (8, 28))
        self.add_line('sym-e21', (8, 28), (9, 25))
        self.add_line('sym-e22', (9, 25), (11, 19))
        self.add_arc('sym-e23', (11, 19), (8, 9), radius_x=13, sweep=False)
        self.add_line('sym-e24', (8, 9), (11, 5))
        self.add_arc('sym-e25', (11, 5), (21, 6), radius_x=11, sweep=False)
        self.add_line('sym-e26', (21, 6), (23, 5))
        self.add_line('sym-e27', (23, 5), (24, 4))
        self.add_line('sym-e33', (24, 4), (25, 5))
        self.add_line('sym-e34', (25, 5), (27, 6))
        self.add_arc('sym-e35', (27, 6), (37, 5), radius_x=12, sweep=False)
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e33', 'sym-e34', 'sym-e35', closed=True)
