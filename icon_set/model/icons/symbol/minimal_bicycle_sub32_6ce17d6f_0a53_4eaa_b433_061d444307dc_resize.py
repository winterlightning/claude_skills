"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '6ce17d6f-0a53-4eaa-b433-061d444307dc'
SOURCE_PATH = 'icon_set/model/icons/symbol/minimal_bicycle_sub32_6ce17d6f_0a53_4eaa_b433_061d444307dc.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'fab4b65315ad4547231533b26689c89131e910177da8130ca6870c9b359006bf'
SOURCE_REFERENCES = (('6ce17d6f-0a53-4eaa-b433-061d444307dc', 'pictographic-primitives/transportation/bicycle_6ce17d6f-0a53-4eaa-b433-061d444307dc.svg'), ('809ac450-efd8-4c1a-94b3-ed96c86e92df', 'pictographic-primitives/transportation/bicycle_809ac450-efd8-4c1a-94b3-ed96c86e92df.svg'), ('c94a3698-f47d-459c-afbc-fc5e64f7a783', 'pictographic-primitives/transportation/bicycle_c94a3698-f47d-459c-afbc-fc5e64f7a783.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'minimal-bicycle-sub32-resize'
    variant_of = 'minimal-bicycle-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'objects/transportation'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (5, 11), ((5, 11), (6, 12), (6, 12)), ((7, 13), (7, 14), (7, 14)), ((7, 15), (7, 16), (6, 17)), ((6, 17), (5, 18), (5, 18)))
        self.add_bezier('p1-r1-2', (5, 18), ((4, 18), (3, 17), (3, 17)), ((2, 16), (2, 15), (2, 14)), ((2, 14), (2, 13), (3, 12)), ((3, 12), (4, 11), (5, 11)))
        self.add_bezier('p2-r1-1', (19, 11), ((20, 11), (21, 12), (21, 12)), ((22, 13), (22, 14), (22, 14)), ((22, 15), (22, 16), (21, 17)), ((21, 17), (20, 18), (19, 18)))
        self.add_bezier('p2-r1-2', (19, 18), ((19, 18), (18, 17), (18, 17)), ((17, 16), (17, 15), (17, 14)), ((17, 14), (17, 13), (18, 12)), ((18, 12), (19, 11), (19, 11)))
        self.add_line('p3-r1-1', (5, 11), (10, 6))
        self.add_line('p3-r1-2', (10, 6), (17, 6))
        self.add_line('p4-r1-1', (2, 2), (7, 2))
        self.add_line('p4-r1-2', (7, 2), (10, 6))
        self.add_line('p5-r1-1', (19, 11), (17, 6))
        self.add_line('p5-r1-2', (17, 6), (16, 2))
        self.add_line('p5-r1-3', (16, 2), (13, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-2', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p3-r1-2', 'p4-r1-2')
        self.relate('connect', 'p3-r1-2', 'p5-r1-1')
        self.relate('connect', 'p3-r1-2', 'p5-r1-2')
