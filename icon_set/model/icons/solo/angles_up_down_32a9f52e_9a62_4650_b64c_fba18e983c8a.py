"""Angles up down (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32a9f52e-9a62-4650-b64c-fba18e983c8a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/angles up down_32a9f52e-9a62-4650-b64c-fba18e983c8a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AnglesUpDown(Solo48):
    icon_id = 'angles-up-down'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('angles', 'up', 'down', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (8, 13), (24, 4))
        self.add_line('e1', (8, 35), (24, 44))
        self.add_line('e2', (40, 35), (24, 44))
        self.add_line('e3', (40, 13), (24, 4))
        self.add_line('e4', (24, 44), (24, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
