"""Fiber access (networks), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ba4638e-ff88-5a77-b904-061a960fe212'
SOURCE_PATH = 'icons-json/networks/fiber access_2ba4638e-ff88-5a77-b904-061a960fe212.json'
AUTHOR = 'json_to_solo'

class FiberAccessNetworks(Solo48):
    icon_id = 'fiber-access-networks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('fiber', 'access', 'networks')

    def build(self):
        self.add_line('e0', (4, 8), (18, 8))
        self.add_line('e1', (40, 19), (44, 16))
        self.add_line('e2', (44, 16), (27, 16))
        self.add_line('e3', (40, 12), (44, 16))
        self.add_line('e4', (18, 8), (17, 10))
        self.add_line('e5', (4, 40), (19, 40))
        self.add_line('e6', (40, 36), (44, 32))
        self.add_line('e7', (40, 29), (44, 32))
        self.add_line('e8', (18, 40), (16, 38))
        self.add_line('e9', (44, 32), (27, 32))
        self.add_line('e10-1', (18, 8), (24, 9))
        self.add_arc('e10-2', (24, 9), (27, 16), radius_x=6)
        self.add_arc('e11', (17, 10), (27, 16), radius_x=6, large_arc=True, sweep=False)
        self.add_line('e12-1', (19, 40), (23, 40))
        self.add_line('e12-2', (23, 40), (26, 37))
        self.add_arc('e12-3', (26, 37), (27, 32), radius_x=8, sweep=False)
        self.add_arc('e13-1', (16, 38), (18, 29), radius_x=6)
        self.add_arc('e13-2', (18, 29), (27, 32), radius_x=6)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e10-1', 'e10-2')
        self.add_contour('c4', 'e4', 'e11')
        self.add_contour('c5', 'e5', 'e12-1', 'e12-2', 'e12-3')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8', 'e13-1', 'e13-2')
        self.add_contour('c9', 'e9')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c9')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c8', 'c5')
