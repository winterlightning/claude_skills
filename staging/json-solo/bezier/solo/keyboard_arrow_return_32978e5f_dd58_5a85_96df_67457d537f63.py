"""Keyboard arrow return (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e5', (39, 34), ((40.988, 34), (41.992, 32.141), (41.992, 30.259)), ((41.992, 30.079), (42, 30.18), (42, 30)))
        self.add_bezier('e6', (42, 8), ((41.992, 7.918), (41.992, 8.291), (41.984, 8.209)), ((41.984, 6.941), (41.211, 6), (40, 6)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
