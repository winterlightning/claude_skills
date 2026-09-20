"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '063ab342-3eb9-4c77-b5e5-59de1a294e59'
SOURCE_PATH = 'icon_set/model/icons/symbol/state32_6d29f24a_3e64_4196_858e_9eff669a98f5_symbol_063ab342_3eb9_4c77_b5e5_59de1a294e59.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '70fcf0fe27744c41442c90d427a1cfd4b33f4b780e96a9611ee4af82238c1a5c'
SOURCE_REFERENCES = (('063ab342-3eb9-4c77-b5e5-59de1a294e59', 'pictographic-primitives/state/video_063ab342-3eb9-4c77-b5e5-59de1a294e59.svg'), ('86847067-8fdd-411e-9dcf-21637870d1dc', 'pictographic-primitives/symbol/video_86847067-8fdd-411e-9dcf-21637870d1dc.svg'), ('6d29f24a-3e64-4196-858e-9eff669a98f5', 'pictographic-primitives/state/video_6d29f24a-3e64-4196-858e-9eff669a98f5.svg'), ('77cac2c6-9ef1-4a3f-85bf-963aeda09df3', 'pictographic-primitives/symbol/video_77cac2c6-9ef1-4a3f-85bf-963aeda09df3.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'state32-6d29f24a-3e64-4196-858e-9eff669a98f5-symbol-resize'
    variant_of = 'state32-6d29f24a-3e64-4196-858e-9eff669a98f5-symbol'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'primitives/mark'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (28, 2))
        self.add_line('p1-r1-2', (28, 2), (28, 11))
        self.add_line('p1-r1-3', (28, 11), (38, 6))
        self.add_line('p1-r1-4', (38, 6), (38, 26))
        self.add_line('p1-r1-5', (38, 26), (28, 21))
        self.add_line('p1-r1-6', (28, 21), (28, 30))
        self.add_line('p1-r1-7', (28, 30), (2, 30))
        self.add_line('p1-r1-8', (2, 30), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
