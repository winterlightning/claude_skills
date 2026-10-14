"""Independent 32px profile of rings-linked-three.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a477d769-3338-4583-96a9-f8e4123574e0'
SOURCE_PATH = 'pictographic-primitives/symbol/ripple_a477d769-3338-4583-96a9-f8e4123574e0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a477d769-3338-4583-96a9-f8e4123574e0', 'pictographic-primitives/symbol/ripple_a477d769-3338-4583-96a9-f8e4123574e0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rings-linked-three',)
SOLO_SOURCE_ICON_IDS = ('rings-linked-three',)
REFERENCE_EXPORT_SHA256 = '81a6d500c74eddd6a22822a94e87ffc3078f29e665036d18dfd3441851582762'

class Drawing(Sub32):
    icon_id = 'rings-linked-three-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (12, 16), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (12, 16), (2, 16), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=True)
        self.add_arc('p2-r1-1', (20, 7), (30, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (30, 7), (20, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=True)
        self.add_arc('p3-r1-1', (20, 25), (30, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (30, 25), (20, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=True)
        self.add_line('p4-r1-1', (12, 16), (15, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (15, 16), (22, 11))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (15, 16), (22, 21))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
        self.relate('connect', 'path-5-1', 'path-2-1')
        self.relate('connect', 'path-6-1', 'path-3-1')
        self.relate('connect', 'path-4-1', 'path-1-1')
