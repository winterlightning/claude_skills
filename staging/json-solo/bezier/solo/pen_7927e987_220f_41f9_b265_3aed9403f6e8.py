"""Pen (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7927e987-220f-41f9-b265-3aed9403f6e8'
SOURCE_PATH = 'icons-json/design/pen_7927e987-220f-41f9-b265-3aed9403f6e8.json'
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
        self.add_line('e0', (18, 39), (37, 20))
        self.add_line('e1', (10, 30), (29, 11))
        self.add_line('e2', (29, 11), (37, 20))
        self.add_line('e3', (29, 11), (32, 8))
        self.add_line('e4', (39, 18), (37, 20))
        self.add_line('e5', (6, 42), (10, 30))
        self.add_line('e6', (10, 30), (18, 39))
        self.add_line('e7', (18, 39), (6, 42))
        self.add_bezier('e8', (32, 8), ((32.835, 7.165), (34.563, 6), (35.774, 6)), ((35.775, 6), (35.776, 6), (35.777, 6)), ((35.85, 6), (35.93, 6), (36.003, 6)), ((36.076, 6), (36.15, 6.008), (36.224, 6.008)), ((38.875, 6.008), (41.992, 9.305), (41.992, 11.915)), ((41.992, 12.005), (42, 12.087), (42, 12.177)), ((42, 12.179), (42, 12.18), (42, 12.181)), ((42, 12.262), (42, 12.342), (42, 12.423)), ((42, 14.877), (40.579, 16.355), (39, 18)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e8', 'e4')
        self.add_contour('c4', 'e5', 'e6', 'e7', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
