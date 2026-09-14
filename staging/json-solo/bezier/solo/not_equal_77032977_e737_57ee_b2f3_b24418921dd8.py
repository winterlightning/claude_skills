"""Not equal (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77032977-e737-57ee-b2f3-b24418921dd8'
SOURCE_PATH = 'icons-json/interface-essential/not equal_77032977-e737-57ee-b2f3-b24418921dd8.json'
AUTHOR = 'json_to_solo'

class NotEqual77032977(Solo48):
    icon_id = 'not-equal-77032977'
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
