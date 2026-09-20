"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '0313a853-8fee-401d-b021-0624788b6cd1'
SOURCE_PATH = 'icon_set/model/icons/symbol/camera_video_sub32_v3_symbol_0313a853_8fee_401d_b021_0624788b6cd1.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '68033c122dd6d31b206f5e689c7e3c7eb9a58d638674549b90bfcda486aa7869'
SOURCE_REFERENCES = (('0313a853-8fee-401d-b021-0624788b6cd1', 'pictographic-primitives/video/camera_0313a853-8fee-401d-b021-0624788b6cd1.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'camera-video-sub32-v3-symbol-resize'
    variant_of = 'camera-video-sub32-v3-symbol'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'video'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (4, 5), (8, 5))
        self.add_bezier('p1-r1-2', (8, 5), ((8, 5), (8, 2), (10, 2)))
        self.add_line('p1-r1-3', (10, 2), (14, 2))
        self.add_bezier('p1-r1-4', (14, 2), ((16, 2), (16, 5), (16, 5)))
        self.add_line('p1-r1-5', (16, 5), (20, 5))
        self.add_arc('p1-r1-6', (20, 5), (22, 7), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (22, 7), (22, 17))
        self.add_arc('p1-r1-8', (22, 17), (20, 19), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (20, 19), (4, 19))
        self.add_arc('p1-r1-10', (4, 19), (2, 17), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (2, 17), (2, 7))
        self.add_arc('p1-r1-12', (2, 7), (4, 5), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (12, 11), (12, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
