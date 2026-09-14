"""Fried egg (food), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8c37c69-5090-5f93-b20c-c17c99ab9d1c'
SOURCE_PATH = 'icons-json/food/fried egg_b8c37c69-5090-5f93-b20c-c17c99ab9d1c.json'
AUTHOR = 'json_to_solo'

class FriedEggFood(Solo48):
    icon_id = 'fried-egg-food'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('fried', 'egg', 'food')

    def build(self):
        self.add_line('e0', (10, 16), (13, 13))
        self.add_line('e1', (36, 37), (26, 41))
        self.add_arc('e2-top', (17, 24), (31, 24), radius_x=7)
        self.add_arc('e2-bottom', (31, 24), (17, 24), radius_x=7)
        self.add_arc('e3-1', (13, 13), (18, 8), radius_x=16, sweep=False)
        self.add_line('e3-2', (18, 8), (24, 6))
        self.add_arc('e3-3', (24, 6), (34, 12), radius_x=12)
        self.add_arc('e3-4', (34, 12), (40, 21), radius_x=16, sweep=False)
        self.add_arc('e3-5', (40, 21), (42, 27), radius_x=11)
        self.add_arc('e3-6', (42, 27), (36, 37), radius_x=12)
        self.add_line('e4-1', (26, 41), (23, 42))
        self.add_arc('e4-2', (23, 42), (16, 39), radius_x=11)
        self.add_arc('e4-3', (16, 39), (8, 29), radius_x=23, sweep=False)
        self.add_arc('e4-4', (8, 29), (6, 23), radius_x=11)
        self.add_arc('e4-5', (6, 23), (10, 16), radius_x=9)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', closed=True)
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
