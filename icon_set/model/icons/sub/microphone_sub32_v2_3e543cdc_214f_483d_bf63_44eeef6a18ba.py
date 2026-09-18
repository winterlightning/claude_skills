# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of microphone.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3e543cdc-214f-483d-bf63-44eeef6a18ba'
SOURCE_PATH = 'pictographic-primitives/audio/microphone_3e543cdc-214f-483d-bf63-44eeef6a18ba.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3e543cdc-214f-483d-bf63-44eeef6a18ba', 'pictographic-primitives/audio/microphone_3e543cdc-214f-483d-bf63-44eeef6a18ba.svg'), ('88610259-450b-43f2-85da-95879335b5f2', 'pictographic-primitives/audio/microphone_88610259-450b-43f2-85da-95879335b5f2.svg'), ('b72da6ab-adc1-4364-be21-8572894c8a90', 'pictographic-primitives/audio/microphone_b72da6ab-adc1-4364-be21-8572894c8a90.svg'))
PROFILE_SOURCE_KEYS = ('solo/microphone', 'solo/microphone-88610259', 'solo/microphone-b72da6ab')
SOLO_SOURCE_ICON_IDS = ('microphone', 'microphone-88610259', 'microphone-b72da6ab')
REFERENCE_EXPORT_SHA256 = '7edbc7992535f7d8f7f630a53f85164a2fefd0cd145278503f584a88b3a90a40'

class DrawingVariant2(Sub32):
    icon_id = 'microphone-sub32-v2'
    variant_of = 'microphone-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'audio'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (16, 2), (16, 2))
        self.add_arc('p1-r1-2', (16, 2), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (20, 6), (20, 15))
        self.add_arc('p1-r1-4', (20, 15), (16, 19), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (16, 19), (16, 19))
        self.add_arc('p1-r1-6', (16, 19), (12, 15), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (12, 15), (12, 6))
        self.add_arc('p1-r1-8', (12, 6), (16, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (short_low, 17), (short_low, 19))
        self.add_arc('p2-r1-2', (short_low, 19), (16, 27), radius_x=12, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('p2-r1-3', (16, 27), (short_high, 19), radius_x=12, radius_y=8, large_arc=False, sweep=False)
        self.add_line('p2-r1-4', (short_high, 19), (short_high, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (16, 27), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
