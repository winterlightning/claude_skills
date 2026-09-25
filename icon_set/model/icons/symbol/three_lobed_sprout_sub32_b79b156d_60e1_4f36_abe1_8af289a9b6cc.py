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
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'nature'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 12), (12, 16), radius_x=11, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (12, 16), (16, 2), radius_x=21, radius_y=21, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 2), (20, 16), radius_x=21, radius_y=21, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (20, 16), (27, 12), radius_x=11, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (27, 12), (16, 24), radius_x=11, radius_y=13, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (16, 24), (5, 12), radius_x=11, radius_y=13, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 24), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
