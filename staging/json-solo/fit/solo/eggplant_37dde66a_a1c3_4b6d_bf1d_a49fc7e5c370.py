"""Eggplant (food), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37dde66a-a1c3-4b6d-bf1d-a49fc7e5c370'
SOURCE_PATH = 'icons-json/food/eggplant_37dde66a-a1c3-4b6d-bf1d-a49fc7e5c370.json'
AUTHOR = 'json_to_solo'

class EggplantFood(Solo48):
    icon_id = 'eggplant-food'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('eggplant', 'food')

    def build(self):
        self.add_line('e0', (44, 8), (41, 11))
        self.add_line('e1', (34, 31), (39, 25))
        self.add_line('e2', (39, 25), (40, 26))
        self.add_arc('e3-1', (27, 14), (35, 16), radius_x=9, sweep=False)
        self.add_arc('e3-2', (35, 16), (39, 25), radius_x=9, sweep=False)
        self.add_arc('e4-1', (27, 14), (11, 22), radius_x=16)
        self.add_arc('e4-2', (11, 22), (4, 30), radius_x=9, sweep=False)
        self.add_line('e4-3', (4, 30), (6, 36))
        self.add_line('e4-4', (6, 36), (7, 37))
        self.add_arc('e4-5', (7, 37), (10, 39), radius_x=12, sweep=False)
        self.add_line('e4-6', (10, 39), (15, 40))
        self.add_arc('e4-7', (15, 40), (34, 31), radius_x=30, sweep=False)
        self.add_arc('e5-1', (27, 14), (27, 11), radius_x=2)
        self.add_arc('e5-2', (27, 11), (34, 9), radius_x=15)
        self.add_arc('e5-3', (34, 9), (41, 11), radius_x=11)
        self.add_arc('e6-1', (40, 26), (44, 17), radius_x=13, sweep=False)
        self.add_arc('e6-2', (44, 17), (41, 11), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e3-1', 'e3-2')
        self.add_contour('c2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e1')
        self.add_contour('c3', 'e5-1', 'e5-2', 'e5-3')
        self.add_contour('c4', 'e2', 'e6-1', 'e6-2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
