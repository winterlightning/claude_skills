"""Ice cream cone (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89acf638-2184-527a-8681-8ad6b144260c'
SOURCE_PATH = 'pictographic-primitives/food/ice cream cone_89acf638-2184-527a-8681-8ad6b144260c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class IceCreamConeFood(Solo48):
    icon_id = 'ice-cream-cone-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('ice', 'cream', 'cone', 'food')

    def build(self):
        self.add_line('e0', (12, 22), (23, 42))
        self.add_line('e1', (23, 42), (24, 44))
        self.add_line('e2', (24, 44), (36, 23))
        self.add_line('e3', (34, 7), (29, 5))
        self.add_bezier('e4', (30, 21), ((29.04, 21.636), (28.246, 22.627), (27.126, 23.091)), ((25.157, 23.909), (22.523, 23.564), (20.8, 22.591)), ((20.086, 22.182), (19.96, 21.755), (19, 21)))
        self.add_bezier('e5', (36, 23), ((37.822, 22.118), (39.988, 21.064), (39.988, 19.282)), ((39.988, 19.139), (40, 19.004), (40, 18.861)), ((40, 18.859), (40, 18.857), (40, 18.855)), ((39.988, 18.709), (39.988, 18.564), (39.975, 18.418)), ((39.975, 17.582), (39.569, 16.664), (38.942, 15.982)), ((38.72, 15.755), (38.277, 15.427), (38.191, 15.145)), ((38.018, 14.555), (38.289, 13.591), (38.203, 12.927)), ((37.945, 11.009), (36.498, 7.927), (34, 7)))
        self.add_bezier('e6', (29, 5), ((27.265, 4.645), (25.255, 4.009), (23.446, 4.009)), ((23.349, 4.009), (23.252, 4), (23.167, 4)), ((23.166, 4), (23.164, 4), (23.163, 4)), ((23.077, 4.009), (22.991, 4.009), (22.917, 4.018)), ((22.006, 4.018), (21.022, 4.291), (20.172, 4.473)), ((15.766, 5.445), (12.271, 7.718), (10.745, 10.982)), ((10.068, 12.427), (10.388, 13.573), (10.006, 14.918)), ((9.723, 15.9), (8.012, 16.545), (8.012, 18.018)), ((8, 18.081), (8, 18.135), (8, 18.197)), ((8, 18.198), (8, 18.199), (8, 18.2)), ((8, 18.318), (8.012, 18.445), (8.012, 18.564)), ((8.012, 20.055), (9.858, 21.664), (11.692, 22.182)), ((14.511, 22.982), (16.822, 22.527), (19, 21)))
        self.add_bezier('e7', (36, 23), ((33.231, 23.091), (31.957, 22.427), (30, 21)))
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e0', 'e1', 'e2')
        self.add_contour('c2', 'e5', 'e3', 'e6')
        self.add_contour('c3', 'e7')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
