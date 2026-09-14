"""Pen (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50e47373-cb10-491f-a428-767a767f9cef'
SOURCE_PATH = 'icons-json/design/pen_50e47373-cb10-491f-a428-767a767f9cef.json'
AUTHOR = 'json_to_solo'

class Pen50e47373(Solo48):
    icon_id = 'pen-50e47373'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pen', 'design')

    def build(self):
        self.add_line('e0', (37, 20), (28, 11))
        self.add_line('e1', (10, 30), (31, 8))
        self.add_line('e2', (40, 17), (18, 39))
        self.add_line('e3', (18, 39), (10, 30))
        self.add_line('e4', (10, 30), (6, 42))
        self.add_line('e5', (6, 42), (18, 39))
        self.add_arc('e6-1', (31, 8), (35, 6), radius_x=5)
        self.add_arc('e6-2', (35, 6), (42, 13), radius_x=7)
        self.add_line('e6-3', (42, 13), (40, 17))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e6-1', 'e6-2', 'e6-3', 'e2')
        self.add_contour('c2', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
