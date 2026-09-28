"""Independent 32px profile of couple-broken-heart.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c2a597c8-14e7-4ae0-abaa-97e0be0e581e'
SOURCE_PATH = 'pictographic-primitives/symbol/two persons with broken heart_c2a597c8-14e7-4ae0-abaa-97e0be0e581e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c2a597c8-14e7-4ae0-abaa-97e0be0e581e', 'pictographic-primitives/symbol/two persons with broken heart_c2a597c8-14e7-4ae0-abaa-97e0be0e581e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/couple-broken-heart',)
SOLO_SOURCE_ICON_IDS = ('couple-broken-heart',)
REFERENCE_EXPORT_SHA256 = 'bd2e2fb634d35d181914c7d49a118897eb55601842bda6d6cf8a9d4349c7b8f6'

class Drawing(Sub32):
    icon_id = 'couple-broken-heart-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 5), (8, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (8, 5), (2, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (24, 5), (30, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (30, 5), (24, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 30), (2, 21))
        self.add_bezier('p3-r1-2', (2, 21), ((2, 19), (3, 17), (4, 16)))
        self.add_bezier('p3-r1-3', (4, 16), ((5, 15), (7, 14), (8, 14)))
        self.add_bezier('p3-r1-4', (8, 14), ((8, 14), (8, 14), (8, 14)))
        self.add_line('p3-r1-5', (8, 14), (10, 14))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (30, 30), (30, 21))
        self.add_bezier('p4-r1-2', (30, 21), ((30, 19), (29, 17), (28, 16)))
        self.add_bezier('p4-r1-3', (28, 16), ((27, 15), (25, 14), (24, 14)))
        self.add_line('p4-r1-4', (24, 14), (22, 14))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_arc('p5-r1-1', (16, 18), (10, 14), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p5-r1-2', (10, 14), (8, 18), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p5-r1-3', (8, 18), (16, 27))
        self.add_line('p5-r1-4', (16, 27), (24, 18))
        self.add_arc('p5-r1-5', (24, 18), (22, 14), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p5-r1-6', (22, 14), (16, 18), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', 'p5-r1-6', closed=False)
        self.add_line('p6-r1-1', (16, 18), (16, 21))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p3-r1-5', 'p5-r1-1')
        self.relate('connect', 'p3-r1-5', 'p5-r1-2')
        self.relate('connect', 'p4-r1-4', 'p5-r1-5')
        self.relate('connect', 'p4-r1-4', 'p5-r1-6')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-6', 'p6-r1-1')
