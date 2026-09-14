"""Peercoin (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e015513e-29e5-48ae-ad99-806d5a1b0b1e'
SOURCE_PATH = 'icons-json/symbol/peercoin_e015513e-29e5-48ae-ad99-806d5a1b0b1e.json'
AUTHOR = 'json_to_solo'

class PeercoinSymbol(Solo48):
    icon_id = 'peercoin-symbol'
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
        self.add_bezier('e11', (32, 23), ((32.455, 23), (33.482, 22.836), (33.912, 22.682)), ((37.213, 21.491), (39.992, 17.891), (39.992, 14.027)), ((39.992, 13.947), (40, 13.875), (40, 13.795)), ((40, 13.793), (40, 13.792), (40, 13.791)), ((40, 13.591), (39.992, 13.391), (39.992, 13.191)), ((39.992, 8.955), (36.783, 5.445), (33.187, 4.345)), ((32.691, 4.191), (32.522, 4), (32, 4)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e11', 'e5')
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
