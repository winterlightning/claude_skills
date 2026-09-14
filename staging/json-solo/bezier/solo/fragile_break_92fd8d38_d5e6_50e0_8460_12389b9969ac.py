"""Fragile break (shipping), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92fd8d38-d5e6-50e0-8460-12389b9969ac'
SOURCE_PATH = 'icons-json/shipping/fragile break_92fd8d38-d5e6-50e0-8460-12389b9969ac.json'
AUTHOR = 'json_to_solo'

class FragileBreakShipping(Solo48):
    icon_id = 'fragile-break-shipping'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('fragile', 'break', 'shipping')

    def build(self):
        self.add_line('e0', (24, 44), (24, 30))
        self.add_line('e1', (17, 44), (33, 44))
        self.add_line('e2', (24, 4), (38, 4))
        self.add_line('e3', (38, 4), (40, 17))
        self.add_line('e4', (8, 19), (10, 4))
        self.add_line('e5', (10, 4), (19, 4))
        self.add_line('e6', (19, 4), (17, 9))
        self.add_line('e7', (17, 9), (23, 13))
        self.add_line('e8', (23, 13), (18, 16))
        self.add_bezier('e9', (40, 17), ((40, 18.064), (39.975, 18.845), (39.975, 19.909)), ((39.975, 20.755), (39.508, 21.673), (39.138, 22.455)), ((36.911, 27.364), (30.855, 30.236), (24, 30.364)), ((16.911, 30.491), (10.302, 26.336), (8.64, 21.336)), ((8.455, 20.773), (8.025, 20.018), (8.025, 19.445)), ((8.012, 19.409), (8.012, 19.364), (8, 19.327)), ((8, 19.064), (8, 19.264), (8, 19)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e9', 'e4', 'e5', 'e6', 'e7', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
