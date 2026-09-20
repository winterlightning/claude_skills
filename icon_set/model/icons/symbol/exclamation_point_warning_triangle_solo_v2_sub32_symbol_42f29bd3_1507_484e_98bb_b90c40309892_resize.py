"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '42f29bd3-1507-484e-98bb-b90c40309892'
SOURCE_PATH = 'icon_set/model/icons/symbol/exclamation_point_warning_triangle_solo_v2_sub32_symbol_42f29bd3_1507_484e_98bb_b90c40309892.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '00f1ce4ebadc130d4741321e99b046cfeaf1c5e544e373ffe87fc6d30b00fc72'
SOURCE_REFERENCES = (('42f29bd3-1507-484e-98bb-b90c40309892', 'icon_set/dist/gallery/combination-originals/42f29bd3-1507-484e-98bb-b90c40309892.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'exclamation-point-warning-triangle-solo-v2-sub32-symbol-resize'
    variant_of = 'exclamation-point-warning-triangle-solo-v2-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (12, 2), (22, 22))
        self.add_line('p1-r1-2', (22, 22), (2, 22))
        self.add_line('p1-r1-3', (2, 22), (12, 2))
        self.add_line('p2-r1-1', (12, 12), (12, 13))
        self.add_line('p3-r1-1', (12, 18), (12, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
