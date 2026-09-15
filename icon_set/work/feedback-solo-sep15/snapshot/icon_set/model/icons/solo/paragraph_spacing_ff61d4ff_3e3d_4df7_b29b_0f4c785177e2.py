"""Paragraph spacing (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff61d4ff-3e3d-4df7-b29b-0f4c785177e2'
SOURCE_PATH = 'pictographic-primitives/interface-essential/paragraph spacing_ff61d4ff-3e3d-4df7-b29b-0f4c785177e2.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ParagraphSpacing(Solo48):
    icon_id = 'paragraph-spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('paragraph', 'spacing', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 10), (10, 6))
        self.add_line('e1', (6, 38), (10, 42))
        self.add_line('e2', (14, 38), (10, 42))
        self.add_line('e3', (14, 10), (10, 6))
        self.add_line('e4', (10, 6), (10, 42))
        self.add_line('e5', (25, 7), (42, 7))
        self.add_line('e6', (25, 16), (42, 16))
        self.add_line('e7', (25, 25), (42, 25))
        self.add_line('e8', (25, 33), (42, 33))
        self.add_line('e9', (25, 42), (42, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.add_contour('c9', 'e9')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
