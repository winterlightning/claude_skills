"""Independent 32px profile of ship-transportation.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8d5fe550-1dfa-4180-b3f3-18aa73106ce5'
SOURCE_PATH = 'pictographic-primitives/transportation/ship_8d5fe550-1dfa-4180-b3f3-18aa73106ce5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8d5fe550-1dfa-4180-b3f3-18aa73106ce5', 'pictographic-primitives/transportation/ship_8d5fe550-1dfa-4180-b3f3-18aa73106ce5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ship-transportation',)
SOLO_SOURCE_ICON_IDS = ('ship-transportation',)
REFERENCE_EXPORT_SHA256 = '3de767a5f6ed37fa3b9bca02399ca9ab009f345ead1af7bde900c8c6c24e7eae'

class Drawing(Sub32):
    icon_id = 'ship-transportation-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 19), (12, 19))
        self.add_line('p1-r1-2', (12, 19), (17, 19))
        self.add_line('p1-r1-3', (17, 19), (26, 19))
        self.add_line('p1-r1-4', (26, 19), (24, 24))
        self.add_bezier('p1-r1-5', (24, 24), ((22, 24), (19, 27), (16, 27)))
        self.add_bezier('p1-r1-6', (16, 27), ((13, 27), (10, 24), (8, 24)))
        self.add_line('p1-r1-7', (8, 24), (6, 19))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_bezier('p2-r1-1', (12, 19), ((13, 16), (13, 14), (13, 12)))
        self.add_bezier('p2-r1-2', (13, 12), ((13, 9), (13, 6), (12, 5)))
        self.add_bezier('p2-r1-3', (12, 5), ((19, 5), (23, 9), (24, 13)))
        self.add_line('p2-r1-4', (24, 13), (17, 19))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (2, 27), ((5, 27), (5, 24), (8, 24)))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (24, 24), ((27, 24), (27, 27), (30, 27)))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-4')
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p4-r1-1')
        self.relate('connect', 'p1-r1-5', 'p4-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
