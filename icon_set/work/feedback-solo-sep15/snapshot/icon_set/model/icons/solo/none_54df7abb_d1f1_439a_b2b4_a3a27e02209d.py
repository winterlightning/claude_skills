"""None (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '54df7abb-d1f1-439a-b2b4-a3a27e02209d'
SOURCE_PATH = 'pictographic-primitives/symbol/none_54df7abb-d1f1-439a-b2b4-a3a27e02209d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class IconNone(Solo48):
    icon_id = 'none'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('none', 'symbol')

    def build(self):
        self.add_line('e0', (8, 44), (8, 4))
        self.add_line('e1', (40, 4), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
