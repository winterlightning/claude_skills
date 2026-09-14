"""Keyboard asterisk (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '955c228f-b1a7-592d-89d5-8a1a99fa4d7e'
SOURCE_PATH = 'icons-json/interface-essential/keyboard asterisk_955c228f-b1a7-592d-89d5-8a1a99fa4d7e.json'
AUTHOR = 'json_to_solo'

class KeyboardAsterisk(Solo48):
    icon_id = 'keyboard-asterisk'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'asterisk', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 4), (40, 44))
        self.add_line('e1', (8, 44), (40, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
