"""Independent 32px profile of hexagon-design.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '96421daf-8508-4131-bcb0-05c368fcbc6a'
SOURCE_PATH = 'pictographic-primitives/design/hexagon_96421daf-8508-4131-bcb0-05c368fcbc6a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('96421daf-8508-4131-bcb0-05c368fcbc6a', 'pictographic-primitives/design/hexagon_96421daf-8508-4131-bcb0-05c368fcbc6a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hexagon-design',)
SOLO_SOURCE_ICON_IDS = ('hexagon-design',)
REFERENCE_EXPORT_SHA256 = '2a927bd278e7929a5d51dd3d5d1b8ceb637cf80f556b66b55b5519d335d417de'

class DrawingVariant2(Sub32):
    icon_id = 'hexagon-design-sub32-v2'
    related_origin_icon_id = 'hexagon-design-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    categories = ('design', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (16, 2), (short_high, 9))
        self.add_line('p1-r1-2', (short_high, 9), (short_high, 23))
        self.add_line('p1-r1-3', (short_high, 23), (16, 30))
        self.add_line('p1-r1-4', (16, 30), (short_low, 23))
        self.add_line('p1-r1-5', (short_low, 23), (short_low, 9))
        self.add_line('p1-r1-6', (short_low, 9), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
