"""Champagne glass (drinks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2cc81fd5-4c06-5fc7-8ad6-30aee42e1323'
SOURCE_PATH = 'icons-json/drinks/champagne glass_2cc81fd5-4c06-5fc7-8ad6-30aee42e1323.json'
AUTHOR = 'json_to_solo'

class ChampagneGlass(Solo48):
    icon_id = 'champagne-glass'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('champagne', 'glass', 'drinks')

    def build(self):
        self.add_line('e0', (12, 4), (8, 19))
        self.add_line('e1', (16, 27), (24, 30))
        self.add_line('e2', (24, 30), (32, 28))
        self.add_line('e3', (40, 18), (36, 4))
        self.add_line('e4', (36, 4), (12, 4))
        self.add_line('e5', (24, 30), (24, 44))
        self.add_line('e6', (10, 44), (38, 44))
        self.add_line('e7-1', (8, 19), (9, 23))
        self.add_line('e7-2', (9, 23), (16, 27))
        self.add_arc('e8-1', (32, 28), (40, 20), radius_x=9, sweep=False)
        self.add_line('e8-2', (40, 20), (40, 18))
        self.add_contour('c0', 'e0', 'e7-1', 'e7-2', 'e1', 'e2', 'e8-1', 'e8-2', 'e3', 'e4', closed=True)
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
