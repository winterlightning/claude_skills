"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '5783646c-bee0-4bc8-8bf2-60ad9a4b7d66'
SOURCE_PATH = 'icon_set/model/icons/symbol/power_sub32_v2_symbol_5783646c_bee0_4bc8_8bf2_60ad9a4b7d66.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '53ae4c29da1b64fba0a989b20021469d6aa67a4b17d63409dc78b9b5abe7dcb0'
SOURCE_REFERENCES = (('5783646c-bee0-4bc8-8bf2-60ad9a4b7d66', 'pictographic-primitives/state/power_5783646c-bee0-4bc8-8bf2-60ad9a4b7d66.svg'), ('f71eb996-3671-43a1-ae4a-03a0b33fa716', 'pictographic-primitives/symbol/power_f71eb996-3671-43a1-ae4a-03a0b33fa716.svg'), ('f24969f4-c5f7-4b83-8736-feb310ab0664', 'pictographic-primitives/symbol/power_f24969f4-c5f7-4b83-8736-feb310ab0664.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'power-sub32-v2-symbol-resize'
    variant_of = 'power-sub32-v2-symbol'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'state'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (10, 2), (10, 11))
        self.add_bezier('p2-r1-1', (6, 8), ((3, 9), (2, 11), (2, 14)))
        self.add_bezier('p2-r1-2', (2, 14), ((2, 18), (6, 22), (10, 22)))
        self.add_bezier('p2-r1-3', (10, 22), ((15, 22), (19, 18), (19, 14)))
        self.add_bezier('p2-r1-4', (19, 14), ((19, 11), (18, 9), (15, 8)))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
