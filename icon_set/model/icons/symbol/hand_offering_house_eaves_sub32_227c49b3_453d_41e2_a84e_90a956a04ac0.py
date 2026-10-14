"""Independent 32px profile of hand-offering-house-eaves.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '227c49b3-453d-41e2-a84e-90a956a04ac0'
SOURCE_PATH = 'pictographic-primitives/symbol/give hand with house_227c49b3-453d-41e2-a84e-90a956a04ac0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('227c49b3-453d-41e2-a84e-90a956a04ac0', 'pictographic-primitives/symbol/give hand with house_227c49b3-453d-41e2-a84e-90a956a04ac0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hand-offering-house-eaves',)
SOLO_SOURCE_ICON_IDS = ('hand-offering-house-eaves',)
REFERENCE_EXPORT_SHA256 = '54ad0f91540c96948f3193918656670bd81594c88b9566b708b3f527f5e96d73'

class Drawing(Sub32):
    icon_id = 'hand-offering-house-eaves-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Hand offering a house: small house held above an open palm with the fingers curling up.
        self.add_polyline('house', (10, 7), (16, 2), (22, 7), (22, 12), (10, 12), closed=True)
        self.add_line('h-1', (2, 22), (22, 22))
        self.add_line('h-2', (22, 22), (30, 16))
        self.add_line('h-3', (30, 16), (30, 26))
        self.add_arc('h-4', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('h-5', (26, 30), (2, 30))
        self.add_line('h-6', (2, 30), (2, 22))
        self.add_contour('hand', 'h-1', 'h-2', 'h-3', 'h-4', 'h-5', 'h-6', closed=True)
