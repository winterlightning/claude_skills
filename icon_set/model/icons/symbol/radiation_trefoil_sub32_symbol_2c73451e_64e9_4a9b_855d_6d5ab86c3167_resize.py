"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '2c73451e-64e9-4a9b-855d-6d5ab86c3167'
SOURCE_PATH = 'icon_set/model/icons/symbol/radiation_trefoil_sub32_symbol_2c73451e_64e9_4a9b_855d_6d5ab86c3167.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '8bb20afca7efe902a010f9fde132d46a564da6c35028aa6218d12108cc8aa23f'
SOURCE_REFERENCES = (('2c73451e-64e9-4a9b-855d-6d5ab86c3167', 'pictographic-primitives/symbol/nuclear energy_2c73451e-64e9-4a9b-855d-6d5ab86c3167.svg'), ('db4b8c72-f358-486f-9136-75181808b594', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/radioactive_db4b8c72-f358-486f-9136-75181808b594.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'radiation-trefoil-sub32-symbol-resize'
    variant_of = 'radiation-trefoil-sub32-symbol'
    variant_label = 'Resize 24 × 22'
    canvas_width = 24
    canvas_height = 22
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (18, 2), ((19, 3), (21, 4), (21, 6)))
        self.add_bezier('p1-r1-2', (21, 6), ((21, 7), (22, 8), (22, 10)))
        self.add_line('p1-r1-3', (22, 10), (17, 10))
        self.add_arc('p1-r1-4', (17, 10), (15, 6), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (15, 6), (18, 2))
        self.add_bezier('p2-r1-1', (2, 10), ((2, 8), (3, 7), (3, 6)))
        self.add_bezier('p2-r1-2', (3, 6), ((3, 4), (5, 3), (6, 2)))
        self.add_line('p2-r1-3', (6, 2), (9, 6))
        self.add_arc('p2-r1-4', (9, 6), (7, 10), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('p2-r1-5', (7, 10), (2, 10))
        self.add_arc('p3-r1-1', (18, 18), (6, 18), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p3-r1-2', (6, 18), (9, 14))
        self.add_arc('p3-r1-3', (9, 14), (15, 14), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('p3-r1-4', (15, 14), (18, 18))
        self.add_line('p4-r1-1', (12, 10), (12, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
