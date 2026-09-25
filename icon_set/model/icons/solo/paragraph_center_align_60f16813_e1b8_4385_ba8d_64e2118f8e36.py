"""Paragraph center align (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '60f16813-e1b8-4385-ba8d-64e2118f8e36'
SOURCE_PATH = 'pictographic-primitives/interface-essential/paragraph center align_60f16813-e1b8-4385-ba8d-64e2118f8e36.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ParagraphCenterAlign(Solo48):
    icon_id = 'paragraph-center-align'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('paragraph', 'center', 'align', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 8), (44, 8))
        self.add_line('e1', (4, 19), (44, 19))
        self.add_line('e2', (4, 29), (44, 29))
        self.add_line('e3', (4, 40), (35, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
