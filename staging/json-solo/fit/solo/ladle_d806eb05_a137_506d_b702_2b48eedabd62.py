"""Ladle (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd806eb05-a137-506d-b702-2b48eedabd62'
SOURCE_PATH = 'icons-json/food/ladle_d806eb05-a137-506d-b702-2b48eedabd62.json'
AUTHOR = 'json_to_solo'

class LadleFood(Solo48):
    icon_id = 'ladle-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('ladle', 'food')

    def build(self):
        self.add_line('e0', (30, 9), (26, 36))
        self.add_line('e1', (8, 33), (26, 33))
        self.add_line('e2-1', (40, 10), (39, 6))
        self.add_arc('e2-2', (39, 6), (36, 4), radius_x=4, sweep=False)
        self.add_line('e2-3', (36, 4), (32, 5))
        self.add_arc('e2-4', (32, 5), (30, 9), radius_x=5, sweep=False)
        self.add_arc('e3-1', (26, 36), (21, 43), radius_x=10)
        self.add_line('e3-2', (21, 43), (16, 44))
        self.add_arc('e3-3', (16, 44), (9, 39), radius_x=8)
        self.add_line('e3-4', (9, 39), (8, 33))
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e1')
