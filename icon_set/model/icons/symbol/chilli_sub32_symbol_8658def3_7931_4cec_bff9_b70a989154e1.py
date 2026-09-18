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
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 16), ((4, 16), (5, 17), (7, 17)))
        self.add_bezier('p1-r1-2', (7, 17), ((13, 17), (17, 14), (22, 12)))
        self.add_bezier('p1-r1-3', (22, 12), ((23, 11), (24, 10), (25, 10)))
        self.add_bezier('p1-r1-4', (25, 10), ((26, 10), (27, 11), (27, 13)))
        self.add_bezier('p1-r1-5', (27, 13), ((28, 14), (28, 15), (28, 16)))
        self.add_bezier('p1-r1-6', (28, 16), ((28, 21), (22, 27), (15, 27)))
        self.add_bezier('p1-r1-7', (15, 27), ((8, 27), (4, 21), (2, 16)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_bezier('p2-r1-1', (27, 13), ((29, 12), (30, 10), (30, 8)))
        self.add_bezier('p2-r1-2', (30, 8), ((30, 6), (29, 5), (27, 5)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
