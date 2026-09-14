"""Eu (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65fb28c3-f621-426e-ba5e-b1b75fdeab5c'
SOURCE_PATH = 'icons-json/symbol/eu (text u)_65fb28c3-f621-426e-ba5e-b1b75fdeab5c.json'
AUTHOR = 'json_to_solo'

class EuTextUSymbol(Solo48):
    icon_id = 'eu-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('eu', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (21, 4), (9, 4))
        self.add_line('e1', (8, 5), (8, 26))
        self.add_line('e2', (9, 27), (21, 27))
        self.add_line('e3', (18, 15), (8, 15))
        self.add_line('e4', (30, 12), (30, 22))
        self.add_line('e5', (40, 12), (40, 27))
        self.add_line('e6', (8, 44), (40, 44))
        self.add_bezier('e7', (9, 4), ((8.83, 4.109), (8.58, 4.027), (8.41, 4.127)), ((8, 4.373), (8.23, 4.718), (8, 5)))
        self.add_bezier('e8', (8, 26), ((8.01, 26.1), (8.02, 26.018), (8.04, 26.109)), ((8.07, 26.2), (8.11, 26.282), (8.15, 26.364)), ((8.4, 26.673), (8.73, 26.827), (9, 27)))
        self.add_bezier('e9', (30, 22), ((30, 26.791), (37.72, 27.727), (39.59, 23.682)), ((39.78, 23.282), (39.99, 22.764), (39.99, 22.318)), ((39.99, 22.273), (40, 22.045), (40, 22)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e9')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c3')
