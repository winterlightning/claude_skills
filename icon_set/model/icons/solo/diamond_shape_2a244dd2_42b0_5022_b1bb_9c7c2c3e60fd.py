"""Diamond shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a244dd2-42b0-5022-b1bb-9c7c2c3e60fd'
SOURCE_PATH = 'pictographic-primitives/design/diamond shape_2a244dd2-42b0-5022-b1bb-9c7c2c3e60fd.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class DiamondShape(Solo48):
    icon_id = 'diamond-shape'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('diamond', 'shape', 'design')

    def build(self):
        self.add_line('sym-e0', (6, 24), (24, 6))
        self.add_line('sym-e1', (24, 6), (42, 24))
        self.add_line('sym-e2', (42, 24), (24, 42))
        self.add_line('sym-e3', (24, 42), (6, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', closed=True)
