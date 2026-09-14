"""Target (war), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa35ca2e-3882-40aa-94b0-a993fab50043'
SOURCE_PATH = 'icons-json/war/target_fa35ca2e-3882-40aa-94b0-a993fab50043.json'
AUTHOR = 'json_to_solo'

class Target(Solo48):
    icon_id = 'target'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('target', 'war')

    def build(self):
        self.add_line('e0', (24, 14), (24, 10))
        self.add_line('e1', (35, 24), (42, 24))
        self.add_line('e2', (24, 34), (24, 42))
        self.add_line('e3', (13, 24), (9, 24))
        self.add_line('e4', (24, 6), (24, 10))
        self.add_line('e5', (6, 24), (9, 24))
        self.add_line('e6', (21, 10), (26, 10))
        self.add_line('e7', (38, 22), (38, 26))
        self.add_arc('e8', (26, 10), (38, 22), radius_x=15)
        self.add_arc('e9-1', (38, 26), (24, 39), radius_x=14)
        self.add_arc('e9-2', (24, 39), (10, 27), radius_x=15)
        self.add_arc('e9-3', (10, 27), (21, 10), radius_x=14)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6', 'e8', 'e7', 'e9-1', 'e9-2', 'e9-3', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
