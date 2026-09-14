"""R (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0effb3a-dd71-5368-9650-1678a3b7798b'
SOURCE_PATH = 'icons-json/typeface/R_d0effb3a-dd71-5368-9650-1678a3b7798b.json'
AUTHOR = 'json_to_solo'

class RD0effb3a(Solo48):
    icon_id = 'r-d0effb3a'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('r', 'typeface')

    def build(self):
        self.add_line('e0', (8, 25), (26, 25))
        self.add_line('e1', (26, 4), (9, 4))
        self.add_line('e2', (8, 5), (8, 44))
        self.add_line('e3', (40, 44), (26, 25))
        self.add_bezier('e4', (26, 25), ((32.782, 25), (37.932, 21.636), (39.397, 16.918)), ((39.643, 16.127), (39.988, 15.3), (39.988, 14.482)), ((39.988, 14.418), (40, 14.364), (40, 14.3)), ((40, 14.227), (40, 14.164), (39.988, 14.091)), ((39.988, 13.391), (39.766, 12.673), (39.582, 11.991)), ((38.363, 7.555), (34.178, 4.018), (27.717, 4.018)), ((27.446, 4.018), (27.175, 4), (26.905, 4)), ((26.757, 4), (26.148, 4), (26, 4)))
        self.add_bezier('e5', (9, 4), ((8.545, 4.191), (8.025, 4.164), (8.025, 4.745)), ((8.012, 4.8), (8.012, 4.945), (8, 5)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2')
        self.add_contour('c1', 'e3')
