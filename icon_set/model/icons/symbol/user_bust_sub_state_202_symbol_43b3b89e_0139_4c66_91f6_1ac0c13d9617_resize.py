"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '43b3b89e-0139-4c66-91f6-1ac0c13d9617'
SOURCE_PATH = 'icon_set/model/icons/symbol/user_bust_sub_state_202_symbol_43b3b89e_0139_4c66_91f6_1ac0c13d9617.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3ae5b95584aff62d1b968c2dee46d3d148901d973dd9431ecb3b7cbbb08a40e5'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'user-bust-sub-state-202-symbol-resize'
    variant_of = 'user-bust-sub-state-202-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'primitives/shape'
    semantic_kind = 'noun'

    def build(self):
        self.add_arc('head-top', (8, 6), (16, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (16, 6), (8, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('shoulders', (2, 20), (22, 20), radius_x=10, radius_y=5, large_arc=False, sweep=True)
        self.add_line('base-1', (22, 20), (22, 22))
        self.add_line('base-2', (22, 22), (2, 22))
        self.add_line('base-3', (2, 22), (2, 20))
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('torso', 'shoulders', 'base-1', 'base-2', 'base-3', closed=True)
