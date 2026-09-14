'disapointed: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '489efe49-b13d-5ebf-b178-cd270ffd39f2'
SOURCE_PATH = 'icons-json/smileys/disapointed_489efe49-b13d-5ebf-b178-cd270ffd39f2.json'
AUTHOR = 'gpt-6'

class Disapointed(Solo48):
    icon_id = 'disapointed'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('disapointed', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_arc('eye-left',(15,18),(19,16),radius_x=6,sweep=False)
        self.add_arc('eye-right',(29,16),(33,18),radius_x=6,sweep=False)
        self.add_arc('mouth',(17,32),(31,32),radius_x=7,radius_y=4)
