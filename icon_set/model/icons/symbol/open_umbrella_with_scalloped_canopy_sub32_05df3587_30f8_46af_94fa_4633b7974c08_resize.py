"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '05df3587-30f8-46af-94fa-4633b7974c08'
SOURCE_PATH = 'icon_set/model/icons/symbol/open_umbrella_with_scalloped_canopy_sub32_05df3587_30f8_46af_94fa_4633b7974c08.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'd17550382053e1e258af6526d7311c182e0308119f5a3b9353303c263260ee8b'
SOURCE_REFERENCES = (('05df3587-30f8-46af-94fa-4633b7974c08', 'pictographic-primitives/accessories/batch-07/umbrella_05df3587-30f8-46af-94fa-4633b7974c08.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'open-umbrella-with-scalloped-canopy-sub32-resize'
    variant_of = 'open-umbrella-with-scalloped-canopy-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/accessories'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (2, 13), ((2, 11), (3, 8), (5, 6)))
        self.add_bezier('p1-r1-2', (5, 6), ((7, 5), (9, 3), (12, 3)))
        self.add_bezier('p1-r1-3', (12, 3), ((12, 3), (12, 3), (12, 3)))
        self.add_bezier('p1-r1-4', (12, 3), ((15, 3), (17, 5), (19, 6)))
        self.add_bezier('p1-r1-5', (19, 6), ((21, 8), (22, 11), (22, 13)))
        self.add_arc('p1-r1-6', (22, 13), (16, 13), radius_x=4, radius_y=1, large_arc=False, sweep=False)
        self.add_arc('p1-r1-7', (16, 13), (12, 11), radius_x=4, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('p1-r1-8', (12, 11), (8, 13), radius_x=4, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('p1-r1-9', (8, 13), (2, 13), radius_x=4, radius_y=1, large_arc=False, sweep=False)
        self.add_line('p2-r1-1', (12, 2), (12, 3))
        self.add_line('p3-r1-1', (12, 11), (12, 19))
        self.add_arc('p3-r1-2', (12, 19), (6, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (6, 19), (6, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
        self.relate('connect', 'p1-r1-8', 'p3-r1-1')
