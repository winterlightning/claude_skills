"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'd7a8728f-7d41-4594-84ad-c41d60d742d9'
SOURCE_PATH = 'icon_set/model/icons/symbol/round_bug_sub32_d7a8728f_7d41_4594_84ad_c41d60d742d9.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '72a067bde4458fe5f8bc924482911c26420ae757ae2b4d5299d3309d55dfe39b'
SOURCE_REFERENCES = (('d7a8728f-7d41-4594-84ad-c41d60d742d9', 'pictographic-primitives/animals/pet_d7a8728f-7d41-4594-84ad-c41d60d742d9.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'round-bug-sub32-resize'
    variant_of = 'round-bug-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'nature/animals'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (6, 13), (8, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (8, 9), (16, 9))
        self.add_arc('p1-r1-3', (16, 9), (18, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (18, 13), (18, 18))
        self.add_bezier('p1-r1-5', (18, 18), ((18, 20), (17, 22), (16, 22)))
        self.add_bezier('p1-r1-6', (16, 22), ((14, 22), (13, 22), (12, 22)))
        self.add_bezier('p1-r1-7', (12, 22), ((11, 22), (10, 22), (8, 22)))
        self.add_bezier('p1-r1-8', (8, 22), ((7, 22), (6, 20), (6, 18)))
        self.add_line('p1-r1-9', (6, 18), (6, 13))
        self.add_line('p2-r1-1', (8, 9), (8, 6))
        self.add_arc('p2-r1-2', (8, 6), (12, 3), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (12, 3), (16, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (16, 6), (16, 9))
        self.add_arc('p3-r1-1', (8, 6), (5, 2), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_arc('p4-r1-1', (16, 6), (19, 2), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('p5-r1-1', (6, 13), (2, 12), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('p6-r1-1', (18, 13), (22, 12), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p7-r1-1', (6, 18), (2, 18))
        self.add_line('p8-r1-1', (18, 18), (22, 18))
        self.add_line('p9-r1-1', (8, 22), (2, 22))
        self.add_line('p10-r1-1', (16, 22), (22, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.add_contour('path-10-1', 'p10-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p5-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-4')
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-3', 'p6-r1-1')
        self.relate('connect', 'p1-r1-4', 'p6-r1-1')
        self.relate('connect', 'p1-r1-4', 'p8-r1-1')
        self.relate('connect', 'p1-r1-5', 'p8-r1-1')
        self.relate('connect', 'p1-r1-5', 'p10-r1-1')
        self.relate('connect', 'p1-r1-6', 'p10-r1-1')
        self.relate('connect', 'p1-r1-7', 'p9-r1-1')
        self.relate('connect', 'p1-r1-8', 'p7-r1-1')
        self.relate('connect', 'p1-r1-8', 'p9-r1-1')
        self.relate('connect', 'p1-r1-9', 'p5-r1-1')
        self.relate('connect', 'p1-r1-9', 'p7-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p4-r1-1')
        self.relate('connect', 'p2-r1-4', 'p4-r1-1')
