"""U turn arrow (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1f1578e-c8a3-4fd5-bd53-81866fca166a'
SOURCE_PATH = 'icons-json/symbol/u turn arrow_f1f1578e-c8a3-4fd5-bd53-81866fca166a.json'
AUTHOR = 'json_to_solo'

class UTurnArrowSymbol(Solo48):
    icon_id = 'u-turn-arrow-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('u', 'turn', 'arrow', 'symbol')

    def build(self):
        self.add_line('e0', (33, 39), (33, 16))
        self.add_line('e1', (33, 39), (27, 32))
        self.add_line('e2', (33, 39), (40, 32))
        self.add_line('e3', (8, 17), (8, 44))
        self.add_bezier('e4', (33, 16), ((33, 15.045), (32.952, 13.827), (32.674, 12.936)), ((31.326, 8.7), (28.101, 5.527), (24.076, 4.427)), ((23.309, 4.218), (22.467, 4.009), (21.676, 4.009)), ((21.608, 4.009), (21.067, 4), (21, 4)))
        self.add_bezier('e5', (21, 4), ((20.225, 4), (19.924, 4.009), (19.158, 4.009)), ((18.392, 4.009), (17.558, 4.327), (16.842, 4.555)), ((13.078, 5.745), (10.164, 8.7), (8.775, 12.645)), ((8.362, 13.818), (8.017, 15.145), (8.017, 16.418)), ((8.008, 16.518), (8.008, 16.9), (8, 17)))
        self.add_contour('c0', 'e0', 'e4')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e5', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
