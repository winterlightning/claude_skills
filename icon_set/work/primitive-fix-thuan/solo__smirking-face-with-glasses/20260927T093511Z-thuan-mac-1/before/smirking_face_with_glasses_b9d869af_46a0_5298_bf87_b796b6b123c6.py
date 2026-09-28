"""Smirking Face with Glasses; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9d869af-46a0-5298-bf87-b796b6b123c6'
SOURCE_PATH = 'pictographic-primitives/smileys/smirk glasses_b9d869af-46a0-5298-bf87-b796b6b123c6.svg'
AUTHOR = 'gpt-6'


class SmirkingFaceWithGlasses(Solo48):
    icon_id = 'smirking-face-with-glasses'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('smirk', 'glasses', 'cool', 'smiling', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: interrupted temples allow broad flat-topped rounded lenses.
        self.add_arc("crown",(12,8),(36,8),radius_x=20)
        self.add_arc("chin",(40,36),(8,36),radius_x=20)
        for side,sign in (("left",1),("right",-1)):
            def p(x,y):return (24+sign*(x-24),y)
            self.add_line(f"lens-{side}-top",p(9,17),p(19,17))
            self.add_line(f"lens-{side}-right",p(19,17),p(19,21))
            self.add_arc(f"lens-{side}-bottom",p(19,21),p(9,21),radius_x=5,radius_y=4,sweep=sign>0)
            self.add_line(f"lens-{side}-left",p(9,21),p(9,17))
            self.add_contour(f"lens-{side}",*(f"lens-{side}-{x}" for x in ('top','right','bottom','left')),closed=True)
        self.add_line("bridge",(19,17),(29,17))
        for m in ("lens-left-top","lens-left-right","lens-right-top","lens-right-right"):
            self.relate("connect","bridge",m)
        self.add_arc("smirk",(20,34),(28,33),radius_x=8,sweep=False)
