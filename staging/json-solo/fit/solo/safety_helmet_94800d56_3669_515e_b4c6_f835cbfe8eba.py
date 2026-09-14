"""Safety helmet (construction), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94800d56-3669-515e-b4c6-f835cbfe8eba'
SOURCE_PATH = 'icons-json/construction/safety helmet_94800d56-3669-515e-b4c6-f835cbfe8eba.json'
AUTHOR = 'json_to_solo'

class SafetyHelmet94800d56(Solo48):
    icon_id = 'safety-helmet-94800d56'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('safety', 'helmet', 'construction')

    def build(self):
        self.add_line('e0', (29, 11), (28, 29))
        self.add_line('e1', (28, 29), (21, 29))
        self.add_line('e2', (21, 29), (19, 11))
        self.add_line('e3', (27, 8), (21, 8))
        self.add_arc('e4-1', (29, 11), (40, 21), radius_x=18)
        self.add_line('e4-2', (40, 21), (42, 31))
        self.add_arc('e4-3', (42, 31), (44, 33), radius_x=3)
        self.add_line('e4-4', (44, 33), (44, 34))
        self.add_arc('e4-5', (44, 34), (41, 37), radius_x=5)
        self.add_arc('e4-6', (41, 37), (34, 39), radius_x=47)
        self.add_line('e4-7', (34, 39), (25, 40))
        self.add_line('e4-8', (25, 40), (14, 39))
        self.add_arc('e4-9', (14, 39), (7, 37), radius_x=35)
        self.add_arc('e4-10', (7, 37), (4, 34), radius_x=5)
        self.add_line('e4-11', (4, 34), (4, 33))
        self.add_arc('e4-12', (4, 33), (6, 31), radius_x=2)
        self.add_arc('e4-13', (6, 31), (10, 18), radius_x=21)
        self.add_arc('e4-14', (10, 18), (19, 11), radius_x=18)
        self.add_arc('e5', (29, 11), (27, 8), radius_x=3, sweep=False)
        self.add_arc('e6', (21, 8), (19, 11), radius_x=3, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e4-9', 'e4-10', 'e4-11', 'e4-12', 'e4-13', 'e4-14')
        self.add_contour('c1', 'e0', 'e1', 'e2')
        self.add_contour('c2', 'e5', 'e3', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
