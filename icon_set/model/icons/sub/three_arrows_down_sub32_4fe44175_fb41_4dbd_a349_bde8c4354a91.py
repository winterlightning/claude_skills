"""Independent 32px profile of three-arrows-down.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4fe44175-fb41-4dbd-a349-bde8c4354a91'
SOURCE_PATH = 'pictographic-primitives/state/three arrows down_4fe44175-fb41-4dbd-a349-bde8c4354a91.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4fe44175-fb41-4dbd-a349-bde8c4354a91', 'pictographic-primitives/state/three arrows down_4fe44175-fb41-4dbd-a349-bde8c4354a91.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-arrows-down',)
SOLO_SOURCE_ICON_IDS = ('three-arrows-down',)
REFERENCE_EXPORT_SHA256 = 'a642aaee0d5b7509366d15c650f70e035204ba14d54e5e1cf992233277c23a7c'

class Drawing(Sub32):
    icon_id = 'three-arrows-down-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 15), (16, 30))
        self.add_line('p1-r1-2', (16, 30), (11, 25))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 12), (7, 17))
        self.add_line('p2-r1-2', (7, 17), (11, 12))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (7, 2), (7, 17))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (21, 25), (16, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (30, 12), (25, 17))
        self.add_line('p5-r1-2', (25, 17), (21, 12))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (25, 2), (25, 17))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p1-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p5-r1-1', 'p6-r1-1')
        self.relate("connect", 'p5-r1-2', 'p6-r1-1')
