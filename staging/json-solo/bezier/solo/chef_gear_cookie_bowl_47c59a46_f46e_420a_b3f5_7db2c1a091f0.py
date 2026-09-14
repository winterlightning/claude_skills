"""Chef gear cookie bowl (food), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47c59a46-f46e-420a-b3f5-7db2c1a091f0'
SOURCE_PATH = 'icons-json/food/chef gear cookie bowl_47c59a46-f46e-420a-b3f5-7db2c1a091f0.json'
AUTHOR = 'json_to_solo'

class ChefGearCookieBowlFood(Solo48):
    icon_id = 'chef-gear-cookie-bowl-food'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('chef', 'gear', 'cookie', 'bowl', 'food')

    def build(self):
        self.add_line('e0', (39, 21), (39, 23))
        self.add_line('e1', (17, 23), (9, 23))
        self.add_line('e2', (17, 23), (39, 23))
        self.add_line('e3', (39, 23), (42, 23))
        self.add_line('e4', (32, 42), (16, 42))
        self.add_line('e5', (15, 36), (12, 35))
        self.add_line('e6', (6, 23), (9, 23))
        self.add_bezier('e7', (25, 8), ((23.331, 7.092), (21.218, 6.008), (19.287, 6.008)), ((19.102, 6.008), (18.925, 6), (18.74, 6)), ((18.737, 6), (18.734, 6), (18.731, 6)), ((18.608, 6), (18.485, 6.008), (18.363, 6.008)), ((16.334, 6.008), (14.133, 6.859), (12.529, 8.078)), ((7.636, 11.793), (6.226, 17.625), (9, 23)))
        self.add_bezier('e8', (17, 23), ((16.935, 22.018), (16.522, 21.259), (16.579, 20.277)), ((16.825, 15.998), (19.59, 12.136), (23.46, 10.402)), ((24.957, 9.731), (26.585, 9.502), (28.214, 9.584)), ((28.353, 9.592), (28.582, 9.543), (28.664, 9.608)), ((28.696, 9.641), (28.721, 10.672), (28.737, 10.803)), ((28.835, 11.744), (29.13, 12.627), (29.605, 13.445)), ((30.218, 14.493), (31.216, 15.295), (32.378, 15.646)), ((32.599, 15.72), (34.252, 15.908), (34.293, 15.949)), ((34.415, 16.105), (34.44, 17.733), (34.546, 18.093)), ((35.135, 20.114), (37.102, 20.885), (39, 21)))
        self.add_bezier('e9', (42, 23), ((42, 23.229), (41.992, 23.632), (41.992, 23.861)), ((41.992, 24.327), (41.845, 24.851), (41.763, 25.317)), ((41.215, 28.5), (39.529, 31.486), (37.197, 33.712)), ((36.502, 34.375), (35.741, 34.972), (34.955, 35.52)), ((34.407, 35.896), (33.818, 36.224), (33.36, 36.706)), ((32.01, 38.155), (32.755, 39.194), (32.91, 40.83)), ((32.943, 41.174), (32.853, 41.992), (32.337, 41.992)), ((32.288, 42), (32.049, 42), (32, 42)))
        self.add_bezier('e10', (16, 42), ((15.951, 41.525), (15.687, 41.084), (15.745, 40.617)), ((15.908, 39.218), (16.669, 36.835), (15, 36)))
        self.add_bezier('e11', (12, 35), ((11.035, 34.517), (10.181, 33.303), (9.551, 32.468)), ((7.849, 30.235), (6.859, 28.287), (6.262, 25.538)), ((6.155, 25.039), (6.008, 24.417), (6.008, 23.918)), ((6, 23.885), (6, 23.861), (6, 23.836)), ((6, 23.615), (6, 23.221), (6, 23)))
        self.add_contour('c0', 'e7')
        self.add_contour('c1', 'e8', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
