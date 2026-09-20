"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '934292aa-0c19-5266-ac04-c173d576425d'
SOURCE_PATH = 'icon_set/model/icons/symbol/antique_axe_sub32_934292aa_0c19_5266_ac04_c173d576425d.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '2a78fadc7692b107aa902242a58178fde8d85477d3fffe5645350e249699cc51'
SOURCE_REFERENCES = (('934292aa-0c19-5266-ac04-c173d576425d', 'pictographic-primitives/war/antique axe_934292aa-0c19-5266-ac04-c173d576425d.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'antique-axe-sub32-resize'
    variant_of = 'antique-axe-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'war'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (8, 6), (12, 2))
        self.add_line('p1-r1-2', (12, 2), (16, 6))
        self.add_line('p1-r1-3', (16, 6), (22, 6))
        self.add_bezier('p1-r1-4', (22, 6), ((22, 13), (18, 18), (16, 18)))
        self.add_line('p1-r1-5', (16, 18), (16, 12))
        self.add_line('p1-r1-6', (16, 12), (12, 8))
        self.add_line('p1-r1-7', (12, 8), (8, 6))
        self.add_line('p2-r1-1', (13, 11), (2, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
