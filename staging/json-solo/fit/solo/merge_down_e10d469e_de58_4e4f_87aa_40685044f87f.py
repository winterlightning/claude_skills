"""Merge down (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e10d469e-de58-4e4f-87aa-40685044f87f'
SOURCE_PATH = 'icons-json/arrows/merge down_e10d469e-de58-4e4f-87aa-40685044f87f.json'
AUTHOR = 'json_to_solo'

class MergeDownArrows(Solo48):
    icon_id = 'merge-down-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('merge', 'down', 'arrows')

    def build(self):
        self.add_line('e0', (24, 19), (24, 44))
        self.add_line('e1', (19, 39), (24, 44))
        self.add_line('e2', (29, 39), (24, 44))
        self.add_line('e3', (25, 15), (24, 19))
        self.add_line('e4-1', (8, 4), (16, 5))
        self.add_arc('e4-2', (16, 5), (19, 7), radius_x=10)
        self.add_arc('e4-3', (19, 7), (24, 19), radius_x=20)
        self.add_arc('e5', (24, 18), (24, 19), radius_x=23, sweep=False)
        self.add_line('e6-1', (40, 4), (32, 5))
        self.add_arc('e6-2', (32, 5), (25, 15), radius_x=14, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e2')
        self.add_contour('c5', 'e6-1', 'e6-2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c5', 'c0')
        self.relate('connect', 'c5', 'c1')
