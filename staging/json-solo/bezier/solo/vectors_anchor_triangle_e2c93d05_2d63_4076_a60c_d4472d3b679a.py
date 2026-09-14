"""Vectors anchor triangle (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2c93d05-2d63-4076-a60c-d4472d3b679a'
SOURCE_PATH = 'icons-json/design/vectors anchor triangle_e2c93d05-2d63-4076-a60c-d4472d3b679a.json'
AUTHOR = 'json_to_solo'

class VectorsAnchorTriangleDesign(Solo48):
    icon_id = 'vectors-anchor-triangle-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('vectors', 'anchor', 'triangle', 'design')

    def build(self):
        self.add_line('sym-e0', (4, 37), (22, 9))
        self.add_bezier('sym-e1', (22, 9), ((22.173, 8.739), (22.636, 8), (23, 8)))
        self.add_bezier('sym-e2', (23, 8), ((23.045, 8), (23.955, 8.008), (24, 8)))
        self.add_bezier('sym-e3', (24, 8), ((24.045, 8), (23.955, 8), (24, 8)))
        self.add_bezier('sym-e4', (24, 8), ((24.096, 8), (23.864, 8), (24, 8)))
        self.add_bezier('sym-e5', (24, 8), ((24.136, 8), (23.904, 8), (24, 8)))
        self.add_bezier('sym-e6', (24, 8), ((24.045, 8), (23.955, 8), (24, 8)))
        self.add_bezier('sym-e7', (24, 8), ((24.045, 8.008), (24.955, 8), (25, 8)))
        self.add_bezier('sym-e8', (25, 8), ((25.364, 8), (25.827, 8.739), (26, 9)))
        self.add_line('sym-e9', (26, 9), (44, 37))
        self.add_bezier('sym-e10', (44, 37), ((44, 37.413), (44, 37.587), (44, 38)))
        self.add_bezier('sym-e11', (44, 38), ((44, 38.926), (41.918, 40), (41, 40)))
        self.add_line('sym-e12', (41, 40), (24, 40))
        self.add_line('sym-e13', (24, 40), (7, 40))
        self.add_bezier('sym-e14', (7, 40), ((6.082, 40), (4, 38.926), (4, 38)))
        self.add_bezier('sym-e15', (4, 38), ((4, 37.587), (4, 37.413), (4, 37)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
