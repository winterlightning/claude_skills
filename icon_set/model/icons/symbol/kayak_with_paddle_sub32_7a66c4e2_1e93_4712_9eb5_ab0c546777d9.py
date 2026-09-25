"""Independent 32px profile of kayak-with-paddle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7a66c4e2-1e93-4712-9eb5-ab0c546777d9'
SOURCE_PATH = 'pictographic-primitives/transportation/kayak_7a66c4e2-1e93-4712-9eb5-ab0c546777d9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7a66c4e2-1e93-4712-9eb5-ab0c546777d9', 'pictographic-primitives/transportation/kayak_7a66c4e2-1e93-4712-9eb5-ab0c546777d9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/kayak-with-paddle',)
SOLO_SOURCE_ICON_IDS = ('kayak-with-paddle',)
REFERENCE_EXPORT_SHA256 = 'fa69b3a20e6b6c62d11685ea5be9b64f50502e0b48cf562fbb8e86a935677afa'

class Drawing(Sub32):
    icon_id = 'kayak-with-paddle-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (30, 2), ((20, 2), (13, 4), (8, 8)))
        self.add_bezier('p1-r1-2', (8, 8), ((4, 13), (2, 20), (2, 30)))
        self.add_bezier('p1-r1-3', (2, 30), ((12, 30), (19, 28), (24, 24)))
        self.add_bezier('p1-r1-4', (24, 24), ((28, 19), (30, 12), (30, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (8, 5), (5, 8), radius_x=3, radius_y=3, large_arc=True, sweep=False)
        self.add_line('p2-r1-2', (5, 8), (8, 8))
        self.add_line('p2-r1-3', (8, 8), (8, 5))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (24, 27), (27, 24), radius_x=3, radius_y=3, large_arc=True, sweep=False)
        self.add_line('p3-r1-2', (27, 24), (24, 24))
        self.add_line('p3-r1-3', (24, 24), (24, 27))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (8, 8), (24, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-2')
        self.relate('connect', 'p1-r1-3', 'p3-r1-3')
        self.relate('connect', 'p1-r1-3', 'p4-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-2')
        self.relate('connect', 'p1-r1-4', 'p3-r1-3')
        self.relate('connect', 'p1-r1-4', 'p4-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
        self.relate('connect', 'p2-r1-3', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
