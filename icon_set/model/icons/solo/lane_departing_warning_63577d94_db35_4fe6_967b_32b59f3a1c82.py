"""Lane departing warning (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63577d94-db35-4fe6-967b-32b59f3a1c82'
SOURCE_PATH = 'pictographic-primitives/transportation/lane departing warning_63577d94-db35-4fe6-967b-32b59f3a1c82.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class LaneDepartingWarning(Solo48):
    icon_id = 'lane-departing-warning'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('lane', 'departing', 'warning', 'transportation')

    def build(self):
        self.add_line('e0', (6, 42), (16, 6))
        self.add_line('e1', (32, 6), (42, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
