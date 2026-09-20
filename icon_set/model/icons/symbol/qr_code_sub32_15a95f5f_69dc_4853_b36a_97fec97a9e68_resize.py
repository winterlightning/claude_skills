"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '15a95f5f-69dc-4853-b36a-97fec97a9e68'
SOURCE_PATH = 'icon_set/model/icons/symbol/qr_code_sub32_15a95f5f_69dc_4853_b36a_97fec97a9e68.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '51c9bd5b6ce15f835e378cacdb45d092ff33249453528e6f3ea7df2940bd20ca'
SOURCE_REFERENCES = (('15a95f5f-69dc-4853-b36a-97fec97a9e68', 'pictographic-primitives/design/qr code_15a95f5f-69dc-4853-b36a-97fec97a9e68.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'qr-code-sub32-resize'
    variant_of = 'qr-code-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'design'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (10, 2), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (2, 16))
        self.add_line('p1-r1-3', (2, 16), (10, 16))
        self.add_line('p1-r1-4', (10, 16), (10, 2))
        self.add_line('p2-r1-1', (22, 2), (14, 2))
        self.add_line('p2-r1-2', (14, 2), (14, 18))
        self.add_line('p2-r1-3', (14, 18), (22, 18))
        self.add_line('p2-r1-4', (22, 18), (22, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
