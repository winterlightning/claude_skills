# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of dna.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b4ea616c-9fe4-40b2-ab7c-11c82b439358'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/dna_b4ea616c-9fe4-40b2-ab7c-11c82b439358.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b4ea616c-9fe4-40b2-ab7c-11c82b439358', 'pictographic-primitives/artificial-intelligence/dna_b4ea616c-9fe4-40b2-ab7c-11c82b439358.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dna',)
SOLO_SOURCE_ICON_IDS = ('dna',)
REFERENCE_EXPORT_SHA256 = '7db5f99141f12a42d646294f38bdb1222ec98b9dbe2e6ab804818860f265ef57'

class DrawingVariant2(Sub32):
    icon_id = 'dna-sub32-v2'
    variant_of = 'dna-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'artificial-intelligence'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_bezier('p1-r1-1', (short_low, 2), ((short_low, 9), (10, 13), (16, 16)))
        self.add_bezier('p1-r1-2', (16, 16), ((22, 19), (short_high, 23), (short_high, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (short_high, 2), ((short_high, 9), (22, 13), (16, 16)))
        self.add_bezier('p2-r1-2', (16, 16), ((10, 19), (short_low, 23), (short_low, 30)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (short_low, 2), (short_high, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (short_low, 30), (short_high, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
