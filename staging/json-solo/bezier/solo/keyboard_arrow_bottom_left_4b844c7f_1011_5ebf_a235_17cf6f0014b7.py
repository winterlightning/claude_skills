"""Keyboard arrow bottom left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b844c7f-1011-5ebf-a235-17cf6f0014b7'
SOURCE_PATH = 'icons-json/interface-essential/keyboard arrow bottom left_4b844c7f-1011-5ebf-a235-17cf6f0014b7.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowBottomLeftInterfaceEssential(Solo48):
    icon_id = 'keyboard-arrow-bottom-left-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'bottom', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 6), (6, 42))
        self.add_line('e1', (6, 42), (6, 25))
        self.add_line('e2', (6, 42), (23, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
