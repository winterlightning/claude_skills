"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '265b5a65-5aa8-4bdf-bbf6-682e357fd957'
SOURCE_PATH = 'icon_set/model/icons/symbol/megaphone_reference_265b5a65_5aa8_4bdf_bbf6_682e357fd957_sub32_symbol_265b5a65_5aa8_4bdf_bbf6_682e357fd957.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '849d1d259047be31925a6f1a76c3507bf65ea4ee74845a907729ba15cc482a6f'
SOURCE_REFERENCES = (('265b5a65-5aa8-4bdf-bbf6-682e357fd957', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/megaphone_265b5a65-5aa8-4bdf-bbf6-682e357fd957.svg'), ('3eda77ef-4a51-4c20-a561-a20d8a86f04f', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/megaphone_3eda77ef-4a51-4c20-a561-a20d8a86f04f.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'megaphone-reference-265b5a65-5aa8-4bdf-bbf6-682e357fd957-sub32-symbol-resize'
    variant_of = 'megaphone-reference-265b5a65-5aa8-4bdf-bbf6-682e357fd957-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 13), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (22, 13))
        self.add_line('p1-r1-3', (22, 13), (16, 14))
        self.add_line('p1-r1-4', (16, 14), (8, 16))
        self.add_line('p1-r1-5', (8, 16), (4, 16))
        self.add_line('p1-r1-6', (4, 16), (2, 13))
        self.add_bezier('p2-r1-1', (8, 16), ((8, 20), (10, 22), (12, 22)))
        self.add_bezier('p2-r1-2', (12, 22), ((14, 22), (16, 20), (16, 14)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
