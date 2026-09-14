"""Ta (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18d74860-f1c9-4d7e-8d64-0337d5eeff19'
SOURCE_PATH = 'icons-json/symbol/ta (text u)_18d74860-f1c9-4d7e-8d64-0337d5eeff19.json'
AUTHOR = 'json_to_solo'

class TaTextUSymbol(Solo48):
    icon_id = 'ta-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ta', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (21, 4))
        self.add_line('e1', (15, 27), (15, 4))
        self.add_line('e2', (40, 27), (40, 23))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_bezier('e4', (40, 23), ((40, 23), (40, 23.1), (39.992, 23.1)), ((39.992, 23.373), (39.234, 24.345), (39.074, 24.545)), ((37.844, 26.073), (36.211, 26.736), (34.375, 26.464)), ((31.023, 25.964), (29.482, 23.291), (29.448, 19.755)), ((29.432, 16.673), (30.922, 13.445), (33.726, 12.364)), ((36.261, 11.391), (39.992, 13.709), (39.992, 16.755)), ((39.992, 16.836), (40, 16.918), (40, 16.991)), ((40, 19.027), (40, 20.964), (40, 23)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', closed=True)
        self.relate('connect', 'c1', 'c0')
