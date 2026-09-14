"""Plane (travel), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39150a1e-77de-4299-ad47-aea402520e87'
SOURCE_PATH = 'icons-json/travel/plane_39150a1e-77de-4299-ad47-aea402520e87.json'
AUTHOR = 'json_to_solo'

class Plane(Solo48):
    icon_id = 'plane'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('plane', 'travel')

    def build(self):
        self.add_line('e0', (22, 18), (16, 13))
        self.add_line('e1', (19, 8), (32, 13))
        self.add_line('e2', (27, 37), (31, 24))
        self.add_line('e3', (32, 23), (40, 19))
        self.add_line('e4', (35, 12), (14, 22))
        self.add_line('e5', (4, 25), (14, 33))
        self.add_line('e6', (14, 33), (22, 28))
        self.add_arc('e7', (16, 13), (19, 8), radius_x=4)
        self.add_line('e8-1', (22, 28), (20, 40))
        self.add_arc('e8-2', (20, 40), (27, 37), radius_x=41, sweep=False)
        self.add_line('e9', (31, 24), (32, 23))
        self.add_arc('e10-1', (40, 19), (44, 14), radius_x=6, sweep=False)
        self.add_arc('e10-2', (44, 14), (35, 12), radius_x=5, sweep=False)
        self.add_arc('e11-1', (14, 22), (6, 20), radius_x=12, sweep=False)
        self.add_line('e11-2', (6, 20), (4, 23))
        self.add_line('e11-3', (4, 23), (4, 25))
        self.add_contour('c0', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e8-1', 'e8-2', 'e2', 'e9', 'e3', 'e10-1', 'e10-2', 'e4', 'e11-1', 'e11-2', 'e11-3', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
