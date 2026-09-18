"""Independent 32px profile of person-kicking-ball.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '33e0f679-82d2-4c2a-b9d1-af30c1a9b528'
SOURCE_PATH = 'pictographic-primitives/symbol/person playing ball_33e0f679-82d2-4c2a-b9d1-af30c1a9b528.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('33e0f679-82d2-4c2a-b9d1-af30c1a9b528', 'pictographic-primitives/symbol/person playing ball_33e0f679-82d2-4c2a-b9d1-af30c1a9b528.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-kicking-ball',)
SOLO_SOURCE_ICON_IDS = ('person-kicking-ball',)
REFERENCE_EXPORT_SHA256 = 'bda8bb7e341247519c7d6c30c44997e357ac735977992e9a1fb35c58c4c685e4'

class Drawing(Sub32):
    icon_id = 'person-kicking-ball-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 6), (24, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (24, 6), (16, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (16, 15), ((15, 18), (14, 19), (13, 21)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 15), (8, 13))
        self.add_line('p3-r1-2', (8, 13), (4, 18))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (16, 15), (21, 18))
        self.add_line('p4-r1-2', (21, 18), (30, 13))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (13, 21), (7, 27))
        self.add_line('p5-r1-2', (7, 27), (2, 27))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (13, 21), (18, 25))
        self.add_line('p6-r1-2', (18, 25), (14, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_arc('p7-r1-1', (24, 27), (30, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p7-r1-2', (30, 27), (24, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p6-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
