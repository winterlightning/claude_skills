"""Square root (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9981fb9d-4558-4c15-acfa-90f0340e9617'
SOURCE_PATH = 'icons-json/interface-essential/square root_9981fb9d-4558-4c15-acfa-90f0340e9617.json'
AUTHOR = 'json_to_solo'

class SquareRootInterfaceEssential(Solo48):
    icon_id = 'square-root-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('square', 'root', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 8), (19, 8))
        self.add_line('e1', (19, 8), (9, 40))
        self.add_line('e2', (9, 40), (4, 26))
        self.add_line('e3', (42, 21), (34, 30))
        self.add_line('e4', (26, 21), (34, 30))
        self.add_line('e5', (27, 38), (34, 30))
        self.add_line('e6', (42, 39), (34, 30))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
