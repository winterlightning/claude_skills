"""Layout 16 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7517780d-21e9-4a66-bbc8-b5debc9349f7'
SOURCE_PATH = 'icons-json/interface-essential/layout 16_7517780d-21e9-4a66-bbc8-b5debc9349f7.json'
AUTHOR = 'json_to_solo'

class Layout16InterfaceEssential(Solo48):
    icon_id = 'layout-16-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 16), (31, 42))
        self.add_line('e1', (31, 16), (42, 16))
        self.add_line('e2', (31, 16), (6, 16))
        self.add_line('e3', (42, 16), (42, 40))
        self.add_line('e4', (40, 42), (31, 42))
        self.add_line('e5', (42, 16), (42, 8))
        self.add_line('e6', (40, 6), (8, 6))
        self.add_line('e7', (6, 8), (6, 16))
        self.add_line('e8', (31, 42), (8, 42))
        self.add_line('e9', (6, 40), (6, 16))
        self.add_line('e10', (42, 40), (40, 42))
        self.add_line('e11', (42, 8), (40, 6))
        self.add_line('e12', (8, 6), (6, 8))
        self.add_arc('e13', (8, 42), (6, 40), radius_x=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e10', 'e4')
        self.add_contour('c4', 'e5', 'e11', 'e6', 'e12', 'e7')
        self.add_contour('c5', 'e8', 'e13', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
