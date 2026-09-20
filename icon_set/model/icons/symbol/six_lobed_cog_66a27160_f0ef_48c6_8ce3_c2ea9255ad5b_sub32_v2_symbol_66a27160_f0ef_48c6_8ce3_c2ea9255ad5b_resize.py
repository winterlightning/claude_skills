"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '66a27160-f0ef-48c6-8ce3-c2ea9255ad5b'
SOURCE_PATH = 'icon_set/model/icons/symbol/six_lobed_cog_66a27160_f0ef_48c6_8ce3_c2ea9255ad5b_sub32_v2_symbol_66a27160_f0ef_48c6_8ce3_c2ea9255ad5b.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '2468e9890504fa59fb1294fed3fe7a25875fcb718247ab9769d5144240ea8d06'
SOURCE_REFERENCES = (('66a27160-f0ef-48c6-8ce3-c2ea9255ad5b', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_66a27160-f0ef-48c6-8ce3-c2ea9255ad5b.svg'), ('e3d63c1e-a685-484b-8eae-ef88e3411b1e', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_e3d63c1e-a685-484b-8eae-ef88e3411b1e.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b-sub32-v2-symbol-resize'
    variant_of = 'six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b-sub32-v2-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('lobe-0', (12, 2), ((16, 2), (13, 7), (17, 7)))
        self.add_bezier('lobe-1', (17, 7), ((18, 7), (18, 5), (20, 5)))
        self.add_bezier('lobe-2', (20, 5), ((21, 5), (22, 6), (22, 8)))
        self.add_bezier('lobe-3', (22, 8), ((22, 10), (18, 10), (18, 12)))
        self.add_bezier('lobe-4', (18, 12), ((18, 14), (22, 14), (22, 16)))
        self.add_bezier('lobe-5', (22, 16), ((22, 18), (21, 19), (20, 19)))
        self.add_bezier('lobe-6', (20, 19), ((18, 19), (18, 17), (17, 17)))
        self.add_bezier('lobe-7', (17, 17), ((13, 17), (16, 22), (12, 22)))
        self.add_bezier('lobe-8', (12, 22), ((8, 22), (11, 17), (7, 17)))
        self.add_bezier('lobe-9', (7, 17), ((6, 17), (6, 19), (4, 19)))
        self.add_bezier('lobe-10', (4, 19), ((3, 19), (2, 18), (2, 16)))
        self.add_bezier('lobe-11', (2, 16), ((2, 14), (6, 14), (6, 12)))
        self.add_bezier('lobe-12', (6, 12), ((6, 10), (2, 10), (2, 8)))
        self.add_bezier('lobe-13', (2, 8), ((2, 6), (3, 5), (4, 5)))
        self.add_bezier('lobe-14', (4, 5), ((6, 5), (6, 7), (7, 7)))
        self.add_bezier('lobe-15', (7, 7), ((11, 7), (8, 2), (12, 2)))
        self.add_line('axle', (12, 11), (12, 13))
        self.add_contour('cog', 'lobe-0', 'lobe-1', 'lobe-2', 'lobe-3', 'lobe-4', 'lobe-5', 'lobe-6', 'lobe-7', 'lobe-8', 'lobe-9', 'lobe-10', 'lobe-11', 'lobe-12', 'lobe-13', 'lobe-14', 'lobe-15', closed=True)
        self.add_contour('center', 'axle', closed=False)
