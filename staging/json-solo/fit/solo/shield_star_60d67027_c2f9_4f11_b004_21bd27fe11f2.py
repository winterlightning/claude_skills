"""Shield star (protection), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '60d67027-c2f9-4f11-b004-21bd27fe11f2'
SOURCE_PATH = 'icons-json/protection/shield star_60d67027-c2f9-4f11-b004-21bd27fe11f2.json'
AUTHOR = 'json_to_solo'

class ShieldStarProtection(Solo48):
    icon_id = 'shield-star-protection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'star', 'protection')

    def build(self):
        self.add_line('sym-e0', (18, 30), (20, 24))
        self.add_line('sym-e1', (20, 24), (15, 19))
        self.add_line('sym-e2', (15, 19), (21, 19))
        self.add_line('sym-e3', (21, 19), (24, 11))
        self.add_line('sym-e4', (24, 11), (27, 19))
        self.add_line('sym-e5', (27, 19), (33, 19))
        self.add_line('sym-e6', (33, 19), (28, 24))
        self.add_line('sym-e7', (28, 24), (30, 30))
        self.add_line('sym-e8', (30, 30), (24, 27))
        self.add_line('sym-e9', (24, 27), (18, 30))
        self.add_arc('sym-e10', (40, 8), (38, 7), radius_x=4, sweep=False)
        self.add_line('sym-e11', (38, 7), (32, 5))
        self.add_line('sym-e12', (32, 5), (26, 4))
        self.add_line('sym-e13', (26, 4), (25, 4))
        self.add_arc('sym-e15', (25, 4), (24, 4), radius_x=1)
        self.add_arc('sym-e16', (24, 4), (23, 4), radius_x=1)
        self.add_line('sym-e18', (23, 4), (22, 4))
        self.add_arc('sym-e19', (22, 4), (16, 5), radius_x=25)
        self.add_line('sym-e20', (16, 5), (10, 7))
        self.add_arc('sym-e21', (10, 7), (8, 8), radius_x=4, sweep=False)
        self.add_line('sym-e22', (8, 8), (8, 26))
        self.add_line('sym-e24', (8, 26), (9, 29))
        self.add_arc('sym-e25', (9, 29), (19, 42), radius_x=22, sweep=False)
        self.add_line('sym-e26', (19, 42), (24, 44))
        self.add_line('sym-e29', (24, 44), (29, 42))
        self.add_arc('sym-e30', (29, 42), (39, 29), radius_x=21, sweep=False)
        self.add_line('sym-e31', (39, 29), (40, 26))
        self.add_line('sym-e33', (40, 26), (40, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e33', closed=True)
