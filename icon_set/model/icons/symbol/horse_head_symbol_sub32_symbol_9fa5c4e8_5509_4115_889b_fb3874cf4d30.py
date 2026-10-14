"""Independent 32px profile of horse-head-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9fa5c4e8-5509-4115-889b-fb3874cf4d30'
SOURCE_PATH = 'pictographic-primitives/symbol/horse head_9fa5c4e8-5509-4115-889b-fb3874cf4d30.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9fa5c4e8-5509-4115-889b-fb3874cf4d30', 'pictographic-primitives/symbol/horse head_9fa5c4e8-5509-4115-889b-fb3874cf4d30.svg'),)
PROFILE_SOURCE_KEYS = ('solo/horse-head-symbol',)
SOLO_SOURCE_ICON_IDS = ('horse-head-symbol',)
REFERENCE_EXPORT_SHA256 = '9830f4531c1a5eb2f9d41b627ac8e8f9751a2fbcf73d9a6087a3673909682c40'

class DrawingContainerSymbol(Sub32):
    icon_id = 'horse-head-symbol-sub32-symbol'
    related_origin_icon_id = 'horse-head-symbol-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/horse-head-symbol-sub32'
    counterpart_icon_id = 'horse-head-symbol-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 30), (22, 30))
        self.add_bezier('p1-r1-2', (22, 30), ((19, 25), (16, 22), (16, 18)))
        self.add_line('p1-r1-3', (16, 18), (22, 18))
        self.add_arc('p1-r1-4', (22, 18), (28, 12), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (28, 12), (21, 5))
        self.add_line('p1-r1-6', (21, 5), (20, 2))
        self.add_line('p1-r1-7', (20, 2), (17, 5))
        self.add_bezier('p1-r1-8', (17, 5), ((8, 8), (4, 16), (4, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=True)
