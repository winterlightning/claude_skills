"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '3057870d-1409-44b0-8369-04ad03f65bba'
SOURCE_PATH = 'icon_set/model/icons/symbol/drop_sub32_v2_symbol_3057870d_1409_44b0_8369_04ad03f65bba.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f71e5dbeb1be239af8b378b3a9e65fa7fc4e556872215bd9fddff1fbd23e3b94'
SOURCE_REFERENCES = (('3057870d-1409-44b0-8369-04ad03f65bba', 'pictographic-primitives/smileys/drop_3057870d-1409-44b0-8369-04ad03f65bba.svg'), ('01d89380-da3f-4d8c-ae1a-a259c8c619ae', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/drop_01d89380-da3f-4d8c-ae1a-a259c8c619ae.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'drop-sub32-v2-symbol-resize'
    variant_of = 'drop-sub32-v2-symbol'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'smileys'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (10, 2), ((8, 6), (2, 11), (2, 14)))
        self.add_bezier('p1-r1-2', (2, 14), ((2, 16), (3, 18), (4, 20)), ((6, 21), (8, 22), (10, 22)), ((13, 22), (15, 21), (17, 20)), ((18, 18), (19, 16), (19, 14)))
        self.add_bezier('p1-r1-3', (19, 14), ((19, 11), (13, 6), (10, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
