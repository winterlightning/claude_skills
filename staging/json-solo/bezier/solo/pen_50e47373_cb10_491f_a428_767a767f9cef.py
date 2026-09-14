"""Pen (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50e47373-cb10-491f-a428-767a767f9cef'
SOURCE_PATH = 'icons-json/design/pen_50e47373-cb10-491f-a428-767a767f9cef.json'
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
        self.add_line('e0', (37, 20), (28, 11))
        self.add_line('e1', (10, 30), (31, 8))
        self.add_line('e2', (40, 17), (18, 39))
        self.add_line('e3', (18, 39), (10, 30))
        self.add_line('e4', (10, 30), (6, 42))
        self.add_line('e5', (6, 42), (18, 39))
        self.add_bezier('e6', (31, 8), ((32.252, 6.699), (33.72, 6), (35.495, 6)), ((35.498, 6), (35.5, 6), (35.503, 6)), ((35.656, 6), (35.809, 6.016), (35.962, 6.016)), ((36.723, 6.016), (37.475, 6.098), (38.179, 6.409)), ((40.265, 7.317), (41.992, 9.903), (41.992, 12.194)), ((41.992, 12.331), (42, 12.467), (42, 12.597)), ((42, 12.599), (42, 12.601), (42, 12.603)), ((42, 12.734), (41.992, 12.865), (41.992, 12.995)), ((41.992, 14.231), (40.859, 16.141), (40, 17)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e6', 'e2')
        self.add_contour('c2', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
