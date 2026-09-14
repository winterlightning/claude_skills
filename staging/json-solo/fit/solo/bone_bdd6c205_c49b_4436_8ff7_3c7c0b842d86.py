"""Bone (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdd6c205-c49b-4436-8ff7-3c7c0b842d86'
SOURCE_PATH = 'icons-json/symbol/bone_bdd6c205-c49b-4436-8ff7-3c7c0b842d86.json'
AUTHOR = 'json_to_solo'

class BoneSymbol(Solo48):
    icon_id = 'bone-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bone', 'symbol')

    def build(self):
        self.add_line('sym-e0', (42, 24), (41, 24))
        self.add_line('sym-e1', (41, 24), (43, 26))
        self.add_line('sym-e2', (43, 26), (44, 31))
        self.add_line('sym-e3-1', (44, 31), (42, 38))
        self.add_arc('sym-e3-2', (42, 38), (39, 40), radius_x=4)
        self.add_line('sym-e4', (39, 40), (38, 40))
        self.add_arc('sym-e6', (38, 40), (33, 35), radius_x=7)
        self.add_arc('sym-e7', (33, 35), (32, 31), radius_x=45)
        self.add_line('sym-e8', (32, 31), (16, 31))
        self.add_arc('sym-e9', (16, 31), (15, 35), radius_x=49)
        self.add_arc('sym-e10', (15, 35), (10, 40), radius_x=6)
        self.add_arc('sym-e12', (10, 40), (9, 40), radius_x=22, sweep=False)
        self.add_line('sym-e13-1', (9, 40), (6, 38))
        self.add_arc('sym-e13-2', (6, 38), (4, 32), radius_x=10)
        self.add_line('sym-e15', (4, 32), (4, 31))
        self.add_line('sym-e16', (4, 31), (5, 26))
        self.add_arc('sym-e17', (5, 26), (7, 24), radius_x=34, sweep=False)
        self.add_arc('sym-e20', (7, 24), (5, 22), radius_x=35)
        self.add_line('sym-e21', (5, 22), (4, 17))
        self.add_line('sym-e22', (4, 17), (4, 16))
        self.add_arc('sym-e24-1', (4, 16), (6, 10), radius_x=10)
        self.add_arc('sym-e24-2', (6, 10), (9, 8), radius_x=5)
        self.add_line('sym-e25', (9, 8), (10, 8))
        self.add_arc('sym-e27', (10, 8), (15, 13), radius_x=6)
        self.add_arc('sym-e28', (15, 13), (16, 17), radius_x=49)
        self.add_line('sym-e29', (16, 17), (32, 17))
        self.add_arc('sym-e30', (32, 17), (33, 13), radius_x=45)
        self.add_arc('sym-e31', (33, 13), (38, 8), radius_x=7)
        self.add_line('sym-e33', (38, 8), (39, 8))
        self.add_arc('sym-e34-1', (39, 8), (42, 10), radius_x=5)
        self.add_line('sym-e34-2', (42, 10), (44, 17))
        self.add_line('sym-e35', (44, 17), (43, 22))
        self.add_line('sym-e36', (43, 22), (41, 24))
        self.add_line('sym-e37', (41, 24), (42, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3-1', 'sym-e3-2', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13-1', 'sym-e13-2', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e24-1', 'sym-e24-2', 'sym-e25', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e33', 'sym-e34-1', 'sym-e34-2', 'sym-e35', 'sym-e36', 'sym-e37', closed=True)
