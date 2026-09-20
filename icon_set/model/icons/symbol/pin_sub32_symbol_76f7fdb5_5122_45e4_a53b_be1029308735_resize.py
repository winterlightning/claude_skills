"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '76f7fdb5-5122-45e4-a53b-be1029308735'
SOURCE_PATH = 'icon_set/model/icons/symbol/pin_sub32_symbol_76f7fdb5_5122_45e4_a53b_be1029308735.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '7dbda63229671af433275c5923a16ef3aef1212dc0a6226406b572146a571fe3'
SOURCE_REFERENCES = (('76f7fdb5-5122-45e4-a53b-be1029308735', 'pictographic-primitives/interface-essential/pin_76f7fdb5-5122-45e4-a53b-be1029308735.svg'), ('9b4b8603-58f9-4f81-8664-658ab7045658', 'pictographic-primitives/interface-essential/pin_9b4b8603-58f9-4f81-8664-658ab7045658.svg'), ('79f28f0f-6da1-42b3-a142-474d81fe6b26', 'pictographic-primitives/state/pin wave_79f28f0f-6da1-42b3-a142-474d81fe6b26.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'pin-sub32-symbol-resize'
    variant_of = 'pin-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (2, 10), (18, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-2', (18, 10), ((18, 15), (13, 19), (10, 22)))
        self.add_bezier('p1-r1-3', (10, 22), ((7, 19), (2, 15), (2, 10)))
        self.add_arc('p2-r1-1', (8, 10), (13, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (13, 10), (8, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
