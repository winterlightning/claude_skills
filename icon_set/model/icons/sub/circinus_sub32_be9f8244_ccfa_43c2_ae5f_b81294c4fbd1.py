"""Independent 32px profile of circinus.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'be9f8244-ccfa-43c2-ae5f-b81294c4fbd1'
SOURCE_PATH = 'pictographic-primitives/state/circinus_be9f8244-ccfa-43c2-ae5f-b81294c4fbd1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('be9f8244-ccfa-43c2-ae5f-b81294c4fbd1', 'pictographic-primitives/state/circinus_be9f8244-ccfa-43c2-ae5f-b81294c4fbd1.svg'), ('f18957c4-d496-4dcc-baef-4934631bc063', 'pictographic-primitives/state/circinus_f18957c4-d496-4dcc-baef-4934631bc063.svg'))
PROFILE_SOURCE_KEYS = ('solo/circinus', 'solo/circinus-state')
SOLO_SOURCE_ICON_IDS = ('circinus', 'circinus-state')
REFERENCE_EXPORT_SHA256 = '61055bf0f80c248bfafae792ce040276c3b0d47254c65e00b81e9a868d56b903'

class Drawing(Sub32):
    icon_id = 'circinus-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 8), (28, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (28, 8), (16, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (27, 4), (30, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (18, 13), (2, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (24, 14), (18, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (12, 17), (21, 22))
        self.add_line('p5-r1-2', (21, 22), (25, 24))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
