"""Xd (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '745c0a55-b6f3-45b5-8923-20698c6b86de'
SOURCE_PATH = 'icons-json/symbol/Xd_745c0a55-b6f3-45b5-8923-20698c6b86de.json'
AUTHOR = 'json_to_solo'

class XdSymbol(Solo48):
    icon_id = 'xd-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('xd', 'symbol')

    def build(self):
        self.add_line('e0', (4, 8), (22, 40))
        self.add_line('e1', (4, 40), (22, 8))
        self.add_line('e2', (44, 8), (44, 35))
        self.add_bezier('e3', (44, 35), ((44, 35.025), (43.991, 35.126), (43.991, 35.151)), ((43.991, 35.545), (43.773, 36.049), (43.645, 36.382)), ((42.691, 38.818), (40.555, 39.988), (38.591, 39.988)), ((38.473, 39.988), (38.345, 40), (38.218, 40)), ((38.009, 40), (37.8, 39.988), (37.582, 39.988)), ((30.082, 39.988), (28.9, 22.732), (35.964, 19.495)), ((38.155, 18.486), (40.582, 18.892), (42.473, 20.714)), ((42.7, 20.935), (43.982, 22.302), (43.982, 22.708)), ((43.991, 22.732), (43.991, 22.975), (44, 23)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
