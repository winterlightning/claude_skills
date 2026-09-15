"""Pyramid shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7abc4afc-60b5-532e-bf33-54ffd635eba0'
SOURCE_PATH = 'pictographic-primitives/design/pyramid shape_7abc4afc-60b5-532e-bf33-54ffd635eba0.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PyramidShape(Solo48):
    icon_id = 'pyramid-shape'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pyramid', 'shape', 'design')

    def build(self):
        self.add_line('e0', (24, 6), (42, 33))
        self.add_line('e1', (42, 33), (24, 42))
        self.add_line('e2', (24, 42), (6, 33))
        self.add_line('e3', (6, 33), (24, 6))
        self.add_line('e4', (24, 6), (24, 42))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
