'sad-face-c6baabbe: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6baabbe-f1f2-4a94-95e5-bb3ef9618a5b'
SOURCE_PATH = 'pictographic-primitives/smileys/sad face_c6baabbe-f1f2-4a94-95e5-bb3ef9618a5b.svg'
AUTHOR = 'gpt-6'

class SadFaceC6baabbe(Solo48):
    icon_id = 'sad-face-c6baabbe'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('sad', 'face', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_line('eye-left',(18,16),(18,19))
        self.add_line('eye-right',(30,16),(30,19))
        self.add_arc('mouth',(17,32),(31,32),radius_x=7,radius_y=4)
