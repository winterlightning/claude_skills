"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '0b7e0cf7-560e-4993-8784-f72f371c1d27'
SOURCE_PATH = 'icon_set/model/icons/symbol/circular_alert_warning_icon_sub32_symbol_0b7e0cf7_560e_4993_8784_f72f371c1d27.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '4bc48444073fc75964d7b1e73be4f402b2f797f6627d0ed934bf0d624ae949fb'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'circular-alert-warning-icon-sub32-symbol-resize'
    variant_of = 'circular-alert-warning-icon-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('outline-top', (2, 12), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (22, 12), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('stem', (12, 7), (12, 13))
        self.add_line('dot', (12, 17), (12, 17))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
