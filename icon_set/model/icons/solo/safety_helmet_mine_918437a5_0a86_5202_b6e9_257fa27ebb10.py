"""Safety helmet mine (construction), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '918437a5-0a86-5202-b6e9-257fa27ebb10'
SOURCE_PATH = 'icons-json/construction/safety helmet mine_918437a5-0a86-5202-b6e9-257fa27ebb10.json'
AUTHOR = 'json_to_solo'

class SafetyHelmetMine(Solo48):
    icon_id = 'safety-helmet-mine'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('safety', 'helmet', 'mine', 'construction')

    def build(self):
        self.add_line('e0', (29, 17), (29, 11))
        self.add_line('e1', (27, 8), (21, 8))
        self.add_line('e2', (19, 12), (19, 17))
        self.add_arc('e3-top', (19, 24), (29, 24), radius_x=5, radius_y=6)
        self.add_arc('e3-bottom', (29, 24), (19, 24), radius_x=5, radius_y=6)
        self.add_arc('e4', (29, 11), (27, 8), radius_x=3, sweep=False)
        self.add_arc('e5', (21, 8), (19, 12), radius_x=3, sweep=False)
        self.add_arc('e6-1', (29, 11), (36, 15), radius_x=19)
        self.add_arc('e6-2', (36, 15), (41, 29), radius_x=19)
        self.add_line('e6-3', (41, 29), (44, 32))
        self.add_arc('e6-4', (44, 32), (44, 33), radius_x=6, sweep=False)
        self.add_arc('e6-5', (44, 33), (38, 38), radius_x=7)
        self.add_line('e6-6', (38, 38), (24, 40))
        self.add_line('e6-7', (24, 40), (10, 38))
        self.add_arc('e6-8', (10, 38), (4, 33), radius_x=6)
        self.add_arc('e6-9', (4, 33), (6, 30), radius_x=4)
        self.add_line('e6-10', (6, 30), (9, 19))
        self.add_arc('e6-11', (9, 19), (19, 11), radius_x=18)
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2')
        self.add_contour('c1', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7', 'e6-8', 'e6-9', 'e6-10', 'e6-11')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c1', 'c0')
