"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '160ed52a-22e5-47c1-8202-7d7e9f91f1ec'
SOURCE_PATH = 'icon_set/model/icons/symbol/human_eye_160ed52a_sub32_symbol_160ed52a_22e5_47c1_8202_7d7e9f91f1ec.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'dc8e2d315cdc63e8d0675194d2b22d8364c6ceae42ab7747ca134f9491b02022'
SOURCE_REFERENCES = (('160ed52a-22e5-47c1-8202-7d7e9f91f1ec', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/eye_160ed52a-22e5-47c1-8202-7d7e9f91f1ec.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'human-eye-160ed52a-sub32-symbol-resize-48x32'
    variant_of = 'human-eye-160ed52a-sub32-symbol'
    variant_label = 'Resize 48 × 32'
    canvas_width = 48
    canvas_height = 32
    category = 'health'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (2, 16), ((5, 12), (8, 8), (12, 6)), ((16, 3), (20, 2), (24, 2)), ((28, 2), (32, 3), (36, 6)), ((40, 8), (43, 12), (46, 16)))
        self.add_bezier('p1-r1-2', (46, 16), ((43, 20), (40, 24), (36, 26)), ((32, 29), (28, 30), (24, 30)), ((20, 30), (16, 29), (12, 26)), ((8, 24), (5, 20), (2, 16)))
        self.add_bezier('p2-r1-1', (19, 16), ((19, 15), (20, 14), (21, 13)), ((22, 13), (23, 13), (24, 13)), ((26, 13), (27, 13), (28, 13)), ((29, 14), (30, 15), (30, 16)))
        self.add_bezier('p2-r1-2', (30, 16), ((30, 17), (29, 18), (28, 19)), ((27, 19), (26, 19), (24, 19)), ((23, 19), (22, 19), (21, 19)), ((20, 18), (19, 17), (19, 16)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
