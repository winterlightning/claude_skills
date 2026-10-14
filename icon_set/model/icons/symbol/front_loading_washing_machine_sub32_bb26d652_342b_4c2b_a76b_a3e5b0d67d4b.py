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
        # Machine body, two dot knobs and a small porthole (closed circle), each 8 units apart.
        self.add_line('p1-r1-1', (7, 2), (25, 2))
        self.add_arc('p1-r1-2', (25, 2), (28, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (28, 5), (28, 27))
        self.add_arc('p1-r1-4', (28, 27), (25, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (25, 30), (7, 30))
        self.add_arc('p1-r1-6', (7, 30), (4, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (4, 27), (4, 5))
        self.add_arc('p1-r1-8', (4, 5), (7, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=True)
        self.add_arc('p2-r1-1', (14, 20), (18, 20), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (18, 20), (14, 20), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=True)
        self.add_line('p3-r1-1', (12, 10), (12, 10))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (20, 10), (20, 10))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
