"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'b4208180-348f-4efd-9c97-aa942b6924da'
SOURCE_PATH = 'icon_set/model/icons/symbol/triangle_design_sub32_b4208180_348f_4efd_9c97_aa942b6924da.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '147c1e9d2bebda56a32f43f60b3cc7418d6899c4b9f18117e8926f0cb506893f'
SOURCE_REFERENCES = (('b4208180-348f-4efd-9c97-aa942b6924da', 'pictographic-primitives/design/triangle_b4208180-348f-4efd-9c97-aa942b6924da.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'triangle-design-sub32-resize'
    variant_of = 'triangle-design-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'design'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (22, 18), (12, 2))
        self.add_line('p1-r1-2', (12, 2), (2, 18))
        self.add_line('p1-r1-3', (2, 18), (22, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
