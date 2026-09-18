# Variant of ring-sight-inner-ticks-sub32; parent file remains unchanged.
"""Independent 32px profile of ring-sight-inner-ticks.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '61a1fffb-c03a-4331-bdb2-c4f0c937d918'
SOURCE_PATH = 'pictographic-primitives/war/target_61a1fffb-c03a-4331-bdb2-c4f0c937d918.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('61a1fffb-c03a-4331-bdb2-c4f0c937d918', 'pictographic-primitives/war/target_61a1fffb-c03a-4331-bdb2-c4f0c937d918.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ring-sight-inner-ticks',)
SOLO_SOURCE_ICON_IDS = ('ring-sight-inner-ticks',)
REFERENCE_EXPORT_SHA256 = '7ecae7256fe5a5cbd99b00c67677a2b71bd5845fe8f1630835fe10f0ec7a0455'

class DrawingVariant2(Sub32):
    icon_id = 'ring-sight-inner-ticks-sub32-v2'
    variant_of = 'ring-sight-inner-ticks-sub32'
    variant_label = 'Record the actual joined strokes; preserve reviewed artwork'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/war'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (11, 16), (21, 16), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (21, 16), (11, 16), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 11), (16, 8))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 21), (16, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (11, 16), (8, 16))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (21, 16), (24, 16))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p6-r1-1')
        self.relate('connect', 'p2-r1-2', 'p5-r1-1')
        self.relate('connect', 'p2-r1-2', 'p6-r1-1')
        self.relate('connect', 'path-2-1', 'path-3-1')
        self.relate('connect', 'path-2-1', 'path-4-1')
