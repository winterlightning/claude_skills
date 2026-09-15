"""Align left (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5638c5a1-e0b4-4dc2-a48d-471b5f1a3a00'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/align left_5638c5a1-e0b4-4dc2-a48d-471b5f1a3a00.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AlignLeft(Solo48):
    icon_id = 'align-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('align', 'left', '_uncategorized_01')

    def build(self):
        self.add_line('e0', (6, 6), (42, 6))
        self.add_line('e1', (6, 15), (33, 15))
        self.add_line('e2', (6, 24), (28, 24))
        self.add_line('e3', (6, 33), (23, 33))
        self.add_line('e4', (6, 42), (19, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
