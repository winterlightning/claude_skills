"""Math (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '623f8b25-c15d-42c1-87af-b086cba90fe2'
SOURCE_PATH = 'pictographic-primitives/symbol/math_623f8b25-c15d-42c1-87af-b086cba90fe2.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Math(Solo48):
    icon_id = 'math'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('math', 'symbol')

    def build(self):
        self.add_line('e0', (24, 4), (24, 19))
        self.add_line('e1', (24, 19), (8, 19))
        self.add_line('e2', (24, 35), (24, 19))
        self.add_line('e3', (24, 19), (40, 19))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
