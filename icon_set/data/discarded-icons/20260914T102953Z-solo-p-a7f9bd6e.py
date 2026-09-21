"""P (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7f9bd6e-79b1-485f-9b27-0d7d582c06cb'
SOURCE_PATH = 'icons-json/typeface/p_a7f9bd6e-79b1-485f-9b27-0d7d582c06cb.json'
AUTHOR = 'json_to_solo'

class PA7f9bd6e(Solo48):
    icon_id = 'p-a7f9bd6e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('p', 'typeface')

    def build(self):
        self.add_line('e0', (8, 15), (8, 44))
        self.add_bezier('e1', (8, 29), ((17.317, 29.227), (29.551, 30.473), (36.271, 24.291)), ((37.44, 23.227), (38.585, 22.018), (39.065, 20.682)), ((39.557, 19.336), (39.988, 17.864), (39.988, 16.455)), ((39.988, 16.383), (40, 16.311), (40, 16.24)), ((40, 16.239), (40, 16.237), (40, 16.236)), ((39.988, 16.164), (39.988, 16.091), (39.975, 16.018)), ((39.975, 12.609), (37.674, 8.664), (34.018, 6.509)), ((30.855, 4.645), (26.572, 4.018), (22.634, 4.018)), ((22.343, 4.018), (22.064, 4), (21.774, 4)), ((21.769, 4), (21.765, 4), (21.76, 4)), ((15.963, 4), (10.942, 6.191), (8.898, 10.264)), ((8.431, 11.2), (8.012, 12.245), (8.012, 13.264)), ((8, 13.336), (8, 13.418), (8, 13.5)), ((8, 13.973), (8, 14.527), (8, 15)))
        self.add_contour('c0', 'e1', 'e0')
