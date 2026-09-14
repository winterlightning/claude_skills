"""Right turn (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '945f460e-d685-422e-a38d-7a5abaf48bef'
SOURCE_PATH = 'icons-json/transportation/right turn_945f460e-d685-422e-a38d-7a5abaf48bef.json'
AUTHOR = 'json_to_solo'

class RightTurn945f460e(Solo48):
    icon_id = 'right-turn-945f460e'
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
