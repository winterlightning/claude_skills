"""Independent 32px profile of cube.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '802601c0-689d-481d-86cd-d13aceeaf9a1'
SOURCE_PATH = 'pictographic-primitives/symbol/cube_802601c0-689d-481d-86cd-d13aceeaf9a1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('802601c0-689d-481d-86cd-d13aceeaf9a1', 'pictographic-primitives/symbol/cube_802601c0-689d-481d-86cd-d13aceeaf9a1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cube',)
SOLO_SOURCE_ICON_IDS = ('cube',)
REFERENCE_EXPORT_SHA256 = 'f611f6378bc2d5b73eb4eb1f7aaac8312a3ca19eedfc0e3077d2e4015c86f227'

class DrawingContainerSymbol(Sub32):
    icon_id = 'cube-sub32-symbol'
    related_origin_icon_id = 'cube-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/cube-sub32'
    counterpart_icon_id = 'cube-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (30, 13))
        self.add_line('p1-r1-2', (30, 13), (30, 22))
        self.add_line('p1-r1-3', (30, 22), (16, 30))
        self.add_line('p1-r1-4', (16, 30), (2, 22))
        self.add_line('p1-r1-5', (2, 22), (2, 13))
        self.add_line('p1-r1-6', (2, 13), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (2, 13), (16, 21))
        self.add_line('p2-r1-2', (16, 21), (30, 13))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 21), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
