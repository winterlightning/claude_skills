"""Card game card club (entertainment), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '620fba34-559d-44dd-802b-138529d208d8'
SOURCE_PATH = 'icons-json/entertainment/card game card club_620fba34-559d-44dd-802b-138529d208d8.json'
AUTHOR = 'json_to_solo'

class CardGameCardClubEntertainment(Solo48):
    icon_id = 'card-game-card-club-entertainment'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('card', 'game', 'club', 'entertainment')

    def build(self):
        self.add_line('e0', (27, 35), (24, 32))
        self.add_line('e1', (24, 32), (24, 44))
        self.add_arc('e2-1', (24, 32), (13, 36), radius_x=9)
        self.add_arc('e2-2', (13, 36), (8, 28), radius_x=9)
        self.add_arc('e2-3', (8, 28), (17, 19), radius_x=9)
        self.add_arc('e2-4', (17, 19), (19, 6), radius_x=12)
        self.add_arc('e2-5', (19, 6), (24, 4), radius_x=8)
        self.add_arc('e2-6', (24, 4), (31, 9), radius_x=8)
        self.add_arc('e2-7', (31, 9), (31, 19), radius_x=13)
        self.add_arc('e2-8', (31, 19), (40, 27), radius_x=9)
        self.add_line('e2-9', (40, 27), (39, 32))
        self.add_arc('e2-10', (39, 32), (35, 36), radius_x=9)
        self.add_arc('e2-11', (35, 36), (27, 35), radius_x=8)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9', 'e2-10', 'e2-11', 'e0', 'e1')
