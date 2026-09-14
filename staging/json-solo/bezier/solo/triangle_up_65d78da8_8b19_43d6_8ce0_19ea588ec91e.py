"""Triangle up (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65d78da8-8b19-43d6-8ce0-19ea588ec91e'
SOURCE_PATH = 'icons-json/symbol/triangle up_65d78da8-8b19-43d6-8ce0-19ea588ec91e.json'
AUTHOR = 'json_to_solo'

class TriangleUp(Solo48):
    icon_id = 'triangle-up'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('triangle', 'up', 'symbol')

    def build(self):
        self.add_line('e0', (4, 40), (23, 8))
        self.add_line('e1', (25, 8), (44, 40))
        self.add_bezier('e2', (23, 8), ((23.173, 8), (23.427, 8), (23.6, 8)), ((23.8, 8), (24.027, 8), (24.227, 8)), ((24.455, 8), (24.773, 8), (25, 8)))
        self.add_contour('c0', 'e0', 'e2', 'e1')
