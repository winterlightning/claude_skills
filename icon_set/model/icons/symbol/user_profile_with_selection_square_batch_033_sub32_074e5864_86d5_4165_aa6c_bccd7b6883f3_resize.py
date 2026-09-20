"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '074e5864-86d5-4165-aa6c-bccd7b6883f3'
SOURCE_PATH = 'icon_set/model/icons/symbol/user_profile_with_selection_square_batch_033_sub32_074e5864_86d5_4165_aa6c_bccd7b6883f3.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '47584a4e09c7a61dd0371a43f6f75c0ca23fcf5bdb616fb918efb66c122abe7b'
SOURCE_REFERENCES = (('074e5864-86d5-4165-aa6c-bccd7b6883f3', 'icon_set/dist/gallery/combination-originals/074e5864-86d5-4165-aa6c-bccd7b6883f3.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'user-profile-with-selection-square-batch-033-sub32-resize'
    variant_of = 'user-profile-with-selection-square-batch-033-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (20, 7), (30, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 7), (20, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-1', (12, 30), (38, 30), radius_x=13, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p3-r1-1', (2, 2), (10, 2))
        self.add_line('p3-r1-2', (10, 2), (10, 12))
        self.add_line('p3-r1-3', (10, 12), (2, 12))
        self.add_line('p3-r1-4', (2, 12), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
