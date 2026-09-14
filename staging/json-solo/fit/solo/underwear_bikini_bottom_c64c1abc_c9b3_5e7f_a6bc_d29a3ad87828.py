"""Underwear bikini bottom (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c64c1abc-c9b3-5e7f-a6bc-d29a3ad87828'
SOURCE_PATH = 'icons-json/clothes/underwear bikini bottom_c64c1abc-c9b3-5e7f-a6bc-d29a3ad87828.json'
AUTHOR = 'json_to_solo'

class UnderwearBikiniBottomClothes(Solo48):
    icon_id = 'underwear-bikini-bottom-clothes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('underwear', 'bikini', 'bottom', 'clothes')

    def build(self):
        self.add_line('sym-e0', (24, 40), (28, 40))
        self.add_arc('sym-e1', (28, 40), (29, 32), radius_x=45)
        self.add_arc('sym-e2', (29, 32), (37, 19), radius_x=21)
        self.add_line('sym-e3', (37, 19), (44, 17))
        self.add_line('sym-e4', (44, 17), (43, 8))
        self.add_line('sym-e5', (43, 8), (24, 8))
        self.add_line('sym-e6', (24, 8), (5, 8))
        self.add_line('sym-e7', (5, 8), (4, 17))
        self.add_line('sym-e8', (4, 17), (11, 19))
        self.add_arc('sym-e9', (11, 19), (19, 32), radius_x=22)
        self.add_arc('sym-e10', (19, 32), (20, 40), radius_x=45)
        self.add_line('sym-e11', (20, 40), (24, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
