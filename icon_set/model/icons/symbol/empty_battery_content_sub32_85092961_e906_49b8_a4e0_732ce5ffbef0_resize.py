"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '85092961-e906-49b8-a4e0-732ce5ffbef0'
SOURCE_PATH = 'icon_set/model/icons/symbol/empty_battery_content_sub32_85092961_e906_49b8_a4e0_732ce5ffbef0.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '02bd2a2dc3142eb0454ab3b70c2a575fd7c24cf144612dcf8a52d8caa04c2683'
SOURCE_REFERENCES = (('85092961-e906-49b8-a4e0-732ce5ffbef0', 'icon_set/dist/gallery/combination-originals/85092961-e906-49b8-a4e0-732ce5ffbef0.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'empty-battery-content-sub32-resize'
    variant_of = 'empty-battery-content-sub32'
    variant_label = 'Resize 24 × 18'
    canvas_width = 24
    canvas_height = 18
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (4, 2), (16, 2))
        self.add_arc('p1-r1-2', (16, 2), (18, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (18, 4), (18, 14))
        self.add_arc('p1-r1-4', (18, 14), (16, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (16, 16), (4, 16))
        self.add_arc('p1-r1-6', (4, 16), (2, 14), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 14), (2, 4))
        self.add_arc('p1-r1-8', (2, 4), (4, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (22, 6), (22, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
