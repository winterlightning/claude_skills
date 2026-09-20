"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '8ddeed7d-559d-4b14-9b46-092f255cb54a'
SOURCE_PATH = 'icon_set/model/icons/symbol/bread_sub32_8ddeed7d_559d_4b14_9b46_092f255cb54a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '34a3f12de0382c98adecf9e4f5ec06fc0b99f34f560e35f8f8287754676aa9d9'
SOURCE_REFERENCES = (('8ddeed7d-559d-4b14-9b46-092f255cb54a', 'pictographic-primitives/symbol/bread_8ddeed7d-559d-4b14-9b46-092f255cb54a.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'bread-sub32-resize'
    variant_of = 'bread-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (12, 2), ((20, 2), (22, 4), (22, 6)))
        self.add_bezier('p1-r1-2', (22, 6), ((22, 8), (21, 9), (21, 10)))
        self.add_line('p1-r1-3', (21, 10), (21, 21))
        self.add_bezier('p1-r1-4', (21, 21), ((21, 21), (20, 21), (20, 21)))
        self.add_bezier('p1-r1-5', (20, 21), ((20, 22), (19, 22), (18, 22)))
        self.add_line('p1-r1-6', (18, 22), (12, 22))
        self.add_line('p1-r1-7', (12, 22), (6, 22))
        self.add_bezier('p1-r1-8', (6, 22), ((5, 22), (4, 22), (4, 21)))
        self.add_bezier('p1-r1-9', (4, 21), ((4, 21), (3, 21), (3, 21)))
        self.add_line('p1-r1-10', (3, 21), (3, 10))
        self.add_bezier('p1-r1-11', (3, 10), ((3, 9), (2, 8), (2, 6)))
        self.add_bezier('p1-r1-12', (2, 6), ((2, 4), (4, 2), (12, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
