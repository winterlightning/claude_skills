"""Card (business), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '006f0542-de8b-4cfd-9623-f45ac4159bfd'
SOURCE_PATH = 'icons-json/business/card_006f0542-de8b-4cfd-9623-f45ac4159bfd.json'
AUTHOR = 'json_to_solo'

class Card(Solo48):
    icon_id = 'card'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('card', 'business')

    def build(self):
        self.add_line('e0', (4, 15), (4, 36))
        self.add_line('e1', (7, 40), (41, 40))
        self.add_line('e2', (44, 36), (44, 19))
        self.add_line('e3', (44, 19), (44, 12))
        self.add_line('e4', (41, 8), (7, 8))
        self.add_line('e5', (4, 12), (4, 20))
        self.add_line('e6', (12, 29), (17, 29))
        self.add_arc('e7', (4, 36), (7, 40), radius_x=5, sweep=False)
        self.add_arc('e8-1', (41, 40), (43, 39), radius_x=3, sweep=False)
        self.add_arc('e8-2', (43, 39), (44, 36), radius_x=5, sweep=False)
        self.add_arc('e9', (44, 12), (41, 8), radius_x=5, sweep=False)
        self.add_arc('e10-1', (7, 8), (5, 9), radius_x=3, sweep=False)
        self.add_line('e10-2', (5, 9), (4, 12))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8-1', 'e8-2', 'e2', 'e3', 'e9', 'e4', 'e10-1', 'e10-2', 'e5')
        self.add_contour('c1', 'e6')
