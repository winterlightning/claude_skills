"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '16a68778-68d4-5f6b-9ce5-e5182435ed96'
SOURCE_PATH = 'icon_set/model/icons/symbol/beamed_eighth_notes_sub32_symbol_16a68778_68d4_5f6b_9ce5_e5182435ed96.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '2eb07c6b218618a600c044101dbdbda77bb5b774dcc6569dc6c1015ac31f15de'
SOURCE_REFERENCES = (('16a68778-68d4-5f6b-9ce5-e5182435ed96', 'pictographic-primitives/music/music note_16a68778-68d4-5f6b-9ce5-e5182435ed96.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'beamed-eighth-notes-sub32-symbol-resize'
    variant_of = 'beamed-eighth-notes-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/music'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (2, 18), (6, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (6, 16), (8, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (8, 18), (6, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (6, 22), (2, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (8, 18), (8, 6))
        self.add_arc('p3-r1-1', (16, 16), (18, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (18, 12), (22, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (22, 16), (18, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (18, 18), (16, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p4-r1-1', (22, 16), (22, 2))
        self.add_line('p5-r1-1', (8, 6), (22, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
