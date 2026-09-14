"""Keyboard arrow right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e04c22b8-a6e1-4e7c-b9aa-431ee1f46ae2'
SOURCE_PATH = 'icons-json/interface-essential/keyboard arrow right_e04c22b8-a6e1-4e7c-b9aa-431ee1f46ae2.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowRightE04c22b8(Solo48):
    icon_id = 'keyboard-arrow-right-e04c22b8'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (23, 40), (15, 40))
        self.add_line('e1', (12, 18), (44, 18))
        self.add_line('e2', (35, 27), (44, 18))
        self.add_line('e3', (35, 8), (44, 18))
        self.add_arc('e4-1', (15, 40), (4, 28), radius_x=13)
        self.add_line('e4-2', (4, 28), (6, 21))
        self.add_arc('e4-3', (6, 21), (12, 18), radius_x=8)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
