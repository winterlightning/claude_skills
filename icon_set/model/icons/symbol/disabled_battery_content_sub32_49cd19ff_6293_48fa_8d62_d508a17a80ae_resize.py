"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '49cd19ff-6293-48fa-8d62-d508a17a80ae'
SOURCE_PATH = 'icon_set/model/icons/symbol/disabled_battery_content_sub32_49cd19ff_6293_48fa_8d62_d508a17a80ae.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '961a5e261daf439e6a47d2d6d89d6273b00eb910bdd0b62cd28520ff5a100a87'
SOURCE_REFERENCES = (('49cd19ff-6293-48fa-8d62-d508a17a80ae', 'icon_set/dist/gallery/combination-originals/49cd19ff-6293-48fa-8d62-d508a17a80ae.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'disabled-battery-content-sub32-resize'
    variant_of = 'disabled-battery-content-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 11), (2, 4))
        self.add_arc('p1-r1-2', (2, 4), (4, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (4, 2), (16, 2))
        self.add_arc('p1-r1-4', (16, 2), (18, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (18, 4), (18, 6))
        self.add_line('p2-r1-1', (18, 12), (18, 16))
        self.add_arc('p2-r1-2', (18, 16), (16, 18), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (16, 18), (4, 18))
        self.add_arc('p2-r1-4', (4, 18), (2, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-1', (22, 8), (22, 12))
        self.add_line('p4-r1-1', (2, 18), (18, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
