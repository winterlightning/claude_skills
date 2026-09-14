"""Virtual shopping (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14954394-1829-4d67-aae8-913ee0e98be3'
SOURCE_PATH = 'icons-json/shopping/virtual shopping_14954394-1829-4d67-aae8-913ee0e98be3.json'
AUTHOR = 'json_to_solo'

class VirtualShopping(Solo48):
    icon_id = 'virtual-shopping'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('virtual', 'shopping')

    def build(self):
        self.add_line('e0', (17, 20), (17, 16))
        self.add_line('e1', (31, 20), (31, 16))
        self.add_line('e2', (17, 16), (11, 16))
        self.add_line('e3', (11, 16), (8, 42))
        self.add_line('e4', (10, 44), (38, 44))
        self.add_line('e5', (40, 41), (37, 17))
        self.add_line('e6', (36, 16), (31, 16))
        self.add_line('e7', (17, 16), (31, 16))
        self.add_arc('e8', (8, 42), (10, 44), radius_x=2, sweep=False)
        self.add_arc('e9-1', (38, 44), (40, 42), radius_x=2, sweep=False)
        self.add_line('e9-2', (40, 42), (40, 41))
        self.add_line('e10', (37, 17), (36, 16))
        self.add_line('e11-1', (17, 16), (18, 8))
        self.add_arc('e11-2', (18, 8), (24, 4), radius_x=7)
        self.add_arc('e11-3', (24, 4), (30, 8), radius_x=7)
        self.add_line('e11-4', (30, 8), (31, 16))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e8', 'e4', 'e9-1', 'e9-2', 'e5', 'e10', 'e6')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e11-1', 'e11-2', 'e11-3', 'e11-4')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
