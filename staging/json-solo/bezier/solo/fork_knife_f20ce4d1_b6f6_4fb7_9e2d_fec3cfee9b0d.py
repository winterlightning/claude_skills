"""Fork knife (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f20ce4d1-b6f6-4fb7-9e2d-fec3cfee9b0d'
SOURCE_PATH = 'icons-json/symbol/fork knife_f20ce4d1-b6f6-4fb7-9e2d-fec3cfee9b0d.json'
AUTHOR = 'json_to_solo'

class ForkKnifeSymbol(Solo48):
    icon_id = 'fork-knife-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('fork', 'knife', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (8, 15))
        self.add_line('e1', (17, 22), (17, 4))
        self.add_line('e2', (17, 44), (17, 22))
        self.add_line('e3', (24, 15), (24, 4))
        self.add_line('e4', (33, 44), (33, 4))
        self.add_line('e5', (33, 4), (40, 24))
        self.add_line('e6', (37, 28), (33, 28))
        self.add_bezier('e7', (8, 15), ((8, 15.773), (8.413, 16.564), (8.733, 17.236)), ((10.535, 21.1), (13.404, 21.6), (17, 22)))
        self.add_bezier('e8', (17, 22), ((19.821, 20.691), (22.509, 19.936), (23.604, 16.573)), ((23.764, 16.082), (24, 15.518), (24, 15)))
        self.add_bezier('e9', (40, 24), ((40, 24.227), (39.992, 24.455), (39.992, 24.682)), ((39.992, 24.791), (39.992, 24.9), (39.983, 25.018)), ((39.992, 25.064), (39.992, 25.118), (40, 25.173)), ((40, 25.464), (40, 25.755), (40, 26.045)), ((39.874, 26.173), (39.756, 26.3), (39.629, 26.427)), ((39.032, 27.073), (37.783, 27.709), (37, 28)))
        self.add_contour('c0', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e2', 'e8', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5', 'e9', 'e6')
        self.relate('connect', 'c3', 'c2')
