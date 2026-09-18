"""Wallet with Cash Bill. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '5de9e319-eb7e-4da2-9b54-9c5c4a5f3449'
SOURCE_PATH = 'pictographic-primitives/state/wallet_5de9e319-eb7e-4da2-9b54-9c5c4a5f3449.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wallet-with-cash-bill-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'wallet with cash bill')
    def build(self):
        self.add_polyline('wallet',(37,24),(37,14),(6,14),(6,42),(37,42),(37,34))
        self.add_polyline('bill',(12,14),(29,6),(33,14))
        self.relate('connect','wallet','bill')
        rounded_rect(self,'clasp',25,24,42,34,4)
        self.relate('connect','wallet','clasp')
