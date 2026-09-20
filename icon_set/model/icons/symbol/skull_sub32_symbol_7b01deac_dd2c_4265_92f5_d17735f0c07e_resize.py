"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '7b01deac-dd2c-4265-92f5-d17735f0c07e'
SOURCE_PATH = 'icon_set/model/icons/symbol/skull_sub32_symbol_7b01deac_dd2c_4265_92f5_d17735f0c07e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'a33acd5b0d88cc69a229714af7d0b6d3d810ed18ac2ed967a75fc092195c1d0a'
SOURCE_REFERENCES = (('7b01deac-dd2c-4265-92f5-d17735f0c07e', 'pictographic-primitives/interface-essential/skull_7b01deac-dd2c-4265-92f5-d17735f0c07e.svg'), ('85266d86-6f31-4d3b-91ca-d5a232d0c46c', 'pictographic-primitives/interface-essential/skull_85266d86-6f31-4d3b-91ca-d5a232d0c46c.svg'), ('bf02abda-c65a-4ff2-af41-3fdc5c490cc7', 'pictographic-primitives/interface-essential/skull_bf02abda-c65a-4ff2-af41-3fdc5c490cc7.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'skull-sub32-symbol-resize'
    variant_of = 'skull-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (5, 22), ((5, 21), (5, 19), (4, 18)))
        self.add_bezier('p1-r1-2', (4, 18), ((3, 16), (2, 15), (2, 11)))
        self.add_bezier('p1-r1-3', (2, 11), ((2, 6), (5, 2), (10, 2)))
        self.add_bezier('p1-r1-4', (10, 2), ((15, 2), (18, 6), (18, 11)))
        self.add_bezier('p1-r1-5', (18, 11), ((18, 15), (17, 16), (16, 18)))
        self.add_bezier('p1-r1-6', (16, 18), ((15, 20), (15, 21), (15, 22)))
        self.add_line('p2-r1-1', (10, 22), (10, 19))
        self.add_line('p3-r1-1', (6, 11), (6, 11))
        self.add_line('p4-r1-1', (14, 11), (14, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
