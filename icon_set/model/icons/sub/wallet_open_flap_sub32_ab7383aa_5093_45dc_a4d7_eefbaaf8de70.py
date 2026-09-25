"""Independent 32px profile of wallet-open-flap.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ab7383aa-5093-45dc-a4d7-eefbaaf8de70'
SOURCE_PATH = 'pictographic-primitives/symbol/wallet_ab7383aa-5093-45dc-a4d7-eefbaaf8de70.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ab7383aa-5093-45dc-a4d7-eefbaaf8de70', 'pictographic-primitives/symbol/wallet_ab7383aa-5093-45dc-a4d7-eefbaaf8de70.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wallet-open-flap',)
SOLO_SOURCE_ICON_IDS = ('wallet-open-flap',)
REFERENCE_EXPORT_SHA256 = '2f0d3eb114a1cb78a8828830d6bf78a333a92607e1d7eaa61c7dd9f544c757fe'

class Drawing(Sub32):
    icon_id = 'wallet-open-flap-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 2), (25, 2))
        self.add_arc('p1-r1-2', (25, 2), (30, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 7), (30, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (7, 2), (19, 11))
        self.add_arc('p2-r1-2', (19, 11), (21, 14), radius_x=2, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (21, 14), (21, 25))
        self.add_arc('p2-r1-4', (21, 25), (16, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (16, 30), (5, 22))
        self.add_arc('p2-r1-6', (5, 22), (2, 16), radius_x=3, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-7', (2, 16), (2, 7))
        self.add_arc('p2-r1-8', (2, 7), (7, 2), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-8')
