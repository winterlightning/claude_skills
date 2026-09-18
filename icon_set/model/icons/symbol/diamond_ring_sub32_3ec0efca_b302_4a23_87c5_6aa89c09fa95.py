"""Independent 32px profile of diamond-ring.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3ec0efca-b302-4a23-87c5-6aa89c09fa95'
SOURCE_PATH = 'pictographic-primitives/symbol/ring 1_3ec0efca-b302-4a23-87c5-6aa89c09fa95.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3ec0efca-b302-4a23-87c5-6aa89c09fa95', 'pictographic-primitives/symbol/ring 1_3ec0efca-b302-4a23-87c5-6aa89c09fa95.svg'),)
PROFILE_SOURCE_KEYS = ('solo/diamond-ring',)
SOLO_SOURCE_ICON_IDS = ('diamond-ring',)
REFERENCE_EXPORT_SHA256 = '780392056ae62ad605957dcae1a14d747b9d44d806a7c70c90d53a6d9cad0a8f'

class Drawing(Sub32):
    icon_id = 'diamond-ring-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 10), (9, 5))
        self.add_line('p1-r1-2', (9, 5), (12, 2))
        self.add_line('p1-r1-3', (12, 2), (20, 2))
        self.add_line('p1-r1-4', (20, 2), (23, 5))
        self.add_line('p1-r1-5', (23, 5), (22, 10))
        self.add_arc('p1-r1-6', (22, 10), (27, 19), radius_x=6, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (27, 19), (16, 30), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-8', (16, 30), (5, 19), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-9', (5, 19), (10, 10), radius_x=6, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_arc('p2-r1-1', (10, 10), (22, 10), radius_x=6, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
