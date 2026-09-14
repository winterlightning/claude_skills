"""Rounded rectangle shape (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '787addf8-2230-543a-ba7e-a43cf42d887d'
SOURCE_PATH = 'icons-json/design/rounded rectangle shape_787addf8-2230-543a-ba7e-a43cf42d887d.json'
AUTHOR = 'json_to_solo'

class RoundedRectangleShape787addf8(Solo48):
    icon_id = 'rounded-rectangle-shape-787addf8'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rounded', 'rectangle', 'shape', 'design')

    def build(self):
        self.add_bezier('sym-e0', (4, 24), ((4, 23.996), (4, 24.004), (4, 24)))
        self.add_bezier('sym-e1', (4, 24), ((4, 23.815), (4, 23.197), (4, 23)))
        self.add_bezier('sym-e2', (4, 23), ((4, 16.132), (8.182, 9.698), (13, 8)))
        self.add_bezier('sym-e3', (13, 8), ((13.673, 8), (14.309, 8), (15, 8)))
        self.add_line('sym-e4', (15, 8), (33, 8))
        self.add_bezier('sym-e5', (33, 8), ((33.082, 8), (32.918, 8), (33, 8)))
        self.add_bezier('sym-e6', (33, 8), ((38.445, 8), (44, 15.849), (44, 23)))
        self.add_bezier('sym-e7', (44, 23), ((44, 23.275), (44, 23.737), (44, 24)))
        self.add_bezier('sym-e8', (44, 24), ((44, 24.263), (44, 24.725), (44, 25)))
        self.add_bezier('sym-e9', (44, 25), ((44, 32.151), (38.445, 40), (33, 40)))
        self.add_bezier('sym-e10', (33, 40), ((32.918, 40), (33.082, 40), (33, 40)))
        self.add_line('sym-e11', (33, 40), (15, 40))
        self.add_bezier('sym-e12', (15, 40), ((14.309, 40), (13.673, 40), (13, 40)))
        self.add_bezier('sym-e13', (13, 40), ((8.182, 38.302), (4, 31.868), (4, 25)))
        self.add_bezier('sym-e14', (4, 25), ((4, 24.803), (4, 24.185), (4, 24)))
        self.add_bezier('sym-e15', (4, 24), ((4, 23.996), (4, 24.004), (4, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
