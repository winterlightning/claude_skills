"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '86f150b1-cf66-5caf-8e7c-715833861202'
SOURCE_PATH = 'icon_set/model/icons/symbol/diagonal_telephone_receiver_sub32_symbol_86f150b1_cf66_5caf_8e7c_715833861202.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '28be6d868513fdd13ad8ad9b6d6f9f80c82c118528e44fa5029f45c3d49fba95'
SOURCE_REFERENCES = (('86f150b1-cf66-5caf-8e7c-715833861202', 'pictographic-primitives/phones/phone_86f150b1-cf66-5caf-8e7c-715833861202.svg'), ('1701ca48-aa5b-4e61-a6fd-9be91a706783', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/phone 1_1701ca48-aa5b-4e61-a6fd-9be91a706783.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'diagonal-telephone-receiver-sub32-symbol-resize'
    variant_of = 'diagonal-telephone-receiver-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/device'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (6, 2), (8, 2))
        self.add_arc('p1-r1-2', (8, 2), (10, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (10, 4), (10, 6))
        self.add_arc('p1-r1-4', (10, 6), (8, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (8, 8), (16, 16), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (16, 16), (18, 14))
        self.add_line('p1-r1-7', (18, 14), (20, 14))
        self.add_arc('p1-r1-8', (20, 14), (22, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (22, 16), (22, 20))
        self.add_arc('p1-r1-10', (22, 20), (20, 22), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (20, 22), (18, 22))
        self.add_arc('p1-r1-12', (18, 22), (2, 6), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('p1-r1-13', (2, 6), (6, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
