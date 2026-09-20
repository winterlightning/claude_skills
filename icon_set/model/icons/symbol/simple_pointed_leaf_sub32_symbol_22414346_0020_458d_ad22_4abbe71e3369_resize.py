"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '22414346-0020-458d-ad22-4abbe71e3369'
SOURCE_PATH = 'icon_set/model/icons/symbol/simple_pointed_leaf_sub32_symbol_22414346_0020_458d_ad22_4abbe71e3369.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '2d23b8ca9ad76298604d4195901130cb3ddd6167a8cb3ec8a9c2c199fb348405'
SOURCE_REFERENCES = (('22414346-0020-458d-ad22-4abbe71e3369', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/hubbard squash_22414346-0020-458d-ad22-4abbe71e3369.svg'), ('1157517b-90dd-480d-990d-dd252676e00e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/leaf right_1157517b-90dd-480d-990d-dd252676e00e.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'simple-pointed-leaf-sub32-symbol-resize'
    variant_of = 'simple-pointed-leaf-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'food'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (2, 22), ((2, 16), (2, 11), (4, 8)))
        self.add_bezier('p1-r1-2', (4, 8), ((7, 6), (11, 3), (15, 3)))
        self.add_bezier('p1-r1-3', (15, 3), ((16, 3), (17, 3), (18, 4)))
        self.add_bezier('p1-r1-4', (18, 4), ((20, 6), (21, 8), (21, 10)))
        self.add_bezier('p1-r1-5', (21, 10), ((21, 12), (20, 14), (18, 16)))
        self.add_bezier('p1-r1-6', (18, 16), ((14, 22), (7, 22), (2, 22)))
        self.add_bezier('p2-r1-1', (2, 22), ((6, 13), (13, 8), (18, 4)))
        self.add_bezier('p2-r1-2', (18, 4), ((21, 4), (21, 3), (22, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
