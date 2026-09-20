"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '8c1610b9-bbb1-4bc2-a858-53d1cdc71603'
SOURCE_PATH = 'icon_set/model/icons/symbol/robot_head_with_twin_antennae_sub32_symbol_8c1610b9_bbb1_4bc2_a858_53d1cdc71603.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'c61ffca0b3bcfdeb8eebd5326a4bc64804f062c47c4bd11e3deb7684b349bc1b'
SOURCE_REFERENCES = (('8c1610b9-bbb1-4bc2-a858-53d1cdc71603', 'pictographic-primitives/artificial-intelligence/robot_8c1610b9-bbb1-4bc2-a858-53d1cdc71603.svg'), ('dbe0f105-1e06-44cc-8dc4-597b67509f96', 'pictographic-primitives/artificial-intelligence/robot_dbe0f105-1e06-44cc-8dc4-597b67509f96.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'robot-head-with-twin-antennae-sub32-symbol-resize'
    variant_of = 'robot-head-with-twin-antennae-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'artificial-intelligence'
    semantic_kind = 'noun'

    def build(self):
        self.add_line('top-1', (2, 8), (8, 8))
        self.add_line('top-2', (8, 8), (16, 8))
        self.add_line('top-3', (16, 8), (22, 8))
        self.add_line('top-4', (22, 8), (22, 15))
        self.add_arc('lower-right', (22, 15), (15, 22), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('base', (15, 22), (9, 22))
        self.add_arc('lower-left', (9, 22), (2, 15), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('left', (2, 15), (2, 8))
        self.add_line('antenna-0', (8, 2), (8, 8))
        self.add_line('eye-0', (8, 13), (8, 15))
        self.add_line('antenna-1', (16, 2), (16, 8))
        self.add_line('eye-1', (16, 13), (16, 15))
        self.add_contour('head', 'top-1', 'top-2', 'top-3', 'top-4', 'lower-right', 'base', 'lower-left', 'left', closed=True)
        self.relate('connect', 'antenna-0', 'head')
        self.relate('connect', 'antenna-1', 'head')
