"""Power plug disconnected (electronics), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a183e55-7edf-42bd-8673-8f347fa5b060'
SOURCE_PATH = 'icons-json/electronics/power plug disconnected_7a183e55-7edf-42bd-8673-8f347fa5b060.json'
AUTHOR = 'json_to_solo'

class PowerPlugDisconnectedElectronics(Solo48):
    icon_id = 'power-plug-disconnected-electronics'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('power', 'plug', 'disconnected', 'electronics')

    def build(self):
        self.add_line('e0', (7, 6), (15, 14))
        self.add_line('e1', (6, 41), (15, 32))
        self.add_line('e2', (42, 42), (34, 34))
        self.add_line('e3', (42, 13), (35, 22))
        self.add_line('e4', (35, 6), (27, 14))
        self.add_line('e5', (15, 14), (32, 32))
        self.add_line('e6', (15, 14), (21, 8))
        self.add_line('e7', (21, 8), (27, 14))
        self.add_line('e8', (32, 32), (34, 34))
        self.add_line('e9', (27, 14), (35, 22))
        self.add_line('e10', (35, 22), (40, 27))
        self.add_line('e11', (40, 27), (34, 34))
        self.add_bezier('e12', (16, 15), ((15.296, 15.818), (14.395, 16.612), (13.814, 17.52)), ((11.637, 20.899), (11.294, 25.375), (12.971, 29.032)), ((13.495, 30.185), (14.247, 30.994), (15, 32)))
        self.add_bezier('e13', (32, 32), ((31.067, 32.851), (30.357, 33.843), (29.261, 34.473)), ((25.775, 36.477), (21.464, 36.42), (17.978, 34.473)), ((16.874, 33.851), (15.941, 32.835), (15, 32)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e12')
        self.add_contour('c6', 'e5')
        self.add_contour('c7', 'e6', 'e7')
        self.add_contour('c8', 'e13')
        self.add_contour('c9', 'e8')
        self.add_contour('c10', 'e9')
        self.add_contour('c11', 'e10', 'e11')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c8')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c11', 'c2')
        self.relate('connect', 'c11', 'c9')
        self.relate('connect', 'c2', 'c9')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c3')
        self.relate('connect', 'c11', 'c3')
        self.relate('connect', 'c10', 'c4')
        self.relate('connect', 'c10', 'c7')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c6', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c5', 'c6')
