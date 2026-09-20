"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '58449573-38e8-4aa0-bebb-14002004402f'
SOURCE_PATH = 'icon_set/model/icons/symbol/download_sub32_58449573_38e8_4aa0_bebb_14002004402f.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '746f2ad0562c31280a790dfb9f0c0b614ddcc35ffe9ba4dc0ab9c887388df3d7'
SOURCE_REFERENCES = (('58449573-38e8-4aa0-bebb-14002004402f', 'pictographic-primitives/arrows/download_58449573-38e8-4aa0-bebb-14002004402f.svg'), ('b452f6dc-091e-4314-a34a-bc3ee182e314', 'pictographic-primitives/emails/download_b452f6dc-091e-4314-a34a-bc3ee182e314.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'download-sub32-resize'
    variant_of = 'download-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'arrows'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 24), (2, 27))
        self.add_arc('p1-r1-2', (2, 27), (5, 30), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (5, 30), (35, 30))
        self.add_arc('p1-r1-4', (35, 30), (38, 27), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (38, 27), (38, 24))
        self.add_line('p2-r1-1', (20, 2), (20, 22))
        self.add_line('p3-r1-1', (11, 15), (20, 22))
        self.add_line('p3-r1-2', (20, 22), (29, 15))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
