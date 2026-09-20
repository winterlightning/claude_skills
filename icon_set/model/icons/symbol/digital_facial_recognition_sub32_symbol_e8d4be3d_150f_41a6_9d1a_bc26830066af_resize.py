"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'e8d4be3d-150f-41a6-9d1a-bc26830066af'
SOURCE_PATH = 'icon_set/model/icons/symbol/digital_facial_recognition_sub32_symbol_e8d4be3d_150f_41a6_9d1a_bc26830066af.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'c86f78ae5ba568e8f6ee43231377988434190a98fcbef72c3e9778992a28e099'
SOURCE_REFERENCES = (('e8d4be3d-150f-41a6-9d1a-bc26830066af', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/deepfake_e8d4be3d-150f-41a6-9d1a-bc26830066af.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'digital-facial-recognition-sub32-symbol-resize'
    variant_of = 'digital-facial-recognition-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (2, 10), (18, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (18, 10), (18, 14))
        self.add_arc('p1-r1-3', (18, 14), (2, 14), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (2, 14), (2, 10))
        self.add_line('p2-r1-1', (2, 10), (18, 10))
        self.add_line('p3-r1-1', (10, 2), (10, 12))
        self.add_bezier('p4-r1-1', (8, 16), ((9, 17), (9, 17), (10, 17)))
        self.add_bezier('p4-r1-2', (10, 17), ((11, 17), (11, 17), (13, 16)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
