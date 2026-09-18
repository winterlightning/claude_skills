"""Independent 32px profile of shirt-width-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '209827a6-da89-4cf7-a37d-a474d679eb0b'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/209827a6-da89-4cf7-a37d-a474d679eb0b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('209827a6-da89-4cf7-a37d-a474d679eb0b', 'icon_set/dist/gallery/combination-originals/209827a6-da89-4cf7-a37d-a474d679eb0b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shirt-width-content',)
SOLO_SOURCE_ICON_IDS = ('shirt-width-content',)
REFERENCE_EXPORT_SHA256 = '55fd29a7b450e76b61bb1194566c81abd5f8e09a44e64ea6286dd52f5354803e'

class Drawing(Sub32):
    icon_id = 'shirt-width-content-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 5), (8, 9))
        self.add_line('p1-r1-2', (8, 9), (10, 12))
        self.add_line('p1-r1-3', (10, 12), (10, 18))
        self.add_line('p1-r1-4', (10, 18), (22, 18))
        self.add_line('p1-r1-5', (22, 18), (22, 12))
        self.add_line('p1-r1-6', (22, 12), (24, 9))
        self.add_line('p1-r1-7', (24, 9), (22, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (22, 5), (19, 5))
        self.add_arc('p2-r1-2', (19, 5), (13, 5), radius_x=3, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (13, 5), (10, 5))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (2, 24), (30, 24))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (5, 20), (2, 24))
        self.add_line('p4-r1-2', (2, 24), (6, 27))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (27, 20), (30, 24))
        self.add_line('p5-r1-2', (30, 24), (26, 27))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-2')
