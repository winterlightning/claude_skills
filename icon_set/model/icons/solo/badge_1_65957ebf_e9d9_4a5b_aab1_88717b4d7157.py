"""Badge 1 (other), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65957ebf-e9d9-4a5b-aab1-88717b4d7157'
SOURCE_PATH = 'icons-json/other/badge 1_65957ebf-e9d9-4a5b-aab1-88717b4d7157.json'
AUTHOR = 'json_to_solo'

class Badge1(Solo48):
    icon_id = 'badge-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('badge', 'other')

    def build(self):
        self.add_line('sym-e1', (40, 24), (41, 26))
        self.add_line('sym-e2', (41, 26), (42, 29))
        self.add_line('sym-e5', (42, 29), (41, 33))
        self.add_arc('sym-e6', (41, 33), (31, 36), radius_x=8)
        self.add_arc('sym-e7', (31, 36), (24, 42), radius_x=8)
        self.add_line('sym-e9', (24, 42), (23, 42))
        self.add_arc('sym-e10', (23, 42), (17, 37), radius_x=7)
        self.add_line('sym-e11', (17, 37), (13, 37))
        self.add_arc('sym-e12', (13, 37), (6, 30), radius_x=8)
        self.add_line('sym-e13', (6, 30), (6, 29))
        self.add_line('sym-e15', (6, 29), (7, 25))
        self.add_arc('sym-e16', (7, 25), (8, 24), radius_x=18)
        self.add_arc('sym-e17', (8, 24), (7, 23), radius_x=19)
        self.add_line('sym-e18', (7, 23), (6, 19))
        self.add_line('sym-e20', (6, 19), (6, 18))
        self.add_arc('sym-e21', (6, 18), (13, 11), radius_x=9)
        self.add_line('sym-e22', (13, 11), (17, 11))
        self.add_arc('sym-e23', (17, 11), (23, 6), radius_x=7)
        self.add_line('sym-e24', (23, 6), (24, 6))
        self.add_arc('sym-e26', (24, 6), (31, 12), radius_x=8)
        self.add_arc('sym-e27', (31, 12), (41, 15), radius_x=8)
        self.add_line('sym-e28', (41, 15), (42, 19))
        self.add_line('sym-e31', (42, 19), (41, 22))
        self.add_line('sym-e32', (41, 22), (40, 24))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e31', 'sym-e32', closed=True)
