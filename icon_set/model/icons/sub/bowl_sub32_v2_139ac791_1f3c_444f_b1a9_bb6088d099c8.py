# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of bowl.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '139ac791-1f3c-444f-b1a9-bb6088d099c8'
SOURCE_PATH = 'pictographic-primitives/symbol/bowl_139ac791-1f3c-444f-b1a9-bb6088d099c8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('139ac791-1f3c-444f-b1a9-bb6088d099c8', 'pictographic-primitives/symbol/bowl_139ac791-1f3c-444f-b1a9-bb6088d099c8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bowl',)
SOLO_SOURCE_ICON_IDS = ('bowl',)
REFERENCE_EXPORT_SHA256 = 'd5a58f567b88873f86f321d705a87d6e917eb64d80c65d3f478526718fc4b819'

class DrawingVariant2(Sub32):
    icon_id = 'bowl-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, short_low), (30, short_low))
        self.add_bezier('p1-r1-2', (30, short_low), ((30, 13), (26, 19), (22, 22)))
        self.add_line('p1-r1-3', (22, 22), (22, short_high))
        self.add_line('p1-r1-4', (22, short_high), (10, short_high))
        self.add_line('p1-r1-5', (10, short_high), (10, 22))
        self.add_bezier('p1-r1-6', (10, 22), ((6, 19), (2, 13), (2, short_low)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
