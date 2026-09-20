"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '3fb03548-09fc-4580-80ab-9c61e488e8e9'
SOURCE_PATH = 'icon_set/model/icons/symbol/eye_outline_sub32_v3_3fb03548_09fc_4580_80ab_9c61e488e8e9.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '84bcc6e63674faf339091ea8ed8dbdcb7dcfdb86d1394b6b0deb49d2416130ff'
SOURCE_REFERENCES = (('3fb03548-09fc-4580-80ab-9c61e488e8e9', 'pictographic-primitives/symbol/eyes_3fb03548-09fc-4580-80ab-9c61e488e8e9.svg'), ('6627b62c-9a54-43be-8f20-fccd8ae111e8', 'pictographic-primitives/symbol/focus with eye_6627b62c-9a54-43be-8f20-fccd8ae111e8.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'eye-outline-sub32-v3-resize-43x32'
    variant_of = 'eye-outline-sub32-v3'
    variant_label = 'Resize 43 × 32'
    canvas_width = 43
    canvas_height = 32
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('ul', (2, 16), ((8, 6), (13, 2), (19, 2)))
        self.add_line('top', (19, 2), (24, 2))
        self.add_bezier('ur', (24, 2), ((30, 2), (35, 6), (41, 16)))
        self.add_bezier('lr', (41, 16), ((35, 26), (30, 30), (24, 30)))
        self.add_line('bottom', (24, 30), (19, 30))
        self.add_bezier('ll', (19, 30), ((13, 30), (8, 26), (2, 16)))
        self.add_arc('pupil-top', (17, 16), (26, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('pupil-bottom', (26, 16), (17, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('eye', 'ul', 'top', 'ur', 'lr', 'bottom', 'll', closed=True)
        self.add_contour('pupil', 'pupil-top', 'pupil-bottom', closed=True)
