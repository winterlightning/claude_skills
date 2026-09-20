"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '830efce8-4d56-4dec-b303-e983ea0fe715'
SOURCE_PATH = 'icon_set/model/icons/symbol/badminton_shuttlecock_sub32_symbol_830efce8_4d56_4dec_b303_e983ea0fe715.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '722b76746c62617090d09ab099d3eeff38eab98624cbd41a700fe5c25f0c5b9c'
SOURCE_REFERENCES = (('830efce8-4d56-4dec-b303-e983ea0fe715', 'pictographic-primitives/symbol/shutterstock badminton_830efce8-4d56-4dec-b303-e983ea0fe715.svg'), ('a72d1038-bdfa-446e-bd28-56516d6ea08b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/badminton ball_a72d1038-bdfa-446e-bd28-56516d6ea08b.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'badminton-shuttlecock-sub32-symbol-resize'
    variant_of = 'badminton-shuttlecock-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (6, 13), (8, 4))
        self.add_bezier('p1-r1-2', (8, 4), ((8, 3), (8, 3), (9, 3)), ((10, 2), (10, 2), (11, 2)), ((12, 2), (13, 2), (13, 3)), ((14, 3), (14, 3), (14, 4)))
        self.add_bezier('p1-r1-3', (14, 4), ((15, 4), (16, 4), (16, 4)), ((17, 4), (18, 5), (18, 5)), ((19, 5), (19, 6), (20, 6)), ((20, 7), (20, 7), (20, 8)))
        self.add_bezier('p1-r1-4', (20, 8), ((20, 8), (20, 8), (20, 8)), ((20, 8), (20, 8), (21, 8)), ((21, 8), (21, 9), (21, 9)), ((21, 10), (22, 10), (22, 11)), ((22, 11), (22, 12), (22, 13)))
        self.add_line('p1-r1-5', (22, 13), (11, 18))
        self.add_bezier('p1-r1-6', (11, 18), ((11, 19), (11, 20), (10, 21)), ((9, 22), (8, 22), (7, 22)), ((5, 22), (4, 22), (3, 21)), ((3, 20), (2, 19), (2, 18)))
        self.add_bezier('p1-r1-7', (2, 18), ((2, 17), (2, 17), (2, 17)), ((2, 16), (2, 16), (2, 16)), ((2, 15), (2, 15), (3, 14)), ((3, 14), (4, 13), (4, 13)), ((5, 13), (5, 13), (6, 13)), ((6, 13), (6, 13), (6, 13)))
        self.add_line('p2-r1-1', (6, 13), (11, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
