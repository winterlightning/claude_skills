"""Keyboard arrow left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e1067c8-00df-510b-aad0-0a8a854e4b8c'
SOURCE_PATH = 'icons-json/interface-essential/keyboard arrow left_8e1067c8-00df-510b-aad0-0a8a854e4b8c.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowLeft8e1067c8(Solo48):
    icon_id = 'keyboard-arrow-left-8e1067c8'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 30), (13, 21))
        self.add_line('e1', (13, 40), (4, 31))
        self.add_line('e2', (4, 31), (34, 31))
        self.add_line('e3', (33, 8), (25, 8))
        self.add_arc('e4-1', (34, 31), (44, 21), radius_x=10, sweep=False)
        self.add_line('e4-2', (44, 21), (42, 14))
        self.add_arc('e4-3', (42, 14), (33, 8), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e3')
