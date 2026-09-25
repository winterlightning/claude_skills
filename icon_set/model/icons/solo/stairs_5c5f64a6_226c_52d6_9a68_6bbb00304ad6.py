"""Stairs (furnitures), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c5f64a6-226c-52d6-9a68-6bbb00304ad6'
SOURCE_PATH = 'pictographic-primitives/furnitures/stairs_5c5f64a6-226c-52d6-9a68-6bbb00304ad6.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Stairs(Solo48):
    icon_id = 'stairs'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('stairs', 'furnitures')

    def build(self):
        self.add_line('e0', (44, 8), (32, 8))
        self.add_line('e1', (32, 8), (32, 19))
        self.add_line('e2', (32, 19), (20, 19))
        self.add_line('e3', (20, 19), (20, 30))
        self.add_line('e4', (20, 30), (8, 30))
        self.add_line('e5', (8, 30), (8, 40))
        self.add_line('e6', (8, 40), (4, 40))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6')
