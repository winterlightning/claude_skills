"""Pot (furnitures), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dcc7af24-9bec-4d53-bd95-0a77208b26b9'
SOURCE_PATH = 'icons-json/furnitures/pot_dcc7af24-9bec-4d53-bd95-0a77208b26b9.json'
AUTHOR = 'json_to_solo'

class PotFurnitures(Solo48):
    icon_id = 'pot-furnitures'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('pot', 'furnitures')

    def build(self):
        self.add_line('e0', (10, 19), (12, 16))
        self.add_line('e1', (35, 33), (35, 39))
        self.add_line('e2', (32, 42), (9, 42))
        self.add_line('e3', (8, 23), (6, 19))
        self.add_line('e4', (6, 19), (31, 19))
        self.add_line('e5', (21, 6), (21, 8))
        self.add_arc('e6-1', (12, 16), (18, 9), radius_x=15)
        self.add_arc('e6-2', (18, 9), (30, 15), radius_x=10)
        self.add_line('e6-3', (30, 15), (35, 33))
        self.add_arc('e7-1', (35, 39), (33, 42), radius_x=3)
        self.add_line('e7-2', (33, 42), (32, 42))
        self.add_arc('e8-1', (9, 42), (6, 39), radius_x=3)
        self.add_line('e8-2', (6, 39), (8, 23))
        self.add_arc('e9-1', (35, 31), (42, 24), radius_x=7, sweep=False)
        self.add_arc('e9-2', (42, 24), (31, 17), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e6-3', 'e1', 'e7-1', 'e7-2', 'e2', 'e8-1', 'e8-2', 'e3', 'e4')
        self.add_contour('c1', 'e9-1', 'e9-2')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
