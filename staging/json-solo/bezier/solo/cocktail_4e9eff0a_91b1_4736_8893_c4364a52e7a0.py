"""Cocktail (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e9eff0a-91b1-4736-8893-c4364a52e7a0'
SOURCE_PATH = 'icons-json/symbol/cocktail_4e9eff0a-91b1-4736-8893-c4364a52e7a0.json'
AUTHOR = 'json_to_solo'

class CocktailSymbol(Solo48):
    icon_id = 'cocktail-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cocktail', 'symbol')

    def build(self):
        self.add_line('e0', (28, 12), (23, 20))
        self.add_line('e1', (23, 44), (23, 28))
        self.add_line('e2', (16, 44), (29, 44))
        self.add_line('e3', (8, 12), (37, 12))
        self.add_bezier('e4', (40, 4), ((39.823, 4), (39.638, 4), (39.461, 4)), ((39.116, 4), (38.796, 4.218), (38.459, 4.3)), ((37.903, 4.427), (37.331, 4.518), (36.766, 4.627)), ((35.663, 4.836), (34.568, 5.045), (33.465, 5.273)), ((31.638, 5.655), (31.84, 6.091), (30.745, 7.909)), ((30.4, 8.5), (30.046, 9.082), (29.701, 9.673)), ((29.213, 10.509), (28.514, 11.173), (28, 12)))
        self.add_bezier('e5', (37, 12), ((37.084, 14.391), (37.28, 16.964), (36.354, 19.173)), ((34.543, 23.445), (30.189, 26.736), (25.954, 27.491)), ((25.044, 27.655), (24.076, 27.627), (23.158, 27.636)), ((15.562, 27.7), (8.008, 21.291), (8.008, 12.709)), ((8.008, 12.527), (8, 12.173), (8, 12)))
        self.add_contour('c0', 'e4', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e5', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
