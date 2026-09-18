"""Independent 32px profile of airplane-horizontal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0e73af01-7338-412e-b76b-79b5b693ad46'
SOURCE_PATH = 'pictographic-primitives/symbol/plane horizontal_0e73af01-7338-412e-b76b-79b5b693ad46.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0e73af01-7338-412e-b76b-79b5b693ad46', 'pictographic-primitives/symbol/plane horizontal_0e73af01-7338-412e-b76b-79b5b693ad46.svg'),)
PROFILE_SOURCE_KEYS = ('solo/airplane-horizontal',)
SOLO_SOURCE_ICON_IDS = ('airplane-horizontal',)
REFERENCE_EXPORT_SHA256 = '1ced619c9f7ceac5ee7827e4a839b108a5f50ff8d495a43abca8958dbf401f3c'

class Drawing(Sub32):
    icon_id = 'airplane-horizontal-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 10), (8, 12))
        self.add_line('p1-r1-2', (8, 12), (12, 12))
        self.add_line('p1-r1-3', (12, 12), (9, 5))
        self.add_line('p1-r1-4', (9, 5), (15, 5))
        self.add_line('p1-r1-5', (15, 5), (22, 12))
        self.add_line('p1-r1-6', (22, 12), (26, 12))
        self.add_arc('p1-r1-7', (26, 12), (26, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (26, 20), (22, 20))
        self.add_line('p1-r1-9', (22, 20), (15, 27))
        self.add_line('p1-r1-10', (15, 27), (9, 27))
        self.add_line('p1-r1-11', (9, 27), (12, 20))
        self.add_line('p1-r1-12', (12, 20), (8, 20))
        self.add_line('p1-r1-13', (8, 20), (2, 22))
        self.add_line('p1-r1-14', (2, 22), (5, 16))
        self.add_line('p1-r1-15', (5, 16), (2, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', closed=False)
