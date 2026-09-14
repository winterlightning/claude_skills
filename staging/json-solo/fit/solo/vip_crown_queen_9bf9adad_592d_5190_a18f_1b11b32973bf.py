"""Vip crown queen (rewards), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9bf9adad-592d-5190-a18f-1b11b32973bf'
SOURCE_PATH = 'icons-json/rewards/vip crown queen_9bf9adad-592d-5190-a18f-1b11b32973bf.json'
AUTHOR = 'json_to_solo'

class VipCrownQueenRewards(Solo48):
    icon_id = 'vip-crown-queen-rewards'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    aliases = ()
    keywords = ('vip', 'crown', 'queen', 'rewards')

    def build(self):
        self.add_line('sym-e1', (24, 40), (13, 39))
        self.add_arc('sym-e2', (13, 39), (9, 36), radius_x=6)
        self.add_arc('sym-e3', (9, 36), (8, 34), radius_x=6)
        self.add_line('sym-e4', (8, 34), (4, 20))
        self.add_line('sym-e5', (4, 20), (4, 18))
        self.add_arc('sym-e6', (4, 18), (7, 17), radius_x=2)
        self.add_arc('sym-e7', (7, 17), (15, 21), radius_x=17)
        self.add_line('sym-e8', (15, 21), (19, 13))
        self.add_arc('sym-e9', (19, 13), (24, 8), radius_x=8)
        self.add_arc('sym-e10', (24, 8), (29, 13), radius_x=8)
        self.add_line('sym-e11', (29, 13), (33, 21))
        self.add_arc('sym-e12', (33, 21), (41, 17), radius_x=17)
        self.add_arc('sym-e13', (41, 17), (44, 18), radius_x=2)
        self.add_line('sym-e14-1', (44, 18), (44, 19))
        self.add_arc('sym-e14-2', (44, 19), (44, 20), radius_x=26, sweep=False)
        self.add_line('sym-e15', (44, 20), (40, 34))
        self.add_arc('sym-e16', (40, 34), (39, 36), radius_x=5)
        self.add_arc('sym-e17', (39, 36), (35, 39), radius_x=6)
        self.add_line('sym-e18', (35, 39), (24, 40))
        self.add_arc('sym-e20', (24, 31), (14, 32), radius_x=47, sweep=False)
        self.add_arc('sym-e21', (14, 32), (10, 34), radius_x=9, sweep=False)
        self.add_line('sym-e22', (10, 34), (8, 35))
        self.add_line('sym-e23', (8, 35), (9, 36))
        self.add_arc('sym-e24', (24, 31), (34, 32), radius_x=48, sweep=False)
        self.add_line('sym-e25', (34, 32), (38, 34))
        self.add_line('sym-e26', (38, 34), (40, 35))
        self.add_line('sym-e27', (40, 35), (39, 36))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14-1', 'sym-e14-2', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', closed=True)
        self.add_contour('sym-c1', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
        self.add_contour('sym-c2', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
