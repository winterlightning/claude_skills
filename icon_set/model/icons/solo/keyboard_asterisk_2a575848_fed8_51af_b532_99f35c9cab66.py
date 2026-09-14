"""Keyboard asterisk (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a575848-fed8-51af-b532-99f35c9cab66'
SOURCE_PATH = 'icons-json/interface-essential/keyboard asterisk_2a575848-fed8-51af-b532-99f35c9cab66.json'
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
        self.add_line('e0', (24, 4), (24, 44))
        self.add_line('e1', (8, 14), (40, 34))
        self.add_line('e2', (8, 34), (40, 14))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
