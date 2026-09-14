"""Batch-02/necklace stand (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81b7ac5c-a567-5591-8a55-414eb7643373'
SOURCE_PATH = 'icons-json/accessories/batch-02/necklace stand_81b7ac5c-a567-5591-8a55-414eb7643373.json'
AUTHOR = 'json_to_solo'

class Batch02NecklaceStand(Solo48):
    icon_id = 'batch-02-necklace-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'necklace', 'stand', 'accessories')

    def build(self):
        self.add_line('e0', (35, 35), (40, 28))
        self.add_line('e1', (42, 26), (42, 17))
        self.add_line('e2', (30, 6), (18, 6))
        self.add_line('e3', (6, 17), (6, 24))
        self.add_line('e4', (8, 29), (15, 35))
        self.add_line('e5', (38, 42), (10, 42))
        self.add_arc('e6', (30, 42), (35, 35), radius_x=10)
        self.add_line('e7', (40, 28), (42, 26))
        self.add_arc('e8-1', (42, 17), (39, 15), radius_x=3, sweep=False)
        self.add_arc('e8-2', (39, 15), (34, 13), radius_x=7)
        self.add_arc('e8-3', (34, 13), (32, 8), radius_x=9)
        self.add_arc('e8-4', (32, 8), (30, 6), radius_x=2, sweep=False)
        self.add_arc('e9-1', (18, 6), (16, 8), radius_x=2, sweep=False)
        self.add_arc('e9-2', (16, 8), (14, 13), radius_x=9)
        self.add_line('e9-3', (14, 13), (6, 17))
        self.add_arc('e10-1', (6, 24), (6, 26), radius_x=15)
        self.add_arc('e10-2', (6, 26), (8, 29), radius_x=5, sweep=False)
        self.add_arc('e11', (15, 35), (18, 42), radius_x=11)
        self.add_contour('c0', 'e6', 'e0', 'e7', 'e1', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e2', 'e9-1', 'e9-2', 'e9-3', 'e3', 'e10-1', 'e10-2', 'e4', 'e11')
        self.add_contour('c1', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
