"""Independent 32px profile of snowmobile-angled.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b75710e7-8d86-43e7-8398-5efed8f7194b'
SOURCE_PATH = 'pictographic-primitives/symbol/snow scooter_b75710e7-8d86-43e7-8398-5efed8f7194b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b75710e7-8d86-43e7-8398-5efed8f7194b', 'pictographic-primitives/symbol/snow scooter_b75710e7-8d86-43e7-8398-5efed8f7194b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/snowmobile-angled',)
SOLO_SOURCE_ICON_IDS = ('snowmobile-angled',)
REFERENCE_EXPORT_SHA256 = '85dca3d6a7e4ca3cc548e35034ccfb39175b24574985faf0cd31c91085beedcc'

class Drawing(Sub32):
    icon_id = 'snowmobile-angled-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 5), (15, 5))
        self.add_line('p1-r1-2', (15, 5), (19, 9))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 20), (3, 15))
        self.add_line('p2-r1-2', (3, 15), (12, 14))
        self.add_line('p2-r1-3', (12, 14), (15, 9))
        self.add_line('p2-r1-4', (15, 9), (19, 9))
        self.add_line('p2-r1-5', (19, 9), (23, 13))
        self.add_arc('p2-r1-6', (23, 13), (23, 20), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-7', (23, 20), (22, 20))
        self.add_line('p2-r1-8', (22, 20), (16, 20))
        self.add_line('p2-r1-9', (16, 20), (13, 20))
        self.add_line('p2-r1-10', (13, 20), (5, 20))
        self.add_line('p2-r1-11', (5, 20), (2, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', closed=False)
        self.add_line('p3-r1-1', (22, 20), (22, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (17, 27), (22, 27))
        self.add_line('p4-r1-2', (22, 27), (26, 27))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_arc('p5-r1-1', (26, 27), (30, 23), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (5, 20), (2, 24), radius_x=3, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p6-r1-2', (2, 24), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p6-r1-3', (5, 27), (9, 27))
        self.add_line('p6-r1-4', (9, 27), (16, 20))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-4')
        self.relate('connect', 'p1-r1-2', 'p2-r1-5')
        self.relate('connect', 'p2-r1-7', 'p3-r1-1')
        self.relate('connect', 'p2-r1-8', 'p3-r1-1')
        self.relate('connect', 'p2-r1-8', 'p6-r1-4')
        self.relate('connect', 'p2-r1-9', 'p6-r1-4')
        self.relate('connect', 'p2-r1-10', 'p6-r1-1')
        self.relate('connect', 'p2-r1-11', 'p6-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p4-r1-2', 'p5-r1-1')
