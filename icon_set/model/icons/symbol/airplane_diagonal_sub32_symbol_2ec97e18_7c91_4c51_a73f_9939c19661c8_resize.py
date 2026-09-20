"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '2ec97e18-7c91-4c51-a73f-9939c19661c8'
SOURCE_PATH = 'icon_set/model/icons/symbol/airplane_diagonal_sub32_symbol_2ec97e18_7c91_4c51_a73f_9939c19661c8.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '7f4523b307e06297811fa148d5aa5b16f5a88f0389205fc095986f95adce37e9'
SOURCE_REFERENCES = (('2ec97e18-7c91-4c51-a73f-9939c19661c8', 'pictographic-primitives/symbol/airplane_2ec97e18-7c91-4c51-a73f-9939c19661c8.svg'), ('995ca841-d25b-4135-bff1-8fefd083a02d', 'pictographic-primitives/travel/plane_995ca841-d25b-4135-bff1-8fefd083a02d.svg'), ('b476e384-418f-4620-b003-0fd2cce07768', 'pictographic-primitives/travel/plane_b476e384-418f-4620-b003-0fd2cce07768.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'airplane-diagonal-sub32-symbol-resize'
    variant_of = 'airplane-diagonal-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbols/standalone'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (18, 2), (22, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (22, 6), (18, 12))
        self.add_line('p1-r1-3', (18, 12), (21, 16))
        self.add_bezier('p1-r1-4', (21, 16), ((21, 17), (22, 17), (22, 18)))
        self.add_bezier('p1-r1-5', (22, 18), ((22, 18), (21, 18), (21, 18)))
        self.add_line('p1-r1-6', (21, 18), (18, 21))
        self.add_bezier('p1-r1-7', (18, 21), ((18, 21), (18, 22), (18, 22)))
        self.add_bezier('p1-r1-8', (18, 22), ((17, 22), (17, 21), (16, 21)))
        self.add_line('p1-r1-9', (16, 21), (13, 16))
        self.add_line('p1-r1-10', (13, 16), (10, 18))
        self.add_line('p1-r1-11', (10, 18), (11, 21))
        self.add_bezier('p1-r1-12', (11, 21), ((11, 21), (11, 21), (11, 21)))
        self.add_bezier('p1-r1-13', (11, 21), ((11, 22), (10, 22), (8, 22)))
        self.add_line('p1-r1-14', (8, 22), (7, 22))
        self.add_arc('p1-r1-15', (7, 22), (6, 21), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p1-r1-16', (6, 21), (6, 18))
        self.add_line('p1-r1-17', (6, 18), (3, 18))
        self.add_bezier('p1-r1-18', (3, 18), ((2, 18), (2, 18), (2, 16)))
        self.add_line('p1-r1-19', (2, 16), (2, 13))
        self.add_bezier('p1-r1-20', (2, 13), ((2, 13), (2, 12), (3, 12)))
        self.add_bezier('p1-r1-21', (3, 12), ((3, 12), (3, 12), (3, 13)))
        self.add_line('p1-r1-22', (3, 13), (6, 13))
        self.add_line('p1-r1-23', (6, 13), (10, 10))
        self.add_line('p1-r1-24', (10, 10), (3, 6))
        self.add_bezier('p1-r1-25', (3, 6), ((3, 6), (2, 6), (2, 6)))
        self.add_bezier('p1-r1-26', (2, 6), ((2, 5), (3, 5), (3, 4)))
        self.add_line('p1-r1-27', (3, 4), (4, 3))
        self.add_bezier('p1-r1-28', (4, 3), ((5, 3), (5, 2), (6, 2)))
        self.add_bezier('p1-r1-29', (6, 2), ((6, 2), (6, 2), (6, 3)))
        self.add_line('p1-r1-30', (6, 3), (13, 6))
        self.add_line('p1-r1-31', (13, 6), (18, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', 'p1-r1-21', 'p1-r1-22', 'p1-r1-23', 'p1-r1-24', 'p1-r1-25', 'p1-r1-26', 'p1-r1-27', 'p1-r1-28', 'p1-r1-29', 'p1-r1-30', 'p1-r1-31', closed=False)
