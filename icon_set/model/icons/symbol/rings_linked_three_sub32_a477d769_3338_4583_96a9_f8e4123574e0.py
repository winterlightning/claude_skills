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
        self.add_bezier('p1-r1-1', (2, 16), ((2, 14), (4, 12), (6, 12)))
        self.add_bezier('p1-r1-2', (6, 12), ((8, 12), (10, 14), (10, 16)))
        self.add_bezier('p1-r1-3', (10, 16), ((10, 18), (8, 20), (6, 20)))
        self.add_bezier('p1-r1-4', (6, 20), ((4, 20), (2, 18), (2, 16)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (24, 9), ((23, 8), (22, 7), (22, 6)))
        self.add_bezier('p2-r1-2', (22, 6), ((22, 5), (22, 4), (23, 4)))
        self.add_bezier('p2-r1-3', (23, 4), ((24, 3), (25, 2), (26, 2)))
        self.add_bezier('p2-r1-4', (26, 2), ((27, 2), (28, 2), (28, 3)))
        self.add_bezier('p2-r1-5', (28, 3), ((29, 4), (30, 5), (30, 6)))
        self.add_bezier('p2-r1-6', (30, 6), ((30, 7), (30, 8), (29, 8)))
        self.add_bezier('p2-r1-7', (29, 8), ((28, 9), (27, 10), (26, 10)))
        self.add_bezier('p2-r1-8', (26, 10), ((25, 10), (24, 10), (24, 9)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.add_bezier('p3-r1-1', (24, 23), ((24, 22), (25, 22), (26, 22)))
        self.add_bezier('p3-r1-2', (26, 22), ((27, 22), (28, 23), (29, 24)))
        self.add_bezier('p3-r1-3', (29, 24), ((30, 24), (30, 25), (30, 26)))
        self.add_bezier('p3-r1-4', (30, 26), ((30, 27), (29, 28), (28, 29)))
        self.add_bezier('p3-r1-5', (28, 29), ((28, 30), (27, 30), (26, 30)))
        self.add_bezier('p3-r1-6', (26, 30), ((25, 30), (24, 29), (23, 28)))
        self.add_bezier('p3-r1-7', (23, 28), ((22, 28), (22, 27), (22, 26)))
        self.add_bezier('p3-r1-8', (22, 26), ((22, 25), (23, 24), (24, 23)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', closed=False)
        self.add_line('p4-r1-1', (10, 16), (16, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (16, 16), (24, 9))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (16, 16), (24, 23))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-3', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-8', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p6-r1-1')
        self.relate('connect', 'p3-r1-8', 'p6-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
