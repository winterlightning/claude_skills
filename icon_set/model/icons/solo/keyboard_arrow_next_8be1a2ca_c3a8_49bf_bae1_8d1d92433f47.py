"""Keyboard arrow next (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8be1a2ca-c3a8-49bf-bae1-8d1d92433f47'
SOURCE_PATH = 'icons-json/interface-essential/keyboard arrow next_8be1a2ca-c3a8-49bf-bae1-8d1d92433f47.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowNext(Solo48):
    icon_id = 'keyboard-arrow-next'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'next', 'interface-essential')

    def build(self):
        self.add_line('e0', (33, 8), (44, 24))
        self.add_line('e1', (4, 24), (44, 24))
        self.add_line('e2', (33, 40), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
