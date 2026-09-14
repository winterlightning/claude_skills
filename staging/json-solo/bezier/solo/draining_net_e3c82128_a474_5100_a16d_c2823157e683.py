"""Draining net (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3c82128-a474-5100-a16d-c2823157e683'
SOURCE_PATH = 'icons-json/food/draining net_e3c82128-a474-5100-a16d-c2823157e683.json'
AUTHOR = 'json_to_solo'

class DrainingNetFood(Solo48):
    icon_id = 'draining-net-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('draining', 'net', 'food')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 44))
        self.add_line('sym-e1', (24, 4), (24, 4))
        self.add_bezier('sym-e2', (24, 4), ((21.747, 4), (19, 6.359), (19, 8)))
        self.add_bezier('sym-e3', (19, 8), ((19, 8.037), (18.997, 7.963), (19, 8)))
        self.add_line('sym-e4', (19, 8), (20, 23))
        self.add_bezier('sym-e5', (20, 23), ((14.853, 24.282), (10.533, 26.2), (9, 30)))
        self.add_bezier('sym-e6', (9, 30), ((8.72, 30.7), (8, 31.264), (8, 32)))
        self.add_bezier('sym-e7', (8, 32), ((8, 32.3), (8, 32.691), (8, 33)))
        self.add_bezier('sym-e8', (8, 33), ((8, 33.218), (8, 33.782), (8, 34)))
        self.add_bezier('sym-e9', (8, 34), ((8, 38.955), (15.76, 44), (23, 44)))
        self.add_bezier('sym-e10', (24, 44), ((23.825, 44), (23.172, 44), (23, 44)))
        self.add_bezier('sym-e11', (24, 44), ((24.175, 44), (24.828, 44), (25, 44)))
        self.add_bezier('sym-e12', (25, 44), ((32.24, 44), (40, 38.955), (40, 34)))
        self.add_bezier('sym-e13', (40, 34), ((40, 33.782), (40, 33.218), (40, 33)))
        self.add_bezier('sym-e14', (40, 33), ((40, 32.691), (40, 32.3), (40, 32)))
        self.add_bezier('sym-e15', (40, 32), ((40, 31.264), (39.28, 30.7), (39, 30)))
        self.add_bezier('sym-e16', (39, 30), ((37.467, 26.2), (33.147, 24.282), (28, 23)))
        self.add_line('sym-e17', (28, 23), (29, 8))
        self.add_bezier('sym-e18', (29, 8), ((29.003, 7.963), (29, 8.037), (29, 8)))
        self.add_bezier('sym-e19', (29, 8), ((29, 6.359), (26.253, 4), (24, 4)))
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10')
        self.add_contour('sym-c3', 'sym-e11')
        self.add_contour('sym-c4', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c3')
