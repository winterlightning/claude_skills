"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '4ad58635-e2af-414f-ab7d-37140c1f0e2d'
SOURCE_PATH = 'icon_set/model/icons/symbol/spark_sub32_symbol_4ad58635_e2af_414f_ab7d_37140c1f0e2d.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '43280a044787b34688cd4017b5cb98f59c47c6b8b478ce744232f8b0b880cb75'
SOURCE_REFERENCES = (('4ad58635-e2af-414f-ab7d-37140c1f0e2d', 'pictographic-primitives/symbol/spark_4ad58635-e2af-414f-ab7d-37140c1f0e2d.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'spark-sub32-symbol-resize'
    variant_of = 'spark-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 12), (6, 11))
        self.add_arc('p1-r1-2', (6, 11), (11, 5), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (11, 5), (12, 2))
        self.add_line('p1-r1-4', (12, 2), (13, 5))
        self.add_arc('p1-r1-5', (13, 5), (19, 11), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (19, 11), (22, 12))
        self.add_line('p1-r1-7', (22, 12), (19, 13))
        self.add_arc('p1-r1-8', (19, 13), (13, 18), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('p1-r1-9', (13, 18), (12, 22))
        self.add_line('p1-r1-10', (12, 22), (11, 19))
        self.add_arc('p1-r1-11', (11, 19), (5, 13), radius_x=15, radius_y=15, large_arc=False, sweep=False)
        self.add_line('p1-r1-12', (5, 13), (2, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
