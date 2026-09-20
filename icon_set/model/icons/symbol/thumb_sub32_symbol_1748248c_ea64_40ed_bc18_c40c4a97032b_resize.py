"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '1748248c-ea64-40ed-bc18-c40c4a97032b'
SOURCE_PATH = 'icon_set/model/icons/symbol/thumb_sub32_symbol_1748248c_ea64_40ed_bc18_c40c4a97032b.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'aeacad628bb35ff46802fe9a584772a05cedb338088bc48b3db5bb47b4e5f685'
SOURCE_REFERENCES = (('1748248c-ea64-40ed-bc18-c40c4a97032b', 'pictographic-primitives/state/thumb_1748248c-ea64-40ed-bc18-c40c4a97032b.svg'), ('c5652a88-5c11-499a-8e2e-486a9b3a75d1', 'pictographic-primitives/symbol/thumb_c5652a88-5c11-499a-8e2e-486a9b3a75d1.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'thumb-sub32-symbol-resize'
    variant_of = 'thumb-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'state'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (2, 11), ((4, 11), (6, 11), (6, 9)))
        self.add_bezier('p1-r1-2', (6, 9), ((7, 7), (7, 2), (9, 2)))
        self.add_bezier('p1-r1-3', (9, 2), ((12, 2), (14, 3), (14, 5)))
        self.add_line('p1-r1-4', (14, 5), (13, 11))
        self.add_line('p1-r1-5', (13, 11), (16, 11))
        self.add_bezier('p1-r1-6', (16, 11), ((18, 11), (18, 12), (18, 13)))
        self.add_line('p1-r1-7', (18, 13), (16, 20))
        self.add_bezier('p1-r1-8', (16, 20), ((16, 21), (14, 22), (13, 22)))
        self.add_line('p1-r1-9', (13, 22), (8, 22))
        self.add_bezier('p1-r1-10', (8, 22), ((6, 22), (6, 20), (4, 20)))
        self.add_line('p1-r1-11', (4, 20), (2, 20))
        self.add_line('p1-r1-12', (2, 20), (2, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
