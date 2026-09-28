"""Independent 32px profile of sparkle-four-point-wide.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '02f35c24-75e1-42ed-8b09-653917d04439'
SOURCE_PATH = 'pictographic-primitives/symbol/spark_02f35c24-75e1-42ed-8b09-653917d04439.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('02f35c24-75e1-42ed-8b09-653917d04439', 'pictographic-primitives/symbol/spark_02f35c24-75e1-42ed-8b09-653917d04439.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sparkle-four-point-wide',)
SOLO_SOURCE_ICON_IDS = ('sparkle-four-point-wide',)
REFERENCE_EXPORT_SHA256 = '054c0dc0d17556d44b20563f76eca319ff01f8f6893f2b7dc96bd905c9a58beb'

class DrawingContainerSymbol(Sub32):
    icon_id = 'sparkle-four-point-wide-sub32-symbol'
    related_origin_icon_id = 'sparkle-four-point-wide-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/sparkle-four-point-wide-sub32'
    counterpart_icon_id = 'sparkle-four-point-wide-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (30, 16), radius_x=19, radius_y=19, large_arc=False, sweep=False)
        self.add_arc('p1-r1-2', (30, 16), (16, 30), radius_x=19, radius_y=19, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (16, 30), (2, 16), radius_x=19, radius_y=19, large_arc=False, sweep=False)
        self.add_arc('p1-r1-4', (2, 16), (16, 2), radius_x=19, radius_y=19, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
