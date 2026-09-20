"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '3334fbb0-436e-4762-bc8a-40fa2559c98c'
SOURCE_PATH = 'icon_set/model/icons/symbol/currency_dollar_sub32_3334fbb0_436e_4762_bc8a_40fa2559c98c.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'ae45d414824a8d42836a0d806ca6ccaf4222b85cfef76cbf73ffdc18a50ce50d'
SOURCE_REFERENCES = (('3334fbb0-436e-4762-bc8a-40fa2559c98c', 'pictographic-primitives/money/currency dollar_3334fbb0-436e-4762-bc8a-40fa2559c98c.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'currency-dollar-sub32-resize'
    variant_of = 'currency-dollar-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'money'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (10, 2), (10, 5))
        self.add_line('p2-r1-1', (10, 22), (10, 19))
        self.add_bezier('p3-r1-1', (2, 18), ((4, 18), (6, 19), (9, 19)))
        self.add_bezier('p3-r1-2', (9, 19), ((9, 19), (9, 19), (10, 19)))
        self.add_bezier('p3-r1-3', (10, 19), ((14, 19), (18, 18), (18, 16)))
        self.add_bezier('p3-r1-4', (18, 16), ((18, 16), (18, 16), (18, 16)))
        self.add_bezier('p3-r1-5', (18, 16), ((18, 12), (10, 12), (6, 11)))
        self.add_bezier('p3-r1-6', (6, 11), ((4, 11), (2, 10), (2, 8)))
        self.add_bezier('p3-r1-7', (2, 8), ((2, 8), (2, 8), (2, 8)))
        self.add_bezier('p3-r1-8', (2, 8), ((2, 8), (2, 8), (2, 8)))
        self.add_bezier('p3-r1-9', (2, 8), ((2, 8), (2, 8), (2, 7)))
        self.add_bezier('p3-r1-10', (2, 7), ((3, 6), (7, 5), (10, 5)))
        self.add_bezier('p3-r1-11', (10, 5), ((12, 5), (14, 6), (17, 6)))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', 'p3-r1-10', 'p3-r1-11', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-10')
        self.relate('connect', 'p1-r1-1', 'p3-r1-11')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-1', 'p3-r1-3')
