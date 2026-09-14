"""Binoculars (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c302c027-d345-469d-98e7-0e924b296946'
SOURCE_PATH = 'icons-json/outdoors/binoculars_c302c027-d345-469d-98e7-0e924b296946.json'
AUTHOR = 'json_to_solo'

class BinocularsOutdoors(Solo48):
    icon_id = 'binoculars-outdoors'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('binoculars', 'outdoors')

    def build(self):
        self.add_line('e0', (6, 24), (7, 22))
        self.add_line('e1', (20, 24), (20, 14))
        self.add_line('e2', (10, 12), (9, 18))
        self.add_line('e3', (9, 18), (7, 22))
        self.add_line('e4', (20, 24), (20, 17))
        self.add_line('e5', (20, 17), (28, 17))
        self.add_line('e6', (28, 17), (28, 24))
        self.add_line('e7', (37, 11), (41, 23))
        self.add_arc('e8', (20, 24), (7, 22), radius_x=10, sweep=False)
        self.add_arc('e9-1', (20, 24), (14, 40), radius_x=10)
        self.add_arc('e9-2', (14, 40), (4, 30), radius_x=10)
        self.add_arc('e9-3', (4, 30), (6, 24), radius_x=13)
        self.add_arc('e10-1', (20, 14), (16, 8), radius_x=5, sweep=False)
        self.add_arc('e10-2', (16, 8), (13, 9), radius_x=5, sweep=False)
        self.add_arc('e10-3', (13, 9), (10, 12), radius_x=6, sweep=False)
        self.add_arc('e11-1', (28, 24), (40, 22), radius_x=10)
        self.add_arc('e11-2', (40, 22), (43, 26), radius_x=6)
        self.add_line('e11-3', (43, 26), (44, 31))
        self.add_arc('e11-4', (44, 31), (35, 40), radius_x=9)
        self.add_arc('e11-5', (35, 40), (26, 28), radius_x=10)
        self.add_line('e11-6', (26, 28), (28, 21))
        self.add_arc('e11-7', (28, 21), (28, 11), radius_x=35)
        self.add_arc('e11-8', (28, 11), (29, 9), radius_x=3)
        self.add_arc('e11-9', (29, 9), (32, 8), radius_x=5)
        self.add_arc('e11-10', (32, 8), (35, 9), radius_x=5)
        self.add_arc('e11-11', (35, 9), (37, 11), radius_x=4)
        self.add_contour('c0', 'e8')
        self.add_contour('c1', 'e9-1', 'e9-2', 'e9-3', 'e0')
        self.add_contour('c2', 'e1', 'e10-1', 'e10-2', 'e10-3', 'e2', 'e3')
        self.add_contour('c3', 'e4', 'e5', 'e6', 'e11-1', 'e11-2', 'e11-3', 'e11-4', 'e11-5', 'e11-6', 'e11-7', 'e11-8', 'e11-9', 'e11-10', 'e11-11', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c2')
