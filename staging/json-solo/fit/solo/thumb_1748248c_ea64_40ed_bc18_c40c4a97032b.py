"""Thumb (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1748248c-ea64-40ed-bc18-c40c4a97032b'
SOURCE_PATH = 'icons-json/state/thumb_1748248c-ea64-40ed-bc18-c40c4a97032b.json'
AUTHOR = 'json_to_solo'

class ThumbState(Solo48):
    icon_id = 'thumb-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('thumb', 'state')

    def build(self):
        self.add_line('e0', (28, 19), (30, 12))
        self.add_line('e1', (8, 23), (8, 39))
        self.add_line('e2', (16, 41), (19, 43))
        self.add_line('e3', (23, 44), (32, 44))
        self.add_line('e4', (37, 39), (40, 25))
        self.add_arc('e5-1', (30, 12), (26, 4), radius_x=6, sweep=False)
        self.add_arc('e5-2', (26, 4), (24, 5), radius_x=3, sweep=False)
        self.add_arc('e5-3', (24, 5), (20, 15), radius_x=26)
        self.add_arc('e5-4', (20, 15), (16, 19), radius_x=12)
        self.add_line('e5-5', (16, 19), (9, 21))
        self.add_arc('e5-6', (9, 21), (8, 23), radius_x=3, sweep=False)
        self.add_arc('e6-1', (8, 39), (11, 41), radius_x=3, sweep=False)
        self.add_line('e6-2', (11, 41), (16, 41))
        self.add_arc('e7', (19, 43), (23, 44), radius_x=10, sweep=False)
        self.add_arc('e8', (32, 44), (37, 39), radius_x=6, sweep=False)
        self.add_line('e9-1', (40, 25), (39, 21))
        self.add_line('e9-2', (39, 21), (37, 20))
        self.add_arc('e9-3', (37, 20), (28, 19), radius_x=24)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e1', 'e6-1', 'e6-2', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9-1', 'e9-2', 'e9-3', closed=True)
