"""Independent 32px profile of dumbbell-sports.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c7617317-0663-433d-b73d-2bfd2f6407c8'
SOURCE_PATH = 'pictographic-primitives/sports/dumbbell_c7617317-0663-433d-b73d-2bfd2f6407c8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c7617317-0663-433d-b73d-2bfd2f6407c8', 'pictographic-primitives/sports/dumbbell_c7617317-0663-433d-b73d-2bfd2f6407c8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dumbbell-sports',)
SOLO_SOURCE_ICON_IDS = ('dumbbell-sports',)
REFERENCE_EXPORT_SHA256 = 'f166361525b4fd3cf8d48db4305defc2524a31bd523e8e7bb4a139fbd4a5705f'

class Drawing(Sub32):
    icon_id = 'dumbbell-sports-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'sports'
    categories = ('sports', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (24, 16), (8, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 27), (2, 5))
        self.add_line('p2-r1-2', (2, 5), (8, 5))
        self.add_line('p2-r1-3', (8, 5), (8, 27))
        self.add_line('p2-r1-4', (8, 27), (2, 27))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (24, 5), (30, 5))
        self.add_line('p3-r1-2', (30, 5), (30, 27))
        self.add_line('p3-r1-3', (30, 27), (24, 27))
        self.add_line('p3-r1-4', (24, 27), (24, 5))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
