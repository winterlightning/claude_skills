"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '8be10246-6ae7-43c7-bc9e-c25a3d070fe3'
SOURCE_PATH = 'icon_set/model/icons/symbol/five_lobed_cannabis_leaf_with_straight_stem_sub32_symbol_8be10246_6ae7_43c7_bc9e_c25a3d070fe3.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '53280992882a65e39add431056029b01027ded4b44a3472b4dc2e32b8b43c821'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'five-lobed-cannabis-leaf-with-straight-stem-sub32-symbol-resize'
    variant_of = 'five-lobed-cannabis-leaf-with-straight-stem-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'cannabis'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('leaf-0', (12, 2), ((14, 6), (15, 8), (14, 11)))
        self.add_bezier('leaf-1', (14, 11), ((16, 8), (18, 6), (21, 6)))
        self.add_bezier('leaf-2', (21, 6), ((21, 10), (18, 13), (16, 14)))
        self.add_bezier('leaf-3', (16, 14), ((18, 14), (21, 16), (22, 16)))
        self.add_bezier('leaf-4', (22, 16), ((21, 18), (19, 18), (18, 18)))
        self.add_line('leaf-5', (18, 18), (12, 18))
        self.add_line('leaf-6', (12, 18), (6, 18))
        self.add_bezier('leaf-7', (6, 18), ((5, 18), (3, 18), (2, 16)))
        self.add_bezier('leaf-8', (2, 16), ((3, 16), (6, 14), (8, 14)))
        self.add_bezier('leaf-9', (8, 14), ((6, 13), (3, 10), (3, 6)))
        self.add_bezier('leaf-10', (3, 6), ((6, 6), (8, 8), (10, 11)))
        self.add_bezier('leaf-11', (10, 11), ((9, 8), (10, 6), (12, 2)))
        self.add_line('stem', (12, 18), (12, 22))
        self.add_contour('leaf', 'leaf-0', 'leaf-1', 'leaf-2', 'leaf-3', 'leaf-4', 'leaf-5', 'leaf-6', 'leaf-7', 'leaf-8', 'leaf-9', 'leaf-10', 'leaf-11', closed=True)
        self.relate('connect', 'leaf', 'stem')
