"""Three bars (other), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33ef65ff-2528-4211-8fb6-5f9788166e2b'
SOURCE_PATH = 'pictographic-primitives/other/three bars_33ef65ff-2528-4211-8fb6-5f9788166e2b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ThreeBars(Solo48):
    icon_id = 'three-bars'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'bars', 'other')

    def build(self):
        self.add_line('e0', (6, 42), (6, 6))
        self.add_line('e1', (24, 42), (24, 6))
        self.add_line('e2', (42, 6), (42, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
