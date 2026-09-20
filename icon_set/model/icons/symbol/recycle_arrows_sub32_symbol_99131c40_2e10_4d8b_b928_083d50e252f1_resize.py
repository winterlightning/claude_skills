"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '99131c40-2e10-4d8b-b928-083d50e252f1'
SOURCE_PATH = 'icon_set/model/icons/symbol/recycle_arrows_sub32_symbol_99131c40_2e10_4d8b_b928_083d50e252f1.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '836f7033483fb83af6e3131fc753888df5158317d4cc17c73fe8faa3425dc8e6'
SOURCE_REFERENCES = (('99131c40-2e10-4d8b-b928-083d50e252f1', 'pictographic-primitives/symbol/recycle_99131c40-2e10-4d8b-b928-083d50e252f1.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'recycle-arrows-sub32-symbol-resize'
    variant_of = 'recycle-arrows-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (8, 6), (16, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (16, 6), (18, 11))
        self.add_line('p2-r1-1', (14, 10), (18, 11))
        self.add_line('p2-r1-2', (18, 11), (20, 6))
        self.add_line('p3-r1-1', (22, 14), (22, 16))
        self.add_arc('p3-r1-2', (22, 16), (18, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (18, 18), (12, 18))
        self.add_line('p4-r1-1', (16, 16), (12, 18))
        self.add_line('p4-r1-2', (12, 18), (16, 22))
        self.add_line('p5-r1-1', (7, 18), (6, 18))
        self.add_arc('p5-r1-2', (6, 18), (2, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p5-r1-3', (2, 16), (6, 10))
        self.add_line('p6-r1-1', (2, 11), (6, 10))
        self.add_line('p6-r1-2', (6, 10), (6, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-2')
        self.relate('connect', 'p5-r1-3', 'p6-r1-1')
        self.relate('connect', 'p5-r1-3', 'p6-r1-2')
