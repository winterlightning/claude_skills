"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '0fa98a0f-6de4-4ade-b905-178ec453bc23'
SOURCE_PATH = 'icon_set/model/icons/symbol/shield_sub32_symbol_0fa98a0f_6de4_4ade_b905_178ec453bc23.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'c596c6b0f90cc97b5ec34a423035777c63aeb9024190f3942ba2fffbf8c6f6a0'
SOURCE_REFERENCES = (('0fa98a0f-6de4-4ade-b905-178ec453bc23', 'pictographic-primitives/protection/shield_0fa98a0f-6de4-4ade-b905-178ec453bc23.svg'), ('8e1100ca-39fe-4e71-b978-93997ec5e7d8', 'pictographic-primitives/protection/shield_8e1100ca-39fe-4e71-b978-93997ec5e7d8.svg'), ('ba7b0c51-fe87-48cd-a5c0-eea81086a3a9', 'pictographic-primitives/protection/shield_ba7b0c51-fe87-48cd-a5c0-eea81086a3a9.svg'), ('ee28756e-a560-4166-b776-2aebcbfcabaa', 'pictographic-primitives/protection/shield_ee28756e-a560-4166-b776-2aebcbfcabaa.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'shield-sub32-symbol-resize'
    variant_of = 'shield-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/protection'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (2, 5), (18, 5), radius_x=8, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (18, 5), (18, 10))
        self.add_arc('p1-r1-3', (18, 10), (10, 22), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (10, 22), (2, 10), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (2, 10), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
