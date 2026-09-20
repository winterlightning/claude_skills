"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '4be75ff3-2cc9-4492-a406-ef7c11b29925'
SOURCE_PATH = 'icon_set/model/icons/symbol/ball_sub32_symbol_4be75ff3_2cc9_4492_a406_ef7c11b29925.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'c40d74dbb8a9f3ed8b2f07447db643dc681de80a5c4aefcd92c0f3031a325655'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'ball-sub32-symbol-resize'
    variant_of = 'ball-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'sports'
    semantic_kind = 'noun'

    def build(self):
        self.add_arc('outline-0', (2, 12), (12, 2), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('outline-1', (12, 2), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('outline-2', (22, 12), (12, 22), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('outline-3', (12, 22), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_bezier('seam-top-0', (12, 2), ((12, 8), (16, 12), (22, 12)))
        self.add_bezier('seam-bottom-0', (2, 12), ((8, 12), (12, 16), (12, 22)))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', closed=True)
        self.add_contour('seam-top', 'seam-top-0', closed=False)
        self.add_contour('seam-bottom', 'seam-bottom-0', closed=False)
        self.relate('connect', 'seam-top', 'outline')
        self.relate('connect', 'seam-bottom', 'outline')
