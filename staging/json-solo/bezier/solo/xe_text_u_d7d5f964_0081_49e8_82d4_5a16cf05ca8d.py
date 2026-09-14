"""Xe (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7d5f964-0081-49e8-82d4-5a16cf05ca8d'
SOURCE_PATH = 'icons-json/symbol/xe (text u)_d7d5f964-0081-49e8-82d4-5a16cf05ca8d.json'
AUTHOR = 'json_to_solo'

class XeTextUSymbol(Solo48):
    icon_id = 'xe-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('xe', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (23, 27))
        self.add_line('e1', (8, 27), (23, 4))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_bezier('e3', (31, 19), ((32.709, 19.236), (37.667, 20.427), (38.939, 19.282)), ((40, 18.045), (39.604, 14.755), (38.602, 13.536)), ((37.061, 11.655), (34.434, 11.727), (32.707, 13.227)), ((31.916, 13.909), (31.301, 14.836), (30.931, 15.855)), ((29.861, 18.855), (30.181, 24.818), (33.491, 26.073)), ((35.453, 26.818), (38.425, 26.118), (39.596, 24.145)), ((39.747, 23.891), (39.992, 23.473), (39.992, 23.155)), ((39.992, 23.136), (40, 23.018), (40, 23)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e2')
