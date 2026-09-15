"""Keyboard arrow bottom left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b844c7f-1011-5ebf-a235-17cf6f0014b7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/keyboard arrow bottom left_4b844c7f-1011-5ebf-a235-17cf6f0014b7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class KeyboardArrowBottomLeft(Solo48):
    icon_id = 'keyboard-arrow-bottom-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'bottom', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 6), (6, 42))
        self.add_line('e1', (6, 42), (6, 25))
        self.add_line('e2', (6, 42), (23, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
