"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '91136439-ae9e-4bd7-833a-71e612217d7c'
SOURCE_PATH = 'icon_set/model/icons/symbol/user_with_id_card_content_sub32_91136439_ae9e_4bd7_833a_71e612217d7c.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'aa3148e68307effe514054e143e8a43fb459419226f59642a9cb76aa0ab7b4f4'
SOURCE_REFERENCES = (('91136439-ae9e-4bd7-833a-71e612217d7c', 'icon_set/dist/gallery/combination-originals/91136439-ae9e-4bd7-833a-71e612217d7c.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'user-with-id-card-content-sub32-resize-40x32'
    variant_of = 'user-with-id-card-content-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (10, 7), (20, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (20, 7), (10, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-1', (2, 30), (28, 30), radius_x=13, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p3-r1-1', (30, 2), (38, 2))
        self.add_line('p3-r1-2', (38, 2), (38, 12))
        self.add_line('p3-r1-3', (38, 12), (30, 12))
        self.add_line('p3-r1-4', (30, 12), (30, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
