"""Pb (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a86d4c64-5422-40b0-81a1-1820524ddd2f'
SOURCE_PATH = 'icons-json/symbol/pb (text u)_a86d4c64-5422-40b0-81a1-1820524ddd2f.json'
AUTHOR = 'json_to_solo'

class PbTextUSymbol(Solo48):
    icon_id = 'pb-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pb', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 16), (15, 16))
        self.add_line('e1', (15, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 27))
        self.add_line('e3', (29, 4), (29, 20))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_bezier('e5', (15, 16), ((15.758, 16), (16.438, 15.464), (17.112, 15.109)), ((21.415, 12.845), (20.825, 5.809), (16.244, 4.336)), ((15.756, 4.182), (15.514, 4), (15, 4)))
        self.add_bezier('e6', (37, 12), ((36.225, 11.627), (35.983, 11.527), (35.124, 11.445)), ((30.316, 11.027), (28.851, 16.164), (29.053, 20.364)), ((29.12, 21.8), (29.331, 23.336), (30.122, 24.545)), ((31.832, 27.136), (35.966, 27.009), (37.996, 24.973)), ((39.394, 23.564), (39.983, 21.355), (39.983, 19.336)), ((39.983, 19.055), (40, 18.773), (40, 18.482)), ((40, 18.182), (39.983, 17.882), (39.983, 17.582)), ((39.983, 15.345), (38.684, 13.282), (37, 12)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e6', closed=True)
        self.relate('connect', 'c1', 'c3')
