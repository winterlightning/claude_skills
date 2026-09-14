"""Cu (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2287aae-54a7-4e4c-9033-5df0a68ec4c5'
SOURCE_PATH = 'icons-json/symbol/cu (text u)_d2287aae-54a7-4e4c-9033-5df0a68ec4c5.json'
AUTHOR = 'json_to_solo'

class CuTextUSymbol(Solo48):
    icon_id = 'cu-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cu', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 9), (8, 21))
        self.add_line('e1', (29, 12), (29, 22))
        self.add_line('e2', (40, 12), (40, 27))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_bezier('e4', (20, 8), ((18.95, 6.109), (17.11, 4.009), (14.58, 4.009)), ((14.42, 4.009), (14.26, 4), (14.11, 4)), ((14.109, 4), (14.107, 4), (14.106, 4)), ((14.027, 4), (13.949, 4), (13.87, 4.009)), ((10.95, 4.009), (8, 6.536), (8, 9.236)), ((8, 9.309), (8, 8.927), (8, 9)))
        self.add_bezier('e5', (8, 21), ((8, 24.491), (12.13, 27.282), (15.7, 26.5)), ((17.78, 26.045), (19.06, 24.655), (20, 23)))
        self.add_bezier('e6', (29, 22), ((29, 26.873), (37.63, 27.664), (39.59, 23.618)), ((39.77, 23.236), (39.99, 22.736), (39.99, 22.309)), ((39.99, 22.264), (40, 22.045), (40, 22)))
        self.add_contour('c0', 'e4', 'e0', 'e5')
        self.add_contour('c1', 'e1', 'e6')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c1', 'c2')
