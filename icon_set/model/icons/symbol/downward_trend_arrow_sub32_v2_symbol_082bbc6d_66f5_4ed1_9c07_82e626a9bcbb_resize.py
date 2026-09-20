"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '082bbc6d-66f5-4ed1-9c07-82e626a9bcbb'
SOURCE_PATH = 'icon_set/model/icons/symbol/downward_trend_arrow_sub32_v2_symbol_082bbc6d_66f5_4ed1_9c07_82e626a9bcbb.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '32bcaad6c31f527d398402ca4d0886e87885d40320797ebd2628b7e793666cca'
SOURCE_REFERENCES = (('082bbc6d-66f5-4ed1-9c07-82e626a9bcbb', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/downtrend arrow_082bbc6d-66f5-4ed1-9c07-82e626a9bcbb.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'downward-trend-arrow-sub32-v2-symbol-resize'
    variant_of = 'downward-trend-arrow-sub32-v2-symbol'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (8, 10))
        self.add_line('p1-r1-2', (8, 10), (13, 5))
        self.add_line('p1-r1-3', (13, 5), (22, 19))
        self.add_line('p2-r1-1', (16, 19), (22, 19))
        self.add_line('p2-r1-2', (22, 19), (22, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
