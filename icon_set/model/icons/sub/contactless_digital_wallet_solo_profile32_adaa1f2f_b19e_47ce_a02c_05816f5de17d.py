"""Independent 32px profile of contactless-digital-wallet-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'adaa1f2f-b19e-47ce-a02c-05816f5de17d'
SOURCE_PATH = 'pictographic-primitives/other/wallet wifi_adaa1f2f-b19e-47ce-a02c-05816f5de17d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('adaa1f2f-b19e-47ce-a02c-05816f5de17d', 'pictographic-primitives/other/wallet wifi_adaa1f2f-b19e-47ce-a02c-05816f5de17d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/contactless-digital-wallet-solo',)
SOLO_SOURCE_ICON_IDS = ('contactless-digital-wallet-solo',)
REFERENCE_EXPORT_SHA256 = '71692d2dc6d94ba391143845826aa618d6359c6e0703f34b97aee8ed7169f685'

class Drawing(Sub32):
    icon_id = 'contactless-digital-wallet-solo-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 7), ((6, 4), (11, 2), (16, 2)))
        self.add_bezier('p1-r1-2', (16, 2), ((21, 2), (26, 4), (30, 7)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (9, 12), ((11, 11), (13, 10), (16, 10)))
        self.add_bezier('p2-r1-2', (16, 10), ((19, 10), (21, 11), (23, 12)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (9, 19), (23, 19))
        self.add_arc('p3-r1-2', (23, 19), (25, 21), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (25, 21), (25, 28))
        self.add_arc('p3-r1-4', (25, 28), (23, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-5', (23, 30), (9, 30))
        self.add_arc('p3-r1-6', (9, 30), (7, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-7', (7, 28), (7, 21))
        self.add_arc('p3-r1-8', (7, 21), (9, 19), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', closed=False)
        self.add_line('p4-r1-1', (9, 19), (18, 24))
        self.add_line('p4-r1-2', (18, 24), (18, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-8', 'p4-r1-1')
