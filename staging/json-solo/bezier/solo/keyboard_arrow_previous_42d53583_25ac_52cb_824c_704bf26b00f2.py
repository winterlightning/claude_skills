"""Keyboard arrow previous (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42d53583-25ac-52cb-824c-704bf26b00f2'
SOURCE_PATH = 'icons-json/interface-essential/keyboard arrow previous_42d53583-25ac-52cb-824c-704bf26b00f2.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowPreviousInterfaceEssential(Solo48):
    icon_id = 'keyboard-arrow-previous-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'previous', 'interface-essential')

    def build(self):
        self.add_line('e0', (19, 8), (4, 24))
        self.add_line('e1', (19, 40), (4, 24))
        self.add_line('e2', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
