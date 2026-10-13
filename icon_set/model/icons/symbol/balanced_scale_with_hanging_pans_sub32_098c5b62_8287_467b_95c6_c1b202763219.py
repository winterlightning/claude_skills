"""Independent 32px profile of balanced-scale-with-hanging-pans.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '098c5b62-8287-467b-95c6-c1b202763219'
SOURCE_PATH = 'pictographic-primitives/business/scale_098c5b62-8287-467b-95c6-c1b202763219.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('098c5b62-8287-467b-95c6-c1b202763219', 'pictographic-primitives/business/scale_098c5b62-8287-467b-95c6-c1b202763219.svg'), ('a443bfb2-9fd7-4e55-96b8-03968dd0394b', 'pictographic-primitives/business/scale_a443bfb2-9fd7-4e55-96b8-03968dd0394b.svg'), ('fcb4406f-0560-4d96-8364-53fb1119bcf0', 'pictographic-primitives/business/scale_fcb4406f-0560-4d96-8364-53fb1119bcf0.svg'))
PROFILE_SOURCE_KEYS = ('solo/balanced-scale-with-hanging-pans',)
SOLO_SOURCE_ICON_IDS = ('balanced-scale-with-hanging-pans',)
REFERENCE_EXPORT_SHA256 = 'ae3e088570ec5dd760668a9bd5846171aefed189ceb4c202eb50c3e1c641a57c'

class Drawing(Sub32):
    icon_id = 'balanced-scale-with-hanging-pans-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'business'
    categories = ('primitives', 'business')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 4), (16, 8))
        self.add_line('p1-r1-2', (16, 8), (16, 28))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (5, 8), (16, 8))
        self.add_line('p2-r1-2', (16, 8), (27, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (10, 28), (16, 28))
        self.add_line('p3-r1-2', (16, 28), (22, 28))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (5, 8), (5, 17))
        self.add_arc('p4-r1-2', (2, 16), (8, 16), radius_x=3, radius_y=1, large_arc=False, sweep=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p4-r1-2', closed=False)
        self.add_line('p6-r1-1', (27, 8), (27, 17))
        self.add_arc('p6-r1-2', (24, 16), (30, 16), radius_x=3, radius_y=1, large_arc=False, sweep=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_contour('path-7-1', 'p6-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-2')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-2', 'p6-r1-1')
        self.relate('connect', 'p4-r1-1', 'p4-r1-2')
        self.relate('connect', 'p6-r1-1', 'p6-r1-2')
        self.relate('connect', 'path-4-1', 'path-5-1')
        self.relate('connect', 'path-6-1', 'path-7-1')
