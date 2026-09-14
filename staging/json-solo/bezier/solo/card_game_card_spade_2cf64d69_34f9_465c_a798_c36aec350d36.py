"""Card game card spade (entertainment), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2cf64d69-34f9-465c-a798-c36aec350d36'
SOURCE_PATH = 'icons-json/entertainment/card game card spade_2cf64d69-34f9-465c-a798-c36aec350d36.json'
AUTHOR = 'json_to_solo'

class CardGameCardSpadeEntertainment(Solo48):
    icon_id = 'card-game-card-spade-entertainment'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('card', 'game', 'spade', 'entertainment')

    def build(self):
        self.add_line('sym-e0', (24, 31), (24, 44))
        self.add_line('sym-e1', (24, 4), (14, 15))
        self.add_bezier('sym-e2', (14, 15), ((11.524, 17.673), (8, 22), (8, 26)))
        self.add_bezier('sym-e3', (8, 26), ((8, 26.218), (8, 25.782), (8, 26)))
        self.add_bezier('sym-e4', (8, 26), ((8, 26.136), (8, 26.864), (8, 27)))
        self.add_bezier('sym-e5', (8, 27), ((8, 28.318), (8.309, 29.945), (9, 31)))
        self.add_bezier('sym-e6', (9, 31), ((11.274, 34.464), (15.371, 35.236), (19, 34)))
        self.add_bezier('sym-e7', (19, 34), ((20.011, 33.655), (23.688, 31), (24, 31)))
        self.add_bezier('sym-e8', (24, 31), ((24.312, 31), (27.989, 33.655), (29, 34)))
        self.add_bezier('sym-e9', (29, 34), ((32.629, 35.236), (36.726, 34.464), (39, 31)))
        self.add_bezier('sym-e10', (39, 31), ((39.691, 29.945), (40, 28.318), (40, 27)))
        self.add_bezier('sym-e11', (40, 27), ((40, 26.864), (40, 26.136), (40, 26)))
        self.add_bezier('sym-e12', (40, 26), ((40, 25.782), (40, 26.218), (40, 26)))
        self.add_bezier('sym-e13', (40, 26), ((40, 22), (36.476, 17.673), (34, 15)))
        self.add_line('sym-e14', (34, 15), (24, 4))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
