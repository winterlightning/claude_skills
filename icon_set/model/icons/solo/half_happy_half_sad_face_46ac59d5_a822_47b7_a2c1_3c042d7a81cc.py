"""Half-Happy Half-Sad Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46ac59d5-a822-47b7-a2c1-3c042d7a81cc'
SOURCE_PATH = 'pictographic-primitives/smileys/mood moody_46ac59d5-a822-47b7-a2c1-3c042d7a81cc.svg'
AUTHOR = 'gpt-6'


class HalfHappyHalfSadFace(Solo48):
    icon_id = 'half-happy-half-sad-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('mood', 'happy', 'sad', 'tear', 'face', 'emoji')

    def build(self) -> None:

        # Circular head split by its shared axis and the mood-changing mouth.
        self.add_arc("head-left",(24,44),(24,4),radius_x=20)
        self.add_arc("head-right",(24,4),(24,44),radius_x=20)
        self.add_contour("head","head-left","head-right",closed=True)
        self.add_line("divider-top",(24,4),(24,30))
        self.add_line("divider-bottom",(24,30),(24,44))
        self.add_contour("divider","divider-top","divider-bottom")
        for h in ("head-left","head-right"):
            self.relate("connect",h,"divider-top")
            self.relate("connect",h,"divider-bottom")
        self.add_line("eye-left",(14,18),(16,18))
        self.add_line("eye-right",(32,18),(34,18))
        self.add_arc("smile-half",(15,27),(24,30),radius_x=10,sweep=False)
        self.add_arc("frown-half",(24,30),(32,32),radius_x=10)
        self.add_contour("mouth","smile-half","frown-half")
        for m in ("smile-half","frown-half"):
            for d in ("divider-top","divider-bottom"):self.relate("connect",m,d)
