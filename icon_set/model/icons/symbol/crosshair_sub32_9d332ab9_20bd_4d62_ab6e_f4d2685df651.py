"""Independent 32px profile of crosshair.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9d332ab9-20bd-4d62-ab6e-f4d2685df651'
SOURCE_PATH = 'pictographic-primitives/symbol/focus with target_9d332ab9-20bd-4d62-ab6e-f4d2685df651.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9d332ab9-20bd-4d62-ab6e-f4d2685df651', 'pictographic-primitives/symbol/focus with target_9d332ab9-20bd-4d62-ab6e-f4d2685df651.svg'),)
PROFILE_SOURCE_KEYS = ('solo/crosshair',)
SOLO_SOURCE_ICON_IDS = ('crosshair',)
REFERENCE_EXPORT_SHA256 = 'f5ea00a610113afb95a5bb8876fe54f736dd023c80564fb4a715593bb85c8faa'

class Drawing(Sub32):
    icon_id = 'crosshair-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 6), (26, 16), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (26, 16), (16, 26), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 26), (6, 16), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (6, 16), (16, 6), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 6))
        self.add_line('p2-r1-2', (16, 6), (16, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (30, 16), (26, 16))
        self.add_line('p3-r1-2', (26, 16), (22, 16))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (16, 30), (16, 26))
        self.add_line('p4-r1-2', (16, 26), (16, 22))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (2, 16), (6, 16))
        self.add_line('p5-r1-2', (6, 16), (10, 16))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-2')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-2')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-2')
        self.relate('connect', 'p1-r1-3', 'p4-r1-1')
        self.relate('connect', 'p1-r1-3', 'p4-r1-2')
        self.relate('connect', 'p1-r1-3', 'p5-r1-1')
        self.relate('connect', 'p1-r1-3', 'p5-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p5-r1-1')
        self.relate('connect', 'p1-r1-4', 'p5-r1-2')
