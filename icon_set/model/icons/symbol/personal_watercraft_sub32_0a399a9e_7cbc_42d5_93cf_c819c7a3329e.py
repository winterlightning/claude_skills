"""Independent 32px profile of personal-watercraft.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0a399a9e-7cbc-42d5-93cf-c819c7a3329e'
SOURCE_PATH = 'pictographic-primitives/recreation/jet ski_0a399a9e-7cbc-42d5-93cf-c819c7a3329e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0a399a9e-7cbc-42d5-93cf-c819c7a3329e', 'pictographic-primitives/recreation/jet ski_0a399a9e-7cbc-42d5-93cf-c819c7a3329e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/personal-watercraft',)
SOLO_SOURCE_ICON_IDS = ('personal-watercraft',)
REFERENCE_EXPORT_SHA256 = '01e00fbdf045ba12c2d63e1e9a783e535412d79a2bc6efaa8018f14e22adf440'

class Drawing(Sub32):
    icon_id = 'personal-watercraft-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/recreation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 24), (8, 13))
        self.add_line('p1-r1-2', (8, 13), (12, 5))
        self.add_line('p1-r1-3', (12, 5), (16, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (8, 13), (13, 13))
        self.add_line('p2-r1-2', (13, 13), (17, 17))
        self.add_line('p2-r1-3', (17, 17), (24, 17))
        self.add_arc('p2-r1-4', (24, 17), (30, 23), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (30, 23), (30, 24))
        self.add_bezier('p2-r1-6', (30, 24), ((30, 26), (29, 26), (29, 27)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (2, 24), (30, 24))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 24), (8, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p2-r1-5', 'p3-r1-1')
        self.relate('connect', 'p2-r1-6', 'p3-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
