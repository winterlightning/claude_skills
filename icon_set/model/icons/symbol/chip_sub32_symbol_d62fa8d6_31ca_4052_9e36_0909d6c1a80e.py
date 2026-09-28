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
        self.add_line('p1-r1-1', (8, 8), (24, 8))
        self.add_line('p1-r1-2', (24, 8), (24, 24))
        self.add_line('p1-r1-3', (24, 24), (8, 24))
        self.add_line('p1-r1-4', (8, 24), (8, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (13, 2), (13, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 24), (13, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 13), (8, 13))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (24, 13), (30, 13))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (19, 2), (19, 8))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (19, 24), (19, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (2, 19), (8, 19))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (24, 19), (30, 19))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
