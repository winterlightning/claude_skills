"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'f8b6ea0a-273a-4932-a93b-52454f7fd328'
SOURCE_PATH = 'icon_set/model/icons/symbol/charging_battery_104_sub32_symbol_f8b6ea0a_273a_4932_a93b_52454f7fd328.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '744b71bcbe27056f29c8c5d9ab65bb163bdfffaf5a0ff93457c9a777b081d705'
SOURCE_REFERENCES = (('f8b6ea0a-273a-4932-a93b-52454f7fd328', 'icon_set/dist/gallery/combination-originals/f8b6ea0a-273a-4932-a93b-52454f7fd328.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'charging-battery-104-sub32-symbol-resize'
    variant_of = 'charging-battery-104-sub32-symbol'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (7, 2), (4, 2))
        self.add_arc('p1-r1-2', (4, 2), (2, 4), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (2, 4), (2, 16))
        self.add_arc('p1-r1-4', (2, 16), (4, 18), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (4, 18), (6, 18))
        self.add_line('p2-r1-1', (18, 5), (18, 16))
        self.add_arc('p2-r1-2', (18, 16), (16, 18), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (16, 18), (16, 18))
        self.add_line('p3-r1-1', (22, 8), (22, 12))
        self.add_line('p4-r1-1', (13, 2), (8, 11))
        self.add_line('p4-r1-2', (8, 11), (13, 11))
        self.add_line('p4-r1-3', (13, 11), (10, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
