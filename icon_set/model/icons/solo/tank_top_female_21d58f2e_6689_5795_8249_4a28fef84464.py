"""Tank top female (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21d58f2e-6689-5795-8249-4a28fef84464'
SOURCE_PATH = 'icons-json/clothes/tank top female_21d58f2e-6689-5795-8249-4a28fef84464.json'
AUTHOR = 'json_to_solo'

class TankTopFemale(Solo48):
    icon_id = 'tank-top-female'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('tank', 'top', 'female', 'clothes')

    def build(self):
        self.add_line('e0', (32, 4), (34, 4))
        self.add_line('e1', (40, 18), (38, 29))
        self.add_line('e2', (38, 33), (39, 39))
        self.add_line('e3', (27, 44), (22, 44))
        self.add_line('e4', (8, 41), (9, 36))
        self.add_line('e5', (10, 25), (8, 18))
        self.add_line('e6', (13, 11), (14, 4))
        self.add_line('e7', (14, 4), (16, 4))
        self.add_arc('e8', (24, 19), (32, 4), radius_x=23, sweep=False)
        self.add_arc('e9', (34, 4), (40, 18), radius_x=18, sweep=False)
        self.add_line('e10', (38, 29), (38, 33))
        self.add_line('e11-1', (39, 39), (40, 42))
        self.add_line('e11-2', (40, 42), (27, 44))
        self.add_arc('e12', (22, 44), (8, 41), radius_x=38)
        self.add_arc('e13', (9, 36), (10, 25), radius_x=20, sweep=False)
        self.add_arc('e14', (8, 18), (13, 11), radius_x=12, sweep=False)
        self.add_arc('e15', (16, 4), (24, 19), radius_x=22, sweep=False)
        self.add_contour('c0', 'e8', 'e0', 'e9', 'e1', 'e10', 'e2', 'e11-1', 'e11-2', 'e3', 'e12', 'e4', 'e13', 'e5', 'e14', 'e6', 'e7', 'e15')
