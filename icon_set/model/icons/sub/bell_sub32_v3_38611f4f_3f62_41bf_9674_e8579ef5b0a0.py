# Centerline repair: continuous intended straight runs and matched tangent directions.
# Variant of bell-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of bell.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '38611f4f-3f62-41bf-9674-e8579ef5b0a0'
SOURCE_PATH = 'pictographic-primitives/symbol/bell_38611f4f-3f62-41bf-9674-e8579ef5b0a0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('38611f4f-3f62-41bf-9674-e8579ef5b0a0', 'pictographic-primitives/symbol/bell_38611f4f-3f62-41bf-9674-e8579ef5b0a0.svg'), ('77ec3808-7ec4-4c77-9f4e-0bb8e7476863', 'pictographic-primitives/symbol/bell_77ec3808-7ec4-4c77-9f4e-0bb8e7476863.svg'))
PROFILE_SOURCE_KEYS = ('solo/bell', 'solo/bell-77ec3808')
SOLO_SOURCE_ICON_IDS = ('bell', 'bell-77ec3808')
REFERENCE_EXPORT_SHA256 = 'de26374281622a462fb648af7bf94525e67a93020cae8059b3b3f49488864bc9'

class DrawingVariant3(Sub32):
    icon_id = 'bell-sub32-v3'
    variant_label = 'Continuous centerlines'
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
        self.add_arc('p1-r1-1', (16, 5), (24, 13), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-2', (24, 13), ((24, 17), (short_high, 18), (short_high, 21)))
        self.add_arc('p1-r1-3', (short_high, 21), (26, 23), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (26, 23), (20, 23))
        self.add_line('p1-r1-5', (20, 23), (12, 23))
        self.add_line('p1-r1-6', (12, 23), (6, 23))
        self.add_arc('p1-r1-7', (6, 23), (short_low, 21), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-8', (short_low, 21), ((short_low, 18), (8, 17), (8, 13)))
        self.add_arc('p1-r1-9', (8, 13), (16, 5), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 5))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (20, 23), (12, 23), radius_x=4, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
