"""Pen (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7927e987-220f-41f9-b265-3aed9403f6e8'
SOURCE_PATH = 'icons-json/design/pen_7927e987-220f-41f9-b265-3aed9403f6e8.json'
AUTHOR = 'json_to_solo'

class Pen7927e987(Solo48):
    icon_id = 'pen-7927e987'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pen', 'design')

    def build(self):
        self.add_line('e0', (18, 39), (37, 20))
        self.add_line('e1', (10, 30), (29, 11))
        self.add_line('e2', (29, 11), (37, 20))
        self.add_line('e3', (29, 11), (32, 8))
        self.add_line('e4', (39, 18), (37, 20))
        self.add_line('e5', (6, 42), (10, 30))
        self.add_line('e6', (10, 30), (18, 39))
        self.add_line('e7', (18, 39), (6, 42))
        self.add_arc('e8-1', (32, 8), (36, 6), radius_x=6)
        self.add_arc('e8-2', (36, 6), (42, 12), radius_x=7)
        self.add_arc('e8-3', (42, 12), (39, 18), radius_x=8)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e8-1', 'e8-2', 'e8-3', 'e4')
        self.add_contour('c4', 'e5', 'e6', 'e7', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
