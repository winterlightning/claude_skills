"""Keyboard arrow bottom right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be80cafb-83a1-5b35-a55c-56b5857864a9'
SOURCE_PATH = 'icons-json/interface-essential/keyboard arrow bottom right_be80cafb-83a1-5b35-a55c-56b5857864a9.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowBottomRight(Solo48):
    icon_id = 'keyboard-arrow-bottom-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'bottom', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 42), (42, 6))
        self.add_line('e1', (42, 6), (42, 23))
        self.add_line('e2', (42, 6), (25, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
