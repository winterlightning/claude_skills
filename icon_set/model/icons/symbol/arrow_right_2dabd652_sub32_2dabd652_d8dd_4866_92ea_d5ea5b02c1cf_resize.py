"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '2dabd652-d8dd-4866-92ea-d5ea5b02c1cf'
SOURCE_PATH = 'icon_set/model/icons/symbol/arrow_right_2dabd652_sub32_2dabd652_d8dd_4866_92ea_d5ea5b02c1cf.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f265ec157d4d157b255cc9817ad18767f898cd2c58526b52e3b76569d29162d8'
SOURCE_REFERENCES = (('2dabd652-d8dd-4866-92ea-d5ea5b02c1cf', 'pictographic-primitives/arrows/arrow right_2dabd652-d8dd-4866-92ea-d5ea5b02c1cf.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'arrow-right-2dabd652-sub32-resize'
    variant_of = 'arrow-right-2dabd652-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'arrows'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (2, 18), (14, 6), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (14, 6), (22, 6))
        self.add_line('p2-r1-1', (17, 2), (22, 6))
        self.add_line('p2-r1-2', (22, 6), (17, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
