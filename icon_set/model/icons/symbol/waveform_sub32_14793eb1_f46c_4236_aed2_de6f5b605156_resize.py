"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '14793eb1-f46c-4236-aed2-de6f5b605156'
SOURCE_PATH = 'icon_set/model/icons/symbol/waveform_sub32_14793eb1_f46c_4236_aed2_de6f5b605156.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f2c7d400935725e0bb4c2bce3309e122c3e4c0b8e0c04dc0831109defe5f0df7'
SOURCE_REFERENCES = (('14793eb1-f46c-4236-aed2-de6f5b605156', 'pictographic-primitives/symbol/waveform_14793eb1-f46c-4236-aed2-de6f5b605156.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'waveform-sub32-resize'
    variant_of = 'waveform-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (22, 11), (19, 11))
        self.add_arc('p1-r1-2', (19, 11), (18, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (18, 8), (15, 18))
        self.add_line('p1-r1-4', (15, 18), (12, 2))
        self.add_line('p1-r1-5', (12, 2), (8, 16))
        self.add_line('p1-r1-6', (8, 16), (6, 11))
        self.add_line('p1-r1-7', (6, 11), (2, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
