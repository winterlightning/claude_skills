"""Corn (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dfc9df01-8144-40e0-b66d-be471956d900'
SOURCE_PATH = 'icons-json/food/corn_dfc9df01-8144-40e0-b66d-be471956d900.json'
AUTHOR = 'json_to_solo'

class Corn(Solo48):
    icon_id = 'corn'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('corn', 'food')

    def build(self):
        self.add_line('e0', (38, 27), (36, 35))
        self.add_line('e1', (18, 27), (15, 24))
        self.add_line('e2', (10, 27), (12, 35))
        self.add_line('e3', (16, 25), (17, 10))
        self.add_line('e4', (31, 10), (32, 25))
        self.add_arc('e5-1', (32, 25), (40, 22), radius_x=17)
        self.add_arc('e5-2', (40, 22), (38, 27), radius_x=22, sweep=False)
        self.add_arc('e6-1', (36, 35), (30, 43), radius_x=12)
        self.add_line('e6-2', (30, 43), (24, 44))
        self.add_line('e6-3', (24, 44), (21, 44))
        self.add_arc('e7', (32, 25), (21, 44), radius_x=20, sweep=False)
        self.add_arc('e8', (23, 34), (18, 27), radius_x=23, sweep=False)
        self.add_arc('e9-1', (15, 24), (8, 22), radius_x=14, sweep=False)
        self.add_arc('e9-2', (8, 22), (10, 27), radius_x=20)
        self.add_arc('e10', (12, 35), (21, 44), radius_x=11, sweep=False)
        self.add_arc('e11-1', (17, 10), (24, 4), radius_x=8)
        self.add_arc('e11-2', (24, 4), (31, 10), radius_x=8)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e0', 'e6-1', 'e6-2', 'e6-3')
        self.add_contour('c1', 'e7')
        self.add_contour('c2', 'e8', 'e1', 'e9-1', 'e9-2', 'e2', 'e10')
        self.add_contour('c3', 'e3', 'e11-1', 'e11-2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c2')
