"""Keyboard arrow previous (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42d53583-25ac-52cb-824c-704bf26b00f2'
SOURCE_PATH = 'pictographic-primitives/interface-essential/keyboard arrow previous_42d53583-25ac-52cb-824c-704bf26b00f2.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class KeyboardArrowPrevious(Solo48):
    icon_id = 'keyboard-arrow-previous'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'previous', 'interface-essential')

    def build(self):
        self.add_line('e0', (19, 8), (4, 24))
        self.add_line('e1', (19, 40), (4, 24))
        self.add_line('e2', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
