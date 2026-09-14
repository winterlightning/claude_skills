"""Gd (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '211bf430-9cef-4aa6-a5a0-5ccec5c0924e'
SOURCE_PATH = 'icons-json/symbol/gd (text u)_211bf430-9cef-4aa6-a5a0-5ccec5c0924e.json'
AUTHOR = 'json_to_solo'

class GdTextUSymbol(Solo48):
    icon_id = 'gd-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('gd', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (21, 19), (21, 16))
        self.add_line('e1', (21, 16), (16, 16))
        self.add_line('e2', (40, 4), (40, 23))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_bezier('e4', (21, 8), ((20.065, 5.827), (18.08, 4.018), (15.722, 4.018)), ((15.596, 4.009), (15.469, 4), (15.343, 4)), ((15.208, 4), (15.074, 4.009), (14.931, 4.009)), ((14.114, 4.009), (13.314, 4.255), (12.547, 4.555)), ((8.665, 6.1), (8.008, 10.845), (8.008, 14.773)), ((8.008, 15.091), (8, 15.409), (8, 15.727)), ((8, 16.109), (8.017, 16.482), (8.017, 16.855)), ((8.017, 19.636), (8.623, 22.891), (10.686, 24.764)), ((13.625, 27.427), (18.459, 26.891), (20.48, 23.236)), ((21.263, 21.8), (21, 20.636), (21, 19)))
        self.add_bezier('e5', (40, 23), ((40, 22.982), (39.992, 23.127), (39.992, 23.145)), ((39.992, 23.5), (39.731, 23.964), (39.571, 24.245)), ((38.408, 26.309), (35.739, 26.845), (33.684, 26.373)), ((30.611, 25.655), (29.095, 22.082), (29.086, 18.945)), ((29.078, 15.464), (31.385, 12.136), (34.611, 11.591)), ((36.202, 11.327), (37.819, 11.773), (39.065, 12.882)), ((39.267, 13.064), (39.992, 13.636), (39.992, 13.982)), ((40, 13.991), (40, 13.991), (40, 14)))
        self.add_contour('c0', 'e4', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e5')
        self.add_contour('c2', 'e3')
