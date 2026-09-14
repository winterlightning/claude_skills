"""Pet head (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '649e9664-56e4-4a51-b43a-634e638038e7'
SOURCE_PATH = 'icons-json/symbol/pet head_649e9664-56e4-4a51-b43a-634e638038e7.json'
AUTHOR = 'json_to_solo'

class PetHeadSymbol(Solo48):
    icon_id = 'pet-head-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pet', 'head', 'symbol')

    def build(self):
        self.add_line('e0', (30, 13), (32, 11))
        self.add_arc('e1-1', (32, 11), (38, 8), radius_x=8)
        self.add_arc('e1-2', (38, 8), (44, 14), radius_x=6)
        self.add_arc('e1-3', (44, 14), (39, 20), radius_x=7)
        self.add_arc('e1-4', (39, 20), (37, 34), radius_x=13)
        self.add_arc('e1-5', (37, 34), (32, 38), radius_x=17)
        self.add_arc('e1-6', (32, 38), (24, 40), radius_x=17)
        self.add_line('e1-7', (24, 40), (18, 39))
        self.add_arc('e1-8', (18, 39), (13, 36), radius_x=17)
        self.add_arc('e1-9', (13, 36), (9, 20), radius_x=14)
        self.add_arc('e1-10', (9, 20), (4, 14), radius_x=7)
        self.add_arc('e1-11', (4, 14), (10, 8), radius_x=6)
        self.add_arc('e1-12', (10, 8), (18, 13), radius_x=10)
        self.add_arc('e1-13', (18, 13), (30, 13), radius_x=20)
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11', 'e1-12', 'e1-13', closed=True)
