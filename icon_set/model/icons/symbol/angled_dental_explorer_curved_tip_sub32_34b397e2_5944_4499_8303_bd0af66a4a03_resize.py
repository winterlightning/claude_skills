"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '34b397e2-5944-4499-8303-bd0af66a4a03'
SOURCE_PATH = 'icon_set/model/icons/symbol/angled_dental_explorer_curved_tip_sub32_34b397e2_5944_4499_8303_bd0af66a4a03.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'c20403b5c8d6fa5e162edbd68d24bf65aaa8b507f6720e1aa694a4a3df14fcce'
SOURCE_REFERENCES = (('34b397e2-5944-4499-8303-bd0af66a4a03', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/tooth_34b397e2-5944-4499-8303-bd0af66a4a03.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'angled-dental-explorer-curved-tip-sub32-resize'
    variant_of = 'angled-dental-explorer-curved-tip-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/health'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 22), (12, 12))
        self.add_line('p1-r1-2', (12, 12), (16, 8))
        self.add_line('p1-r1-3', (16, 8), (16, 6))
        self.add_arc('p1-r1-4', (16, 6), (18, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (18, 2), (22, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (22, 6), (22, 8))
        self.add_line('p2-r1-1', (12, 12), (16, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
