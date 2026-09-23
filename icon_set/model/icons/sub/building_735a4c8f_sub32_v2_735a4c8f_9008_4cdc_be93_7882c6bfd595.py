# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of building-735a4c8f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '735a4c8f-9008-4cdc-be93-7882c6bfd595'
SOURCE_PATH = 'pictographic-primitives/building/building_735a4c8f-9008-4cdc-be93-7882c6bfd595.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('735a4c8f-9008-4cdc-be93-7882c6bfd595', 'pictographic-primitives/building/building_735a4c8f-9008-4cdc-be93-7882c6bfd595.svg'),)
PROFILE_SOURCE_KEYS = ('solo/building-735a4c8f',)
SOLO_SOURCE_ICON_IDS = ('building-735a4c8f',)
REFERENCE_EXPORT_SHA256 = '31935fe550c61641571f58c14198bd26f2e0b658fbc2b81d61588e4360d1b4b7'

class DrawingVariant2(Sub32):
    icon_id = 'building-735a4c8f-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'building'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (short_low, 30), (short_low, 19))
        self.add_line('p1-r1-2', (short_low, 19), (10, 15))
        self.add_line('p1-r1-3', (10, 15), (10, 5))
        self.add_line('p1-r1-4', (10, 5), (19, 10))
        self.add_line('p1-r1-5', (19, 10), (19, 30))
        self.add_line('p1-r1-6', (19, 30), (short_low, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (19, 10), (short_high, 2))
        self.add_line('p2-r1-2', (short_high, 2), (short_high, 30))
        self.add_line('p2-r1-3', (short_high, 30), (19, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-3')
        self.relate('connect', 'p1-r1-6', 'p2-r1-3')
