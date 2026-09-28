"""Independent 32px profile of simple-open-umbrella.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'bb6872fb-7ad7-4948-9e90-e03cf896cf9a'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/umbrella_bb6872fb-7ad7-4948-9e90-e03cf896cf9a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bb6872fb-7ad7-4948-9e90-e03cf896cf9a', 'pictographic-primitives/accessories/batch-02/umbrella_bb6872fb-7ad7-4948-9e90-e03cf896cf9a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/simple-open-umbrella',)
SOLO_SOURCE_ICON_IDS = ('simple-open-umbrella',)
REFERENCE_EXPORT_SHA256 = '1965b45b606c18bd5f063472aa719c21bfb7f4dcad2caddcd317bbaa9af5368a'

class Drawing(Sub32):
    icon_id = 'simple-open-umbrella-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (5, 17), ((5, 14), (6, 11), (8, 9)))
        self.add_bezier('p1-r1-2', (8, 9), ((10, 7), (13, 6), (16, 6)))
        self.add_bezier('p1-r1-3', (16, 6), ((19, 6), (22, 7), (24, 9)))
        self.add_bezier('p1-r1-4', (24, 9), ((26, 11), (27, 14), (27, 17)))
        self.add_line('p1-r1-5', (27, 17), (16, 17))
        self.add_line('p1-r1-6', (16, 17), (5, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 6))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 17), (16, 26))
        self.add_bezier('p3-r1-2', (16, 26), ((16, 28), (14, 30), (12, 30)))
        self.add_bezier('p3-r1-3', (12, 30), ((11, 30), (9, 28), (9, 26)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
