"""Lamp (office), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fffde25-08b0-46d2-9123-537377f28274'
SOURCE_PATH = 'icons-json/office/lamp_8fffde25-08b0-46d2-9123-537377f28274.json'
AUTHOR = 'json_to_solo'

class LampOffice(Solo48):
    icon_id = 'lamp-office'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('lamp', 'office')

    def build(self):
        self.add_line('e0', (33, 35), (39, 23))
        self.add_line('e1', (21, 41), (22, 40))
        self.add_line('e2', (38, 42), (22, 42))
        self.add_line('e3', (37, 20), (22, 12))
        self.add_line('e4', (18, 7), (16, 9))
        self.add_line('e5', (16, 9), (8, 9))
        self.add_line('e6', (6, 12), (18, 23))
        self.add_line('e7', (22, 22), (21, 14))
        self.add_arc('e8-top', (38, 21), (42, 21), radius_x=2)
        self.add_arc('e8-bottom', (42, 21), (38, 21), radius_x=2)
        self.add_arc('e9-1', (22, 40), (34, 35), radius_x=10)
        self.add_arc('e9-2', (34, 35), (38, 42), radius_x=5)
        self.add_arc('e10', (22, 42), (21, 41), radius_x=1)
        self.add_arc('e11-1', (8, 9), (6, 10), radius_x=2)
        self.add_line('e11-2', (6, 10), (6, 12))
        self.add_arc('e12', (18, 23), (22, 22), radius_x=3, sweep=False)
        self.add_arc('e13-1', (21, 14), (23, 8), radius_x=7, sweep=False)
        self.add_arc('e13-2', (23, 8), (20, 6), radius_x=4, sweep=False)
        self.add_line('e13-3', (20, 6), (18, 7))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e9-1', 'e9-2', 'e2', 'e10', closed=True)
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e5', 'e11-1', 'e11-2', 'e6', 'e12', 'e7', 'e13-1', 'e13-2', 'e13-3', closed=True)
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c2', 'e8')
        self.relate('connect', 'c2', 'c3')
