'tired-face: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8112462-62f6-570b-bc97-3c13f730433f'
SOURCE_PATH = 'pictographic-primitives/smileys/tired face_a8112462-62f6-570b-bc97-3c13f730433f.svg'
AUTHOR = 'gpt-6'

class TiredFace(Solo48):
    icon_id = 'tired-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('tired', 'face', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_arc('eye-left',(15,17),(19,17),radius_x=2,radius_y=2,sweep=False)
        self.add_arc('eye-right',(29,17),(33,17),radius_x=2,radius_y=2,sweep=False)
        self.add_arc('mouth',(17,32),(31,32),radius_x=7,radius_y=4)
