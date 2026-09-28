"""Move bottom left (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6742b6f0-e815-4e2d-8ec1-12df0b549f2c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_27/move bottom left_6742b6f0-e815-4e2d-8ec1-12df0b549f2c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MoveBottomLeft(Solo48):
    icon_id = 'move-bottom-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('move', 'bottom', 'left', '_uncategorized')

    def build(self):
        self.add_line('e0', (6, 6), (6, 42))
        self.add_line('e1', (6, 42), (42, 42))
        self.add_contour('c0', 'e0', 'e1')
