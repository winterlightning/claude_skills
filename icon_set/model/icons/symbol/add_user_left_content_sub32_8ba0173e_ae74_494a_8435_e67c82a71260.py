"""Independent 32px profile of add-user-left-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8ba0173e-ae74-494a-8435-e67c82a71260'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/8ba0173e-ae74-494a-8435-e67c82a71260.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8ba0173e-ae74-494a-8435-e67c82a71260', 'icon_set/dist/gallery/combination-originals/8ba0173e-ae74-494a-8435-e67c82a71260.svg'),)
PROFILE_SOURCE_KEYS = ('solo/add-user-left-content',)
SOLO_SOURCE_ICON_IDS = ('add-user-left-content',)
REFERENCE_EXPORT_SHA256 = '061c965af2977a97a0487093676ff310f581ee1595dc3a016ae9f50bbb25bd16'

class Drawing(Sub32):
    icon_id = 'add-user-left-content-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 9), (24, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (24, 9), (16, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (10, 27), (30, 27), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (5, 9), (2, 9))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (5, 9), (8, 9))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (5, 9), (5, 6))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (5, 9), (5, 12))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p6-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
