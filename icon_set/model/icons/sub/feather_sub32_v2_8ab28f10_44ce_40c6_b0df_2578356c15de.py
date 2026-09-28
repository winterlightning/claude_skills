# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of feather.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '8ab28f10-44ce-40c6-b0df-2578356c15de'
SOURCE_PATH = 'pictographic-primitives/symbol/feather_8ab28f10-44ce-40c6-b0df-2578356c15de.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8ab28f10-44ce-40c6-b0df-2578356c15de', 'pictographic-primitives/symbol/feather_8ab28f10-44ce-40c6-b0df-2578356c15de.svg'),)
PROFILE_SOURCE_KEYS = ('solo/feather',)
SOLO_SOURCE_ICON_IDS = ('feather',)
REFERENCE_EXPORT_SHA256 = '306d142b45ce3c96f1e95efb9fa40788b4c3337c6868db586959fae3d43ad148'

class DrawingVariant2(Sub32):
    icon_id = 'feather-sub32-v2'
    variant_of = 'feather-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_bezier('p1-r1-1', (8, 24), ((6, 22), (short_low, 20), (short_low, 17)))
        self.add_bezier('p1-r1-2', (short_low, 17), ((short_low, 10), (18, 4), (26, 2)))
        self.add_bezier('p1-r1-3', (26, 2), ((short_high, 4), (short_high, 6), (short_high, 8)))
        self.add_bezier('p1-r1-4', (short_high, 8), ((short_high, 13), (23, 16), (20, 18)))
        self.add_bezier('p1-r1-5', (20, 18), ((20, 22), (16, 25), (12, 25)))
        self.add_bezier('p1-r1-6', (12, 25), ((11, 25), (10, 26), (8, 24)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (short_low, 30), (8, 24))
        self.add_line('p2-r1-2', (8, 24), (16, 12))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-2')
