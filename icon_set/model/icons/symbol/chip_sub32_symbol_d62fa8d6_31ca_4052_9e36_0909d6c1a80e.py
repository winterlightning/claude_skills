"""Independent 32px profile of chip.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'd62fa8d6-31ca-4052-9e36-0909d6c1a80e'
SOURCE_PATH = 'pictographic-primitives/state/chip_d62fa8d6-31ca-4052-9e36-0909d6c1a80e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d62fa8d6-31ca-4052-9e36-0909d6c1a80e', 'pictographic-primitives/state/chip_d62fa8d6-31ca-4052-9e36-0909d6c1a80e.svg'), ('d0dd0f52-f552-4b31-8bb1-bed37c84eff0', 'pictographic-primitives/symbol/chip_d0dd0f52-f552-4b31-8bb1-bed37c84eff0.svg'))
PROFILE_SOURCE_KEYS = ('solo/chip', 'solo/chip-symbol')
SOLO_SOURCE_ICON_IDS = ('chip', 'chip-symbol')
REFERENCE_EXPORT_SHA256 = '412d4aec8a5078c4a220a81f21eed8d171a85595b8e3b17f79e9bc208e9488a9'

class DrawingContainerSymbol(Sub32):
    icon_id = 'chip-sub32-symbol'
    related_origin_icon_id = 'chip-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/chip-sub32'
    counterpart_icon_id = 'chip-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Chip: square body with two pins on each side.
        self.add_line('body-1', (8, 6), (24, 6))
        self.add_arc('body-2', (24, 6), (26, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('body-3', (26, 8), (26, 24))
        self.add_arc('body-4', (26, 24), (24, 26), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('body-5', (24, 26), (8, 26))
        self.add_arc('body-6', (8, 26), (6, 24), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('body-7', (6, 24), (6, 8))
        self.add_arc('body-8', (6, 8), (8, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', closed=True)
        self.add_line('pin-0', (12, 2), (12, 6))
        self.relate('connect', 'body', 'pin-0')
        self.add_line('pin-1', (20, 2), (20, 6))
        self.relate('connect', 'body', 'pin-1')
        self.add_line('pin-2', (12, 26), (12, 30))
        self.relate('connect', 'body', 'pin-2')
        self.add_line('pin-3', (20, 26), (20, 30))
        self.relate('connect', 'body', 'pin-3')
        self.add_line('pin-4', (2, 12), (6, 12))
        self.relate('connect', 'body', 'pin-4')
        self.add_line('pin-5', (2, 20), (6, 20))
        self.relate('connect', 'body', 'pin-5')
        self.add_line('pin-6', (26, 12), (30, 12))
        self.relate('connect', 'body', 'pin-6')
        self.add_line('pin-7', (26, 20), (30, 20))
        self.relate('connect', 'body', 'pin-7')
