"""Loading bar 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0e10581-e9da-4ad2-86ee-9fb92f7f28f3'
SOURCE_PATH = 'icons-json/interface-essential/loading bar 1_a0e10581-e9da-4ad2-86ee-9fb92f7f28f3.json'
AUTHOR = 'json_to_solo'

class LoadingBar1InterfaceEssential(Solo48):
    icon_id = 'loading-bar-1-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('loading', 'bar', 'interface-essential')

    def build(self):
        self.add_line('e0', (23, 8), (9, 40))
        self.add_line('e1', (39, 8), (25, 40))
        self.add_line('e2', (38, 40), (11, 40))
        self.add_line('e3', (10, 8), (37, 8))
        self.add_line('e4-1', (11, 40), (9, 40))
        self.add_arc('e4-2', (9, 40), (7, 38), radius_x=5)
        self.add_arc('e4-3', (7, 38), (5, 33), radius_x=17)
        self.add_line('e4-4', (5, 33), (4, 26))
        self.add_line('e4-5', (4, 26), (5, 16))
        self.add_arc('e4-6', (5, 16), (10, 8), radius_x=12)
        self.add_line('e5-1', (37, 8), (40, 9))
        self.add_arc('e5-2', (40, 9), (42, 12), radius_x=12)
        self.add_line('e5-3', (42, 12), (44, 23))
        self.add_arc('e5-4', (44, 23), (42, 34), radius_x=32)
        self.add_arc('e5-5', (42, 34), (38, 40), radius_x=8)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e3', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
