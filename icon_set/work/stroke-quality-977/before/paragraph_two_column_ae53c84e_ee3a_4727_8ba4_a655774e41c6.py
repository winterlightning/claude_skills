"""Paragraph two column (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae53c84e-ee3a-4727-8ba4-a655774e41c6'
SOURCE_PATH = 'pictographic-primitives/interface-essential/paragraph two column_ae53c84e-ee3a-4727-8ba4-a655774e41c6.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ParagraphTwoColumn(Solo48):
    icon_id = 'paragraph-two-column'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('paragraph', 'two', 'column', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (4, 24), (20, 24))
        self.add_line('sym-e1', (29, 24), (44, 24))
        self.add_line('sym-e2', (4, 8), (20, 8))
        self.add_line('sym-e3', (29, 8), (44, 8))
        self.add_line('sym-e4', (4, 40), (20, 40))
        self.add_line('sym-e5', (29, 40), (44, 40))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2')
        self.add_contour('sym-c3', 'sym-e3')
        self.add_contour('sym-c4', 'sym-e4')
        self.add_contour('sym-c5', 'sym-e5')
