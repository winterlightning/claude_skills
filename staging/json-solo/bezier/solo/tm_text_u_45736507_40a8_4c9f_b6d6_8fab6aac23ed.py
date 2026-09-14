"""Tm (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45736507-40a8-4c9f-b6d6-8fab6aac23ed'
SOURCE_PATH = 'icons-json/symbol/tm (text u)_45736507-40a8-4c9f-b6d6-8fab6aac23ed.json'
AUTHOR = 'json_to_solo'

class TmTextUSymbol(Solo48):
    icon_id = 'tm-text-u-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('tm', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (4, 8), (19, 8))
        self.add_line('e1', (11, 26), (11, 8))
        self.add_line('e2', (26, 15), (26, 26))
        self.add_line('e3', (35, 18), (35, 26))
        self.add_line('e4', (44, 18), (44, 26))
        self.add_line('e5', (4, 40), (44, 40))
        self.add_bezier('e6', (26, 17), ((26.391, 16.2), (26.6, 15.773), (27.4, 15.242)), ((29.718, 13.701), (34.309, 14.274), (34.909, 17.263)), ((34.964, 17.541), (35, 17.722), (35, 18)))
        self.add_bezier('e7', (35, 17), ((35.382, 16.2), (35.682, 15.781), (36.482, 15.259)), ((38.882, 13.667), (43.991, 14.568), (43.991, 17.886)), ((43.991, 17.962), (44, 17.924), (44, 18)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e6', 'e3')
        self.add_contour('c4', 'e7', 'e4')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c4', 'c3')
