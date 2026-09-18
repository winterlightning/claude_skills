"""Independent 32px profile of snowboarding.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6bd421c1-b45f-42f7-bc55-f1a7d00409df'
SOURCE_PATH = 'pictographic-primitives/symbol/skiing_6bd421c1-b45f-42f7-bc55-f1a7d00409df.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6bd421c1-b45f-42f7-bc55-f1a7d00409df', 'pictographic-primitives/symbol/skiing_6bd421c1-b45f-42f7-bc55-f1a7d00409df.svg'),)
PROFILE_SOURCE_KEYS = ('solo/snowboarding',)
SOLO_SOURCE_ICON_IDS = ('snowboarding',)
REFERENCE_EXPORT_SHA256 = '98706e3f5edaf11862d3eeafe16e4c01339420b23272ca9d1902f55181afb345'

class Drawing(Sub32):
    icon_id = 'snowboarding-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (22, 11), (30, 11), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 11), (22, 11), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (17, 14), ((14, 16), (13, 17), (13, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (17, 14), (8, 13))
        self.add_line('p3-r1-2', (8, 13), (14, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (13, 18), (7, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (13, 18), (16, 27))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (2, 22), (7, 24))
        self.add_line('p6-r1-2', (7, 24), (16, 27))
        self.add_line('p6-r1-3', (16, 27), (21, 28))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', closed=False)
        self.add_arc('p7-r1-1', (21, 28), (30, 28), radius_x=5, radius_y=2, large_arc=False, sweep=False)
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-1', 'p6-r1-1')
        self.relate("connect", 'p4-r1-1', 'p6-r1-2')
        self.relate("connect", 'p5-r1-1', 'p6-r1-2')
        self.relate("connect", 'p5-r1-1', 'p6-r1-3')
        self.relate("connect", 'p6-r1-3', 'p7-r1-1')
