"""@ (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e799354-211d-4a17-873a-6f0ec808f6e8'
SOURCE_PATH = 'icons-json/state/@_6e799354-211d-4a17-873a-6f0ec808f6e8.json'
AUTHOR = 'json_to_solo'

class IconState(Solo48):
    icon_id = 'icon-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('state',)

    def build(self):
        self.add_line('e0', (28, 41), (25, 42))
        self.add_line('e1', (34, 31), (32, 28))
        self.add_arc('e2-1', (25, 42), (21, 42), radius_x=18, sweep=False)
        self.add_arc('e2-2', (21, 42), (14, 39), radius_x=20)
        self.add_arc('e2-3', (14, 39), (9, 34), radius_x=18)
        self.add_arc('e2-4', (9, 34), (7, 30), radius_x=17)
        self.add_line('e2-5', (7, 30), (6, 24))
        self.add_arc('e2-6', (6, 24), (24, 6), radius_x=18)
        self.add_line('e2-7', (24, 6), (31, 7))
        self.add_arc('e2-8', (31, 7), (36, 10), radius_x=18)
        self.add_arc('e2-9', (36, 10), (40, 15), radius_x=18)
        self.add_line('e2-10', (40, 15), (42, 23))
        self.add_line('e2-11', (42, 23), (41, 29))
        self.add_arc('e2-12', (41, 29), (39, 31), radius_x=5)
        self.add_arc('e2-13', (39, 31), (34, 31), radius_x=4)
        self.add_arc('e3-1', (32, 28), (20, 31), radius_x=9)
        self.add_arc('e3-2', (20, 31), (19, 18), radius_x=8)
        self.add_arc('e3-3', (19, 18), (30, 18), radius_x=8)
        self.add_arc('e3-4', (30, 18), (32, 28), radius_x=10)
        self.add_contour('c0', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9', 'e2-10', 'e2-11', 'e2-12', 'e2-13', 'e1')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', closed=True)
        self.relate('connect', 'c0', 'c1')
