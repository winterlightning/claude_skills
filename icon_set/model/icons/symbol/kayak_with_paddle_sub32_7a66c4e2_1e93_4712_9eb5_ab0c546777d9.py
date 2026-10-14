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
    categories = ('transportation', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Adopted from the production stroke edit (Browser Edit by hina).
        self.add_bezier('p1-r1-1', (30, 2), ((20, 2), (15, 6), (10, 10)))
        self.add_bezier('p1-r1-2', (10, 10), ((6, 15), (2, 20), (2, 30)))
        self.add_bezier('p1-r1-3', (2, 30), ((12, 30), (17, 25), (22, 21)))
        self.add_bezier('p1-r1-4', (22, 21), ((26, 16), (30, 12), (30, 2)))
        self.add_arc('p2-r1-1', (6, 4), (4, 6), radius_x=2, radius_y=2, large_arc=True, sweep=False)
        self.add_line('p2-r1-2', (4, 6), (6, 6))
        self.add_line('p2-r1-3', (6, 6), (6, 4))
        self.add_arc('p3-r1-1', (26, 28), (28, 26), radius_x=2, radius_y=2, large_arc=True, sweep=False)
        self.add_line('p3-r1-2', (28, 26), (26, 26))
        self.add_line('p3-r1-3', (26, 26), (26, 28))
        self.add_line('p4-r1-1', (6, 6), (26, 26))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
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
        # Declared joints: these strokes meet or cross on purpose.
        self.relate('connect', 'path-1-1', 'path-4-1')
