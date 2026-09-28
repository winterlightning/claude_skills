# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of card-fc09bb7b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'fc09bb7b-da25-41fc-9ec5-f3b12e7a09cd'
SOURCE_PATH = 'pictographic-primitives/business/card_fc09bb7b-da25-41fc-9ec5-f3b12e7a09cd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fc09bb7b-da25-41fc-9ec5-f3b12e7a09cd', 'pictographic-primitives/business/card_fc09bb7b-da25-41fc-9ec5-f3b12e7a09cd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/card-fc09bb7b',)
SOLO_SOURCE_ICON_IDS = ('card-fc09bb7b',)
REFERENCE_EXPORT_SHA256 = '13feea51af8cafb93e445945c0d9decfee24ba94db3b08899b3c3c187aa9910f'

class DrawingVariant2(Sub32):
    icon_id = 'card-fc09bb7b-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'business'
    categories = ('primitives', 'business')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (5, short_low), (27, short_low))
        self.add_arc('p1-r1-2', (27, short_low), (30, 8), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 8), (30, 19))
        self.add_line('p1-r1-4', (30, 19), (30, 24))
        self.add_arc('p1-r1-5', (30, 24), (27, short_high), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (27, short_high), (5, short_high))
        self.add_arc('p1-r1-7', (5, short_high), (2, 24), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (2, 24), (2, 19))
        self.add_line('p1-r1-9', (2, 19), (2, 8))
        self.add_arc('p1-r1-10', (2, 8), (5, short_low), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (2, 19), (30, 19))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (9, 12), (9, 12))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 12), (16, 12))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
