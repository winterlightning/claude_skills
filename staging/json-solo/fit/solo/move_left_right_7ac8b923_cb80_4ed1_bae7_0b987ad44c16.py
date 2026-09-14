"""Move left right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ac8b923-cb80-4ed1-bae7-0b987ad44c16'
SOURCE_PATH = 'icons-json/interface-essential/move left right_7ac8b923-cb80-4ed1-bae7-0b987ad44c16.json'
AUTHOR = 'json_to_solo'

class MoveLeftRightInterfaceEssential(Solo48):
    icon_id = 'move-left-right-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('move', 'left', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (15, 6), (6, 15))
        self.add_line('e1', (15, 24), (6, 15))
        self.add_line('e2', (34, 15), (6, 15))
        self.add_line('e3', (35, 26), (42, 34))
        self.add_line('e4', (16, 34), (42, 34))
        self.add_line('e5', (35, 42), (42, 34))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
