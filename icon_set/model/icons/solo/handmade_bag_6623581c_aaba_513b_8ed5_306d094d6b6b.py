"""Handmade bag (hobbies), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6623581c-aaba-513b-8ed5-306d094d6b6b'
SOURCE_PATH = 'icons-json/hobbies/handmade bag_6623581c-aaba-513b-8ed5-306d094d6b6b.json'
AUTHOR = 'gpt-6'

class HandmadeBag(Solo48):
    icon_id = 'handmade-bag'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    aliases = ()
    keywords = ('handmade', 'bag', 'hobbies')

    def build(self):
        self.add_line('sym-e0', (15, 23), (15, 13))
        self.add_arc('sym-e1', (15, 13), (16, 12), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('sym-e2', (16, 12), (23, 6), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('sym-e3', (23, 6), (24, 6))
        self.add_arc('sym-e6', (24, 6), (25, 6), radius_x=51, radius_y=51, large_arc=False, sweep=False)
        self.add_arc('sym-e7', (25, 6), (32, 12), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('sym-e8', (32, 12), (33, 13), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('sym-e9', (33, 13), (33, 23))
        self.add_line('sym-e10', (9, 18), (39, 18))
        self.add_arc('sym-e12', (39, 18), (40, 20), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e13', (40, 20), (42, 35))
        self.add_line('sym-e14-1', (42, 35), (42, 39))
        self.add_arc('sym-e16', (42, 39), (37, 42), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e17', (37, 42), (12, 42))
        self.add_arc('sym-e20', (12, 42), (11, 42), radius_x=22, radius_y=22, large_arc=False, sweep=False)
        self.add_arc('sym-e21', (11, 42), (6, 39), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e22', (6, 39), (6, 35))
        self.add_line('sym-e24', (6, 35), (8, 20))
        self.add_arc('sym-e25', (8, 20), (9, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=False)
        self.add_contour('sym-c1', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e14-1', 'sym-e16', 'sym-e17', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e24', 'sym-e25', closed=True)
