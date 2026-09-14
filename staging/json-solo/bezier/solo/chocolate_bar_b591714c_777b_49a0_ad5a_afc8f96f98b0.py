"""Chocolate bar (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b591714c-777b-49a0-ad5a-afc8f96f98b0'
SOURCE_PATH = 'icons-json/food/chocolate bar_b591714c-777b-49a0-ad5a-afc8f96f98b0.json'
AUTHOR = 'json_to_solo'

class ChocolateBarFood(Solo48):
    icon_id = 'chocolate-bar-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('chocolate', 'bar', 'food')

    def build(self):
        self.add_line('e0', (35, 21), (23, 29))
        self.add_line('e1', (18, 30), (8, 27))
        self.add_line('e2', (35, 21), (24, 21))
        self.add_line('e3', (35, 21), (38, 21))
        self.add_line('e4', (10, 12), (38, 12))
        self.add_line('e5', (10, 12), (10, 21))
        self.add_line('e6', (10, 12), (10, 5))
        self.add_line('e7', (11, 4), (24, 4))
        self.add_line('e8', (24, 21), (24, 4))
        self.add_line('e9', (24, 21), (10, 21))
        self.add_line('e10', (38, 12), (38, 21))
        self.add_line('e11', (38, 12), (38, 5))
        self.add_line('e12', (37, 4), (24, 4))
        self.add_line('e13', (8, 22), (8, 27))
        self.add_line('e14', (8, 27), (8, 41))
        self.add_line('e15', (11, 44), (37, 44))
        self.add_line('e16', (40, 41), (40, 22))
        self.add_bezier('e17', (23, 29), ((21.93, 29.727), (19.33, 30.482), (18, 30)))
        self.add_bezier('e18', (10, 5), ((10.19, 4.745), (10.25, 4.309), (10.57, 4.136)), ((10.71, 4.091), (10.86, 4.045), (11, 4)))
        self.add_bezier('e19', (38, 5), ((37.81, 4.755), (37.74, 4.309), (37.43, 4.155)), ((37.3, 4.082), (37.12, 4.091), (37, 4)))
        self.add_bezier('e20', (10, 21), ((9.5, 21), (8.02, 21.373), (8.02, 22.091)), ((8.01, 22.118), (8.01, 21.973), (8, 22)))
        self.add_bezier('e21', (8, 41), ((8.41, 42.036), (8.92, 43.091), (10.04, 43.645)), ((10.31, 43.773), (10.69, 44), (11, 44)))
        self.add_bezier('e22', (37, 44), ((37.05, 43.991), (37.09, 43.991), (37.14, 43.982)), ((38.08, 43.982), (39.98, 42.227), (39.98, 41.373)), ((39.99, 41.336), (39.99, 41.036), (40, 41)))
        self.add_bezier('e23', (40, 22), ((39.91, 21.891), (39.9, 21.891), (39.8, 21.773)), ((39.36, 21.273), (38.63, 21.055), (38, 21)))
        self.add_contour('c0', 'e0', 'e17', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6', 'e18', 'e7')
        self.add_contour('c6', 'e8')
        self.add_contour('c7', 'e9')
        self.add_contour('c8', 'e10')
        self.add_contour('c9', 'e11', 'e19', 'e12')
        self.add_contour('c10', 'e20', 'e13')
        self.add_contour('c11', 'e14', 'e21', 'e15', 'e22', 'e16', 'e23')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c10')
        self.relate('connect', 'c0', 'c11')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c11', 'c2')
        self.relate('connect', 'c11', 'c8')
        self.relate('connect', 'c2', 'c8')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c8')
        self.relate('connect', 'c3', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c10', 'c4')
        self.relate('connect', 'c10', 'c7')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c6', 'c9')
