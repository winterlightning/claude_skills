"""Not equal (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77032977-e737-57ee-b2f3-b24418921dd8'
SOURCE_PATH = 'pictographic-primitives/interface-essential/not equal_77032977-e737-57ee-b2f3-b24418921dd8.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class NotEqual(Solo48):
    icon_id = 'not-equal'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('not', 'equal', 'interface-essential')

    def build(self):
        self.add_line('e0', (33, 4), (16, 44))
        self.add_line('e1', (40, 19), (8, 19))
        self.add_line('e2', (8, 30), (40, 30))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
