"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'fcd99980-17d1-4b09-be6c-5d3d4bfc0c24'
SOURCE_PATH = 'icon_set/model/icons/symbol/six_tooth_gear_fcd99980_17d1_4b09_be6c_5d3d4bfc0c24_sub32_symbol_fcd99980_17d1_4b09_be6c_5d3d4bfc0c24.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '44995749b23ae7fa882cf8076cbf1e372190e5d1f95261d374c3d98798746eee'
SOURCE_REFERENCES = (('fcd99980-17d1-4b09-be6c-5d3d4bfc0c24', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_fcd99980-17d1-4b09-be6c-5d3d4bfc0c24.svg'), ('fe49e273-5964-4f58-94cd-8a4c93927aa8', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_fe49e273-5964-4f58-94cd-8a4c93927aa8.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'six-tooth-gear-fcd99980-17d1-4b09-be6c-5d3d4bfc0c24-sub32-symbol-resize'
    variant_of = 'six-tooth-gear-fcd99980-17d1-4b09-be6c-5d3d4bfc0c24-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (11, 2), (13, 2))
        self.add_bezier('p1-r1-2', (13, 2), ((15, 2), (14, 6), (16, 6)))
        self.add_bezier('p1-r1-3', (16, 6), ((18, 6), (19, 5), (20, 5)))
        self.add_bezier('p1-r1-4', (20, 5), ((20, 5), (21, 5), (21, 5)))
        self.add_bezier('p1-r1-5', (21, 5), ((21, 6), (21, 7), (22, 8)))
        self.add_bezier('p1-r1-6', (22, 8), ((22, 10), (18, 11), (18, 12)))
        self.add_bezier('p1-r1-7', (18, 12), ((18, 13), (22, 14), (22, 16)))
        self.add_bezier('p1-r1-8', (22, 16), ((21, 17), (21, 18), (21, 19)))
        self.add_bezier('p1-r1-9', (21, 19), ((21, 19), (20, 19), (20, 19)))
        self.add_bezier('p1-r1-10', (20, 19), ((19, 19), (18, 18), (16, 18)))
        self.add_bezier('p1-r1-11', (16, 18), ((14, 18), (15, 22), (13, 22)))
        self.add_line('p1-r1-12', (13, 22), (11, 22))
        self.add_bezier('p1-r1-13', (11, 22), ((9, 22), (10, 18), (8, 18)))
        self.add_bezier('p1-r1-14', (8, 18), ((6, 18), (5, 19), (4, 19)))
        self.add_bezier('p1-r1-15', (4, 19), ((4, 19), (3, 19), (3, 19)))
        self.add_bezier('p1-r1-16', (3, 19), ((3, 18), (3, 17), (2, 16)))
        self.add_bezier('p1-r1-17', (2, 16), ((2, 14), (6, 13), (6, 12)))
        self.add_bezier('p1-r1-18', (6, 12), ((6, 11), (2, 10), (2, 8)))
        self.add_bezier('p1-r1-19', (2, 8), ((3, 7), (3, 6), (3, 5)))
        self.add_bezier('p1-r1-20', (3, 5), ((3, 5), (4, 5), (4, 5)))
        self.add_bezier('p1-r1-21', (4, 5), ((5, 5), (6, 6), (8, 6)))
        self.add_bezier('p1-r1-22', (8, 6), ((10, 6), (9, 2), (11, 2)))
        self.add_line('p2-r1-1', (12, 11), (12, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', 'p1-r1-21', 'p1-r1-22', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
