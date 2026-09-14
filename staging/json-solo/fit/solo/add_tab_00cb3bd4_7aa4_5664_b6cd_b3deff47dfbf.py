"""Add tab (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00cb3bd4-7aa4-5664-b6cd-b3deff47dfbf'
SOURCE_PATH = 'icons-json/interface-essential/add tab_00cb3bd4-7aa4-5664-b6cd-b3deff47dfbf.json'
AUTHOR = 'json_to_solo'

class AddTabInterfaceEssential(Solo48):
    icon_id = 'add-tab-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('add', 'tab', 'interface-essential')

    def build(self):
        self.add_line('e0', (18, 15), (18, 33))
        self.add_line('e1', (10, 24), (24, 24))
        self.add_line('e2', (28, 40), (8, 40))
        self.add_line('e3', (4, 35), (4, 13))
        self.add_line('e4', (8, 8), (31, 8))
        self.add_line('e5', (35, 10), (42, 20))
        self.add_line('e6', (41, 30), (34, 39))
        self.add_line('e7', (34, 39), (28, 40))
        self.add_line('e8-1', (8, 40), (5, 39))
        self.add_line('e8-2', (5, 39), (4, 37))
        self.add_line('e8-3', (4, 37), (4, 35))
        self.add_line('e9-1', (4, 13), (5, 9))
        self.add_line('e9-2', (5, 9), (7, 8))
        self.add_line('e9-3', (7, 8), (8, 8))
        self.add_line('e10', (31, 8), (35, 10))
        self.add_line('e11-1', (42, 20), (44, 24))
        self.add_arc('e11-2', (44, 24), (41, 30), radius_x=8)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e7', 'e2', 'e8-1', 'e8-2', 'e8-3', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e4', 'e10', 'e5', 'e11-1', 'e11-2', 'e6', closed=True)
