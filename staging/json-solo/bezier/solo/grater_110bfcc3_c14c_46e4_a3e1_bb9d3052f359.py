"""Grater (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '110bfcc3-c14c-46e4-a3e1-bb9d3052f359'
SOURCE_PATH = 'icons-json/food/grater_110bfcc3-c14c-46e4-a3e1-bb9d3052f359.json'
AUTHOR = 'json_to_solo'

class GraterFood(Solo48):
    icon_id = 'grater-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('grater', 'food')

    def build(self):
        self.add_line('sym-e0', (9, 12), (24, 12))
        self.add_line('sym-e1', (24, 12), (39, 12))
        self.add_line('sym-e2', (39, 12), (40, 41))
        self.add_bezier('sym-e3', (40, 41), ((40, 41.091), (40, 41.909), (40, 42)))
        self.add_bezier('sym-e4', (40, 42), ((40, 43.218), (39.02, 43.455), (38, 44)))
        self.add_line('sym-e5', (38, 44), (24, 44))
        self.add_line('sym-e6', (24, 44), (10, 44))
        self.add_bezier('sym-e7', (10, 44), ((8.98, 43.455), (8, 43.218), (8, 42)))
        self.add_bezier('sym-e8', (8, 42), ((8, 41.909), (8, 41.091), (8, 41)))
        self.add_line('sym-e9', (8, 41), (9, 12))
        self.add_bezier('sym-e10', (9, 12), ((9.11, 8.918), (9.73, 6.7), (13, 5)))
        self.add_bezier('sym-e11', (13, 5), ((13.61, 4.682), (14.28, 4), (15, 4)))
        self.add_line('sym-e12', (15, 4), (24, 4))
        self.add_line('sym-e13', (24, 4), (33, 4))
        self.add_bezier('sym-e14', (33, 4), ((33.72, 4), (34.39, 4.682), (35, 5)))
        self.add_bezier('sym-e15', (35, 5), ((38.27, 6.7), (38.89, 8.918), (39, 12)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
