"""Independent 32px profile of cracked-shield.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '83e2a7c2-7e92-57f9-a0d4-a9b2bd0095d5'
SOURCE_PATH = 'pictographic-primitives/protection/cracked shield_83e2a7c2-7e92-57f9-a0d4-a9b2bd0095d5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('83e2a7c2-7e92-57f9-a0d4-a9b2bd0095d5', 'pictographic-primitives/protection/cracked shield_83e2a7c2-7e92-57f9-a0d4-a9b2bd0095d5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cracked-shield',)
SOLO_SOURCE_ICON_IDS = ('cracked-shield',)
REFERENCE_EXPORT_SHA256 = '1d59bc02b0a1c183966450ad1ec0fbdf13e9860e24fcc2cb0762993957ddd17e'

class DrawingVariant2(Sub32):
    icon_id = 'cracked-shield-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'protection'
    categories = ('protection', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (16, 2), (10, 5))
        self.add_bezier('p1-r1-2', (10, 5), ((8, 6), (6, 6), (4, 6)))
        self.add_line('p1-r1-3', (short_low, 6), (short_low, 15))
        self.add_bezier('p1-r1-4', (4, 15), ((4, 22), (10, 28), (16, 30)))
        self.add_bezier('p1-r1-5', (16, 30), ((22, 28), (28, 22), (28, 15)))
        self.add_line('p1-r1-6', (short_high, 15), (short_high, 6))
        self.add_bezier('p1-r1-7', (28, 6), ((26, 6), (24, 6), (22, 5)))
        self.add_line('p1-r1-8', (22, 5), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (22, 5), (15, 13))
        self.add_line('p2-r1-2', (15, 13), (20, 16))
        self.add_line('p2-r1-3', (20, 16), (15, 24))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
