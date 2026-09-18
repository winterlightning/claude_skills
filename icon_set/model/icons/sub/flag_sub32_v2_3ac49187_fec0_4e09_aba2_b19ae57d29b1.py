"""Independent 32px profile of flag.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3ac49187-fec0-4e09-aba2-b19ae57d29b1'
SOURCE_PATH = 'pictographic-primitives/social/flag_3ac49187-fec0-4e09-aba2-b19ae57d29b1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3ac49187-fec0-4e09-aba2-b19ae57d29b1', 'pictographic-primitives/social/flag_3ac49187-fec0-4e09-aba2-b19ae57d29b1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flag',)
SOLO_SOURCE_ICON_IDS = ('flag',)
REFERENCE_EXPORT_SHA256 = 'da12d6216d72f07d2d547a551af2902c8d08e57dd8be3314ac2c129b92bfbd0d'

class DrawingVariant2(Sub32):
    icon_id = 'flag-sub32-v2'
    variant_of = 'flag-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'social'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (8, 2), (8, 5))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (short_low, 30), (10, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (8, 5), ((10, 4), (12, 4), (15, 4)))
        self.add_bezier('p3-r1-2', (15, 4), ((17, 4), (18, 5), (21, 5)))
        self.add_bezier('p3-r1-3', (21, 5), ((24, 5), (26, 5), (28, 4)))
        self.add_line('p3-r1-4', (short_high, 4), (short_high, 15))
        self.add_bezier('p3-r1-5', (28, 15), ((26, 16), (24, 16), (21, 16)))
        self.add_bezier('p3-r1-6', (21, 16), ((18, 16), (17, 15), (15, 15)))
        self.add_bezier('p3-r1-7', (15, 15), ((12, 15), (10, 15), (8, 16)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
        self.add_line('p4-r1-1', (8, 5), (8, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (8, 16), (8, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-7', 'p4-r1-1')
        self.relate('connect', 'p3-r1-7', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
