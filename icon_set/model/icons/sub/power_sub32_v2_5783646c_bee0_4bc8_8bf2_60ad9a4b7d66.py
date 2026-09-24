# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of power.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5783646c-bee0-4bc8-8bf2-60ad9a4b7d66'
SOURCE_PATH = 'pictographic-primitives/state/power_5783646c-bee0-4bc8-8bf2-60ad9a4b7d66.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5783646c-bee0-4bc8-8bf2-60ad9a4b7d66', 'pictographic-primitives/state/power_5783646c-bee0-4bc8-8bf2-60ad9a4b7d66.svg'), ('f71eb996-3671-43a1-ae4a-03a0b33fa716', 'pictographic-primitives/symbol/power_f71eb996-3671-43a1-ae4a-03a0b33fa716.svg'), ('f24969f4-c5f7-4b83-8736-feb310ab0664', 'pictographic-primitives/symbol/power_f24969f4-c5f7-4b83-8736-feb310ab0664.svg'))
PROFILE_SOURCE_KEYS = ('solo/power', 'solo/power-f71eb996', 'solo/power-symbol')
SOLO_SOURCE_ICON_IDS = ('power', 'power-f71eb996', 'power-symbol')
REFERENCE_EXPORT_SHA256 = '7c817548ff415228863e6c8585187889006bbb7cb98800fa2fb9e1879261366f'

class DrawingVariant2(Sub32):
    icon_id = 'power-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (16, 2), (16, 15))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (9, 10), ((6, 12), (short_low, 15), (short_low, 19)))
        self.add_bezier('p2-r1-2', (short_low, 19), ((short_low, 25), (10, 30), (16, 30)))
        self.add_bezier('p2-r1-3', (16, 30), ((22, 30), (short_high, 25), (short_high, 19)))
        self.add_bezier('p2-r1-4', (short_high, 19), ((short_high, 15), (26, 12), (23, 10)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
