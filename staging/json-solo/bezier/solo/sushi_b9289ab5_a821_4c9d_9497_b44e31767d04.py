"""Sushi (food), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9289ab5-a821-4c9d-9497-b44e31767d04'
SOURCE_PATH = 'icons-json/food/sushi_b9289ab5-a821-4c9d-9497-b44e31767d04.json'
AUTHOR = 'json_to_solo'

class SushiFood(Solo48):
    icon_id = 'sushi-food'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('sushi', 'food')

    def build(self):
        self.add_line('e0', (34, 40), (14, 40))
        self.add_line('e1', (40, 30), (42, 30))
        self.add_line('e2', (12, 25), (19, 9))
        self.add_line('e3', (34, 24), (39, 14))
        self.add_line('e4', (24, 22), (30, 9))
        self.add_bezier('e5', (40, 30), ((38.236, 27.46), (36.636, 25.39), (34, 24)))
        self.add_bezier('e6', (40, 30), ((39.882, 33.73), (39.927, 36.75), (36.764, 38.92)), ((35.991, 39.45), (34.936, 40), (34, 40)))
        self.add_bezier('e7', (14, 40), ((13.082, 40), (12.064, 39.51), (11.282, 39.01)), ((8.055, 36.91), (8.191, 33.68), (8, 30)))
        self.add_bezier('e8', (42, 30), ((42.973, 29.45), (43.991, 28.84), (43.991, 27.46)), ((43.991, 27.371), (44, 27.273), (44, 27.184)), ((44, 27.183), (44, 27.181), (44, 27.18)), ((44, 27.09), (43.991, 27.01), (43.991, 26.93)), ((43.991, 21.96), (41.991, 17.52), (39, 14)))
        self.add_bezier('e9', (8, 30), ((9.382, 28.14), (10.245, 26.45), (12, 25)))
        self.add_bezier('e10', (8, 30), ((7.573, 30.08), (6.709, 30.24), (6.245, 30.21)), ((5.045, 30.14), (4.018, 28.84), (4.018, 27.52)), ((4.009, 27.42), (4.009, 27.31), (4, 27.2)), ((4, 27.198), (4, 27.196), (4, 27.194)), ((4, 27.066), (4.018, 26.948), (4.018, 26.82)), ((4.018, 24.93), (4.591, 22.98), (5.209, 21.24)), ((7.791, 14.01), (12.373, 10.65), (19, 9)))
        self.add_bezier('e11', (12, 25), ((16.018, 22.68), (19.473, 21.88), (24, 22)))
        self.add_bezier('e12', (34, 24), ((30.827, 22.48), (27.427, 22.09), (24, 22)))
        self.add_bezier('e13', (30, 9), ((33.127, 10.03), (36.555, 11.62), (39, 14)))
        self.add_bezier('e14', (30, 9), ((28.6, 8.56), (27.391, 8.01), (25.918, 8.01)), ((25.856, 8.01), (25.793, 8), (25.73, 8)), ((25.729, 8), (25.728, 8), (25.727, 8)), ((25.527, 8), (25.327, 8.01), (25.127, 8.01)), ((23.273, 8.01), (20.818, 8.56), (19, 9)))
        self.add_contour('c0', 'e5')
        self.add_contour('c1', 'e6', 'e0', 'e7')
        self.add_contour('c2', 'e1', 'e8')
        self.add_contour('c3', 'e9')
        self.add_contour('c4', 'e10')
        self.add_contour('c5', 'e11')
        self.add_contour('c6', 'e2')
        self.add_contour('c7', 'e3')
        self.add_contour('c8', 'e12')
        self.add_contour('c9', 'e4')
        self.add_contour('c10', 'e13')
        self.add_contour('c11', 'e14')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c0', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c10', 'c2')
        self.relate('connect', 'c10', 'c7')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c11', 'c4')
        self.relate('connect', 'c11', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c11', 'c9')
