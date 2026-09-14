"""Condom (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56cbe40d-c073-46c1-98ab-44e9f8ae8fb5'
SOURCE_PATH = 'icons-json/money/condom_56cbe40d-c073-46c1-98ab-44e9f8ae8fb5.json'
AUTHOR = 'json_to_solo'

class Condom(Solo48):
    icon_id = 'condom'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('condom', 'money')

    def build(self):
        self.add_line('sym-e0', (40, 44), (36, 40))
        self.add_line('sym-e1', (36, 40), (32, 44))
        self.add_line('sym-e2', (32, 44), (28, 40))
        self.add_line('sym-e3', (28, 40), (24, 44))
        self.add_line('sym-e4', (24, 44), (20, 40))
        self.add_line('sym-e5', (20, 40), (16, 44))
        self.add_line('sym-e6', (16, 44), (12, 40))
        self.add_line('sym-e7', (12, 40), (8, 44))
        self.add_line('sym-e8', (8, 44), (8, 4))
        self.add_line('sym-e9', (8, 4), (12, 8))
        self.add_line('sym-e10', (12, 8), (16, 4))
        self.add_line('sym-e11', (16, 4), (20, 8))
        self.add_line('sym-e12', (20, 8), (24, 4))
        self.add_line('sym-e13', (24, 4), (28, 8))
        self.add_line('sym-e14', (28, 8), (32, 4))
        self.add_line('sym-e15', (32, 4), (36, 8))
        self.add_line('sym-e16', (36, 8), (40, 4))
        self.add_line('sym-e17', (40, 4), (40, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
