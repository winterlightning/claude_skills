"""Taste tongue (health), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32a014c0-daf4-5e3d-b48d-32fc545c2338'
SOURCE_PATH = 'icons-json/health/taste tongue_32a014c0-daf4-5e3d-b48d-32fc545c2338.json'
AUTHOR = 'json_to_solo'

class TasteTongueHealth(Solo48):
    icon_id = 'taste-tongue-health'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('taste', 'tongue', 'health')

    def build(self):
        self.add_line('e0', (40, 14), (36, 10))
        self.add_line('e1', (24, 19), (24, 31))
        self.add_line('e2', (4, 16), (6, 15))
        self.add_arc('e3', (37, 18), (24, 19), radius_x=15, sweep=False)
        self.add_arc('e4-1', (37, 18), (34, 36), radius_x=24)
        self.add_arc('e4-2', (34, 36), (33, 37), radius_x=11)
        self.add_arc('e4-3', (33, 37), (24, 40), radius_x=15)
        self.add_arc('e4-4', (24, 40), (12, 33), radius_x=14)
        self.add_arc('e4-5', (12, 33), (11, 18), radius_x=29)
        self.add_arc('e5-1', (37, 18), (44, 16), radius_x=19, sweep=False)
        self.add_arc('e5-2', (44, 16), (40, 14), radius_x=15, sweep=False)
        self.add_line('e6-1', (36, 10), (33, 8))
        self.add_line('e6-2', (33, 8), (30, 8))
        self.add_arc('e6-3', (30, 8), (24, 11), radius_x=8, sweep=False)
        self.add_arc('e7', (24, 19), (11, 18), radius_x=15, sweep=False)
        self.add_arc('e8', (11, 18), (4, 16), radius_x=18)
        self.add_arc('e9-1', (6, 15), (17, 8), radius_x=16)
        self.add_line('e9-2', (17, 8), (22, 9))
        self.add_arc('e9-3', (22, 9), (24, 11), radius_x=13, sweep=False)
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5')
        self.add_contour('c2', 'e5-1', 'e5-2', 'e0', 'e6-1', 'e6-2', 'e6-3')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e1')
        self.add_contour('c5', 'e8', 'e2', 'e9-1', 'e9-2', 'e9-3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
