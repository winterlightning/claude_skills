"""Independent 32px profile of checklist.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ee9d1910-a200-4e57-8b40-f41cdef29366'
SOURCE_PATH = 'pictographic-primitives/work/checklist_ee9d1910-a200-4e57-8b40-f41cdef29366.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ee9d1910-a200-4e57-8b40-f41cdef29366', 'pictographic-primitives/work/checklist_ee9d1910-a200-4e57-8b40-f41cdef29366.svg'),)
PROFILE_SOURCE_KEYS = ('solo/checklist',)
SOLO_SOURCE_ICON_IDS = ('checklist',)
REFERENCE_EXPORT_SHA256 = 'dc72fbb8823e2d0e1538bca01930fd065ef1f24ec231f0533a07201b6321506b'

class Drawing(Sub32):
    icon_id = 'checklist-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'work'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (14, 8), (10, 12))
        self.add_line('p1-r1-2', (10, 12), (8, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (18, 13), (24, 13))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (14, 18), (10, 21))
        self.add_line('p3-r1-2', (10, 21), (8, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (18, 23), (24, 23))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (28, 2), (4, 2))
        self.add_line('p5-r1-2', (4, 2), (2, 4))
        self.add_line('p5-r1-3', (2, 4), (2, 28))
        self.add_line('p5-r1-4', (2, 28), (4, 30))
        self.add_line('p5-r1-5', (4, 30), (28, 30))
        self.add_line('p5-r1-6', (28, 30), (30, 28))
        self.add_line('p5-r1-7', (30, 28), (30, 4))
        self.add_line('p5-r1-8', (30, 4), (28, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', 'p5-r1-6', 'p5-r1-7', 'p5-r1-8', closed=False)
