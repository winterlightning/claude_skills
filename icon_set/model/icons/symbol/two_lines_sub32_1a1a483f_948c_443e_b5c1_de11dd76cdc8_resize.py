"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '1a1a483f-948c-443e-b5c1-de11dd76cdc8'
SOURCE_PATH = 'icon_set/model/icons/symbol/two_lines_sub32_1a1a483f_948c_443e_b5c1_de11dd76cdc8.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '06a72ad2f345b76d6c07a6f5652bdcdda745bf7af26b5ccd51fc8e3cd5f3c7b8'
SOURCE_REFERENCES = (('1a1a483f-948c-443e-b5c1-de11dd76cdc8', 'pictographic-primitives/symbol/two lines_1a1a483f-948c-443e-b5c1-de11dd76cdc8.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'two-lines-sub32-resize'
    variant_of = 'two-lines-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (18, 2), (18, 22))
        self.add_line('p1-r1-2', (18, 22), (2, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
