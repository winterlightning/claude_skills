"""Cocktail (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e4-1', (40, 4), (32, 6), radius_x=17, sweep=False)
        self.add_line('e4-2', (32, 6), (28, 12))
        self.add_arc('e5-1', (37, 12), (19, 27), radius_x=14)
        self.add_arc('e5-2', (19, 27), (8, 12), radius_x=16)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e5-1', 'e5-2', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
