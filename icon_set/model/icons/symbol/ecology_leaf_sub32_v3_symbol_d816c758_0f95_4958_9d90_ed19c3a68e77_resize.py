"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'd816c758-0f95-4958-9d90-ed19c3a68e77'
SOURCE_PATH = 'icon_set/model/icons/symbol/ecology_leaf_sub32_v3_symbol_d816c758_0f95_4958_9d90_ed19c3a68e77.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'dfb187a25bef58ab810ca03b20004a387ae226f8df5327305a4d7badaba42812'
SOURCE_REFERENCES = (('d816c758-0f95-4958-9d90-ed19c3a68e77', 'pictographic-primitives/ecology/ecology leaf_d816c758-0f95-4958-9d90-ed19c3a68e77.svg'), ('164d9e51-fa44-4293-94e6-d83af50f3387', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/leaf right_164d9e51-fa44-4293-94e6-d83af50f3387.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'ecology-leaf-sub32-v3-symbol-resize'
    variant_of = 'ecology-leaf-sub32-v3-symbol'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'ecology'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('right', (22, 2), ((22, 13), (17, 19), (9, 19)))
        self.add_bezier('lower-left', (9, 19), ((5, 19), (3, 16), (3, 12)))
        self.add_bezier('upper-left', (3, 12), ((3, 8), (6, 5), (11, 5)))
        self.add_bezier('tip', (11, 5), ((16, 5), (19, 5), (22, 2)))
        self.add_bezier('vein', (2, 19), ((6, 14), (10, 11), (16, 8)))
        self.add_contour('leaf', 'right', 'lower-left', 'upper-left', 'tip', closed=True)
        self.relate('connect', 'leaf', 'vein')
