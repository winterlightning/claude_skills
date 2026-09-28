"""Italic (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4810359a-a8eb-4793-bc1d-5d80dbc61f7e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_23/italic_4810359a-a8eb-4793-bc1d-5d80dbc61f7e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Italic(Solo48):
    icon_id = 'italic'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('italic', '_uncategorized')

    def build(self):
        self.add_line('e0', (28, 4), (34, 4))
        self.add_line('e1', (8, 44), (14, 44))
        self.add_line('e2', (20, 44), (14, 44))
        self.add_line('e3', (40, 4), (34, 4))
        self.add_line('e4', (34, 4), (14, 44))
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
