# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of ghost.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a257f108-5e8d-40d4-97ad-643846319b7b'
SOURCE_PATH = 'pictographic-primitives/symbol/ghost_a257f108-5e8d-40d4-97ad-643846319b7b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a257f108-5e8d-40d4-97ad-643846319b7b', 'pictographic-primitives/symbol/ghost_a257f108-5e8d-40d4-97ad-643846319b7b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ghost',)
SOLO_SOURCE_ICON_IDS = ('ghost',)
REFERENCE_EXPORT_SHA256 = '6060ec47344bdb9577b363215c76cbfc21c9c01af9fd1470f54d160065400f0e'

class DrawingVariant2(Sub32):
    icon_id = 'ghost-sub32-v2'
    variant_of = 'ghost-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (short_low, 24), (short_low, 13))
        self.add_arc('p1-r1-2', (short_low, 13), (16, 2), radius_x=12, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 2), (short_high, 13), radius_x=12, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (short_high, 13), (short_high, 24))
        self.add_bezier('p1-r1-5', (short_high, 24), ((short_high, 27), (short_high, 30), (24, 30)))
        self.add_bezier('p1-r1-6', (24, 30), ((22, 30), (22, 27), (20, 27)))
        self.add_bezier('p1-r1-7', (20, 27), ((18, 27), (18, 30), (16, 30)))
        self.add_bezier('p1-r1-8', (16, 30), ((14, 30), (14, 27), (12, 27)))
        self.add_bezier('p1-r1-9', (12, 27), ((10, 27), (10, 30), (8, 30)))
        self.add_bezier('p1-r1-10', (8, 30), ((short_low, 30), (short_low, 27), (short_low, 24)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
