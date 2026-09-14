"""Rounded rectangle shape (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5957fd82-3c5a-4a75-8fed-377ad2e68869'
SOURCE_PATH = 'icons-json/design/rounded rectangle shape_5957fd82-3c5a-4a75-8fed-377ad2e68869.json'
AUTHOR = 'json_to_solo'

class RoundedRectangleShape5957fd82(Solo48):
    icon_id = 'rounded-rectangle-shape-5957fd82'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rounded', 'rectangle', 'shape', 'design')

    def build(self):
        self.add_line('sym-e0', (24, 40), (14, 40))
        self.add_bezier('sym-e1', (14, 40), ((13.3, 40), (12.655, 39.32), (12, 39)))
        self.add_bezier('sym-e2', (12, 39), ((7.7, 36.871), (4, 31.363), (4, 25)))
        self.add_bezier('sym-e3', (4, 25), ((4, 24.902), (4, 25.098), (4, 25)))
        self.add_bezier('sym-e4', (4, 25), ((4, 24.631), (4, 23.369), (4, 23)))
        self.add_bezier('sym-e5', (4, 23), ((4, 16.317), (7.482, 11.166), (12, 9)))
        self.add_bezier('sym-e6', (12, 9), ((12.909, 8.569), (14.018, 8), (15, 8)))
        self.add_bezier('sym-e7', (15, 8), ((15.136, 8), (14.864, 8), (15, 8)))
        self.add_bezier('sym-e8', (15, 8), ((15.136, 8), (15.864, 8), (16, 8)))
        self.add_line('sym-e9', (16, 8), (24, 8))
        self.add_line('sym-e10', (24, 8), (32, 8))
        self.add_bezier('sym-e11', (32, 8), ((32.136, 8), (32.864, 8), (33, 8)))
        self.add_bezier('sym-e12', (33, 8), ((33.136, 8), (32.864, 8), (33, 8)))
        self.add_bezier('sym-e13', (33, 8), ((33.982, 8), (35.091, 8.569), (36, 9)))
        self.add_bezier('sym-e14', (36, 9), ((40.518, 11.166), (44, 16.317), (44, 23)))
        self.add_bezier('sym-e15', (44, 23), ((44, 23.369), (44, 24.631), (44, 25)))
        self.add_bezier('sym-e16', (44, 25), ((44, 25.098), (44, 24.902), (44, 25)))
        self.add_bezier('sym-e17', (44, 25), ((44, 31.363), (40.3, 36.871), (36, 39)))
        self.add_bezier('sym-e18', (36, 39), ((35.345, 39.32), (34.7, 40), (34, 40)))
        self.add_line('sym-e19', (34, 40), (24, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
