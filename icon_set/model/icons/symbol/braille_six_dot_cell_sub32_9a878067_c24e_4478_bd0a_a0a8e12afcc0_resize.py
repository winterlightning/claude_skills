"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '9a878067-c24e-4478-bd0a-a0a8e12afcc0'
SOURCE_PATH = 'icon_set/model/icons/symbol/braille_six_dot_cell_sub32_9a878067_c24e_4478_bd0a_a0a8e12afcc0.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'c9521f4525221040955c30e3c50c96a3b9adefa40795abd0958f2dca0070d5e1'
SOURCE_REFERENCES = (('9a878067-c24e-4478-bd0a-a0a8e12afcc0', 'icon_set/dist/gallery/combination-originals/9a878067-c24e-4478-bd0a-a0a8e12afcc0.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'braille-six-dot-cell-sub32-resize'
    variant_of = 'braille-six-dot-cell-sub32'
    variant_label = 'Resize 18 × 24'
    canvas_width = 18
    canvas_height = 24
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (2, 2))
        self.add_line('p2-r1-1', (2, 12), (2, 12))
        self.add_line('p3-r1-1', (2, 22), (2, 22))
        self.add_line('p4-r1-1', (16, 2), (16, 2))
        self.add_line('p5-r1-1', (16, 12), (16, 12))
        self.add_line('p6-r1-1', (16, 22), (16, 22))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
