'Koala head: mirrored round ears and a compact oval nose with clear face margins.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f02ee94d-07a6-5d6f-baf8-a6cbb0cb8ed2'
SOURCE_PATH = 'pictographic-primitives/animals/koala head_f02ee94d-07a6-5d6f-baf8-a6cbb0cb8ed2.svg'
AUTHOR = 'gpt-6'


class KoalaFace(Solo48):
    icon_id = 'koala-face'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('koala', 'face', 'head', 'ears', 'nose', 'marsupial', 'australia', 'cute')

    def build(self) -> None:
        # Reflected ear lobes and a broad central face preserve koala proportions.
        self.add_bezier('left-ear',(16,14),((16,10),(14,8),(10,8)),((6,8),(4,11),(4,16)),((4,21),(6,24),(10,24)))
        self.add_bezier('chin',(10,24),((10,34),(15,40),(24,40)),((33,40),(38,34),(38,24)))
        self.add_bezier('right-ear',(38,24),((42,24),(44,21),(44,16)),((44,11),(42,8),(38,8)),((34,8),(32,10),(32,14)))
        self.add_bezier('crown',(32,14),((28,11),(20,11),(16,14)))
        self.add_contour('face','left-ear','chin','right-ear','crown',closed=True)

        self.add_arc('nose-top', (21,27), (27,27), radius_x=3, radius_y=4)
        self.add_arc('nose-bottom', (27,27), (21,27), radius_x=3, radius_y=4)
        self.add_contour('nose', 'nose-top', 'nose-bottom', closed=True)
