"""Sign badge badge (maps), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0606d6db-2248-5c0f-86c8-a52713867ba6'
SOURCE_PATH = 'icons-json/maps/sign badge badge_0606d6db-2248-5c0f-86c8-a52713867ba6.json'
AUTHOR = 'json_to_solo'

class SignBadgeBadge0606d6db(Solo48):
    icon_id = 'sign-badge-badge-0606d6db'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('sign', 'badge', 'maps')

    def build(self):
        self.add_line('e0', (27, 42), (24, 44))
        self.add_line('e1', (9, 24), (11, 20))
        self.add_line('e2', (11, 12), (8, 9))
        self.add_line('e3', (8, 9), (12, 4))
        self.add_line('e4', (12, 4), (18, 8))
        self.add_line('e5', (18, 8), (24, 4))
        self.add_line('e6', (24, 4), (30, 8))
        self.add_line('e7', (30, 8), (36, 4))
        self.add_line('e8', (36, 4), (39, 9))
        self.add_bezier('e9', (39, 9), ((36.684, 11.955), (34.989, 14.791), (36.665, 18.736)), ((37.886, 21.618), (39.992, 23.382), (39.992, 26.882)), ((39.992, 27.025), (40, 27.177), (40, 27.32)), ((40, 27.323), (40, 27.325), (40, 27.327)), ((40, 27.627), (39.983, 27.918), (39.983, 28.218)), ((39.983, 29.236), (39.697, 30.245), (39.394, 31.2)), ((37.566, 36.973), (31.674, 39.482), (27, 42)))
        self.add_bezier('e10', (24, 44), ((18.307, 41.927), (8.008, 35.718), (8.008, 28.164)), ((8.008, 28.018), (8, 27.873), (8, 27.727)), ((8.008, 27.664), (8.008, 27.6), (8.017, 27.536)), ((8.017, 26.718), (8.688, 24.673), (9, 24)))
        self.add_bezier('e11', (11, 20), ((11.404, 19.127), (11.411, 18.673), (11.739, 17.755)), ((12.295, 16.173), (12.229, 13.327), (11, 12)))
        self.add_contour('c0', 'e9', 'e0', 'e10', 'e1', 'e11', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', closed=True)
