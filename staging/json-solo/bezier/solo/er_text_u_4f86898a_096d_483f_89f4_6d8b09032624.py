"""Er (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f86898a-096d-483f-89f4-6d8b09032624'
SOURCE_PATH = 'icons-json/symbol/er (text u)_4f86898a-096d-483f-89f4-6d8b09032624.json'
AUTHOR = 'json_to_solo'

class ErTextUSymbol(Solo48):
    icon_id = 'er-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('er', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (22, 4), (9, 4))
        self.add_line('e1', (8, 5), (8, 26))
        self.add_line('e2', (9, 27), (22, 27))
        self.add_line('e3', (19, 15), (8, 15))
        self.add_line('e4', (31, 13), (31, 27))
        self.add_line('e5', (8, 44), (40, 44))
        self.add_bezier('e6', (9, 4), ((8.85, 4.073), (8.65, 4.027), (8.49, 4.1)), ((8.04, 4.3), (8.19, 4.682), (8, 5)))
        self.add_bezier('e7', (8, 26), ((8.09, 26.136), (8.02, 26.136), (8.11, 26.273)), ((8.33, 26.645), (8.67, 26.836), (9, 27)))
        self.add_bezier('e8', (40, 13), ((40, 13), (39.99, 13.082), (39.99, 13.082)), ((39.99, 13.018), (39.71, 12.845), (39.67, 12.818)), ((38.62, 12.064), (37.25, 11.736), (35.93, 11.945)), ((33.19, 12.391), (31.76, 14.791), (31, 17)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e8')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
