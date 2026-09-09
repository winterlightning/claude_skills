# Variant of open-locket-with-portrait; parent file remains unchanged.
"""Open locket with intrinsic head-and-shoulders portrait, omitting the separate bail. HRECT_L fits the simplified two-half silhouette. Lucide user-round informs the round head and curved shoulders; overlap is deliberately asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '57afb5e4-7b86-4ac6-adf1-571db810e527'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/locket_57afb5e4-7b86-4ac6-adf1-571db810e527.svg'
AUTHOR = 'gpt-6'

class OpenLocketWithPortraitVariant2(Solo48):
    icon_id = 'open-locket-with-portrait-v2'
    variant_of = 'open-locket-with-portrait'
    variant_label = 'Simpler locket silhouette'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('open', 'locket', 'with', 'portrait')

    def build(self) -> None:
        self.add_arc('front-ne', (31, 10), (46, 25), radius_x=15)
        self.add_arc('front-se', (46, 25), (31, 40), radius_x=15)
        self.add_arc('front-sw-tip', (31, 40), (22, 37), radius_x=15)
        self.add_arc('front-sw', (22, 37), (16, 25), radius_x=15)
        self.add_arc('front-nw', (16, 25), (22, 13), radius_x=15)
        self.add_arc('front-nw-tip', (22, 13), (31, 10), radius_x=15)
        self.add_contour('front', 'front-ne', 'front-se', 'front-sw-tip', 'front-sw', 'front-nw', 'front-nw-tip', closed=True)
        self.add_arc('back-top', (22, 13), (12, 8), radius_x=10, radius_y=5, sweep=False)
        self.add_arc('back-upper', (12, 8), (2, 24), radius_x=10, radius_y=16, sweep=False)
        self.add_arc('back-lower', (2, 24), (12, 40), radius_x=10, radius_y=16, sweep=False)
        self.add_arc('back-bottom', (12, 40), (22, 37), radius_x=10, radius_y=3, sweep=False)
        self.add_contour('back', 'back-top', 'back-upper', 'back-lower', 'back-bottom')
        self.relate('connect', 'front', 'back')
        self.add_dot('portrait-head', (31, 19))
        self.add_arc('portrait-shoulders', (25, 31), (37, 31), radius_x=6, radius_y=5)
