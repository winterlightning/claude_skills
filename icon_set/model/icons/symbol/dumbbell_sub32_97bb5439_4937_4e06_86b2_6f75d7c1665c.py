"""Independent 32px profile of dumbbell.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '97bb5439-4937-4e06-86b2-6f75d7c1665c'
SOURCE_PATH = 'pictographic-primitives/sports/dumbbell_97bb5439-4937-4e06-86b2-6f75d7c1665c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('97bb5439-4937-4e06-86b2-6f75d7c1665c', 'pictographic-primitives/sports/dumbbell_97bb5439-4937-4e06-86b2-6f75d7c1665c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dumbbell',)
SOLO_SOURCE_ICON_IDS = ('dumbbell',)
REFERENCE_EXPORT_SHA256 = 'a283ea9b4706f65adba06193a96333064abe271113d4d88440fe8b129fd50976'

class Drawing(Sub32):
    icon_id = 'dumbbell-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'sports'
    categories = ('sports', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 4), (10, 4))
        self.add_arc('p1-r1-2', (10, 4), (12, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (12, 6), (12, 16))
        self.add_line('p1-r1-4', (12, 16), (12, 26))
        self.add_arc('p1-r1-5', (12, 26), (10, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (10, 28), (6, 28))
        self.add_arc('p1-r1-7', (6, 28), (4, 26), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (4, 26), (4, 16))
        self.add_line('p1-r1-9', (4, 16), (4, 6))
        self.add_arc('p1-r1-10', (4, 6), (6, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (22, 4), (26, 4))
        self.add_arc('p2-r1-2', (26, 4), (28, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (28, 6), (28, 16))
        self.add_line('p2-r1-4', (28, 16), (28, 26))
        self.add_arc('p2-r1-5', (28, 26), (26, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-6', (26, 28), (22, 28))
        self.add_arc('p2-r1-7', (22, 28), (20, 26), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-8', (20, 26), (20, 16))
        self.add_line('p2-r1-9', (20, 16), (20, 6))
        self.add_arc('p2-r1-10', (20, 6), (22, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', closed=False)
        self.add_line('p3-r1-1', (12, 16), (20, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 16), (4, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (28, 16), (30, 16))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-8', 'p4-r1-1')
        self.relate('connect', 'p1-r1-9', 'p4-r1-1')
        self.relate('connect', 'p2-r1-3', 'p5-r1-1')
        self.relate('connect', 'p2-r1-4', 'p5-r1-1')
        self.relate('connect', 'p2-r1-8', 'p3-r1-1')
        self.relate('connect', 'p2-r1-9', 'p3-r1-1')
