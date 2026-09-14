"""Pen (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d7410cc-8df1-40ed-b2e1-f198d65f3a13'
SOURCE_PATH = 'icons-json/design/pen_4d7410cc-8df1-40ed-b2e1-f198d65f3a13.json'
AUTHOR = 'json_to_solo'

class Pen(Solo48):
    icon_id = 'pen'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pen', 'design')

    def build(self):
        self.add_line('e0', (35, 22), (26, 13))
        self.add_line('e1', (6, 42), (11, 30))
        self.add_line('e2', (11, 30), (32, 8))
        self.add_line('e3', (35, 21), (19, 38))
        self.add_arc('e4-1', (32, 8), (36, 6), radius_x=6)
        self.add_line('e4-2', (36, 6), (40, 7))
        self.add_arc('e4-3', (40, 7), (42, 11), radius_x=7)
        self.add_arc('e4-4', (42, 11), (35, 21), radius_x=13)
        self.add_line('e5', (19, 38), (6, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e3', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
