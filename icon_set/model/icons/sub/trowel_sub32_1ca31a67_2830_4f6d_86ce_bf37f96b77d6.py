"""Independent 32px profile of trowel.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1ca31a67-2830-4f6d-86ce-bf37f96b77d6'
SOURCE_PATH = 'pictographic-primitives/symbol/trowel_1ca31a67-2830-4f6d-86ce-bf37f96b77d6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1ca31a67-2830-4f6d-86ce-bf37f96b77d6', 'pictographic-primitives/symbol/trowel_1ca31a67-2830-4f6d-86ce-bf37f96b77d6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/trowel',)
SOLO_SOURCE_ICON_IDS = ('trowel',)
REFERENCE_EXPORT_SHA256 = 'd863669de562d3dfc09be218a055b5efe9f591effe1cafd459e12881bf8a3d42'

class Drawing(Sub32):
    icon_id = 'trowel-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (10, 13))
        self.add_line('p1-r1-2', (10, 13), (13, 11))
        self.add_line('p1-r1-3', (13, 11), (18, 14))
        self.add_line('p1-r1-4', (18, 14), (22, 19))
        self.add_line('p1-r1-5', (22, 19), (21, 22))
        self.add_line('p1-r1-6', (21, 22), (5, 30))
        self.add_line('p1-r1-7', (5, 30), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (13, 19), (18, 14))
        self.add_line('p2-r1-2', (18, 14), (18, 11))
        self.add_line('p2-r1-3', (18, 11), (30, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
