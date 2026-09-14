"""Head (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97903c22-da46-4913-b7f3-4e20608ab202'
SOURCE_PATH = 'icons-json/symbol/head_97903c22-da46-4913-b7f3-4e20608ab202.json'
AUTHOR = 'json_to_solo'

class HeadSymbol(Solo48):
    icon_id = 'head-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('head', 'symbol')

    def build(self):
        self.add_line('e0', (12, 44), (12, 32))
        self.add_line('e1', (36, 14), (40, 27))
        self.add_line('e2', (37, 28), (37, 33))
        self.add_line('e3', (32, 38), (29, 38))
        self.add_line('e4', (29, 38), (29, 44))
        self.add_bezier('e5', (12, 32), ((12, 31.727), (12.168, 31.591), (12.051, 31.345)), ((11.882, 30.973), (11.486, 30.673), (11.242, 30.364)), ((10.771, 29.764), (10.383, 29.127), (10.038, 28.436)), ((8.96, 26.282), (8.008, 22.891), (8.008, 20.464)), ((8.008, 20.338), (8, 20.213), (8, 20.096)), ((8, 20.095), (8, 20.093), (8, 20.091)), ((8, 19.8), (8.008, 19.5), (8.008, 19.209)), ((8.008, 11.045), (14.543, 4.018), (22.097, 4.018)), ((22.291, 4.018), (22.476, 4), (22.669, 4)), ((22.67, 4), (22.671, 4), (22.672, 4)), ((22.731, 4), (22.797, 4), (22.855, 4)), ((28.893, 4), (33.979, 7.891), (36, 14)))
        self.add_bezier('e6', (40, 27), ((39.882, 27.164), (39.891, 27.091), (39.756, 27.245)), ((39.183, 27.855), (37.699, 27.991), (37, 28)))
        self.add_bezier('e7', (37, 33), ((37, 35.045), (33.886, 38), (32, 38)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e4')
