"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '26f40b93-a3b7-419f-a55b-3b6e5693c80a'
SOURCE_PATH = 'icon_set/model/icons/symbol/smiling_face_sub_symbol_26f40b93_a3b7_419f_a55b_3b6e5693c80a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '795e339fcf54974c45cef13133ff6e11fdb7a00d73385058d884191eb0f78238'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'smiling-face-sub-symbol-resize'
    variant_of = 'smiling-face-sub-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'primitives/mark'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('face-top', (2, 12), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('face-bottom', (22, 12), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('eye-10', (8, 8), (8, 10))
        self.add_line('eye-22', (16, 8), (16, 10))
        self.add_arc('smile', (8, 15), (16, 15), radius_x=4, radius_y=2, large_arc=False, sweep=False)
        self.add_contour('face', 'face-top', 'face-bottom', closed=True)
