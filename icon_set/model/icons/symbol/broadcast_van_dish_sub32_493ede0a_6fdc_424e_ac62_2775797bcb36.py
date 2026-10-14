"""Independent 32px profile of broadcast-van-dish.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '493ede0a-6fdc-424e-ac62-2775797bcb36'
SOURCE_PATH = 'pictographic-primitives/symbol/radio van_493ede0a-6fdc-424e-ac62-2775797bcb36.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('493ede0a-6fdc-424e-ac62-2775797bcb36', 'pictographic-primitives/symbol/radio van_493ede0a-6fdc-424e-ac62-2775797bcb36.svg'),)
PROFILE_SOURCE_KEYS = ('solo/broadcast-van-dish',)
SOLO_SOURCE_ICON_IDS = ('broadcast-van-dish',)
REFERENCE_EXPORT_SHA256 = '248828e4eaffce2711a67afdde9dace5fc00aa2c6e17093d6f7c447cfd225b25'

class Drawing(Sub32):
    icon_id = 'broadcast-van-dish-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Broadcast van: body with a slanted front and two wheel arches in its base, a dish on a mast.
        self.add_line('v-1', (2, 27), (2, 21))
        self.add_line('v-2', (2, 21), (5, 18))
        self.add_line('v-3', (5, 18), (30, 18))
        self.add_line('v-4', (30, 18), (30, 27))
        self.add_line('v-5', (30, 27), (26, 27))
        self.add_arc('wheel-r', (26, 27), (20, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('v-6', (20, 27), (12, 27))
        self.add_arc('wheel-l', (12, 27), (6, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('v-7', (6, 27), (2, 27))
        self.add_contour('body', 'v-1', 'v-2', 'v-3', 'v-4', 'v-5', 'wheel-r', 'v-6', 'wheel-l', 'v-7', closed=True)
        self.add_arc('dish', (10, 2), (22, 2), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('mast', (16, 8), (16, 18))
        self.relate('connect', 'dish', 'mast')
        self.relate('connect', 'body', 'mast')
