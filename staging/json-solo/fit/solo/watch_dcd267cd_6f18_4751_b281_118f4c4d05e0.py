"""Batch-02/watch (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dcd267cd-6f18-4751-b281-118f4c4d05e0'
SOURCE_PATH = 'icons-json/accessories/batch-02/watch_dcd267cd-6f18-4751-b281-118f4c4d05e0.json'
AUTHOR = 'json_to_solo'

class Batch02Watch(Solo48):
    icon_id = 'batch-02-watch'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'watch', 'accessories')

    def build(self):
        self.add_line('e0', (24, 34), (26, 33))
        self.add_line('e1', (26, 31), (26, 17))
        self.add_line('e2', (23, 34), (9, 34))
        self.add_line('e3', (31, 42), (17, 42))
        self.add_line('e4', (9, 14), (24, 14))
        self.add_line('e5', (6, 17), (6, 31))
        self.add_line('e6', (30, 6), (18, 6))
        self.add_arc('e7-1', (42, 30), (37, 40), radius_x=18)
        self.add_line('e7-2', (37, 40), (31, 42))
        self.add_arc('e7-3', (31, 42), (24, 34), radius_x=12)
        self.add_arc('e8', (26, 33), (26, 31), radius_x=5)
        self.add_arc('e9-1', (26, 17), (24, 14), radius_x=3, sweep=False)
        self.add_line('e9-2', (24, 14), (25, 11))
        self.add_arc('e9-3', (25, 11), (32, 6), radius_x=8)
        self.add_arc('e9-4', (32, 6), (42, 18), radius_x=13)
        self.add_arc('e9-5', (42, 18), (32, 23), radius_x=7)
        self.add_arc('e10', (17, 42), (9, 34), radius_x=12)
        self.add_arc('e11', (8, 14), (6, 17), radius_x=4, sweep=False)
        self.add_arc('e12', (6, 31), (9, 34), radius_x=3, sweep=False)
        self.add_arc('e13', (18, 6), (9, 14), radius_x=12, sweep=False)
        self.add_contour('c0', 'e7-1', 'e7-2', 'e7-3', 'e0', 'e8', 'e1', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e9-5')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e10')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e11', 'e5', 'e12')
        self.add_contour('c5', 'e6', 'e13')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c0')
