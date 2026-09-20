"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '1bbf46af-b1e3-4c99-a128-75a6fbed4550'
SOURCE_PATH = 'icon_set/model/icons/symbol/person_silhouette_outline_sub32_1bbf46af_b1e3_4c99_a128_75a6fbed4550.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '9c18a3f7818d938ea4a4f32a204674f9c9c8b55fe1650352580910884de0ea6f'
SOURCE_REFERENCES = (('1bbf46af-b1e3-4c99-a128-75a6fbed4550', 'pictographic-primitives/symbol/person 1_1bbf46af-b1e3-4c99-a128-75a6fbed4550.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'person-silhouette-outline-sub32-resize'
    variant_of = 'person-silhouette-outline-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 22), (2, 19))
        self.add_arc('p1-r1-2', (2, 19), (4, 17), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (4, 17), (6, 15), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (6, 15), (6, 14))
        self.add_arc('p1-r1-5', (6, 14), (4, 10), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (4, 10), (4, 8))
        self.add_arc('p1-r1-7', (4, 8), (16, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (16, 8), (16, 10))
        self.add_arc('p1-r1-9', (16, 10), (14, 14), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (14, 14), (14, 15))
        self.add_arc('p1-r1-11', (14, 15), (16, 17), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('p1-r1-12', (16, 17), (18, 19), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-13', (18, 19), (18, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
