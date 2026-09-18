"""Independent 32px profile of sparkles-star-plus.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a760b4a2-03ae-462b-9aa6-3ee940a9e6bb'
SOURCE_PATH = 'pictographic-primitives/symbol/sparkles_a760b4a2-03ae-462b-9aa6-3ee940a9e6bb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a760b4a2-03ae-462b-9aa6-3ee940a9e6bb', 'pictographic-primitives/symbol/sparkles_a760b4a2-03ae-462b-9aa6-3ee940a9e6bb.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sparkles-star-plus',)
SOLO_SOURCE_ICON_IDS = ('sparkles-star-plus',)
REFERENCE_EXPORT_SHA256 = '15338d1f6470fbe5d19d42ac0230cbfa6a888a37c70f7bb228a5af313a355ed8'

class Drawing(Sub32):
    icon_id = 'sparkles-star-plus-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 7), (13, 15))
        self.add_line('p1-r1-2', (13, 15), (18, 19))
        self.add_line('p1-r1-3', (18, 19), (13, 22))
        self.add_line('p1-r1-4', (13, 22), (10, 30))
        self.add_line('p1-r1-5', (10, 30), (7, 22))
        self.add_line('p1-r1-6', (7, 22), (2, 19))
        self.add_line('p1-r1-7', (2, 19), (7, 15))
        self.add_line('p1-r1-8', (7, 15), (10, 7))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (19, 5), (22, 5))
        self.add_line('p2-r1-2', (22, 5), (25, 5))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (22, 2), (22, 5))
        self.add_line('p3-r1-2', (22, 5), (22, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (24, 22), (27, 22))
        self.add_line('p4-r1-2', (27, 22), (30, 22))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (27, 19), (27, 22))
        self.add_line('p5-r1-2', (27, 22), (27, 25))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-2')
        self.relate('connect', 'p4-r1-2', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p5-r1-2')
