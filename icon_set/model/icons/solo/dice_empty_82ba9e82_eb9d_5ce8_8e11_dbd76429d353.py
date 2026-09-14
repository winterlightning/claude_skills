"""Dice empty (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82ba9e82-eb9d-5ce8-8e11-dbd76429d353'
SOURCE_PATH = 'icons-json/video-games/dice empty_82ba9e82-eb9d-5ce8-8e11-dbd76429d353.json'
AUTHOR = 'json_to_solo'

class DiceEmpty(Solo48):
    icon_id = 'dice-empty'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('dice', 'empty', 'video-games')

    def build(self):
        self.add_arc('sym-e0', (8, 8), (11, 6), radius_x=5)
        self.add_line('sym-e1', (11, 6), (12, 6))
        self.add_line('sym-e2', (12, 6), (36, 6))
        self.add_arc('sym-e4', (36, 6), (42, 12), radius_x=6)
        self.add_line('sym-e5', (42, 12), (42, 35))
        self.add_line('sym-e6', (42, 35), (42, 36))
        self.add_arc('sym-e7', (42, 36), (40, 40), radius_x=6)
        self.add_arc('sym-e8', (40, 40), (36, 42), radius_x=6)
        self.add_line('sym-e9', (36, 42), (35, 42))
        self.add_line('sym-e10', (35, 42), (12, 42))
        self.add_arc('sym-e11', (12, 42), (6, 36), radius_x=6)
        self.add_line('sym-e13', (6, 36), (6, 12))
        self.add_line('sym-e14', (6, 12), (6, 11))
        self.add_arc('sym-e15', (6, 11), (8, 8), radius_x=5)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
