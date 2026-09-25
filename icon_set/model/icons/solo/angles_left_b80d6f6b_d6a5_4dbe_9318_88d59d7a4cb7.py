"""Angles left (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b80d6f6b-d6a5-4dbe-9318-88d59d7a4cb7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/angles left_b80d6f6b-d6a5-4dbe-9318-88d59d7a4cb7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AnglesLeft(Solo48):
    icon_id = 'angles-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('angles', 'left', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (21, 8), (4, 24))
        self.add_line('e1', (21, 40), (4, 24))
        self.add_line('e2', (44, 24), (4, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
