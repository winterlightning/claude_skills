"""Whale (animals), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68a536d7-1274-4ac9-a6a2-1c2c8e10550f'
SOURCE_PATH = 'icons-json/animals/whale_68a536d7-1274-4ac9-a6a2-1c2c8e10550f.json'
AUTHOR = 'json_to_solo'

class Whale(Solo48):
    icon_id = 'whale'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('whale', 'animals')

    def build(self):
        self.add_line('e0', (22, 7), (24, 11))
        self.add_line('e1', (24, 11), (24, 14))
        self.add_line('e2', (24, 11), (25, 9))
        self.add_arc('e3-1', (15, 9), (19, 4), radius_x=5)
        self.add_arc('e3-2', (19, 4), (22, 7), radius_x=4)
        self.add_arc('e4', (24, 10), (24, 11), radius_x=15, sweep=False)
        self.add_arc('e5-1', (25, 9), (29, 4), radius_x=5)
        self.add_arc('e5-2', (29, 4), (33, 9), radius_x=5)
        self.add_arc('e6', (27, 44), (30, 33), radius_x=18, sweep=False)
        self.add_line('e7-1', (27, 44), (24, 44))
        self.add_line('e7-2', (24, 44), (21, 44))
        self.add_arc('e8-1', (27, 44), (28, 44), radius_x=31)
        self.add_arc('e8-2', (28, 44), (40, 32), radius_x=12, sweep=False)
        self.add_arc('e8-3', (40, 32), (40, 30), radius_x=33)
        self.add_arc('e9', (30, 33), (18, 33), radius_x=36)
        self.add_arc('e10', (30, 33), (40, 30), radius_x=34, sweep=False)
        self.add_arc('e11', (21, 44), (18, 33), radius_x=18)
        self.add_line('e12-1', (21, 44), (20, 44))
        self.add_arc('e12-2', (20, 44), (8, 32), radius_x=12)
        self.add_line('e12-3', (8, 32), (8, 30))
        self.add_arc('e13', (18, 33), (8, 30), radius_x=33)
        self.add_arc('e14', (24, 14), (40, 30), radius_x=17)
        self.add_arc('e15', (24, 14), (8, 30), radius_x=17, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e0')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2', 'e5-1', 'e5-2')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7-1', 'e7-2')
        self.add_contour('c6', 'e8-1', 'e8-2', 'e8-3')
        self.add_contour('c7', 'e9')
        self.add_contour('c8', 'e10')
        self.add_contour('c9', 'e11')
        self.add_contour('c10', 'e12-1', 'e12-2', 'e12-3')
        self.add_contour('c11', 'e13')
        self.add_contour('c12', 'e14')
        self.add_contour('c13', 'e15')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c12', 'c13')
        self.relate('connect', 'c12', 'c2')
        self.relate('connect', 'c13', 'c2')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c10', 'c5')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c12', 'c6')
        self.relate('connect', 'c12', 'c8')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c11', 'c7')
        self.relate('connect', 'c11', 'c9')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c13')
        self.relate('connect', 'c11', 'c13')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c3')
