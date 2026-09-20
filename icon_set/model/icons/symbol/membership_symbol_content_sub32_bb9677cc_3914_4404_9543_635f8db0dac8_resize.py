"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'bb9677cc-3914-4404-9543-635f8db0dac8'
SOURCE_PATH = 'icon_set/model/icons/symbol/membership_symbol_content_sub32_bb9677cc_3914_4404_9543_635f8db0dac8.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'e7d783279f6d28453c4e034948dd423316e30df70186885ff8961fcbbe64b9d4'
SOURCE_REFERENCES = (('bb9677cc-3914-4404-9543-635f8db0dac8', 'icon_set/dist/gallery/combination-originals/bb9677cc-3914-4404-9543-635f8db0dac8.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'membership-symbol-content-sub32-resize'
    variant_of = 'membership-symbol-content-sub32'
    variant_label = 'Resize 18 × 24'
    canvas_width = 18
    canvas_height = 24
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (12, 2))
        self.add_arc('p1-r1-2', (12, 2), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (2, 12), (12, 22), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (12, 22), (16, 22))
        self.add_line('p2-r1-1', (2, 12), (14, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
