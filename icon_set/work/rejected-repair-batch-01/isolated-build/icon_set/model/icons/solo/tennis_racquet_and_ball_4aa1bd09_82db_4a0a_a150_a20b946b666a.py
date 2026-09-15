'A tennis racquet beside a ball.\nConstruction: Square centerlines (6,6)-(42,42) accommodate a diagonal grip and circular racquet head. Two crossing strings retain the sporting identity; omit dense string mesh and grip bands. The ball, where supplied, remains detached. Diagonal asymmetry follows the source.\nLucide: dumbbell: a single shaft connects the main mass.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4aa1bd09-82db-4a0a-a150-a20b946b666a'
SOURCE_PATH = 'pictographic-primitives/sports/tennis_4aa1bd09-82db-4a0a-a150-a20b946b666a.svg'
AUTHOR = 'gpt-6'

class TennisRacquetAndBall(Solo48):
    icon_id = 'tennis-racquet-and-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('tennis', 'racquet', 'and', 'ball', 'sport')

    def build(self):
        self.add_arc('rim-0', (26, 24), (24, 10), radius_x=10)
        self.add_arc('rim-1', (24, 10), (38, 8), radius_x=10)
        self.add_arc('rim-2', (38, 8), (40, 22), radius_x=10)
        self.add_arc('rim-3', (40, 22), (26, 24), radius_x=10)
        self.add_contour('rim', 'rim-0', 'rim-1', 'rim-2', 'rim-3', closed=True)
        self.add_polyline('string-long', (26,24), (32,16), (38,8))
        self.add_polyline('string-cross', (24,10), (32,16), (40,22))
        self.relate('connect', 'rim', 'string-long')
        self.relate('connect', 'rim', 'string-cross')
        self.relate('connect', 'string-long', 'string-cross')
        self.relate('connect', 'string-long', 'handle')
        self.add_line('handle', (26, 24), (6, 42))
        self.relate("connect", 'rim', 'handle')
        self.add_arc('ball-top', (6, 9), (12, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('ball-bottom', (12, 9), (6, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('ball', 'ball-top', 'ball-bottom', closed=True)
