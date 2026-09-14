"""Cocktail martini (drinks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22495c58-f9b2-522e-aaa8-85134643b82b'
SOURCE_PATH = 'icons-json/drinks/cocktail martini_22495c58-f9b2-522e-aaa8-85134643b82b.json'
AUTHOR = 'json_to_solo'

class CocktailMartiniDrinks(Solo48):
    icon_id = 'cocktail-martini-drinks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('cocktail', 'martini', 'drinks')

    def build(self):
        self.add_line('sym-e0', (24, 22), (24, 44))
        self.add_line('sym-e1', (24, 44), (17, 44))
        self.add_line('sym-e2', (24, 44), (31, 44))
        self.add_line('sym-e3', (24, 22), (25, 22))
        self.add_arc('sym-e4', (25, 22), (28, 19), radius_x=6, sweep=False)
        self.add_line('sym-e5', (28, 19), (40, 4))
        self.add_line('sym-e6', (40, 4), (24, 4))
        self.add_line('sym-e7', (24, 4), (8, 4))
        self.add_line('sym-e8', (8, 4), (20, 19))
        self.add_arc('sym-e9', (20, 19), (23, 22), radius_x=6, sweep=False)
        self.add_line('sym-e10', (23, 22), (24, 22))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
