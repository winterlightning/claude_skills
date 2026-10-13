"""Independent 32px profile of ball-with-lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '02c70f52-9dee-4f13-8c03-a5f8a38f8a84'
SOURCE_PATH = 'pictographic-primitives/symbol/ball with lines_02c70f52-9dee-4f13-8c03-a5f8a38f8a84.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('02c70f52-9dee-4f13-8c03-a5f8a38f8a84', 'pictographic-primitives/symbol/ball with lines_02c70f52-9dee-4f13-8c03-a5f8a38f8a84.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ball-with-lines',)
SOLO_SOURCE_ICON_IDS = ('ball-with-lines',)
REFERENCE_EXPORT_SHA256 = 'edcaccf2aa1dcf1b62b748fabe78aa61fd55ee72354fec029f28633d12128f1c'

class Drawing(Sub32):
    icon_id = 'ball-with-lines-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Soccer ball: ring, a centre hexagon and six spokes running straight out to the ring.
        self.add_arc('r-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('r-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('ring', 'r-1', 'r-2', closed=True)
        self.add_polyline('hex', (16, 10), (21, 13), (21, 19), (16, 22), (11, 19), (11, 13), closed=True)
        spokes = (((16, 10), (16, 2)), ((21, 13), (28, 9)), ((21, 19), (28, 23)),
                  ((16, 22), (16, 30)), ((11, 19), (4, 23)), ((11, 13), (4, 9)))
        for k, (a, b) in enumerate(spokes):
            self.add_line(f'spoke-{k}', a, b)
            self.relate('connect', 'hex', f'spoke-{k}')
            self.relate('connect', 'ring', f'spoke-{k}')
