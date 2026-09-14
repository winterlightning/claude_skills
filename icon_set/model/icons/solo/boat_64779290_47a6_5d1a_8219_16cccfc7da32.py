"""Boat (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64779290-47a6-5d1a-8219-16cccfc7da32'
SOURCE_PATH = 'icons-json/transportation/boat_64779290-47a6-5d1a-8219-16cccfc7da32.json'
AUTHOR = 'json_to_solo'

class Boat(Solo48):
    icon_id = 'boat'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('boat', 'transportation')

    def build(self):
        self.add_line('e0', (14, 8), (25, 8))
        self.add_line('e1', (28, 10), (33, 21))
        self.add_line('e2', (18, 8), (13, 22))
        self.add_line('e3', (35, 21), (7, 24))
        self.add_line('e4', (6, 26), (4, 38))
        self.add_line('e5', (4, 40), (32, 40))
        self.add_line('e6', (44, 21), (35, 21))
        self.add_bezier('e7', (25, 8), ((25.273, 8), (25.455, 8.016), (25.727, 8.016)), ((26.427, 8.016), (27.545, 9.056), (28, 10)))
        self.add_bezier('e8', (7, 24), ((6.664, 24.528), (6.3, 25.424), (6, 26)))
        self.add_bezier('e9', (4, 38), ((4, 38.528), (4, 39.472), (4, 40)))
        self.add_bezier('e10', (32, 40), ((32.073, 40), (32.318, 40), (32.391, 40)), ((33.091, 40), (33.991, 39.2), (34.627, 38.752)), ((38.582, 35.856), (41.209, 29.712), (43.218, 23.28)), ((43.391, 22.704), (43.691, 22.224), (43.855, 21.648)), ((44, 20.08), (43.545, 22.424), (44, 21)))
        self.add_contour('c0', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c2')
