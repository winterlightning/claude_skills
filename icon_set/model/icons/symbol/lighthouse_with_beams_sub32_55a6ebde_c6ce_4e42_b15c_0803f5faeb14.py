"""Independent 32px profile of lighthouse-with-beams.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '55a6ebde-c6ce-4e42-b15c-0803f5faeb14'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/lighthouse_55a6ebde-c6ce-4e42-b15c-0803f5faeb14.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('55a6ebde-c6ce-4e42-b15c-0803f5faeb14', 'pictographic-primitives/landmarks/batch-06/lighthouse_55a6ebde-c6ce-4e42-b15c-0803f5faeb14.svg'),)
PROFILE_SOURCE_KEYS = ('solo/lighthouse-with-beams',)
SOLO_SOURCE_ICON_IDS = ('lighthouse-with-beams',)
REFERENCE_EXPORT_SHA256 = 'a27016b858ba8279a831816f3efd9025aecee5991ed03369121e33a63a165533'

class Drawing(Sub32):
    icon_id = 'lighthouse-with-beams-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'landmarks'
    categories = ('landmarks', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 30), (11, 14))
        self.add_line('p1-r1-2', (11, 14), (11, 9))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (11, 9), (16, 4), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (16, 4), (21, 9), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (21, 9), (21, 14))
        self.add_line('p3-r1-2', (21, 14), (27, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (11, 14), (21, 14))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (16, 2), (16, 4))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (5, 30), (16, 30))
        self.add_line('p6-r1-2', (16, 30), (27, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (16, 25), (16, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (2, 7), (4, 9))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (28, 9), (30, 7))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-1', 'p6-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p6-r1-2')
        self.relate('connect', 'p6-r1-1', 'p7-r1-1')
        self.relate('connect', 'p6-r1-2', 'p7-r1-1')
