"""Card (business), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc09bb7b-da25-41fc-9ec5-f3b12e7a09cd'
SOURCE_PATH = 'icons-json/business/card_fc09bb7b-da25-41fc-9ec5-f3b12e7a09cd.json'
AUTHOR = 'json_to_solo'

class CardFc09bb7b(Solo48):
    icon_id = 'card-fc09bb7b'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('card', 'business')

    def build(self):
        self.add_line('sym-e0', (4, 18), (44, 18))
        self.add_line('sym-e1', (44, 18), (44, 36))
        self.add_arc('sym-e2-1', (44, 36), (43, 39), radius_x=5)
        self.add_arc('sym-e2-2', (43, 39), (41, 40), radius_x=3)
        self.add_line('sym-e3', (41, 40), (24, 40))
        self.add_line('sym-e4', (24, 40), (7, 40))
        self.add_arc('sym-e5-1', (7, 40), (5, 39), radius_x=3)
        self.add_arc('sym-e5-2', (5, 39), (4, 36), radius_x=5)
        self.add_line('sym-e6', (4, 36), (4, 18))
        self.add_line('sym-e7', (4, 18), (4, 12))
        self.add_arc('sym-e8-1', (4, 12), (5, 9), radius_x=5)
        self.add_arc('sym-e8-2', (5, 9), (7, 8), radius_x=3)
        self.add_line('sym-e9', (7, 8), (24, 8))
        self.add_line('sym-e10', (24, 8), (41, 8))
        self.add_arc('sym-e11-1', (41, 8), (43, 9), radius_x=3)
        self.add_arc('sym-e11-2', (43, 9), (44, 12), radius_x=5)
        self.add_arc('sym-e12-1', (44, 12), (44, 15), radius_x=25, sweep=False)
        self.add_line('sym-e12-2', (44, 15), (44, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2-1', 'sym-e2-2', 'sym-e3', 'sym-e4', 'sym-e5-1', 'sym-e5-2', 'sym-e6', 'sym-e7', 'sym-e8-1', 'sym-e8-2', 'sym-e9', 'sym-e10', 'sym-e11-1', 'sym-e11-2', 'sym-e12-1', 'sym-e12-2')
