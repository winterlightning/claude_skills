"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cd9ddfe2-dfc2-5c87-aa38-d1de45646346'
SOURCE_PATH = 'icons-json/protection/shield_cd9ddfe2-dfc2-5c87-aa38-d1de45646346.json'
AUTHOR = 'gpt-6'

class ShieldCd9ddfe2(Solo48):
    icon_id = 'shield-cd9ddfe2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'protection')

    def build(self):
        self.add_line('sym-e0', (8, 9), (8, 24))
        self.add_arc('sym-e2', (8, 24), (14, 38), radius_x=21, radius_y=21, large_arc=False, sweep=False)
        self.add_line('sym-e3', (14, 38), (18, 41))
        self.add_arc('sym-e4', (18, 41), (24, 44), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('sym-e7', (24, 44), (30, 41), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('sym-e8', (30, 41), (34, 38))
        self.add_arc('sym-e9', (34, 38), (40, 24), radius_x=20, radius_y=20, large_arc=False, sweep=False)
        self.add_line('sym-e10', (40, 24), (40, 9))
        self.add_arc('sym-e12', (40, 9), (40, 8), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('sym-e13', (40, 8), (36, 6))
        self.add_arc('sym-e14', (36, 6), (25, 4), radius_x=38, radius_y=38, large_arc=False, sweep=False)
        self.add_arc('sym-e15', (25, 4), (24, 4), radius_x=75, radius_y=75, large_arc=False, sweep=True)
        self.add_arc('sym-e18', (24, 4), (23, 4), radius_x=69, radius_y=69, large_arc=False, sweep=True)
        self.add_arc('sym-e19', (23, 4), (12, 6), radius_x=38, radius_y=38, large_arc=False, sweep=False)
        self.add_line('sym-e20', (12, 6), (8, 8))
        self.add_line('sym-e21', (8, 8), (8, 9))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
