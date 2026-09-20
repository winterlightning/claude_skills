"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '40d938a7-d3a2-43fa-ada3-7ab755c8d6d2'
SOURCE_PATH = 'icon_set/model/icons/symbol/woman_news_display_content_sub32_40d938a7_d3a2_43fa_ada3_7ab755c8d6d2.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'b54cc583b951f38b08804cf7dd227d7b95404ff024f538e24f4734f78ef56596'
SOURCE_REFERENCES = (('40d938a7-d3a2-43fa-ada3-7ab755c8d6d2', 'icon_set/dist/gallery/combination-originals/40d938a7-d3a2-43fa-ada3-7ab755c8d6d2.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'woman-news-display-content-sub32-resize'
    variant_of = 'woman-news-display-content-sub32'
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
        self.add_line('p4-r1-1', (20, 7), (19, 13))
        self.add_line('p5-r1-1', (30, 7), (33, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-1', 'p5-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p5-r1-1')
