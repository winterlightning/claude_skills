"""Hypnotized Face; rebuilt from the supplied visual reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e67e67e8-fb33-47eb-a330-05cfafa37994'
SOURCE_PATH = 'pictographic-primitives/smileys/hypnotized_e67e67e8-fb33-47eb-a330-05cfafa37994.svg'
AUTHOR = 'gpt-6'


class HypnotizedFace(Solo48):
    icon_id = 'hypnotized-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('hypnotized', 'spiral', 'dizzy', 'trance', 'face', 'emoji')

    def build(self) -> None:

        # Paired single-turn eye curls above a round lower face.
        self.add_arc("crown",(12,8),(36,8),radius_x=20)
        self.add_arc("chin",(40,36),(8,36),radius_x=20)
        for side,sign in (("left",1),("right",-1)):
            def p(x,y): return (24+sign*(x-24),y)
            self.add_arc(f"coil-{side}-top",p(7,22),p(19,22),radius_x=6,sweep=sign>0)
            self.add_arc(f"coil-{side}-bottom",p(19,22),p(13,28),radius_x=6,sweep=sign>0)
            self.add_arc(f"coil-{side}-curl",p(13,28),p(10,25),radius_x=3,sweep=sign>0)
            self.add_contour(f"coil-{side}",f"coil-{side}-top",f"coil-{side}-bottom",f"coil-{side}-curl")
        self.add_line("mouth",(20,35),(28,35))
