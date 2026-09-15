"""Helmet (protection), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0209d9df-8004-4d01-8d63-b5f783021ddb'
SOURCE_PATH = 'icons-json/protection/helmet_0209d9df-8004-4d01-8d63-b5f783021ddb.json'
AUTHOR = 'gpt-6'

class Helmet(Solo48):
    icon_id = 'helmet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('helmet', 'protection')

    def build(self):
        self.add_arc('sym-e0', (40, 31), (40, 30), radius_x=31, radius_y=31, large_arc=False, sweep=False)
        self.add_line('sym-e1', (40, 30), (40, 27))
        self.add_arc('sym-e2', (40, 27), (29, 13), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_line('sym-e3', (29, 13), (29, 11))
        self.add_arc('sym-e4', (29, 11), (29, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e5', (29, 10), (26, 8))
        self.add_line('sym-e7', (26, 8), (22, 8))
        self.add_line('sym-e10', (22, 8), (19, 10))
        self.add_arc('sym-e11', (19, 10), (19, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e12', (19, 11), (19, 13))
        self.add_arc('sym-e13', (19, 13), (8, 27), radius_x=17, radius_y=17, large_arc=False, sweep=False)
        self.add_arc('sym-e14', (8, 27), (8, 30), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_arc('sym-e15', (8, 30), (8, 31), radius_x=63, radius_y=63, large_arc=False, sweep=False)
        self.add_line('sym-e16', (8, 31), (6, 31))
        self.add_line('sym-e17', (6, 31), (4, 33))
        self.add_line('sym-e18', (4, 33), (4, 36))
        self.add_line('sym-e20', (4, 36), (5, 39))
        self.add_arc('sym-e21', (5, 39), (5, 40), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('sym-e22', (5, 40), (6, 40), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('sym-e23', (6, 40), (43, 40))
        self.add_arc('sym-e26', (43, 40), (43, 39), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('sym-e27', (43, 39), (44, 36))
        self.add_line('sym-e28', (44, 36), (44, 34))
        self.add_arc('sym-e29', (44, 34), (44, 33), radius_x=34, radius_y=34, large_arc=False, sweep=True)
        self.add_line('sym-e30', (44, 33), (42, 31))
        self.add_line('sym-e31', (42, 31), (29, 31))
        self.add_line('sym-e33', (29, 31), (29, 13))
        self.add_line('sym-e34', (29, 31), (19, 31))
        self.add_line('sym-e36', (19, 31), (19, 13))
        self.add_line('sym-e37', (8, 31), (19, 31))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e33', closed=False)
        self.add_contour('sym-c1', 'sym-e34', 'sym-e36', closed=False)
        self.add_contour('sym-c2', 'sym-e37', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
