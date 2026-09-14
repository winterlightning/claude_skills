"""Hamburger (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4eb3fceb-2f4c-4167-ac6b-944c1693b563'
SOURCE_PATH = 'icons-json/symbol/hamburger_4eb3fceb-2f4c-4167-ac6b-944c1693b563.json'
AUTHOR = 'json_to_solo'

class Hamburger4eb3fceb(Solo48):
    icon_id = 'hamburger-4eb3fceb'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('hamburger', 'symbol')

    def build(self):
        self.add_line('e0', (33, 20), (36, 18))
        self.add_line('e1', (31, 8), (19, 8))
        self.add_line('e2', (8, 31), (40, 31))
        self.add_line('e3', (35, 40), (14, 40))
        self.add_line('e4-1', (8, 18), (13, 20))
        self.add_arc('e4-2', (13, 20), (22, 18), radius_x=11, sweep=False)
        self.add_line('e4-3', (22, 18), (33, 20))
        self.add_line('e5', (36, 18), (40, 18))
        self.add_arc('e6-1', (40, 18), (39, 12), radius_x=9, sweep=False)
        self.add_arc('e6-2', (39, 12), (32, 8), radius_x=10, sweep=False)
        self.add_line('e6-3', (32, 8), (31, 8))
        self.add_line('e7-1', (19, 8), (13, 9))
        self.add_arc('e7-2', (13, 9), (10, 11), radius_x=9, sweep=False)
        self.add_arc('e7-3', (10, 11), (8, 18), radius_x=10, sweep=False)
        self.add_line('e8-1', (40, 18), (43, 19))
        self.add_arc('e8-2', (43, 19), (44, 21), radius_x=3)
        self.add_arc('e8-3', (44, 21), (41, 24), radius_x=4)
        self.add_arc('e9', (40, 31), (35, 40), radius_x=7)
        self.add_arc('e10-1', (14, 40), (13, 40), radius_x=16, sweep=False)
        self.add_arc('e10-2', (13, 40), (8, 35), radius_x=6)
        self.add_arc('e10-3', (8, 35), (8, 31), radius_x=25)
        self.add_arc('e10-4', (8, 31), (4, 27), radius_x=4)
        self.add_arc('e10-5', (4, 27), (7, 24), radius_x=4)
        self.add_arc('e11-1', (7, 24), (4, 21), radius_x=4)
        self.add_arc('e11-2', (4, 21), (5, 19), radius_x=3)
        self.add_line('e11-3', (5, 19), (8, 18))
        self.add_arc('e12-1', (41, 24), (44, 27), radius_x=4)
        self.add_arc('e12-2', (44, 27), (40, 31), radius_x=4)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e0', 'e5')
        self.add_contour('c1', 'e6-1', 'e6-2', 'e6-3', 'e1', 'e7-1', 'e7-2', 'e7-3')
        self.add_contour('c2', 'e8-1', 'e8-2', 'e8-3')
        self.add_contour('c3', 'e2', 'e9', 'e3', 'e10-1', 'e10-2', 'e10-3', 'e10-4', 'e10-5')
        self.add_contour('c4', 'e11-1', 'e11-2', 'e11-3')
        self.add_contour('c5', 'e12-1', 'e12-2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
