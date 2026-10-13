"""Independent 32px profile of chilli.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8658def3-7931-4cec-bff9-b70a989154e1'
SOURCE_PATH = 'pictographic-primitives/symbol/chilli_8658def3-7931-4cec-bff9-b70a989154e1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8658def3-7931-4cec-bff9-b70a989154e1', 'pictographic-primitives/symbol/chilli_8658def3-7931-4cec-bff9-b70a989154e1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/chilli',)
SOLO_SOURCE_ICON_IDS = ('chilli',)
REFERENCE_EXPORT_SHA256 = 'e38aa7e61051b5c25c0f65421c0853c0d50362b6ce2d9bd3fe13b1c6c772f65b'

class DrawingContainerSymbol(Sub32):
    icon_id = 'chilli-sub32-symbol'
    related_origin_icon_id = 'chilli-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/chilli-sub32'
    counterpart_icon_id = 'chilli-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Chili pepper: pod tapering from a slanted top to a curled tip, short stem on top.
        self.add_line('top', (16, 12), (28, 6))
        self.add_arc('outer', (28, 6), (4, 30), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_arc('inner', (4, 30), (16, 12), radius_x=13, radius_y=13, large_arc=False, sweep=False)
        self.add_contour('pod', 'top', 'outer', 'inner', closed=True)
        self.add_line('stem', (20, 10), (18, 2))
        self.relate('connect', 'pod', 'stem')
