"""Independent 32px profile of institution.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2ee457ae-4157-4c6d-bafa-66a532de7822'
SOURCE_PATH = 'pictographic-primitives/symbol/institution_2ee457ae-4157-4c6d-bafa-66a532de7822.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2ee457ae-4157-4c6d-bafa-66a532de7822', 'pictographic-primitives/symbol/institution_2ee457ae-4157-4c6d-bafa-66a532de7822.svg'),)
PROFILE_SOURCE_KEYS = ('solo/institution',)
SOLO_SOURCE_ICON_IDS = ('institution',)
REFERENCE_EXPORT_SHA256 = '189ef2fbb9dadc46a702f2f2f7809f177bcd758609ac6d0da0a09e785fd98271'

class Drawing(Sub32):
    icon_id = 'institution-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 22), (16, 13), radius_x=11, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 13), (27, 22), radius_x=11, radius_y=9, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (27, 22), (24, 22))
        self.add_line('p1-r1-4', (24, 22), (8, 22))
        self.add_line('p1-r1-5', (8, 22), (5, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (8, 22), (8, 30))
        self.add_line('p2-r1-2', (8, 30), (24, 30))
        self.add_line('p2-r1-3', (24, 30), (24, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (16, 2), (24, 2))
        self.add_line('p3-r1-2', (24, 2), (24, 8))
        self.add_line('p3-r1-3', (24, 8), (16, 8))
        self.add_line('p3-r1-4', (16, 8), (16, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (16, 8), (16, 13))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p1-r1-2', 'p4-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-3')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-3')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p3-r1-3', 'p4-r1-1')
        self.relate("connect", 'p3-r1-4', 'p4-r1-1')
