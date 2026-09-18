"""Independent 32px profile of obelisk-on-plinth.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '58e11e3e-2b0c-402a-935d-87f070933827'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/tower_58e11e3e-2b0c-402a-935d-87f070933827.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('58e11e3e-2b0c-402a-935d-87f070933827', 'pictographic-primitives/landmarks/batch-02/tower_58e11e3e-2b0c-402a-935d-87f070933827.svg'),)
PROFILE_SOURCE_KEYS = ('solo/obelisk-on-plinth',)
SOLO_SOURCE_ICON_IDS = ('obelisk-on-plinth',)
REFERENCE_EXPORT_SHA256 = 'bcd71e46155f9c263ac76cf69ef02c8d3bdc2f65c108a3e0b801e8f2101214e9'

class Drawing(Sub32):
    icon_id = 'obelisk-on-plinth-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'places/landmarks'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 30), (8, 4))
        self.add_line('p1-r1-2', (8, 4), (11, 2))
        self.add_line('p1-r1-3', (11, 2), (11, 2))
        self.add_line('p1-r1-4', (11, 2), (14, 4))
        self.add_line('p1-r1-5', (14, 4), (17, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (2, 30), (6, 30))
        self.add_line('p2-r1-2', (6, 30), (17, 30))
        self.add_line('p2-r1-3', (17, 30), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (22, 6), (29, 6), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (29, 6), (28, 10), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (28, 10), (22, 10))
        self.add_arc('p3-r1-4', (22, 10), (22, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-5', 'p2-r1-2')
        self.relate('connect', 'p1-r1-5', 'p2-r1-3')
