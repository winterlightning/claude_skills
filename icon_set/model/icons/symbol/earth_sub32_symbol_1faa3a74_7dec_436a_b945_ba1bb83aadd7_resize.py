"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '1faa3a74-7dec-436a-b945-ba1bb83aadd7'
SOURCE_PATH = 'icon_set/model/icons/symbol/earth_sub32_symbol_1faa3a74_7dec_436a_b945_ba1bb83aadd7.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'caaf6bd24457148f47e435deec29b5dd501db6cbe5455fd7ce97c9c160cac833'
SOURCE_REFERENCES = (('1faa3a74-7dec-436a-b945-ba1bb83aadd7', 'pictographic-primitives/maps/earth_1faa3a74-7dec-436a-b945-ba1bb83aadd7.svg'), ('89744ee7-77df-4bf2-a24f-f1af9e4d239b', 'pictographic-primitives/maps/earth_89744ee7-77df-4bf2-a24f-f1af9e4d239b.svg'), ('d015ebfd-28ea-4f8e-ae85-82a0c2e8077c', 'pictographic-primitives/maps/earth_d015ebfd-28ea-4f8e-ae85-82a0c2e8077c.svg'), ('862e1938-ba92-42a6-be54-909eda881f11', 'pictographic-primitives/maps/earth_862e1938-ba92-42a6-be54-909eda881f11.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'earth-sub32-symbol-resize'
    variant_of = 'earth-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'maps'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (4, 6), (12, 2), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (12, 2), (18, 4), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (18, 4), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (22, 12), (20, 18), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (20, 18), (12, 22), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (12, 22), (6, 20), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (6, 20), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-8', (2, 12), (4, 6), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-1', (4, 6), ((5, 6), (6, 7), (8, 8)))
        self.add_line('p2-r1-2', (8, 8), (6, 12))
        self.add_bezier('p2-r1-3', (6, 12), ((6, 13), (9, 13), (11, 14)))
        self.add_bezier('p2-r1-4', (11, 14), ((11, 17), (9, 19), (6, 20)))
        self.add_bezier('p3-r1-1', (18, 4), ((15, 5), (13, 6), (13, 8)))
        self.add_bezier('p3-r1-2', (13, 8), ((13, 9), (16, 10), (16, 11)))
        self.add_line('p3-r1-3', (16, 11), (17, 15))
        self.add_bezier('p3-r1-4', (17, 15), ((18, 16), (18, 18), (20, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-4')
        self.relate('connect', 'p1-r1-5', 'p3-r1-4')
        self.relate('connect', 'p1-r1-6', 'p2-r1-4')
        self.relate('connect', 'p1-r1-7', 'p2-r1-4')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
