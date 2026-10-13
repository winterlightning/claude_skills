"""Independent 32px profile of sailboat-on-waves.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b61a055f-e1d4-4f45-b688-2b287b42a5a9'
SOURCE_PATH = 'pictographic-primitives/transportation/boat_b61a055f-e1d4-4f45-b688-2b287b42a5a9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b61a055f-e1d4-4f45-b688-2b287b42a5a9', 'pictographic-primitives/transportation/boat_b61a055f-e1d4-4f45-b688-2b287b42a5a9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sailboat-on-waves',)
SOLO_SOURCE_ICON_IDS = ('sailboat-on-waves',)
REFERENCE_EXPORT_SHA256 = 'fec85ca6fedf2946d8cb6262f7bf95cb55612b2eeb73d94abf3aa1b958406cc7'

class Drawing(Sub32):
    icon_id = 'sailboat-on-waves-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 2), (11, 14))
        self.add_line('p1-r1-2', (11, 14), (24, 14))
        self.add_bezier('p1-r1-3', (24, 14), ((24, 11), (22, 8), (20, 6)))
        self.add_bezier('p1-r1-4', (20, 6), ((18, 3), (15, 2), (11, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 19), (7, 21))
        self.add_line('p2-r1-2', (7, 21), (25, 21))
        self.add_line('p2-r1-3', (25, 21), (30, 19))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (2, 29), (16, 29), radius_x=12, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (16, 29), (30, 29), radius_x=12, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
