"""Te (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c11d8345-5e6e-493f-985d-ee6acb6e9b09'
SOURCE_PATH = 'icons-json/symbol/te (text u)_c11d8345-5e6e-493f-985d-ee6acb6e9b09.json'
AUTHOR = 'json_to_solo'

class TeTextUSymbol(Solo48):
    icon_id = 'te-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('te', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (22, 4))
        self.add_line('e1', (16, 27), (16, 4))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_bezier('e3', (30, 19), ((31.516, 19.2), (32.935, 19.809), (34.467, 19.845)), ((35.646, 19.873), (37.726, 20.018), (38.779, 19.345)), ((40, 18.345), (39.587, 14.864), (38.661, 13.673)), ((36.977, 11.5), (33.945, 11.736), (32.118, 13.518)), ((29.263, 16.3), (29.086, 24.564), (33.28, 26.091)), ((35.301, 26.818), (38.408, 26.136), (39.613, 24.1)), ((39.756, 23.855), (39.992, 23.455), (39.992, 23.145)), ((39.992, 23.127), (40, 23.018), (40, 23)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e2')
        self.relate('connect', 'c1', 'c0')
