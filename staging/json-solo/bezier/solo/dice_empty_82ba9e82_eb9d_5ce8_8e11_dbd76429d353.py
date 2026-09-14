"""Dice empty (video-games), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82ba9e82-eb9d-5ce8-8e11-dbd76429d353'
SOURCE_PATH = 'icons-json/video-games/dice empty_82ba9e82-eb9d-5ce8-8e11-dbd76429d353.json'
AUTHOR = 'json_to_solo'

class DiceEmptyVideoGames(Solo48):
    icon_id = 'dice-empty-video-games'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('dice', 'empty', 'video-games')

    def build(self):
        self.add_bezier('sym-e0', (8, 8), ((9.039, 6.944), (9.761, 6), (11, 6)))
        self.add_bezier('sym-e1', (11, 6), ((11.098, 6), (11.902, 6.008), (12, 6)))
        self.add_line('sym-e2', (12, 6), (36, 6))
        self.add_bezier('sym-e3', (36, 6), ((36.065, 6), (35.935, 6), (36, 6)))
        self.add_bezier('sym-e4', (36, 6), ((38.7, 6), (42, 9.349), (42, 12)))
        self.add_line('sym-e5', (42, 12), (42, 35))
        self.add_bezier('sym-e6', (42, 35), ((42, 35.196), (42, 35.804), (42, 36)))
        self.add_bezier('sym-e7', (42, 36), ((42, 37.492), (41.079, 38.864), (40, 40)))
        self.add_bezier('sym-e8', (40, 40), ((38.864, 41.079), (37.492, 42), (36, 42)))
        self.add_bezier('sym-e9', (36, 42), ((35.804, 42), (35.196, 42), (35, 42)))
        self.add_line('sym-e10', (35, 42), (12, 42))
        self.add_bezier('sym-e11', (12, 42), ((9.349, 42), (6, 38.7), (6, 36)))
        self.add_bezier('sym-e12', (6, 36), ((6, 35.935), (6, 36.065), (6, 36)))
        self.add_line('sym-e13', (6, 36), (6, 12))
        self.add_bezier('sym-e14', (6, 12), ((6.008, 11.902), (6, 11.098), (6, 11)))
        self.add_bezier('sym-e15', (6, 11), ((6, 9.761), (6.944, 9.039), (8, 8)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
