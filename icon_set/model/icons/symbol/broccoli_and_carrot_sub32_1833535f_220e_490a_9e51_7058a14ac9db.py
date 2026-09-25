"""Independent 32px profile of broccoli-and-carrot.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1833535f-220e-490a-9e51-7058a14ac9db'
SOURCE_PATH = 'pictographic-primitives/symbol/broccoli carrot_1833535f-220e-490a-9e51-7058a14ac9db.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1833535f-220e-490a-9e51-7058a14ac9db', 'pictographic-primitives/symbol/broccoli carrot_1833535f-220e-490a-9e51-7058a14ac9db.svg'),)
PROFILE_SOURCE_KEYS = ('solo/broccoli-and-carrot',)
SOLO_SOURCE_ICON_IDS = ('broccoli-and-carrot',)
REFERENCE_EXPORT_SHA256 = '5abca3a5480bb7ebe2639c9eed0ff71302aede2d9c5d95604220028bf0299213'

class Drawing(Sub32):
    icon_id = 'broccoli-and-carrot-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (7, 16), (2, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (2, 11), (7, 5), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (7, 5), (13, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (13, 5), (16, 10), radius_x=3, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (16, 10), (11, 16), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (11, 16), (9, 15))
        self.add_line('p1-r1-7', (9, 15), (7, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (7, 16), (8, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 30), (21, 18))
        self.add_arc('p3-r1-2', (21, 18), (25, 19), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (25, 19), (28, 25), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p3-r1-4', (28, 25), (13, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (27, 10), (27, 18))
        self.add_line('p4-r1-2', (27, 18), (30, 14))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (27, 18), (25, 19))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p3-r1-2', 'p5-r1-1')
        self.relate('connect', 'p3-r1-3', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p5-r1-1')
