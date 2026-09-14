'Crouching mouse: retain the large round ear, low body and curled tail; broaden the muzzle for a clear eye.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1fc63f6-12db-5dd9-8649-42850ceca103'
SOURCE_PATH = 'pictographic-primitives/animals/mouse 1_d1fc63f6-12db-5dd9-8649-42850ceca103.svg'
AUTHOR = 'gpt-6'


class CrouchingMouse(Solo48):
    icon_id = 'crouching-mouse'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('crouching', 'mouse')

    def build(self) -> None:
        self.add_arc('ear-top', (25,14), (37,14), radius_x=6, radius_y=6)
        self.add_arc('ear-bottom', (37,14), (25,14), radius_x=6, radius_y=6)
        self.add_contour('ear', 'ear-top', 'ear-bottom', closed=True)

        self.add_polyline('head',(37,14),(37,19),(44,32))
        self.add_bezier('chin',(44,32),((44,36),(41,38),(37,38)))
        self.add_line('belly',(37,38),(14,38))
        self.add_bezier('back',(14,38),((7,38),(6,33),(9,27)),((12,20),(18,16),(25,14)))
        self.relate('connect','ear','head');self.relate('connect','ear','back');self.relate('connect','head','chin');self.relate('connect','chin','belly');self.relate('connect','belly','back')
        self.add_bezier('tail',(9,27),((5,29),(4,32),(4,35)),((4,38),(7,40),(11,40)))
        self.relate('connect','tail','back')
        self.add_dot('eye',(32,28))
