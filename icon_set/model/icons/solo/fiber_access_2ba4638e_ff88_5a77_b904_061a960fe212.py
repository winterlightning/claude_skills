"""Fiber access (networks), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ba4638e-ff88-5a77-b904-061a960fe212'
SOURCE_PATH = 'icons-json/networks/fiber access_2ba4638e-ff88-5a77-b904-061a960fe212.json'
AUTHOR = 'json_to_solo'

class FiberAccess(Solo48):
    icon_id = 'fiber-access'
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
        self.add_bezier('e10', (18, 8), ((19.145, 8), (19.918, 8.02), (21.064, 8.02)), ((23.882, 8.02), (26.745, 10.53), (27.009, 13.71)), ((27.073, 14.5), (27.155, 15.23), (27, 16)))
        self.add_bezier('e11', (17, 10), ((12.582, 15.69), (18.273, 22.15), (23.855, 19.23)), ((25.218, 18.52), (26.309, 17.42), (27, 16)))
        self.add_bezier('e12', (19, 40), ((20.209, 40), (20.955, 40), (22.164, 40)), ((22.718, 40), (23.391, 39.52), (23.855, 39.21)), ((26.473, 37.47), (27.491, 35.21), (27, 32)))
        self.add_bezier('e13', (16, 38), ((12.118, 31.97), (19.055, 25.74), (24.345, 28.98)), ((25.518, 29.7), (26.409, 30.72), (27, 32)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e10')
        self.add_contour('c4', 'e4', 'e11')
        self.add_contour('c5', 'e5', 'e12')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8', 'e13')
        self.add_contour('c9', 'e9')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c9')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c8', 'c5')
