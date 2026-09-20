"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'de7e132d-7335-404c-ba94-0dc5f8acf724'
SOURCE_PATH = 'icon_set/model/icons/symbol/standing_human_figure_sub32_de7e132d_7335_404c_ba94_0dc5f8acf724.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f5ce6e04f2b4cffe2ba6b792ed820fd7807595395c4e0696c9381c92026ade81'
SOURCE_REFERENCES = (('de7e132d-7335-404c-ba94-0dc5f8acf724', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/full body person_de7e132d-7335-404c-ba94-0dc5f8acf724.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'standing-human-figure-sub32-resize'
    variant_of = 'standing-human-figure-sub32'
    variant_label = 'Resize 18 × 24'
    canvas_width = 18
    canvas_height = 24
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (6, 5), (9, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (9, 2), (12, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (12, 5), (9, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (9, 8), (6, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-1', (2, 16), (9, 12), radius_x=7, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (9, 12), (16, 16), radius_x=7, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (16, 16), (16, 18))
        self.add_line('p2-r1-4', (16, 18), (13, 18))
        self.add_line('p2-r1-5', (13, 18), (12, 22))
        self.add_line('p2-r1-6', (12, 22), (6, 22))
        self.add_line('p2-r1-7', (6, 22), (5, 18))
        self.add_line('p2-r1-8', (5, 18), (2, 18))
        self.add_line('p2-r1-9', (2, 18), (2, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', closed=False)
