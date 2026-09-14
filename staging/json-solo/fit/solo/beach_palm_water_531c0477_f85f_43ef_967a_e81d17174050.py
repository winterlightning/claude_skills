"""Beach palm water (recreation), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '531c0477-f85f-43ef-967a-e81d17174050'
SOURCE_PATH = 'icons-json/recreation/beach palm water_531c0477-f85f-43ef-967a-e81d17174050.json'
AUTHOR = 'json_to_solo'

class BeachPalmWaterRecreation(Solo48):
    icon_id = 'beach-palm-water-recreation'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'recreation'
    aliases = ()
    keywords = ('beach', 'palm', 'water', 'recreation')

    def build(self):
        self.add_line('e0', (20, 6), (22, 9))
        self.add_line('e1', (40, 16), (26, 21))
        self.add_line('e2', (26, 21), (12, 26))
        self.add_line('e3', (26, 21), (29, 30))
        self.add_line('e4', (6, 42), (8, 41))
        self.add_arc('e5', (22, 9), (40, 16), radius_x=14)
        self.add_arc('e6-1', (12, 26), (11, 25), radius_x=1)
        self.add_arc('e6-2', (11, 25), (12, 19), radius_x=15)
        self.add_arc('e6-3', (12, 19), (22, 9), radius_x=15)
        self.add_arc('e7-1', (8, 41), (12, 38), radius_x=9, sweep=False)
        self.add_arc('e7-2', (12, 38), (18, 42), radius_x=7, sweep=False)
        self.add_line('e7-3', (18, 42), (25, 39))
        self.add_arc('e7-4', (25, 39), (31, 42), radius_x=8, sweep=False)
        self.add_arc('e7-5', (31, 42), (37, 39), radius_x=9, sweep=False)
        self.add_arc('e7-6', (37, 39), (42, 42), radius_x=7, sweep=False)
        self.add_contour('c0', 'e0', 'e5', 'e1')
        self.add_contour('c1', 'e2', 'e6-1', 'e6-2', 'e6-3')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e7-6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
