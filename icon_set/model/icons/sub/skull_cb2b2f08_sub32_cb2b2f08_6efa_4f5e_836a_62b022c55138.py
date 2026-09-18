"""Independent 32px profile of skull-cb2b2f08.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'cb2b2f08-6efa-4f5e-836a-62b022c55138'
SOURCE_PATH = 'pictographic-primitives/interface-essential/skull_cb2b2f08-6efa-4f5e-836a-62b022c55138.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cb2b2f08-6efa-4f5e-836a-62b022c55138', 'pictographic-primitives/interface-essential/skull_cb2b2f08-6efa-4f5e-836a-62b022c55138.svg'),)
PROFILE_SOURCE_KEYS = ('solo/skull-cb2b2f08',)
SOLO_SOURCE_ICON_IDS = ('skull-cb2b2f08',)
REFERENCE_EXPORT_SHA256 = '52150fccc150717127a6ce745013d819258f1bd0fadf2055b41c84a09f006ed2'

class Drawing(Sub32):
    icon_id = 'skull-cb2b2f08-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 5), ((8, 5), (2, 11), (2, 17)))
        self.add_bezier('p1-r1-2', (2, 17), ((2, 20), (8, 20), (8, 23)))
        self.add_line('p1-r1-3', (8, 23), (8, 24))
        self.add_arc('p1-r1-4', (8, 24), (10, 27), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (10, 27), (16, 27))
        self.add_line('p1-r1-6', (16, 27), (22, 27))
        self.add_arc('p1-r1-7', (22, 27), (24, 24), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-8', (24, 24), (24, 23))
        self.add_bezier('p1-r1-9', (24, 23), ((24, 20), (30, 20), (30, 17)))
        self.add_bezier('p1-r1-10', (30, 17), ((30, 11), (24, 5), (16, 5)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (10, 15), (10, 15))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 15), (22, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 22), (16, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-5', 'p4-r1-1')
        self.relate("connect", 'p1-r1-6', 'p4-r1-1')
