# Variant of sitting-cat-side-view-sub32; parent file remains unchanged.
"""Independent 32px profile of sitting-cat-side-view.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '58377584-5a28-47bf-954d-6f0f493ca1fb'
SOURCE_PATH = 'pictographic-primitives/pets/cat_58377584-5a28-47bf-954d-6f0f493ca1fb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('58377584-5a28-47bf-954d-6f0f493ca1fb', 'pictographic-primitives/pets/cat_58377584-5a28-47bf-954d-6f0f493ca1fb.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sitting-cat-side-view',)
SOLO_SOURCE_ICON_IDS = ('sitting-cat-side-view',)
REFERENCE_EXPORT_SHA256 = '1157191c38e62a59ea1c51619411b5f8040b8e3b9da7c6c77b2bde9330b675ec'

class DrawingVariant2(Sub32):
    icon_id = 'sitting-cat-side-view-sub32-v2'
    variant_of = 'sitting-cat-side-view-sub32'
    variant_label = 'Record the actual joined strokes; preserve reviewed artwork'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/pets'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (14, 10), (14, 2))
        self.add_line('p1-r1-2', (14, 2), (21, 7))
        self.add_line('p1-r1-3', (21, 7), (24, 7))
        self.add_line('p1-r1-4', (24, 7), (30, 2))
        self.add_line('p1-r1-5', (30, 2), (30, 30))
        self.add_line('p1-r1-6', (30, 30), (16, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_arc('p2-r1-1', (16, 30), (16, 14), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-2', (16, 14), (14, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (8, 22), (2, 13), radius_x=6, radius_y=9, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'path-2-1', 'path-3-1')
