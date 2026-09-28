"""Independent 32px profile of turn-right-transportation.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b654ed27-4d6a-4c36-8d1d-071810327791'
SOURCE_PATH = 'pictographic-primitives/transportation/turn right_b654ed27-4d6a-4c36-8d1d-071810327791.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b654ed27-4d6a-4c36-8d1d-071810327791', 'pictographic-primitives/transportation/turn right_b654ed27-4d6a-4c36-8d1d-071810327791.svg'),)
PROFILE_SOURCE_KEYS = ('solo/turn-right-transportation',)
SOLO_SOURCE_ICON_IDS = ('turn-right-transportation',)
REFERENCE_EXPORT_SHA256 = '7a222b0ae69f2a72550660746000d4f97d5430d48aff0160c465af85c7d972bf'

class Drawing(Sub32):
    icon_id = 'turn-right-transportation-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (27, 8), (15, 8))
        self.add_arc('p1-r1-2', (15, 8), (5, 17), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (5, 17), (5, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (22, 2), (27, 8))
        self.add_line('p2-r1-2', (27, 8), (22, 13))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
