"""Wifi weak (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc627aea-f704-45dd-9d8e-63f8c1e726fd'
SOURCE_PATH = 'icons-json/symbol/wifi weak_cc627aea-f704-45dd-9d8e-63f8c1e726fd.json'
AUTHOR = 'json_to_solo'

class WifiWeakSymbol(Solo48):
    icon_id = 'wifi-weak-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('wifi', 'weak', 'symbol')

    def build(self):
        self.add_line('sym-e0', (19, 32), (24, 37))
        self.add_line('sym-e1', (24, 37), (20, 40))
        self.add_bezier('sym-e2', (4, 16), ((8.945, 11.032), (15.582, 8), (23, 8)))
        self.add_bezier('sym-e3', (23, 8), ((23.191, 8), (23.811, 8.003), (24, 8)))
        self.add_bezier('sym-e4', (24, 8), ((24.189, 8.003), (24.809, 8), (25, 8)))
        self.add_bezier('sym-e5', (25, 8), ((32.418, 8), (39.055, 11.032), (44, 16)))
        self.add_bezier('sym-e6', (12, 25), ((15.458, 21.869), (19.814, 20.036), (24, 20)))
        self.add_bezier('sym-e7', (24, 20), ((28.186, 20.036), (32.542, 21.869), (36, 25)))
        self.add_line('sym-e8', (29, 32), (24, 37))
        self.add_line('sym-e9', (24, 37), (28, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c3', 'sym-e8', 'sym-e9')
        self.relate('connect', 'sym-c0', 'sym-c3')
