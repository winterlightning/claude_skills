# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of horse-head-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '9fa5c4e8-5509-4115-889b-fb3874cf4d30'
SOURCE_PATH = 'pictographic-primitives/symbol/horse head_9fa5c4e8-5509-4115-889b-fb3874cf4d30.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9fa5c4e8-5509-4115-889b-fb3874cf4d30', 'pictographic-primitives/symbol/horse head_9fa5c4e8-5509-4115-889b-fb3874cf4d30.svg'),)
PROFILE_SOURCE_KEYS = ('solo/horse-head-symbol',)
SOLO_SOURCE_ICON_IDS = ('horse-head-symbol',)
REFERENCE_EXPORT_SHA256 = '9830f4531c1a5eb2f9d41b627ac8e8f9751a2fbcf73d9a6087a3673909682c40'

class DrawingContainerSymbol(Sub32):
    icon_id = 'horse-head-symbol-sub32-symbol'
    variant_of = 'horse-head-symbol-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/horse-head-symbol-sub32'
    counterpart_icon_id = 'horse-head-symbol-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (17, 2), (15, 5))
        self.add_bezier('p1-r1-2', (15, 5), ((14, 5), (13, 5), (12, 6)))
        self.add_bezier('p1-r1-3', (12, 6), ((11, 6), (10, 7), (9, 8)))
        self.add_bezier('p1-r1-4', (9, 8), ((5, 13), (5, 21), (5, 27)))
        self.add_bezier('p1-r1-5', (5, 27), ((5, 27), (5, 27), (5, 27)))
        self.add_bezier('p1-r1-6', (5, 27), ((5, 28), (5, 29), (5, 30)))
        self.add_line('p1-r1-7', (5, 30), (22, 30))
        self.add_bezier('p1-r1-8', (22, 30), ((20, 26), (18, 22), (17, 18)))
        self.add_bezier('p1-r1-9', (17, 18), ((17, 18), (16, 17), (16, 16)))
        self.add_bezier('p1-r1-10', (16, 16), ((16, 15), (16, 15), (16, 15)))
        self.add_bezier('p1-r1-11', (16, 15), ((16, 15), (16, 15), (16, 15)))
        self.add_bezier('p1-r1-12', (16, 15), ((16, 15), (16, 15), (16, 15)))
        self.add_bezier('p1-r1-13', (16, 15), ((16, 15), (17, 15), (18, 16)))
        self.add_bezier('p1-r1-14', (18, 16), ((19, 16), (20, 16), (21, 16)))
        self.add_bezier('p1-r1-15', (21, 16), ((22, 17), (23, 17), (24, 17)))
        self.add_bezier('p1-r1-16', (24, 17), ((24, 17), (24, 17), (24, 17)))
        self.add_bezier('p1-r1-17', (24, 17), ((25, 17), (26, 16), (26, 15)))
        self.add_line('p1-r1-18', (26, 15), (27, 13))
        self.add_bezier('p1-r1-19', (27, 13), ((26, 12), (25, 11), (23, 10)))
        self.add_bezier('p1-r1-20', (23, 10), ((22, 9), (21, 8), (20, 7)))
        self.add_bezier('p1-r1-21', (20, 7), ((19, 7), (18, 6), (18, 6)))
        self.add_bezier('p1-r1-22', (18, 6), ((18, 5), (18, 3), (17, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', 'p1-r1-21', 'p1-r1-22', closed=False)
