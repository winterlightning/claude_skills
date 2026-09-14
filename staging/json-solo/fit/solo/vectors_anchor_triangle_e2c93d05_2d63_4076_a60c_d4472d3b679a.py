"""Vectors anchor triangle (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_line('sym-e1', (22, 9), (23, 8))
        self.add_line('sym-e2', (23, 8), (24, 8))
        self.add_line('sym-e7', (24, 8), (25, 8))
        self.add_line('sym-e8', (25, 8), (26, 9))
        self.add_line('sym-e9', (26, 9), (44, 37))
        self.add_line('sym-e10', (44, 37), (44, 38))
        self.add_arc('sym-e11', (44, 38), (41, 40), radius_x=4)
        self.add_line('sym-e12', (41, 40), (24, 40))
        self.add_line('sym-e13', (24, 40), (7, 40))
        self.add_arc('sym-e14', (7, 40), (4, 38), radius_x=4)
        self.add_line('sym-e15', (4, 38), (4, 37))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
