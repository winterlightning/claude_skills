"""Move top left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e38072dd-bc40-476d-9b86-95018577e29e'
SOURCE_PATH = 'icons-json/interface-essential/move top left_e38072dd-bc40-476d-9b86-95018577e29e.json'
AUTHOR = 'json_to_solo'

class MoveTopLeftInterfaceEssential(Solo48):
    icon_id = 'move-top-left-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('move', 'top', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (37, 8), (4, 8))
        self.add_line('e1', (4, 8), (4, 39))
        self.add_line('e2', (37, 21), (24, 21))
        self.add_line('e3', (24, 33), (24, 21))
        self.add_line('e4', (44, 40), (26, 23))
        self.add_line('e5', (26, 23), (24, 21))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e5')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
