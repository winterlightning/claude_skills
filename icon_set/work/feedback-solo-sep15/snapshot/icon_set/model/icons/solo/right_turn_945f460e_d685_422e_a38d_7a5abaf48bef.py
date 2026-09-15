"""Right turn (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '945f460e-d685-422e-a38d-7a5abaf48bef'
SOURCE_PATH = 'pictographic-primitives/transportation/right turn_945f460e-d685-422e-a38d-7a5abaf48bef.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class RightTurnTransportation(Solo48):
    icon_id = 'right-turn-transportation'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('right', 'turn', 'transportation')

    def build(self):
        self.add_line('e0', (8, 44), (8, 9))
        self.add_line('e1', (8, 9), (40, 9))
        self.add_line('e2', (35, 4), (40, 9))
        self.add_line('e3', (35, 13), (40, 9))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
