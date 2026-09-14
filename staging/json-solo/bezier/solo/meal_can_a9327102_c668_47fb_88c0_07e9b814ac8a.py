"""Meal can (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a9327102-c668-47fb-88c0-07e9b814ac8a'
SOURCE_PATH = 'icons-json/food/meal can_a9327102-c668-47fb-88c0-07e9b814ac8a.json'
AUTHOR = 'json_to_solo'

class MealCanFood(Solo48):
    icon_id = 'meal-can-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('meal', 'can', 'food')

    def build(self):
        self.add_bezier('sym-e0', (24, 16), ((19.672, 16), (14.91, 15.259), (12, 14)))
        self.add_bezier('sym-e1', (12, 14), ((10.366, 13.291), (9.457, 12.091), (8, 11)))
        self.add_line('sym-e2', (8, 11), (8, 38))
        self.add_bezier('sym-e3', (8, 38), ((8.269, 38.764), (8.461, 39.391), (9, 40)))
        self.add_bezier('sym-e4', (9, 40), ((11.754, 43.109), (19.051, 44), (23, 44)))
        self.add_bezier('sym-e5', (23, 44), ((23.196, 44), (23.803, 44), (24, 44)))
        self.add_bezier('sym-e6', (24, 44), ((24.197, 44), (24.804, 44), (25, 44)))
        self.add_bezier('sym-e7', (25, 44), ((28.949, 44), (36.246, 43.109), (39, 40)))
        self.add_bezier('sym-e8', (39, 40), ((39.539, 39.391), (39.731, 38.764), (40, 38)))
        self.add_line('sym-e9', (40, 38), (40, 11))
        self.add_bezier('sym-e10', (40, 11), ((38.543, 12.091), (37.634, 13.291), (36, 14)))
        self.add_bezier('sym-e11', (36, 14), ((33.09, 15.259), (28.328, 16), (24, 16)))
        self.add_bezier('sym-e12', (24, 4), ((23.613, 4), (23.389, 4), (23, 4)))
        self.add_bezier('sym-e13', (23, 4), ((19.152, 4), (14.537, 4.318), (11, 6)))
        self.add_bezier('sym-e14', (11, 6), ((9.914, 6.518), (8, 8.482), (8, 10)))
        self.add_bezier('sym-e15', (8, 10), ((8, 10.318), (8, 10.682), (8, 11)))
        self.add_bezier('sym-e16', (8, 11), ((8, 11.245), (8, 10.755), (8, 11)))
        self.add_bezier('sym-e17', (16, 23), ((18.808, 23.591), (21.194, 24), (24, 24)))
        self.add_bezier('sym-e18', (24, 24), ((26.806, 24), (29.192, 23.591), (32, 23)))
        self.add_line('sym-e19', (32, 23), (32, 35))
        self.add_bezier('sym-e20', (32, 35), ((29.179, 35.673), (26.8, 36), (24, 36)))
        self.add_bezier('sym-e21', (24, 36), ((21.2, 36), (18.821, 35.673), (16, 35)))
        self.add_line('sym-e22', (16, 35), (16, 23))
        self.add_bezier('sym-e23', (24, 4), ((24.387, 4), (24.611, 4), (25, 4)))
        self.add_bezier('sym-e24', (25, 4), ((28.848, 4), (33.463, 4.318), (37, 6)))
        self.add_bezier('sym-e25', (37, 6), ((38.086, 6.518), (40, 8.482), (40, 10)))
        self.add_bezier('sym-e26', (40, 10), ((40, 10.318), (40, 10.682), (40, 11)))
        self.add_bezier('sym-e27', (40, 11), ((40, 11.245), (40, 10.755), (40, 11)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c2', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', closed=True)
        self.add_contour('sym-c3', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
