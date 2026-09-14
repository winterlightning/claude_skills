"""Hierarchy (programing), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03c563a0-7c54-57e4-a8ff-454322ef2c14'
SOURCE_PATH = 'icons-json/programing/hierarchy_03c563a0-7c54-57e4-a8ff-454322ef2c14.json'
AUTHOR = 'json_to_solo'

class Hierarchy03c563a0(Solo48):
    icon_id = 'hierarchy-03c563a0'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('hierarchy', 'programing')

    def build(self):
        self.add_line('e0', (10, 30), (7, 30))
        self.add_line('e1', (6, 40), (14, 40))
        self.add_line('e2', (17, 37), (17, 32))
        self.add_line('e3', (10, 30), (11, 24))
        self.add_line('e4', (11, 24), (38, 24))
        self.add_line('e5', (38, 24), (38, 30))
        self.add_line('e6', (24, 24), (24, 17))
        self.add_line('e7', (24, 17), (29, 17))
        self.add_line('e8', (29, 8), (19, 8))
        self.add_line('e9', (17, 11), (17, 15))
        self.add_line('e10', (19, 17), (24, 17))
        self.add_line('e11', (31, 33), (31, 37))
        self.add_line('e12', (34, 40), (41, 40))
        self.add_line('e13', (44, 37), (44, 32))
        self.add_line('e14', (41, 30), (37, 30))
        self.add_arc('e15-1', (7, 30), (4, 32), radius_x=3, sweep=False)
        self.add_arc('e15-2', (4, 32), (4, 35), radius_x=17)
        self.add_line('e15-3', (4, 35), (4, 38))
        self.add_arc('e15-4', (4, 38), (6, 40), radius_x=3, sweep=False)
        self.add_arc('e16', (14, 40), (17, 37), radius_x=3, sweep=False)
        self.add_arc('e17', (17, 32), (10, 30), radius_x=5, sweep=False)
        self.add_arc('e18-1', (29, 17), (32, 16), radius_x=2, sweep=False)
        self.add_line('e18-2', (32, 16), (32, 10))
        self.add_arc('e18-3', (32, 10), (30, 8), radius_x=2, sweep=False)
        self.add_line('e18-4', (30, 8), (29, 8))
        self.add_arc('e19', (19, 8), (17, 11), radius_x=3, sweep=False)
        self.add_arc('e20', (17, 15), (19, 17), radius_x=2, sweep=False)
        self.add_arc('e21', (37, 30), (31, 33), radius_x=4, sweep=False)
        self.add_arc('e22', (31, 37), (34, 40), radius_x=3, sweep=False)
        self.add_arc('e23', (41, 40), (44, 37), radius_x=3, sweep=False)
        self.add_arc('e24', (44, 32), (41, 30), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e15-1', 'e15-2', 'e15-3', 'e15-4', 'e1', 'e16', 'e2', 'e17', 'e3', 'e4', 'e5')
        self.add_contour('c1', 'e6', 'e7', 'e18-1', 'e18-2', 'e18-3', 'e18-4', 'e8', 'e19', 'e9', 'e20', 'e10')
        self.add_contour('c2', 'e21', 'e11', 'e22', 'e12', 'e23', 'e13', 'e24', 'e14', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c0')
