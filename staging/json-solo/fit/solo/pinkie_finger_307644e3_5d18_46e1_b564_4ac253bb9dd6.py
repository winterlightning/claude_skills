"""Pinkie finger (wayfinding), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '307644e3-5d18-46e1-b564-4ac253bb9dd6'
SOURCE_PATH = 'icons-json/wayfinding/pinkie finger_307644e3-5d18-46e1-b564-4ac253bb9dd6.json'
AUTHOR = 'json_to_solo'

class PinkieFingerWayfinding(Solo48):
    icon_id = 'pinkie-finger-wayfinding'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('pinkie', 'finger', 'wayfinding')

    def build(self):
        self.add_line('e0', (15, 24), (15, 20))
        self.add_line('e1', (8, 22), (8, 32))
        self.add_line('e2', (40, 32), (40, 7))
        self.add_line('e3', (32, 8), (32, 24))
        self.add_line('e4', (22, 15), (23, 17))
        self.add_line('e5', (23, 17), (23, 24))
        self.add_line('e6', (23, 24), (23, 21))
        self.add_line('e7', (30, 14), (32, 17))
        self.add_arc('e8-1', (15, 20), (9, 20), radius_x=5, sweep=False)
        self.add_arc('e8-2', (9, 20), (8, 22), radius_x=3, sweep=False)
        self.add_arc('e9-1', (8, 32), (12, 40), radius_x=12, sweep=False)
        self.add_arc('e9-2', (12, 40), (17, 43), radius_x=15, sweep=False)
        self.add_line('e9-3', (17, 43), (24, 44))
        self.add_line('e9-4', (24, 44), (34, 42))
        self.add_arc('e9-5', (34, 42), (40, 32), radius_x=12, sweep=False)
        self.add_arc('e10-1', (40, 7), (39, 5), radius_x=3, sweep=False)
        self.add_arc('e10-2', (39, 5), (36, 4), radius_x=5, sweep=False)
        self.add_arc('e10-3', (36, 4), (32, 8), radius_x=4, sweep=False)
        self.add_arc('e11', (32, 24), (32, 23), radius_x=24)
        self.add_arc('e12', (15, 20), (22, 15), radius_x=5)
        self.add_arc('e13', (23, 17), (30, 14), radius_x=4)
        self.add_contour('c0', 'e0', 'e8-1', 'e8-2', 'e1', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e9-5', 'e2', 'e10-1', 'e10-2', 'e10-3', 'e3', 'e11')
        self.add_contour('c1', 'e12', 'e4', 'e5', 'e6')
        self.add_contour('c2', 'e13', 'e7')
        self.relate('connect', 'c2', 'c0')
