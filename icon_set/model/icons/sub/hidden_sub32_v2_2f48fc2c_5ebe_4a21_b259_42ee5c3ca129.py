# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of hidden.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2f48fc2c-5ebe-4a21-b259-42ee5c3ca129'
SOURCE_PATH = 'pictographic-primitives/symbol/hidden_2f48fc2c-5ebe-4a21-b259-42ee5c3ca129.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2f48fc2c-5ebe-4a21-b259-42ee5c3ca129', 'pictographic-primitives/symbol/hidden_2f48fc2c-5ebe-4a21-b259-42ee5c3ca129.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hidden',)
SOLO_SOURCE_ICON_IDS = ('hidden',)
REFERENCE_EXPORT_SHA256 = '887e49d709ee5b7b152870a6bfa100d7d2263b4d65ff8450edfa3a8fea9c5cbf'

class DrawingVariant2(Sub32):
    icon_id = 'hidden-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_bezier('p1-r1-1', (2, 16), ((4, 12), (6, 10), (9, 8)))
        self.add_bezier('p1-r1-2', (9, 8), ((12, 6), (13, short_low), (16, short_low)))
        self.add_bezier('p1-r1-3', (16, short_low), ((19, short_low), (20, 6), (23, 8)))
        self.add_bezier('p1-r1-4', (23, 8), ((26, 10), (28, 12), (30, 16)))
        self.add_bezier('p1-r1-5', (30, 16), ((28, 20), (26, 22), (23, 24)))
        self.add_bezier('p1-r1-6', (23, 24), ((20, 26), (19, short_high), (16, short_high)))
        self.add_bezier('p1-r1-7', (16, short_high), ((13, short_high), (12, 26), (9, 24)))
        self.add_bezier('p1-r1-8', (9, 24), ((6, 22), (4, 20), (2, 16)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (9, 8), (23, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
