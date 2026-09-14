"""Symbol armor (war), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '874f7bd6-cdff-431b-9907-a5c3452b8113'
SOURCE_PATH = 'icons-json/war/symbol armor_874f7bd6-cdff-431b-9907-a5c3452b8113.json'
AUTHOR = 'json_to_solo'

class SymbolArmorWar(Solo48):
    icon_id = 'symbol-armor-war'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('symbol', 'armor', 'war')

    def build(self):
        self.add_line('e0', (44, 14), (32, 14))
        self.add_line('e1', (10, 40), (37, 40))
        self.add_line('e2', (13, 22), (34, 22))
        self.add_line('e3', (13, 22), (15, 12))
        self.add_line('e4', (18, 8), (29, 8))
        self.add_line('e5', (32, 12), (32, 14))
        self.add_line('e6', (34, 22), (32, 14))
        self.add_bezier('e7', (13, 22), ((9.9, 22), (7.027, 21.095), (5.018, 24.997)), ((4.436, 26.129), (4, 27.606), (4, 29.009)), ((4, 29.015), (4, 29.02), (4, 29.026)), ((4, 29.377), (4.018, 29.729), (4.018, 30.08)), ((4.018, 33.526), (7.309, 40), (10, 40)))
        self.add_bezier('e8', (37, 40), ((39.745, 40), (42.5, 34.425), (42.964, 31.089)), ((43.218, 29.243), (43.027, 27.311), (42.364, 25.649)), ((40.527, 21.034), (37.273, 22), (34, 22)))
        self.add_bezier('e9', (15, 12), ((15.355, 10.068), (16.736, 8.64), (18, 8)))
        self.add_bezier('e10', (29, 8), ((29.064, 8), (28.682, 8), (28.745, 8)), ((30.145, 8), (31.336, 10.597), (32, 12)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e7', 'e1', 'e8')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e9', 'e4', 'e10', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
