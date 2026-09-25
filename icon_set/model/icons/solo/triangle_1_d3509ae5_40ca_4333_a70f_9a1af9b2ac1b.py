"""Triangle 1 (other), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3509ae5-40ca-4333-a70f-9a1af9b2ac1b'
SOURCE_PATH = 'pictographic-primitives/other/triangle 1_d3509ae5-40ca-4333-a70f-9a1af9b2ac1b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Triangle1Other(Solo48):
    icon_id = 'triangle-1-other'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('container', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('triangle', 'other')

    def build(self):
        self.add_line('e0', (24, 6), (6, 42))
        self.add_line('e1', (6, 42), (42, 42))
        self.add_line('e2', (42, 42), (24, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
