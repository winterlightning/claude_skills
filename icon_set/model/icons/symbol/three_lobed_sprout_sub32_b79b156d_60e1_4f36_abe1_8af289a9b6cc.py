"""Independent 32px profile of three-lobed-sprout.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b79b156d-60e1-4f36-abe1-8af289a9b6cc'
SOURCE_PATH = 'pictographic-primitives/nature/wheat_b79b156d-60e1-4f36-abe1-8af289a9b6cc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b79b156d-60e1-4f36-abe1-8af289a9b6cc', 'pictographic-primitives/nature/wheat_b79b156d-60e1-4f36-abe1-8af289a9b6cc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-lobed-sprout',)
SOLO_SOURCE_ICON_IDS = ('three-lobed-sprout',)
REFERENCE_EXPORT_SHA256 = '53acc94d294059479f57a469b2b080e85f07ff8cf6efc5470d0e09e454b52dd8'

class Drawing(Sub32):
    icon_id = 'three-lobed-sprout-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'nature'
    categories = ('nature', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 16), (2, 6))
        self.add_line('p1-r1-2', (2, 6), (2, 16))
        self.add_arc('p1-r1-3', (2, 16), (12, 26), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (12, 26), (20, 26))
        self.add_arc('p1-r1-5', (20, 26), (30, 16), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (30, 16), (30, 6))
        self.add_line('p1-r1-7', (30, 6), (20, 16))
        self.add_bezier('p1-r1-8', (20, 16), ((21, 9), (19, 5), (16, 2)))
        self.add_bezier('p1-r1-9', (16, 2), ((13, 5), (11, 9), (12, 16)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=True)
        self.add_line('p2-r1-1', (16, 26), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
