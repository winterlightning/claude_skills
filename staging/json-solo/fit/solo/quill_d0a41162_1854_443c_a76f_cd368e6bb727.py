"""Quill (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e6-1', (11, 31), (21, 15), radius_x=20)
        self.add_line('e6-2', (21, 15), (35, 8))
        self.add_arc('e7-1', (41, 12), (29, 34), radius_x=37)
        self.add_arc('e7-2', (29, 34), (14, 37), radius_x=17)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6-1', 'e6-2', 'e3', 'e4', 'e7-1', 'e7-2', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
