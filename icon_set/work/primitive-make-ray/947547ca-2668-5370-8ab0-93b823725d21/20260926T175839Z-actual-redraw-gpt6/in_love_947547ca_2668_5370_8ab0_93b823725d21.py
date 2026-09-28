"""Heart-Eyes Face; rebuilt from the supplied visual reference on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '947547ca-2668-5370-8ab0-93b823725d21'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__heart-eyes-face/20260926T172218Z-thuan-mac-1/reference/in love_947547ca-2668-5370-8ab0-93b823725d21.svg'
AUTHOR = "gpt-6"


class HeartEyesFace(Solo48):
    icon_id = 'heart-eyes-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('love', 'heart', 'smile', 'adoring', 'face', 'emoji')

    def build(self) -> None:
        # The original is a round face with paired heart eyes and a low smile.
        self.add_arc('face-top',(4,24),(44,24),radius_x=20)
        self.add_arc('face-bottom',(44,24),(4,24),radius_x=20)
        self.add_contour('face','face-top','face-bottom',closed=True)
        for side,cx in (('left',17),('right',31)):
            self.add_polyline(f'heart-{side}',(cx-2,18),(cx,24),(cx+2,18))
        self.add_arc('smile',(17,33),(31,33),radius_x=10,sweep=False)
