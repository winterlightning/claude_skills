"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '0c73aef1-a234-5fa7-88ee-9a36a0ed8263'
SOURCE_PATH = 'icon_set/model/icons/symbol/eighth_note_wavy_flag_sub32_symbol_0c73aef1_a234_5fa7_88ee_9a36a0ed8263.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'ca7a65a5f131e740aac21e1051c737d923be8aa401767f73bc540010004f594e'
SOURCE_REFERENCES = (('0c73aef1-a234-5fa7-88ee-9a36a0ed8263', 'pictographic-primitives/music/music note_0c73aef1-a234-5fa7-88ee-9a36a0ed8263.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'eighth-note-wavy-flag-sub32-symbol-resize'
    variant_of = 'eighth-note-wavy-flag-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/music'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (2, 18), (6, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (6, 14), (10, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (10, 18), (6, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (6, 22), (2, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (10, 18), (10, 2))
        self.add_bezier('p3-r1-1', (10, 2), ((10, 6), (18, 6), (18, 10)))
        self.add_bezier('p3-r1-2', (18, 10), ((18, 12), (16, 13), (16, 14)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
