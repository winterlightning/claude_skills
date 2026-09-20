"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '8e306dff-212c-4c03-9e9f-74e443e01b07'
SOURCE_PATH = 'icon_set/model/icons/symbol/vortex_sub32_8e306dff_212c_4c03_9e9f_74e443e01b07.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '2f7064398812733a977d4e80f0f3dc18864314cdbf2fb5e020a2a0b5304d307d'
SOURCE_REFERENCES = (('8e306dff-212c-4c03-9e9f-74e443e01b07', 'pictographic-primitives/symbol/vortex_8e306dff-212c-4c03-9e9f-74e443e01b07.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'vortex-sub32-resize'
    variant_of = 'vortex-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (9, 20))
        self.add_bezier('p1-r1-2', (9, 20), ((9, 21), (9, 22), (10, 22)))
        self.add_bezier('p1-r1-3', (10, 22), ((11, 22), (11, 21), (11, 20)))
        self.add_line('p1-r1-4', (11, 20), (18, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
