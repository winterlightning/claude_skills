"""Independent 32px profile of three-way-text-sign.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '641fe73b-5492-4567-a942-75d036a0fce7'
SOURCE_PATH = 'pictographic-primitives/transportation/3 way_641fe73b-5492-4567-a942-75d036a0fce7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('641fe73b-5492-4567-a942-75d036a0fce7', 'pictographic-primitives/transportation/3 way_641fe73b-5492-4567-a942-75d036a0fce7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-way-text-sign',)
SOLO_SOURCE_ICON_IDS = ('three-way-text-sign',)
REFERENCE_EXPORT_SHA256 = '03bb15dba8912ed6bb7f5e76314f341d5bfbc113ec3d683cfad858721f26d787'

class Drawing(Sub32):
    icon_id = 'three-way-text-sign-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (11, 2))
        self.add_line('p1-r1-2', (11, 2), (11, 8))
        self.add_line('p1-r1-3', (11, 8), (11, 14))
        self.add_line('p1-r1-4', (11, 14), (2, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (5, 8), (11, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (18, 2), (18, 14))
        self.add_line('p3-r1-2', (18, 14), (24, 8))
        self.add_line('p3-r1-3', (24, 8), (30, 14))
        self.add_line('p3-r1-4', (30, 14), (30, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (2, 30), (4, 28))
        self.add_line('p4-r1-2', (4, 28), (8, 21))
        self.add_line('p4-r1-3', (8, 21), (13, 28))
        self.add_line('p4-r1-4', (13, 28), (14, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (4, 28), (13, 28))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (21, 21), (25, 25))
        self.add_line('p6-r1-2', (25, 25), (30, 21))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (25, 25), (25, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p5-r1-1')
        self.relate('connect', 'p4-r1-3', 'p5-r1-1')
        self.relate('connect', 'p4-r1-4', 'p5-r1-1')
        self.relate('connect', 'p6-r1-1', 'p7-r1-1')
        self.relate('connect', 'p6-r1-2', 'p7-r1-1')
