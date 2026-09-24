# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of cloud.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '1a5b10c5-e3d9-4568-9b2c-8d04c5b409cd'
SOURCE_PATH = 'pictographic-primitives/internet/cloud_1a5b10c5-e3d9-4568-9b2c-8d04c5b409cd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1a5b10c5-e3d9-4568-9b2c-8d04c5b409cd', 'pictographic-primitives/internet/cloud_1a5b10c5-e3d9-4568-9b2c-8d04c5b409cd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cloud',)
SOLO_SOURCE_ICON_IDS = ('cloud',)
REFERENCE_EXPORT_SHA256 = '92d6f7aa5f112153455bbef090004fb08fac8d48ea6f7685b095906911cde5f6'

class DrawingVariant2(Sub32):
    icon_id = 'cloud-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'internet'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_bezier('p1-r1-1', (9, short_high), ((5, short_high), (2, 24), (2, 20)))
        self.add_bezier('p1-r1-2', (2, 20), ((2, 15), (6, 14), (8, 12)))
        self.add_bezier('p1-r1-3', (8, 12), ((10, 10), (11, short_low), (16, short_low)))
        self.add_bezier('p1-r1-4', (16, short_low), ((21, short_low), (22, 10), (24, 12)))
        self.add_bezier('p1-r1-5', (24, 12), ((26, 14), (30, 15), (30, 20)))
        self.add_bezier('p1-r1-6', (30, 20), ((30, 24), (27, short_high), (23, short_high)))
        self.add_line('p1-r1-7', (23, short_high), (9, short_high))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
