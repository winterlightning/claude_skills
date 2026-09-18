"""Independent 32px profile of right-reverse-turn-ahead.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '182f0248-c380-4521-a855-6c9c834f593d'
SOURCE_PATH = 'pictographic-primitives/transportation/right reverse turn ahead_182f0248-c380-4521-a855-6c9c834f593d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('182f0248-c380-4521-a855-6c9c834f593d', 'pictographic-primitives/transportation/right reverse turn ahead_182f0248-c380-4521-a855-6c9c834f593d.svg'), ('7740d388-2c2b-4378-bd9e-8bad227a64cf', 'pictographic-primitives/symbol/right reverse turn ahead 1_7740d388-2c2b-4378-bd9e-8bad227a64cf.svg'))
PROFILE_SOURCE_KEYS = ('solo/right-reverse-turn-ahead', 'solo/right-reverse-turn-ahead-1')
SOLO_SOURCE_ICON_IDS = ('right-reverse-turn-ahead', 'right-reverse-turn-ahead-1')
REFERENCE_EXPORT_SHA256 = '23dcd9fcf93e26503b6d2a96b9228733305a07fe47828e47ca8a3752d0bd5645'

class Drawing(Sub32):
    icon_id = 'right-reverse-turn-ahead-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 30), (5, 15))
        self.add_line('p1-r1-2', (5, 15), (20, 15))
        self.add_line('p1-r1-3', (20, 15), (20, 2))
        self.add_line('p1-r1-4', (20, 2), (14, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (20, 2), (27, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
