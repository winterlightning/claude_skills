"""Card (business), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b42901ee-f812-48ee-a415-b6ce160f17ba'
SOURCE_PATH = 'icons-json/business/card_b42901ee-f812-48ee-a415-b6ce160f17ba.json'
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
        self.add_line('e0', (31, 29), (36, 29))
        self.add_line('e1', (4, 15), (4, 34))
        self.add_line('e2', (8, 40), (39, 40))
        self.add_line('e3', (44, 35), (44, 19))
        self.add_line('e4', (44, 19), (44, 13))
        self.add_line('e5', (39, 8), (8, 8))
        self.add_line('e6', (4, 13), (4, 20))
        self.add_arc('e7-1', (4, 34), (5, 38), radius_x=9, sweep=False)
        self.add_line('e7-2', (5, 38), (7, 40))
        self.add_line('e7-3', (7, 40), (8, 40))
        self.add_arc('e8', (39, 40), (44, 35), radius_x=5, sweep=False)
        self.add_line('e9-1', (44, 13), (43, 9))
        self.add_line('e9-2', (43, 9), (40, 8))
        self.add_line('e9-3', (40, 8), (39, 8))
        self.add_arc('e10-1', (8, 8), (4, 12), radius_x=4, sweep=False)
        self.add_line('e10-2', (4, 12), (4, 13))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e2', 'e8', 'e3', 'e4', 'e9-1', 'e9-2', 'e9-3', 'e5', 'e10-1', 'e10-2', 'e6')
