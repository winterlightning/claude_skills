"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '3bb45fbb-182b-4dcd-92bf-ebd5c20fa96c'
SOURCE_PATH = 'icon_set/model/icons/symbol/bar_chart_lines_sub32_symbol_3bb45fbb_182b_4dcd_92bf_ebd5c20fa96c.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '25871b8eb1a07299f02774db50e49e5ed1e4473f3bef94cb56d9f759ed8c9c08'
SOURCE_REFERENCES = (('3bb45fbb-182b-4dcd-92bf-ebd5c20fa96c', 'pictographic-primitives/symbol/bar chart_3bb45fbb-182b-4dcd-92bf-ebd5c20fa96c.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'bar-chart-lines-sub32-symbol-resize'
    variant_of = 'bar-chart-lines-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbols/standalone'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 22), (22, 22))
        self.add_line('p2-r1-1', (6, 8), (6, 18))
        self.add_line('p3-r1-1', (12, 2), (12, 18))
        self.add_line('p4-r1-1', (18, 13), (18, 18))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
