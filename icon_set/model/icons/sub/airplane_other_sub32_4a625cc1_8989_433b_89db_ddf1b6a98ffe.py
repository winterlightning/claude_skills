"""Independent 32px profile of airplane-other.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4a625cc1-8989-433b-89db-ddf1b6a98ffe'
SOURCE_PATH = 'pictographic-primitives/other/airplane_4a625cc1-8989-433b-89db-ddf1b6a98ffe.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4a625cc1-8989-433b-89db-ddf1b6a98ffe', 'pictographic-primitives/other/airplane_4a625cc1-8989-433b-89db-ddf1b6a98ffe.svg'),)
PROFILE_SOURCE_KEYS = ('solo/airplane-other',)
SOLO_SOURCE_ICON_IDS = ('airplane-other',)
REFERENCE_EXPORT_SHA256 = '71fea4c7397e16d0129ef815a68871c7c07a8e6f98d58b1d3e6ee8094214d97e'

class Drawing(Sub32):
    icon_id = 'airplane-other-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (19, 5), (19, 7))
        self.add_line('p1-r1-2', (19, 7), (30, 13))
        self.add_line('p1-r1-3', (30, 13), (30, 21))
        self.add_line('p1-r1-4', (30, 21), (19, 14))
        self.add_line('p1-r1-5', (19, 14), (19, 22))
        self.add_line('p1-r1-6', (19, 22), (25, 30))
        self.add_line('p1-r1-7', (25, 30), (16, 30))
        self.add_line('p1-r1-8', (16, 30), (7, 30))
        self.add_line('p1-r1-9', (7, 30), (13, 22))
        self.add_line('p1-r1-10', (13, 22), (13, 14))
        self.add_line('p1-r1-11', (13, 14), (2, 21))
        self.add_line('p1-r1-12', (2, 21), (2, 13))
        self.add_line('p1-r1-13', (2, 13), (13, 7))
        self.add_line('p1-r1-14', (13, 7), (13, 5))
        self.add_arc('p1-r1-15', (13, 5), (19, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', closed=False)
