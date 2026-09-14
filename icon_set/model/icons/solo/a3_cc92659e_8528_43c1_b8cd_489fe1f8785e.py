"""A3 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc92659e-8528-43c1-b8cd-489fe1f8785e'
SOURCE_PATH = 'icons-json/symbol/A3_cc92659e-8528-43c1-b8cd-489fe1f8785e.json'
AUTHOR = 'json_to_solo'

class A3(Solo48):
    icon_id = 'a3'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('a3', 'symbol')

    def build(self):
        self.add_line('e0', (21, 40), (15, 10))
        self.add_line('e1', (11, 9), (4, 40))
        self.add_line('e2', (7, 29), (19, 29))
        self.add_arc('e3-1', (15, 10), (13, 8), radius_x=2, sweep=False)
        self.add_line('e3-2', (13, 8), (11, 9))
        self.add_arc('e4-1', (31, 13), (34, 9), radius_x=7)
        self.add_line('e4-2', (34, 9), (38, 8))
        self.add_arc('e4-3', (38, 8), (42, 10), radius_x=5)
        self.add_line('e4-4', (42, 10), (44, 16))
        self.add_line('e4-5', (44, 16), (43, 20))
        self.add_arc('e4-6', (43, 20), (37, 24), radius_x=7)
        self.add_arc('e4-7', (37, 24), (42, 26), radius_x=6)
        self.add_line('e4-8', (42, 26), (44, 32))
        self.add_arc('e4-9', (44, 32), (42, 38), radius_x=10)
        self.add_arc('e4-10', (42, 38), (38, 40), radius_x=5)
        self.add_arc('e4-11', (38, 40), (31, 34), radius_x=8)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e4-9', 'e4-10', 'e4-11')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
