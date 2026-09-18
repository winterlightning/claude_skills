"""Independent 32px profile of wallet-with-cash-bill-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5de9e319-eb7e-4da2-9b54-9c5c4a5f3449'
SOURCE_PATH = 'pictographic-primitives/state/wallet_5de9e319-eb7e-4da2-9b54-9c5c4a5f3449.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5de9e319-eb7e-4da2-9b54-9c5c4a5f3449', 'pictographic-primitives/state/wallet_5de9e319-eb7e-4da2-9b54-9c5c4a5f3449.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wallet-with-cash-bill-solo',)
SOLO_SOURCE_ICON_IDS = ('wallet-with-cash-bill-solo',)
REFERENCE_EXPORT_SHA256 = '8039d2f55f827a1ceedd38c4f74323eb316677fdc305c3fb9d1e3722c90cf3eb'

class Drawing(Sub32):
    icon_id = 'wallet-with-cash-bill-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 8), (8, 2))
        self.add_line('p1-r1-2', (8, 2), (22, 2))
        self.add_line('p1-r1-3', (22, 2), (22, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (27, 16), (27, 8))
        self.add_line('p2-r1-2', (27, 8), (2, 8))
        self.add_line('p2-r1-3', (2, 8), (2, 30))
        self.add_line('p2-r1-4', (2, 30), (27, 30))
        self.add_line('p2-r1-5', (27, 30), (27, 24))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (20, 16), (27, 16))
        self.add_arc('p3-r1-2', (27, 16), (30, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (30, 19), (30, 21))
        self.add_arc('p3-r1-4', (30, 21), (27, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-5', (27, 24), (20, 24))
        self.add_arc('p3-r1-6', (20, 24), (17, 21), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-7', (17, 21), (17, 19))
        self.add_arc('p3-r1-8', (17, 19), (20, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-5', 'p3-r1-4')
        self.relate("connect", 'p2-r1-5', 'p3-r1-5')
