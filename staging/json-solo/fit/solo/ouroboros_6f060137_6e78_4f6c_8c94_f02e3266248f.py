"""Ouroboros (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f060137-6e78-4f6c-8c94-f02e3266248f'
SOURCE_PATH = 'icons-json/_uncategorized_29/ouroboros_6f060137-6e78-4f6c-8c94-f02e3266248f.json'
AUTHOR = 'json_to_solo'

class OuroborosUncategorized(Solo48):
    icon_id = 'ouroboros-uncategorized'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('ouroboros', '_uncategorized')

    def build(self):
        self.add_line('e0-1', (8, 17), (6, 25))
        self.add_arc('e0-2', (6, 25), (14, 39), radius_x=17, sweep=False)
        self.add_arc('e0-3', (14, 39), (18, 41), radius_x=18, sweep=False)
        self.add_line('e0-4', (18, 41), (24, 42))
        self.add_line('e0-5', (24, 42), (30, 41))
        self.add_arc('e0-6', (30, 41), (34, 39), radius_x=18, sweep=False)
        self.add_arc('e0-7', (34, 39), (42, 25), radius_x=17, sweep=False)
        self.add_arc('e0-8', (42, 25), (25, 6), radius_x=21, sweep=False)
        self.add_arc('e0-9', (25, 6), (8, 17), radius_x=20, sweep=False)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', 'e0-7', 'e0-8', 'e0-9', closed=True)
