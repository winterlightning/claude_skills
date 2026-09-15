# Repair: Broaden the front thumb while retaining the two overlapping palms.
"""Two overlapping raised hands, front palm dominant; simplify fingers and omit detached motion ticks.
Live centerline extremes: SQUARE (6,6)-(42,42); HRECT_L (4,8)-(44,40);
VRECT_L (8,4)-(40,44). Lucide hand informs construction, source sets subject.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '022ed6ca-1bba-4414-9cf4-8d828d81df26'
SOURCE_PATH = 'pictographic-primitives/rewards/reward claps hand_022ed6ca-1bba-4414-9cf4-8d828d81df26.svg'
AUTHOR = 'gpt-6'

class ClappingHands(Solo48):
    icon_id = 'overlapping-clapping-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/award'
    aliases = ()
    keywords = ('reward', 'celebration', 'clapping-hands')

    def build(self) -> None:
        self.add_line('thumb-1', (16, 42), (6, 30))
        self.add_line('thumb-2', (6, 30), (6, 18))
        self.add_line('thumb-3', (6, 18), (14, 24))
        self.add_line('thumb-4', (14, 24), (14, 10))
        self.add_arc('finger-left', (14, 10), (22, 10), radius_x=4)
        self.add_arc('finger-right', (22, 10), (30, 10), radius_x=4)
        self.add_line('side', (30, 10), (30, 28))
        self.add_arc('palm', (30, 28), (16, 42), radius_x=14)
        self.add_contour('front', 'thumb-1', 'thumb-2', 'thumb-3', 'thumb-4', 'finger-left', 'finger-right', 'side', 'palm', closed=True)
        self.add_line('finger-seam', (22, 10), (22, 22))
        self.relate('connect', 'front', 'finger-seam')
        self.add_arc('rear-finger', (30, 10), (38, 10), radius_x=4)
        self.add_polyline('rear', (38, 10), (42, 18), (42, 28), (34, 38))
        self.relate('connect', 'rear-finger', 'rear')
        self.relate('connect', 'rear-finger', 'front')
