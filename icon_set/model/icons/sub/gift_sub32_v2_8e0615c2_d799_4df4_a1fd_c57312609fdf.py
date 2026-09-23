# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of gift.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '8e0615c2-d799-4df4-a1fd-c57312609fdf'
SOURCE_PATH = 'pictographic-primitives/holidays/gift_8e0615c2-d799-4df4-a1fd-c57312609fdf.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8e0615c2-d799-4df4-a1fd-c57312609fdf', 'pictographic-primitives/holidays/gift_8e0615c2-d799-4df4-a1fd-c57312609fdf.svg'),)
PROFILE_SOURCE_KEYS = ('solo/gift',)
SOLO_SOURCE_ICON_IDS = ('gift',)
REFERENCE_EXPORT_SHA256 = '2272fb7a9add11c0527b1458260875f82bd5e79e5dd4106654a16189ffe362b5'

class DrawingVariant2(Sub32):
    icon_id = 'gift-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'holidays'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (6, 11), (16, 11))
        self.add_line('p1-r1-2', (16, 11), (26, 11))
        self.add_line('p1-r1-3', (26, 11), (26, 30))
        self.add_line('p1-r1-4', (26, 30), (6, 30))
        self.add_line('p1-r1-5', (6, 30), (6, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (short_low, 11), (6, 11))
        self.add_line('p2-r1-2', (6, 11), (16, 11))
        self.add_line('p2-r1-3', (16, 11), (26, 11))
        self.add_line('p2-r1-4', (26, 11), (short_high, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (16, 11), ((11, 11), (8, 10), (8, 6)))
        self.add_bezier('p3-r1-2', (8, 6), ((8, 3), (9, 2), (11, 2)))
        self.add_bezier('p3-r1-3', (11, 2), ((15, 2), (16, 8), (16, 11)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_bezier('p4-r1-1', (16, 11), ((16, 8), (17, 2), (21, 2)))
        self.add_bezier('p4-r1-2', (21, 2), ((23, 2), (24, 3), (24, 6)))
        self.add_bezier('p4-r1-3', (24, 6), ((24, 10), (21, 11), (16, 11)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-3')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-4')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-3')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-3')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-3')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-3')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-3')
        self.relate('connect', 'p2-r1-3', 'p4-r1-1')
        self.relate('connect', 'p2-r1-3', 'p4-r1-3')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-3')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-3')
