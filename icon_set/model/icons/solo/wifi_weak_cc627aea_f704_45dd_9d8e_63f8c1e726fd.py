"""Wifi weak (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cc627aea-f704-45dd-9d8e-63f8c1e726fd'
SOURCE_PATH = 'icons-json/symbol/wifi weak_cc627aea-f704-45dd-9d8e-63f8c1e726fd.json'
AUTHOR = 'gpt-6'

class WifiWeak(Solo48):
    icon_id = 'wifi-weak'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('wifi', 'weak', 'symbol')

    def build(self):
        self.add_line('sym-e0', (19, 32), (24, 37))
        self.add_line('sym-e1', (24, 37), (20, 40))
        self.add_arc('sym-e2', (4, 16), (23, 8), radius_x=28, radius_y=28, large_arc=False, sweep=True)
        self.add_line('sym-e3', (23, 8), (25, 8))
        self.add_arc('sym-e5', (25, 8), (44, 16), radius_x=29, radius_y=29, large_arc=False, sweep=True)
        self.add_arc('sym-e6', (12, 25), (24, 20), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_arc('sym-e7', (24, 20), (36, 25), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('sym-e8', (29, 32), (24, 37))
        self.add_line('sym-e9', (24, 37), (28, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=False)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e5', closed=False)
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7', closed=False)
        self.add_contour('sym-c3', 'sym-e8', 'sym-e9', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c3')
