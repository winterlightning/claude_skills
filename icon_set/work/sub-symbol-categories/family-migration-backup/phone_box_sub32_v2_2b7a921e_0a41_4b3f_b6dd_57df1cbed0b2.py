# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of phone-box.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2b7a921e-0a41-4b3f-b6dd-57df1cbed0b2'
SOURCE_PATH = 'pictographic-primitives/symbol/phone box_2b7a921e-0a41-4b3f-b6dd-57df1cbed0b2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2b7a921e-0a41-4b3f-b6dd-57df1cbed0b2', 'pictographic-primitives/symbol/phone box_2b7a921e-0a41-4b3f-b6dd-57df1cbed0b2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/phone-box',)
SOLO_SOURCE_ICON_IDS = ('phone-box',)
REFERENCE_EXPORT_SHA256 = 'fea5bd1a665c33a146ddb00058cc960de11ee61e9b8cf08974573be174c5e42a'

class DrawingVariant2(Sub32):
    icon_id = 'phone-box-sub32-v2'
    variant_of = 'phone-box-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_arc('p1-r1-1', (short_low, 13), (16, 2), radius_x=12, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (short_high, 13), radius_x=12, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (short_low, 30), (short_low, 13))
        self.add_line('p2-r1-2', (short_low, 13), (short_high, 13))
        self.add_line('p2-r1-3', (short_high, 13), (short_high, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (16, 20), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
