"""Triangle (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4208180-348f-4efd-9c97-aa942b6924da'
SOURCE_PATH = 'pictographic-primitives/design/triangle_b4208180-348f-4efd-9c97-aa942b6924da.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class TriangleDesign(Solo48):
    icon_id = 'triangle-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('triangle', 'design')

    def build(self):
        self.add_line('e0', (44, 40), (24, 8))
        self.add_line('e1', (24, 8), (4, 40))
        self.add_line('e2', (4, 40), (44, 40))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
