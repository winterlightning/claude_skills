"""Casino clover (entertainment), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '940923da-19e4-4b49-811d-53f2118f022d'
SOURCE_PATH = 'icons-json/entertainment/casino clover_940923da-19e4-4b49-811d-53f2118f022d.json'
AUTHOR = 'json_to_solo'

class CasinoClover(Solo48):
    icon_id = 'casino-clover'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('casino', 'clover', 'entertainment')

    def build(self):
        self.add_line('e0', (29, 20), (31, 18))
        self.add_line('e1', (19, 20), (17, 18))
        self.add_line('e2', (18, 31), (24, 28))
        self.add_line('e3', (24, 38), (24, 28))
        self.add_arc('e4-1', (31, 18), (38, 16), radius_x=14)
        self.add_arc('e4-2', (38, 16), (41, 18), radius_x=5)
        self.add_arc('e4-3', (41, 18), (42, 21), radius_x=5)
        self.add_arc('e4-4', (42, 21), (40, 25), radius_x=5)
        self.add_arc('e4-5', (40, 25), (42, 29), radius_x=5)
        self.add_arc('e4-6', (42, 29), (37, 34), radius_x=5)
        self.add_arc('e4-7', (37, 34), (24, 28), radius_x=29)
        self.add_line('e5-1', (17, 18), (10, 16))
        self.add_arc('e5-2', (10, 16), (7, 18), radius_x=5, sweep=False)
        self.add_arc('e5-3', (7, 18), (6, 21), radius_x=5, sweep=False)
        self.add_arc('e5-4', (6, 21), (8, 25), radius_x=6, sweep=False)
        self.add_arc('e5-5', (8, 25), (6, 29), radius_x=5, sweep=False)
        self.add_arc('e5-6', (6, 29), (7, 32), radius_x=5, sweep=False)
        self.add_arc('e5-7', (7, 32), (10, 34), radius_x=4, sweep=False)
        self.add_arc('e5-8', (10, 34), (18, 31), radius_x=14, sweep=False)
        self.add_arc('e6-1', (29, 42), (26, 41), radius_x=5)
        self.add_arc('e6-2', (26, 41), (24, 38), radius_x=4)
        self.add_arc('e7-1', (18, 19), (15, 9), radius_x=11)
        self.add_arc('e7-2', (15, 9), (19, 6), radius_x=5)
        self.add_arc('e7-3', (19, 6), (24, 9), radius_x=6)
        self.add_arc('e7-4', (24, 9), (28, 6), radius_x=5)
        self.add_arc('e7-5', (28, 6), (31, 7), radius_x=5)
        self.add_arc('e7-6', (31, 7), (33, 9), radius_x=5)
        self.add_arc('e7-7', (33, 9), (30, 19), radius_x=12)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7')
        self.add_contour('c1', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e2')
        self.add_contour('c2', 'e6-1', 'e6-2', 'e3')
        self.add_contour('c3', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e7-6', 'e7-7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c1')
        self.relate('connect', 'c3', 'c0')
