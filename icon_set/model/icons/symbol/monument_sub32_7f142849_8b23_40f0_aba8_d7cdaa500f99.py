"""Independent 32px profile of monument.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7f142849-8b23-40f0-aba8-d7cdaa500f99'
SOURCE_PATH = 'pictographic-primitives/symbol/monument_7f142849-8b23-40f0-aba8-d7cdaa500f99.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7f142849-8b23-40f0-aba8-d7cdaa500f99', 'pictographic-primitives/symbol/monument_7f142849-8b23-40f0-aba8-d7cdaa500f99.svg'),)
PROFILE_SOURCE_KEYS = ('solo/monument',)
SOLO_SOURCE_ICON_IDS = ('monument',)
REFERENCE_EXPORT_SHA256 = '6693946bbcde9a5b15ca86f2606529fa45b1b3405dfb4e454b16ac00d73d6dc6'

class Drawing(Sub32):
    icon_id = 'monument-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (30, 30))
        self.add_bezier('p1-r1-2', (30, 30), ((29, 25), (28, 20), (25, 20)))
        self.add_line('p1-r1-3', (25, 20), (7, 20))
        self.add_bezier('p1-r1-4', (7, 20), ((4, 20), (3, 25), (2, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (7, 20), (7, 15))
        self.add_arc('p2-r1-2', (7, 15), (16, 7), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (16, 7), (25, 15), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (25, 15), (25, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 7))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-4')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
