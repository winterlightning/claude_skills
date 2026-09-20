"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '3fb03548-09fc-4580-80ab-9c61e488e8e9'
SOURCE_PATH = 'icon_set/model/icons/symbol/eye_outline_sub32_v3_3fb03548_09fc_4580_80ab_9c61e488e8e9.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '84bcc6e63674faf339091ea8ed8dbdcb7dcfdb86d1394b6b0deb49d2416130ff'
SOURCE_REFERENCES = (('3fb03548-09fc-4580-80ab-9c61e488e8e9', 'pictographic-primitives/symbol/eyes_3fb03548-09fc-4580-80ab-9c61e488e8e9.svg'), ('6627b62c-9a54-43be-8f20-fccd8ae111e8', 'pictographic-primitives/symbol/focus with eye_6627b62c-9a54-43be-8f20-fccd8ae111e8.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'eye-outline-sub32-v3-resize'
    variant_of = 'eye-outline-sub32-v3'
    variant_label = 'Resize 24 × 18'
    canvas_width = 24
    canvas_height = 18
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('ul', (2, 9), ((5, 4), (8, 2), (11, 2)))
        self.add_line('top', (11, 2), (13, 2))
        self.add_bezier('ur', (13, 2), ((16, 2), (19, 4), (22, 9)))
        self.add_bezier('lr', (22, 9), ((19, 14), (16, 16), (13, 16)))
        self.add_line('bottom', (13, 16), (11, 16))
        self.add_bezier('ll', (11, 16), ((8, 16), (5, 14), (2, 9)))
        self.add_arc('pupil-top', (10, 9), (14, 9), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('pupil-bottom', (14, 9), (10, 9), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('eye', 'ul', 'top', 'ur', 'lr', 'bottom', 'll', closed=True)
        self.add_contour('pupil', 'pupil-top', 'pupil-bottom', closed=True)
