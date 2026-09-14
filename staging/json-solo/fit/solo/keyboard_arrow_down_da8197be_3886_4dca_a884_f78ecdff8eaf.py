"""Keyboard arrow down (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da8197be-3886-4dca-a884-f78ecdff8eaf'
SOURCE_PATH = 'icons-json/interface-essential/keyboard arrow down_da8197be-3886-4dca-a884-f78ecdff8eaf.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowDownInterfaceEssential(Solo48):
    icon_id = 'keyboard-arrow-down-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'down', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 4), (24, 44))
        self.add_line('e1', (8, 31), (24, 44))
        self.add_line('e2', (40, 31), (24, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
