"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'fe641fda-6a23-4dc4-970c-90a6fe33f671'
SOURCE_PATH = 'icon_set/model/icons/symbol/person_pushing_wall_sub32_fe641fda_6a23_4dc4_970c_90a6fe33f671.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '02c56e342754cd0ccfc7c6188a79b94b05ff408bf675ae0d593b9706809bbdd4'
SOURCE_REFERENCES = (('fe641fda-6a23-4dc4-970c-90a6fe33f671', 'pictographic-primitives/symbol/person pushing_fe641fda-6a23-4dc4-970c-90a6fe33f671.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'person-pushing-wall-sub32-resize'
    variant_of = 'person-pushing-wall-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (11, 6), (16, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 6), (11, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-1', (11, 13), ((10, 15), (8, 16), (8, 18)))
        self.add_line('p3-r1-1', (8, 18), (2, 22))
        self.add_line('p4-r1-1', (11, 13), (16, 16))
        self.add_line('p4-r1-2', (16, 16), (22, 11))
        self.add_line('p5-r1-1', (8, 18), (14, 18))
        self.add_line('p5-r1-2', (14, 18), (12, 22))
        self.add_line('p6-r1-1', (22, 2), (22, 11))
        self.add_line('p6-r1-2', (22, 11), (22, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p6-r1-1')
        self.relate('connect', 'p4-r1-2', 'p6-r1-2')
