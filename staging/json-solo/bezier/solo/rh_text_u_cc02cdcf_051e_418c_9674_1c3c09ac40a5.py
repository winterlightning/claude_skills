"""Rh (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc02cdcf-051e-418c-9674-1c3c09ac40a5'
SOURCE_PATH = 'icons-json/symbol/rh (text u)_cc02cdcf-051e-418c-9674-1c3c09ac40a5.json'
AUTHOR = 'json_to_solo'

class RhTextUSymbol(Solo48):
    icon_id = 'rh-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('rh', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 16), (16, 16))
        self.add_line('e1', (16, 4), (9, 4))
        self.add_line('e2', (8, 5), (8, 27))
        self.add_line('e3', (21, 27), (16, 16))
        self.add_line('e4', (30, 4), (30, 27))
        self.add_line('e5', (40, 19), (40, 27))
        self.add_line('e6', (8, 44), (40, 44))
        self.add_bezier('e7', (16, 16), ((16.497, 16), (17.499, 15.627), (17.971, 15.464)), ((20.514, 14.545), (21.432, 11.891), (21.171, 9.182)), ((21.095, 8.345), (20.943, 7.473), (20.531, 6.736)), ((20.059, 5.909), (19.309, 5.209), (18.535, 4.727)), ((17.912, 4.345), (16.724, 4), (16, 4)))
        self.add_bezier('e8', (9, 4), ((8.924, 4.009), (8.691, 4.009), (8.606, 4.018)), ((8.354, 4.018), (8.017, 4.4), (8.017, 4.673)), ((8.008, 4.755), (8.008, 4.918), (8, 5)))
        self.add_bezier('e9', (30, 15), ((30.354, 14.227), (30.585, 13.445), (31.183, 12.845)), ((32.118, 11.927), (33.331, 11.482), (34.577, 11.455)), ((37.743, 11.391), (39.983, 13.755), (39.983, 17.209)), ((39.992, 17.282), (39.992, 17.355), (40, 17.427)), ((40, 17.8), (40, 18.627), (40, 19)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e9', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
