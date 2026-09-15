"""Keyboard arrow top left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3607e005-537c-5778-af7a-c288014fa6b0'
SOURCE_PATH = 'pictographic-primitives/interface-essential/keyboard arrow top left_3607e005-537c-5778-af7a-c288014fa6b0.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class KeyboardArrowTopLeft(Solo48):
    icon_id = 'keyboard-arrow-top-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'top', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 6), (22, 6))
        self.add_line('e1', (6, 22), (6, 6))
        self.add_line('e2', (6, 6), (42, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
