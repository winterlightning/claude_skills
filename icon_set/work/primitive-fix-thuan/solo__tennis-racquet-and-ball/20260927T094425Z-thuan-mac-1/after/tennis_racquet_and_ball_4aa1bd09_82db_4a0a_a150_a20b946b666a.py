'A tennis racquet beside a ball.\nConstruction: Square centerlines (6,6)-(42,42) accommodate a diagonal grip and circular racquet head. Two crossing strings retain the sporting identity; omit dense string mesh and grip bands. The ball, where supplied, remains detached. Diagonal asymmetry follows the source.\nLucide: dumbbell: a single shaft connects the main mass.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4aa1bd09-82db-4a0a-a150-a20b946b666a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tennis-racquet-and-ball/20260927T094425Z-thuan-mac-1/reference/tennis_4aa1bd09-82db-4a0a-a150-a20b946b666a.svg'
AUTHOR = 'gpt-6'
REVISION_COMPARISON = 'The rejected crossed strings dominated the plain oval head in the source.'
REVISION_CHANGE = 'Removed the X so the oval racket head and detached ball read clearly.'


class TennisRacquetAndBall(Solo48):
    icon_id = 'tennis-racquet-and-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('tennis', 'racquet', 'and', 'ball', 'sport')

    def build(self):
        self.add_arc('rim-0', (26, 24), (24, 10), radius_x=10)
        self.add_arc('rim-1', (24, 10), (38, 8), radius_x=10)
        self.add_arc('rim-2', (38, 8), (40, 22), radius_x=10)
        self.add_arc('rim-3', (40, 22), (26, 24), radius_x=10)
        self.add_contour('rim', 'rim-0', 'rim-1', 'rim-2', 'rim-3', closed=True)
        self.add_line('handle', (26, 24), (6, 42))
        self.relate("connect", 'rim', 'handle')
        self.add_arc('ball-top', (6, 9), (12, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('ball-bottom', (12, 9), (6, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('ball', 'ball-top', 'ball-bottom', closed=True)
