"""Oval (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a24b950-1725-4da0-b49d-dcbe11225bd1'
SOURCE_PATH = 'icons-json/design/oval_1a24b950-1725-4da0-b49d-dcbe11225bd1.json'
AUTHOR = 'json_to_solo'

class Oval1a24b950(Solo48):
    icon_id = 'oval-1a24b950'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('oval', 'design')

    def build(self):
        self.add_bezier('sym-e0', (24, 40), ((24.045, 40), (23.955, 40), (24, 40)))
        self.add_bezier('sym-e1', (24, 40), ((24.345, 40), (24.664, 40), (25, 40)))
        self.add_bezier('sym-e2', (25, 40), ((26.682, 40), (28.345, 39.369), (30, 39)))
        self.add_bezier('sym-e3', (30, 39), ((36.055, 37.683), (44, 33.994), (44, 24)))
        self.add_bezier('sym-e4', (44, 24), ((44, 23.918), (44, 24.082), (44, 24)))
        self.add_bezier('sym-e5', (44, 24), ((44, 23.918), (44, 24.082), (44, 24)))
        self.add_bezier('sym-e6', (44, 24), ((44, 14.006), (36.055, 10.317), (30, 9)))
        self.add_bezier('sym-e7', (30, 9), ((28.345, 8.631), (26.682, 8), (25, 8)))
        self.add_bezier('sym-e8', (25, 8), ((24.664, 8), (24.345, 8), (24, 8)))
        self.add_bezier('sym-e9', (24, 8), ((23.955, 8), (24.045, 8), (24, 8)))
        self.add_bezier('sym-e10', (24, 8), ((23.955, 8), (24.045, 8), (24, 8)))
        self.add_bezier('sym-e11', (24, 8), ((23.655, 8), (23.336, 8), (23, 8)))
        self.add_bezier('sym-e12', (23, 8), ((21.318, 8), (19.655, 8.631), (18, 9)))
        self.add_bezier('sym-e13', (18, 9), ((11.945, 10.317), (4, 14.006), (4, 24)))
        self.add_bezier('sym-e14', (4, 24), ((4, 24.082), (4, 23.918), (4, 24)))
        self.add_bezier('sym-e15', (4, 24), ((4, 24.082), (4, 23.918), (4, 24)))
        self.add_bezier('sym-e16', (4, 24), ((4, 33.994), (11.945, 37.683), (18, 39)))
        self.add_bezier('sym-e17', (18, 39), ((19.655, 39.369), (21.318, 40), (23, 40)))
        self.add_bezier('sym-e18', (23, 40), ((23.336, 40), (23.655, 40), (24, 40)))
        self.add_bezier('sym-e19', (24, 40), ((24.045, 40), (23.955, 40), (24, 40)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
