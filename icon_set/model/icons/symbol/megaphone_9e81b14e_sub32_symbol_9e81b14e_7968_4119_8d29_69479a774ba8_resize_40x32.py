"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '9e81b14e-7968-4119-8d29-69479a774ba8'
SOURCE_PATH = 'icon_set/model/icons/symbol/megaphone_9e81b14e_sub32_symbol_9e81b14e_7968_4119_8d29_69479a774ba8.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'db836821463fea096a9a4e384599d19daa5bd7b6cbcf97c526001f0cfe95b2c6'
SOURCE_REFERENCES = (('9e81b14e-7968-4119-8d29-69479a774ba8', 'pictographic-primitives/interface-essential/megaphone_9e81b14e-7968-4119-8d29-69479a774ba8.svg'), ('419cefd4-6e8d-4c3c-8b36-3566f3fa846b', 'pictographic-primitives/interface-essential/megaphone_419cefd4-6e8d-4c3c-8b36-3566f3fa846b.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'megaphone-9e81b14e-sub32-symbol-resize-40x32'
    variant_of = 'megaphone-9e81b14e-sub32-symbol'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (7, 15), (15, 15))
        self.add_bezier('p1-r1-2', (15, 15), ((21, 12), (28, 6), (34, 2)))
        self.add_line('p1-r1-3', (34, 2), (38, 24))
        self.add_bezier('p1-r1-4', (38, 24), ((34, 22), (30, 21), (28, 21)))
        self.add_bezier('p1-r1-5', (28, 21), ((23, 21), (19, 22), (15, 24)))
        self.add_line('p1-r1-6', (15, 24), (11, 24))
        self.add_line('p1-r1-7', (11, 24), (7, 24))
        self.add_bezier('p1-r1-8', (7, 24), ((5, 24), (2, 21), (2, 19)))
        self.add_bezier('p1-r1-9', (2, 19), ((2, 16), (5, 15), (7, 15)))
        self.add_line('p2-r1-1', (15, 15), (15, 24))
        self.add_bezier('p3-r1-1', (11, 24), ((12, 26), (15, 30), (17, 30)))
        self.add_line('p3-r1-2', (17, 30), (21, 29))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
