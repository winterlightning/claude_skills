"""Ux (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7321caa-2093-463e-8477-ffed0ebcfa59'
SOURCE_PATH = 'pictographic-primitives/symbol/ux_d7321caa-2093-463e-8477-ffed0ebcfa59.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Ux(Solo48):
    icon_id = 'ux'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ux', 'symbol')

    def build(self):
        self.add_line('e0', (6, 26), (6, 22))
        self.add_line('e1', (35, 6), (42, 6))
        self.add_line('e2', (42, 6), (42, 13))
        self.add_line('e3', (13, 6), (6, 6))
        self.add_line('e4', (6, 6), (6, 13))
        self.add_line('e5', (22, 6), (26, 6))
        self.add_line('e6', (6, 35), (6, 42))
        self.add_line('e7', (6, 42), (13, 42))
        self.add_line('e8', (42, 27), (42, 22))
        self.add_line('e9', (42, 35), (42, 42))
        self.add_line('e10', (42, 42), (36, 42))
        self.add_line('e11', (21, 42), (26, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6', 'e7')
        self.add_contour('c5', 'e8')
        self.add_contour('c6', 'e9', 'e10')
        self.add_contour('c7', 'e11')
