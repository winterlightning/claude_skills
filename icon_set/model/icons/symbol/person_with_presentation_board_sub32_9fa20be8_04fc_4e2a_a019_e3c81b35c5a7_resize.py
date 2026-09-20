"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '9fa20be8-04fc-4e2a-a019-e3c81b35c5a7'
SOURCE_PATH = 'icon_set/model/icons/symbol/person_with_presentation_board_sub32_9fa20be8_04fc_4e2a_a019_e3c81b35c5a7.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '4db29190b45695c9fd79925af8d8244096a23fc20943411e92d6594a96907773'
SOURCE_REFERENCES = (('9fa20be8-04fc-4e2a-a019-e3c81b35c5a7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/man square_9fa20be8-04fc-4e2a-a019-e3c81b35c5a7.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'person-with-presentation-board-sub32-resize'
    variant_of = 'person-with-presentation-board-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (3, 2), (15, 2))
        self.add_arc('p1-r1-2', (15, 2), (16, 3), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (16, 3), (16, 12))
        self.add_arc('p1-r1-4', (16, 12), (15, 15), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (15, 15), (3, 15))
        self.add_bezier('p1-r1-6', (3, 15), ((3, 15), (3, 13), (2, 13)))
        self.add_bezier('p1-r1-7', (2, 13), ((2, 13), (2, 13), (2, 12)))
        self.add_line('p1-r1-8', (2, 12), (2, 3))
        self.add_arc('p1-r1-9', (2, 3), (3, 2), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('p2-r1-1', (26, 8), (30, 5), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (30, 5), (35, 8), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (35, 8), (30, 13), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-4', (30, 13), (26, 8), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p3-r1-1', (24, 30), (24, 24))
        self.add_arc('p3-r1-2', (24, 24), (38, 24), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (38, 24), (38, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
