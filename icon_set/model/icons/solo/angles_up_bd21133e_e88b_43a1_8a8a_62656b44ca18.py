"""Angles up (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd21133e-e88b-43a1-8a8a-62656b44ca18'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/angles up_bd21133e-e88b-43a1-8a8a-62656b44ca18.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AnglesUp(Solo48):
    icon_id = 'angles-up'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('angles', 'up', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (8, 19), (24, 4))
        self.add_line('e1', (24, 44), (24, 4))
        self.add_line('e2', (40, 19), (24, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
