# Refinement: Open the thumb bend without crowding the right cuff.
# Refinement: Align the gripping edge eight units inside the right cuff.
# Repair: Open the clasp counter between the thumb and upper left knuckles.
"""Two hands clasp between short cuff bars. HRECT_L extremes (6,8)-(42,40). Lucide handshake informs the central hooked thumb and outer grip. Omit tiny individual finger scallops; retain two cuffs and the asymmetric overlapping hands."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '533cf846-1648-4bd0-a7f9-03a05d166f40'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__handshake/20260927T075459Z-thuan-mac-1/reference/handshake_533cf846-1648-4bd0-a7f9-03a05d166f40.svg'
AUTHOR = 'gpt-6'

class Handshake(Solo48):
    icon_id = 'handshake'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('handshake', 'deal', 'agreement', 'partnership', 'business', 'trust', 'greeting', 'cooperation')

    def build(self) -> None:
        # Three lower knuckles restore the clasp silhouette in the source.
        self.add_polyline('hands', (10, 14), (15, 8), (28, 8), (38, 14), (38, 28), (29, 33), (31, 35), (29, 37), (27, 36), (26, 39), (24, 40), (22, 40), (10, 28), (10, 14), closed=True)
        self.add_polyline('cuff-left', (4, 12), (10, 12), (10, 14), (10, 28), (10, 32), (4, 32))
        self.add_polyline('cuff-right', (44, 12), (38, 12), (38, 14), (38, 28), (38, 32), (44, 32))
        self.relate('connect', 'hands', 'cuff-left')
        self.relate('connect', 'hands', 'cuff-right')
        self.add_line('thumb-top', (28, 8), (20, 18))
        self.add_arc('thumb-round', (20, 18), (24, 24), radius_x=5, sweep=False)
        self.add_line('thumb-inner', (24, 24), (29, 23))
        self.add_line('grip', (29, 23), (29, 33))
        self.add_contour('clasp', 'thumb-top', 'thumb-round', 'thumb-inner', 'grip')
        self.relate('connect', 'hands', 'clasp')
