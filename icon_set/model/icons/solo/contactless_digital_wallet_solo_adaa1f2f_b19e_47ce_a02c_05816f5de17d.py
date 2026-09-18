"""Contactless Digital Wallet. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'adaa1f2f-b19e-47ce-a02c-05816f5de17d'
SOURCE_PATH = 'pictographic-primitives/other/wallet wifi_adaa1f2f-b19e-47ce-a02c-05816f5de17d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'contactless-digital-wallet-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'contactless digital wallet')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_bezier('signal-outer',(6,12),((16,4),(32,4),(42,12)))
        self.add_bezier('signal-inner',(15,19),((20,15),(28,15),(33,19)))
        rounded_rect(self,'wallet',12,28,36,42,3)
        self.add_polyline('flap',(15,28),(26,34),(26,42))
        self.relate('connect','wallet','flap')
