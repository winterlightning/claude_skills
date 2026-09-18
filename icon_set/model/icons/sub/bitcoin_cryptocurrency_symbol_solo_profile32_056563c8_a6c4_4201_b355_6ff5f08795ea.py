"""Independent 32px profile of bitcoin-cryptocurrency-symbol-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '056563c8-a6c4-4201-b355-6ff5f08795ea'
SOURCE_PATH = 'pictographic-primitives/other/circle bitcoin_056563c8-a6c4-4201-b355-6ff5f08795ea.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('056563c8-a6c4-4201-b355-6ff5f08795ea', 'pictographic-primitives/other/circle bitcoin_056563c8-a6c4-4201-b355-6ff5f08795ea.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bitcoin-cryptocurrency-symbol-solo',)
SOLO_SOURCE_ICON_IDS = ('bitcoin-cryptocurrency-symbol-solo',)
REFERENCE_EXPORT_SHA256 = '6db0f41abd34096506cbe717f84b6feed6b423dc6a6f03c030b5246b03c11ac7'

class Drawing(Sub32):
    icon_id = 'bitcoin-cryptocurrency-symbol-solo-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (12, 10), (17, 10))
        self.add_arc('p2-r1-2', (17, 10), (17, 16), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (17, 16), (17, 22), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (17, 22), (12, 22))
        self.add_line('p2-r1-5', (12, 22), (12, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (12, 16), (17, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (12, 10), (12, 10))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (12, 22), (12, 22))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (17, 10), (17, 10))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (17, 22), (17, 22))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p6-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p6-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p7-r1-1')
        self.relate("connect", 'p2-r1-4', 'p5-r1-1')
        self.relate("connect", 'p2-r1-4', 'p7-r1-1')
        self.relate("connect", 'p2-r1-5', 'p4-r1-1')
        self.relate("connect", 'p2-r1-5', 'p5-r1-1')
