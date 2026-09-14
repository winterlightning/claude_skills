"""View (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a73a3ea1-b1ee-5adb-a13b-215a290d268a'
SOURCE_PATH = 'icons-json/interface-essential/view_a73a3ea1-b1ee-5adb-a13b-215a290d268a.json'
AUTHOR = 'json_to_solo'

class View(Solo48):
    icon_id = 'view'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('view', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (18, 24), (30, 24), radius_x=6, radius_y=9)
        self.add_arc('sym-e1', (30, 24), (18, 24), radius_x=6, radius_y=9)
        self.add_line('sym-e2', (4, 24), (4, 25))
        self.add_line('sym-e3', (4, 25), (5, 25))
        self.add_arc('sym-e4', (5, 25), (9, 31), radius_x=18, sweep=False)
        self.add_arc('sym-e5', (9, 31), (24, 40), radius_x=21, sweep=False)
        self.add_line('sym-e7', (24, 40), (25, 40))
        self.add_arc('sym-e8', (25, 40), (41, 29), radius_x=23, sweep=False)
        self.add_line('sym-e9', (41, 29), (43, 25))
        self.add_line('sym-e10', (43, 25), (44, 24))
        self.add_line('sym-e13', (44, 24), (43, 23))
        self.add_line('sym-e14', (43, 23), (41, 19))
        self.add_arc('sym-e15', (41, 19), (25, 8), radius_x=23, sweep=False)
        self.add_line('sym-e16', (25, 8), (24, 8))
        self.add_arc('sym-e18', (24, 8), (9, 17), radius_x=21, sweep=False)
        self.add_arc('sym-e19', (9, 17), (5, 23), radius_x=18, sweep=False)
        self.add_line('sym-e20', (5, 23), (4, 23))
        self.add_line('sym-e21', (4, 23), (4, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
