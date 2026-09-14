"""Peercoin (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e015513e-29e5-48ae-ad99-806d5a1b0b1e'
SOURCE_PATH = 'icons-json/symbol/peercoin_e015513e-29e5-48ae-ad99-806d5a1b0b1e.json'
AUTHOR = 'json_to_solo'

class Peercoin(Solo48):
    icon_id = 'peercoin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('peercoin', 'symbol')

    def build(self):
        self.add_line('e0', (8, 31), (14, 31))
        self.add_line('e1', (14, 44), (14, 31))
        self.add_line('e2', (21, 44), (21, 31))
        self.add_line('e3', (30, 31), (21, 31))
        self.add_line('e4', (21, 23), (32, 23))
        self.add_line('e5', (32, 4), (21, 4))
        self.add_line('e6', (21, 23), (21, 4))
        self.add_line('e7', (21, 23), (21, 31))
        self.add_line('e8', (21, 4), (14, 4))
        self.add_line('e9', (14, 4), (14, 31))
        self.add_line('e10', (21, 31), (14, 31))
        self.add_arc('e11-1', (32, 23), (40, 14), radius_x=10, sweep=False)
        self.add_line('e11-2', (40, 14), (39, 9))
        self.add_arc('e11-3', (39, 9), (32, 4), radius_x=9, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e11-1', 'e11-2', 'e11-3', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7')
        self.add_contour('c7', 'e8', 'e9')
        self.add_contour('c8', 'e10')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c0', 'c8')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c1', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c8')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c3', 'c8')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c5', 'c7')
