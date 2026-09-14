"""Sn (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1b903d5-9189-45f0-9880-e909e013544b'
SOURCE_PATH = 'icons-json/symbol/sn (text u)_b1b903d5-9189-45f0-9880-e909e013544b.json'
AUTHOR = 'json_to_solo'

class SnTextUSymbol(Solo48):
    icon_id = 'sn-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('sn', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (16, 16), (12, 14))
        self.add_line('e1', (30, 12), (30, 27))
        self.add_line('e2', (40, 17), (40, 27))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_bezier('e4', (8, 23), ((8.16, 23.164), (8.17, 23.455), (8.36, 23.609)), ((9.43, 24.509), (10.52, 25.455), (11.92, 25.936)), ((15.45, 27.155), (19.5, 25.982), (20.62, 22.518)), ((20.99, 21.391), (20.98, 20.091), (20.46, 19)), ((19.66, 17.318), (17.69, 16.773), (16, 16)))
        self.add_bezier('e5', (12, 14), ((11.67, 13.855), (11.36, 13.564), (11.07, 13.355)), ((10.42, 12.891), (9.74, 12.355), (9.32, 11.682)), ((8, 8.682), (9.61, 4.009), (13.68, 4.009)), ((13.818, 4.009), (13.965, 4), (14.113, 4)), ((14.115, 4), (14.118, 4), (14.12, 4)), ((14.27, 4), (14.42, 4.009), (14.57, 4.009)), ((16.72, 4.009), (18.53, 5.845), (20, 7)))
        self.add_bezier('e6', (30, 16), ((30.59, 14.582), (31.42, 13.164), (33.07, 12.591)), ((36.02, 11.573), (39.98, 13.191), (39.98, 16.345)), ((39.98, 16.473), (40, 16.873), (40, 17)))
        self.add_contour('c0', 'e4', 'e0', 'e5')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e6', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c2', 'c1')
