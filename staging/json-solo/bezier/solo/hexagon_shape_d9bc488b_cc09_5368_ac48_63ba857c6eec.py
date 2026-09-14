"""Hexagon shape (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9bc488b-cc09-5368-ac48-63ba857c6eec'
SOURCE_PATH = 'icons-json/design/hexagon shape_d9bc488b-cc09-5368-ac48-63ba857c6eec.json'
AUTHOR = 'json_to_solo'

class HexagonShapeD9bc488b(Solo48):
    icon_id = 'hexagon-shape-d9bc488b'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('hexagon', 'shape', 'design')

    def build(self):
        self.add_bezier('sym-e0', (24, 44), ((24.281, 44), (24.719, 44), (25, 44)))
        self.add_line('sym-e1', (25, 44), (38, 35))
        self.add_bezier('sym-e2', (38, 35), ((38.884, 34.4), (40, 33.2), (40, 32)))
        self.add_bezier('sym-e3', (40, 32), ((40, 31.873), (39.992, 32.127), (40, 32)))
        self.add_bezier('sym-e4', (40, 32), ((40, 31.827), (40, 31.173), (40, 31)))
        self.add_line('sym-e5', (40, 31), (40, 24))
        self.add_line('sym-e6', (40, 24), (40, 17))
        self.add_bezier('sym-e7', (40, 17), ((40, 16.827), (40, 16.173), (40, 16)))
        self.add_bezier('sym-e8', (40, 16), ((39.992, 15.873), (40, 16.127), (40, 16)))
        self.add_bezier('sym-e9', (40, 16), ((40, 14.8), (38.884, 13.6), (38, 13)))
        self.add_line('sym-e10', (38, 13), (25, 4))
        self.add_bezier('sym-e11', (25, 4), ((24.719, 4), (24.281, 4), (24, 4)))
        self.add_bezier('sym-e12', (24, 4), ((23.719, 4), (23.281, 4), (23, 4)))
        self.add_line('sym-e13', (23, 4), (10, 13))
        self.add_bezier('sym-e14', (10, 13), ((9.116, 13.6), (8, 14.8), (8, 16)))
        self.add_bezier('sym-e15', (8, 16), ((8, 16.127), (8.008, 15.873), (8, 16)))
        self.add_bezier('sym-e16', (8, 16), ((8, 16.173), (8, 16.827), (8, 17)))
        self.add_line('sym-e17', (8, 17), (8, 24))
        self.add_line('sym-e18', (8, 24), (8, 31))
        self.add_bezier('sym-e19', (8, 31), ((8, 31.173), (8, 31.827), (8, 32)))
        self.add_bezier('sym-e20', (8, 32), ((8.008, 32.127), (8, 31.873), (8, 32)))
        self.add_bezier('sym-e21', (8, 32), ((8, 33.2), (9.116, 34.4), (10, 35)))
        self.add_line('sym-e22', (10, 35), (23, 44))
        self.add_bezier('sym-e23', (23, 44), ((23.281, 44), (23.719, 44), (24, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
