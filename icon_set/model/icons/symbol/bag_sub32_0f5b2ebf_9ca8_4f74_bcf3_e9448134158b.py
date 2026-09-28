"""Independent 32px profile of bag.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0f5b2ebf-9ca8-4f74-bcf3-e9448134158b'
SOURCE_PATH = 'pictographic-primitives/photography/bag_0f5b2ebf-9ca8-4f74-bcf3-e9448134158b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0f5b2ebf-9ca8-4f74-bcf3-e9448134158b', 'pictographic-primitives/photography/bag_0f5b2ebf-9ca8-4f74-bcf3-e9448134158b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bag',)
SOLO_SOURCE_ICON_IDS = ('bag',)
REFERENCE_EXPORT_SHA256 = '67a89b4777630e93f311de085ca8addb3edbae925d1d95d9bc1ef8ec2359800c'

class Drawing(Sub32):
    icon_id = 'bag-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'photography'
    categories = ('photography', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 11), (10, 8))
        self.add_arc('p1-r1-2', (10, 8), (22, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (22, 8), (22, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (5, 11), (10, 11))
        self.add_line('p2-r1-2', (10, 11), (22, 11))
        self.add_line('p2-r1-3', (22, 11), (27, 11))
        self.add_bezier('p2-r1-4', (27, 11), ((28, 14), (30, 18), (30, 21)))
        self.add_bezier('p2-r1-5', (30, 21), ((30, 28), (27, 30), (21, 30)))
        self.add_line('p2-r1-6', (21, 30), (11, 30))
        self.add_bezier('p2-r1-7', (11, 30), ((5, 30), (2, 28), (2, 21)))
        self.add_bezier('p2-r1-8', (2, 21), ((2, 18), (4, 14), (5, 11)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
