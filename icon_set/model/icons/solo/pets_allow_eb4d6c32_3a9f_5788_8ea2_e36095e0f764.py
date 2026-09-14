"""Pets allow (wayfinding), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb4d6c32-3a9f-5788-8ea2-e36095e0f764'
SOURCE_PATH = 'icons-json/wayfinding/pets allow_eb4d6c32-3a9f-5788-8ea2-e36095e0f764.json'
AUTHOR = 'json_to_solo'

class PetsAllow(Solo48):
    icon_id = 'pets-allow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('pets', 'allow', 'wayfinding')

    def build(self):
        self.add_line('e0', (26, 12), (24, 21))
        self.add_line('e1', (22, 22), (10, 22))
        self.add_line('e2', (5, 22), (7, 24))
        self.add_line('e3', (7, 24), (7, 40))
        self.add_line('e4', (7, 40), (11, 40))
        self.add_line('e5', (11, 40), (14, 32))
        self.add_line('e6', (14, 32), (28, 32))
        self.add_line('e7', (28, 32), (30, 40))
        self.add_line('e8', (30, 40), (35, 40))
        self.add_line('e9', (35, 40), (35, 22))
        self.add_line('e10', (35, 22), (39, 22))
        self.add_line('e11', (44, 16), (32, 12))
        self.add_line('e12', (32, 12), (32, 8))
        self.add_arc('e13', (32, 8), (26, 12), radius_x=7, sweep=False)
        self.add_arc('e14', (24, 21), (22, 22), radius_x=2)
        self.add_arc('e15-1', (10, 22), (4, 18), radius_x=12)
        self.add_arc('e15-2', (4, 18), (5, 22), radius_x=9, sweep=False)
        self.add_arc('e16-1', (39, 22), (43, 20), radius_x=4, sweep=False)
        self.add_line('e16-2', (43, 20), (44, 16))
        self.add_contour('c0', 'e13', 'e0', 'e14', 'e1', 'e15-1', 'e15-2', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e16-1', 'e16-2', 'e11', 'e12', closed=True)
