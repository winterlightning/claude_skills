"""Monospaced text character (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '819c9468-6d6a-52cb-9fcb-9f7eb1f983ee'
SOURCE_PATH = 'icons-json/interface-essential/monospaced text character_819c9468-6d6a-52cb-9fcb-9f7eb1f983ee.json'
AUTHOR = 'json_to_solo'

class MonospacedTextCharacterInterfaceEssential(Solo48):
    icon_id = 'monospaced-text-character-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('monospaced', 'text', 'character', 'interface-essential')

    def build(self):
        self.add_line('e0', (40, 4), (24, 36))
        self.add_line('e1', (24, 36), (8, 4))
        self.add_line('e2', (8, 44), (8, 4))
        self.add_line('e3', (40, 44), (40, 19))
        self.add_line('e4', (40, 19), (40, 4))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
