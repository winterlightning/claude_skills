"""Independent 32px profile of car-horn.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '6e120b10-f09c-4f71-9e1d-244b8eb9fd47'
SOURCE_PATH = 'pictographic-primitives/transportation/horn_6e120b10-f09c-4f71-9e1d-244b8eb9fd47.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6e120b10-f09c-4f71-9e1d-244b8eb9fd47', 'pictographic-primitives/transportation/horn_6e120b10-f09c-4f71-9e1d-244b8eb9fd47.svg'),)
PROFILE_SOURCE_KEYS = ('solo/car-horn',)
SOLO_SOURCE_ICON_IDS = ('car-horn',)
REFERENCE_EXPORT_SHA256 = 'af3318d9d06e136eac0f445c02586cb0e8e0dea711af5402a7a29813dfad5498'

class Drawing(Sub32):
    icon_id = 'car-horn-sub32'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Car horn: trumpet bell, a bar into the cup, two sound dashes 8 units apart above it.
        self.add_polyline('bell', (2, 9), (12, 16), (2, 23), closed=True)
        self.add_line('bar', (12, 16), (30, 16))
        self.add_line('cup-1', (19, 16), (19, 20))
        self.add_arc('cup-2', (19, 20), (23, 24), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('cup-3', (23, 24), (27, 20), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('cup-4', (27, 20), (27, 16))
        self.add_contour('cup', 'cup-1', 'cup-2', 'cup-3', 'cup-4')
        self.add_line('dash-1', (16, 8), (19, 8))
        self.add_line('dash-2', (27, 8), (30, 8))
        self.relate('connect', 'bell', 'bar')
        self.relate('connect', 'bar', 'cup')
