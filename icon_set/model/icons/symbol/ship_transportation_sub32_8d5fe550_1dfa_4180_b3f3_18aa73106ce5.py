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
        # Ship: hull with a cabin on deck.
        self.add_polyline('hull', (2, 20), (30, 20), (24, 28), (8, 28), closed=True)
        self.add_polyline('cabin', (10, 20), (10, 8), (22, 8), (22, 20))
        self.add_line('funnel', (16, 8), (16, 4))
        self.relate('connect', 'hull', 'cabin')
        self.relate('connect', 'cabin', 'funnel')
