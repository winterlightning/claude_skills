'very-happy: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '882fdc6f-fb69-486c-9abe-a9e651b9caf0'
SOURCE_PATH = 'icons-json/smileys/very happy_882fdc6f-fb69-486c-9abe-a9e651b9caf0.json'
AUTHOR = 'gpt-6'

class VeryHappy(Solo48):
    icon_id = 'very-happy'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('very', 'happy', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_arc('eye-left',(15,18),(19,18),radius_x=2,radius_y=2)
        self.add_arc('eye-right',(29,18),(33,18),radius_x=2,radius_y=2)
        self.add_line('mouth-top',(17,27),(31,27))
        self.add_arc('mouth-bottom',(31,27),(17,27),radius_x=7,radius_y=7)
        self.add_contour('mouth','mouth-top','mouth-bottom',closed=True)
