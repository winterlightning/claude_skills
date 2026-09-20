"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '2b2755f6-afff-4284-a954-40e23b277e6f'
SOURCE_PATH = 'icon_set/model/icons/symbol/code_programing_sub32_2b2755f6_afff_4284_a954_40e23b277e6f.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '38675414fe5a7e9be673cbfa332fcd6bae2b5144828237866573ff8461362c14'
SOURCE_REFERENCES = (('2b2755f6-afff-4284-a954-40e23b277e6f', 'pictographic-primitives/programing/code_2b2755f6-afff-4284-a954-40e23b277e6f.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'code-programing-sub32-resize'
    variant_of = 'code-programing-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'programing'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (16, 30), (25, 2))
        self.add_line('p2-r1-1', (10, 6), (2, 16))
        self.add_line('p2-r1-2', (2, 16), (10, 26))
        self.add_line('p3-r1-1', (30, 6), (38, 16))
        self.add_line('p3-r1-2', (38, 16), (30, 26))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
