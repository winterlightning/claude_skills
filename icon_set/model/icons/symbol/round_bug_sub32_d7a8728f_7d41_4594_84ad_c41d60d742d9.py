"""Independent 32px profile of round-bug.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'd7a8728f-7d41-4594-84ad-c41d60d742d9'
SOURCE_PATH = 'pictographic-primitives/animals/pet_d7a8728f-7d41-4594-84ad-c41d60d742d9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d7a8728f-7d41-4594-84ad-c41d60d742d9', 'pictographic-primitives/animals/pet_d7a8728f-7d41-4594-84ad-c41d60d742d9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/round-bug',)
SOLO_SOURCE_ICON_IDS = ('round-bug',)
REFERENCE_EXPORT_SHA256 = 'dd7bc93b25c928afcefe72bc8524292a771e8c6acdc7a00a2059a9f0e1ecd855'

class Drawing(Sub32):
    icon_id = 'round-bug-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'animals'
    categories = ('animals', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (7, 18), (11, 12), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (11, 12), (21, 12))
        self.add_arc('p1-r1-3', (21, 12), (25, 18), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (25, 18), (25, 24))
        self.add_bezier('p1-r1-5', (25, 24), ((25, 27), (23, 30), (21, 30)))
        self.add_bezier('p1-r1-6', (21, 30), ((19, 30), (18, 30), (16, 30)))
        self.add_bezier('p1-r1-7', (16, 30), ((14, 30), (13, 30), (11, 30)))
        self.add_bezier('p1-r1-8', (11, 30), ((9, 30), (7, 27), (7, 24)))
        self.add_line('p1-r1-9', (7, 24), (7, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (11, 12), (11, 7))
        self.add_arc('p2-r1-2', (11, 7), (16, 3), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (16, 3), (21, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (21, 7), (21, 12))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_arc('p3-r1-1', (11, 7), (6, 2), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (21, 7), (26, 2), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (7, 18), (2, 16), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (25, 18), (30, 16), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (7, 24), (2, 24))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (25, 24), (30, 24))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (11, 30), (2, 30))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.add_line('p10-r1-1', (21, 30), (30, 30))
        self.add_contour('path-10-1', 'p10-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p5-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-4')
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-3', 'p6-r1-1')
        self.relate('connect', 'p1-r1-4', 'p6-r1-1')
        self.relate('connect', 'p1-r1-4', 'p8-r1-1')
        self.relate('connect', 'p1-r1-5', 'p8-r1-1')
        self.relate('connect', 'p1-r1-5', 'p10-r1-1')
        self.relate('connect', 'p1-r1-6', 'p10-r1-1')
        self.relate('connect', 'p1-r1-7', 'p9-r1-1')
        self.relate('connect', 'p1-r1-8', 'p7-r1-1')
        self.relate('connect', 'p1-r1-8', 'p9-r1-1')
        self.relate('connect', 'p1-r1-9', 'p5-r1-1')
        self.relate('connect', 'p1-r1-9', 'p7-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p4-r1-1')
        self.relate('connect', 'p2-r1-4', 'p4-r1-1')
