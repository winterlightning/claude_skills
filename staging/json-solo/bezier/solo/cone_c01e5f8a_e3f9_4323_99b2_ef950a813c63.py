"""Cone (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c01e5f8a-e3f9-4323-99b2-ef950a813c63'
SOURCE_PATH = 'icons-json/symbol/cone_c01e5f8a-e3f9-4323-99b2-ef950a813c63.json'
AUTHOR = 'json_to_solo'

class ConeSymbol(Solo48):
    icon_id = 'cone-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cone', 'symbol')

    def build(self):
        self.add_line('e0', (24, 4), (40, 39))
        self.add_line('e1', (8, 39), (24, 4))
        self.add_bezier('e2', (40, 39), ((39.848, 39.118), (39.798, 39.745), (39.629, 39.855)), ((38.661, 40.482), (37.693, 41.136), (36.648, 41.627)), ((33.103, 43.318), (27.907, 43.982), (24.042, 43.982)), ((23.832, 43.982), (23.629, 44), (23.419, 44)), ((23.417, 44), (23.414, 44), (23.412, 44)), ((23.271, 44), (23.13, 43.982), (22.989, 43.982)), ((18.097, 43.982), (11.411, 43.018), (8, 39)))
        self.add_contour('c0', 'e0', 'e2', 'e1', closed=True)
