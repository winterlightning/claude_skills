"""Seasoning chilli (food), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41f0de58-c686-4c1c-bb67-50e2eae2c9b5'
SOURCE_PATH = 'icons-json/food/seasoning chilli_41f0de58-c686-4c1c-bb67-50e2eae2c9b5.json'
AUTHOR = 'json_to_solo'

class SeasoningChilliFood(Solo48):
    icon_id = 'seasoning-chilli-food'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('seasoning', 'chilli', 'food')

    def build(self):
        self.add_line('e0', (6, 30), (6, 32))
        self.add_arc('e1', (42, 6), (37, 12), radius_x=6, sweep=False)
        self.add_arc('e2-1', (6, 32), (21, 42), radius_x=17, sweep=False)
        self.add_arc('e2-2', (21, 42), (41, 25), radius_x=21, sweep=False)
        self.add_arc('e3-1', (6, 30), (26, 33), radius_x=15, sweep=False)
        self.add_arc('e3-2', (26, 33), (31, 21), radius_x=15, sweep=False)
        self.add_line('e4-1', (31, 21), (33, 21))
        self.add_arc('e4-2', (33, 21), (38, 26), radius_x=6, sweep=False)
        self.add_line('e4-3', (38, 26), (41, 25))
        self.add_line('e4-4', (41, 25), (42, 18))
        self.add_line('e4-5', (42, 18), (40, 13))
        self.add_arc('e4-6', (40, 13), (37, 12), radius_x=7, sweep=False)
        self.add_line('e5-1', (31, 21), (32, 14))
        self.add_arc('e5-2', (32, 14), (37, 12), radius_x=5)
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e0', 'e2-1', 'e2-2')
        self.add_contour('c2', 'e3-1', 'e3-2')
        self.add_contour('c3', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6')
        self.add_contour('c4', 'e5-1', 'e5-2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
