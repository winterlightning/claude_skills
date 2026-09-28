"""Triangle (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f3278f2-204f-48d0-a5f6-ed0aeccba60e'
SOURCE_PATH = 'pictographic-primitives/design/triangle_7f3278f2-204f-48d0-a5f6-ed0aeccba60e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Triangle(Solo48):
    icon_id = 'triangle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('triangle', 'design')

    def build(self):
        self.add_line('e0', (44, 40), (24, 8))
        self.add_line('e1', (24, 8), (4, 40))
        self.add_line('e2', (4, 40), (44, 40))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
