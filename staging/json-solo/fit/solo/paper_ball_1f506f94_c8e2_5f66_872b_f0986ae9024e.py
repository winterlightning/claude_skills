"""Paper ball (ecology), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f506f94-c8e2-5f66-872b-f0986ae9024e'
SOURCE_PATH = 'icons-json/ecology/paper ball_1f506f94-c8e2-5f66-872b-f0986ae9024e.json'
AUTHOR = 'json_to_solo'

class PaperBallEcology(Solo48):
    icon_id = 'paper-ball-ecology'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    aliases = ()
    keywords = ('paper', 'ball', 'ecology')

    def build(self):
        self.add_line('e0', (29, 30), (31, 30))
        self.add_line('e1', (31, 30), (40, 33))
        self.add_line('e2', (40, 33), (42, 23))
        self.add_line('e3', (41, 20), (35, 14))
        self.add_line('e4', (32, 8), (26, 7))
        self.add_line('e5', (18, 40), (16, 40))
        self.add_line('e6', (12, 36), (7, 28))
        self.add_line('e7', (18, 25), (20, 29))
        self.add_arc('e8', (26, 22), (34, 12), radius_x=21, sweep=False)
        self.add_line('e9-1', (42, 23), (42, 22))
        self.add_arc('e9-2', (42, 22), (41, 20), radius_x=3, sweep=False)
        self.add_line('e10', (35, 14), (32, 8))
        self.add_arc('e11-1', (26, 7), (23, 6), radius_x=9, sweep=False)
        self.add_line('e11-2', (23, 6), (10, 14))
        self.add_line('e11-3', (10, 14), (9, 17))
        self.add_arc('e12-1', (40, 33), (26, 42), radius_x=21)
        self.add_arc('e12-2', (26, 42), (18, 40), radius_x=18, sweep=False)
        self.add_arc('e13', (16, 40), (12, 36), radius_x=4)
        self.add_arc('e14-1', (7, 28), (6, 26), radius_x=3)
        self.add_arc('e14-2', (6, 26), (9, 20), radius_x=15)
        self.add_line('e14-3', (9, 20), (9, 18))
        self.add_arc('e14-4', (9, 18), (10, 18), radius_x=1)
        self.add_line('e14-5', (10, 18), (12, 19))
        self.add_arc('e14-6', (12, 19), (18, 25), radius_x=7)
        self.add_contour('c0', 'e8')
        self.add_contour('c1', 'e0', 'e1', 'e2', 'e9-1', 'e9-2', 'e3', 'e10', 'e4', 'e11-1', 'e11-2', 'e11-3')
        self.add_contour('c2', 'e12-1', 'e12-2', 'e5', 'e13', 'e6', 'e14-1', 'e14-2', 'e14-3', 'e14-4', 'e14-5', 'e14-6', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
