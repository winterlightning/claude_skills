"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'a576eae9-10c6-460b-afb1-570ec971a498'
SOURCE_PATH = 'icon_set/model/icons/symbol/state32_a576eae9_10c6_460b_afb1_570ec971a498_v2_symbol_a576eae9_10c6_460b_afb1_570ec971a498.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '8fdde6edd03b9b24eddb5f0fa6f90da022255d9aff859fb72affa9cadc26c89f'
SOURCE_REFERENCES = (('a576eae9-10c6-460b-afb1-570ec971a498', 'icon_set/assets/combination-state32/a576eae9-10c6-460b-afb1-570ec971a498.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'state32-a576eae9-10c6-460b-afb1-570ec971a498-v2-symbol-resize'
    variant_of = 'state32-a576eae9-10c6-460b-afb1-570ec971a498-v2-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'primitives/mark'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (21, 8), ((19, 4), (16, 2), (12, 2)))
        self.add_bezier('p1-r1-2', (12, 2), ((8, 2), (3, 5), (3, 10)))
        self.add_bezier('p1-r1-3', (3, 10), ((2, 11), (2, 12), (2, 13)))
        self.add_bezier('p1-r1-4', (2, 13), ((2, 18), (7, 22), (12, 22)))
        self.add_bezier('p1-r1-5', (12, 22), ((16, 22), (20, 20), (22, 15)))
        self.add_line('p1-r2-1', (16, 8), (22, 8))
        self.add_line('p1-r2-2', (22, 8), (22, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.relate('connect', 'path-1-1', 'path-1-2')
