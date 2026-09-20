"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '160ed52a-22e5-47c1-8202-7d7e9f91f1ec'
SOURCE_PATH = 'icon_set/model/icons/symbol/human_eye_160ed52a_sub32_symbol_160ed52a_22e5_47c1_8202_7d7e9f91f1ec.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'dc8e2d315cdc63e8d0675194d2b22d8364c6ceae42ab7747ca134f9491b02022'
SOURCE_REFERENCES = (('160ed52a-22e5-47c1-8202-7d7e9f91f1ec', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/eye_160ed52a-22e5-47c1-8202-7d7e9f91f1ec.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'human-eye-160ed52a-sub32-symbol-resize'
    variant_of = 'human-eye-160ed52a-sub32-symbol'
    variant_label = 'Resize 24 × 17'
    canvas_width = 24
    canvas_height = 17
    category = 'health'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (2, 8), ((3, 6), (5, 5), (6, 4)), ((8, 3), (10, 2), (12, 2)), ((14, 2), (16, 3), (18, 4)), ((19, 5), (21, 6), (22, 8)))
        self.add_bezier('p1-r1-2', (22, 8), ((21, 11), (19, 12), (18, 13)), ((16, 14), (14, 15), (12, 15)), ((10, 15), (8, 14), (6, 13)), ((5, 12), (3, 11), (2, 8)))
        self.add_bezier('p2-r1-1', (10, 8), ((10, 8), (11, 8), (11, 7)), ((12, 7), (12, 7), (12, 7)), ((13, 7), (13, 7), (14, 7)), ((14, 8), (15, 8), (15, 8)))
        self.add_bezier('p2-r1-2', (15, 8), ((15, 9), (14, 9), (14, 10)), ((13, 10), (13, 10), (12, 10)), ((12, 10), (12, 10), (11, 10)), ((11, 9), (10, 9), (10, 8)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
