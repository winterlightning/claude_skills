"""Independent 32px profile of front-loading-washing-machine.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'bb26d652-342b-4c2b-a76b-a3e5b0d67d4b'
SOURCE_PATH = 'pictographic-primitives/wayfinding/laundry machine_bb26d652-342b-4c2b-a76b-a3e5b0d67d4b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bb26d652-342b-4c2b-a76b-a3e5b0d67d4b', 'pictographic-primitives/wayfinding/laundry machine_bb26d652-342b-4c2b-a76b-a3e5b0d67d4b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/front-loading-washing-machine',)
SOLO_SOURCE_ICON_IDS = ('front-loading-washing-machine',)
REFERENCE_EXPORT_SHA256 = '7a315550a38b27161215307a2a1e47906de5e94a0e5a848f06b50e031dddbf3f'

class Drawing(Sub32):
    icon_id = 'front-loading-washing-machine-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'wayfinding'
    categories = ('wayfinding', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (24, 2))
        self.add_arc('p1-r1-2', (24, 2), (27, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (27, 5), (27, 27))
        self.add_arc('p1-r1-4', (27, 27), (24, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (24, 30), (8, 30))
        self.add_arc('p1-r1-6', (8, 30), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (5, 27), (5, 5))
        self.add_arc('p1-r1-8', (5, 5), (8, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_arc('p2-r1-1', (11, 19), (21, 19), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (21, 19), (11, 19), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (12, 8), (12, 8))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (20, 8), (20, 8))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
