"""Card game card spade (entertainment), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2cf64d69-34f9-465c-a798-c36aec350d36'
SOURCE_PATH = 'icons-json/entertainment/card game card spade_2cf64d69-34f9-465c-a798-c36aec350d36.json'
AUTHOR = 'json_to_solo'

class CardGameCardSpade(Solo48):
    icon_id = 'card-game-card-spade'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('card', 'game', 'spade', 'entertainment')

    def build(self):
        self.add_line('sym-e0', (24, 31), (24, 44))
        self.add_line('sym-e1', (24, 4), (14, 15))
        self.add_arc('sym-e2', (14, 15), (8, 26), radius_x=18, sweep=False)
        self.add_line('sym-e4', (8, 26), (8, 27))
        self.add_line('sym-e5', (8, 27), (9, 31))
        self.add_arc('sym-e6', (9, 31), (19, 34), radius_x=9, sweep=False)
        self.add_line('sym-e7', (19, 34), (24, 31))
        self.add_line('sym-e8', (24, 31), (29, 34))
        self.add_arc('sym-e9', (29, 34), (39, 31), radius_x=9, sweep=False)
        self.add_line('sym-e10', (39, 31), (40, 27))
        self.add_arc('sym-e11', (40, 27), (40, 26), radius_x=28)
        self.add_arc('sym-e13', (40, 26), (34, 15), radius_x=18, sweep=False)
        self.add_line('sym-e14', (34, 15), (24, 4))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
