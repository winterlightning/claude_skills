"""Independent 32px profile of person-pushing-wall.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'fe641fda-6a23-4dc4-970c-90a6fe33f671'
SOURCE_PATH = 'pictographic-primitives/symbol/person pushing_fe641fda-6a23-4dc4-970c-90a6fe33f671.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fe641fda-6a23-4dc4-970c-90a6fe33f671', 'pictographic-primitives/symbol/person pushing_fe641fda-6a23-4dc4-970c-90a6fe33f671.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-pushing-wall',)
SOLO_SOURCE_ICON_IDS = ('person-pushing-wall',)
REFERENCE_EXPORT_SHA256 = '883e6cf9d9b923d86ace4e53cf77785abbbceb1de6c7c5ed68efc5d3f4ff44e6'

class Drawing(Sub32):
    icon_id = 'person-pushing-wall-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (14, 8), (22, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (22, 8), (14, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (14, 18), ((13, 20), (11, 22), (10, 24)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (10, 24), (2, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (14, 18), (21, 21))
        self.add_line('p4-r1-2', (21, 21), (30, 14))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (10, 24), (19, 24))
        self.add_line('p5-r1-2', (19, 24), (16, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (30, 2), (30, 14))
        self.add_line('p6-r1-2', (30, 14), (30, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p6-r1-1')
        self.relate('connect', 'p4-r1-2', 'p6-r1-2')
