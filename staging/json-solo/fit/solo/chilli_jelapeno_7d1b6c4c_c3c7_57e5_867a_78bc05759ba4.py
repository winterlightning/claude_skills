"""Chilli jelapeno (food), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d1b6c4c-c3c7-57e5-867a-78bc05759ba4'
SOURCE_PATH = 'icons-json/food/chilli jelapeno_7d1b6c4c-c3c7-57e5-867a-78bc05759ba4.json'
AUTHOR = 'json_to_solo'

class ChilliJelapenoFood(Solo48):
    icon_id = 'chilli-jelapeno-food'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('chilli', 'jelapeno', 'food')

    def build(self):
        self.add_arc('e0-1', (40, 18), (35, 17), radius_x=6, sweep=False)
        self.add_line('e0-2', (35, 17), (20, 27))
        self.add_line('e0-3', (20, 27), (4, 29))
        self.add_arc('e0-4', (4, 29), (4, 30), radius_x=3)
        self.add_arc('e0-5', (4, 30), (20, 40), radius_x=18, sweep=False)
        self.add_line('e0-6', (20, 40), (27, 39))
        self.add_arc('e0-7', (27, 39), (33, 36), radius_x=26, sweep=False)
        self.add_arc('e0-8', (33, 36), (42, 26), radius_x=25, sweep=False)
        self.add_arc('e0-9', (42, 26), (40, 18), radius_x=6, sweep=False)
        self.add_arc('e1-1', (40, 18), (44, 12), radius_x=8, sweep=False)
        self.add_arc('e1-2', (44, 12), (40, 8), radius_x=4, sweep=False)
        self.add_line('e2', (40, 8), (41, 8))
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', 'e0-7', 'e0-8', 'e0-9', closed=True)
        self.add_contour('c1', 'e1-1', 'e1-2')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
