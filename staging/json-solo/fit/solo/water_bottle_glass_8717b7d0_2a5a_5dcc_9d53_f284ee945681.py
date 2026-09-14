"""Water bottle glass (drinks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8717b7d0-2a5a-5dcc-9d53-f284ee945681'
SOURCE_PATH = 'icons-json/drinks/water bottle glass_8717b7d0-2a5a-5dcc-9d53-f284ee945681.json'
AUTHOR = 'json_to_solo'

class WaterBottleGlassDrinks(Solo48):
    icon_id = 'water-bottle-glass-drinks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('water', 'bottle', 'glass', 'drinks')

    def build(self):
        self.add_line('e0', (40, 19), (40, 24))
        self.add_line('e1', (8, 18), (8, 22))
        self.add_line('e2', (38, 24), (40, 24))
        self.add_line('e3', (8, 22), (8, 39))
        self.add_line('e4', (15, 44), (33, 44))
        self.add_line('e5', (40, 39), (40, 24))
        self.add_line('e6', (18, 4), (15, 4))
        self.add_line('e7-1', (33, 4), (31, 4))
        self.add_arc('e7-2', (31, 4), (31, 8), radius_x=3, sweep=False)
        self.add_line('e7-3', (31, 8), (38, 12))
        self.add_line('e7-4', (38, 12), (40, 18))
        self.add_arc('e7-5', (40, 18), (40, 19), radius_x=24, sweep=False)
        self.add_arc('e8-1', (18, 4), (17, 8), radius_x=5)
        self.add_arc('e8-2', (17, 8), (8, 17), radius_x=10, sweep=False)
        self.add_line('e8-3', (8, 17), (8, 18))
        self.add_line('e9-1', (8, 22), (17, 21))
        self.add_arc('e9-2', (17, 21), (27, 24), radius_x=29)
        self.add_arc('e9-3', (27, 24), (38, 24), radius_x=20, sweep=False)
        self.add_line('e10-1', (8, 39), (9, 42))
        self.add_line('e10-2', (9, 42), (15, 44))
        self.add_line('e11-1', (33, 44), (39, 42))
        self.add_line('e11-2', (39, 42), (40, 39))
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e0')
        self.add_contour('c2', 'e8-1', 'e8-2', 'e8-3', 'e1')
        self.add_contour('c3', 'e9-1', 'e9-2', 'e9-3', 'e2')
        self.add_contour('c4', 'e3', 'e10-1', 'e10-2', 'e4', 'e11-1', 'e11-2', 'e5')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
