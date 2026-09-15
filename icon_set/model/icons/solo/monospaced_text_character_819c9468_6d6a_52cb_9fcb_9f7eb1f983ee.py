"""Monospaced text character (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '819c9468-6d6a-52cb-9fcb-9f7eb1f983ee'
SOURCE_PATH = 'pictographic-primitives/interface-essential/monospaced text character_819c9468-6d6a-52cb-9fcb-9f7eb1f983ee.svg'
AUTHOR = 'gpt-6'

class MonospacedTextCharacter(Solo48):
    icon_id = 'monospaced-text-character'
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
        self.add_line('e3', (40, 44), (40, 4))
        self.add_contour('c0', 'e0', 'e1', closed=False)
        self.add_contour('c1', 'e2', closed=False)
        self.add_contour('c2', 'e3', closed=False)
