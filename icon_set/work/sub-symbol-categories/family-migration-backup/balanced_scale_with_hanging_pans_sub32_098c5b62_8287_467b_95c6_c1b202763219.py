"""Independent 32px profile of balanced-scale-with-hanging-pans.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

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
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'business'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 5), (16, 8))
        self.add_line('p1-r1-2', (16, 8), (16, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (6, 8), (16, 8))
        self.add_line('p2-r1-2', (16, 8), (26, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (10, 27), (16, 27))
        self.add_line('p3-r1-2', (16, 27), (22, 27))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (6, 8), (9, 16))
        self.add_arc('p4-r1-2', (9, 16), (2, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p4-r1-3', (2, 16), (6, 8))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.add_line('p5-r1-1', (2, 16), (9, 16))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (26, 8), (30, 16))
        self.add_arc('p6-r1-2', (30, 16), (23, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p6-r1-3', (23, 16), (26, 8))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', closed=False)
        self.add_line('p7-r1-1', (23, 16), (30, 16))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-2')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-3')
        self.relate("connect", 'p2-r1-2', 'p6-r1-1')
        self.relate("connect", 'p2-r1-2', 'p6-r1-3')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-2', 'p5-r1-1')
        self.relate("connect", 'p4-r1-3', 'p5-r1-1')
        self.relate("connect", 'p6-r1-1', 'p7-r1-1')
        self.relate("connect", 'p6-r1-2', 'p7-r1-1')
        self.relate("connect", 'p6-r1-3', 'p7-r1-1')
