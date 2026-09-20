"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '949214a5-cd3d-46da-8416-617e71942aa0'
SOURCE_PATH = 'icon_set/model/icons/symbol/flame_sub32_symbol_949214a5_cd3d_46da_8416_617e71942aa0.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '4d212bf504d852b61ff83a3188e4811e752dccc2c0f232bb95bc1ae0dbdcf365'
SOURCE_REFERENCES = (('949214a5-cd3d-46da-8416-617e71942aa0', 'pictographic-primitives/fire/flame_949214a5-cd3d-46da-8416-617e71942aa0.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'flame-sub32-symbol-resize'
    variant_of = 'flame-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'fire'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (10, 2), ((14, 3), (14, 6), (14, 8)))
        self.add_bezier('p1-r1-2', (14, 8), ((14, 10), (14, 11), (14, 13)))
        self.add_bezier('p1-r1-3', (14, 13), ((14, 13), (14, 14), (14, 14)))
        self.add_bezier('p1-r1-4', (14, 14), ((14, 15), (14, 15), (14, 15)))
        self.add_bezier('p1-r1-5', (14, 15), ((15, 15), (17, 13), (17, 11)))
        self.add_bezier('p1-r1-6', (17, 11), ((17, 13), (18, 13), (18, 15)))
        self.add_bezier('p1-r1-7', (18, 15), ((18, 20), (14, 22), (10, 22)))
        self.add_bezier('p1-r1-8', (10, 22), ((5, 22), (2, 19), (2, 16)))
        self.add_bezier('p1-r1-9', (2, 16), ((2, 9), (11, 8), (11, 3)))
        self.add_bezier('p1-r1-10', (11, 3), ((11, 3), (10, 3), (10, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
