"""Independent 32px profile of lit-pillar-candle-5f3444ae-892d-4884-834e-0ac133b299e6.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5f3444ae-892d-4884-834e-0ac133b299e6'
SOURCE_PATH = 'pictographic-primitives/lights/candle_5f3444ae-892d-4884-834e-0ac133b299e6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5f3444ae-892d-4884-834e-0ac133b299e6', 'pictographic-primitives/lights/candle_5f3444ae-892d-4884-834e-0ac133b299e6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/lit-pillar-candle-5f3444ae-892d-4884-834e-0ac133b299e6',)
SOLO_SOURCE_ICON_IDS = ('lit-pillar-candle-5f3444ae-892d-4884-834e-0ac133b299e6',)
REFERENCE_EXPORT_SHA256 = 'a7c0c4d42ff463a01d521cd8753d73961b3e01b37343f118311c023e902946d7'

class DrawingVariant2(Sub32):
    icon_id = 'lit-pillar-candle-5f3444ae-892d-4884-834e-0ac133b299e6-sub32-v2'
    variant_of = 'lit-pillar-candle-5f3444ae-892d-4884-834e-0ac133b299e6-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/lighting'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (16, 2), (19, 7))
        self.add_bezier('p1-r1-2', (19, 7), ((20.2, 9), (20, 13), (16, 13)))
        self.add_bezier('p1-r1-3', (16, 13), ((12, 13), (11.8, 9), (13, 7)))
        self.add_line('p1-r1-4', (13, 7), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (16, 13), (16, 19))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (8, 19), (16, 19))
        self.add_line('p3-r1-2', (16, 19), (24, 19))
        self.add_arc('p3-r1-3', (24, 19), (short_high, 22), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-4', (short_high, 22), (short_high, 30))
        self.add_line('p3-r1-5', (short_high, 30), (short_low, 30))
        self.add_line('p3-r1-6', (short_low, 30), (short_low, 22))
        self.add_arc('p3-r1-7', (short_low, 22), (8, 19), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
