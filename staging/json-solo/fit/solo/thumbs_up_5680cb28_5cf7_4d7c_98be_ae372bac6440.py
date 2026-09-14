"""Thumbs up (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5680cb28-5cf7-4d7c-98be-ae372bac6440'
SOURCE_PATH = 'icons-json/symbol/thumbs up_5680cb28-5cf7-4d7c-98be-ae372bac6440.json'
AUTHOR = 'json_to_solo'

class ThumbsUp(Solo48):
    icon_id = 'thumbs-up'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('thumbs', 'up', 'symbol')

    def build(self):
        self.add_line('e0', (39, 21), (29, 21))
        self.add_line('e1', (29, 21), (30, 13))
        self.add_line('e2', (27, 6), (25, 6))
        self.add_line('e3', (25, 6), (24, 10))
        self.add_line('e4', (13, 22), (8, 22))
        self.add_line('e5', (6, 23), (6, 39))
        self.add_line('e6', (23, 42), (34, 42))
        self.add_arc('e7', (30, 13), (27, 6), radius_x=6, sweep=False)
        self.add_arc('e8-1', (24, 10), (18, 20), radius_x=27)
        self.add_arc('e8-2', (18, 20), (13, 22), radius_x=6)
        self.add_arc('e9', (8, 22), (6, 23), radius_x=2)
        self.add_arc('e10-1', (6, 39), (13, 39), radius_x=17, sweep=False)
        self.add_arc('e10-2', (13, 39), (23, 42), radius_x=24, sweep=False)
        self.add_arc('e11-1', (34, 42), (37, 41), radius_x=5, sweep=False)
        self.add_arc('e11-2', (37, 41), (39, 38), radius_x=5, sweep=False)
        self.add_arc('e11-3', (39, 38), (39, 34), radius_x=6, sweep=False)
        self.add_arc('e11-4', (39, 34), (41, 29), radius_x=5, sweep=False)
        self.add_line('e11-5', (41, 29), (40, 27))
        self.add_arc('e11-6', (40, 27), (42, 24), radius_x=4, sweep=False)
        self.add_arc('e11-7', (42, 24), (39, 21), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2', 'e3', 'e8-1', 'e8-2', 'e4', 'e9', 'e5', 'e10-1', 'e10-2', 'e6', 'e11-1', 'e11-2', 'e11-3', 'e11-4', 'e11-5', 'e11-6', 'e11-7', closed=True)
