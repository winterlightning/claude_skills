# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of building-68b98b76.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '68b98b76-99c3-4bca-a93b-dc7b4a54ff1a'
SOURCE_PATH = 'pictographic-primitives/building/building_68b98b76-99c3-4bca-a93b-dc7b4a54ff1a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('68b98b76-99c3-4bca-a93b-dc7b4a54ff1a', 'pictographic-primitives/building/building_68b98b76-99c3-4bca-a93b-dc7b4a54ff1a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/building-68b98b76',)
SOLO_SOURCE_ICON_IDS = ('building-68b98b76',)
REFERENCE_EXPORT_SHA256 = 'a81292d82674cbcb68fd68c8b95dc31b1e319c649a66468c039ca49e87ab9de2'

class DrawingVariant2(Sub32):
    icon_id = 'building-68b98b76-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'building'
    categories = ('building', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (16, 30), (16, 9))
        self.add_line('p1-r1-2', (16, 9), (short_high, 2))
        self.add_line('p1-r1-3', (short_high, 2), (short_high, 30))
        self.add_line('p1-r1-4', (short_high, 30), (16, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (16, 16), (short_low, 16))
        self.add_line('p2-r1-2', (short_low, 16), (short_low, 30))
        self.add_line('p2-r1-3', (short_low, 30), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-4', 'p2-r1-3')
