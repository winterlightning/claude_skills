"""Q (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e40e093e-f5b4-5416-8ac1-2cb3ee5d6d0d'
SOURCE_PATH = 'icons-json/typeface/Q_e40e093e-f5b4-5416-8ac1-2cb3ee5d6d0d.json'
AUTHOR = 'json_to_solo'

class Q(Solo48):
    icon_id = 'q'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('q', 'typeface')

    def build(self):
        self.add_line('e0', (8, 14), (8, 29))
        self.add_bezier('e1', (28, 38), ((28.431, 42.027), (29.462, 43.282), (35, 44)))
        self.add_bezier('e2', (28, 38), ((30.56, 37.5), (32.849, 36.6), (34.991, 35.382)), ((37.834, 33.773), (39.692, 31.109), (39.877, 28.455)), ((39.963, 27.273), (39.84, 26.082), (39.84, 24.9)), ((39.852, 23.2), (39.975, 21.491), (39.975, 19.791)), ((39.975, 19.352), (40, 18.923), (40, 18.485)), ((40, 18.478), (40, 18.471), (40, 18.464)), ((40, 17.945), (39.975, 17.427), (39.975, 16.909)), ((39.975, 15.191), (39.902, 13.245), (39.311, 11.573)), ((37.674, 6.973), (31.36, 4.018), (25.12, 4.018)), ((24.732, 4.018), (24.345, 4), (23.957, 4)), ((23.951, 4), (23.945, 4), (23.938, 4)), ((23.446, 4), (22.966, 4.018), (22.474, 4.018)), ((16.714, 4.018), (11.877, 6.5), (9.28, 10.2)), ((8.702, 11.009), (8.025, 12.2), (8.025, 13.136)), ((8.012, 13.273), (8.012, 13.418), (8, 13.564)), ((8, 13.709), (8, 13.855), (8, 14)))
        self.add_bezier('e3', (8, 29), ((8.763, 30.336), (9.415, 32.273), (10.646, 33.491)), ((14.818, 37.618), (21.588, 38.345), (28, 38)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2', 'e0', 'e3')
