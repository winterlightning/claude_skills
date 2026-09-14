"""Unlock 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c432ee35-e1c4-49b6-9d74-d7aef0fe659c'
SOURCE_PATH = 'icons-json/symbol/unlock 1_c432ee35-e1c4-49b6-9d74-d7aef0fe659c.json'
AUTHOR = 'json_to_solo'

class Unlock1Symbol(Solo48):
    icon_id = 'unlock-1-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('unlock', 'symbol')

    def build(self):
        self.add_line('e0', (13, 14), (13, 21))
        self.add_line('e1', (33, 44), (14, 44))
        self.add_line('e2', (8, 38), (8, 21))
        self.add_line('e3', (8, 21), (40, 21))
        self.add_line('e4', (40, 21), (40, 39))
        self.add_bezier('e5', (35, 15), ((34.95, 13.4), (34.84, 11.736), (34.21, 10.218)), ((32.78, 6.8), (28.87, 4.018), (24.75, 4.018)), ((24.514, 4.018), (24.277, 4), (24.041, 4)), ((24.037, 4), (24.034, 4), (24.03, 4)), ((23.78, 4), (23.54, 4.018), (23.29, 4.018)), ((19.1, 4.018), (14.96, 6.891), (13.56, 10.418)), ((13.12, 11.509), (13, 12.845), (13, 14)))
        self.add_bezier('e6', (40, 39), ((40, 39.136), (40, 38.818), (40, 38.955)), ((40, 42.064), (37.11, 43.982), (33.93, 43.982)), ((33.62, 43.982), (33.31, 44), (33, 44)))
        self.add_bezier('e7', (14, 44), ((13.83, 43.991), (13.67, 43.991), (13.5, 43.982)), ((10.78, 43.982), (8.02, 41.682), (8.02, 39.164)), ((8.02, 38.991), (8, 38.827), (8, 38.655)), ((8, 38.318), (8, 38.336), (8, 38)))
        self.add_contour('c0', 'e5', 'e0')
        self.add_contour('c1', 'e6', 'e1', 'e7', 'e2', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
