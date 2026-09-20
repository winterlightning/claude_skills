"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '5ae6e559-27d0-490b-b13a-e0950315fc03'
SOURCE_PATH = 'icon_set/model/icons/symbol/house_with_door_division_sub32_symbol_5ae6e559_27d0_490b_b13a_e0950315fc03.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'c24df156dabdaa0f95fad7467be730e0106326246483c887589ac5c1ff5aa90c'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'house-with-door-division-sub32-symbol-resize'
    variant_of = 'house-with-door-division-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('roof-1', (2, 12), (4, 10))
        self.add_line('roof-2', (4, 10), (12, 2))
        self.add_line('roof-3', (12, 2), (20, 10))
        self.add_line('roof-4', (20, 10), (22, 12))
        self.add_line('walls-1', (4, 10), (4, 22))
        self.add_line('walls-2', (4, 22), (12, 22))
        self.add_line('walls-3', (12, 22), (20, 22))
        self.add_line('walls-4', (20, 22), (20, 10))
        self.add_line('door-division', (12, 16), (12, 22))
        self.add_contour('roof', 'roof-1', 'roof-2', 'roof-3', 'roof-4', closed=False)
        self.add_contour('walls', 'walls-1', 'walls-2', 'walls-3', 'walls-4', closed=False)
        self.relate('connect', 'roof', 'walls')
        self.relate('connect', 'door-division', 'walls')
