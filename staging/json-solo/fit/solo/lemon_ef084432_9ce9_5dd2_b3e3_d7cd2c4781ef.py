"""Lemon (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef084432-9ce9-5dd2-b3e3-d7cd2c4781ef'
SOURCE_PATH = 'icons-json/food/lemon_ef084432-9ce9-5dd2-b3e3-d7cd2c4781ef.json'
AUTHOR = 'json_to_solo'

class LemonFood(Solo48):
    icon_id = 'lemon-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('lemon', 'food')

    def build(self):
        self.add_line('e0', (18, 8), (13, 12))
        self.add_line('e1', (12, 36), (20, 42))
        self.add_arc('e2-1', (13, 12), (8, 24), radius_x=18, sweep=False)
        self.add_arc('e2-2', (8, 24), (12, 36), radius_x=20, sweep=False)
        self.add_arc('e3-1', (20, 42), (24, 44), radius_x=6, sweep=False)
        self.add_arc('e3-2', (24, 44), (40, 24), radius_x=23, sweep=False)
        self.add_arc('e3-3', (40, 24), (25, 4), radius_x=24, sweep=False)
        self.add_line('e3-4', (25, 4), (21, 5))
        self.add_arc('e3-5', (21, 5), (18, 8), radius_x=23, sweep=False)
        self.add_contour('c0', 'e0', 'e2-1', 'e2-2', 'e1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', closed=True)
