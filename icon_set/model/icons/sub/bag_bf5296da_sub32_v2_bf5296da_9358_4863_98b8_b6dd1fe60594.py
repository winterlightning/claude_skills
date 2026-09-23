# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of bag-bf5296da.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'bf5296da-9358-4863-98b8-b6dd1fe60594'
SOURCE_PATH = 'pictographic-primitives/photography/bag_bf5296da-9358-4863-98b8-b6dd1fe60594.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bf5296da-9358-4863-98b8-b6dd1fe60594', 'pictographic-primitives/photography/bag_bf5296da-9358-4863-98b8-b6dd1fe60594.svg'), ('e213494f-7bcb-44b0-a54e-8a069e24c6ea', 'pictographic-primitives/shopping/bag_e213494f-7bcb-44b0-a54e-8a069e24c6ea.svg'))
PROFILE_SOURCE_KEYS = ('solo/bag-bf5296da', 'solo/bag-e213494f')
SOLO_SOURCE_ICON_IDS = ('bag-bf5296da', 'bag-e213494f')
REFERENCE_EXPORT_SHA256 = 'f8984b6f8ad8c4ba37ca4ae88c4a981fc5236f9bad4541f8aebd346099ebddd3'

class DrawingVariant2(Sub32):
    icon_id = 'bag-bf5296da-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'photography'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (12, 10), (12, 6))
        self.add_arc('p1-r1-2', (12, 6), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (20, 6), (20, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (8, 10), (12, 10))
        self.add_line('p2-r1-2', (12, 10), (20, 10))
        self.add_line('p2-r1-3', (20, 10), (24, 10))
        self.add_line('p2-r1-4', (24, 10), (short_high, 30))
        self.add_line('p2-r1-5', (short_high, 30), (short_low, 30))
        self.add_line('p2-r1-6', (short_low, 30), (8, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
