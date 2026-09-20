"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '13ea8366-b426-4bc2-a649-eea82df87819'
SOURCE_PATH = 'icon_set/model/icons/symbol/code_sub32_v3_13ea8366_b426_4bc2_a649_eea82df87819.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'db448ed231cadcd79e55fc2b814f0f7c64029336485d88dc1bc4176c1472fdd0'
SOURCE_REFERENCES = (('13ea8366-b426-4bc2-a649-eea82df87819', 'pictographic-primitives/programing/code_13ea8366-b426-4bc2-a649-eea82df87819.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'code-sub32-v3-resize'
    variant_of = 'code-sub32-v3'
    variant_label = 'Resize 43 × 32'
    canvas_width = 43
    canvas_height = 32
    category = 'programing'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('left-1', (16, 2), (2, 16))
        self.add_line('left-2', (2, 16), (16, 30))
        self.add_line('right-1', (27, 2), (41, 16))
        self.add_line('right-2', (41, 16), (27, 30))
        self.add_contour('left', 'left-1', 'left-2', closed=False)
        self.add_contour('right', 'right-1', 'right-2', closed=False)
