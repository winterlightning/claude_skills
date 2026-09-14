"""Bandaid (health), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d6f2522-2f4b-4001-af2d-ea58f858d927'
SOURCE_PATH = 'icons-json/health/bandaid_1d6f2522-2f4b-4001-af2d-ea58f858d927.json'
AUTHOR = 'json_to_solo'

class Bandaid(Solo48):
    icon_id = 'bandaid'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('bandaid', 'health')

    def build(self):
        self.add_line('e0', (13, 24), (24, 35))
        self.add_line('e1', (13, 24), (8, 30))
        self.add_line('e2', (18, 40), (24, 35))
        self.add_line('e3', (13, 24), (24, 13))
        self.add_line('e4', (13, 24), (8, 18))
        self.add_line('e5', (18, 8), (24, 13))
        self.add_line('e6', (24, 35), (30, 40))
        self.add_line('e7', (40, 30), (35, 24))
        self.add_line('e8', (24, 35), (35, 24))
        self.add_line('e9', (35, 24), (24, 13))
        self.add_line('e10', (35, 24), (40, 18))
        self.add_line('e11', (30, 8), (24, 13))
        self.add_arc('e12-1', (8, 30), (7, 31), radius_x=4, sweep=False)
        self.add_line('e12-2', (7, 31), (6, 35))
        self.add_arc('e12-3', (6, 35), (10, 41), radius_x=7, sweep=False)
        self.add_line('e12-4', (10, 41), (14, 42))
        self.add_arc('e12-5', (14, 42), (18, 40), radius_x=6, sweep=False)
        self.add_arc('e13-1', (8, 18), (7, 17), radius_x=4)
        self.add_line('e13-2', (7, 17), (6, 13))
        self.add_arc('e13-3', (6, 13), (10, 7), radius_x=7)
        self.add_line('e13-4', (10, 7), (14, 6))
        self.add_arc('e13-5', (14, 6), (18, 8), radius_x=5)
        self.add_arc('e14-1', (30, 40), (34, 42), radius_x=6, sweep=False)
        self.add_arc('e14-2', (34, 42), (42, 34), radius_x=8, sweep=False)
        self.add_arc('e14-3', (42, 34), (40, 30), radius_x=6, sweep=False)
        self.add_arc('e15-1', (40, 18), (42, 13), radius_x=8, sweep=False)
        self.add_line('e15-2', (42, 13), (40, 8))
        self.add_line('e15-3', (40, 8), (34, 6))
        self.add_arc('e15-4', (34, 6), (30, 8), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e12-1', 'e12-2', 'e12-3', 'e12-4', 'e12-5', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e13-1', 'e13-2', 'e13-3', 'e13-4', 'e13-5', 'e5')
        self.add_contour('c4', 'e6', 'e14-1', 'e14-2', 'e14-3', 'e7')
        self.add_contour('c5', 'e8')
        self.add_contour('c6', 'e9')
        self.add_contour('c7', 'e10', 'e15-1', 'e15-2', 'e15-3', 'e15-4', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
