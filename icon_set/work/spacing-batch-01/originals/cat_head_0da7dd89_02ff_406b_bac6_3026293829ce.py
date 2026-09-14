"""Cat head (pets), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0da7dd89-02ff-406b-bac6-3026293829ce'
SOURCE_PATH = 'icons-json/pets/cat head_0da7dd89-02ff-406b-bac6-3026293829ce.json'
AUTHOR = 'json_to_solo'

class CatHead(Solo48):
    icon_id = 'cat-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('cat', 'head', 'pets')

    def build(self):
        self.add_line('e0', (30, 33), (28, 34))
        self.add_line('e1', (7, 13), (8, 20))
        self.add_line('e2', (40, 20), (41, 13))
        self.add_line('e3', (17, 25), (17, 23))
        self.add_arc('e4', (31, 24), (31, 25), radius_x=26)
        self.add_arc('e5', (24, 31), (24, 32), radius_x=34, sweep=False)
        self.add_arc('e6', (18, 33), (24, 32), radius_x=4, sweep=False)
        self.add_arc('e7', (28, 34), (24, 32), radius_x=5)
        self.add_arc('e8-1', (8, 20), (6, 27), radius_x=19, sweep=False)
        self.add_arc('e8-2', (6, 27), (12, 38), radius_x=15, sweep=False)
        self.add_arc('e8-3', (12, 38), (24, 42), radius_x=20, sweep=False)
        self.add_line('e8-4', (24, 42), (30, 41))
        self.add_arc('e8-5', (30, 41), (36, 38), radius_x=20, sweep=False)
        self.add_arc('e8-6', (36, 38), (42, 27), radius_x=15, sweep=False)
        self.add_arc('e8-7', (42, 27), (40, 20), radius_x=20, sweep=False)
        self.add_arc('e9-1', (41, 13), (39, 6), radius_x=5, sweep=False)
        self.add_arc('e9-2', (39, 6), (31, 13), radius_x=16, sweep=False)
        self.add_arc('e9-3', (31, 13), (28, 12), radius_x=6, sweep=False)
        self.add_arc('e9-4', (28, 12), (17, 13), radius_x=18, sweep=False)
        self.add_arc('e9-5', (17, 13), (9, 6), radius_x=19, sweep=False)
        self.add_arc('e9-6', (9, 6), (7, 13), radius_x=6, sweep=False)
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e0', 'e7')
        self.add_contour('c5', 'e1', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5', 'e8-6', 'e8-7', 'e2', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e9-5', 'e9-6', closed=True)
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
