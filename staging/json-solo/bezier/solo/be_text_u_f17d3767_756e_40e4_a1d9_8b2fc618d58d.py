"""Be (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f17d3767-756e-40e4-a1d9-8b2fc618d58d'
SOURCE_PATH = 'icons-json/symbol/be (text u)_f17d3767-756e-40e4-a1d9-8b2fc618d58d.json'
AUTHOR = 'json_to_solo'

class BeTextUSymbol(Solo48):
    icon_id = 'be-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('be', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (15, 4), (8, 4))
        self.add_line('e1', (8, 4), (8, 27))
        self.add_line('e2', (8, 27), (13, 27))
        self.add_line('e3', (16, 15), (8, 15))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_bezier('e5', (13, 27), ((14.886, 27), (17.011, 26.8), (18.678, 25.673)), ((21.145, 24), (22.013, 19.945), (20.168, 17.4)), ((19.293, 16.191), (18.013, 15.6), (16.682, 15.227)), ((16.362, 15.127), (15.848, 15.1), (15.579, 14.909)), ((15.571, 14.9), (15.874, 14.845), (16.227, 14.727)), ((16.691, 14.582), (17.154, 14.391), (17.566, 14.127)), ((18.813, 13.355), (19.731, 12.082), (20.042, 10.564)), ((20.817, 6.773), (18.478, 4), (15, 4)))
        self.add_bezier('e6', (30, 19), ((31.558, 19.191), (33.011, 19.8), (34.577, 19.827)), ((35.815, 19.855), (37.617, 20.036), (38.728, 19.327)), ((40, 18.273), (39.52, 14.673), (38.417, 13.491)), ((36.118, 11.018), (32.345, 12.073), (30.611, 14.709)), ((28.48, 17.945), (29.044, 25.227), (33.255, 26.218)), ((35.301, 26.7), (38.299, 26.1), (39.571, 24.127)), ((39.731, 23.882), (39.992, 23.464), (39.992, 23.145)), ((39.992, 23.127), (40, 23.018), (40, 23)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e5', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e6')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
