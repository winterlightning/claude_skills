"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '55d86d50-5f31-41c5-8057-8a88c92a68bc'
SOURCE_PATH = 'icon_set/model/icons/symbol/beamed_eighth_notes_level_sub32_symbol_55d86d50_5f31_41c5_8057_8a88c92a68bc.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '0852d4cad6a9fb135f4de7896be2e2afe9cba53bb6fcb88a4e94592034e1a7a3'
SOURCE_REFERENCES = (('55d86d50-5f31-41c5-8057-8a88c92a68bc', 'pictographic-primitives/music/music_55d86d50-5f31-41c5-8057-8a88c92a68bc.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'beamed-eighth-notes-level-sub32-symbol-resize'
    variant_of = 'beamed-eighth-notes-level-sub32-symbol'
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
        self.add_line('p2-r1-1', (8, 18), (8, 9))
        self.add_line('p2-r1-2', (8, 9), (8, 4))
        self.add_arc('p3-r1-1', (16, 18), (18, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (18, 16), (22, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (22, 18), (18, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (18, 22), (16, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p4-r1-1', (22, 18), (22, 7))
        self.add_line('p4-r1-2', (22, 7), (22, 2))
        self.add_line('p5-r1-1', (8, 4), (22, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p2-r1-2', 'p5-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
        self.relate('connect', 'p4-r1-2', 'p5-r1-1')
