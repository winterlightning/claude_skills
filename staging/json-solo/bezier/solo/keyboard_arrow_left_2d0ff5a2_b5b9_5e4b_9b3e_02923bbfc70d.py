"""Keyboard arrow left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d0ff5a2-b5b9-5e4b-9b3e-02923bbfc70d'
SOURCE_PATH = 'icons-json/interface-essential/keyboard arrow left_2d0ff5a2-b5b9-5e4b-9b3e-02923bbfc70d.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowLeft2d0ff5a2(Solo48):
    icon_id = 'keyboard-arrow-left-2d0ff5a2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (13, 8), (4, 24))
        self.add_line('e1', (4, 24), (44, 24))
        self.add_line('e2', (13, 40), (4, 24))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
