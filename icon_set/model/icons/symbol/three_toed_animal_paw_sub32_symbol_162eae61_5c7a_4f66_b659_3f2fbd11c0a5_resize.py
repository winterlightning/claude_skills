"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '162eae61-5c7a-4f66-b659-3f2fbd11c0a5'
SOURCE_PATH = 'icon_set/model/icons/symbol/three_toed_animal_paw_sub32_symbol_162eae61_5c7a_4f66_b659_3f2fbd11c0a5.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'ab836422f44314c5fc078332dc080bc471dcd98d41275c9136368045eec5820c'
SOURCE_REFERENCES = (('162eae61-5c7a-4f66-b659-3f2fbd11c0a5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_162eae61-5c7a-4f66-b659-3f2fbd11c0a5.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'three-toed-animal-paw-sub32-symbol-resize'
    variant_of = 'three-toed-animal-paw-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (10, 4), (12, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (12, 2), (14, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (14, 4), (12, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (12, 6), (10, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-1', (2, 9), (4, 7), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (4, 7), (6, 9), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (6, 9), (4, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-4', (4, 11), (2, 9), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-1', (18, 9), (20, 7), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (20, 7), (22, 9), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (22, 9), (20, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (20, 11), (18, 9), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_bezier('p4-r1-1', (12, 13), ((9, 13), (10, 16), (7, 18)))
        self.add_bezier('p4-r1-2', (7, 18), ((6, 19), (5, 20), (5, 21)))
        self.add_bezier('p4-r1-3', (5, 21), ((5, 22), (8, 22), (12, 22)))
        self.add_bezier('p4-r1-4', (12, 22), ((12, 22), (12, 22), (12, 22)))
        self.add_bezier('p4-r1-5', (12, 22), ((16, 22), (19, 22), (19, 21)))
        self.add_bezier('p4-r1-6', (19, 21), ((19, 20), (18, 19), (17, 18)))
        self.add_bezier('p4-r1-7', (17, 18), ((14, 16), (15, 13), (12, 13)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', closed=False)
