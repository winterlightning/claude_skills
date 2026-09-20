"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '2e44a4da-4f72-452e-869b-7b4b265330f4'
SOURCE_PATH = 'icon_set/model/icons/symbol/peace_travel_sub32_2e44a4da_4f72_452e_869b_7b4b265330f4.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '6cd7526c6bab56447bede83c822844cf26195da59c3f073f9828b88c2393cbe0'
SOURCE_REFERENCES = (('2e44a4da-4f72-452e-869b-7b4b265330f4', 'pictographic-primitives/travel/peace_2e44a4da-4f72-452e-869b-7b4b265330f4.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'peace-travel-sub32-resize'
    variant_of = 'peace-travel-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'travel'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (12, 22), (12, 11))
        self.add_line('p1-r1-2', (12, 11), (6, 20))
        self.add_line('p2-r1-1', (18, 20), (12, 11))
        self.add_line('p2-r1-2', (12, 11), (12, 2))
        self.add_arc('p3-r1-1', (2, 12), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (22, 12), (18, 20), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (18, 20), (6, 20), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (6, 20), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p3-r1-3')
        self.relate('connect', 'p1-r1-2', 'p3-r1-4')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-1', 'p3-r1-3')
