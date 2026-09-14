"""Unlock (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90a6ff07-21bc-47ed-b588-aacc1c25c397'
SOURCE_PATH = 'icons-json/symbol/unlock_90a6ff07-21bc-47ed-b588-aacc1c25c397.json'
AUTHOR = 'json_to_solo'

class Unlock(Solo48):
    icon_id = 'unlock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('unlock', 'symbol')

    def build(self):
        self.add_line('e0', (14, 13), (14, 21))
        self.add_line('e1', (8, 24), (8, 40))
        self.add_line('e2', (11, 44), (37, 44))
        self.add_line('e3', (40, 40), (40, 25))
        self.add_line('e4', (37, 21), (14, 21))
        self.add_bezier('e5', (34, 14), ((33.83, 10.264), (32.26, 6.709), (28.38, 4.945)), ((27.23, 4.418), (25.94, 4.009), (24.63, 4.009)), ((24.571, 4.009), (24.512, 4), (24.453, 4)), ((24.452, 4), (24.451, 4), (24.45, 4)), ((24.21, 4), (23.98, 4.009), (23.74, 4.009)), ((18.59, 4.009), (14, 8.391), (14, 13)))
        self.add_bezier('e6', (14, 21), ((10.91, 20.918), (9.11, 20.864), (8, 24)))
        self.add_bezier('e7', (8, 40), ((8.01, 40.055), (8.01, 40.482), (8.02, 40.536)), ((8.02, 41.727), (9.05, 43.164), (10.14, 43.755)), ((10.42, 43.909), (10.7, 43.9), (11, 44)))
        self.add_bezier('e8', (37, 44), ((37.24, 43.9), (37.48, 43.918), (37.71, 43.782)), ((38.77, 43.155), (39.98, 41.764), (39.98, 40.545)), ((39.99, 40.482), (39.99, 40.064), (40, 40)))
        self.add_bezier('e9', (40, 25), ((40, 23.291), (38.54, 21.664), (37, 21)))
        self.add_contour('c0', 'e5', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4')
