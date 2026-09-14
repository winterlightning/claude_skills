"""Pen (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ee2f930-e642-4295-aaa3-5150e3fc91e5'
SOURCE_PATH = 'icons-json/design/pen_7ee2f930-e642-4295-aaa3-5150e3fc91e5.json'
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
        self.add_line('e0', (6, 42), (10, 30))
        self.add_line('e1', (11, 29), (32, 8))
        self.add_line('e2', (40, 17), (21, 37))
        self.add_line('e3', (19, 38), (6, 42))
        self.add_bezier('e4', (10, 30), ((10.106, 29.681), (10.779, 29.221), (11, 29)))
        self.add_bezier('e5', (32, 8), ((32.886, 7.114), (34.709, 6), (35.983, 6)), ((36.004, 6), (36.024, 6), (36.044, 6)), ((38.932, 6), (41.992, 8.708), (41.992, 11.654)), ((41.992, 11.831), (42, 12.008), (42, 12.185)), ((42, 12.188), (42, 12.191), (42, 12.194)), ((42, 13.805), (41.145, 15.805), (40, 17)))
        self.add_bezier('e6', (21, 37), ((20.607, 37.409), (19.524, 37.836), (19, 38)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2', 'e6', 'e3', closed=True)
