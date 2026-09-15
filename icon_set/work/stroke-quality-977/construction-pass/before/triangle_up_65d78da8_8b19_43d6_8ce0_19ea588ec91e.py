"""Triangle up (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65d78da8-8b19-43d6-8ce0-19ea588ec91e'
SOURCE_PATH = 'pictographic-primitives/symbol/triangle up_65d78da8-8b19-43d6-8ce0-19ea588ec91e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class TriangleUp(Solo48):
    icon_id = 'triangle-up-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('triangle', 'up', 'symbol')

    def build(self):
        self.add_line('e0', (4, 40), (23, 8))
        self.add_line('e1', (25, 8), (44, 40))
        self.add_arc('e2', (23, 8), (25, 8), radius_x=40, sweep=False)
        self.add_contour('c0', 'e0', 'e2', 'e1')
