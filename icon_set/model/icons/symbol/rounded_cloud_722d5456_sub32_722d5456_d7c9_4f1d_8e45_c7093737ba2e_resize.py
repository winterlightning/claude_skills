"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '722d5456-d7c9-4f1d-8e45-c7093737ba2e'
SOURCE_PATH = 'icon_set/model/icons/symbol/rounded_cloud_722d5456_sub32_722d5456_d7c9_4f1d_8e45_c7093737ba2e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3de4f47034606746c2f614065468cd2f445ae75555530daa0fd8021827eb28f4'
SOURCE_REFERENCES = (('722d5456-d7c9-4f1d-8e45-c7093737ba2e', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/cloud 1_722d5456-d7c9-4f1d-8e45-c7093737ba2e.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'rounded-cloud-722d5456-sub32-resize'
    variant_of = 'rounded-cloud-722d5456-sub32'
    variant_label = 'Resize 43 × 32'
    canvas_width = 43
    canvas_height = 32
    category = 'objects/cloud'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (10, 15), ((10, 14), (10, 14), (10, 13)), ((10, 12), (10, 11), (10, 10)), ((11, 8), (12, 7), (13, 6)), ((14, 4), (15, 3), (17, 3)), ((18, 2), (19, 2), (21, 2)), ((21, 2), (22, 2), (22, 2)))
        self.add_bezier('p1-r1-2', (22, 2), ((22, 2), (22, 2), (22, 2)), ((24, 2), (25, 2), (27, 3)), ((28, 4), (30, 5), (31, 6)), ((32, 7), (32, 9), (33, 10)), ((33, 11), (33, 12), (33, 13)), ((33, 14), (33, 14), (33, 15)))
        self.add_bezier('p1-r1-3', (33, 15), ((33, 15), (33, 15), (33, 15)), ((34, 15), (35, 15), (36, 16)), ((37, 16), (38, 16), (38, 17)), ((39, 18), (40, 18), (40, 19)), ((41, 20), (41, 21), (41, 22)))
        self.add_bezier('p1-r1-4', (41, 22), ((41, 23), (41, 24), (40, 25)), ((40, 26), (39, 27), (39, 28)), ((38, 28), (37, 29), (36, 29)), ((35, 30), (34, 30), (33, 30)))
        self.add_line('p1-r1-5', (33, 30), (10, 30))
        self.add_bezier('p1-r1-6', (10, 30), ((9, 30), (8, 30), (7, 29)), ((6, 29), (5, 28), (4, 28)), ((4, 27), (3, 26), (3, 25)), ((2, 24), (2, 23), (2, 22)))
        self.add_bezier('p1-r1-7', (2, 22), ((2, 21), (2, 20), (3, 19)), ((3, 18), (4, 18), (5, 17)), ((5, 16), (6, 16), (7, 16)), ((8, 15), (9, 15), (10, 15)), ((10, 15), (10, 15), (10, 15)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
