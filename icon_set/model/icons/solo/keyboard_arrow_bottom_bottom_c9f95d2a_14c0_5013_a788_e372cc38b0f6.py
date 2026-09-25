"""Keyboard arrow bottom bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9f95d2a-14c0-5013-a788-e372cc38b0f6'
SOURCE_PATH = 'pictographic-primitives/arrows/keyboard arrow bottom bottom_c9f95d2a-14c0-5013-a788-e372cc38b0f6.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class KeyboardArrowBottomBottom(Solo48):
    icon_id = 'keyboard-arrow-bottom-bottom'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('keyboard', 'arrow', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (6, 6), (42, 42))
        self.add_line('e1', (42, 42), (25, 42))
        self.add_line('e2', (42, 42), (42, 25))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
