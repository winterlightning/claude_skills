"""Independent 32px profile of key-and-padlock.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1ac8d6ec-d8d0-4f95-a290-6b9afd057567'
SOURCE_PATH = 'pictographic-primitives/symbol/key and lock_1ac8d6ec-d8d0-4f95-a290-6b9afd057567.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1ac8d6ec-d8d0-4f95-a290-6b9afd057567', 'pictographic-primitives/symbol/key and lock_1ac8d6ec-d8d0-4f95-a290-6b9afd057567.svg'),)
PROFILE_SOURCE_KEYS = ('solo/key-and-padlock',)
SOLO_SOURCE_ICON_IDS = ('key-and-padlock',)
REFERENCE_EXPORT_SHA256 = 'fcb55f1eb5f066d9980d2d1cf487222db905048e86e1a0fb5a143fa9afd13578'

class Drawing(Sub32):
    icon_id = 'key-and-padlock-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 24), (5, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (5, 30), (5, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (5, 24), (5, 11))
        self.add_line('p2-r1-2', (5, 11), (5, 5))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 5), (5, 5))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 11), (5, 11))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (18, 14), (28, 14))
        self.add_bezier('p5-r1-2', (28, 14), ((28, 14), (29, 15), (29, 15)))
        self.add_bezier('p5-r1-3', (29, 15), ((30, 16), (30, 16), (30, 17)))
        self.add_line('p5-r1-4', (30, 17), (30, 28))
        self.add_arc('p5-r1-5', (30, 28), (28, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p5-r1-6', (28, 30), (18, 30))
        self.add_arc('p5-r1-7', (18, 30), (16, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p5-r1-8', (16, 28), (16, 17))
        self.add_arc('p5-r1-9', (16, 17), (18, 14), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', 'p5-r1-6', 'p5-r1-7', 'p5-r1-8', 'p5-r1-9', closed=False)
        self.add_line('p6-r1-1', (18, 14), (18, 7))
        self.add_arc('p6-r1-2', (18, 7), (28, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p6-r1-3', (28, 7), (28, 14))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', closed=False)
        self.add_line('p7-r1-1', (23, 21), (23, 23))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-3')
        self.relate('connect', 'p5-r1-2', 'p6-r1-3')
        self.relate('connect', 'p5-r1-9', 'p6-r1-1')
