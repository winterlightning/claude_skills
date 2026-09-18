"""Independent 32px profile of phone-box-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'd7e72503-159f-4e5f-b0ad-c81408e24d67'
SOURCE_PATH = 'pictographic-primitives/symbol/phone box_d7e72503-159f-4e5f-b0ad-c81408e24d67.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d7e72503-159f-4e5f-b0ad-c81408e24d67', 'pictographic-primitives/symbol/phone box_d7e72503-159f-4e5f-b0ad-c81408e24d67.svg'),)
PROFILE_SOURCE_KEYS = ('solo/phone-box-symbol',)
SOLO_SOURCE_ICON_IDS = ('phone-box-symbol',)
REFERENCE_EXPORT_SHA256 = 'd928c1093260b7ecc43dbc7a29da4a63d7aee630e069bcde7ef22863308d9ad2'

class DrawingVariant2(Sub32):
    icon_id = 'phone-box-symbol-sub32-v2'
    related_origin_icon_id = 'phone-box-symbol-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_arc('p1-r1-1', (short_low, 10), (short_high, 10), radius_x=12, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (short_high, 10), (26, 10))
        self.add_line('p1-r1-3', (26, 10), (6, 10))
        self.add_line('p1-r1-4', (6, 10), (short_low, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (6, 10), (6, 20))
        self.add_line('p2-r1-2', (6, 20), (6, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (26, 10), (26, 20))
        self.add_line('p3-r1-2', (26, 20), (26, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (short_low, 30), (6, 30))
        self.add_line('p4-r1-2', (6, 30), (26, 30))
        self.add_line('p4-r1-3', (26, 30), (short_high, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.add_line('p5-r1-1', (6, 20), (26, 20))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-2')
        self.relate('connect', 'p2-r1-2', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-2')
        self.relate('connect', 'p3-r1-2', 'p4-r1-3')
        self.relate('connect', 'p3-r1-2', 'p5-r1-1')
