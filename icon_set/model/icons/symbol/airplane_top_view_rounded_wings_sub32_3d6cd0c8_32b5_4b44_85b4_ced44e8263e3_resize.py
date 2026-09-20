"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '3d6cd0c8-32b5-4b44-85b4-ced44e8263e3'
SOURCE_PATH = 'icon_set/model/icons/symbol/airplane_top_view_rounded_wings_sub32_3d6cd0c8_32b5_4b44_85b4_ced44e8263e3.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '60267b064011fdeef7ea560f46891726604946c5daa098cd2dd9891b31242525'
SOURCE_REFERENCES = (('3d6cd0c8-32b5-4b44-85b4-ced44e8263e3', 'pictographic-primitives/travel/plane_3d6cd0c8-32b5-4b44-85b4-ced44e8263e3.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'airplane-top-view-rounded-wings-sub32-resize'
    variant_of = 'airplane-top-view-rounded-wings-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/travel'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (15, 5), (15, 6))
        self.add_line('p1-r1-2', (15, 6), (20, 7))
        self.add_arc('p1-r1-3', (20, 7), (20, 13), radius_x=2, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (20, 13), (15, 11))
        self.add_line('p1-r1-5', (15, 11), (15, 16))
        self.add_line('p1-r1-6', (15, 16), (18, 16))
        self.add_arc('p1-r1-7', (18, 16), (18, 22), radius_x=2, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (18, 22), (12, 20))
        self.add_line('p1-r1-9', (12, 20), (6, 22))
        self.add_arc('p1-r1-10', (6, 22), (6, 16), radius_x=2, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (6, 16), (9, 16))
        self.add_line('p1-r1-12', (9, 16), (9, 11))
        self.add_line('p1-r1-13', (9, 11), (4, 13))
        self.add_arc('p1-r1-14', (4, 13), (4, 7), radius_x=2, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-15', (4, 7), (9, 6))
        self.add_line('p1-r1-16', (9, 6), (9, 5))
        self.add_arc('p1-r1-17', (9, 5), (15, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', closed=False)
