"""Chef gear cookie bowl (food), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47c59a46-f46e-420a-b3f5-7db2c1a091f0'
SOURCE_PATH = 'icons-json/food/chef gear cookie bowl_47c59a46-f46e-420a-b3f5-7db2c1a091f0.json'
AUTHOR = 'json_to_solo'

class ChefGearCookieBowl(Solo48):
    icon_id = 'chef-gear-cookie-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('chef', 'gear', 'cookie', 'bowl', 'food')

    def build(self):
        self.add_line('e0', (39, 21), (39, 23))
        self.add_line('e1', (17, 23), (9, 23))
        self.add_line('e2', (17, 23), (39, 23))
        self.add_line('e3', (39, 23), (42, 23))
        self.add_line('e4', (32, 42), (16, 42))
        self.add_line('e5', (15, 36), (12, 35))
        self.add_line('e6', (6, 23), (9, 23))
        self.add_arc('e7-1', (25, 8), (19, 6), radius_x=11, sweep=False)
        self.add_arc('e7-2', (19, 6), (9, 23), radius_x=12, sweep=False)
        self.add_arc('e8-1', (17, 23), (25, 10), radius_x=11)
        self.add_arc('e8-2', (25, 10), (29, 10), radius_x=4)
        self.add_arc('e8-3', (29, 10), (30, 14), radius_x=6, sweep=False)
        self.add_arc('e8-4', (30, 14), (34, 16), radius_x=5, sweep=False)
        self.add_arc('e8-5', (34, 16), (36, 20), radius_x=5, sweep=False)
        self.add_line('e8-6', (36, 20), (39, 21))
        self.add_arc('e9-1', (42, 23), (40, 30), radius_x=14)
        self.add_arc('e9-2', (40, 30), (33, 37), radius_x=20)
        self.add_arc('e9-3', (33, 37), (33, 41), radius_x=5, sweep=False)
        self.add_arc('e9-4', (33, 41), (32, 42), radius_x=1)
        self.add_line('e10', (16, 42), (15, 36))
        self.add_arc('e11-1', (12, 35), (6, 24), radius_x=16)
        self.add_line('e11-2', (6, 24), (6, 23))
        self.add_contour('c0', 'e7-1', 'e7-2')
        self.add_contour('c1', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5', 'e8-6', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e4', 'e10', 'e5', 'e11-1', 'e11-2', 'e6')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
