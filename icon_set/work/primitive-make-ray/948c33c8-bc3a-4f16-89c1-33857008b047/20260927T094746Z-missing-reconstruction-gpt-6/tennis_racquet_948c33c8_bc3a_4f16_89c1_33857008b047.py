'A tennis racquet with a diagonal handle.\nConstruction: Square centerlines (6,6)-(42,42) accommodate a diagonal grip and circular racquet head. Two crossing strings retain the sporting identity; omit dense string mesh and grip bands. The ball, where supplied, remains detached. Diagonal asymmetry follows the source.\nLucide: dumbbell: a single shaft connects the main mass.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '948c33c8-bc3a-4f16-89c1-33857008b047'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tennis-racquet/20260927T094425Z-thuan-mac-1/reference/tennis racquet_948c33c8-bc3a-4f16-89c1-33857008b047.svg'
AUTHOR = 'gpt-6'
REVISION_COMPARISON = 'The rejected crossed strings dominated the source’s empty oval racket head.'
REVISION_CHANGE = 'Removed the X to restore the open racket head and diagonal grip.'


class TennisRacquet(Solo48):
    icon_id = 'tennis-racquet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('tennis', 'racquet', 'sport')

    def build(self):
        self.add_arc('rim-0', (26, 24), (24, 10), radius_x=10)
        self.add_arc('rim-1', (24, 10), (38, 8), radius_x=10)
        self.add_arc('rim-2', (38, 8), (40, 22), radius_x=10)
        self.add_arc('rim-3', (40, 22), (26, 24), radius_x=10)
        self.add_contour('rim', 'rim-0', 'rim-1', 'rim-2', 'rim-3', closed=True)
        self.add_line('handle', (26, 24), (6, 42))
        self.relate("connect", 'rim', 'handle')
