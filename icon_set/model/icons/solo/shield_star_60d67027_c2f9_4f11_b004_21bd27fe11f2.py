"""Shield star (protection), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '60d67027-c2f9-4f11-b004-21bd27fe11f2'
SOURCE_PATH = 'icons-json/protection/shield star_60d67027-c2f9-4f11-b004-21bd27fe11f2.json'
AUTHOR = 'gpt-6'

class ShieldStar(Solo48):
    icon_id = 'shield-star'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'star', 'protection')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('sym-e0', (19, 28), (21, 23))
        self.add_line('sym-e1', (21, 23), (17, 19))
        self.add_line('sym-e2', (17, 19), (22, 19))
        self.add_line('sym-e3', (22, 19), (24, 13))
        self.add_line('sym-e4', (24, 13), (26, 19))
        self.add_line('sym-e5', (26, 19), (31, 19))
        self.add_line('sym-e6', (31, 19), (27, 23))
        self.add_line('sym-e7', (27, 23), (29, 28))
        self.add_line('sym-e8', (29, 28), (24, 26))
        self.add_line('sym-e9', (24, 26), (19, 28))
        self.add_arc('sym-e10', (40, 8), (38, 7), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e11', (38, 7), (32, 5))
        self.add_line('sym-e12', (32, 5), (26, 4))
        self.add_line('sym-e13', (26, 4), (25, 4))
        self.add_arc('sym-e15', (25, 4), (24, 4), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('sym-e16', (24, 4), (23, 4), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('sym-e18', (23, 4), (22, 4))
        self.add_arc('sym-e19', (22, 4), (16, 5), radius_x=25, radius_y=25, large_arc=False, sweep=True)
        self.add_line('sym-e20', (16, 5), (10, 7))
        self.add_arc('sym-e21', (10, 7), (8, 8), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e22', (8, 8), (8, 26))
        self.add_line('sym-e24', (8, 26), (9, 29))
        self.add_arc('sym-e25', (9, 29), (19, 42), radius_x=22, radius_y=22, large_arc=False, sweep=False)
        self.add_line('sym-e26', (19, 42), (24, 44))
        self.add_line('sym-e29', (24, 44), (29, 42))
        self.add_arc('sym-e30', (29, 42), (39, 29), radius_x=21, radius_y=21, large_arc=False, sweep=False)
        self.add_line('sym-e31', (39, 29), (40, 26))
        self.add_line('sym-e33', (40, 26), (40, 8))
        self.add_contour('sym-c0', *('sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9'), closed=True)
        self.add_contour('sym-c1', *('sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e33'), closed=True)
