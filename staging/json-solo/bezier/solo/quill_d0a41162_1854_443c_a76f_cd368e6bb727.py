"""Quill (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0a41162-1854-443c-a76f-cd368e6bb727'
SOURCE_PATH = 'icons-json/design/quill_d0a41162-1854-443c-a76f-cd368e6bb727.json'
AUTHOR = 'json_to_solo'

class QuillDesign(Solo48):
    icon_id = 'quill-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('quill', 'design')

    def build(self):
        self.add_line('e0', (28, 21), (12, 36))
        self.add_line('e1', (6, 42), (12, 36))
        self.add_line('e2', (12, 36), (11, 31))
        self.add_line('e3', (35, 8), (42, 6))
        self.add_line('e4', (42, 6), (41, 12))
        self.add_line('e5', (14, 37), (12, 36))
        self.add_bezier('e6', (11, 31), ((10.411, 27.457), (12.398, 24.033), (14.444, 21.316)), ((19.328, 14.828), (27.465, 10.512), (35, 8)))
        self.add_bezier('e7', (41, 12), ((40.689, 14.16), (40.225, 16.055), (39.554, 18.125)), ((36.87, 26.389), (31.143, 34.775), (22.355, 37.181)), ((19.631, 37.925), (16.692, 37.9), (14, 37)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6', 'e3', 'e4', 'e7', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
