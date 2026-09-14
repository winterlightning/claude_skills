'blessed: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4669a42f-119e-5431-9305-4e31305f43c1'
SOURCE_PATH = 'icons-json/smileys/blessed_4669a42f-119e-5431-9305-4e31305f43c1.json'
AUTHOR = 'gpt-6'

class Blessed(Solo48):
    icon_id = 'blessed'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('blessed', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_arc('eye-left',(15,18),(19,18),radius_x=2,radius_y=2)
        self.add_arc('eye-right',(29,18),(33,18),radius_x=2,radius_y=2)
        self.add_arc('mouth',(17,28),(31,28),radius_x=7,radius_y=5,sweep=False)
