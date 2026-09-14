"""Card (business), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea0b88fe-d35a-445a-9011-2bdc59c40a03'
SOURCE_PATH = 'icons-json/business/card_ea0b88fe-d35a-445a-9011-2bdc59c40a03.json'
AUTHOR = 'json_to_solo'

class CardEa0b88fe(Solo48):
    icon_id = 'card-ea0b88fe'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('card', 'business')

    def build(self):
        self.add_line('e0', (4, 20), (4, 15))
        self.add_line('e1', (4, 20), (4, 36))
        self.add_line('e2', (7, 40), (41, 40))
        self.add_line('e3', (44, 36), (44, 19))
        self.add_line('e4', (44, 19), (44, 12))
        self.add_line('e5', (41, 8), (7, 8))
        self.add_line('e6', (4, 12), (4, 15))
        self.add_line('e7', (31, 29), (36, 29))
        self.add_arc('e8', (4, 36), (7, 40), radius_x=5, sweep=False)
        self.add_arc('e9-1', (41, 40), (43, 39), radius_x=3, sweep=False)
        self.add_arc('e9-2', (43, 39), (44, 36), radius_x=5, sweep=False)
        self.add_arc('e10', (44, 12), (41, 8), radius_x=5, sweep=False)
        self.add_arc('e11-1', (7, 8), (5, 9), radius_x=3, sweep=False)
        self.add_line('e11-2', (5, 9), (4, 12))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e8', 'e2', 'e9-1', 'e9-2', 'e3', 'e4', 'e10', 'e5', 'e11-1', 'e11-2', 'e6')
        self.add_contour('c2', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
