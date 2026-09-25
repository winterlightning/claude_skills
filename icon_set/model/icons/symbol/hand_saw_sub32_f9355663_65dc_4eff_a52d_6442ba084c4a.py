"""Independent 32px profile of hand-saw.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f9355663-65dc-4eff-a52d-6442ba084c4a'
SOURCE_PATH = 'pictographic-primitives/symbol/saw_f9355663-65dc-4eff-a52d-6442ba084c4a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f9355663-65dc-4eff-a52d-6442ba084c4a', 'pictographic-primitives/symbol/saw_f9355663-65dc-4eff-a52d-6442ba084c4a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hand-saw',)
SOLO_SOURCE_ICON_IDS = ('hand-saw',)
REFERENCE_EXPORT_SHA256 = '777b80d74728ad80c5da5136b3cafffa398bd6f35d5a9981c815888679ceadf6'

class Drawing(Sub32):
    icon_id = 'hand-saw-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 7), (8, 2))
        self.add_line('p1-r1-2', (8, 2), (21, 14))
        self.add_line('p1-r1-3', (21, 14), (28, 22))
        self.add_bezier('p1-r1-4', (28, 22), ((29, 22), (30, 23), (30, 25)))
        self.add_bezier('p1-r1-5', (30, 25), ((30, 26), (29, 27), (28, 27)))
        self.add_line('p1-r1-6', (28, 27), (25, 30))
        self.add_line('p1-r1-7', (25, 30), (13, 22))
        self.add_line('p1-r1-8', (13, 22), (10, 19))
        self.add_line('p1-r1-9', (10, 19), (10, 14))
        self.add_line('p1-r1-10', (10, 14), (5, 14))
        self.add_line('p1-r1-11', (5, 14), (5, 10))
        self.add_line('p1-r1-12', (5, 10), (2, 10))
        self.add_line('p1-r1-13', (2, 10), (2, 7))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
        self.add_line('p2-r1-1', (21, 14), (16, 19))
        self.add_line('p2-r1-2', (16, 19), (13, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-2')
        self.relate('connect', 'p1-r1-8', 'p2-r1-2')
