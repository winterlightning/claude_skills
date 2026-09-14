"""Liquid cup (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '667e1906-3fca-4780-84bf-d40ebcd6754f'
SOURCE_PATH = 'icons-json/symbol/liquid cup_667e1906-3fca-4780-84bf-d40ebcd6754f.json'
AUTHOR = 'json_to_solo'

class LiquidCupSymbol(Solo48):
    icon_id = 'liquid-cup-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('liquid', 'cup', 'symbol')

    def build(self):
        self.add_line('e0', (21, 22), (29, 24))
        self.add_line('e1', (8, 23), (9, 37))
        self.add_line('e2', (14, 42), (34, 42))
        self.add_line('e3', (39, 38), (40, 23))
        self.add_line('e4', (8, 23), (6, 6))
        self.add_line('e5', (6, 6), (42, 6))
        self.add_line('e6', (42, 6), (40, 23))
        self.add_bezier('e7', (8, 23), ((9.399, 22.55), (10.377, 22.233), (11.809, 21.955)), ((14.689, 21.382), (18.136, 21.427), (21, 22)))
        self.add_bezier('e8', (29, 24), ((33.312, 24.859), (35.77, 23.99), (40, 23)))
        self.add_bezier('e9', (9, 37), ((9.278, 39.389), (11.447, 42), (14, 42)))
        self.add_bezier('e10', (34, 42), ((34.131, 42), (34.088, 41.992), (34.219, 41.992)), ((34.489, 41.992), (34.988, 41.828), (35.225, 41.755)), ((37.009, 41.223), (38.787, 39.939), (39, 38)))
        self.add_contour('c0', 'e7', 'e0', 'e8')
        self.add_contour('c1', 'e1', 'e9', 'e2', 'e10', 'e3')
        self.add_contour('c2', 'e4', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
