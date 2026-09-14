"""Lightning with wrench (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a4d7838-471b-4d28-87da-ddd67295cbe7'
SOURCE_PATH = 'icons-json/symbol/lightning with wrench_7a4d7838-471b-4d28-87da-ddd67295cbe7.json'
AUTHOR = 'json_to_solo'

class LightningWithWrenchSymbol(Solo48):
    icon_id = 'lightning-with-wrench-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('lightning', 'with', 'wrench', 'symbol')

    def build(self):
        self.add_line('e0', (25, 11), (29, 7))
        self.add_line('e1', (17, 17), (6, 29))
        self.add_line('e2', (13, 35), (24, 22))
        self.add_line('e3', (40, 20), (34, 31))
        self.add_line('e4', (34, 31), (42, 31))
        self.add_line('e5', (42, 31), (33, 42))
        self.add_bezier('e6', (31, 18), ((29.265, 17.296), (27.952, 16.775), (26.365, 15.777)), ((26.013, 15.548), (24.998, 14.82), (24.867, 14.435)), ((24.499, 13.306), (24.755, 12.113), (25, 11)))
        self.add_bezier('e7', (29, 7), ((27.953, 6.64), (26.7, 6.016), (25.571, 6.016)), ((25.473, 6.008), (25.375, 6.008), (25.276, 6)), ((25.271, 6), (25.265, 6), (25.259, 6)), ((24.905, 6), (24.543, 6.008), (24.188, 6.008)), ((19.934, 6.008), (16.154, 9.641), (16.375, 13.953)), ((16.432, 15.237), (16.46, 15.863), (17, 17)))
        self.add_bezier('e8', (31, 18), ((29.2, 20.733), (27.175, 22.221), (24, 22)))
        self.add_contour('c0', 'e6', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e8')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5')
