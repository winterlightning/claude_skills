"""Wallet with Cash Bill. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: inspected local Lucide hand, truck, piggy-bank, globe, zap, video and wallet originals and atomic-debug geometry for coherent outlines, shared radii and simplification.

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
    category = 'state'
    tags = ('sub icon',)
    keywords = ('sub icon', 'wallet with cash bill')
    def build(self):
        # Cash bill has a rectangular exposed band; clasp joins open wallet edge.
        self.add_polyline('bill',(14,14),(14,6),(32,6),(32,14))
        self.add_polyline('wallet',(38,24),(38,14),(6,14),(6,42),(38,42),(38,34))
        rounded_rect(self,'clasp',25,24,42,34,4)
        self.relate('connect','wallet','bill')
        self.relate('connect','wallet','clasp')
