"""Keyboard arrow return (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32978e5f-dd58-5a85-96df-67457d537f63'
SOURCE_PATH = 'icons-json/interface-essential/keyboard arrow return_32978e5f-dd58-5a85-96df-67457d537f63.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowReturnInterfaceEssential(Solo48):
    icon_id = 'keyboard-arrow-return-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'return', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 34), (39, 34))
        self.add_line('e1', (42, 30), (42, 8))
        self.add_line('e2', (40, 6), (24, 6))
        self.add_line('e3', (6, 34), (15, 26))
        self.add_line('e4', (6, 34), (15, 42))
        self.add_line('e5-1', (39, 34), (41, 33))
        self.add_arc('e5-2', (41, 33), (42, 30), radius_x=5, sweep=False)
        self.add_line('e6', (42, 8), (40, 6))
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
