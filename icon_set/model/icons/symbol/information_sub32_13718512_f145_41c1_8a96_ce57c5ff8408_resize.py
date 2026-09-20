"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '13718512-f145-41c1-8a96-ce57c5ff8408'
SOURCE_PATH = 'icon_set/model/icons/symbol/information_sub32_13718512_f145_41c1_8a96_ce57c5ff8408.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '4cf2fb2e1f8f04aba6aca7dac6badda90dcc05acdf42bcaab9d25add0037ab20'
SOURCE_REFERENCES = (('13718512-f145-41c1-8a96-ce57c5ff8408', 'pictographic-primitives/symbol/information_13718512-f145-41c1-8a96-ce57c5ff8408.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'information-sub32-resize'
    variant_of = 'information-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (13, 2))
        self.add_line('p2-r1-1', (2, 9), (10, 9))
        self.add_line('p2-r1-2', (10, 9), (10, 22))
        self.add_line('p3-r1-1', (2, 22), (18, 22))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
