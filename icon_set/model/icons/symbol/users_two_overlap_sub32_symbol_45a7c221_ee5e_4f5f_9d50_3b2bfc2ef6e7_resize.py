"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7'
SOURCE_PATH = 'icon_set/model/icons/symbol/users_two_overlap_sub32_symbol_45a7c221_ee5e_4f5f_9d50_3b2bfc2ef6e7.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '046fe5d257b99926d700c3ad6ef216dd844a4dbb24f2f35c947504697729f7a0'
SOURCE_REFERENCES = (('45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7', 'pictographic-primitives/symbol/two persons_45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'users-two-overlap-sub32-symbol-resize'
    variant_of = 'users-two-overlap-sub32-symbol'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (3, 5), (7, 5), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (7, 5), (3, 5), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-1', (13, 6), (21, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (21, 6), (13, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p3-r1-1', (2, 16), (2, 15))
        self.add_arc('p3-r1-2', (2, 15), (5, 11), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (5, 11), (7, 11))
        self.add_arc('p4-r1-1', (10, 18), (22, 18), radius_x=6, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
