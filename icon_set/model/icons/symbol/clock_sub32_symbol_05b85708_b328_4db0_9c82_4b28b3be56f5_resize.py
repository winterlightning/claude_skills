"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '05b85708-b328-4db0-9c82-4b28b3be56f5'
SOURCE_PATH = 'icon_set/model/icons/symbol/clock_sub32_symbol_05b85708_b328_4db0_9c82_4b28b3be56f5.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '8cde1f9718c6e5d3a3b3ca681fb99e66dee94f3e1c18f5453f27566fe0dbb880'
SOURCE_REFERENCES = (('05b85708-b328-4db0-9c82-4b28b3be56f5', 'pictographic-primitives/office/clock_05b85708-b328-4db0-9c82-4b28b3be56f5.svg'), ('4ab76b4c-c88a-4586-b84f-4ffd7244d650', 'pictographic-primitives/office/clock_4ab76b4c-c88a-4586-b84f-4ffd7244d650.svg'), ('9f37004b-ad82-4bff-ba0a-63d3fdc12e97', 'pictographic-primitives/office/clock_9f37004b-ad82-4bff-ba0a-63d3fdc12e97.svg'), ('e7f654f6-570d-40dd-84e5-be7ff0923e87', 'pictographic-primitives/office/clock_e7f654f6-570d-40dd-84e5-be7ff0923e87.svg'), ('282df875-ad80-4f27-9f87-f3b69a27f229', 'pictographic-primitives/office/clock_282df875-ad80-4f27-9f87-f3b69a27f229.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'clock-sub32-symbol-resize'
    variant_of = 'clock-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'office'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (2, 12), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (22, 12), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (12, 6), (12, 12))
        self.add_line('p2-r1-2', (12, 12), (16, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
