"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '0b3968b5-326d-4914-af72-39a55b85a974'
SOURCE_PATH = 'icon_set/model/icons/symbol/play_sub32_0b3968b5_326d_4914_af72_39a55b85a974.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '7c8239a29d7850b329d8f2f87677dd8c5d7ea71245987c043dc8e4de4c47e0f6'
SOURCE_REFERENCES = (('0b3968b5-326d-4914-af72-39a55b85a974', 'pictographic-primitives/design/play_0b3968b5-326d-4914-af72-39a55b85a974.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'play-sub32-resize'
    variant_of = 'play-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'design'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (22, 11), (20, 13))
        self.add_line('p1-r1-2', (20, 13), (2, 22))
        self.add_line('p1-r1-3', (2, 22), (2, 2))
        self.add_line('p1-r1-4', (2, 2), (22, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
