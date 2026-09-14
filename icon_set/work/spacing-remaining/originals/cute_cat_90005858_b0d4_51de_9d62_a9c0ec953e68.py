"""Cute cat (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90005858-b0d4-51de-9d62-a9c0ec953e68'
SOURCE_PATH = 'icons-json/video-games/cute cat_90005858-b0d4-51de-9d62-a9c0ec953e68.json'
AUTHOR = 'json_to_solo'

class CuteCat(Solo48):
    icon_id = 'cute-cat'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('cute', 'cat', 'video-games')

    def build(self):
        self.add_line('e0', (22, 35), (24, 33))
        self.add_line('e1', (18, 14), (12, 8))
        self.add_line('e2', (35, 8), (30, 14))
        self.add_line('e3', (19, 33), (22, 35))
        self.add_arc('e4', (24, 33), (29, 33), radius_x=3, sweep=False)
        self.add_line('e7', (30, 14), (18, 14))
        self.add_arc('e8-1', (12, 8), (8, 6), radius_x=6, sweep=False)
        self.add_arc('e8-2', (8, 6), (6, 8), radius_x=2, sweep=False)
        self.add_line('e8-3', (6, 8), (6, 10))
        self.add_line('e8-4', (6, 10), (8, 21))
        self.add_arc('e8-5', (8, 21), (8, 34), radius_x=22, sweep=False)
        self.add_arc('e8-6', (8, 34), (12, 39), radius_x=12, sweep=False)
        self.add_arc('e8-7', (12, 39), (16, 41), radius_x=14, sweep=False)
        self.add_line('e8-8', (16, 41), (24, 42))
        self.add_line('e8-9', (24, 42), (32, 41))
        self.add_arc('e8-10', (32, 41), (40, 34), radius_x=12, sweep=False)
        self.add_arc('e8-11', (40, 34), (40, 21), radius_x=22, sweep=False)
        self.add_line('e8-12', (40, 21), (42, 10))
        self.add_arc('e8-13', (42, 10), (42, 8), radius_x=14)
        self.add_arc('e8-14', (42, 8), (40, 6), radius_x=2, sweep=False)
        self.add_line('e8-15', (40, 6), (35, 8))
        self.add_contour('c0', 'e3', 'e0', 'e4')
        self.add_contour('c3', 'e7', 'e1', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5', 'e8-6', 'e8-7', 'e8-8', 'e8-9', 'e8-10', 'e8-11', 'e8-12', 'e8-13', 'e8-14', 'e8-15', 'e2', closed=True)
