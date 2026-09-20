"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'ac736fb4-930d-5099-ae75-efdc2b2a7f88'
SOURCE_PATH = 'icon_set/model/icons/symbol/snail_shell_spiral_sub32_ac736fb4_930d_5099_ae75_efdc2b2a7f88.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '6c40a3e565f90a3737a3bd57ac8d1c01b3022c15a790f8e0737e6edacebd4f2e'
SOURCE_REFERENCES = (('ac736fb4-930d-5099-ae75-efdc2b2a7f88', 'pictographic-primitives/animals/snail shell_ac736fb4-930d-5099-ae75-efdc2b2a7f88.svg'), ('7795da4a-94f4-4d32-9e97-2b2255bfc247', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hotels/food_7795da4a-94f4-4d32-9e97-2b2255bfc247.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'snail-shell-spiral-sub32-resize'
    variant_of = 'snail-shell-spiral-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'nature/animals'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (2, 12), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (22, 12), (8, 12), radius_x=7, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (8, 12), (16, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 12), (13, 12), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
