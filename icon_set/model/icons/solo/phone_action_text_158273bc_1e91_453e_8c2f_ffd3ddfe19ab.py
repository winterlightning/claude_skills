"""Phone action text (phones), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '158273bc-1e91-453e-8c2f-ffd3ddfe19ab'
SOURCE_PATH = 'pictographic-primitives/phones/phone action text_158273bc-1e91-453e-8c2f-ffd3ddfe19ab.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PhoneActionText(Solo48):
    icon_id = 'phone-action-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    categories = ('phones', 'primitives')
    aliases = ()
    keywords = ('phone', 'action', 'text', 'phones')

    def build(self):
        self.add_line('e0', (4, 8), (44, 8))
        self.add_line('e1', (4, 24), (35, 24))
        self.add_line('e2', (4, 40), (26, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
