"""Keyhole (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94b02a29-f0e3-482a-8b4a-725005a9332e'
SOURCE_PATH = 'icons-json/symbol/keyhole_94b02a29-f0e3-482a-8b4a-725005a9332e.json'
AUTHOR = 'json_to_solo'

class KeyholeSymbol(Solo48):
    icon_id = 'keyhole-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('keyhole', 'symbol')

    def build(self):
        self.add_line('e0', (26, 4), (20, 4))
        self.add_line('e1', (15, 24), (10, 44))
        self.add_line('e2', (10, 44), (38, 44))
        self.add_line('e3', (38, 44), (33, 24))
        self.add_bezier('e4', (33, 24), ((37.234, 22.091), (39.988, 18.891), (39.988, 15.082)), ((39.988, 14.948), (40, 14.805), (40, 14.67)), ((40, 14.668), (40, 14.666), (40, 14.664)), ((40, 14.527), (39.988, 14.382), (39.988, 14.245)), ((39.988, 9.664), (34.818, 5.618), (29.095, 4.427)), ((28.258, 4.255), (26.862, 4), (26, 4)))
        self.add_bezier('e5', (20, 4), ((19.163, 4), (18.511, 4.336), (17.735, 4.555)), ((12.48, 6.064), (8.025, 10.164), (8.025, 14.436)), ((8.012, 14.5), (8.012, 14.573), (8, 14.645)), ((8, 14.646), (8, 14.647), (8, 14.648)), ((8, 14.711), (8.012, 14.774), (8.012, 14.836)), ((8.012, 19.136), (10.606, 21.564), (15, 24)))
        self.add_contour('c0', 'e4', 'e0', 'e5', 'e1', 'e2', 'e3')
